# -*- coding: utf-8 -*-
import os

import pytest

INIT_FORBIDDEN_IN = {'scripts', 'notebooks'}
INIT_FILENAME = '__init__.py'


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption(
        '--init-check',
        action='store_true',
        help='Perform checks for __init__.py presence in certain forbidden folders')


def pytest_collect_file(path, parent):
    config = parent.config
    basename = os.path.basename(path.dirname)
    filename = path.basename
    if config.option.init_check and basename in INIT_FORBIDDEN_IN:
        return InitCheckItem(path, parent, basename, filename)


class ForbiddenInitError(Exception):
    """ Indicates missing newline at the end of file. """

    def __init__(self, path, basename):
        self.path = path.dirname
        self.basename = basename

    def get_message(self):
        return f'{self.path}: {INIT_FILENAME} forbidden under {self.basename} directory'


class InitCheckItem(pytest.Item, pytest.File):

    def __init__(self, path, parent, basename, filename):
        super().__init__(path, parent)
        self.basename = basename
        self.filename = filename

        self.add_marker('init-check')

    def runtest(self):
        if self.filename == INIT_FILENAME:
            raise ForbiddenInitError(self.fspath, self.basename)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(ForbiddenInitError):
            return excinfo.value.get_message()
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, -1, 'init-check'
