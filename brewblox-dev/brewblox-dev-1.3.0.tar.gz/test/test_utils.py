"""Tests brewblox_dev.utils"""

import pytest

from brewblox_dev import utils

TESTED = utils.__name__


@pytest.fixture
def mocked_ext(mocker):
    mocked = [
        'input',
        'pathlib',
        'remove',
        'copy',
        'check_call',
        'glob'
    ]
    return {k: mocker.patch(TESTED + '.' + k) for k in mocked}


@pytest.mark.parametrize('user_input,expected', [
    (['y'], True),
    (['n'], False),
    (['Y'], True),
    (['N'], False),
    (['Yes'], True),
    (['No'], False),
    (['y', 'n'], True),
    (['n', 'y'], False),
    (['maybe', 'y'], True),
    (['maybe', 'I think so...', 'n'], False),
    ([''], True),
])
def test_user_yes_no_query(mocked_ext, user_input, expected):
    mocked_ext['input'].side_effect = user_input
    assert utils.confirm('Are you sure?') == expected


def test_run(mocked_ext):
    utils.run('cmd')
    mocked_ext['check_call'].assert_called_once_with('cmd', shell=True, stderr=utils.STDOUT)


def test_distcopy(mocked_ext):
    mocked_ext['glob'].side_effect = [
        ['dest1.1', 'dest1.2'],
        ['source1.1', 'source1.2'],
        ['dest2.1', 'dest2.2'],
        ['source2.1', 'source2.2', 'source2.3'],
    ]

    utils.distcopy('s', ['d1', 'd2'])
    assert mocked_ext['remove'].call_count == 4
    assert mocked_ext['copy'].call_count == 5
