import asyncio
import asyncssh
import sys
from pathlib import Path
import re
import logging
import subprocess


async def run_scp_copy_dask_prefs(filename: Path, server: str, key: Path, remote_folder: Path):
    print("remote_path: ", remote_folder)
    await asyncssh.scp(str(filename), (server, remote_folder),
                       client_keys=key)


async def run_launch_dask_head_node(gateway: str, key: Path, prefs: dict, saver, home_folder: Path):
    command1 = f"conda activate {prefs['remote_conf']['env']}"
    print(f"command1: {command1}")
    command2 = (f"sbatch -c {prefs['cluster_conf']['cores']} -p {prefs['cluster_conf']['queue']} "
                f"{prefs['remote_conf']['command']} {prefs['remote_conf']['env']} {home_folder}")
    print(f"command2: {command2}")
    command = command1 + ' ; ' + command2
    async with asyncssh.connect(gateway, client_keys=key) as conn:
        result = await conn.run(command, check=True)
        job_id_match = re.match(r'Submitted batch job (?P<JOB_ID>\d+)', result.stdout)
        if job_id_match:
            head_node_id = job_id_match.groupdict()["JOB_ID"]
            saver.write_prefect_job_id(head_node_id)
        else:
            logging.warning(f"Could not parse job_id:")
            logging.warning(f"\t{result.stdout}")


async def run_watch_and_report_ports(gateway: str, key: Path, rel_folder):
    pattern = re.compile(r"tcp://(?P<host>[\d\.]+):(?P<DASK_PORT>\d+)\s+(?P<DASHBOARD_PORT>\d+)$",
                               re.MULTILINE)
    rel_pidfile = rel_folder / "pidfile"
    rel_stdout = rel_folder / "stdout"
    command1 = f"while [ ! -s {rel_pidfile} ] ; do sleep 1; done \n"
    command2 = f"while [ ! -s {rel_stdout} ]; do sleep 1; done \n"
    command3 = f"cat {rel_stdout} \n"
    result = None
    async with asyncssh.connect(gateway, client_keys=key) as conn:
        await conn.run(command1, check=True)
        await conn.run(command2, check=True)
        result = await conn.run(command3, check=True)
        my_match = pattern.match(result.stdout)
        if my_match:
            result = my_match.groupdict()
        else:
            logging.warning(f"Regular expression couldn't parse ports from :")
            logging.warning(f"\t{result.stdout}")
    return result


async def shutdown_dask_head_node(gateway: str, key: Path, job_id: int, pidfile: Path):
    command = f"scancel {job_id}; rm {pidfile}\n"
    async with asyncssh.connect(gateway, client_keys=key) as conn:
        await conn.run(command, check=True)
