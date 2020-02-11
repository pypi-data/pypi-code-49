from . import qsubr
import sys
import os
from subprocess import Popen, PIPE
import argparse
import getpass

def run_qsubr(args=None):
    parser = argparse.ArgumentParser('The missing qsub command')
    parser.add_argument('command', type=str, help='A quoted string of commands')
    parser.add_argument('--environment', '-e', type=str, default="SLURM", , choices=['SLURM', 'PBS'], help='job submission environment')
    parser.add_argument('--queue', '-q', type=str, default="workq", help='queue; PBS only')
    parser.add_argument('--account', '-A', type=str, default="sfurla", help='account_string; PBS only')
    parser.add_argument('--name', '-N', type=str, default="qsubr_job", help='name')
    parser.add_argument('--mem', '-m', type=int, default=8, help='memory in gigabytes per node')
    parser.add_argument('--nodes', '-n', type=int, default=1, help='nodes')
    parser.add_argument('--threads', '-t', type=int, default=4, help='threads per node')
    parser.add_argument('--partition', '-p', type=str, default='campus', help='partition; aka -p on slurm')
    parser.add_argument('--cluster', '-t', type=str, default='gizmo', help='cluster; aka -M on slurm')
    parser.add_argument('--log', '-l', type=str, default="log_out", help='log filename')
    parser.add_argument('--debug', '-d', action='store_true', help='To print commands (For testing flow). OPTIONAL')
    """
    call = 'qsubr "command"'
    args = parser.parse_args(call.split(" ")[1:])
    """
    args = parser.parse_args()
    qsubr_job = qsubr.make_script(command = args.command, partition=args.partition, cluster=args.cluster, environment = args.environment, threads = args.threads, nodes = args.nodes, mem = args.mem, name = args.name, debug=args.debug, cluster=args.cluster, log=args.log, user=args.account)
    qsubr_job.run_job()
