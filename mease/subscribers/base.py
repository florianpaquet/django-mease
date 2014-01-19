# -*- coding: utf-8 -*-


class BaseSubscriber(object):
    """
    Base subscriber that dispatch message to callback functions
    """
    def dispatch_message(self, channel, args, kwargs):
        """
        Calls callback functions
        """
        for func, channels in self.application.registry.senders:
            if channels is None or channel in channels:
                self.application.executor.submit(
                    func, channel, self.application.clients, *args, **kwargs)
