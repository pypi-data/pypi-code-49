# -*- coding: utf-8 -*-

#  -*- coding: utf-8 -*-
#  =====================================================================
#  Copyright (c)2019, 恒生电子股份有限公司
#  All rights reserved.
# 
#  文件名称：cache_storage.py
#  摘    要：
# 
#  当前版本：V1.0.0
#  作    者：qianmx21829
#  完成日期：2019-07-17
#  备    注：
#  =====================================================================

###############################################################################
#
# 文件名称：cache_storage.py
# 摘    要：时间段缓存
#
# 当前版本：V1.0.0
# 作    者：qianmx21829
# 完成日期：2019-04-15
# 备    注：
###############################################################################
import datetime
import inspect
from functools import wraps

import numpy as np
import pandas as pd

from IQCommon.utils import get_original_function

TIMEDELTA = datetime.timedelta(days=365)

PD_TYPES = (pd.Series, pd.DataFrame, pd.Panel)
NP_TYPES = (np.core.ndarray,)


def to_hashable_args(value):
    """
    将变量变为可哈希化的
    :param value:
    :return:
    """
    if value.__hash__:
        # 原本就是可hash得变量
        return value
    if isinstance(value, dict):
        # 字典类型的处理
        return tuple(sorted(value.items()))
    if isinstance(value, list):
        # 列表类型的处理
        return tuple(value)


class Cache(object):

    """
    缓存组件
    """
    def __init__(self):
        self._miss = 0  # 未中靶
        self._hit = 0  # 中靶
        self._cache = {}  # 缓存信息

    @property
    def cache(self):
        return self._cache

    def clear(self):
        """
        清空缓存
        :return: None
        """
        self._cache.clear()
        self._hit = 0
        self._miss = 0

    @property
    def miss(self):
        return self._miss

    def add_miss(self):
        """
        加一次未中靶
        :return:
        """
        self._miss += 1

    @property
    def hit(self):
        return self._hit

    def add_hit(self):

        """
        加一次中靶
        :return:
        """
        self._hit += 1

    @property
    def status(self):
        """
        状态展示
        :return: dict
        """
        return {
            'miss': self._miss,
            'hit': self._hit
        }

    @property
    def keys(self):
        """
        缓存key信息
        :return:
        """
        return [
            (i, v[0], v[1])
            for i, v in self.cache.items()
        ]

    def __getitem__(self, item):
        return self._cache[item]

    def __setitem__(self, key, value):
        self._cache[key] = value


def apply_cache(
        range_start_args,
        range_end_args,
        on_off_limit_start,
        on_off_limit_end,
        sort_key=None
):
    """
    获取缓存装饰器
    :param range_start_args: 时间变量"开始"的变量名
    :type range_start_args: str
    :param range_end_args: 时间变量“结束”的变量名
    :type range_end_args: str
    :param on_off_limit_start: 时间变量"开始"缓存扩展范围时候的变化函数
    :type on_off_limit_start: function
    :param on_off_limit_end: 时间变量"结束"缓存扩展范围时候的变化函数
    :type on_off_limit_end: function
    :param sort_key: 排序字段， 如果为None则不排序
    :type sort_key: str / None
    :return:
    """
    
    def decorator(func):
        """
        装饰器
        :param func:
        :return:
        """
        base_func = get_original_function(func)
        # 函数变量列表
        argument_list = [
            name
            for name in sorted(inspect.signature(base_func).parameters)
            if name != range_start_args and name != range_end_args
        ]

        cache = Cache()

        @wraps(func)
        def func_wrapper(*args, **kwargs):

            call_args = inspect.getcallargs(
                base_func, *args, **kwargs)
            # 静态遍历
            static_args = tuple(
                [
                    to_hashable_args(call_args[name])
                    for name in argument_list
                ]
            )
            # 时间范围变量
            start = call_args[range_start_args]
            end = call_args[range_end_args]
            try:
                # 检查是否有对应静态变量的缓存
                cache_start, cache_end, data = cache[static_args]
            except KeyError:
                # 没有则增加缓存
                start_ = on_off_limit_start(start, **call_args)
                end_ = on_off_limit_end(end, **call_args)
                call_args[range_start_args] = start_
                call_args[range_end_args] = end_
                data = func(** call_args)
                if sort_key and isinstance(data, PD_TYPES):
                    data.sort_values([sort_key], inplace=True)
                cache[static_args] = start_, end_, data
                cache.add_miss()
            else:
                # 有则比较是否在时间区段内
                concat_list = []
                if start < cache_start:
                    start_ = call_args[range_start_args] = on_off_limit_start(start)
                    call_args[end] = cache_start
                    concat_list.append(func(** call_args))
                else:
                    start_ = cache_start
                concat_list.append(data)
                if end > cache_end:
                    end_ = call_args[range_end_args] = on_off_limit_end(end)
                    call_args[range_start_args] = cache_end
                    concat_list.append(func(**call_args))
                else:
                    end_ = cache_end
                # 如果有区段的扩充则更新数据
                if len(concat_list) != 1:
                    data = pd.concat(concat_list)
                    data.sort_values([sort_key], inplace=True)
                    cache[static_args] = start_, end_, data
                    cache.add_miss()
                else:
                    cache.add_hit()
            # 截取所需数据
            s = data[sort_key].searchsorted(start)
            e = data[sort_key].searchsorted(end, side='right')
            try:
                return data.iloc[s:e].reset_index(drop=True)
            except TypeError:
                # 后续需要详细排查原因
                s = s[0]
                e = e[0]
                return data.iloc[s:e].reset_index(drop=True)
            except AttributeError:
                return data[s:e]
            
        # 为函数加入所需方法
        func_wrapper.clear = cache.clear
        func_wrapper.cache = cache
        func_wrapper.status = lambda :cache.status
        func_wrapper.get_info = lambda: '<cache_wrapper({}):{}({})>'.format(
            base_func.__name__,
            cache.status,
            cache.keys
        )
        return func_wrapper

    return decorator


# --提供传入on_off_limit_start，on_off_limit_end的预置函数-- #

# noinspection PyUnusedLocal
def get_next_year_date(_t, **kwargs):
    """
    往后推一年
    :param _t: 时间
    :type _t: datetime.datetime
    :return:
    """
    return _t + TIMEDELTA


# noinspection PyUnusedLocal
def get_pre_year_date(_t, **kwargs):
    """
    往后前一年
    :param _t: 时间
    :type _t: datetime.datetime
    """
    return _t - TIMEDELTA


# noinspection PyUnusedLocal
def get_next_year_date_str(_t, **kwargs):
    """
    往后推一年
    :param _t: 时间
    :type _t: str
    :return:
    """
    _t[:4] = str(int(_t[:4]) - 1)
    if _t[4:8] == '0229':
        _t[4:8] = '0228'
    return _t


# noinspection PyUnusedLocal
def get_pre_year_date_str(_t, **kwargs):
    """
    往后前一年
    :param _t: 时间
    :type _t: str
    """
    _t[:4] = str(int(_t[:4]) + 1)
    if _t[4:8] == '0229':
        _t[4:8] = '0228'
    return _t
