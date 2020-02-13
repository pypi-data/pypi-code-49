#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2019/12/29
# @time: 15:32
# @doc: 中国手机号
# Copyright © 2019 natloc_developer. All rights reserved.
#

import nat.string


# 是否 11 位长度
def __isLenCorrect(phoneStr):
    return 11 == len(nat.string.trim(phoneStr))


# 判断是否合法的字符
def __isCharCorrect(phoneStr):
    ascii0 = ord('0')
    ascii9 = ascii0 + 9

    phoneStr = nat.string.trim(phoneStr)
    for c in phoneStr:
        ascii = ord(c)
        if ascii < ascii0 or ascii > ascii9:
            return False

    return 1 == ord(phoneStr[0])


# 判断是否有效手机号
def isValid(phoneStr):
    return __isLenCorrect(phoneStr) and __isCharCorrect(phoneStr)

