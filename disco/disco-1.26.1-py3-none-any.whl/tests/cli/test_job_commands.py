from pathlib import Path
from time import sleep
import os

from disco.models import ClusterDetails
from disco import Job
from disco.core.exceptions import BucketPathsException, BucketPathsErrorTypes, RequestException
from disco.core.constants import JobStatus, ClusterType
from disco.task import TaskResult

from .sdk_mocks import MockListJobsResponse, MockViewJobResponse, MockBadIdException
from mock import patch, call
from click.testing import CliRunner
from disco_cli import cli, setup_cli
from .cli_test_utils import output_message_includes
from tests.base_test import BaseTest


class TestJobCommands(BaseTest):

    def setup_class(self):
        setup_cli()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    def test_job_list(self, is_logged_in_mock):
        """
        Tests job list
        Returns:

        """
        is_logged_in_mock.return_value = True
        with patch('disco.Job.list_jobs') as list_jobs_mock:
            list_jobs_mock.return_value = MockListJobsResponse
            runner = CliRunner()
            result = runner.invoke(cli, ['job', 'list'])
            assert result.exit_code == 0
            list_jobs_mock.assert_called()
            is_logged_in_mock.assert_called()
            assert output_message_includes(result, '| 5d66595208edfa000a250dda | Cool Humor       | Done     |')

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.list_jobs')
    def test_action_without_login(self, list_jobs_mock, is_logged_in_mock):
        list_jobs_mock.return_value = []
        is_logged_in_mock.return_value = False
        runner = CliRunner()
        result = runner.invoke(cli, ['job', 'list'])
        assert result.exit_code == 0
        assert result.output == "You must be logged in to perform this operation\n"

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.get_details')
    def test_view_job(self, get_details_mock, is_logged_in_mock):
        """
        Tests a successful job view command
        Returns:

        """
        is_logged_in_mock.return_value = True
        get_details_mock.return_value = MockViewJobResponse
        runner = CliRunner()
        result = runner.invoke(cli, ['job', 'view', 'job_id'])
        get_details_mock.assert_called_once()
        assert result.exit_code == 0
        assert output_message_includes(result, "Status: Done")
        assert output_message_includes(result, "Name: dsfgfdsgs")
        assert output_message_includes(result, "failed: 1")

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.get_details')
    def test_view_job_malformed_id(self, get_details_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        get_details_mock.side_effect = MockBadIdException
        get_details_mock.return_value = MockViewJobResponse
        runner = CliRunner()
        result = runner.invoke(cli, ['job', 'view', 'job_id'])
        get_details_mock.assert_called_once()
        assert result.exit_code == 0
        assert output_message_includes(result, "Bad format for Id")

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_input_file(self, asset_upload_mock, path_is_dir_mock,
                                   path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using input files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py -i input_file".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id='file_id', input_file_ids=['file_id'],
                                                   constants_file_ids=[], job_name='job_name', cluster_instance_type='s',
                                                   cluster_id=None, script_repo_id=None, script_file_path_in_repo=None,
                                                   auto_start=False, upload_requirements_file=True, docker_image_id=None
                                                   )

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.input_files_from_bucket')
    @patch('disco.Cluster.fetch_and_validate_by_id')
    def test_create_job_with_invalid_cluster(self, cluster_fetch_and_validate_by_id, input_files_from_bucket_mock,
                                             job_create_mock, is_logged_in_mock):
        """
        Create job with input files from bucket paths - no files found
        """
        unauthorized_cluster_id = self.random_str('unauthorized_cluster_id')
        job_name = self.random_str('job_name')
        script_file_name = 'script_file.py'

        invalid_cluster_error_message = f'Cluster {unauthorized_cluster_id} is invalid or missing.'

        is_logged_in_mock.return_value = True
        cluster_fetch_and_validate_by_id.return_value = False
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open(script_file_name, 'w') as f:
                f.write("print('hi!')")
                command = f"job create " \
                          f" --name {job_name} "\
                          f" --script {script_file_name}"\
                          f" --cluster-id {unauthorized_cluster_id}"
                result = runner.invoke(cli, command)
                assert result.exit_code == 0

                expected_result_output = f'{invalid_cluster_error_message}\n'

                assert result.output == expected_result_output

                input_files_from_bucket_mock.assert_not_called()
                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    @patch('disco.asset.Asset.input_files_from_bucket')
    @patch('disco.Cluster.fetch_and_validate_by_id')
    def test_create_job_with_bucket_input_files(self, cluster_fetch_and_validate_by_id, input_files_from_bucket_mock,
                                                asset_upload_mock, job_create_mock, is_logged_in_mock):
        """
        Create job with input files from bucket paths
        """
        bucket_paths = self.random_list('bucket_path', length=3)
        raw_bucket_paths = ','.join(bucket_paths)
        bucket_input_file_ids = self.random_list('bucket_input_file_id', length=3)

        cluster_id = self.random_str('cluster_id')
        cluster = ClusterDetails(dict(id=cluster_id, type=ClusterType.AWS.value))
        job_name = self.random_str('job_name')
        script_file_id = self.random_str('script_file_id')
        script_file_name = 'script_file.py'
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job(job_id)
        asset_upload_mock.return_value = script_file_id
        input_files_from_bucket_mock.return_value = bucket_input_file_ids
        cluster_fetch_and_validate_by_id.return_value = cluster
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open(script_file_name, 'w') as f:
                f.write("print('hi!')")
                command = f"job create " \
                          f" --name {job_name} "\
                          f" --script {script_file_name}"\
                          f" --bucket {raw_bucket_paths}" \
                          f" --cluster-id {cluster_id}"
                result = runner.invoke(cli, command)
                assert result.exit_code == 0
                assert output_message_includes(result, f'Found {len(bucket_input_file_ids)} input files in your bucket')
                assert output_message_includes(result, f'Created job with id {job_id}')

                input_file_ids = bucket_input_file_ids

                cluster_fetch_and_validate_by_id.assert_called_with(cluster_id)
                input_files_from_bucket_mock.assert_called_with(bucket_paths, cluster_id)

                job_create_mock.assert_called_with(script_file_id=script_file_id, input_file_ids=input_file_ids,
                                                   constants_file_ids=[],
                                                   job_name=job_name, docker_image_id=None, script_repo_id=None,
                                                   script_file_path_in_repo=None,
                                                   cluster_instance_type='s', cluster_id=cluster_id, auto_start=False,
                                                   upload_requirements_file=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    @patch('disco.asset.Asset.input_files_from_bucket')
    @patch('disco.Cluster.fetch_and_validate_by_id')
    def test_create_job_with_bucket_input_files_no_files_found(self, cluster_fetch_and_validate_by_id,
                                                               input_files_from_bucket_mock, asset_upload_mock,
                                                               job_create_mock, is_logged_in_mock):
        """
        Create job with input files from bucket paths - no files found
        """
        bucket_paths = self.random_list('bucket_path', length=3)
        raw_bucket_paths = ','.join(bucket_paths)
        no_bucket_input_file_ids = []

        cluster_id = self.random_str('cluster_id')
        cluster = ClusterDetails(dict(id=cluster_id, type=ClusterType.AWS.value))
        job_name = self.random_str('job_name')
        script_file_id =  self.random_str('script_file_id')
        script_file_name = 'script_file.py'
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job(job_id)
        asset_upload_mock.return_value = script_file_id
        input_files_from_bucket_mock.return_value = no_bucket_input_file_ids
        cluster_fetch_and_validate_by_id.return_value = cluster
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open(script_file_name, 'w') as f:
                f.write("print('hi!')")
                command = f"job create " \
                          f" --name {job_name} "\
                          f" --script {script_file_name}"\
                          f" --bucket {raw_bucket_paths}" \
                          f" --cluster-id {cluster_id}"
                result = runner.invoke(cli, command)
                assert result.exit_code == 0
                assert result.output == 'No input files found in the specified buckets paths\n'

                cluster_fetch_and_validate_by_id.assert_called_with(cluster_id)
                input_files_from_bucket_mock.assert_called_with(bucket_paths, cluster_id)

                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    @patch('disco.asset.Asset.input_files_from_bucket')
    @patch('disco.Cluster.fetch_and_validate_by_id')
    def test_create_job_with_bucket_input_files_error_bucket_path(self, cluster_fetch_and_validate_by_id,
                                                                  input_files_from_bucket_mock, asset_upload_mock,
                                                                  job_create_mock, is_logged_in_mock):
        """
        Create job with input files from bucket paths - no files found
        """
        valid_bucket_paths = self.random_list('valid_bucket_paths', length=2)
        invalid_bucket_paths = self.random_list('invalid_bucket_paths', length=2)
        empty_bucket_paths = self.random_list('empty_bucket_paths', length=2)
        bucket_paths = valid_bucket_paths + invalid_bucket_paths + empty_bucket_paths
        raw_bucket_paths = ','.join(bucket_paths)

        bucket_paths_errors = {
            invalid_bucket_paths[0]: BucketPathsErrorTypes.InvalidPath,
            invalid_bucket_paths[1]: BucketPathsErrorTypes.InvalidPath,
            empty_bucket_paths[0]: BucketPathsErrorTypes.NoFilesInPath,
            empty_bucket_paths[1]: BucketPathsErrorTypes.NoFilesInPath,
        }

        cluster_id = self.random_str('cluster_id')
        cluster = ClusterDetails(dict(id=cluster_id, type=ClusterType.AWS.value))
        job_name = self.random_str('job_name')
        script_file_id =  self.random_str('script_file_id')
        script_file_name = 'script_file.py'
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job(job_id)
        asset_upload_mock.return_value = script_file_id
        input_files_from_bucket_mock.side_effect = BucketPathsException('some error message',
                                                                        bucket_paths_errors=bucket_paths_errors)
        cluster_fetch_and_validate_by_id.return_value = cluster
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open(script_file_name, 'w') as f:
                f.write("print('hi!')")
                command = f"job create " \
                          f" --name {job_name} "\
                          f" --script {script_file_name}"\
                          f" --bucket {raw_bucket_paths}" \
                          f" --cluster-id {cluster_id}"
                result = runner.invoke(cli, command)
                assert result.exit_code == 0

                sorted_list_invalid_bucket_paths_output = '\n'.join(sorted(invalid_bucket_paths))
                sorted_list_empty_bucket_paths_output = '\n'.join(sorted(empty_bucket_paths))

                expected_result_output = f'Invalid or missing buckets paths specified:\n' \
                                         f'{sorted_list_invalid_bucket_paths_output}\n' \
                                         f'No input files found in the following buckets paths:\n' \
                                         f'{sorted_list_empty_bucket_paths_output}\n'

                assert result.output == expected_result_output

                cluster_fetch_and_validate_by_id.assert_called_with(cluster_id)
                input_files_from_bucket_mock.assert_called_with(bucket_paths, cluster_id)

                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.input_files_from_bucket')
    @patch('disco.Cluster.fetch_and_validate_by_id')
    def test_create_job_with_bucket_input_files_error_unauthorized_cluster_error(self, cluster_fetch_and_validate_by_id,
                                                                                 input_files_from_bucket_mock,
                                                                                 job_create_mock, is_logged_in_mock):
        """
        When a user tries to register files from Dis.co Net managed cluster -
        the backend should return Unauthorized error
        """
        bucket_paths = self.random_list('bucket_paths', length=2)
        raw_bucket_paths = ','.join(bucket_paths)

        unauthorized_cluster_id = self.random_str('unauthorized_cluster_id')
        cluster = ClusterDetails(dict(id=unauthorized_cluster_id, type=ClusterType.AWS.value))

        job_name = self.random_str('job_name')
        script_file_name = 'script_file.py'

        unauthorized_error_message = 'You can only use files from buckets on your own private cluster'

        is_logged_in_mock.return_value = True
        input_files_from_bucket_mock.side_effect = RequestException(unauthorized_error_message)
        cluster_fetch_and_validate_by_id.return_value = cluster
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open(script_file_name, 'w') as f:
                f.write("print('hi!')")
                command = f"job create " \
                          f" --name {job_name} "\
                          f" --script {script_file_name}"\
                          f" --bucket {raw_bucket_paths}" \
                          f" --cluster-id {unauthorized_cluster_id}"
                result = runner.invoke(cli, command)
                assert result.exit_code == 0

                expected_result_output = f'{unauthorized_error_message}\n'

                assert result.output == expected_result_output

                cluster_fetch_and_validate_by_id.assert_called_with(unauthorized_cluster_id)
                input_files_from_bucket_mock.assert_called_with(bucket_paths, unauthorized_cluster_id)

                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    @patch('disco.asset.Asset.input_files_from_bucket')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.Cluster.fetch_and_validate_by_id')
    def test_create_job_with_bucket_and_local_input_files(self, cluster_fetch_and_validate_by_id,
                                                          path_is_dir_mock, path_exists_mock,
                                                          input_files_from_bucket_mock, asset_upload_mock,
                                                          job_create_mock, is_logged_in_mock):
        """
        Create job with input files from bucket paths and local input paths
        """
        bucket_paths = self.random_list('bucket_path', length=3)
        raw_bucket_paths = ','.join(bucket_paths)
        bucket_input_file_ids = self.random_list('bucket_input_file_id', length=3)

        input_paths = self.random_list('input_paths', length=3)
        raw_input_paths = ','.join(input_paths)
        local_input_file_ids = self.random_list('local_input_file_id', length=3)

        cluster_id = self.random_str('cluster_id')
        cluster = ClusterDetails(dict(id=cluster_id, type=ClusterType.AWS.value))
        job_name = self.random_str('job_name')
        script_file_id = self.random_str('script_file_id')
        script_file_name = 'script_file.py'
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job(job_id)
        asset_upload_mock.side_effect = local_input_file_ids + [script_file_id]
        input_files_from_bucket_mock.return_value = bucket_input_file_ids
        cluster_fetch_and_validate_by_id.return_value = cluster
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open(script_file_name, 'w') as f:
                f.write("print('hi!')")
                command = f"job create " \
                          f" --name {job_name} "\
                          f" --script {script_file_name}" \
                          f" --input {raw_input_paths}" \
                          f" --bucket {raw_bucket_paths}" \
                          f" --cluster-id {cluster_id}"
                result = runner.invoke(cli, command)
                assert result.exit_code == 0
                assert output_message_includes(result, f'Found {len(bucket_input_file_ids)} input files in your bucket')
                assert output_message_includes(result, f'Created job with id {job_id}')

                input_file_ids = bucket_input_file_ids + local_input_file_ids

                cluster_fetch_and_validate_by_id.assert_called_with(cluster_id)
                input_files_from_bucket_mock.assert_called_with(bucket_paths, cluster_id)

                job_create_mock.assert_called_with(script_file_id=script_file_id, input_file_ids=input_file_ids,
                                                   constants_file_ids=[],
                                                   job_name=job_name, docker_image_id=None, script_repo_id=None,
                                                   script_file_path_in_repo=None,
                                                   cluster_instance_type='s', cluster_id=cluster_id, auto_start=False,
                                                   upload_requirements_file=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    def test_create_job_quite_mode(self, asset_upload_mock, job_create_mock, is_logged_in_mock):
        """
        Run create job in quite mode
        """
        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py --quite")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id='file_id', input_file_ids=[], constants_file_ids=[],
                                                   job_name='job_name', cluster_instance_type='s', cluster_id=None,
                                                   script_repo_id=None, script_file_path_in_repo=None, auto_start=False,
                                                   upload_requirements_file=True, docker_image_id=None)

                asset_upload_mock.assert_called_with('script_file.py', Path('script_file.py'),
                                                     cluster=None, show_progress_bar=False)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    def test_create_job_quite_mode_disabled_by_default(self, asset_upload_mock, job_create_mock, is_logged_in_mock):
        """
        Run create job, quite mode disabled by default
        """
        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id='file_id', input_file_ids=[], constants_file_ids=[],
                                                   job_name='job_name', cluster_instance_type='s', cluster_id=None,
                                                   script_repo_id=None, script_file_path_in_repo=None, auto_start=False,
                                                   upload_requirements_file=True, docker_image_id=None)

                asset_upload_mock.assert_called_with('script_file.py', Path('script_file.py'),
                                                     cluster=None, show_progress_bar=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_without_req_file(self, asset_upload_mock, path_is_dir_mock,
                                         path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using input files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py -i "
                                            "input_file --dont-generate-req-file".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id='file_id', input_file_ids=['file_id'],
                                                   constants_file_ids=[], job_name='job_name',
                                                   cluster_instance_type='s', cluster_id=None, script_repo_id=None,
                                                   script_file_path_in_repo=None, auto_start=False,
                                                   upload_requirements_file=False, docker_image_id=None)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_constant_file(self, asset_upload_mock, path_is_dir_mock,
                                      path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using constant files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py -c const_file".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id='file_id', input_file_ids=[],
                                                   constants_file_ids=['file_id'], job_name='job_name',
                                                   cluster_instance_type='s', cluster_id=None, script_repo_id=None,
                                                   script_file_path_in_repo=None, auto_start=False,
                                                   upload_requirements_file=True, docker_image_id=None)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_many_files(self, asset_upload_mock, path_is_dir_mock,
                                   path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using many input and constant files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py "
                                            "-i input_file1,input_file2 "
                                            "-c const_file1,const_file2".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id='file_id', input_file_ids=['file_id', 'file_id'],
                                                   constants_file_ids=['file_id', 'file_id'], job_name='job_name',
                                                   cluster_instance_type='s', cluster_id=None, script_repo_id=None,
                                                   script_file_path_in_repo=None, auto_start=False,
                                                   upload_requirements_file=True, docker_image_id=None)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    @patch('disco.Cluster.fetch_and_validate_by_id')
    def test_create_job_many_files_with_cluster(self, cluster_fetch_and_validate_by_id,
                                                asset_upload_mock, path_is_dir_mock,
                                                path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using many input and cluster
        """
        script_file_id = self.random_str("script_file_id")
        input_file_id1 = self.random_str("input_file_id1")
        input_file_id2 = self.random_str("input_file_id2")

        script_file_name = 'script_file.py'
        input_filename1 = 'input1.txt'
        input_filename2 = 'input2.txt'

        job_name = self.random_str('job_name')
        cluster_id = self.random_str('cluster_id')
        cluster = ClusterDetails(dict(id=cluster_id, type=ClusterType.AWS.value))

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.side_effect = [input_file_id1, input_file_id2, script_file_id]
        cluster_fetch_and_validate_by_id.return_value = cluster
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open(script_file_name, 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create"
                                            f" --name {job_name} "
                                            f" --script {script_file_name} "
                                            f" --input {input_filename1},{input_filename2} "
                                            f" --cluster-id {cluster_id} ")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id=script_file_id,
                                                   input_file_ids=[input_file_id1, input_file_id2],
                                                   constants_file_ids=[], job_name=job_name,
                                                   cluster_instance_type='s', cluster_id=cluster_id,
                                                   script_repo_id=None,
                                                   script_file_path_in_repo=None, auto_start=False,
                                                   upload_requirements_file=True, docker_image_id=None)

                cluster_fetch_and_validate_by_id.assert_called_with(cluster_id)

                asset_upload_mock.assert_has_calls([
                    call(script_file_name, Path(script_file_name), cluster=cluster, show_progress_bar=True),
                    call(input_filename1, Path(input_filename1), cluster=cluster, show_progress_bar=True),
                    call(input_filename2, Path(input_filename2), cluster=cluster, show_progress_bar=True),
                ], any_order=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('pathlib.Path.glob')
    @patch('disco.asset.Asset.upload')
    def test_create_job_directory(self, asset_upload_mock, path_glob_mock, path_is_dir_mock,
                                  path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using directory as input
        Args:
            asset_upload_file_mock:
            path_glob_mock:
            path_is_dir_mock:
            path_exists_mock:
            job_create_mock:

        Returns:

        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        path_glob_mock.return_value = [Path('file1'), Path('file2')]
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py "
                                            "-i dir_path ")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id='file_id', input_file_ids=['file_id', 'file_id'],
                                                   constants_file_ids=[], job_name='job_name',
                                                   cluster_instance_type='s', cluster_id=None, script_repo_id=None,
                                                   script_file_path_in_repo=None, auto_start= False,
                                                   upload_requirements_file=True, docker_image_id=None)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('pathlib.Path.glob')
    @patch('disco.asset.Asset.upload')
    def test_create_job_wildcard(self, asset_upload_mock, path_glob_mock, path_is_dir_mock,
                                 path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using file with wildcards
        """
        script_file_id = self.random_str("script_file_id")
        input_file_id1 = self.random_str("input_file_id1")
        input_file_id2 = self.random_str("input_file_id2")

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.side_effect = [input_file_id1, input_file_id2, script_file_id]
        path_glob_mock.return_value = [Path('file1'), Path('file2')]
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f, open("input_file1.txt", 'w') as i1:
                sleep(1)
                i2 = open("input_file2.txt", 'w')
                input_file_contents1 = self.random_str("input_contents1")
                input_file_contents2 = self.random_str("input_contents2")
                i1.write(input_file_contents1)

                i2.write(input_file_contents2)
                i2.close()
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py "
                                            "-i inp* ")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Created job with id job_id')
                job_create_mock.assert_called_with(script_file_id=script_file_id,
                                                   input_file_ids=[input_file_id1, input_file_id2],
                                                   constants_file_ids=[], job_name='job_name',
                                                   cluster_instance_type='s', cluster_id=None, script_repo_id=None,
                                                   script_file_path_in_repo=None, auto_start=False,
                                                   upload_requirements_file=True, docker_image_id=None)

                asset_upload_mock.assert_has_calls([
                    call('script_file.py', Path('script_file.py'), cluster=None, show_progress_bar=True),
                    call('input_file1.txt', Path('input_file1.txt'), cluster=None, show_progress_bar=True),
                    call('input_file2.txt', Path('input_file2.txt'), cluster=None, show_progress_bar=True),
                ], any_order=True)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    def test_create_job_not_supported_script(self, path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Unsuccessful path for creating a job with a script file that is not supported
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file")
                assert result.exit_code == 0
                assert result.output == 'Cannot use script file. ' \
                                        'Currently only Python and bash scripts are supported\n'
                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('pathlib.Path.glob')
    def test_create_job_empty_directory(self, path_glob_mock, path_is_dir_mock,
                                        path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using directory as input
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = True
        path_glob_mock.return_value = []
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py "
                                            "-i dir_path ")
                assert result.exit_code == 0
                assert output_message_includes(result, 'Folder dir_path is empty')
                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    def test_create_job_missing_input(self, path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Unsuccessful path for creating a job with a script file that is not supported
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = False
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py -i input_file")
                assert result.exit_code == 0
                assert output_message_includes(result, 'input_file doesn\'t exist')
                job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    @patch('disco.Job.wait_for_finish')
    def test_create_job_wait_success(self, wait_for_finish_mock, asset_upload_mock, path_is_dir_mock,
                                   path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using input files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        wait_for_finish_mock.return_value = JobStatus.done
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli,
                                       "job create -n job_name -s script_file.py --run --wait".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Job job_id finished successfully')

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    @patch('disco.Job.wait_for_finish')
    def test_create_job_wait_failure(self, wait_for_finish_mock, asset_upload_mock, path_is_dir_mock,
                                     path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using input files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        wait_for_finish_mock.return_value = JobStatus.failed
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli,
                                       "job create -n job_name -s script_file.py --run --wait".split(' '))
                assert result.exit_code == 0
                assert output_message_includes(result, 'Job job_id failed')

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('disco.asset.Asset.upload')
    def test_create_job_script_file_in_home_dir(self, asset_upload_mock, job_create_mock, is_logged_in_mock):
        """
        Create job with script file from user's home directory, i.e `~/script_file.py`
        """
        script_file_id = self.random_str("script_file_id")
        input_file_id1 = self.random_str("input_file_id1")
        input_file_id2 = self.random_str("input_file_id2")
        constant_file_id = self.random_str("constant_file_id")

        is_logged_in_mock.return_value = True
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.side_effect = [input_file_id1, input_file_id2, constant_file_id, script_file_id]
        runner = CliRunner()

        script_filename = 'script_file.py'
        input_filename1 = 'input1.txt'
        input_filename2 = 'input2.txt'
        constant_filename = 'constant.txt'

        script_file_path = os.path.join("~", script_filename)
        input_file_path1 = os.path.join("~", input_filename1)
        input_file_path2 = os.path.join("~", input_filename2)
        constant_file_path = os.path.join("~", constant_filename)

        script_full_file_path = str(Path.home() / script_filename)
        input_file_full_path1 = str(Path.home() / input_filename1)
        input_file_full_path2 = str(Path.home() / input_filename2)
        constant_file_full_path = str(Path.home() / constant_filename)

        try:
            with open(script_full_file_path, 'w') as script_file:
                script_file.write("print('hi!')")

            with open(input_file_full_path1, 'w') as input_file1:
                input_file1.write(self.random_str('input1_content'))

            with open(input_file_full_path2, 'w') as input_file2:
                input_file2.write(self.random_str('input2_content'))

            with open(constant_file_full_path, 'w') as constant_file:
                constant_file.write(self.random_str('constant_file_content'))

            result = runner.invoke(cli, f"job create -n job_name --script {script_file_path} "
                                        f"--input {input_file_path1},{input_file_path2} "
                                        f"--constants {constant_file_path}")
            assert result.exit_code == 0
            assert output_message_includes(result, 'Created job with id job_id')
            job_create_mock.assert_called_with(script_file_id=script_file_id,
                                               input_file_ids=[input_file_id1, input_file_id2],
                                               constants_file_ids=[constant_file_id], job_name='job_name',
                                               cluster_instance_type='s', cluster_id=None, script_repo_id=None,
                                               script_file_path_in_repo=None, auto_start=False,
                                               upload_requirements_file=True, docker_image_id=None)

            asset_upload_mock.assert_has_calls([
                call(script_filename, Path(script_full_file_path), cluster=None, show_progress_bar=True),
                call(input_filename1, Path(input_file_full_path1), cluster=None, show_progress_bar=True),
                call(input_filename2, Path(input_file_full_path2), cluster=None, show_progress_bar=True),
                call(constant_filename, Path(constant_file_full_path), cluster=None, show_progress_bar=True),
            ], any_order=True)

        finally:
            os.remove(script_full_file_path)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_script_file_from_git_repository(self, asset_upload_mock, path_is_dir_mock,
                                    path_exists_mock, job_create_mock, is_logged_in_mock):
        """ Create job with script file from git repository with repository id and path. """
        job_name = self.random_str('job_name')
        input_file_id = self.random_str('input_file_id')
        repository_id = self.random_str('repository_id')
        file_path = 'file_path.py'
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job(job_id)
        asset_upload_mock.return_value = input_file_id
        runner = CliRunner()
        with runner.isolated_filesystem():
            command = f"job create -n {job_name} " \
                      f"-i {input_file_id} " \
                      f"-rep {repository_id} " \
                      f"-f {file_path}"
            result = runner.invoke(cli, command)
            assert result.exit_code == 0
            assert output_message_includes(result, f'Created job with id {job_id}')
            job_create_mock.assert_called_with(script_file_id=None, input_file_ids=[input_file_id],
                                               constants_file_ids=[], job_name=job_name, cluster_instance_type='s',
                                               cluster_id=None, script_repo_id=repository_id,
                                               script_file_path_in_repo=file_path, auto_start=False,
                                               upload_requirements_file=True, docker_image_id=None)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_script_file_from_git_repository_missing_file_path(self, asset_upload_mock, path_is_dir_mock,
                                    path_exists_mock, job_create_mock, is_logged_in_mock):
        """ Create job with script file from git repository - missing file path. """
        job_name = self.random_str('job_name')
        input_file_id = self.random_str('input_file_id')
        repository_id = self.random_str('repository_id')
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job(job_id)
        asset_upload_mock.return_value = input_file_id
        runner = CliRunner()
        with runner.isolated_filesystem():
            command = f"job create -n {job_name} " \
                      f"-i {input_file_id} " \
                      f"-rep {repository_id} "
            result = runner.invoke(cli, command)
            assert result.exit_code == 0
            assert result.output == "Please specify the script file path using `--file-path`\n"
            job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    def test_create_job_script_file_from_git_repository_not_supported_script(self,
                                                                             path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Unsuccessful path for creating a job with a script file that is not supported
        """
        job_name = self.random_str('job_name')
        input_file_id = self.random_str('input_file_id')
        repository_id = self.random_str('repository_id')
        file_path = self.random_str('file_path')
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        job_create_mock.return_value = Job(job_id)
        runner = CliRunner()
        with runner.isolated_filesystem():
            command = f"job create -n {job_name} " \
                      f"-i {input_file_id} " \
                      f"-rep {repository_id} " \
                      f"-f {file_path}"
            result = runner.invoke(cli, command)
            assert result.exit_code == 0
            assert result.output == 'Cannot use script file. ' \
                                    'Currently only Python and bash scripts are supported\n'
            job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_missing_script_file(self, asset_upload_mock, path_is_dir_mock,
                                    path_exists_mock, job_create_mock, is_logged_in_mock):
        """ Create job - no script file. """
        job_name = self.random_str('job_name')
        input_file_id = self.random_str('input_file_id')
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job(job_id)
        asset_upload_mock.return_value = input_file_id
        runner = CliRunner()
        with runner.isolated_filesystem():
            command = f"job create -n {job_name} -i {input_file_id} "
            result = runner.invoke(cli, command)
            assert result.exit_code == 0
            assert result.output == 'Please specify the script file using either `--script` or `--repository-id` with `--file-path`\n'
            job_create_mock.assert_not_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    def test_create_job_script_file_with_docker_image(self, asset_upload_mock, path_is_dir_mock,
                                    path_exists_mock, job_create_mock, is_logged_in_mock):
        """ Create job with script file from git repository with repository id and path. """
        job_name = self.random_str('job_name')
        input_file_id = self.random_str('input_file_id')
        repository_id = self.random_str('repository_id')
        docker_image_id = self.random_str(('docker_img_id'))
        file_path = 'file_path.py'
        job_id = self.random_str('job_id')

        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job(job_id)
        asset_upload_mock.return_value = input_file_id
        runner = CliRunner()
        with runner.isolated_filesystem():
            command = f"job create -n {job_name} " \
                      f"-i {input_file_id} " \
                      f"-rep {repository_id} " \
                      f"-f {file_path} " \
                      f"-did {docker_image_id}"
            result = runner.invoke(cli, command)
            assert result.exit_code == 0
            assert output_message_includes(result, f'Created job with id {job_id}')
            job_create_mock.assert_called_with(script_file_id=None, input_file_ids=[input_file_id],
                                               constants_file_ids=[], job_name=job_name, cluster_instance_type='s',
                                               cluster_id=None, script_repo_id=repository_id,
                                               script_file_path_in_repo=file_path, auto_start=False,
                                               upload_requirements_file=True, docker_image_id=docker_image_id)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.create')
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.is_dir')
    @patch('disco.asset.Asset.upload')
    @patch('disco.Job.wait_for_finish')
    def test_create_job_with_timeout(self, wait_for_finish_mock, asset_upload_mock, path_is_dir_mock,
                                   path_exists_mock, job_create_mock, is_logged_in_mock):
        """
        Successful path for creating a job using input files
        """
        is_logged_in_mock.return_value = True
        path_exists_mock.return_value = True
        path_is_dir_mock.return_value = False
        job_create_mock.return_value = Job("job_id")
        asset_upload_mock.return_value = 'file_id'
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('script_file.py', 'w') as f:
                f.write("print('hi!')")
                result = runner.invoke(cli, "job create -n job_name -s script_file.py --run --wait --timeout 1000".split(' '))
                assert result.exit_code == 0
                wait_for_finish_mock.assert_called_with(timeout=1000)

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.start')
    def test_start_job(self, job_start_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        runner = CliRunner()
        result = runner.invoke(cli, 'job start job_id')
        assert result.exit_code == 0
        assert result.output == 'Job job_id started\n'
        job_start_mock.assert_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.stop')
    def test_stop_job(self, job_stop_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        runner = CliRunner()
        result = runner.invoke(cli, 'job stop job_id')
        assert result.exit_code == 0
        assert result.output == 'Stopping job job_id\n'
        job_stop_mock.assert_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.archive')
    def test_archive_job(self, job_archive_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        runner = CliRunner()
        result = runner.invoke(cli, 'job archive job_id')
        assert result.exit_code == 0
        assert result.output == 'Job job_id was archived\n'
        job_archive_mock.assert_called()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Job.get_results')
    @patch('pathlib.Path.exists', return_value=True)
    @patch('pathlib.Path.is_dir', return_value=True)
    @patch('os.makedirs')
    @patch('disco.task.TaskResult.write_files')
    def test_download_results(self, write_files_mock, makedirs_mock, is_dir_mock, path_exists_mock,
                              get_results_mock, is_logged_in_mock):
        get_results_mock.return_value = [TaskResult('task_id', {'Iqoqo.stdout.log': 'some output'})]
        is_logged_in_mock.return_value = True
        runner = CliRunner()
        result = runner.invoke(cli, 'job download-results job_id -d destdir')
        assert result.exit_code == 0
        assert result.output == 'Results downloaded successfully\n'
        get_results_mock.assert_called()
        makedirs_mock.assert_called()
