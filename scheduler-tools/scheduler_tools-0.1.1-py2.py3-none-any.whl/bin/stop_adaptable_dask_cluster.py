#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This sample script will get deployed in the bin directory of the
users' virtualenv when the parent module is installed using pip.
"""

import argparse
import logging
import sys
import traceback
from pathlib import Path

from scheduler_tools.aics_prefect_daemon import AicsPrefectDaemon

###############################################################################

log = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)4s:%(lineno)4s %(asctime)s] %(message)s')

###############################################################################

###############################################################################


class Args(argparse.Namespace):

    DEFAULT_FIRST = 10
    DEFAULT_SECOND = 20

    def __init__(self):
        # Arguments that could be passed in through the command line
        self.first = self.DEFAULT_FIRST
        self.second = self.DEFAULT_SECOND
        self.debug = False
        #
        self.__parse()

    def __parse(self):
        pth = Path("~/.prefect").expanduser().resolve()
        p = argparse.ArgumentParser(prog='stop_adaptable_dask_cluster',
                                    description='shutdown the adaptable dask cluster daemon running for prefect')
        p.add_argument('-p', '--pidfile', help='where to lookup the pid', dest='pidfile', type=Path,
                       default=pth / "pidfile")
        p.add_argument('--debug', action='store_true', dest='debug', help=argparse.SUPPRESS)
        p.parse_args(namespace=self)


###############################################################################

def main():
    dbg = True
    try:
        args = Args()
        dbg = args.debug

        print("pid file => ", args.pidfile)
        daemon = AicsPrefectDaemon(pidfile=args.pidfile)
        daemon.stop()

    except Exception as e:
        log.error("=============================================")
        if dbg:
            log.error("\n\n" + traceback.format_exc())
            log.error("=============================================")
        log.error("\n\n" + str(e) + "\n")
        log.error("=============================================")
        sys.exit(1)


###############################################################################
# Allow caller to directly run this module (usually in development scenarios)


if __name__ == '__main__':
    main()
