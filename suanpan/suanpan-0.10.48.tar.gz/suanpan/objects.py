# coding=utf-8
from __future__ import absolute_import, print_function

from addict import Dict


class HasName(object):
    @property
    def name(self):
        return self.__class__.__name__


class Context(Dict, HasName):
    @classmethod
    def froms(cls, *args, **kwargs):
        context = cls()
        context.update(item for arg in args for item in arg.items())
        context.update(kwargs)
        return context

    def __getitem__(self, name):
        value = super(Context, self).__getitem__(name)
        if isinstance(value, property):
            value = value.fget(self)
            self.__setitem__(name, value)
        return value
