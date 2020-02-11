"""Tests brewblox_dev.docker"""


import json
from unittest.mock import mock_open

import pytest
from click.testing import CliRunner

from brewblox_dev import docker

TESTED = docker.__name__


@pytest.fixture
def mocked_ext(mocker):
    mocked = [
        'utils',
        'path',
        'makedirs',
    ]
    return {k: mocker.patch(TESTED + '.' + k) for k in mocked}


def test_enable_experimental(mocker, mocked_ext):
    content = {'experimental': True}
    mocker.patch(TESTED + '.open', mock_open(read_data=json.dumps(content)))
    docker.enable_experimental()

    mocker.patch(TESTED + '.open', mock_open(read_data=''))
    docker.enable_experimental()


def test_install_qemu(mocked_ext):
    docker.install_qemu()
    assert mocked_ext['utils'].run.call_count == 3


def test_docker_info():
    runner = CliRunner()
    assert not runner.invoke(docker.docker_info).exception


def test_docker_images(mocker, mocked_ext):
    mocker.patch(TESTED + '.open', mock_open())

    runner = CliRunner()
    assert not runner.invoke(docker.docker_images, ['--python']).exception
    assert not runner.invoke(docker.docker_images, ['--node']).exception
    assert not runner.invoke(docker.docker_images, ['--python', '--node']).exception


def test_release_stable(mocked_ext):
    runner = CliRunner()
    assert not runner.invoke(docker.release_stable).exception
