"""
DISCO Jobs representation
"""
import re
import time
import uuid
import sys
import subprocess
from collections import defaultdict
from typing import Union

from .models import JobDetails, Task
from .asset import Asset
from .core import constants, exceptions, \
    is_venv, zip_tools
from .task import TaskResult
from .base_controller import BaseController


class Job(BaseController):
    """A job that runs on DISCO machines.

    Every `Job` object has its own Python script and data files, and runs
    independently on the cloud, until it produces a result.
    """

    _task_result_pattern = re.compile('^([^.]*?).zip$')
    TIMEOUT = 10 * constants.MINUTE

    # WARNING: Does not handle paging
    @classmethod
    def list_jobs(cls, limit=None, next_=None):
        """Show a list of all the jobs belonging to this user.

        Args:
            limit (int):
            next_:

        Returns:
            list(JobDetails)
        """

        res = cls.query('findJobsByProfile', limit=limit,
                        ownerId=cls.get_current_user(),
                        archived=False, next=next_)

        if res is None:
            return []

        results = res['findJobs']['results']

        return [JobDetails(result) for result in results]

    @classmethod
    def jobs_summary(cls):
        """Gets a summary of all job statuses.

        Returns:
            dict: Dictionary [str, int] of status->count
        """

        status_counts = defaultdict(int)

        # This will work when list jobs supports paging and `yields`
        for job_detail in cls.list_jobs():
            status_counts[job_detail.status] += 1
        return dict(status_counts)

    @classmethod
    def _get_venv_requirements(cls, cluster_id: str):
        if is_venv():
            freeze_command = [sys.executable, '-m', 'pip', 'freeze']

            process = subprocess.Popen(
                freeze_command,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, _ = process.communicate()
            requirements = stdout.decode("utf-8")
            # filtering out disco packages
            split_req = filter(lambda line: "disco" not in line and "iqoqo" not in line, requirements.splitlines())
            requirements = "\n".join(split_req)
            req_file_id = Asset().upload(
                'requirements.txt',
                requirements,
                cluster_id,
                show_progress_bar=False)
            return req_file_id

        print("Warning: Python virtual environment was not detected. "
              "Dis.co will not be able to automatically "
              "update your cloud environment when not using "
              "Python virtual environment.")
        return None

    @classmethod
    def create(  # pylint: disable-msg=too-many-arguments,too-many-locals
            cls,
            script_file_id=None,
            input_file_ids: Union[str, list] = None,
            constants_file_ids: Union[str, list] = None,
            job_name=None,
            cluster_instance_type='s',
            cluster_id=None,
            script_repo_id=None,
            script_file_path_in_repo=None,
            auto_start=False,
            upload_requirements_file=True,
            docker_image_id=None
    ):
        """Creates a new job.

        Args:
            script_file_id (str): The ID of the script file to run.
            input_file_ids: A list of IDs of files that will be used as
                standard input.
            constants_file_ids:  A list of IDs of constants files.
            job_name: Is a name you can give to your job. Leave empty
                to use a random string.
            cluster_instance_type: Is the size of instance used. Choose 'm'
                for a medium instance and 'l' for a large instance.
                The default is 's' for small.
            cluster_id: Specifies the ID of the cluster on which to run the
                job. Leave as `None` to run on DISCO's cluster.
            script_repo_id (str): The id of the Git repository in which the script file to run is.
                (Alternative to script_file_id).
            script_file_path_in_repo (str): The path in the Git repository to the script file.
            auto_start: Automatically start the job upon creation.
            upload_requirements_file (bool): if True uploads a requirements file if in venv.
            docker_image_id (str): The id of the docker image to run the job in.

        Returns:
            obj: The created job object.
        """
        if script_file_id is None and script_repo_id is None:
            raise exceptions.DiscoException("Script file is missing")
        if script_repo_id is not None and script_file_path_in_repo is None:
            raise exceptions.DiscoException("Script file path in repository is missing")

        constants_file_ids = constants_file_ids or []
        input_file_ids = input_file_ids or []

        venv_requirements = cls._get_venv_requirements(cluster_id)
        if upload_requirements_file and venv_requirements:
            constants_file_ids.append(venv_requirements)

        job_meta = {
            'name': job_name or uuid.uuid4().hex,
            'inputIds': input_file_ids,
            'constantIds': constants_file_ids,
            'clusterId': cluster_id,
            'clusterInstanceType': cluster_instance_type,
            'dockerImageId': docker_image_id
        }

        if script_file_id is not None:
            job_meta['scriptId'] = script_file_id
        else:
            job_meta['scriptRepoId'] = script_repo_id
            job_meta['scriptFilePath'] = script_file_path_in_repo

        job_options = {
            'executeOnSubmit': auto_start
        }

        result = cls.query('createJob', args=job_meta, options=job_options)
        return Job(result['createJob']['id'])

    def __init__(self, job_id):
        self.job_id = job_id
        super().__init__()

    def start(self):
        """Start the job.

        When you run `job.start()`, the DISCO server will queue the job for
        execution.

        Returns:
            obj: The job object.
        """
        return self.query('startJob', id=self.job_id)

    def stop(self):
        """Cancels a running job.

        When you run `job.stop()`, the DISCO server will stop running the job
        and return any results retrieved so far.
        """

        self.query('stopJob', id=self.job_id)

    def archive(self):
        """Archive the job, making it unusable."""
        self.query('archiveJob', id=self.job_id)

    def get_details(self):
        """
        Get details about the job.

        This includes its name, last activity, status and task states.

        Returns:
            JobDetails
        """
        response = self.query('fetchJob', id=self.job_id)

        return JobDetails(response['fetchJob'])

    def get_tasks(self, limit=None, next_=None):
        """
        Get job tasks

        Args:
            limit (int):
            next_:

        Returns:
            list(Task)
        """
        # WARNING: Does not handle paging
        response = self.query(
            'findTasksByJob',
            limit=limit,
            next=next_,
            jobId=self.job_id)

        results = response['findTasks']['results']
        return [Task(result) for result in results]

    def get_status(self):
        """Get the job's status.

        This is a `JobStatus` object, equal to one of
        `['Unknown',
          'Listed',
          'Working',
          'Stopped',
          'Done',
          'Failed',
          'Deleted']`.

          Returns:
              The status of the job.
        """
        job_details = self.get_details()
        if constants.JobStatus(job_details.status) == constants.JobStatus.done and \
                job_details.tasks_summary.failed > 0:
            return constants.JobStatus.failed
        return constants.JobStatus(job_details.status)

    def wait_for_finish(self, interval=5, timeout=TIMEOUT):
        """Wait for a job to finish.

        This means waiting until it's no longer in "listed" or "working"
        statuses.

        Args:
            interval (int): Interval in seconds to check if the job has
                finished running.
            timeout (int): Timeout in seconds.

        Returns:
            The status of the job.
        """
        return self.wait_for_status(
            *constants.JOB_TERMINAL_STATES,
            interval=interval, timeout=timeout
        )

    def wait_for_status(self, *expected_statuses, interval=5, timeout=TIMEOUT):
        """Wait for one of a job statuses.

        Args:
            *expected_statuses (str): List of expected job statuses.
            interval (int): Interval in seconds to check the job's status.
            timeout (int): Timeout in seconds.

        Returns:
            The status of the job.
        """
        start_time = time.time()
        timeout_time = start_time + timeout

        while time.time() <= timeout_time:
            status = self.get_status()
            if status in expected_statuses:
                return status

            time.sleep(interval)
        raise exceptions.TimeOutError

    def get_results(self, block=False, block_timeout=TIMEOUT):
        """Get the job's result.

        Args:
            block (bool): Pass `block=True` to first wait for the job
                to be completed.
            block_timeout (int): timeout in seconds.

        Returns:
        """
        if block:
            self.wait_for_finish(block_timeout)

        response = self.stream(f"/jobs/{self.job_id}/result")

        archive = zip_tools.unzip_in_memory(response)
        task_results = []
        for file_name, file_content in archive:
            if file_name == 'no-results-found.txt':
                continue

            match = self._task_result_pattern.match(file_name)
            if not match:
                continue

            task_id = match.group(1)
            task_results.append(
                TaskResult(
                    task_id,
                    zip_tools.unzip_in_memory(file_content)
                )
            )
        return task_results

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, repr(self.job_id))
