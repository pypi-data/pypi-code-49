#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2019/12/31
# @time: 16:52
# @doc:
# Copyright © 2019 natloc_developer. All rights reserved.
#

import time
import datetime


# 获取时间戳
# return double
def getTi():
    return time.time()


# 获取当前时刻的对象
# 可直接获取成员属性；如：now = nat.datetime.now(); now.year
def now():
    return datetime.datetime.now()


# 获取日期数字
# return: int   # 如：20190909
def getDateInt(datetimeObj):
    if datetime.datetime != type(datetimeObj):
        return 0
    else:
        return (datetimeObj.year * 10000) + (datetimeObj.month * 100) + datetimeObj.day


# 获取星期几
# return: int   [1(星期一), 7(星期天)]
def getWeekday(datetimeObj = now()):
    if datetime.datetime == type(datetimeObj):
        return datetimeObj.weekday() + 1

    else:
        return None