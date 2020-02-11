
from datetime import datetime
import os
import shutil
import subprocess
import uuid

from logging import getLogger
from glob import glob
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

import requests
import virtualenv

from filelock import FileLock
from celery.utils.log import get_task_logger

from worker.utils import is_windows

log = get_task_logger(__name__)

def fileset(directory):
    files = []
    for dirpath, _, filelist in os.walk(directory):
        for filename in filelist:
            files.append(os.path.relpath(os.path.join(dirpath, filename), directory))
    return files

class PackInstallation:
    def __init__(self, pack_identifier, njinn_api):
        self.pack_namespace, self.pack_name = pack_identifier.split('.')
        self.qualified_name = f"{self.pack_namespace}/{self.pack_name}"
        self.njinn_api = njinn_api
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.target_path = f"{self.base_path}/packs/{self.qualified_name}"
        self.venv_path = f"{self.base_path}/venv/{self.qualified_name}"
        self.display_name = self.qualified_name
        self.status = f"Pack {self.display_name} not set up."
        self.bundle_status_file_name = None

    @staticmethod
    def identifier_from_status_filename(status_filename):
        dirname = Path(status_filename).parent
        pack_name = dirname.name
        pack_namespace = dirname.parent.name
        return f"{pack_namespace}.{pack_name}"

    def get_metadata(self):
        pack_api = '/api/v1/workercom/packs/' + self.qualified_name
        response = self.njinn_api.get(pack_api)

        if response.status_code != requests.codes.ok:
            raise Exception(
                f"Problem trying to get {pack_api}. API responded with ({response.status_code}): {response.text}")
        self.metadata = response.json()
        if 'version_identifier' in self.metadata and len(self.metadata['version_identifier']):
            self.version_identifier = self.metadata['version_identifier']
            self.bundle_status_base_path = f"{self.base_path}/bundle_status/{self.qualified_name}"
            self.bundle_status_file_name = f"{self.bundle_status_base_path}/{self.version_identifier}-log.txt"
            if 'title' in self.metadata:
                self.display_name = f"{self.qualified_name} ({self.metadata['title']})"
        log.debug("%s: Downloaded metadata.", self.display_name)
    
    def download_pack_zip(self, temp_zip_name):
        log.debug("%s: Downloading version %s from API.", self.display_name, self.version_identifier)
        pack_bundle_url = f"/api/v1/workercom/packs/{self.qualified_name}/bundle"
        response = self.njinn_api.get(pack_bundle_url)
        if response.status_code != requests.codes.ok:
            raise Exception(
                f"Problem trying to get {pack_bundle_url}. API responded with ({response.status_code}): {response.text}")
        log.info("%s: Downloaded version %s from API.", self.display_name, self.version_identifier)
        with open(temp_zip_name, 'wb') as f:
                    f.write(response.content)

    def sync_target_from_zip(self, temp_zip_name):
        """ 
        Sync self.target_path with the zipfile and create/update environment according to its contents
        
        Return true if self.target_path was updated, false if it was created.
        """

        # Create self.target_path if required
        update = False
        if os.path.exists(self.target_path):
            update = True
        else:
            os.makedirs(self.target_path)
        
        # Attempt installation.
        # Remove self.target_path after failed initial installation, since we use its existence
        # to determine whether to create a new environment or update an existing one.
        try:
            with TemporaryDirectory() as temp_dir:
                with ZipFile(temp_zip_name) as zip_file:
                    zip_file.extractall(path=temp_dir)
                    source_files = fileset(temp_dir)
                    target_files = fileset(self.target_path)
                    for filename in source_files:
                        log.info("%s: Copying %s", self.display_name, filename)
                        target_filename = os.path.join(self.target_path, filename)
                        os.makedirs(os.path.dirname(target_filename), exist_ok=True)
                        shutil.move(os.path.join(temp_dir, filename), target_filename)
                    for filename in [f for f in target_files if not f in source_files]:
                        log.info("%s: Removing %s which does not exist in bundled version of action.", self.display_name, filename)
                        os.remove(os.path.join(self.target_path, filename))
            if not update:
                self.on_clone()
            else:
                self.on_change()
        except Exception as e:
            log.warning("Error during pack installation: %s", e)
            if not update and os.path.exists(self.target_path):
                log.info("%s Cleaning up %s after failed initial installation.", self.display_name, self.target_path)
                try:
                    shutil.rmtree(self.target_path)
                except Exception as e:
                    log.warning("%s Failed to clean up %s after failed installation: %s", self.display_name, self.target_path, e)
            raise e
        return update

    def on_bundle_setup_success(self):
        """ Writes new and removes old status files from the bundle directory """
        os.makedirs(self.bundle_status_base_path, exist_ok=True)
        with open(self.bundle_status_file_name, "wt") as status_file:
            status_file.write(f"Installed {datetime.now()}")

        for some_bundle_status_file in glob(f"{self.bundle_status_base_path}/*"):
            if os.path.normpath(self.bundle_status_file_name) != os.path.normpath(some_bundle_status_file):
                log.info("Removing old status file %s", some_bundle_status_file)
                try:
                    os.remove(some_bundle_status_file)
                except Exception as e:
                    log.warning("Failed to delete %s: %s", some_bundle_status_file, e)


    def get_pack_from_api(self):
        """ Install/update the pack from the API """
        # skip if already finished successfully, determined by whether the status file exists
        if os.path.isfile(self.bundle_status_file_name):
            with open(self.bundle_status_file_name, "rt") as status_file:
                status_text = status_file.read()
            log.debug("%s: bundle is up to date: %s", self.display_name, status_text)
            self.status = f"Pack {self.display_name} using version identifier {self.version_identifier} ({status_text}) provided by API."
            return

        # save to a temporary directory and install
        with TemporaryDirectory() as temp_dir:
            temp_zip_name = f"{temp_dir}/temp.zip"
            self.download_pack_zip(temp_zip_name)
            update = self.sync_target_from_zip(temp_zip_name)

        self.on_bundle_setup_success()
        
        self.status = f"Pack {self.display_name} {'updated' if update else 'set up'} based on version identifier {self.version_identifier} provided by API."
        log.info(self.status)

    def on_change(self):
        self.install_requirements()

    def on_clone(self):
        log.debug("%s: Creating venv in %s.", self.display_name, self.venv_path)
        virtualenv.create_environment(self.venv_path, clear=True)
        
        self.install_requests_jwt_and_cryptography()
        self.install_requirements()

    def get_version_identifier_from_repo(self, repo):
        try:
            self.version_identifier = repo.active_branch.commit.hexsha
        except Exception as e:
            log.warning("Error getting version identifier from repo: %s", e)

    def clone_repository(self):
        """
        Clone repository from pack repository url to the 'repository_path' path.
        """
        import git
        repository_url = self.metadata['repository']
        branch = self.metadata['branch']
        log.debug("%s: Cloning branch %s from %s into %s",
                self.display_name, branch, repository_url, self.target_path)

        repo = git.Repo.clone_from(repository_url, self.target_path, branch=branch)
        self.on_clone()
        self.get_version_identifier_from_repo(repo)
        self.status = f"Pack {self.display_name} set up based on commit hash {self.version_identifier or 'UNKNOWN'} from git repository {repository_url}."
    


    def update_repository(self):
        """
        Update the repository at 'repository_path' from remote pack repository.
        """
        import git
        log.info("%s: Updating repo %s.", self.display_name, self.target_path)
        pack_branch = self.metadata['branch']
        repository_url = self.metadata['repository']

        repo = git.Repo(self.target_path)

        if repo.active_branch is not pack_branch:
            repo.git.checkout(pack_branch)

        origin = repo.remotes.origin
        origin.fetch()

        commits_behind = list(repo.iter_commits(
            f'{pack_branch}..origin/{pack_branch}'))
        commits_ahead = list(repo.iter_commits(
            f'origin/{pack_branch}..{pack_branch}'))
        
        if repo.is_dirty() or commits_behind or commits_ahead:
            log.info("Updating  repo %s", self.target_path)
            repo.git.reset('--hard', f'origin/{pack_branch}')
            self.on_change()
            self.get_version_identifier_from_repo(repo)
            self.status = f"Pack {self.display_name} updated based on commit hash {self.version_identifier or 'UNKNOWN'} from git repository {repository_url}."
        else:
            log.debug("Nothing to do in repo %s", self.target_path)
            self.get_version_identifier_from_repo(repo)
            self.status = f"Pack {self.display_name} using commit hash {self.version_identifier or 'UNKNOWN'} from git repository {repository_url}."
    
    def setup(self):
        self.get_metadata()
        log.info("%s: Setting up inside: %s", self.display_name, self.target_path)
        lock_name = self.qualified_name.replace("/", ".") + ".lock"
        log.debug("%s: Locking %s", self.display_name, lock_name)
        with FileLock(lock_name):
            if self.bundle_status_file_name:
                log.debug("%s: Using version %s provided by API.", self.display_name, self.version_identifier)
                self.get_pack_from_api()
            elif not os.path.isdir(self.target_path):
                log.debug("%s: No version available from API and path %s doesn't exist, cloning git repository.", 
                     self.display_name, self.target_path)
                self.clone_repository()
            else:
                log.debug("%s: No version available from API and path %s already exists, updating git repository.",
                        self.display_name, self.target_path)
                self.update_repository()

    def run_pip(self, pip_argline, log=log):
        """
        Runs pip in a cross-platform way
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        command = 'pip ' + pip_argline
        log.info("%s: Running %s", self.display_name, command)
        # shell=True is needed for env to work on Windows
        result = subprocess.run(
            command,
            universal_newlines=True,
            cwd=dir_path,
            stderr=subprocess.STDOUT,
            shell=True,
            env=self.virtualenv_env()
        )
        result.check_returncode()
                


    def install_requests_jwt_and_cryptography(self, log=log):
        """
        Install ``requests_jwt`` and ``cryptography`` packages.
        """

        log.info("%s: Installing default dependencies.", self.display_name)
        self.run_pip('install "requests_jwt >=0.5, <0.6" "cryptography >=2.8, <=2.9"', log=log)


    def install_requirements(self):
        """
        Install requirements if 'requirements.txt' file is provided. 
        """
        
        log.info("%s: Installing package specific dependencies.", self.display_name)
        requirements_path = (Path(self.target_path) / "requirements.txt").resolve()

        if os.path.exists(requirements_path):
            self.run_pip(f'install -r "{requirements_path}"')
        else:
            log.warning("Requirements file %s doesn't exist", requirements_path)
    
    def virtualenv_env(self):
        """
        Creates a copy of the current system environment variables modified for
        running commands inside this pack's virtualenv, mimicking what the
        activate scripts do.
        """

        # if already in a virtualenv, this is set to the original PATH by activate - use this.
        old_path = os.environ.get('_OLD_VIRTUAL_PATH', os.environ['PATH'])
        if is_windows():
            # https://virtualenv.pypa.io/en/latest/userguide/#windows-notes
            binary_dir = 'Scripts'
            # https://en.wikipedia.org/wiki/PATH_(variable)#DOS,_OS/2,_and_Windows
            path_sep = ';'
        else:
            binary_dir = 'bin'
            path_sep = ':'
        virtualenv_bin_dir = (Path(self.venv_path) / binary_dir).resolve()
        # Fail instead of accidentally messing with parent environment.
        assert virtualenv_bin_dir.exists(), (
                f"Pack installation in unexpected state - virtualenv bin directory does not exist: {virtualenv_bin_dir}", 
            )
        new_path = f'{str(virtualenv_bin_dir)}{path_sep}{old_path}'
        env_copy = os.environ.copy()
        # play nice with existing virtualenvs, see comment above
        env_copy['_OLD_VIRTUAL_PATH'] = old_path
        env_copy['PATH'] = new_path
        return env_copy