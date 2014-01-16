# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.websocket
from toredis import Client

from .settings import REDIS_HOST, REDIS_PORT, REDIS_CHANNELS
from .registry import registry, autodiscover

autodiscover()

__all__ = ('WebSocketServer',)


class RedisClient(Client):
    def on_disconnect(self):
        self.connect(host=REDIS_HOST, port=REDIS_PORT)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        """
        Appends client to application clients
        """
        if self not in self.application.clients:
            self.application.clients.append(self)

    def on_close(self):
        """
        Removes client from application clients
        """
        if self in self.application.clients:
            self.application.clients.remove(self)

    def on_message(self, message):
        for func in registry.receivers:
            func(self, message, self.application.clients)


class WebSocketServer(object):
    def __init__(self, debug, port):
        # Redis client
        self.redis_client = RedisClient()
        self.redis_client.connect(host=REDIS_HOST, port=REDIS_PORT)
        self.redis_client.subscribe(REDIS_CHANNELS, callback=self.on_receive)

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

    def on_receive(self, message):
        """
        Redis pubsub callback
        """
        event, channel, message = message

        if event.decode() == 'message':
            for func, channels in registry.senders:
                if channels is None or channel.decode() in channels:
                    func(self.application.clients, channel, message)

    def run(self):
        """
        Starts websocket server
        """
        self.application.listen(self.port)
        self.ioloop.start()
