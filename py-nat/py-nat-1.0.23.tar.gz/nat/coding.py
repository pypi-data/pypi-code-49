#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/11
# @time: 21:40
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import sys
import nat.cmd


# 设置默认为 utf8 编码
def setDefaultUTF8():
    __setDefaultEncoding('utf-8')


# 设置默认编码
def __setDefaultEncoding(encoding):
    if nat.cmd.isPythonVsn2():
        reload(sys)
        sys.setdefaultencoding(encoding)


