import abc
import ftplib
from pathlib import Path
import subprocess
import logging

import globus_sdk

from brainbox.core import Bunch
from ibllib.io.hashfile import md5
import alf.io
from ibllib.misc import version

_logger = logging.getLogger('ibllib')

FLATIRON_HOST = 'ibl.flatironinstitute.org'
FLATIRON_PORT = 61022
FLATIRON_USER = 'datauser'
FLATIRON_MOUNT = '/mnt/ibl'
FTP_HOST = 'test.alyx.internationalbrainlab.org'
FTP_PORT = 21


def _run_command(cmd, dry=True):
    _logger.info(cmd)
    if dry:
        return 0, '', ''
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    info, error = p.communicate()
    if p.returncode != 0:
        _logger.error(error)
        raise RuntimeError(error)
    return p.returncode, info, error


class Patcher(abc.ABC):
    def __init__(self, one=None):
        # one object
        if one is None:
            self.one = one.ONE()
        else:
            self.one = one

    def patch_dataset(self, path, dset_id=None, dry=False):
        """
        Uploads a dataset from an arbitrary location to FlatIron.
        :param path:
        :param dset_id:
        :param dry:
        :return:
        """
        status = self._patch_dataset(path, dset_id=dset_id, dry=dry)
        if not dry and status == 0:
            self.one.alyx.rest('datasets', 'partial_update', id=dset_id,
                               data={'hash': md5(path),
                                     'file_size': path.stat().st_size,
                                     'version': version.ibllib()}
                               )

    def _patch_dataset(self, path, dset_id=None, dry=False):
        """
        Private method that skips
        """
        path = Path(path)
        if dset_id is None:
            dset_id = path.name.split('.')[-2]
            if not alf.io.is_uuid_string(dset_id):
                dset_id = None
        assert dset_id
        assert alf.io.is_uuid_string(dset_id)
        assert path.exists()
        dset = self.one.alyx.rest('datasets', "read", id=dset_id)
        fr = next(fr for fr in dset['file_records'] if 'flatiron' in fr['data_repository'])
        remote_path = Path(fr['data_repository_path']).joinpath(fr['relative_path'])
        remote_path = alf.io.add_uuid_string(remote_path, dset_id)
        if remote_path.is_absolute():
            remote_path = remote_path.relative_to(remote_path.root)
        status = self._scp(path, Path(FLATIRON_MOUNT) / remote_path, dry=dry)[0]
        return status

    def register_dataset(self, file_list, created_by='root', server_repository=None, dry=False):
        """
        Registers a set of files belonging to a session only on the server
        :param session_path:
        :param filenames:
        :param created_by:
        :param server_repository:
        :param dry:
        :return:
        """
        if not isinstance(file_list, list):
            file_list = [Path(file_list)]
        assert len(set([alf.io.get_session_path(f) for f in file_list])) == 1
        assert all([Path(f).exists() for f in file_list])
        session_path = alf.io.get_session_path(file_list[0])
        # first register the file
        r = {'created_by': created_by,
             'path': str(session_path.relative_to((session_path.parents[2]))),
             'filenames': [str(p.relative_to(session_path)) for p in file_list],
             'name': server_repository,
             'server_only': True,
             'hashes': [md5(p) for p in file_list],
             'filesizes': [p.stat().st_size for p in file_list],
             'versions': [version.ibllib() for _ in file_list]}
        if not dry:
            return self.one.alyx.rest('register-file', 'create', data=r)
        else:
            print(r)

    def create_dataset(self, file_list, server_repository=None, created_by='root', dry=False):
        """
        Creates a new dataset on FlatIron and uploads it from arbitrary location.
        Rules for creation/patching are the same that apply for registration via Alyx
        as this uses the registration endpoint to get the dataset.
        An existing file (same session and path relative to session) will be patched.
        :param path: full file path. Must be whithin an ALF session folder (subject/date/number)
        can also be a list of full file pathes belonging to the same session.
        :param server_repository: Alyx server repository name
        :param created_by: alyx username for the dataset (optional, defaults to root)
        :return:
        """
        # first register the file
        if not isinstance(file_list, list):
            file_list = [Path(file_list)]
        assert len(set([alf.io.get_session_path(f) for f in file_list])) == 1
        assert all([Path(f).exists() for f in file_list])
        datasets = self.register_dataset(file_list, created_by=created_by,
                                         server_repository=server_repository, dry=dry)
        if dry:
            return
        # from the dataset info, set flatIron flag to exists=True
        for p, d in zip(file_list, datasets):
            self._patch_dataset(p, dset_id=d['id'], dry=dry)

    def delete_dataset(self, dset_id, dry=False):
        dset = self.one.alyx.rest('datasets', "read", id=dset_id)
        assert dset
        for fr in dset['file_records']:
            if 'flatiron' in fr['data_repository']:
                flatiron_path = Path(FLATIRON_MOUNT).joinpath(fr['data_repository_path'][1:],
                                                              fr['relative_path'])
                flatiron_path = alf.io.add_uuid_string(flatiron_path, dset_id)
                status = self._rm(flatiron_path, dry=dry)[0]
                if status == 0:
                    self.one.alyx.rest('datasets', 'delete', id=dset_id)

    def delete_session_datasets(self, eid, dry=True):
        """
            Deletes all datasets attached to the session from database and flatiron but leaves
            the session on the database.
            Useful for a full re-extraction
        """
        ses_details = self.one.alyx.rest('sessions', 'read', id=eid)
        raise NotImplementedError("Code below only removes existing files. Need to search"
                                  "for datasets in a better way")
        # first delete attached datasets from the database
        dataset_details = self.one.list(eid, details=True)
        for n in range(len(dataset_details.dataset_id)):
            print(dataset_details.dataset_id[n])
            if dry:
                continue
            try:
                self.one.alyx.rest('datasets', 'delete', id=dataset_details.dataset_id[n])
            except Exception as e:
                print(e)

        # then delete the session folder from flatiron
        flatiron_path = Path(FLATIRON_MOUNT).joinpath(ses_details['lab'],
                                                      'Subjects',
                                                      ses_details['subject'],
                                                      ses_details['start_time'][:10],
                                                      str(ses_details['number']).zfill(3))

        cmd = f"ssh -p {FLATIRON_PORT} {FLATIRON_USER}@{FLATIRON_HOST} rm -fR {flatiron_path}"
        print(cmd)

    @abc.abstractmethod
    def _scp(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def _rm(self, *args, **kwargs):
        pass


class GlobusPatcher(Patcher):
    """
    Requires GLOBUS keys access
    """

    def __init__(self, one=None, globus_transfer=None, globus_delete=None):
        # handles the globus objects
        self.globus_transfer = globus_transfer
        self.globus_delete = globus_delete
        if globus_transfer is None:
            self.globus_transfer = Bunch({'path_src': [], 'path_dest': []})
        if globus_delete is None:
            self.globus_delete = Bunch({'path': []})
        super().__init__(one=one)

    def _scp(self, local_path, remote_path, dry=True):
        remote_path = Path('/').joinpath(remote_path.relative_to(Path(FLATIRON_MOUNT)))
        _logger.info(f"Globus copy {local_path} to {remote_path}")
        if not dry:
            if isinstance(self.globus_transfer, globus_sdk.transfer.data.TransferData):
                self.globus_transfer.add_item(local_path, remote_path)
            else:
                self.globus_transfer.path_src.append(local_path)
                self.globus_transfer.path_dest.append(remote_path)
        return 0, ''

    def _rm(self, flatiron_path, dry=True):
        flatiron_path = Path('/').joinpath(flatiron_path.relative_to(Path(FLATIRON_MOUNT)))
        _logger.info(f"Globus del {flatiron_path}")
        if not dry:
            if isinstance(self.globus_delete, globus_sdk.transfer.data.DeleteData):
                self.globus_delete.add_item(flatiron_path)
            else:
                self.globus_delete.path.append(flatiron_path)
        return 0, ''

    def launch_transfers(self, globus_transfer_client, wait=True):
        gtc = globus_transfer_client

        def _wait_for_task(resp):
            if wait:
                status = gtc.task_wait(task_id=resp['task_id'], timeout=1)
                while gtc.get_task(task_id=resp['task_id'])['nice_status'] == 'OK':
                    status = gtc.task_wait(task_id=resp['task_id'], timeout=30)
                if status is False:
                    tinfo = gtc.get_task(task_id=resp['task_id'])['nice_status']
                    raise ConnectionError(f"Could not connect to Globus {tinfo}")

        # handles the transfers first
        if len(self.globus_transfer['DATA']) > 0:
            # launch the transfer
            _wait_for_task(gtc.submit_transfer(self.globus_transfer))
            # re-initialize the globus_transfer property
            self.globus_transfer = globus_sdk.TransferData(
                gtc,
                self.globus_transfer['source_endpoint'],
                self.globus_transfer['destination_endpoint'],
                label=self.globus_transfer['label'],
                verify_checksum=True, sync_level='checksum')

        # do the same for deletes
        if len(self.globus_delete['DATA']) > 0:
            _wait_for_task(gtc.submit_delete(self.globus_delete))
            self.globus_delete = globus_sdk.DeleteData(
                gtc,
                endpoint=self.globus_delete['endpoint'],
                label=self.globus_delete['label'],
                verify_checksum=True, sync_level='checksum')


class SSHPatcher(Patcher):
    """
    Requires SSH keys access on the FlatIron
    """
    def __init__(self, one=None, globus_client=None):
        res = _run_command(f"ssh -p {FLATIRON_PORT} {FLATIRON_USER}@{FLATIRON_HOST} ls")
        if res[0] != 0:
            raise PermissionError("Could not connect to the Flatiron via SSH. Check your RSA keys")
        super().__init__(one=one)

    def _scp(self, local_path, remote_path, dry=True):
        cmd = f"ssh -p {FLATIRON_PORT} {FLATIRON_USER}@{FLATIRON_HOST}" \
              f" mkdir -p {remote_path.parent}; "
        cmd += f"scp -P {FLATIRON_PORT} {local_path} {FLATIRON_USER}@{FLATIRON_HOST}:{remote_path}"
        return _run_command(cmd, dry=dry)

    def _rm(self, flatiron_path, dry=True):
        cmd = f"ssh -p {FLATIRON_PORT} {FLATIRON_USER}@{FLATIRON_HOST} rm {flatiron_path}"
        return _run_command(cmd, dry=dry)


class FTPPatcher(Patcher):
    """
    This is used to register from anywhere without write access to FlatIron
    """
    def __init__(self, one=None, globus_client=None):
        super().__init__(one=one)
        self.ftp = ftplib.FTP_TLS(host=FTP_HOST,
                                  user=one._par.FTP_DATA_SERVER_LOGIN,
                                  passwd=one._par.FTP_DATA_SERVER_PWD)
        # self.ftp.ssl_version = ssl.PROTOCOL_TLSv1
        # self.ftp.auth()
        self.ftp.prot_p()
        self.ftp.login(one._par.FTP_DATA_SERVER_LOGIN, one._par.FTP_DATA_SERVER_PWD)

    def create_dataset(self, path, created_by='root', dry=False, **kwargs):
        # overrides the superclass just to remove the server repository argument
        super().create_dataset(path, created_by=created_by, dry=dry)

    def _scp(self, local_path, remote_path, dry=True):
        # remote_path = '/mnt/ibl/zadorlab/Subjects/flowers/2018-07-13/001
        remote_path = Path(Path(FLATIRON_MOUNT).root).joinpath(
            remote_path.relative_to(FLATIRON_MOUNT))
        # local_path
        # remote_path.parent
        self.mktree(remote_path.parent)
        self.ftp.pwd()
        with open(local_path, 'rb') as fid:
            self.ftp.storbinary(f'STOR {local_path.name}', fid)
        return 0, ''

    def mktree(self, remote_path):
        """ Browse to the tree on the ftp server, making directories on the way"""
        if str(remote_path) != '.':
            try:
                self.ftp.cwd(str(remote_path))
            except ftplib.all_errors:
                self.cdtree(Path(remote_path.parent))
                self.ftp.mkd(str(remote_path))
                self.ftp.cwd(str(remote_path))

    def _rm(self, flatiron_path, dry=True):
        raise PermissionError("This Patcher does not have admin permissions to remove data "
                              "from the FlatIron server. ")
