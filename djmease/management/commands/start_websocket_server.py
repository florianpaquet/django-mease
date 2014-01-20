# -*- coding: utf-8 -*-
import logging
from django.core.management.base import BaseCommand

from mease.server import WebSocketServer

from ... import mease
from ...loader import autodiscover

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
        autodiscover()
        websocket_server = WebSocketServer(mease)

        # Log registry
        LOGGER.debug("Registered callback functions :")

        LOGGER.debug(
            "Openers : [%s]" % self._registry_names(
                websocket_server.application.mease.openers))

        LOGGER.debug(
            "Closers : [%s]" % self._registry_names(
                websocket_server.application.mease.closers))

        LOGGER.debug(
            "Receivers : [%s]" % self._registry_names(
                websocket_server.application.mease.receivers))

        LOGGER.debug(
            "Senders : [%s]" % self._registry_names(
                websocket_server.application.mease.senders))

        # Start server
        #LOGGER.info("Started websocket server on port {port}".format(port=port))
        websocket_server.run()
