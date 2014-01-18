# -*- coding: utf-8 -*-
import json
import logging
import tornado.gen
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornadoredis
from concurrent.futures import ThreadPoolExecutor
from django.utils.module_loading import import_by_path

from .settings import SUBSCRIBER_CLASS_PATH, REDIS_HOST, REDIS_PORT
from .settings import REDIS_CHANNELS, MAX_WORKERS
from .registry import registry, autodiscover

autodiscover()

__all__ = ('WebSocketServer',)
LOGGER = logging.getLogger('mease.websocket_server')


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        # Init storage
        self.storage = {}

        # Call openers callbacks
        for func in self.application.registry.openers:
            self.application.executor.submit(func, self, self.application.clients)

        # Append client to clients list
        if self not in self.application.clients:
            self.application.clients.append(self)

    def on_close(self):
        # Call closer callbacks
        for func in self.application.registry.closers:
            self.application.executor.submit(func, self, self.application.clients)

        # Remove client from clients list
        if self in self.application.clients:
            self.application.clients.remove(self)

    def on_message(self, message):
        # Call receiver callbacks
        for func, to_json in self.application.registry.receivers:

            if to_json:
                try:
                    message = json.loads(message)
                except ValueError:
                    continue

            self.application.executor.submit(
                func, self, message, self.application.clients)


class WebSocketServer(object):

    def __init__(self, debug, port):

        # Tornado loop
        self.ioloop = tornado.ioloop.IOLoop.instance()

        # Tornado application
        self.debug = debug
        self.port = port

        self.application = tornado.web.Application([
            (r'/', WebSocketHandler),
        ], debug=self.debug)

        # Clients list
        self.application.clients = []

        # Registry
        self.application.registry = registry

        # Executor
        self.application.executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

        # Connect to redis
        subscriber_class = import_by_path(SUBSCRIBER_CLASS_PATH)

        LOGGER.info("Connecting to Redis on {host}:{port}".format(
            host=REDIS_HOST, port=REDIS_PORT))

        self.subscriber = subscriber_class(
            tornadoredis.Client(host=REDIS_HOST, port=REDIS_PORT))

        LOGGER.info("Successfully connected to Redis")

        # Subscribe to channels
        self.subscriber.subscribe(REDIS_CHANNELS, self)

        LOGGER.debug("Subscribed to [{channels}] Redis channels".format(
            channels=', '.join(REDIS_CHANNELS)))

        self.subscriber.application = self.application
        self.subscriber.registry = registry

    def run(self):
        """
        Starts websocket server
        """
        self.application.listen(self.port)
        self.ioloop.start()
