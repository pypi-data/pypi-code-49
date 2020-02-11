import argparse
import json
import os
import tempfile

import certifi
import pytest
from ruamel.yaml import YAML

from flywheel_cli.bulk_import.config.global_config import GlobalConfig, GlobalConfigInitError


class MockArgs:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def test_config_read_config_no_config_arg():
    assert GlobalConfig.read_config_file(MockArgs(no_config=True)) is None


def test_config_read_config_file_json_fail():
    with pytest.raises(GlobalConfigInitError):
        GlobalConfig.read_config_file(MockArgs(config_file='non-existent.json'))


def test_config_read_config_file_yaml_fail():
    with pytest.raises(GlobalConfigInitError):
        GlobalConfig.read_config_file(MockArgs(config_file='non-existent.yml'))


def test_config_read_config_file_not_supported():
    with pytest.raises(GlobalConfigInitError):
        with tempfile.NamedTemporaryFile(suffix='.txt') as temp_file:
            GlobalConfig.read_config_file(MockArgs(config_file=temp_file.name))


def test_config_read_config_file_json(mocker):
    test_config = {
        'deid-profile': 'dicom',
        'assume-yes': True,
        'de-identify': True,
    }
    with tempfile.TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, 'test_config.json')
        with open(path, 'w') as json_file:
            json.dump(test_config, json_file)

        assert GlobalConfig.read_config_file(MockArgs(config_file=path)) == test_config


def test_config_read_config_file_yaml(mocker):
    test_config = {
        'deid-profile': 'dicom',
        'assume-yes': True,
        'de-identify': True,
    }
    with tempfile.TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, 'test_config.yml')
        yaml = YAML()
        with open(path, 'w') as yaml_file:
            yaml.dump(test_config, yaml_file)

        assert GlobalConfig.read_config_file(MockArgs(config_file=path)) == test_config


def test_config_quiet_log_level():
    mock_args = MockArgs(quiet=True)
    config = GlobalConfig(mock_args)
    assert config.quiet


def test_config_ca_certs():
    mock_args = MockArgs(ca_certs='cacert.pem')
    GlobalConfig(mock_args)
    assert certifi.where() == 'cacert.pem'


def test_config_add_arguments():
    parser = GlobalConfig.add_arguments(argparse.ArgumentParser())
    args = parser.parse_args(['--config-file', 'config_path', '-y', '--debug'])
    assert args.config_file == 'config_path'
    assert args.debug
    assert args.assume_yes


def test_config_add_arguments_mutually_exclusive_config():
    parser = GlobalConfig.add_arguments(argparse.ArgumentParser())
    with pytest.raises(SystemExit):
        args = parser.parse_args(['--config-file', 'config_path', '--no-config'])


def test_config_add_arguments_mutually_exclusive_log():
    parser = GlobalConfig.add_arguments(argparse.ArgumentParser())
    with pytest.raises(SystemExit):
        args = parser.parse_args(['--debug', '--quiet'])
