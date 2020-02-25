#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@corp.ovh.com>


"""
from collections import OrderedDict


class Registry(object):
    __errors = OrderedDict()

    @classmethod
    def register(cls, clazz):
        if clazz.MSGID not in cls.__errors:
            cls.__errors[clazz.MSGID] = clazz
        return clazz

    @classmethod
    def filter_by_status(cls, code):
        return [x for x in cls.__errors.values() if x.CODE == code]

    @staticmethod
    def error_to_dict(clazz):
        return dict(
            code=clazz.CODE, description=clazz.__doc__, msgid=clazz.MSGID,
            name=clazz.__name__
        )

    @classmethod
    def to_list(cls):
        return [cls.error_to_dict(x) for x in cls.__errors.values()]

    @classmethod
    def to_dict(cls):
        return cls.__errors

    @classmethod
    def craft_error(cls, msgid, **kwargs):
        data = dict(msgid=msgid, **kwargs)
        if msgid in cls.__errors.keys():
            return cls.__errors[msgid](**data)
        else:
            from cdumay_error import Error
            return Error(**data)
