import mock
import pkg_resources
from tests.base_test import BaseTest
from disco.core import utils


class TestUtils(BaseTest):
    @mock.patch('pkg_resources.get_distribution')
    def test_installed_version_ok(self, _get_distribution: mock.MagicMock):
        pkg = self.random_str('pkg')
        version = self.random_str('version')
        res = mock.MagicMock(version=version)

        _get_distribution.return_value = res
        assert utils.pkg_version(pkg) == version
        _get_distribution.assert_called_once_with(pkg)

    @mock.patch('pkg_resources.get_distribution')
    def test_installed_version_none(self, _get_distribution):
        pkg = self.random_str('pkg')

        _get_distribution.side_effect = pkg_resources.DistributionNotFound
        assert utils.pkg_version(pkg) is None
        _get_distribution.assert_called_once_with(pkg)
