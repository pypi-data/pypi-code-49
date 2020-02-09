from mock import patch
from click.testing import CliRunner

from disco.core.exceptions import InvalidCredentials
from disco_cli import cli, setup_cli
from .cli_test_utils import output_message_includes

from tests.base_test import BaseTest


class TestAuthCommands(BaseTest):

    def setup_class(self):
        setup_cli()

    def test_login_success(self):
        """
        Tests a successful login
        Returns:

        """
        with patch('disco.gql.authentication.Authentication.login') as login_mock:
            runner = CliRunner()
            result = runner.invoke(cli, ['login', '-u', 'user@user.com', '-p', 'password'])
            assert result.exit_code == 0
            login_mock.assert_called_with('user@user.com', 'password')
            assert result.output == 'Signed in successfully\n'

    def test_login_fail(self):
        """
        Tests a login with wrong password
        Returns:

        """
        with patch('disco.gql.authentication.Authentication.login') as login_mock:
            login_mock.side_effect = InvalidCredentials("Wrong email or password")
            runner = CliRunner()
            result = runner.invoke(cli, ['login', '-u', 'user@user.com', '-p', 'password'])
            assert result.exit_code == 0
            assert result.output == 'Wrong username or password\n'

    def test_logout(self):
        """
        Tests logout
        """
        with patch('disco.gql.authentication.Authentication.logout') as logout_mock:
            runner = CliRunner()
            result = runner.invoke(cli, ['logout'])
            assert result.exit_code == 0
            logout_mock.assert_called()
            assert result.output == 'Logged out successfully\n'


