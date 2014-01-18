import pickle
import tornadoredis.pubsub


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
                    self.application.executor.submit(
                        func, message.channel, self.application.clients, *args, **kwargs)
