#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 13:19
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import os
import platform

import nat.string
import nat.log


# MARK:- 版本

# 获取当前 Python 的版本
# return: string   # 如："2.7.5"
def getPythonVsn():
    return platform.python_version()

# 判断当前是否 Python 2.x
# return: bool
def isPythonVsn2():
    return "2" == getPythonVsn().split(".")[0]

# 判断当前是否 Python 3.x
# return: bool
def isPythonVsn3():
    return "3" == getPythonVsn().split(".")[0]



# MARK:- 执行命令

# 执行命令
# return int   # 0-成功
def execute(cmdStr):
    return 0 == os.system(cmdStr)

def executeRead(cmdStr):
    return os.popen(cmdStr)


# MARK:- 安装命令

# 判断是否已安装命令
# return: bool
def hasCmd(commandStr):
    commandStr = nat.string.trim(commandStr)
    if "" == commandStr:
        return False
    else:
        return execute("which %s" %(commandStr))

# 安装 pip 命令
# return true
def installPip():
    cmdStr = "sudo easy_install pip"
    return execute(cmdStr)




# 根据当前 python 版本获取 pip ｜ pip3 命令
# return: string
def __getPipCmdByVsn():
    return "pip3" if isPythonVsn3() else "pip"

# pip 安装命令工具
# return bool
def installPipDep(depName, withSudo = False):
    depName = nat.string.trim(depName)

    if "" == depName:
        nat.log.error(u"要安装的依赖名称为空字符串")
        return False
    elif hasInstalledPipDep(depName):
        return True
    else:
        return __installPipDep(depName)

def __installPipDep(depName):
    pipCmd = __getPipCmdByVsn()
    cmdStr = "%s install %s --user" %(pipCmd, depName)
    isSuccess = execute(cmdStr)

    if not isSuccess:
        nat.log.error(u"%s 安装命令 %s 失败！" %(pipCmd, depName))

    return isSuccess

# 判断是否已通过 pip 安装依赖
# return: bool
def hasInstalledPipDep(depName):
    depName = nat.string.trim(depName)
    if "" == depName:
        return False
    else:
        pipCmd = "pip3" if isPythonVsn3() else "pip"
        return "" != executeRead("%s show %s" %(pipCmd, depName)).read()




# MARK:- 执行结果

# 获取上一条命令执行的返回码
# @return code :: int   # 0-成功；

def getLastCmdRetCode():
    return int(nat.string.trim(executeRead("echo $?").read()))

# 判断上一条命令是否执行成功

def isLastCmdSuccess():
    return 0 == getLastCmdRetCode()
    



