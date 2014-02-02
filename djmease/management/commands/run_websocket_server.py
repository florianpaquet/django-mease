# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import BaseCommand
from optparse import make_option

from ... import mease
from ...loader import autodiscover


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '--port',
            '-p',
            action='store',
            dest='port',
            default=9090,
            help="Port to listen"),
        make_option(
            '--host',
            '-H',
            action='store',
            dest='host',
            default='localhost',
            help="Host to bind"),
        make_option(
            '--debug',
            '-d',
            action='store_true',
            dest='debug',
            default=getattr(settings, 'DEBUG', False),
            help="Debug mode")
    )

    def handle(self, *args, **options):
        """
        Starts websocket server
        """
        # Load registry
        autodiscover()

        # Start server
        mease.run_websocket_server(
            host=options['host'],
            port=options['port'],
            debug=options['debug'])
