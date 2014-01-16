from colorama import Fore
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from optparse import make_option

from ...server import WebSocketServer

DEBUG = getattr(settings, 'DEBUG', False)

LOG_INFO, LOG_SUCCESS, LOG_ERROR = 1, 2, 3
LOG_COLORS = {
    LOG_INFO: Fore.YELLOW,
    LOG_SUCCESS: Fore.GREEN,
    LOG_ERROR: Fore.RED,
}


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

    def log(self, message, level=LOG_INFO):
        """
        Prints log
        """
        assert level in LOG_COLORS.keys()
        log_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

        self.stdout.write("{time} {color}{message}{reset}".format(
            color=LOG_COLORS[level],
            time=log_time,
            message=message,
            reset=Fore.RESET))

    def handle(self, *args, **options):
        """
        Starts websocket server
        """
        debug, port = options['debug'], options['port']

        self.log("Starting websocket server on port {port}".format(port=port))

        websocket_server = WebSocketServer(debug=options['debug'], port=options['port'])
        websocket_server.run()
