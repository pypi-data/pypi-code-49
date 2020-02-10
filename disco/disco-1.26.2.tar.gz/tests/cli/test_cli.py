from click.testing import CliRunner
from mock import patch
from requests import ConnectionError, HTTPError

from tests.base_test import BaseTest
from disco_cli import main, setup_cli


class TestCli(BaseTest):

    def setup_class(self):
        setup_cli()

    @patch('disco_cli.cli')
    @patch('click.echo')
    def test_no_connection(self, click_echo, cli):
        cli.side_effect = ConnectionError
        main()
        click_echo.assert_called_with("\x1b[31mCouldn't establish internet connection. "
                                      "Please connect to the internet and try again\x1b[0m")

    @patch('disco_cli.cli')
    @patch('click.echo')
    def test_unknown_exception(self, click_echo, cli):
        cli.side_effect = InterruptedError
        main()
        click_echo.assert_called_with("\x1b[31mUnknown error occurred\x1b[0m")

    @patch('disco_cli.cli')
    @patch('click.echo')
    def test_unknown_server_error(self, click_echo, cli):
        cli.side_effect = HTTPError
        main()
        click_echo.assert_called_with("\x1b[31mUnknown error received from server\x1b[0m")


