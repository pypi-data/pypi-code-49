import argparse
import encodings
import multiprocessing

import pytest

from flywheel_cli.bulk_import.config.config import BaseImporterConfig, BulkImportConfig


class MockArgs:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def test_config_register_encoding_aliases(mocker):
    mocker.patch.dict(encodings.aliases.aliases, {}, clear=True)
    BaseImporterConfig.register_encoding_aliases(['win_1251=cp1251'])
    assert encodings.aliases.aliases == {'win_1251': 'cp1251'}


def test_config_register_encoding_aliases_called(mocker):
    mocker.patch.object(BaseImporterConfig, 'register_encoding_aliases')
    config = BaseImporterConfig.from_multi_src([MockArgs(encodings='win_1251=cp1251')])
    config.register_encoding_aliases.assert_called_once()


def test_config_cpu_count(mocker):
    mocker.patch.object(multiprocessing, 'cpu_count', return_value=8)
    config = BulkImportConfig(MockArgs(jobs=-1))
    assert config.cpu_count == 4


def test_config_overwrite_config(mocker):
    test_config = {
        'max_retries': 4,
        'jobs': 1}
    mocker.patch.object(BulkImportConfig, 'read_config_file', return_value=test_config)
    config = BulkImportConfig(MockArgs(max_retries=5, jobs=2))
    assert config.cpu_count == 2


def test_config_add_arguments():
    parser = BulkImportConfig.add_arguments(argparse.ArgumentParser())
    args = parser.parse_args(['--jobs', '4'])
    assert args.jobs == 4
