from mock import patch
from tests.base_test import BaseTest
from cli.utilities import  utils

class TestUtils(BaseTest):

    @patch('cli.utilities.utils._installed_version')
    def test_current_version_updated(self, mock_get_cli_installed_version):
        mock_get_cli_installed_version.return_value = "500.0.0"
        result = utils.is_update_needed()

        assert result == False

    @patch('cli.utilities.utils._installed_version')
    def test_current_version_not_updated(self, mock_get_cli_installed_version):
        mock_get_cli_installed_version.return_value = "1.0.0"
        result = utils.is_update_needed()

        assert result == True

    @patch('cli.utilities.utils._installed_version')
    def test_current_version_equal(self, mock_get_cli_installed_version):
        current_version = utils._latest_version()
        mock_get_cli_installed_version.return_value = current_version

        result = utils.is_update_needed()

        assert result == False