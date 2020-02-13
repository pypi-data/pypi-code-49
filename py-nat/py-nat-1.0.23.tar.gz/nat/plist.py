#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/12
# @time: 22:33
# @doc: plist 文件
# Copyright © 2019 natloc. All rights reserved.
#

import nat.string
import nat.path
import nat.file
import nat.cmd


__CMD_PLIST_BUDDY = "/usr/libexec/PlistBuddy"



# 添加 布尔
# return: bool
def addBool(file, key, value, dictKey = ""):
    argKey = nat.string.trim(key)
    if nat.path.isFilePlist(file) and "" != argKey and (0 == value or 1 == value):

        if value:
            boolStr = "true"
        else:
            boolStr = "false"

        plistCmd = "Add %s:%s bool %s" %(__mkDictKey(dictKey), argKey, boolStr)
        return __execPlistCmd(plistCmd, file)
    else:
        return False

# 添加 字符串
# return: bool
def addStr(file, key, value, dictKey = ""):
    argKey = nat.string.trim(key)
    if nat.path.isFilePlist(file) and "" != argKey and nat.string.isStr(value):
        plistCmd = "Add %s:%s string '%s'" %(__mkDictKey(dictKey), argKey, value)
        return __execPlistCmd(plistCmd, file)
    else:
        return False

# 设置 字符串
# return: bool
def setStr(file, key, value):
    argKey = nat.string.trim(key)
    if nat.path.isFilePlist(file) and "" != argKey:
        plistCmd = "Set :%s '%s'" %(argKey, value)
        return __execPlistCmd(plistCmd, file)
    else:
        return False

# 添加 字典
# return: bool
def addDict(file, key):
    argKey = nat.string.trim(key)
    if nat.path.isFilePlist(file) and "" != argKey:
        plistCmd = "Add :%s dict" %(argKey)
        return __execPlistCmd(plistCmd, file)
    else:
        return False

# 移除键值对
# return: bool
def remove(file, key):
    argKey = nat.string.trim(key)
    if nat.path.isFilePlist(file) and "" != argKey:
        plistCmd = "Delete :%s" %(argKey)
        return __execPlistCmd(plistCmd, file)
    else:
        return False


# 创建 plist 的空文件
# return: bool
def createEmptyFile(file):
    initContent = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
</dict>
</plist>
"""
    return nat.file.createEmptyFile(file, initContent)





# return: string
def __mkDictKey(key):
    argKey = nat.string.trim(key)
    if "" != argKey:
        return ":%s" %(argKey)
    else:
        return ""

# return: bool
def __execPlistCmd(plistCmd, file):
    cmdStr = "%s -c \"%s\" %s" %(__CMD_PLIST_BUDDY, plistCmd, file)
    return nat.cmd.execute(cmdStr)