import pytest
from pathlib import Path
from scheduler_tools.connector import Connector
import asyncssh
import asyncio
from scheduler_tools.ScpDaskPrefs import run_launch_dask_head_node


class MockSaver(object):
    def write_prefect_job_id(self, job_id):
        print(f"mock saver asked to save cluster_job_id: {job_id}")


# test user name
def test_constructor():
    ctr = Connector()


async def remote_spawn():
    command = "sbatch -o ~/.aics_dask_gpu/sOut -e ~/.aics_dask_gpu/sErr -c 2 -p aics_gpu_general setup_and_spawn.bash dask_gpu ~/.aics_dask_gpu\n"
    command2 = "conda activate dask_gpu; echo 'Yes this seems to have executed'"
    async with asyncssh.connect('slurm-master.corp.alleninstitute.org',
                                client_keys=Path('/Users/jamies/Dropbox/SSH/AICS/privateKeys/jamiesAICS')) as conn:
        result = await conn.run(command, check=True)
        print(result)


def test_remote_spawn():
    asyncio.get_event_loop().run_until_complete(remote_spawn())


def test_remote_spawn_func():
    mock_saver = MockSaver()
    prefs = {
             'cores': 2,
             'queue': 'aics_gpu_general',
             'remote_env': 'dask_gpu',
             'remote_command': 'setup_and_spawn.bash'
             }
    print("sbatch -c 2 -p aics_gpu_general setup_and_spawn.bash dask_gpu ~/.aics_dask_gpu")
    asyncio.get_event_loop().run_until_complete(run_launch_dask_head_node('slurm-master.corp.alleninstitute.org',
                                                                          Path('/Users/jamies/Dropbox/SSH/AICS/privateKeys/jamiesAICS'),
                                                                          prefs,
                                                                          mock_saver,
                                                                          Path('.aics_dask_gpu')
                                                                          ))


def test_connect():
    ctr = Connector()
    ctr.create_connection(passphrase="")
    ctr.serialize_and_push_prefs()
    print("yes")




