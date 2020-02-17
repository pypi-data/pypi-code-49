import importlib
from pathlib import Path
from unittest.mock import Mock

import pytest

from tests import RESOURCE_PATH

from click.testing import CliRunner

from yeahyeah.persistence import YeahYeahPersistenceException


@pytest.fixture
def mock_config_path(tmpdir, monkeypatch):
    config_path = Path(tmpdir)
    monkeypatch.setattr('yeahyeah.config.CORE_CONFIG_PATH', config_path)
    return config_path


def test_cli_read_settings(mock_config_path, disable_click_echo):
    # run cli without settings file
    runner = CliRunner()
    yeahyeah_lib = importlib.import_module('yeahyeah.cli')
    runner.invoke(yeahyeah_lib.yeahyeah, catch_exceptions=False)


def test_cli_read_settings_corrupted(monkeypatch):
    # run cli with corrupt settings file
    mock_get_settings = Mock(side_effect=YeahYeahPersistenceException(
        "Could not read settings. These settings are weird"))
    monkeypatch.setattr("yeahyeah.core.YeahYeah.get_settings",  mock_get_settings)
    runner = CliRunner()
    yeahyeah_lib = importlib.import_module('yeahyeah.cli')
    result = runner.invoke(yeahyeah_lib.yeahyeah, catch_exceptions=False)
    assert result.exit_code == 0
#    assert 'Please check' in result.output

