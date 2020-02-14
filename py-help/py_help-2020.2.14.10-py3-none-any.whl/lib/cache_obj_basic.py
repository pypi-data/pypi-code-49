# -*- coding: utf-8 -*-
import os
from .CommonLogger import debug


class CacheObjBasic(object):
    __instance = None
    _is_init = False

    def __init__(self):
        pass

    @classmethod
    def get_uniq_id(cls, *args, **kwargs):
        # debug("调了默认id方法:{}".format(args))
        args_str = '_'.join([str(one) for one in args])
        kwargs_str = '_'.join(["%s:%s" % (k, v) for k, v in kwargs.items()])
        return "%s-%s" % (args_str, kwargs_str)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = {}
        uniq_id = cls.get_uniq_id(*args, **kwargs)
        if cls.__instance.get(uniq_id) is not None:
            return cls.__instance.get(uniq_id)
        # debug("创建类:{},参数:{},uniq_id:{}".format(cls, args,uniq_id))
        the_instance = object.__new__(cls)
        # debug("创建类:{},对象为 {}".format(cls, the_instance))
        # the_instance.__init__(*args, **kwargs)
        cls.__instance[uniq_id] = the_instance
        return cls.__instance[uniq_id]
