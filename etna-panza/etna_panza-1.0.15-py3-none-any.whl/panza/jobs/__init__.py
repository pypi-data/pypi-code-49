"""
Module providing helpers to manipulate jobs
"""
import os
import shutil
from typing import Dict, Any
import quixote
from quixote.build import GeneratorType
import panza.build
from panza import BlueprintLoadError
from panza.config import get_config
from textwrap import dedent
from subprocess import Popen, run, DEVNULL, PIPE, STDOUT
import tempfile
import logging
import json

_logger = logging.getLogger("panza-jobs")
_logger.setLevel(logging.DEBUG)


def add_logger_handler(handler):
    """
    Add a handler to the logger

    :param handler:             the handler to add
    """
    _logger.addHandler(handler)


class WorkspaceCreationError(Exception):
    """
    Exception class representing an error related to creating a workspace for a job
    """

    def __init__(self, cause: Exception):
        self.__cause__ = cause

    def __str__(self):
        if isinstance(self.__cause__, OSError):
            return f"cannot create workspace: {self.__cause__.strerror}: {self.__cause__.filename}"
        else:
            return f"cannot create workspace: {str(self.__cause__)}"


class EnvironmentBuildError(Exception):
    """
    Exception class representing an error related to the construction of an environment
    """

    def __init__(self, cause: Exception):
        self.__cause__ = cause

    def __str__(self):
        return f"cannot build environment: {str(self.__cause__)}"


class DataFetchingError(Exception):
    """
    Exception class representing an error related to the fetching of data needed by the job
    """

    def __init__(self, cause):
        self.__cause__ = cause

    def __str__(self):
        return f"cannot fetch data to analyze: {str(self.__cause__)}"


class _DockerDaemonSetupError(Exception):
    """
    Exception class representing an error related to the setup of the additional Docker daemon
    """

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"cannot setup the additional docker daemon: {self.message}"


class JobExecutionError(Exception):
    """
    Exception class representing an error related to the execution of the inspection phase of the job
    """

    def __init__(self, cause):
        self.__cause__ = cause

    def __str__(self):
        return f"cannot complete inspection phase: {str(self.__cause__)}"


class _DockerDaemon:
    def __init__(self):
        self.dockerd = None
        self.root_dir = tempfile.TemporaryDirectory(prefix="panza_").name
        self.network_brige_name = os.path.basename(self.root_dir).replace('_', '-')

    def launch(self, bridge_ip: str):
        script = dedent(
            f"""
            set -e

            ip link add name {self.network_brige_name} type bridge
            ip addr add {bridge_ip} dev {self.network_brige_name}
            ip link set dev {self.network_brige_name} up
            """
        )
        result = run(["bash", "-c", script], capture_output=True)
        if result.returncode != 0:
            raise _DockerDaemonSetupError(f"cannot configure a network bridge: {result.stderr.decode()}")
        command = dedent(
            f"""
            dockerd \
              --bridge={self.network_brige_name} \
              --data-root={self.root_dir}/data \
              --exec-root={self.root_dir}/exec \
              --host=unix://{self.root_dir}/docker.sock \
              --pidfile={self.root_dir}/docker.pid
              """
        )
        self.dockerd = Popen(["bash", "-c", command], stdout=DEVNULL, stderr=DEVNULL)

    def stop(self):
        if self.dockerd is not None:
            self.dockerd.terminate()
            self.dockerd.wait()
            shutil.rmtree(self.root_dir)
            os.system(f"ip link set {self.network_brige_name} down")
            os.system(f"ip link delete {self.network_brige_name}")

    def socket_path(self) -> str:
        return f"{self.root_dir}/docker.sock"


class JobExitStatus:
    """
    Class representing the exit status of a job
    """

    SUCCESS = 0
    FAILURE = 1

    def __init__(self, kind, **kwargs):
        self.kind = kind
        self._extra = kwargs

    def __getattr__(self, item):
        if item not in self._extra:
            raise AttributeError(item)
        return self._extra[item]

    def is_success(self) -> bool:
        return self.kind == self.SUCCESS

    def is_failure(self) -> bool:
        return self.kind == self.FAILURE

    def __bool__(self):
        return self.is_success()

    def __neg__(self):
        return self.is_failure()

    def __eq__(self, other: 'JobExitStatus'):
        return self.kind == other.kind and self._extra == other._extra

    def __ne__(self, other: 'JobExitStatus'):
        return self != other

    def __repr__(self):
        return f"JobStatus(kind={'SUCCESS' if self else 'FAILURE'}, extra={self._extra})"

    @classmethod
    def success(cls) -> 'JobExitStatus':
        """
        Create a successful JobExitStatus
        """
        return JobExitStatus(cls.SUCCESS)

    @classmethod
    def failure(cls, **kwargs) -> 'JobExitStatus':
        """
        Create a failed JobExitStatus
        """
        return JobExitStatus(cls.FAILURE, **kwargs)


class ExecutableJobHandle:
    """
    Class representing a job that is ready to be executed
    """

    def __init__(self, job_dir: str, env_name: str, blueprint: quixote.Blueprint):
        self.job_dir = job_dir
        self.env_name = env_name
        self.blueprint = blueprint

    def execute_job(self, context: Dict[str, Any]):
        """
        Execute the job and collect its result

        :param context:         the context to use when calling the inspection steps
        """
        delivery_path = os.path.join(
            get_config()["root_dir"],
            "fetcher_cache",
            os.path.basename(self.job_dir),
            _sanitize_filename(context["request_date"])
        )

        volumes = [(self.job_dir, "/moulinette/"), (delivery_path, "/moulinette/rendu/")]

        dockerd = _DockerDaemon()
        if self.blueprint.allow_docker is True:
            _logger.info("Starting docker daemon...")
            try:
                dockerd.launch(get_config()["docker_bridge_ip"])
            except _DockerDaemonSetupError as e:
                _logger.error(f"Unable to execute inspection phase for job {os.path.basename(self.job_dir)}")
                raise JobExecutionError(e)
            volumes.append((dockerd.socket_path(), "/var/run/docker.sock"))

        volumes = map(lambda vol: f"-v{vol[0]}:{vol[1]}", volumes)

        try:
            os.mkdir(f"{self.job_dir}/workdir")

            with open(f"{self.job_dir}/context.json", 'w') as context_file:
                json.dump(context, context_file)
            _logger.info("Running inspections in the job's environment...")
            inspector_process = Popen(
                ["docker", "run", "--rm", *volumes, self.env_name, "panza_executor.py"],
                stderr=STDOUT,
                stdout=PIPE,
            )
            _logger.debug("Inspection output:")
            for line in inspector_process.stdout:
                _logger.debug("  " + line.decode().rstrip())

            return_code = inspector_process.wait()
            if return_code != 0:
                raise RuntimeError(f"inspector process exited with error status {return_code}")

            with open(f"{self.job_dir}/result.json", 'r') as result_file:
                job_result = json.load(result_file)
            if "errors" in job_result:
                return JobExitStatus.failure(**job_result["errors"]), job_result["feedback"]
            return JobExitStatus.success(), job_result["feedback"]
        except Exception as e:
            _logger.error(f"Unable to execute inspection phase for job {os.path.basename(self.job_dir)}")
            raise JobExecutionError(e)
        finally:
            if self.blueprint.allow_docker is True:
                _logger.info("Stopping docker daemon...")
                dockerd.stop()


def _sanitize_filename(name: str) -> str:
    import string
    from functools import reduce
    allowed_chars = string.ascii_lowercase + string.digits
    name = map(lambda x: x if x in allowed_chars else '_', name.lower())
    return reduce(lambda acc, x: (acc + x) if x != '_' or (len(acc) > 0 and acc[-1] != '_') else acc, name, "")


class DataAwaitingJobHandle:
    """
    Class representing a job whose environment is already built, and needs to fetch data to operate on
    """

    def __init__(self, job_dir: str, env_name: str, blueprint: quixote.Blueprint):
        self.job_dir = job_dir
        self.env_name = env_name
        self.blueprint = blueprint

    def _fetch_data(self, fetcher, job_name: str):
        try:
            fetcher()
        except Exception as e:
            _logger.error(f"Unable to fetch data for job {job_name}")
            raise DataFetchingError(e)

    def _fetch_data_from_cache(self, fetcher, delivery_path: str, job_name: str):
        _logger.debug(f"Looking for a cached directory: '{delivery_path}'")
        if not os.path.isdir(delivery_path):
            _logger.debug(f"No cache directory found, fetching data")
            return self._fetch_data(fetcher, job_name)
        _logger.debug(f"Using cached directory '{delivery_path}'")

    def fetch_data(self, context: Dict[str, Any]) -> ExecutableJobHandle:
        """
        Fetch the data on which this job will operate
        The fetcher functions specified in the blueprint will be used

        :param context:         the context to use when calling the fetch steps
        """
        job_name = os.path.basename(self.job_dir)
        delivery_path = os.path.join(
            get_config()["root_dir"],
            "fetcher_cache",
            job_name,
            _sanitize_filename(context["request_date"])
        )
        resources_path = os.path.join(self.job_dir, "resources")
        _logger.info(f"Fetching data for job {job_name}")
        with quixote.new_context(
                **get_config(),
                **context,
                delivery_path=delivery_path,
                resources_path=resources_path
        ):
            for fetcher in self.blueprint.fetchers:
                if fetcher.cached is True:
                    self._fetch_data_from_cache(fetcher, delivery_path, job_name)
                else:
                    self._fetch_data(fetcher, job_name)
        return ExecutableJobHandle(self.job_dir, self.env_name, self.blueprint)


class JobWorkspaceHandle:
    """
    Class representing a job workspace, that is, a job with its working directory and its resources
    """

    def __init__(self, job_dir: str, blueprint: quixote.Blueprint):
        self.job_dir = job_dir
        self.blueprint = blueprint

    def __enter__(self):
        return self

    def cleanup(self):
        """
        Cleanup the job's working directory
        """
        job_name = os.path.basename(self.job_dir)
        _logger.info(f"Cleaning up job {job_name}...")
        shutil.rmtree(self.job_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

    def build_job_environment(self, env_name: str) -> DataAwaitingJobHandle:
        """
        Build the environment specified by the blueprint for this job.
        The builder functions specified in the blueprint will be used to build a suitable Docker image

        :param env_name:        the name to give to the resulting environment
        """
        try:
            _logger.info(f"Building environment {env_name}...")
            generator = panza.build.create_script_generator(GeneratorType.DOCKER)
            generator.generate_to_file(
                self.blueprint,
                os.path.join(self.job_dir, "Dockerfile"),
                extra_context={**get_config(), "resources_path": os.path.join(self.job_dir, "resources")}
            )
            build_process = Popen(
                ["docker", "build", "--pull", "-t", env_name, self.job_dir],
                stderr=STDOUT,
                stdout=PIPE,
            )
            _logger.debug("Docker builder output:")
            for line in build_process.stdout:
                _logger.debug("  " + line.decode().rstrip())
            return_code = build_process.wait()
            if return_code != 0:
                raise RuntimeError(f"builder process exited with error status {return_code}")
            _logger.debug("Cleaning up after building...")
            os.remove(os.path.join(self.job_dir, "Dockerfile"))
        except Exception as e:
            _logger.error(f"unable to build environment {env_name}: {str(e)}")
            raise EnvironmentBuildError(e)
        return DataAwaitingJobHandle(self.job_dir, env_name, self.blueprint)


def new_job_workspace(job_files_dir: str, job_name: str) -> JobWorkspaceHandle:
    """
    Create a workspace in which the job can be executed.
    This will create a directory, copy the required files, and load the blueprint

    :param job_files_dir:       the path to the directory containing the job's resources files
    :param job_name:            the name of the job, used to create its workspace
    """
    job_dir = os.path.normpath(os.path.join(get_config()["root_dir"], job_name))
    _logger.info(f"Creating workspace {job_dir} for job {job_name}...")

    try:
        shutil.copytree(job_files_dir, job_dir)
    except OSError as e:
        raise WorkspaceCreationError(e)

    _logger.info(f"Loading blueprint for job {job_name}...")

    try:
        blueprint = panza.BlueprintLoader.load_from_directory(job_dir)
    except BlueprintLoadError as e:
        shutil.rmtree(job_dir)
        raise WorkspaceCreationError(e)

    return JobWorkspaceHandle(job_dir, blueprint)
