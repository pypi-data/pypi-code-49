# -*- coding: utf-8 -*-
from datetime import datetime
from .CommonLogger import warn


def str_to_datetime(the_str):
    if isinstance(the_str, str):
        if len(the_str.split('T')) == 2:
            try:
                return datetime.strptime(the_str, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=None)
            except ValueError:
                try:
                    return datetime.strptime(the_str, "%Y-%m-%dT%H:%M:%S.%f%z").replace(tzinfo=None)
                except ValueError:
                    warn("转换出现异常")
                    return None
        if len(the_str.split(' ')) == 2:
            try:
                return datetime.strptime(the_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=None)
            except ValueError:
                try:
                    return datetime.strptime(the_str, "%Y-%m-%d %H:%M:%S.%f%z").replace(tzinfo=None)
                except ValueError:
                    warn("转换出现异常")
                    return None
        try:
            return datetime.strptime(the_str, "%Y-%m-%d").replace(tzinfo=None)
        except ValueError:
            warn("转换出现异常")
            return None
    elif isinstance(the_str, datetime):
        return the_str
    else:
        warn("不支持的类型:{}".format(the_str))
        return None
