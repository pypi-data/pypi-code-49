#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
import logging
import logging.handlers
#############################################
# File Name: maind.py
# Author: stosc
# Mail: stosc@sidaxin.com
# Created Time:  2020-2-8 19:17:34
#############################################
import os
import sys
import time

import _thread

import logging
import logging.handlers

try:
    from data2es.myDaemon import Daemon
    from data2es.main import *
    from data2es import __daemonName__, __serverName__
except ModuleNotFoundError:
    from myDaemon import Daemon
    from main import  *
    from __init__ import __daemonName__, __serverName__    



class D2esServiceDaemon(Daemon):
    def run(self, args):        
        sys.stdout.write('Daemon started with pid %s \n' % (os.getpid()))               
        runData2es(args[1],self.splitLogFile)
    def stop(self):
        super(D2esServiceDaemon, self).stop()


def run():
    PIDFILE = '/tmp/%s.pid' % __daemonName__
    LOG = '/tmp/%s.log' % __daemonName__
    ERR = '/tmp/%s.err.log' % __daemonName__
    rc = 'start|stop|restart|kill'
    parser = argparse.ArgumentParser(prog='%s' % __daemonName__, usage='%s {%s} [-c]' %(__daemonName__ ,rc))
    parser.add_argument("-c", "--config", help="Specify configuration file path.", metavar='CONFIGFILE_PATH',
                        required=False)
    parser.add_argument("-l", "--logfile", help="Specify log file path.", metavar='LOG_FILE_PATH',
                        required=False)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')
    # 添加参数解析
    parser.add_argument("runControl", metavar='{%s}' % rc, nargs='+', choices=rc.split('|'),
                        help="This control command can be used with %s. Used to control the running of data2esd daemons" % (
                            rc.replace('|', ' or ')))
    # 开始解析
    args = parser.parse_args()
    runCmd = args.runControl[0]
    if args.logfile != None:
        with open(args.logfile, 'w'): # OSError if file exists or is invalid
            pass
        if os.path.isfile(args.logfile):            
            LOG = args.logfile
    config = ""
    rca = rc.split('|')
    daemon = D2esServiceDaemon(pidfile=PIDFILE, stdout=LOG, stderr=ERR)
    
    if runCmd == rca[0]:
        config = args.config
        if config == None:
            logger.error('when start must specify configuration file path use -c/--config.')
            sys.exit(-1)
        else:
            print('The log file is %s'%os.path.abspath(LOG))                       
            daemon.start(['-c', '%s' % config])            
    elif runCmd == rca[1]:
        daemon.stop()
    elif runCmd == rca[2]:
        daemon.restart()
    elif runCmd == rca[3]:
        daemon.kill()


if __name__ == '__main__':
    run()
