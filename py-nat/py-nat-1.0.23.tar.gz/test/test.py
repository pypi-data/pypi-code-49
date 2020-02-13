#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2020/1/2
# @time: 15:03
# @doc:
# Copyright © 2020 natloc_developer. All rights reserved.
#

import sys
import os

sys.path.insert(0, os.path.dirname(sys.path[0]))
print(sys.path[0])

import nat.datetime
import nat.cmd
import nat.log

nat.log.warn("---vsn: %s" %(nat.cmd.getPythonVsn()))

import notice.notice_meican