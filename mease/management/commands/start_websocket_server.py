# -*- coding: utf-8 -*-
import logging
from django.core.management.base import BaseCommand
from django.conf import settings
from optparse import make_option

from ...server import WebSocketServer

DEBUG = getattr(settings, 'DEBUG', False)
LOGGER = logging.getLogger('mease.websocket_server')


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        # Debug
        make_option(
            '-d',
            '--debug',
            action='store_true',
            dest='debug',
            default=DEBUG,
            help="Debug mode"),

        # Listen port
        make_option(
            '-p',
            '--port',
            action='store',
            dest='port',
            default=9090,
            help="Port to listen"),
    )

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
        debug, port = options['debug'], options['port']

        websocket_server = WebSocketServer(
            debug=options['debug'], port=options['port'])

        # Log registry
        LOGGER.debug("Registered callback functions :")

        LOGGER.debug(
            "Openers : [%s]" % self._registry_names(
                websocket_server.application.registry.openers))

        LOGGER.debug(
            "Closers : [%s]" % self._registry_names(
                websocket_server.application.registry.closers))

        LOGGER.debug(
            "Receivers : [%s]" % self._registry_names(
                websocket_server.application.registry.receivers))

        LOGGER.debug(
            "Senders : [%s]" % self._registry_names(
                websocket_server.application.registry.senders))

        # Start server
        LOGGER.info("Started websocket server on port {port}".format(port=port))
        websocket_server.run()
