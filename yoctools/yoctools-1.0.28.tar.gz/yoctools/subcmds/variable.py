# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class Variable(Command):
    common = True
    helpSummary = "Display variables for the current project"
    helpUsage = """
%prog [<variable>...]
"""
    helpDescription = """
Display variables for the current project
"""
    # def _Options(self, p):
    #     p.add_option('-a', '--all',
    #                  dest='show_all', action='store_true',
    #                  help='show the complete list of commands')

    def Execute(self, opt, args):
        yoc = YoC()
        solution = yoc.getSolution()
        if len(args) == 0:
            for k, v in solution.variables.items():
                print("%-10s = %s" % (k, v))
        else:
            for arg in args:
                var = solution.variables.get(arg)
                print(var)
