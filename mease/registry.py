from django.conf import settings
from django.utils.importlib import import_module

__all__ = ('autodiscover', 'registry', 'opener', 'closer', 'receiver', 'sender')


class MeaseRegistry(object):
    """
    Registry for mease callbacks
    """
    def __init__(self):
        self.openers = []
        self.closers = []
        self.receivers = []
        self.senders = []

    def opener(self, func):
        """
        Registers an opener function
        """
        self.openers.append(func)

    def closer(self, func):
        """
        Registers a closer function
        """
        self.closers.append(func)

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

registry = MeaseRegistry()


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


def opener(func):
    return registry.opener(func)


def closer(func):
    return registry.closer(func)


def receiver(func):
    return registry.receiver(func)


def sender(func, channels=None):
    return registry.sender(func, channels or [])
