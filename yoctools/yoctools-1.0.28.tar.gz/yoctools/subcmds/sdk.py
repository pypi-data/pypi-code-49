# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
from yoctools import *


class Sdk(Command):
    common = True
    helpSummary = "generate current solution SDK"
    helpUsage = """
%prog
"""
    helpDescription = """
generate current solution SDK.
"""
    # def _Options(self, p):
    #     p.add_option('-a', '--all',
    #                  dest='show_all', action='store_true',
    #                  help='show the complete list of commands')

    def Execute(self, opt, args):
        yoc = YoC()
        solution = yoc.getSolution()
        if solution:
            solution.install()
