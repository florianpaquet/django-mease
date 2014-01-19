# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.importlib import import_module

__all__ = ('autodiscover', 'registry', 'opener', 'closer', 'receiver', 'sender')


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

    def receiver(self, func, json=False):
        """
        Registers a receiver function
        """
        self.receivers.append((func, json))

    def sender(self, func, channels=None):
        """
        Registers a sender function
        """
        self.senders.append((func, channels))

registry = MeaseRegistry()
