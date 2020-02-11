"""
Tests localbuild.py
"""

from unittest.mock import call

import pytest
from click.testing import CliRunner

from brewblox_dev import localbuild

TESTED = localbuild.__name__


@pytest.fixture
def mocked_ext(mocker):
    mocked = [
        'glob',
        'getenv',
        'remove',
        'check_output',
        'utils',
    ]
    return {k: mocker.patch(TESTED + '.' + k) for k in mocked}


def localbuild_sh(context):
    return f'cd {context} && if [ -f ./localbuild.sh ]; then bash ./localbuild.sh; fi'


def test_localbuild_simple(mocked_ext):
    utils = mocked_ext['utils']
    mocked_ext['glob'].return_value = ['f1', 'f2']
    mocked_ext['getenv'].side_effect = [
        'bb-repo',
    ]

    runner = CliRunner()
    assert not runner.invoke(localbuild.localbuild).exception

    assert utils.distcopy.call_args_list == [
        call('dist/', ['docker/dist/']),
    ]
    assert mocked_ext['remove'].call_args_list == [
        call('f1'),
        call('f2'),
    ]
    assert utils.run.call_args_list == [
        call('python setup.py sdist'),
        call('pipenv lock --requirements > docker/requirements.txt'),
        call(localbuild_sh('docker')),
        call('docker build ' +
             '--build-arg service_info="$(git describe) @ $(date)" ' +
             '--no-cache --tag bb-repo:local --file docker/amd/Dockerfile docker')
    ]


def test_localbuild_all(mocked_ext):
    utils = mocked_ext['utils']
    mocked_ext['glob'].return_value = ['f1', 'f2']
    mocked_ext['getenv'].side_effect = [
        'bb-repo',
        'feature/funky_branch',
    ]

    runner = CliRunner()
    assert not runner.invoke(
        localbuild.localbuild,
        ['--arch', 'amd',
         '--arch', 'arm',
         '--tag', 'test:tag',
         '--push',
         '--branch-tag',
         '--pull',
         '--context', 'dk',
         '--file', 'df',
         ]
    ).exception

    assert utils.distcopy.call_args_list == [
        call('dist/', ['dk/dist/']),
    ]
    assert utils.run.call_args_list == [
        call('python setup.py sdist'),
        call('pipenv lock --requirements > dk/requirements.txt'),
        call(localbuild_sh('dk')),
        call('docker build --pull ' +
             '--build-arg service_info="$(git describe) @ $(date)" --no-cache ' +
             '--tag bb-repo:local ' +
             '--tag bb-repo:test-tag ' +
             '--tag bb-repo:feature-funky-branch ' +
             '--file dk/amd/df ' +
             'dk'),
        call('docker push bb-repo:test-tag'),
        call('docker push bb-repo:feature-funky-branch'),
        call('docker run --rm --privileged multiarch/qemu-user-static:register --reset ' +
             '&& ' +
             'docker build --pull ' +
             '--build-arg service_info="$(git describe) @ $(date)" --no-cache ' +
             '--tag bb-repo:rpi-local ' +
             '--tag bb-repo:rpi-test-tag ' +
             '--tag bb-repo:rpi-feature-funky-branch ' +
             '--file dk/arm/df ' +
             'dk'),
        call('docker push bb-repo:rpi-test-tag'),
        call('docker push bb-repo:rpi-feature-funky-branch'),
    ]


def test_localbuild_no_setup(mocked_ext):
    utils = mocked_ext['utils']
    mocked_ext['glob'].return_value = ['f1', 'f2']
    mocked_ext['getenv'].side_effect = [
        'bb-repo',
    ]

    runner = CliRunner()
    assert not runner.invoke(localbuild.localbuild, ['--no-setup']).exception

    assert utils.distcopy.call_count == 0
    assert mocked_ext['remove'].call_count == 0
    assert utils.run.call_args_list == [
        call(localbuild_sh('docker')),
        call('docker build ' +
             '--build-arg service_info="$(git describe) @ $(date)" ' +
             '--no-cache --tag bb-repo:local --file docker/amd/Dockerfile docker')
    ]
