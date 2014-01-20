# -*- coding: utf-8 -*-
from django.utils.module_loading import import_by_path

from mease import Mease

from .settings import GLOBAL_CONF
from .settings import BACKEND_CLASS_PATH


BACKEND_CLASS = import_by_path(BACKEND_CLASS_PATH)
mease = Mease(BACKEND_CLASS, GLOBAL_CONF)
