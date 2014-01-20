# -*- coding: utf-8 -*-
from django.conf import settings

GLOBAL_CONF = getattr(settings, 'MEASE', {})
WEBSOCKET = GLOBAL_CONF.get('WEBSOCKET_SERVER', {})

BACKEND_CLASS_PATH = GLOBAL_CONF.get('BACKEND_CLASS', 'mease.backends.redis.RedisBackend')

WEBSOCKET_PORT = WEBSOCKET.get('PORT', 9090)
WEBSOCKET_AUTORELOAD = WEBSOCKET.get('AUTORELOAD', getattr(settings, 'DEBUG', False))
