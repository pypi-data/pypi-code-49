#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from unittest.mock import Mock

import pytest
from click.testing import CliRunner

from yeahyeah.persistence import YeahYeahPersistenceException
from yeahyeah_plugins.clockify_plugin.core import ClockifyPlugin
from yeahyeah_plugins.path_item_plugin.core import PathItemPlugin
from yeahyeah_plugins.url_pattern_plugin.core import UrlPatternsPlugin
from yeahyeah.plugin_testing import MockContextCliRunner

from yeahyeah.core import YeahYeah, YeahYeahSettings, YeahYeahSettingsFile, \
    assert_yeahyeah_settings, DEFAULT_YEAHYEAH_SETTINGS
from tests import RESOURCE_PATH


@pytest.fixture(autouse=True)
def disable_click_echo(monkeypatch):
    """Don't print click.echo to console. Click runner disables this, but not
    all tests use click runner to invoke all commands. So this is needed"""
    monkeypatch.setattr("yeahyeah.core.click.echo", Mock())


@pytest.fixture()
def a_yeahyeah_instance(tmpdir):
    """YeahYeah instance with tmp configuration path and default yeahyeah_plugins """

    return YeahYeah(configuration_path=Path(str(tmpdir)))


@pytest.fixture()
def a_yeahyeah_instance_with_plugins(a_yeahyeah_instance):
    """YeahYeah instance with tmp configuration path and default yeahyeah_plugins """

    jj = a_yeahyeah_instance

    jj.add_plugin_instance(ClockifyPlugin.init_from_context(context=jj.context))
    jj.add_plugin_instance(PathItemPlugin.init_from_context(context=jj.context))
    jj.add_plugin_instance(UrlPatternsPlugin.init_from_context(context=jj.context))

    return jj


@pytest.fixture()
def mock_cli_runner(a_yeahyeah_instance_with_plugins):
    """Runner that injects default context into each call, configuration path is
     tmpdir"""
    return MockContextCliRunner(mock_context=a_yeahyeah_instance_with_plugins.context)


def test_command_line_interface(a_yeahyeah_instance_with_plugins, mock_cli_runner):
    """Test the CLI."""
    result = mock_cli_runner.invoke(a_yeahyeah_instance_with_plugins.root_cli)
    assert result.exit_code == 0


def test_command_admin_status(a_yeahyeah_instance_with_plugins, mock_cli_runner):
    """Test the yeahyeah admin command"""
    result = mock_cli_runner.invoke(a_yeahyeah_instance_with_plugins.root_cli,
                                    args='admin yeahyeah status'.split(' '))
    assert result.exit_code == 0


@pytest.fixture
def disable_click_launch(monkeypatch):
    """Make sure click.launch does not actually launch anything"""
    mock_launch = Mock()
    monkeypatch.setattr('yeahyeah.core.click.launch', mock_launch)
    return mock_launch


def test_command_admin_edit_plugins(a_yeahyeah_instance, mock_cli_runner,
                                    disable_click_launch):
    """Test the yeahyeah admin command"""
    result = mock_cli_runner.invoke(a_yeahyeah_instance.root_cli,
                                    args='admin yeahyeah edit-plugins'.split(' '))
    assert result.exit_code == 0
    assert disable_click_launch.called


def test_yeahyeah_settings_load():
    settings_file = YeahYeahSettingsFile(path=RESOURCE_PATH / 'yeahyeah_settings.json')
    settings = settings_file.load_settings()
    assert settings.plugin_paths == ['someplugin.core.SomePlugin',
                                     'otherplugin.core.OtherPlugin']


def test_yeahyeah_settings_assert(tmpdir):
    # non-existent path should force default file creation
    path = Path(tmpdir) / 'test_settings'
    assert not path.exists()
    settings = assert_yeahyeah_settings(path)
    assert path.exists()
    assert settings == DEFAULT_YEAHYEAH_SETTINGS

    # now load existing file. Should not modify
    settings = assert_yeahyeah_settings(RESOURCE_PATH / 'yeahyeah_settings.json')
    assert len(settings.plugin_paths) == 2


def test_yeahyeah_settings_load_errors():
    """Load settings from corrupted and non-existent files"""
    with pytest.raises(YeahYeahPersistenceException):
        YeahYeahSettingsFile(
            path=RESOURCE_PATH / 'yeahyeah_settings_corrupt.json').load_settings()
    with pytest.raises(FileNotFoundError):
        YeahYeahSettingsFile(
                path='non_existent_path').load_settings()


def test_plugin_load(a_yeahyeah_instance, disable_click_echo):
    """Load a valid plugin as class"""
    assert len(a_yeahyeah_instance.plugins) == 0
    a_yeahyeah_instance.add_plugin(UrlPatternsPlugin)
    assert len(a_yeahyeah_instance.plugins) == 1


def test_plugin_load_as_path(a_yeahyeah_instance, disable_click_echo):
    """Load a valid plugin by import path"""
    assert len(a_yeahyeah_instance.plugins) == 0
    plugin_path = "yeahyeah_plugins.url_pattern_plugin.core.UrlPatternsPlugin"
    a_yeahyeah_instance.add_plugin(plugin_path)
    assert len(a_yeahyeah_instance.plugins) == 1


def test_plugin_load_errors(a_yeahyeah_instance):
    """Load all kinds of crap but not valid plugin. Helpful exceptions should happen
    """
    # A non-existent import path
    with pytest.raises(ModuleNotFoundError):
        a_yeahyeah_instance.add_plugin("non_existent.import.path.Plugin")

    with pytest.raises(AttributeError):
        a_yeahyeah_instance.add_plugin("tests.conftest.MockContextCliRunner")


