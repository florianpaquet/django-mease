# -*- coding: utf-8 -*-
from django.conf import settings

BACKEND_CLASS_PATH = getattr(
    settings, 'MEASE_BACKEND_CLASS', 'mease.backends.redis.RedisBackend')
BACKEND_CONF = getattr(settings, 'MEASE_BACKEND_CONFIG', {})

WEBSOCKET = getattr(settings, 'MEASE_WEBSOCKET_CONFIG', {})

WEBSOCKET_PORT = WEBSOCKET.get('PORT', 9090)
WEBSOCKET_AUTORELOAD = WEBSOCKET.get('AUTORELOAD', getattr(settings, 'DEBUG', False))
