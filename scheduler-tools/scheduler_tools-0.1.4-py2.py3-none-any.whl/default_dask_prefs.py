from os import uname
from typing import Union


def default_dask_prefs(remote_user: Union[str, type(None)]):
    # in no remote user is provided assume the remote username is the same as the local one
    if remote_user is None:
        remote_user = uname()

    # setup the dictionary
    dask_prefs = {'cluster_obj_name': {}, 'cluster_conf': {}, 'worker_conf': {}, 'remote_conf': {}}

    # specify the command to specify the type of cluster to launch and the module in which it lives
    dask_prefs['cluster_obj_name'] = {'module': 'dask_jobqueue', 'object': 'SLURMCluster'}

    # dictionary of setting to pass to sbatch (to define host resources)
    dask_prefs['host_conf'] = {'queue': 'aics_cpu_general', 'cores': 2, 'memory': '8GB',
                                           'walltime': '02:00:00'}

    # specify the arguments to the SLURMCluster specified above
    dask_prefs['worker_conf'] = {'queue': 'aics_cpu_general', 'cores': 2, 'memory': '8GB',
                                           'walltime': '02:00:00'}

    # specify the worker parameters here
    dask_prefs['adapt_conf'] = {'minimum_jobs': 2, 'maximum_jobs': 40}

    # spicify the remote conda environment,
    # the remote command to fire (this shouldn't be changed),
    # the remote settings folder
    dask_prefs['remote_conf']['env'] = 'dask-scheduler'
    dask_prefs['remote_conf']['command'] = 'setup_and_spawn.bash'
    dask_prefs['remote_conf']['path'] = f"/home/{remote_user}/.aics_dask"

    return dask_prefs
