from tests.base_test import BaseTest
from mock import patch
import mock
import disco


class TestDockerImages(BaseTest):

    @BaseTest.with_config_and_env(authenticated=True)
    # @patch('disco.gql.authentication.Authentication.get_current_user')
    def test_list_docker_images(self):
        with mock.patch('disco.gql.authentication.Authentication.query') as graphql_mock:
            graphql_mock.return_value = {'getDockerImagesByOwnerId': [
                {'id': '5e143698be608b000c6064b0', 'displayName': 'docker 1', 'repositoryType': 'dockerHub',
                 'path': 'path1', 'entryPoint': 'ep1', 'isActive': True},
                {'id': '5e143698be608b000c6064b1', 'displayName': 'docker 2', 'repositoryType': 'aws',
                 'path': 'path2', 'entryPoint': 'ep2', 'isActive': True},
                {'id': '5e143698be608b000c6064b2', 'displayName': 'docker 3', 'repositoryType': 'gcp',
                 'path': 'path3', 'entryPoint': 'ep3', 'isActive': False}]}

            result = disco.DockerImage.list_docker_images()

        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0].id == '5e143698be608b000c6064b0'
        assert result[0].name == 'docker 1'
        assert result[0].repository_type == 'dockerHub'
        assert result[0].path == 'path1'
        assert result[0].entry_point == 'ep1'
        assert result[1].id == '5e143698be608b000c6064b1'
        assert result[1].name == 'docker 2'
        assert result[1].repository_type == 'aws'
        assert result[1].path == 'path2'
        assert result[1].entry_point == 'ep2'


