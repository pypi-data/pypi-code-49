#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/22
# @time: 10:15
# @doc: 版本管理：由 Major.Minor.Patch 组成
# Copyright © 2019 natloc. All rights reserved.
#

import nat.string



# 判断是否合法的版本号
# return: bool
def isValid(vsnStr):
    vsnArr = vsnStr.split(".")

    if 3 != len(vsnArr):
        return False

    major = nat.string.trim(vsnArr[0])
    minor = nat.string.trim(vsnArr[1])
    patch = nat.string.trim(vsnArr[2])

    if not nat.string.isIntStr(major) or int(major) < 0:
        return False

    elif not nat.string.isIntStr(minor) or int(minor) < 0:
        return False

    elif not nat.string.isIntStr(patch) or int(patch) < 0:
        return False

    else:
        return True


# 转为版本号码
# return: string   # 如："010101"
def toCodeStr(vsnStr):
    if not isValid(vsnStr):
        return ""

    vsnArr = vsnStr.split(".")
    major = int(nat.string.trim(vsnArr[0]))
    minor = int(nat.string.trim(vsnArr[1]))
    patch = int(nat.string.trim(vsnArr[2]))

    return "%02d%02d%02d" %(major, minor, patch)