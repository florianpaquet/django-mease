# -*- coding: utf-8 -*-
from .registry import registry

__all__ = ('opener', 'closer', 'receiver', 'sender')


def opener(function=None):
    def actual_decorator(f):
        registry.opener(f)

    if function:
        return actual_decorator(function)
    return actual_decorator


def closer(function=None):
    def actual_decorator(f):
        registry.closer(f)

    if function:
        return actual_decorator(function)
    return actual_decorator


def receiver(function=None, json=False):
    def actual_decorator(f):
        registry.receiver(f, json)

    if function:
        return actual_decorator(function)
    return actual_decorator


def sender(function=None, channels=None):
    def actual_decorator(f):
        registry.sender(f, channels)

    if function:
        return actual_decorator(function)
    return actual_decorator
