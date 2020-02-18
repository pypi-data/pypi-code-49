#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import textwrap
import time
import uuid
import disco
from time import sleep
from disco.core.constants import JobStatus, TaskStatus
from tests.base_test import BaseTest
from .env import LIVE_TESTS_TIMEOUT_SECONDS, LIVE_TESTS_JOB_START_WAIT_TIME, LIVE_TESTS_TASKS_RUNNING_WAIT_TIME
from .utils import get_non_running_tasks


# @pytest.mark.skipif(env.skip, reason=env.reason)
# TODO: Test with a non-default cluster
# TODO: Archive jobs on tear-down even if an exception was thrown
class TestJobsLive(object):

    def setup_class(self):
        BaseTest.disable_progress_bar()

    def test_start_job(self):
        script_content = 'print(\'Hello from automation!\')'
        script_file_id = disco.upload_file('hello.py', script_content)
        input_file_id = disco.upload_file('input.txt', '13')
        constants_file_id = disco.upload_file('constants.txt', 'ZZZ')

        job_name = 'Automation Start Job %s' % uuid.uuid4()
        job = disco.Job.create(script_file_id=script_file_id,
                               input_file_ids=[input_file_id],
                               constants_file_ids=[constants_file_id],
                               job_name=job_name)

        job.start()
        job_details = job.get_details()
        job_id = job_details.id

        assert job_id
        assert job_details.name == job_name

        print(f'Waiting for job {job.job_id} to finish...')

        job.wait_for_finish(interval=10, timeout=LIVE_TESTS_TIMEOUT_SECONDS)
        assert job.get_status() == JobStatus.done

        print(f'job {job.job_id} finished!')

        job_tasks = job.get_tasks()
        assert job_tasks[0].status == TaskStatus.success.value

        jobs_list = disco.Job.list_jobs()
        assert job_id in [job_details.id for job_details in jobs_list]

        job.archive()

    def test_create_job_from_git_repository(self):
        input_file_id = disco.upload_file('input.txt', '13')
        constants_file_id = disco.upload_file('constants.txt', 'ZZZ')
        users_repositories = disco.Repository.list_repositories()
        if len(users_repositories) > 0:
            script_repo_id = users_repositories[0].id;
            script_file_path = 'aaa'
            job_name = 'Automation Start Job %s' % uuid.uuid4()
            job = disco.Job.create(input_file_ids=[input_file_id],
                                   constants_file_ids=[constants_file_id],
                                   job_name=job_name,
                                   script_repo_id = script_repo_id,
                                   script_file_path_in_repo= script_file_path)

            job_details = job.get_details()
            job_id = job_details.id
            assert job_id
            assert job_details.name == job_name

            job.archive()

    def test_cancel_job(self):
        script_content = textwrap.dedent('''
        import time
        
        for i in range(9000):
            print(i)
            time.sleep(1)
        ''')

        script_file_id = disco.upload_file('sleep.py', script_content)
        job_name = 'Automation Cancel Job %s' % uuid.uuid4()
        job = disco.Job.create(script_file_id=script_file_id,
                               job_name=job_name)

        print(f'Starting job {job.job_id}...')
        job.start()
        job_status = job.wait_for_status(JobStatus.working, interval=10,
                                         timeout=LIVE_TESTS_JOB_START_WAIT_TIME)
        assert job_status == JobStatus.working

        print("Waiting for job tasks to start running...")
        start_time = time.time()
        timeout_time = start_time + LIVE_TESTS_TASKS_RUNNING_WAIT_TIME
        while time.time() <= timeout_time:
            stale_tasks = get_non_running_tasks(job.get_tasks())
            if len(stale_tasks) == 0:
                return
            print("Following tasks haven't started yet: {}".format(stale_tasks))
            sleep(10)
        assert len(stale_tasks) == 0

        print(f'Job {job.job_id} started, tasks are running stopping job...')
        job.stop()

        print(f'Waiting for job {job.job_id} to finish...')
        # TODO: Distinguish between failed or completed and stopped jobs on the
        #       server side! Currently we can't tell a stopped job from a
        #       completed job that has a failed task
        job_status = job.wait_for_status(JobStatus.done, interval=10,
                                         timeout=LIVE_TESTS_TIMEOUT_SECONDS)
        assert job_status == JobStatus.done

        print(f'job {job.job_id} was cancelled!')

        tasks = job.get_tasks()
        assert len(tasks) == 1
        assert tasks[0].status == TaskStatus.failed.value

        job.archive()

    def test_auto_start_job(self):
        script_content = 'print(\'Hello from automation!\')'
        script_file_id = disco.upload_file('hello.py', script_content)

        job_name = 'Automation Auto Start Job %s' % uuid.uuid4()
        job = disco.Job.create(script_file_id=script_file_id,
                               job_name=job_name, auto_start=True)

        print(f'job {job.job_id} finished!')

        job.wait_for_finish(interval=10, timeout=LIVE_TESTS_TIMEOUT_SECONDS)
        assert job.get_status() == JobStatus.done

        job.archive()

    def test_list_jobs(self):
        jobs = disco.Job.list_jobs(1)
        assert isinstance(jobs, list)
        if jobs:
            assert len(jobs) == 1
            job_details = jobs[0]
            assert job_details.id is not None
            assert job_details.name is not None
            assert job_details.status is not None

    def test_exception_on_job(self):
        erroneous_script = '1 / 0'
        script_file_id = disco.upload_file('woof.py', erroneous_script)

        job_name = 'Automation Failing Job %s' % uuid.uuid4()
        job = disco.Job.create(script_file_id, job_name=job_name, auto_start=True)

        print(f'Waiting for job {job.job_id} to finish...')

        job.wait_for_finish(interval=10, timeout=LIVE_TESTS_TIMEOUT_SECONDS)
        assert job.get_status() == JobStatus.failed

        print(f'job {job.job_id} finished!')

        job_tasks = job.get_tasks()
        assert job_tasks[0].status == TaskStatus.failed.value

        job.archive()
