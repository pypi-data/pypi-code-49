#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/12
# @time: 10:54
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import platform



# MARK:- 去空白

# 去除左右空白
# return string   # 非 None
def trim(value):
    if isStr(value):
        return value.strip()
    else:
        return ""


# MARK:- 是否为空串

def isEmpty(value):
    return isStr(value) and "" == value

def isNotEmpty(value):
    return isStr(value) and len(value) > 0



# MARK:- 类型判断

# 判断是否字符串
def isStr(value):
    return isinstance(value, str) or ("2" == platform.python_version().split(".")[0] and isinstance(value, unicode))


# MARK:- 编码

# 字符转 ascii 码
# return: int?
def char2Ascii(c):
    c = trim(c)
    if 1 != len(c):
        return None
    else:
        return ord(c)



# 判断是否整数字符串
# return: bool
def isIntStr(value):
    value = trim(value)

    if "" == value:
        return False

    fromInt = char2Ascii('0')
    toInt = char2Ascii('9')

    for c in value:
        cAscii = char2Ascii(c)
        if None == cAscii:
            return False
        elif fromInt <= cAscii and cAscii <= toInt:
            pass
        else:
            return False

    return True