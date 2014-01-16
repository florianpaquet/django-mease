from django.conf import settings
from django.utils.importlib import import_module

__all__ = ('autodiscover', 'registry', 'receiver', 'sender')


class WebSocketRegistry(object):
    """
    Registry for websocket callbacks
    """
    def __init__(self):
        self.receivers = []
        self.senders = []

    def receiver(self, func):
        """
        Registers a receiver function
        """
        self.receivers.append(func)

    def sender(self, func, channels):
        """
        Registers a sender function
        """
        self.senders.append((func, channels))

registry = WebSocketRegistry()


def autodiscover():
    """
    Autodiscovers apps with `mease_registry` modules
    """
    for app in getattr(settings, 'INSTALLED_APPS', []):
        import_module(app)

        try:
            import_module('%s.mease_registry' % app)
        except ImportError:
            pass


def receiver(func):
    return registry.receiver(func)


def sender(func, channels=None):
    return registry.sender(func, channels or [])
