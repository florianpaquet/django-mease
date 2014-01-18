from django.conf import settings

__all__ = ('REDIS_CHANNELS', 'REDIS_HOST', 'REDIS_PORT', 'MAX_WORKERS')


REDIS_CHANNELS = getattr(settings, 'MEASE_REDIS_CHANNELS', 'websocket')
REDIS_HOST = getattr(settings, 'MEASE_REDIS_HOST', 'localhost')
REDIS_PORT = getattr(settings, 'MEASE_REDIS_PORT', 6379)

MAX_WORKERS = getattr(settings, 'MEASE_MAX_WORKERS', 15)
