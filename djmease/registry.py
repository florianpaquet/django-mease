# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.module_loading import import_by_path

from mease import Mease


# Get mease conf
MEASE_CONF = getattr(settings, 'MEASE_CONF', {})

# Get backend class
BACKEND_CLASS_PATH = MEASE_CONF.get('BACKEND_CLASS', 'mease.backends.redis.RedisBackend')
BACKEND_CLASS = import_by_path(BACKEND_CLASS_PATH)

mease = Mease(BACKEND_CLASS, MEASE_CONF)
