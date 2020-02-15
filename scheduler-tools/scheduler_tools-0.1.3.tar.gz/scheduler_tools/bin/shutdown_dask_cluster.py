import argparse
from scheduler_tools import Connector
import logging
import sys
import traceback

from pathlib import Path

###############################################################################

log = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)4s:%(lineno)4s %(asctime)s] %(message)s')

###############################################################################

###############################################################################


class Args(argparse.Namespace):

    def __init__(self):
        # Arguments that could be passed in through the command line
        self.debug = False
        #
        self.__parse()

    # cluster = SLURMCluster(cores=2, memory="8GB", walltime="01:00:00", queue="aics_cpu_general")
    # cluster.adapt(minimum_jobs=2, maximum_jobs=40)

    def __parse(self):
        pth = Path("~/.aics_dask").expanduser()
        p = argparse.ArgumentParser(prog='shutdown_dask_cluster',
                                    description='stop remote dask head node and shut down port forwards.')
        p.add_argument('-s', '--sshjson', help='json file with gateway, url, id, and identity file.', dest='sshjson',
                       type=Path, default=pth / "ssh.json")
        p.add_argument('--debug', action='store_true', dest='debug', help=argparse.SUPPRESS)
        p.parse_args(namespace=self)


###############################################################################

def main():
    dbg = True
    try:
        args = Args()
        dbg = args.debug

        conn = Connector(prefs=args.sshjson)
        conn.stop_dask()

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

