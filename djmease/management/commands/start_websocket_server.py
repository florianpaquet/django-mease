# -*- coding: utf-8 -*-
import logging
from django.core.management.base import BaseCommand

from ... import mease
from ...loader import autodiscover
from ...settings import WEBSOCKET_PORT
from ...settings import WEBSOCKET_AUTORELOAD

LOGGER = logging.getLogger('mease.websocket_server')


class Command(BaseCommand):

    def _registry_names(self, registry):
        """
        Returns functions names for a registry
        """
        return ', '.join(
            f.__name__ if not isinstance(f, tuple) else f[0].__name__
            for f in registry)

    def handle(self, *args, **options):
        """
        Starts websocket server
        """
        # Load registry
        autodiscover()

        # Start server
        mease.run_websocket_server(WEBSOCKET_PORT, WEBSOCKET_AUTORELOAD)
