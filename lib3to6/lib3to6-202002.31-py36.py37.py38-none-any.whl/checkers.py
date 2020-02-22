# -*- coding: utf-8 -*-
# This file is part of the lib3to6 project
# https://gitlab.com/mbarkhau/lib3to6
#
# Copyright (c) 2019 Manuel Barkhau (mbarkhau@gmail.com) - MIT License
# SPDX-License-Identifier: MIT

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import ast
import typing as typ
from . import utils
from . import common


class VersionInfo(object):
    prohibited_until = None

    def __init__(self, prohibited_until=None):
        self.prohibited_until = prohibited_until


class CheckerBase(object):
    version_info = None

    def is_prohibited_for(self, version):
        return (self.version_info.prohibited_until is None or self.
            version_info.prohibited_until >= version)

    def __call__(self, cfg, tree):
        raise NotImplementedError()


class NoStarImports(CheckerBase):
    version_info = VersionInfo()

    def __call__(self, cfg, tree):
        for node in ast.walk(tree):
            if not isinstance(node, ast.ImportFrom):
                continue
            for alias in node.names:
                if alias.name == '*':
                    raise common.CheckError('Prohibited from {0} import *.'
                        .format(node.module), node)


def _iter_scope_names(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            yield node.name, node
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            yield node.id, node
        elif isinstance(node, (ast.ImportFrom, ast.Import)):
            for alias in node.names:
                name = alias.name if alias.asname is None else alias.asname
                yield name, node
        elif isinstance(node, ast.arg):
            yield node.arg, node


class NoOverriddenFixerImportsChecker(CheckerBase):
    """Don't override names that fixers may reference."""
    version_info = VersionInfo()
    prohibited_import_overrides = {'itertools', 'six', 'builtins'}

    def __call__(self, cfg, tree):
        for name_in_scope, node in _iter_scope_names(tree):
            is_fixer_import = isinstance(node, ast.Import) and len(node.names
                ) == 1 and node.names[0].asname is None and node.names[0
                ].name == name_in_scope
            if is_fixer_import:
                continue
            if name_in_scope in self.prohibited_import_overrides:
                msg = "Prohibited override of import '{0}'".format(
                    name_in_scope)
                raise common.CheckError(msg, node)


class NoOverriddenBuiltinsChecker(CheckerBase):
    """Don't override names that fixers may reference."""
    version_info = VersionInfo()

    def __call__(self, cfg, tree):
        for name_in_scope, node in _iter_scope_names(tree):
            if name_in_scope in common.BUILTIN_NAMES:
                msg = "Prohibited override of builtin '{0}'".format(
                    name_in_scope)
                raise common.CheckError(msg, node)


MODULE_BACKPORTS = {'lzma': ((3, 3), 'backports.lzma'), 'pathlib': ((3, 4),
    'pathlib2'), 'statistics': ((3, 4), 'statistics'), 'ipaddress': ((3, 4),
    'py2-ipaddress'), 'asyncio': ((3, 4), None), 'selectors': ((3, 4), None
    ), 'enum': ((3, 4), 'enum34'), 'zipapp': ((3, 5), None), 'typing': ((3,
    5), 'typing'), 'contextvars': ((3, 7), 'contextvars'), 'dataclasses': (
    (3, 7), 'dataclasses'), 'importlib.resources': ((3, 7),
    'importlib_resources')}


class NoThreeOnlyImports(CheckerBase):
    version_info = VersionInfo(prohibited_until='2.7')

    def __call__(self, cfg, tree):
        pass


PROHIBITED_OPEN_ARGUMENTS = {'encoding', 'errors', 'newline', 'closefd',
    'opener'}


class NoOpenWithEncodingChecker(CheckerBase):
    version_info = VersionInfo(prohibited_until='2.7')

    def __call__(self, cfg, tree):
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func_node = node.func
            if not isinstance(func_node, ast.Name):
                continue
            if func_node.id != 'open' or not isinstance(func_node.ctx, ast.Load
                ):
                continue
            mode = 'r'
            if len(node.args) >= 2:
                mode_node = node.args[1]
                if isinstance(mode_node, ast.Str):
                    mode = mode_node.s
                else:
                    msg = (
                        "Prohibited value for argument 'mode' of builtin.open. "
                         + 'Expected ast.Str node, got: {0}'.format(mode_node))
                    raise common.CheckError(msg, node)
            if len(node.args) > 3:
                raise common.CheckError(
                    'Prohibited positional arguments to builtin.open'.
                    format(), node)
            for kw in node.keywords:
                if kw.arg in PROHIBITED_OPEN_ARGUMENTS:
                    msg = ("Prohibited keyword argument '{0}' to builtin.open."
                        .format(kw.arg))
                    raise common.CheckError(msg, node)
                if kw.arg != 'mode':
                    continue
                mode_node = kw.value
                if isinstance(mode_node, ast.Str):
                    mode = mode_node.s
                else:
                    msg = (
                        "Prohibited value for argument 'mode' of builtin.open. "
                         + 'Expected ast.Str node, got: {0}'.format(mode_node))
                    raise common.CheckError(msg, node)
            if 'b' not in mode:
                msg = (
                    "Prohibited value '{0}' for argument 'mode' of builtin.open. "
                    .format(mode) +
                    'Only binary modes are allowed, use io.open as an alternative.'
                    )
                raise common.CheckError(msg, node)


ASYNC_AWAIT_NODE_TYPES = (ast.AsyncFor, ast.AsyncWith, ast.AsyncFunctionDef,
    ast.Await)


class NoAsyncAwait(CheckerBase):
    version_info = VersionInfo(prohibited_until='3.4')

    def __call__(self, cfg, tree):
        for node in ast.walk(tree):
            if isinstance(node, ASYNC_AWAIT_NODE_TYPES):
                raise common.CheckError('Prohibited use of async/await', node)


class NoComplexNamedTuple(CheckerBase):
    version_info = VersionInfo(prohibited_until='3.4')

    def __call__(self, cfg, tree):
        _typing_module_name = None
        _namedtuple_class_name = 'NamedTuple'
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == 'typing':
                        if alias.asname is None:
                            _typing_module_name = alias.name
                        else:
                            _typing_module_name = alias.asname
            if isinstance(node, ast.ImportFrom) and node.module == 'typing':
                for alias in node.names:
                    if alias.name == 'NamedTuple':
                        if alias.asname is None:
                            _namedtuple_class_name = alias.name
                        else:
                            _namedtuple_class_name = alias.asname
            if not isinstance(node, ast.ClassDef):
                continue
            if not (_typing_module_name or _namedtuple_class_name):
                continue
            if not utils.has_base_class(node, _typing_module_name,
                _namedtuple_class_name):
                continue
            for subnode in node.body:
                if isinstance(subnode, ast.Expr) and isinstance(subnode.
                    value, ast.Str):
                    pass
                elif isinstance(subnode, ast.AnnAssign):
                    if subnode.value:
                        tgt = subnode.target
                        assert isinstance(tgt, ast.Name)
                        msg = 'Prohibited use of default value '.format(
                            ) + "for field '{0}' of class '{1}'".format(tgt
                            .id, node.name)
                        raise common.CheckError(msg, subnode, node)
                elif isinstance(subnode, ast.FunctionDef):
                    msg = 'Prohibited definition of method '.format(
                        ) + "'{0}' for class '{1}'".format(subnode.name,
                        node.name)
                    raise common.CheckError(msg, subnode, node)
                else:
                    msg = ('Unexpected subnode defined for class {0}: {1}'.
                        format(node.name, subnode))
                    raise common.CheckError(msg, subnode, node)
