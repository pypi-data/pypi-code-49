#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# File Name: daemon.py
# Author: stosc
# Mail: stosc@sidaxin.com
# Created Time:  2020-2-8 19:17:34
#############################################

import atexit
import os
import signal
import sys
import time



class Daemon:
    def __init__(self, pidfile='/tmp/daemon.pid', stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
        self.out_file = None
        

    def reSetLog(self):
        self.setLog()

    def setLog(self):
        # Flush I/O buffers
        sys.stdout.flush()
        sys.stderr.flush()
        
        with open(self.stdout, 'ab', 0) as f:            
            os.dup2(f.fileno(), sys.stdout.fileno())

        with open(self.stderr, 'ab', 0) as f:            
            os.dup2(f.fileno(), sys.stderr.fileno())
        

    def daemonize(self):
        if os.path.exists(self.pidfile):
            raise RuntimeError('Already running.')

        # First fork (detaches from parent)
        try:
            if os.fork() > 0:
                raise SystemExit(0)
        except OSError as e:
            raise RuntimeError('fork #1 faild: {0} ({1})\n'.format(e.errno, e.strerror))

        os.chdir('/')
        os.setsid()
        os.umask(0o22)

        # Second fork (relinquish session leadership)
        try:
            if os.fork() > 0:
                raise SystemExit(0)
        except OSError as e:
            raise RuntimeError('fork #2 faild: {0} ({1})\n'.format(e.errno, e.strerror))
        

        # Replace file descriptors for stdin, stdout, and stderr
        self.setLog()
        
        # Write the PID file
        with open(self.pidfile, 'w') as f:
            print(os.getpid(), file=f)

        def delPid():
            if os.path.exists(self.pidfile):
                os.remove(self.pidfile)

        # Arrange to have the PID file removed on exit/signal
        atexit.register(lambda: delPid())

        signal.signal(signal.SIGTERM, self.__sigterm_handler)

    # Signal handler for termination (required)
    @staticmethod
    def __sigterm_handler(signo, frame):
        raise SystemExit(1)

    def start(self, args):
        try:
            self.daemonize()
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)
        self.run(args)

    def kill(self):
        if os.path.exists(self.pidfile):
            try:
                with open(self.pidfile) as f:
                    pid = int(f.read())
                    print(pid)
                    os.kill(pid, signal.SIGTERM)
            finally:
                os.remove(self.pidfile)

    def stop(self):
        try:
            if os.path.exists(self.pidfile):
                with open(self.pidfile) as f:
                    os.kill(int(f.read()), signal.SIGTERM)
            else:
                print('Not running.', file=sys.stderr)
                raise SystemExit(1)
        except OSError as e:
            if 'No such process' in str(e) and os.path.exists(self.pidfile):
                os.remove(self.pidfile)

    def restart(self):
        self.stop()
        self.start()

    def run(self, args):
        pass

    def splitLogFile(self):        
        #if self.split.run(): 
            #self.setLog()           
        pass        



