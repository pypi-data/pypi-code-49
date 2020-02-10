#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import os
import shutil
import sys
import textwrap
import pytest
import mock
import virtualenv
from tempfile import TemporaryDirectory
import pathlib
import subprocess
import disco
from disco.core.constants import JobStatus
from tests.base_test import BaseTest
from tests.live import env
from .env import LIVE_TESTS_TIMEOUT_SECONDS


@pytest.mark.skipif(env.skip, reason=env.reason)
class TestTasksLive(BaseTest):

    def setup_class(self):
        BaseTest.disable_progress_bar()

    def test_files(self):

        expected_output = 'All done!'

        task_content = textwrap.dedent('''
            import os
            import sys
            import time
            os.makedirs('run-result/foo/bar/baz')
            open('run-result/file1', 'w').write('tip\\n'
                                     'top')
            open('run-result/foo/file2', 'w')
            glissando = (bytes(range(256)) if sys.version_info[0] == 3 else
                         b''.join(chr(i) for i in range(256)))
            open('run-result/foo/bar/baz/file3', 'wb').write(glissando)
            time.sleep(3)
            print('All done!')
        ''')
        script_file_id = disco.upload_file('woof.py', task_content)

        job = disco.Job.create(script_file_id)
        job.start()

        print(f'Waiting for job {job.job_id} to finish...')

        job.wait_for_status(JobStatus.done, interval=10, timeout=LIVE_TESTS_TIMEOUT_SECONDS)

        print(f'job {job.job_id} finished!')
        print('Waiting for the jobs results')

        (task_result,) = job.get_results(block=True)

        print('Finished getting the results')

        task_result_output = self._stdout_to_output(task_result.stdout)
        assert task_result_output == expected_output

        glissando = (bytes(range(256)) if sys.version_info[0] == 3 else
                     b''.join(chr(i) for i in range(256)))
        assert ('foo/bar/baz/file3', glissando) in task_result.raw_result

        with TemporaryDirectory(prefix='test_disco_') as temp_folder:
            temp_folder = pathlib.Path(str(temp_folder))
            task_result.write_files(temp_folder)
            current_paths = list(temp_folder.rglob('*'))

            assert len(current_paths) == 8

            (output_path,) = (path for path in current_paths if path == temp_folder / 'IqoqoTask.stdout.0.txt')
            current_paths.remove(output_path)

            output_path_text = self._stdout_to_output(output_path.read_text())

            assert output_path_text == expected_output

            (file1_path,) = (path for path in current_paths if path == temp_folder / 'file1')
            current_paths.remove(file1_path)
            assert file1_path.read_text() == ('tip\n'
                                              'top')

            (file2_path,) = (path for path in current_paths if path == temp_folder / 'foo' / 'file2')
            current_paths.remove(file2_path)
            assert file2_path.read_text() == ''

            (file3_path,) = (path for path in current_paths if path == temp_folder / 'foo' / 'bar' / 'baz' / 'file3')
            current_paths.remove(file3_path)
            assert file3_path.read_bytes() == glissando

            folder_paths = [path for path in current_paths if path.name in ('foo', 'bar', 'baz')]
            for folder_path in folder_paths:
                assert folder_path.is_dir()
                current_paths.remove(folder_path)

            assert len(current_paths) == 1
            (meta_stderr_path,) = current_paths
            assert 'stderr' in meta_stderr_path.name
            assert meta_stderr_path.is_file()

    def test_multiple_tasks(self):
        task_content = textwrap.dedent('''
        import sys
        import time
        content = open(sys.argv[1]).read()
        print('%s' % content)
        time.sleep(3)
        ''')

        number_of_inputs = 30

        expected_outputs = [self.random_str(prefix=f"output{i}-") for i in range(number_of_inputs)]

        print(f'Uploading input files...')

        input_file_ids = [disco.upload_file(f'input_{i}.txt', expected_outputs[i]) for i in range(number_of_inputs)]
        script_file_id = disco.upload_file('meow.py', task_content)

        job = disco.Job.create(
            script_file_id,
            input_file_ids=input_file_ids
        )

        job.start()

        print(f'Waiting for job {job.job_id} to finish...')

        job.wait_for_status(JobStatus.done, interval=10, timeout=LIVE_TESTS_TIMEOUT_SECONDS)

        print(f'job {job.job_id} finished!')
        print('Waiting for the jobs results')

        task_results = job.get_results(block=True)

        print('Finished getting the results')

        assert len(expected_outputs) == len(task_results), 'expected output length matches the task results length'

        # Verify that the result matches the output
        task_result_outputs = [self._stdout_to_output(task_result.stdout) for task_result in task_results]

        assert task_result_outputs == expected_outputs, 'task result outputs matches the expected output'

    def test_running_in_venv(self):

        expected_output = 'All done!'

        venv_temp_dir = self._create_and_activate_venv()
        venv_pip_path = os.path.join(venv_temp_dir, "bin", "pip")
        venv_python_path = os.path.join(venv_temp_dir, "bin", "python")

        install_return_code = subprocess.call([venv_pip_path, "install", 'setuptools==42.0.2'])
        assert install_return_code == 0

        task_content = textwrap.dedent('''
        from setuptools import setup
        print('All done!')
        ''')

        script_file_id = disco.upload_file('code-with-package.py', task_content)

        # Ensure we use the correct python path when doing `pip freeze` to get the venv requirements
        with mock.patch('sys.executable', venv_python_path):
            job = disco.Job.create(script_file_id)

        job.start()

        print(f'Waiting for job {job.job_id} to finish...')

        job.wait_for_status(JobStatus.done, interval=10, timeout=LIVE_TESTS_TIMEOUT_SECONDS)

        print(f'job {job.job_id} finished!')
        print('Waiting for the jobs results')

        task_results = job.get_results(block=True)

        print('Finished getting the results')

        task_result_output = self._stdout_to_output(task_results[0].stdout)

        assert task_result_output == expected_output

        self._delete_venv()

    def test_get_tasks(self):
        task_content = textwrap.dedent('''
        import sys
        content = open(sys.argv[1]).read()
        print('foo %s' % content)
        ''')

        script_file_id = disco.upload_file('meow.py', task_content)

        job = disco.Job.create(script_file_id)

        print(f'Waiting for tasks of job {job.job_id}')

        job_tasks = job.get_tasks()

        print('Finished getting the tasks')

        assert isinstance(job_tasks, list)
        assert len(job_tasks) == 1

        task = job_tasks[0]

        assert task.id is not None
        assert task.status is not None
        assert task.duration >= 0

    @staticmethod
    def _stdout_to_output(stdout):
        stdout_str = stdout

        if isinstance(stdout, bytes):
            stdout_str = stdout.decode("utf-8")

        output_lines = stdout_str.strip().split('\n')
        return output_lines[-1]

    @staticmethod
    def _venv_temp_dir():
        return os.path.join(os.path.expanduser("~"), ".venv-test-temp")

    @classmethod
    def _delete_venv(cls):
        try:
            shutil.rmtree(cls._venv_temp_dir())
        except OSError:
            return

    @classmethod
    def _create_and_activate_venv(cls):
        venv_temp_dir = cls._venv_temp_dir()

        cls._delete_venv()

        virtualenv.create_environment(venv_temp_dir)
        path = os.path.join(venv_temp_dir, "bin", "activate_this.py")
        exec(open(path).read(), {'__file__': path})

        return venv_temp_dir
