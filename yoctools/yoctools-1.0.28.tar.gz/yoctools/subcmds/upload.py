# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
from yoctools import *


class Upload(Command):
    common = True
    helpSummary = "upload compoent to OCC"
    helpUsage = """
%prog [<component>...]
"""
    helpDescription = """
upload compoent to OCC
"""
    # def _Options(self, p):
    #     p.add_option('-a', '--all',
    #                  dest='show_all', action='store_true',
    #                  help='show the complete list of commands')

    def Execute(self, opt, args):
        yoc = YoC()
        if len(args) == 0:
            yoc.uploadall()
        else:
            for name in args:
                yoc.upload(name)
