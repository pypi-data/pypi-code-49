from tests.base_test import BaseTest
from disco_cli import cli, setup_cli
from mock import patch
from click.testing import CliRunner
from .cli_test_utils import output_message_includes
from disco.models import RepositoryDetails

class TestRepository(BaseTest):

    def setup_class(self):
        setup_cli()

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Repository.list_repositories')
    def test_list_repositories(self, list_repositories_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        list_repositories = [
            RepositoryDetails({'id': '5e143698be608b000c6064b0', 'displayName': 'test repository 1', 'is_active': True}),
            RepositoryDetails({'id': '5e1c62f8a1c673000c1e68a3', 'displayName': 'test repository 2', 'is_active': True})
        ]

        list_repositories_mock.return_value = list_repositories
        runner = CliRunner()
        result = runner.invoke(cli, ['repository', 'list'])
        assert result.exit_code == 0
        list_repositories_mock.assert_called()
        assert output_message_includes(result, '| 5e143698be608b000c6064b0 | test repository 1 |')
        assert output_message_includes(result, '| 5e1c62f8a1c673000c1e68a3 | test repository 2 |')

    @patch('disco.gql.authentication.Authentication.is_logged_in')
    @patch('disco.Repository.list_repositories')
    def test_empty_list_repositories(self, list_repositories_mock, is_logged_in_mock):
        is_logged_in_mock.return_value = True
        list_repositories = []

        list_repositories_mock.return_value = list_repositories
        runner = CliRunner()
        result = runner.invoke(cli, ['repository', 'list'])
        assert result.exit_code == 0
        list_repositories_mock.assert_called()
        assert result.output == 'There are no set repositories for your account\n'




