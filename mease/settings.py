# -*- coding: utf-8 -*-
from django.conf import settings

__all__ = (
    'SUBSCRIBER_CLASS_PATH', 'REDIS_CHANNELS', 'REDIS_HOST', 'REDIS_PORT', 'MAX_WORKERS')

SUBSCRIBER_CLASS_PATH = getattr(
    settings, 'MEASE_SUBSCRIBER_CLASS', 'mease.subscribers.redis.RedisSubscriber')

REDIS_CHANNELS = getattr(settings, 'MEASE_REDIS_CHANNELS', 'websocket')
REDIS_HOST = getattr(settings, 'MEASE_REDIS_HOST', 'localhost')
REDIS_PORT = getattr(settings, 'MEASE_REDIS_PORT', 6379)

MAX_WORKERS = getattr(settings, 'MEASE_MAX_WORKERS', 15)
