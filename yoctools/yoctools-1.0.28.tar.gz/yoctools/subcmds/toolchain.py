# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

import os
from yoctools import *


class Toolchain(Command):
    common = True
    helpSummary = "Install toolchain"
    helpUsage = """
%prog [-a] [-c] [-r]
"""
    helpDescription = """
Install toolchain.
"""

    def _Options(self, p):
        p.add_option('-c', '--csky',
                     dest='install_csky', action='store_true',
                     help=' install csky-elfabiv2-tools')
        p.add_option('-r', '--riscv',
                     dest='install_riscv', action='store_true',
                     help=' install riscv-elf-tools')
        p.add_option('-a', '--all',
                     dest='install_all', action='store_true',
                     help=' install csky-elfabiv2-tools and riscv-elf-tools')

    def Execute(self, opt, args):
        if os.getuid() != 0:
            print('error: you cannot perform this operation unless you are root. \nsudo ' + ' '.join(sys.argv))
            exit(-1)

        need_usage = True
        tool = ToolchainInstall()
        if opt.install_all:
            tool.check_toolchain('csky-abiv2-elf')
            tool.check_toolchain('riscv64-unknown-elf')
            need_usage = False
        else:
            if opt.install_csky:
                tool.check_toolchain('csky-abiv2-elf')
                need_usage = False
            if opt.install_riscv:
                tool.check_toolchain('riscv64-unknown-elf')
                need_usage = False
        if need_usage:
            self.Usage()
