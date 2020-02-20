# -*- coding: utf-8 -*-
import os

import pytest

REQUIRED_NEWLINE_IN = {
    'requirements*',
    '.gitignore',
    'Pipfile',
}


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption(
        '--newline-check',
        action='store_true',
        help='Perform checks on specified files whether there is newline present'
             ' at the end of file')

    parser.addini('newline_require', type='linelist', help=(
        'Each line specifies a glob filename patter which will be checked against newline. '
        'Example: */requirements.txt'
    ))


def pytest_sessionstart(session):
    """
    Checks whether there are filename patters to be checked against newline, as specified by user
    If user specifies filenames, they overrides default ones!
    """
    config = session.config
    if config.option.newline_check:
        ini_newline_require = config.getini('newline_require')
        if ini_newline_require:
            config.require_newline = FileMatcher(ini_newline_require)
        else:
            config.require_newline = FileMatcher(REQUIRED_NEWLINE_IN)


def pytest_collect_file(path, parent):
    config = parent.config
    if config.option.newline_check and config.require_newline(path):
        return NewlineCheckItem(path, parent)


def check_newline(path):
    """
    Performs newline checks and returns rule violation status. If file is empty, test is passed.
    Otherwise file is checked against occurrence of newline at the end and eventually
    against forbidden multiple newlines at the end
    """
    with open(path, 'r') as f:
        lines = f.readlines()
        if not lines:
            return False
        if lines[-1] == '\n':
            return 'Extra newline(s) at the end of file'
        if not lines[-1].endswith('\n'):
            return 'Missing newline at the end of file'
        return False


class FileMatcher:
    """
    Class helps to maintain custom list of files, which are forced to end with newline character
    Based on pytest-isort implementation:
        https://github.com/moccu/pytest-isort/blob/master/pytest_isort.py
    """

    def __init__(self, require_lines):
        self.requires = []

        for line in require_lines:
            comment_position = line.find("#")
            # Strip comments.
            if comment_position != -1:
                line = line[:comment_position]

            glob = line.strip()

            # Skip blank lines.
            if not glob:
                continue

            # Normalize path if needed.
            if glob and os.sep != '/' and '/' in glob:
                glob = glob.replace('/', os.sep)

            self.requires.append(glob)

    def __call__(self, path):
        for glob in self.requires:
            if path.fnmatch(glob):
                return glob


class MissingNewlineError(Exception):
    """ Indicates missing newline at the end of file. """

    def __init__(self, path, message):
        self.path = path
        self.message = message

    def get_message(self):
        return f'{self.path}: {self.message}'


class NewlineCheckItem(pytest.Item, pytest.File):

    def __init__(self, path, parent):
        super().__init__(path, parent)
        self.add_marker('newline-check')

    def runtest(self):
        newline_err = check_newline(self.fspath)

        if newline_err:
            raise MissingNewlineError(str(self.fspath), newline_err)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(MissingNewlineError):
            return excinfo.value.get_message()
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, -1, 'newline-check'
