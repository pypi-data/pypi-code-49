from pathlib import Path
from scheduler_tools.types import PrefDict


class PrefectPreferences:
    """
    This class handles reading of a ~/.prefect/ssh.json file. This file has settings for the
    name of the gateway, the username to authenticate with, the path to the local ssh identity
    file.
    """

    def __init__(self, prefs: PrefDict):
        """

        :param prefs:
        """
        print(prefs)
        p_localfolder = Path(prefs['localfolder'])
        print("1: ")
        if not p_localfolder.exists():
            p_localfolder.mkdir(parents=True)

        print("2: ")
        self._path = p_localfolder

        print("3: ")
        self._data = prefs

    def default_path(self) -> Path:
        return self._path

    @property
    def gateway_url(self):
        return self._data['gateway']['url']

    @property
    def username(self):
        return self._data['gateway']['user']

    @property
    def identity_file(self):
        return self._data['gateway']['identityfile']

    @property
    def known_hosts(self):
        return Path('~/.ssh/known_hosts').expanduser()

    def write_ssh_pid(self, pid):
        with open(str(self.ssh_pid_path()), 'w') as fp:
            fp.write(str(pid))

    def read_ssh_pid(self) -> [str, type(None)]:
        pid = None
        if self.ssh_pid_path().expanduser().exists():
            pid = open(str(self.ssh_pid_path().expanduser()), 'r').read()
        return pid

    def remove_ssh_pid(self):
        if self.ssh_pid_path().exists():
            self.ssh_pid_path().unlink()

    def ssh_pid_path(self):
        return self.default_path().expanduser() / "ssh_pid.txt"

    def cluster_job_id_path(self):
        return self.default_path().expanduser() / "cluster_job_id.txt"

    def read_prefect_job_id(self) -> [str, type(None)]:
        job_id = None
        if self.cluster_job_id_path().exists():
            job_id = open(str(self.cluster_job_id_path().expanduser()), 'r').read()
        return job_id

    def write_prefect_job_id(self, job_id):
        print(f"jobid: {job_id}")
        with open(str(self.cluster_job_id_path().expanduser()), 'w') as fp:
            fp.write(str(job_id))

    def remove_prefect_job_id(self):
        if self.cluster_job_id_path().exists():
            self.cluster_job_id_path().unlink()

    def cluster_pid_path(self):
        # this needs to be made dynamic
        return self.default_path().relative_to(Path().home()) / "pidfile"

    @property
    def local_dask_port(self):
        return self._data['dask_port']

    @property
    def local_dashboard_port(self):
        return self._data['dashboard_port']
