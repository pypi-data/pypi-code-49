# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import getpass

try:
    raw_input = raw_input
except NameError:
    raw_input = input

from yoctools import *


class Init(Command):
    common = True
    helpSummary = "Initialize yoc workspace in the current directory"
    helpUsage = """
%prog
"""
    helpDescription = """
Initialize yoc workspace in the current directory.
"""
    # def _Options(self, p):
    #     p.add_option('-a', '--all',
    #                  dest='show_all', action='store_true',
    #                  help='show the complete list of commands')

    def Execute(self, opt, args):
        conf = Configure()
        occ = OCC(conf)

        while not conf.init:
            conf.username = raw_input('Input OCC username: ')
            conf.password = getpass.getpass('password: ')

            if occ.login() == 0:
                conf.save()
                break
