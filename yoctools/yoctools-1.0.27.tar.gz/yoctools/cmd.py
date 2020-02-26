# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import os
import sys
import optparse

from .subcmds import all_commands
from .yoc import *


global_options = optparse.OptionParser(
    usage="yoc COMMAND [ARGS]"
)


class YocCommand:
    def __init__(self):
        self.conf = Configure()
        self.commands = {}
        if self.conf.init:
            self.commands = all_commands
        else:
            self.commands['init'] = all_commands['init']
            self.commands['help'] = all_commands['help']
            self.commands['toolchain'] = all_commands['toolchain']
            all_commands['help'].commands = self.commands


    def _ParseArgs(self, argv):
        """Parse the main `yoc` command line options."""
        name = None
        glob = []

        for i in range(len(argv)):
            if not argv[i].startswith('-'):
                name = argv[i]
                if i > 0:
                    glob = argv[:i]
                argv = argv[i + 1:]
                break
        if not name:
            glob = argv
            name = 'help'
            argv = []
        gopts, _gargs = global_options.parse_args(glob)
        return (name, gopts, argv)

    def _Run(self, name, gopts, argv):
        result = 0
        try:
            cmd = self.commands[name]

        except KeyError:
            print("yoc: '%s' is not a yoc command.  See 'yoc help'." %
                  name, file=sys.stderr)
            return 1

        try:
            copts, cargs = cmd.OptionParser.parse_args(argv)
            copts = cmd.ReadEnvironmentOptions(copts)
        except Exception as e:
            print('error: in `%s`: %s' % (' '.join([name] + argv), str(e)),
                  file=sys.stderr)
            print('error: manifest missing or unreadable -- please run init',
                  file=sys.stderr)
            return 1
        try:
            cmd.ValidateOptions(copts, cargs)
            result = cmd.Execute(copts, cargs)
        except Exception as e:
            print(e)
            pass
        return result

    def Execute(self, argv):
        name, gopts, argv = self._ParseArgs(argv)

        self._Run(name, gopts, argv)


def main():
    cmd = YocCommand()
    cmd.Execute(sys.argv[1:])
