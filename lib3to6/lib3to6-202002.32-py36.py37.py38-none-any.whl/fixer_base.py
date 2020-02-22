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
from . import common


class VersionInfo(object):
    apply_since = None
    apply_until = None
    works_since = None
    works_until = None

    def __init__(self, apply_since, apply_until, works_since=None,
        works_until=None):
        self.apply_since = [int(part) for part in apply_since.split('.')]
        self.apply_until = [int(part) for part in apply_until.split('.')]
        if works_since is None:
            self.works_since = self.apply_since
        else:
            self.works_since = [int(part) for part in works_since.split('.')]
        self.works_until = [int(part) for part in works_until.split('.')
            ] if works_until else None


class FixerBase(object):
    version_info = None
    required_imports = None
    module_declarations = None

    def __init__(self):
        self.required_imports = set()
        self.module_declarations = set()

    def __call__(self, cfg, tree):
        raise NotImplementedError()

    def is_required_for(self, version):
        version_num = [int(part) for part in version.split('.')]
        nfo = self.version_info
        return nfo.apply_since <= version_num <= nfo.apply_until

    def is_compatible_with(self, version):
        version_num = [int(part) for part in version.split('.')]
        nfo = self.version_info
        return nfo.works_since <= version_num and (nfo.works_until is None or
            version_num <= nfo.works_until)

    def is_applicable_to(self, src_version, tgt_version):
        return self.is_compatible_with(src_version) and self.is_required_for(
            tgt_version)


class TransformerFixerBase(FixerBase, ast.NodeTransformer):

    def __call__(self, cfg, tree):
        try:
            return self.visit(tree)
        except common.FixerError as ex:
            if ex.module is None:
                ex.module = tree
            raise
