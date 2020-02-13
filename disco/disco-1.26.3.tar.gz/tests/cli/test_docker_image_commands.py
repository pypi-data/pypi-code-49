from tests.base_test import BaseTest
from disco_cli import cli, setup_cli
from mock import patch
from click.testing import CliRunner
from .cli_test_utils import output_message_includes
from disco.models import DockerImageDetails

class TestDockerImage(BaseTest):

    def setup_class(self):
        setup_cli()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.DockerImage.list_docker_images')
    def test_list_docker_images(self, list_docker_images_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        list_docker_images = [
            DockerImageDetails({'id': '5e143698be608b000c6064b0', 'displayName': 'docker 1',
                                'repositoryType': 'dockerHub', 'path': 'path1', 'entryPoint': 'ep1'}),
            DockerImageDetails({'id': '5e143698be608b000c6064b1', 'displayName': 'docker 2',
                                'repositoryType': 'aws', 'path': 'path2', 'entryPoint': 'ep2'})
        ]

        list_docker_images_mock.return_value = list_docker_images
        runner = CliRunner()
        result = runner.invoke(cli, ['docker', 'list'])
        assert result.exit_code == 0
        list_docker_images_mock.assert_called()
        assert output_message_includes(result, '| 5e143698be608b000c6064b0 | docker 1 | dockerHub         | path1  | ep1           |')
        assert output_message_includes(result, '| 5e143698be608b000c6064b1 | docker 2 | aws               | path2  | ep2           |')

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.DockerImage.list_docker_images')
    def test_empty_list_docker_images(self, list_docker_images_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        list_docker_images = []

        list_docker_images_mock.return_value = list_docker_images
        runner = CliRunner()
        result = runner.invoke(cli, ['docker', 'list'])
        assert result.exit_code == 0
        list_docker_images_mock.assert_called()
        assert result.output == 'There are no set docker images for your account\n'

