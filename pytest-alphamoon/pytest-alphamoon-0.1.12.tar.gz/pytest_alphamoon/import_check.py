# -*- coding: utf-8 -*-
import ast

import pytest

IMPORTS_FORBIDDEN_FROM = {'scripts', 'user_settings', 'notebooks'}


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption(
        '--import-check',
        action='store_true',
        help='Perform initial import checks')


def pytest_collect_file(path, parent):
    config = parent.config
    if config.option.import_check and path.ext == '.py':
        return ImportCheckItem(path, parent)


class ImportCheckError(Exception):
    """ Indicates error during import checks. """

    def __init__(self, path, forbidden_imports):
        self.path = path
        self.forbidden_imports = forbidden_imports

    def get_message(self):
        msg = ''
        for line_num, import_type in self.forbidden_imports:
            msg += f'{self.path}:{line_num}: imports from {import_type} are forbidden\n'
        return msg


class ImportCheckItem(pytest.Item, pytest.File):

    def __init__(self, path, parent):
        super().__init__(path, parent)
        self.add_marker('import-check')

    def runtest(self):
        checker = ImportChecker(self.fspath)
        forbidden_imports = checker.check()
        if forbidden_imports:
            raise ImportCheckError(str(self.fspath), forbidden_imports)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(ImportCheckError):
            return excinfo.value.get_message()
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, -1, 'import-check'


class ImportChecker(ast.NodeVisitor):
    def __init__(self, path):
        self.path = path
        self.forbidden_imports = []

    def check(self):
        self.forbidden_imports = []
        with open(self.path, 'r') as src_code:
            ast_tree = ast.parse(src_code.read())
            self.visit(ast_tree)
            return self.forbidden_imports

    def visit_Import(self, node):
        for stmt in node.names:
            self._check_import_forbidden(stmt.name, node.lineno)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        self._check_import_forbidden(node.module, node.lineno)
        for stmt in node.names:
            self._check_import_forbidden(stmt.name, node.lineno)
        self.generic_visit(node)

    def _check_import_forbidden(self, import_chunk, line_num):
        for forbid_import in IMPORTS_FORBIDDEN_FROM:
            if forbid_import in import_chunk:
                self.forbidden_imports.append((line_num, forbid_import))
