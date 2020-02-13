#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2020/1/6
# @time: 18:17
# @doc:
# Copyright © 2020 natloc_developer. All rights reserved.
#

import argparse


# 实例化对象
def createParser():
    return argparse.ArgumentParser()

# 生成参数对象
def genArgs(parser):
    if None != parser:
        return parser.parse_args()
    else:
        return None



# MARK:- 组

# 创建分组信息
def createGroup(parser, required = False):
    if None != parser:
        return parser.add_mutually_exclusive_group(required = required)
    else:
        return None


