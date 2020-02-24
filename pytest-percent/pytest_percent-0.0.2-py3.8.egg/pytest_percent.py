# -*- coding: utf-8 -*-

import logging

import pytest

LOGGER = logging.getLogger(__name__)
REQUIRED_PERCENT = 100


def pytest_addoption(parser):
    parser.addoption(
        '--required-percent',
        action='store',
        help='Percent of tests required to pass.',
    )


def pytest_configure(config):
    global REQUIRED_PERCENT
    required_percent = config.getoption('--required-percent')
    if isinstance(required_percent, float):
        required_percent *= 100
        required_percent = int(required_percent)
    if isinstance(required_percent, int):
        REQUIRED_PERCENT = required_percent
    LOGGER.info(f'Required percent set to {REQUIRED_PERCENT}%')


@pytest.mark.trylast
def pytest_sessionfinish(session, exitstatus):
    if passed_percent := int((session.testsfailed / session.testscollected) * 100) >= REQUIRED_PERCENT:
        LOGGER.info(f'{passed_percent}% of tests passed, required {REQUIRED_PERCENT}%.')
        exitstatus = pytest.ExitCode.OK
    else:
        LOGGER.error(f'{passed_percent}% of tests passed, required {REQUIRED_PERCENT}%.')


@pytest.fixture(scope='session')
def required_percent():
    return REQUIRED_PERCENT


__version__ = '0.0.2'
