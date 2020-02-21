#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import warnings
import psutil


class PyPid:

    def __init__(self, path_pid_file):
        self.path_pid_file = path_pid_file

    def open(self):
        self.checkpid()
        self.write_pid_file()

    def close(self):
        self.delete_pidfile()

    def write_pid_file(self):
        pid = os.getpid()
        lockfile = open(self.path_pid_file, 'w')
        lockfile.write(str(pid))
        lockfile.close()

    def checkpid(self):
        if os.path.exists(self.path_pid_file):
            pid = open(self.path_pid_file, 'r').read()
            if not pid.isdigit():
                warnings.warn(
                    'Pid file already exists, but containts an invalid pid --> {}'.format(pid),
                    UserWarning,
                    stacklevel=2
                )
            if psutil.pid_exists(int(pid)):
                raise IOError('Pid file already exists, the process is running!! --> {}'.format(pid))

    def delete_pidfile(self):
        if os.path.exists(self.path_pid_file):
            os.remove(self.path_pid_file)
        else:
            warnings.warn(
                "Pid file does not exists: '{path_pid_file}'".format(
                    path_pid_file=self.path_pid_file),
                UserWarning,
                stacklevel=1)
