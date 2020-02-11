import asyncio
import json
import logging
import os
from pathlib import Path
import re
import subprocess
import sys

import asyncssh
import psutil

from scheduler_tools.PrefectPreferences import PrefectPreferences
from scheduler_tools.ScpDaskPrefs import run_scp_copy_dask_prefs, \
    run_launch_dask_head_node, run_watch_and_report_ports, shutdown_dask_head_node
from scheduler_tools.types import PathDict, PrefDict


class Connector:

    def __init__(self, distributed_dict: dict = None, prefs: PathDict = None):

        self._dask_scheduler_ip = None
        self._dask_scheduler_port = None
        self._dask_dashboard_port = None
        self._tunnel = None
        self._pattern = re.compile(r"tcp://(?P<host>[\d\.]+):(?P<DASK_PORT>\d+)\s+(?P<DASHBOARD_PORT>\d+)$",
                                   re.MULTILINE)

        if prefs is None:
            prefs = PrefDict()
            prefs['gateway']['url'] = 'slurm-machine.bettertech.com'
            prefs['gateway']['user'] = 'flanders'
            prefs['gateway']['identityfile'] = '~/.ssh/id_rsa'
            prefs['dask_port'] = 34009
            prefs['dashboard_port'] = 8787
            prefs['localfolder'] = '~/.aics_dask'
        elif isinstance(prefs, (Path, str)):
            localfolder = Path(prefs).parent
            if Path(prefs).expanduser().exists():
                with open(Path(prefs).expanduser(), 'r') as fp:
                    prefs = json.load(fp)
                print(f"localfolder: {localfolder}")
                if 'localfolder' not in prefs.keys():
                    prefs['localfolder'] = localfolder
            else:
                raise FileNotFoundError(f"{prefs} file does not exists.")
            print("survived elsif")
        print("in pref")
        self._pref = PrefectPreferences(prefs)
        print("from pref")

        if distributed_dict is None:
            dask_prefs = {}

            dask_prefs['cluster_conf'] = {}
            dask_prefs['cluster_conf']['queue'] = 'aics_cpu_general'
            dask_prefs['cluster_conf']['cores'] = 2
            dask_prefs['cluster_conf']['memory'] = '8GB'
            dask_prefs['cluster_conf']['walltime'] = "02:00:00"
            # dask_prefs['cluster_conf']['job_extra'] = ["--gres=gpu:v100:1"]

            dask_prefs['worker_conf'] = {}
            dask_prefs['worker_conf']['minimum_jobs'] = 2
            dask_prefs['worker_conf']['maximum_jobs'] = 40

            dask_prefs['remote_conf'] = {}
            dask_prefs['remote_conf']['env'] = 'dask_scheduler'
            dask_prefs['remote_conf']['command'] = 'setup_and_spawn.bash'
            dask_prefs['remote_conf']['path'] = str(self._pref.default_path())
            self._dask_prefs = dask_prefs
        else:
            self._dask_prefs = distributed_dict
        print("survived init")
        self.serialize_and_push_prefs()

    def serialize_and_push_prefs(self):
        # serialize the json prefs
        dask_prefs_path = self._pref.default_path().expanduser() / "dask_prefs.json"
        print(f"in serialize: {dask_prefs_path}")
        with open(str(dask_prefs_path), 'w') as fp:
            json.dump(self._dask_prefs, fp)
        # scp json to cluster
        try:
            relative_path = Path(self._dask_prefs['remote_conf']['path']).relative_to(Path().home())
            print(f"rel path: {relative_path}")
            asyncio.get_event_loop().run_until_complete(run_scp_copy_dask_prefs(dask_prefs_path,
                                                                                self._pref.gateway_url,
                                                                                self._pref.identity_file,
                                                                                relative_path))
        except (OSError, asyncssh.Error) as exc:
            sys.exit('SCP connection failed: ' + str(exc))

    def run_command(self):
        self.serialize_and_push_prefs()
        remote_home = self._pref.default_path().relative_to(Path().home())
        try:
            asyncio.get_event_loop().run_until_complete(run_launch_dask_head_node(self._pref.gateway_url,
                                                                                  self._pref.identity_file,
                                                                                  self._dask_prefs,
                                                                                  self._pref,
                                                                                  remote_home))
        except (OSError, asyncssh.Error) as exc:
            sys.exit('Launch dask cluster failed: ' + str(exc))

    def stop_forward_if_running(self, query=True):
        pid_str = self._pref.read_ssh_pid()
        # if there is no pid or the pid isn't valid return
        if pid_str is None or not psutil.pid_exists(int(pid_str)):
            self._pref.remove_ssh_pid()
            return
        # if the pid doesn't match the command issued
        ppid = psutil.Process(pid=int(pid_str))
        if not re.match(r'ssh.*', ppid.name()):
            self._pref.remove_ssh_pid()
            return
        children = ppid.children(recursive=True)
        if ppid and children:
            logging.info(f"Shutting down PID({ppid.pid}): {ppid.name()}")
            for child in children:
                logging.info(f"Shutting down PID({child.pid}): {child.name()}")
            remove = True
            if query:
                data = input("Shutdown the above processes? [YES/no]")
                pat = r'\s*(no|NO|No)\s*'
                remove = not re.match(pat, data)
            if remove:
                for child in children:
                    child.kill()
                ppid.kill()
        # remove the file
        self._pref.ssh_pid_path().unlink()

    def forward_ports(self):
        rel_folder = self._pref.default_path().relative_to(Path().home())
        info = asyncio.get_event_loop().run_until_complete(
            run_watch_and_report_ports(self._pref.gateway_url, self._pref.identity_file, rel_folder)
        )

        ssh_command = (f"ssh -o StrictHostKeyChecking=no -i {self._pref.identity_file} "
                       f"-N -A -J {self._pref.gateway_url} "
                       f"-L {self._pref.local_dask_port}:{info['host']}:{info['DASK_PORT']} "
                       f"-L {self._pref.local_dashboard_port}:{info['host']}:{info['DASHBOARD_PORT']} "
                       f"{self._pref.username}@{info['host']}"
                       )

        self._tunnel = subprocess.Popen(ssh_command, shell=True, executable='/bin/bash')
        os.environ['DASK_PORT'] = info['DASK_PORT']
        print(f"\nTo connect to remote server use \n\tDask:\t \t localhost:{self._pref.local_dask_port}\n"
              f"\tDashboard:\t localhost:{self._pref.local_dashboard_port}")
        self._pref.write_ssh_pid(pid=self._tunnel.pid)

    def stop_dask(self):
        job_id = self._pref.read_prefect_job_id()
        pidfile = self._pref.cluster_pid_path()
        if job_id is None:
            logging.warning("Job ID is None")
            return
        logging.info(f"Cancelling Slurm Head Node: {job_id}")
        asyncio.get_event_loop().run_until_complete(shutdown_dask_head_node(self._pref.gateway_url,
                                                                            self._pref.identity_file,
                                                                            job_id,
                                                                            pidfile))
        self.stop_forward_if_running(query=False)

