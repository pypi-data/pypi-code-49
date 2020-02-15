# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：py2.py
# 摘    要：兼容python2模块
#
# 当前版本：V1.0.0
# 作    者：qianmx21829
# 完成日期：2018-10-08
# 备    注：该模块用于p
###############################################################################

import six

if six.PY2:
    import sys

    # ignore
    reload(sys)
    sys.setdefaultencoding("utf-8")


def to_utf8(string):
    try:
        if six.PY2:
            return string.encode('utf-8')
        else:
            return string
    except AttributeError:
        return to_utf8(str(string))
    except UnicodeDecodeError:
        return to_utf8(unicode(string, 'utf-8'))


def from_utf8(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string


try:
    from functools import lru_cache as base_lru_cache
except ImportError:
    from fastcache import lru_cache as base_lru_cache

cached_functions = []


def lru_cache(*args, **kwargs):
    def decorator(func):
        func = base_lru_cache(*args, **kwargs)(func)
        cached_functions.append(func)
        return func

    return decorator


def clear_all_cached_functions():
    for func in cached_functions:
        func.cache_clear()


try:
    from inspect import signature
except ImportError:
    from funcsigs import signature
