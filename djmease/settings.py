# -*- coding: utf-8 -*-
from django.conf import settings

MEASE_SETTINGS = getattr(settings, 'MEASE', {})

# Backend

BACKEND_CLASS_PATH = MEASE_SETTINGS.get(
    'BACKEND', 'mease.backends.redis.RedisBackend')

BACKEND_SETTINGS = MEASE_SETTINGS.get('BACKEND_SETTINGS', {})
