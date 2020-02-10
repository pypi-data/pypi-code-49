from tests.base_test import BaseTest
from mock import patch
import mock
import disco


class TestRepositories(BaseTest):

    @BaseTest.with_config_and_env(authenticated=True)
    @patch('disco.gql.authentication.Authentication.get_current_user_id')
    def test_list_repositories(self, get_current_user_id_mock):
        get_current_user_id_mock.return_value = '123'
        with mock.patch('disco.gql.authentication.Authentication.query') as graphql_mock:
            graphql_mock.return_value = {'getArtifactsRepositories': [
                {'id': '5e143698be608b000c6064b0', 'displayName': 'Repository1', 'isActive': True},
                {'id': '5e143698be608b000c6064b1', 'displayName': 'Repository2', 'isActive': False},
                {'id': '5e143698be608b000c6064b2', 'displayName': 'Repository3', 'isActive': True}]}

            result = disco.Repository.list_repositories()

        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0].id == '5e143698be608b000c6064b0'
        assert result[0].name == 'Repository1'
        assert result[1].id == '5e143698be608b000c6064b2'
        assert result[1].name == 'Repository3'


