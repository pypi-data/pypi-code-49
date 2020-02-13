#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 15:38
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import json

import nat.string

# 从字符串转为 json
# return: dict
def str2json(jsonStr):
    return json.loads( nat.string.trim(jsonStr) )


# 从 json 转为字符串
# param: jsonObj :: dict
# return string
def json2str(jsonObj):
    if isinstance(jsonObj, dict):
        return json.dumps(jsonObj)
    else:
        return None
