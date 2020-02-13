# -*- coding: utf-8 -*-
import json

import pytest

JUPYTER_NOTEBOOK = '.ipynb'
NOTEBOOKS_ALLOWED_IN = {'notebooks'}


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption(
        '--notebook-check',
        action='store_true',
        help='Perform checks whether notebooks has been cleaned'
             ' and are placed under /notebooks directory')


def pytest_collect_file(path, parent):
    config = parent.config
    if config.option.notebook_check and path.ext == JUPYTER_NOTEBOOK:
        return NotebookCheckItem(path, parent)


def check_notebook_dir(path):
    if not any(name in path.strpath for name in NOTEBOOKS_ALLOWED_IN):
        return 'notebook not under /notebooks directory'
    return ''


def check_notebook_output(path):
    with open(path, 'r') as notebook_file:
        notebook = json.load(notebook_file)
        for cell in notebook['cells']:
            if (cell.get('ExecuteTime') is not None or
                    cell.get('execution_count') is not None or
                    cell.get('outputs')):
                return 'notebook with output'
    return ''


class NotebookCheckError(Exception):
    """ Indicates incorrect .ipnyb file placement. """

    def __init__(self, path, error_messages):
        self.path = path
        self.error_messages = error_messages

    def get_message(self):
        return f'{self.path}: {", ".join(self.error_messages)}\n'


class NotebookCheckItem(pytest.Item, pytest.File):

    def __init__(self, path, parent):
        super().__init__(path, parent)
        self.add_marker('notebook-check')

    def runtest(self):
        error_messages = []
        dir_error = check_notebook_dir(self.fspath)
        if dir_error:
            error_messages.append(dir_error)

        output_error = check_notebook_output(self.fspath)
        if output_error:
            error_messages.append(output_error)

        if error_messages:
            raise NotebookCheckError(str(self.fspath), error_messages)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(NotebookCheckError):
            return excinfo.value.get_message()
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, -1, 'notebook-check'
