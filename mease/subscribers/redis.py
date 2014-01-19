# -*- coding: utf-8 -*-
import pickle

from .base import BaseSubscriber


class RedisSubscriber(BaseSubscriber):

    def on_message(self, message):
        """
        Redis pubsub callback
        """
        event, channel, data = message

        if event.decode() == 'message':
            args, kwargs = pickle.loads(data)
            self.dispatch_message(channel.decode(), args, kwargs)
