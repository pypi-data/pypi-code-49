"""
Tests bump.py
"""

from subprocess import STDOUT

import pytest
from click.testing import CliRunner

from brewblox_dev import repository

TESTED = repository.__name__


@pytest.fixture
def mocked_ext(mocker):
    mocked = [
        'check_output',
        'check_call',
        'makedirs',
        'path',
        'which',
        'utils',
    ]
    return {k: mocker.patch(TESTED + '.' + k) for k in mocked}


@pytest.mark.parametrize('bump_type,new_version', [
    ('major', '4.0.0'),
    ('minor', '3.3.0'),
    ('patch', '3.2.2')
])
def test_bump(mocked_ext, bump_type, new_version):
    mocked_ext['check_output'].return_value = b'1.2.3\n3.2.1\n'

    runner = CliRunner()
    assert not runner.invoke(repository.bump, [bump_type]).exception

    mocked_ext['check_output'].assert_any_call(f'git tag -a {new_version} -m "Version {new_version}"', shell=True)
    mocked_ext['check_call'].assert_any_call('git push --tags', shell=True, stderr=STDOUT)


def test_init(mocked_ext):
    mocked_ext['check_output'].return_value = b'1.2.3\n3.2.1\n'

    runner = CliRunner()
    assert not runner.invoke(repository.bump, ['minor', '--init']).exception

    mocked_ext['check_output'].assert_any_call(f'git tag -a 0.1.0 -m "Version 0.1.0"', shell=True)
    mocked_ext['check_call'].assert_any_call('git push --tags', shell=True, stderr=STDOUT)


def test_bump_no_push(mocked_ext):
    mocked_ext['check_output'].return_value = b'1.2.3\n3.2.1\n'
    mocked_ext['utils'].confirm.side_effect = [True, False]

    runner = CliRunner()
    assert not runner.invoke(repository.bump, ['minor']).exception

    mocked_ext['check_output'].assert_any_call(f'git tag -a 3.3.0 -m "Version 3.3.0"', shell=True)
    assert mocked_ext['check_call'].call_count == 0


def test_bump_nok(mocked_ext):
    mocked_ext['check_output'].return_value = b'1.2.3\n3.2.1\n'
    mocked_ext['utils'].confirm.side_effect = [False]

    runner = CliRunner()
    assert not runner.invoke(repository.bump, ['minor']).exception

    assert mocked_ext['check_output'].call_count == 1


def test_install_hub(mocked_ext):
    mocked_ext['which'].return_value = False
    repository.prepare()
    assert mocked_ext['check_output'].call_count == 4


def test_git_info(mocked_ext):
    runner = CliRunner()
    assert not runner.invoke(repository.git_info).exception


def test_delta(mocked_ext):
    runner = CliRunner()
    assert not runner.invoke(repository.delta).exception


def test_release_edge(mocked_ext):
    runner = CliRunner()
    assert not runner.invoke(repository.release_edge).exception
    assert mocked_ext['check_call'].call_count == len(repository.REPOS)

    mocked_ext['utils'].confirm.return_value = False
    assert not runner.invoke(repository.release_edge).exception
    assert mocked_ext['check_call'].call_count == len(repository.REPOS)
