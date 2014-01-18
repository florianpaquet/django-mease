import pickle
import tornadoredis.pubsub

from .base import BaseSubscriber


class RedisSubscriber(BaseSubscriber, tornadoredis.pubsub.BaseSubscriber):

    def on_message(self, message):
        """
        Redis pubsub callback
        """
        if message.kind == 'message':
            args, kwargs = pickle.loads(message.body)
            self.dispatch_message(message.channel, args, kwargs)
