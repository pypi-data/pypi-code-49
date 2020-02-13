#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019-10-21
# @time: 23:44
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#


import nat.string



__globalMap = {}





# 判断是否有键值对
# return: bool
def hasKey(keyStr):
    keyStr = nat.string.trim(keyStr)
    return keyStr in __globalMap



# 根据键获取值
# return: Any
def get(keyStr):
    keyStr = nat.string.trim(keyStr)
    return __globalMap.get(keyStr, None)

# 获取字符串值
# return: string
def getStr(keyStr, defValue = ""):
    value = get(keyStr)
    if nat.string.isStr(value):
        return value
    elif None == defValue:
        return ""
    else:
        return defValue

# 获取整型值
# return: int
def getInt(keyStr, defValue = 0):
    value = get(keyStr)
    if isinstance(value, int):
        return value
    elif None == defValue:
        return 0
    else:
        return defValue


# 获取布尔值
# return: bool
def getBool(keyStr, defValue = False):
    value = get(keyStr)
    if isinstance(value, bool):
        return value
    elif None == defValue:
        return False
    else:
        return defValue



# 设置键值对
# param: value :: Any   # 当 value 为 None 时移除键值对
# return: bool
def set(keyStr, value):
    keyStr = nat.string.trim(keyStr)
    if "" == keyStr:
        return False

    elif None == value:
        del __globalMap[keyStr]
        return True

    else:
        __globalMap[keyStr] = value
        return True


