# -*- coding: utf-8 -*-
import logging
from django.core.management.base import BaseCommand

from ... import mease
from ...loader import autodiscover
from ...settings import WEBSOCKET_PORT
from ...settings import WEBSOCKET_AUTORELOAD

LOGGER = logging.getLogger('mease.websocket_server')


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Starts websocket server
        """
        # Load registry
        autodiscover()

        # Start server
        mease.run_websocket_server(WEBSOCKET_PORT, WEBSOCKET_AUTORELOAD)
