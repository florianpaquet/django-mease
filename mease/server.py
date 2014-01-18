# -*- coding: utf-8 -*-
import json
import pickle
import tornado.gen
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornadoredis
import tornadoredis.pubsub
from concurrent.futures import ThreadPoolExecutor

from .settings import REDIS_HOST, REDIS_PORT, REDIS_CHANNELS, MAX_WORKERS
from .registry import registry, autodiscover

autodiscover()

__all__ = ('WebSocketServer',)

EXECUTOR = ThreadPoolExecutor(max_workers=MAX_WORKERS)


class RedisSubscriber(tornadoredis.pubsub.BaseSubscriber):

    def on_message(self, message):
        """
        Redis pubsub callback
        """
        # Call sender callbacks
        if message.kind == 'message':
            args, kwargs = pickle.loads(message.body)

            for func, channels in self.registry.senders:
                if channels is None or message.channel in channels:
                    EXECUTOR.submit(
                        func, message.channel, self.application.clients, *args, **kwargs)


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        # Init storage
        self.storage = {}

        # Call openers callbacks
        for func in self.application.registry.openers:
            EXECUTOR.submit(func, self, self.application.clients)

        # Append client to clients list
        if self not in self.application.clients:
            self.application.clients.append(self)

    def on_close(self):
        # Call closer callbacks
        for func in self.application.registry.closers:
            EXECUTOR.submit(func, self, self.application.clients)

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

            EXECUTOR.submit(func, self, message, self.application.clients)


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

        # Redis subscriber
        self.subscriber = RedisSubscriber(
            tornadoredis.Client(host=REDIS_HOST, port=REDIS_PORT))
        self.subscriber.subscribe(REDIS_CHANNELS, self)

        self.subscriber.application = self.application
        self.subscriber.registry = registry

    def run(self):
        """
        Starts websocket server
        """
        self.application.listen(self.port)
        self.ioloop.start()
