import argparse
from scheduler_tools import Connector
from scheduler_tools.types import PrefDict
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
        p = argparse.ArgumentParser(prog='spawn_adaptable_dask_cluster',
                                    description='launch a daemon to keep an adaptable dask cluster running for prefect')
        p.add_argument('-s', '--sshjson', help='json file with gateway, url, id, and identity file.', dest='sshjson',
                       type=Path, default=pth/"ssh.json")
        p.add_argument('-q', '--queue', dest='queue', type=str, default='aics_cpu_general',
                       help='The queue to use on the cluster {aics_cpu_general, aics_gpu_general, etc}.')

        p.add_argument('-c', '--cores', dest='cores', type=int, default=2,
                       help='number of cores to give each worker')
        p.add_argument('-g', '--memoryGB', dest='memory', type=int, default=8,
                       help='The amount of memory to request for each worker.')
        p.add_argument('-w', '--walltime', dest='walltime', type=str, default="02:00:00",
                       help='wall time for the worker nodes.')
        p.add_argument('-m', '--minimum_workers', dest='minworkers', type=int, default=2,
                       help='minimum number of workers to spin up.')
        p.add_argument('-x', '--maximum_workers', dest='maxworkers', type=int, default=40,
                       help='maximum number of workers to spin up.')
        p.add_argument('-r', '--remote_env', dest='remoteenv', type=str, default="dask-scheduler",
                       help='name of the remote environment to activate')
        p.add_argument('--debug', action='store_true', dest='debug', help=argparse.SUPPRESS)
        p.parse_args(namespace=self)


###############################################################################

def main():
    dbg = True
    try:
        args = Args()
        dbg = args.debug

        dask_prefs = {'cluster_conf': {}, 'worker_conf': {}, 'remote_conf':{}}
        dask_prefs['cluster_conf']['queue'] = args.queue
        dask_prefs['cluster_conf']['cores'] = args.cores
        dask_prefs['cluster_conf']['memory'] = str(args.memory) + 'GB'
        dask_prefs['cluster_conf']['walltime'] = args.walltime
        dask_prefs['worker_conf']['minimum_jobs'] = args.minworkers
        dask_prefs['worker_conf']['maximum_jobs'] = args.maxworkers
        dask_prefs['remote_conf']['env'] = args.remoteenv
        dask_prefs['remote_conf']['command'] = 'setup_and_spawn.bash'
        dask_prefs['remote_conf']['path'] = str(args.sshjson.parent.relative_to(Path().home()))
        ssh_info = args.sshjson

        conn = Connector(distributed_dict=dask_prefs, prefs=ssh_info)
        conn.run_command()
        conn.stop_forward_if_running()
        conn.forward_ports()

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

