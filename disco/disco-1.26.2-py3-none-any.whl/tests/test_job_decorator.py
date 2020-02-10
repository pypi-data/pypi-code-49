#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import os

import mock

from disco.core import constants as const
from .helper import add


class MockTaskResult:
    raw_result_mock = (('result.pickle', b'\x80\x03K\x03.'),
                       ('IqoqoTask.stdout.0.txt',
                        b'result is:  3\nand the result is (drumroll):  3\nresult is:  3\n'),
                       ('IqoqoTask.stderr.0.txt', b''))

    def __init__(self):
        pass

    def get_raw_result(self):
        return self.raw_result_mock


class MockFailedTaskResult:
    raw_result_mock = (('IqoqoTask.stdout.0.txt', b'fail'),
                       ('IqoqoTask.stderr.0.txt', b'error: failed'))

    def __init__(self):
        pass

    def get_raw_result(self):
        return self.raw_result_mock


class MockJob:
    def __init__(self):
        pass

    def start(self):
        pass

    @staticmethod
    def get_results(block):
        return [MockTaskResult()]


class MockFailedJob:
    def __init__(self):
        pass

    def start(self):
        pass

    @staticmethod
    def get_results(block):
        return [MockFailedTaskResult()]


job = MockJob()


@mock.patch.dict(os.environ,
                 {const.ENV_VAR_EMAIL_NAME: 'i@dis.co',
                  const.ENV_VAR_PASSWORD_NAME: 'wheel'},
                 clear=True)
@mock.patch('disco.asset.upload_file', return_value="some_id")
@mock.patch('disco.Job.create', return_value=job)
def test_disco_job_success(job_add_mock, upload_file_mock):
    result = add(1, 2)
    assert upload_file_mock.call_count == 2
    assert job_add_mock.call_count == 1
    # We have two versions here depending on the python version
    assert upload_file_mock.call_args_list[1][0][1] == b'(L1L\nL2L\ntp0\n.' or \
           upload_file_mock.call_args_list[1][0][1] == b'(I1\nI2\ntp0\n.'
    assert job_add_mock.call_args_list[0][0][0] == "some_id"
    assert job_add_mock.call_args_list[0][0][1] == ["some_id"]
    assert result == 3


failed_job = MockFailedJob()


@mock.patch.dict(os.environ,
                 {const.ENV_VAR_EMAIL_NAME: 'i@dis.co',
                  const.ENV_VAR_PASSWORD_NAME: 'wheel'},
                 clear=True)
@mock.patch('disco.asset.upload_file', mock.MagicMock(return_value="some_id"))
@mock.patch('disco.Job.create', mock.MagicMock(return_value=failed_job))
def test_disco_job_fail():
    result = add(1, 2)
    assert not result
