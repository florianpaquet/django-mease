# -*- coding: utf-8 -*-
from django.utils.module_loading import import_by_path

from mease import Mease

from .settings import BACKEND_CLASS_PATH
from .settings import BACKEND_CONF

BACKEND_CLASS = import_by_path(BACKEND_CLASS_PATH)

mease = Mease(BACKEND_CLASS, BACKEND_CONF)
