# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class Show(Command):
    common = True
    helpSummary = "Display the detailed compilation information of the current project"
    helpUsage = """
%prog [<component>...]
"""
    helpDescription = """
Display the detailed compilation information of the current project.
"""
    # def _Options(self, p):
    #     p.add_option('-a', '--all',
    #                  dest='show_all', action='store_true',
    #                  help='show the complete list of commands')

    def Execute(self, opt, args):
        yoc = YoC()
        solution = yoc.getSolution()
        if solution:
            solution.show()
            for c in solution.components:
                c.show()
                c.info(4)
