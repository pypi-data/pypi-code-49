#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 11:59
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import sys

__colorDefault = 0
__colorRed = 91
__colorGreen = 92
__colorBlue = 96
__colorYellow = 93
__colorPurple = 95



def debug(contentStr):
    __printWithColor(__colorDefault, "debug", contentStr)

def warn(contentStr):
    __printWithColor(__colorGreen, "warn", contentStr)

def error(contentStr):
    __printWithColor(__colorRed, "error", contentStr)

def exit(contentStr):
    __printWithColor(__colorRed, "exit", contentStr)
    sys.exit(1)



# MARK:- 内部方法

def __printWithColor(colorInt, tag, contentStr):
    print(u"\033[%im[%-5s]=== %s\033[%im" %(colorInt, tag, contentStr, __colorDefault))


