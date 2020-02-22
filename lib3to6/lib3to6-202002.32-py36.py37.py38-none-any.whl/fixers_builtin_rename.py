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
from . import common
from . import fixer_base as fb


class BuiltinsRenameFixerBase(fb.FixerBase):
    new_name = None
    old_name = None

    def __call__(self, cfg, tree):
        for node in ast.walk(tree):
            is_access_to_builtin = isinstance(node, ast.Name) and isinstance(
                node.ctx, ast.Load) and node.id == self.new_name
            if is_access_to_builtin:
                self.required_imports.add(common.ImportDecl('builtins',
                    None, '__builtin__'))
                builtin_renmae_decl_str = (
                    """
                {0} = getattr(builtins, '{1}', {2})
                """
                    .format(self.new_name, self.old_name, self.new_name))
                self.module_declarations.add(builtin_renmae_decl_str.strip())
        return tree


class XrangeToRangeFixer(BuiltinsRenameFixerBase):
    version_info = fb.VersionInfo(apply_since='1.0', apply_until='2.7',
        works_until='3.99')
    new_name = 'range'
    old_name = 'xrange'


class UnicodeToStrFixer(BuiltinsRenameFixerBase):
    version_info = fb.VersionInfo(apply_since='1.0', apply_until='2.7',
        works_until='3.99')
    new_name = 'str'
    old_name = 'unicode'


class UnichrToChrFixer(BuiltinsRenameFixerBase):
    version_info = fb.VersionInfo(apply_since='1.0', apply_until='2.7',
        works_until='3.99')
    new_name = 'chr'
    old_name = 'unichr'


class RawInputToInputFixer(BuiltinsRenameFixerBase):
    version_info = fb.VersionInfo(apply_since='1.0', apply_until='2.7',
        works_until='3.99')
    new_name = 'input'
    old_name = 'raw_input'
