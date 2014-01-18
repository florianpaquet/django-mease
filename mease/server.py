# -*- coding: utf-8 -*-
import json
import tornado.gen
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornadoredis
from concurrent.futures import ThreadPoolExecutor

from .settings import REDIS_HOST, REDIS_PORT, REDIS_CHANNELS, MAX_WORKERS
from .registry import registry, autodiscover

autodiscover()

__all__ = ('WebSocketServer',)

EXECUTOR = ThreadPoolExecutor(max_workers=MAX_WORKERS)


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
        # Redis client
        self.redis_client = tornadoredis.Client(host=REDIS_HOST, port=REDIS_PORT)
        self.redis_client.connect()
        self.redis_client.subscribe(REDIS_CHANNELS)
        self.redis_client.listen(self.on_receive)

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

    def on_receive(self, message):
        """
        Redis pubsub callback
        """
        event, channel, message = message

        # Call sender callbacks
        if event.decode() == 'message':
            for func, channels in self.registry.senders:
                if channels is None or channel.decode() in channels:
                    EXECUTOR.submit(func, channel, message, self.application.clients)

    def run(self):
        """
        Starts websocket server
        """
        self.application.listen(self.port)
        self.ioloop.start()
