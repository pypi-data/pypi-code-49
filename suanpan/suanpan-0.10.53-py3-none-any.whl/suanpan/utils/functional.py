# coding=utf-8
from __future__ import absolute_import, print_function

import functools


def instancemethod(func):
    @functools.wraps(func)
    def _dec(self, *args, **kwargs):  # pylint: disable=unused-argument
        return func(*args, **kwargs)

    return _dec


def bindmethod(instance, func, name=None):
    name = name or func.__name__
    func = func.__get__(instance, instance.__class__)
    setattr(instance, name, func)
    return instance


def bind(instance, func, name=None):
    return bindmethod(instance, instancemethod(func), name=name)


def onlyonce(func):
    setattr(func, "__onlyonce_called__", False)
    setattr(func, "__onlyonce_return__", None)

    @functools.wraps(func)
    def _dec(*args, **kwargs):
        if not getattr(func, "__onlyonce_called__", False):
            setattr(func, "__onlyonce_called__", True)
            setattr(func, "__onlyonce_return__", func(*args, **kwargs))
        return getattr(func, "__onlyonce_return__")

    return _dec
