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
try:
    import builtins
except ImportError:
    import __builtin__ as builtins
str = getattr(builtins, 'unicode', str)
PackageDir = typ.Dict[str, str]
BuildConfig = typ.Dict[str, str]


class InvalidPackage(Exception):
    pass


class CheckError(Exception):

    def __init__(self, msg, node=None, parent=None):
        node_lineno = node.lineno if isinstance(node, (ast.stmt, ast.expr)
            ) else 0
        parent_lineno = parent.lineno if isinstance(parent, (ast.stmt, ast.
            expr)) else 0
        lineno = node_lineno or parent_lineno
        if lineno:
            msg += ' on line {0}'.format(lineno)
        super(CheckError, self).__init__(msg)


class FixerError(Exception):
    msg = None
    node = None
    module = None

    def __init__(self, msg, node, module=None):
        self.msg = msg
        self.node = node
        self.module = module


ImportDecl = typ.NamedTuple('ImportDecl', [('module_name', str), (
    'import_name', typ.Optional[str]), ('py2_module_name', typ.Optional[str])])
BUILTIN_NAMES = {'ArithmeticError', 'AssertionError', 'AttributeError',
    'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError',
    'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
    'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError',
    'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
    'Exception', 'False', 'FileExistsError', 'FileNotFoundError',
    'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError',
    'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
    'InterruptedError', 'IsADirectoryError', 'KeyError',
    'KeyboardInterrupt', 'LookupError', 'MemoryError',
    'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError',
    'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError',
    'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
    'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError',
    'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError',
    'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError',
    'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
    'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
    'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
    'Warning', 'ZeroDivisionError', 'abs', 'all', 'any', 'ascii', 'bin',
    'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',
    'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir',
    'display', 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float',
    'format', 'frozenset', 'get_ipython', 'getattr', 'globals', 'hasattr',
    'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
    'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
    'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print',
    'property', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
    'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple',
    'type', 'vars', 'zip', 'StandardError', 'apply', 'basestring', 'buffer',
    'cmp', 'coerce', 'dreload', 'execfile', 'file', 'intern', 'long',
    'raw_input', 'reduce', 'reload', 'unichr', 'unicode', 'xrange'}
BUILTIN_NAMES.update([name for name in dir(builtins) if not name.startswith
    ('__')])
