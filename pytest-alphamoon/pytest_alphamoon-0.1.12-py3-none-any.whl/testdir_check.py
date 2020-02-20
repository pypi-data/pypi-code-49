# -*- coding: utf-8 -*-
"""
NOTE:
    This plugin should have been based on pytest's test discovery, but since this requires
    analysis of gathered tests at different pytest stage, for now plugin implements own
    discovery, which reports failure each time when function / class / file
    contains 'test' token without being under tests/ directory
"""
import os
import re

import pytest

test_files_patterns = [
    r'test[\w]*\.py',
    r'[\w]*test\.py',
]

TEST_DIR_REQUIRED_TOKEN = 'tests'


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption(
        '--testdir-check',
        action='store_true',
        help='Perform initial tests placement checks')


def pytest_collect_file(path, parent):
    config = parent.config
    filename = path.basename
    if config.option.testdir_check and any(
            re.match(pattern, filename) for pattern in test_files_patterns):
        rel_path = config.rootdir.bestrelpath(path)
        return TestdirCheckItem(path, parent, rel_path)


class TestdirCheckError(Exception):
    """ Indicates error during checks of placement of test functions . """

    def __init__(self, path, err_message):
        self.path = path
        self.err_message = err_message

    def get_message(self):
        return f'{self.path}: {self.err_message}'


class TestdirCheckItem(pytest.Item, pytest.File):

    def __init__(self, path, parent, rel_path):
        super().__init__(path, parent)
        self.rel_path = rel_path
        self.add_marker('testdir-check')

    def runtest(self):
        testdir_err = check_testdir(self.rel_path)

        if testdir_err:
            raise TestdirCheckError(self.fspath, testdir_err)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(TestdirCheckError):
            return excinfo.value.get_message()
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, -1, 'testdir-check'


def check_testdir(rel_path):
    path_components = rel_path.split(os.sep)
    for component in path_components:
        if TEST_DIR_REQUIRED_TOKEN == component:
            return ''
    return f'Invalid test file placement, tests should be placed under ' \
           f'{TEST_DIR_REQUIRED_TOKEN}/ directory'
