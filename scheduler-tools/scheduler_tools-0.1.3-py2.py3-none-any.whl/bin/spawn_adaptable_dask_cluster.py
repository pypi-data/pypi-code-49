#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This sample script will get deployed in the bin directory of the
users' virtualenv when the parent module is installed using pip.
"""

import argparse
import json
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
        p = argparse.ArgumentParser(prog='spawn_adaptable_dask_cluster',
                                    description='launch a daemon to keep an adaptable dask cluster running for prefect')
        p.add_argument('-m', '--home_folder', help="folder where control and logging files are written.",
                       type=Path, dest='home', default=Path("~/.aics_dask").expanduser())
        p.add_argument('--debug', action='store_true', dest='debug', help=argparse.SUPPRESS)
        p.parse_args(namespace=self)


###############################################################################

def main():
    dbg = True
    try:
        args = Args()
        dbg = args.debug

        if not args.home.exists():
            args.home.mkdir()

        with open(args.home / "dask_prefs.json", 'r') as fp:
            slurm_prefs = json.load(fp)

        daemon = AicsPrefectDaemon(slurm_prefs=slurm_prefs,
                                   pidfile=args.home / "pidfile",
                                   stdin=args.home / "stdin",
                                   stdout=args.home / "stdout",
                                   stderr=args.home / "stderr",
                                   foreground=True
                                   )
        daemon.start()

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
