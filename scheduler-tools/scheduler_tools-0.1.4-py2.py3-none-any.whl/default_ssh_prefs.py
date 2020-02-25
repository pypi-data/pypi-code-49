from .types import PrefDict
from pathlib import Path
from os import uname


def default_ssh_prefs():
    ssh_prefs = PrefDict()
    ssh_prefs['localfolder'] = Path('~/.aics_dask').expanduser()
    ssh_prefs['gateway'] = {'url': 'slurm-master', 'user': uname(),
                            'identityfile': ssh_prefs['localfolder']/'.ssh/id_rsa'}
    ssh_prefs['dask_port'] = 34000
    ssh_prefs['dashboard_port'] = 8787
