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
import os
import sys
import shutil
import typing as typ
import hashlib as hl
import tempfile
try:
    import builtins
except ImportError:
    import __builtin__ as builtins
import pathlib2 as pl
str = getattr(builtins, 'unicode', str)
from . import common
from . import transpile
ENV_PATH = str(pl.Path(sys.executable).parent.parent)
PYTHON_TAG_PREFIXES = {'py': 'Generic Python', 'cp': 'CPython', 'ip':
    'IronPython', 'pp': 'PyPy', 'jy': 'Jython'}
CACHE_DIR = pl.Path(tempfile.gettempdir()) / '.lib3to6_cache'


def eval_build_config():
    return {'target_version': '2.7', 'force_transpile': '1', 'fixers': '',
        'checkers': ''}


def _ignore_tmp_files(src, names):
    if isinstance(src, str):
        src_str = src
    elif isinstance(src, os.DirEntry):
        src_str = src.path
    else:
        src_str = str(src)
    if src_str.startswith('build') or src_str.startswith('./build'):
        return names
    if src_str.endswith('.egg-info'):
        return names
    if src_str.endswith('dist'):
        return names
    if src_str.endswith('__pycache__'):
        return names
    return [name for name in names if name.endswith('.pyc')]


def init_build_package_dir(local_package_dir):
    output_dir = pl.Path('build') / 'lib3to6_out'
    try:
        output_dir.mkdir(parents=True)
    except Exception:
        pass
    build_package_dir = {}
    for package, src_package_dir in local_package_dir.items():
        is_abs_path = pl.Path(src_package_dir) == pl.Path(src_package_dir
            ).absolute()
        if is_abs_path:
            raise Exception("package_dir must use relative paths, got '{0}'"
                .format(src_package_dir))
        build_package_subdir = output_dir / src_package_dir
        if build_package_subdir.exists():
            shutil.rmtree(build_package_subdir)
        shutil.copytree(src_package_dir, str(build_package_subdir), ignore=
            _ignore_tmp_files)
        build_package_dir[package] = str(build_package_subdir)
    return build_package_dir


def build_package(cfg, package, build_dir):
    for root, _dirs, files in os.walk(build_dir):
        for filename in files:
            filepath = pl.Path(root) / filename
            if filepath.suffix != '.py':
                continue
            with open(filepath, mode='rb') as fh:
                module_source_data = fh.read()
            filehash = hl.sha1(module_source_data).hexdigest()
            cache_path = CACHE_DIR / (filehash + '.py')
            if int(cfg['force_transpile']) or not cache_path.exists():
                try:
                    fixed_module_source_data = transpile.transpile_module_data(
                        cfg, module_source_data)
                except common.CheckError as err:
                    err.args = (err.args[0] + ' of file {0} '.format(filepath),
                        ) + err.args[1:]
                    raise
                with open(cache_path, mode='wb') as fh:
                    fh.write(fixed_module_source_data)
            shutil.copy(cache_path, filepath)


def build_packages(cfg, build_package_dir):
    CACHE_DIR.mkdir(exist_ok=True)
    for package, build_dir in build_package_dir.items():
        build_package(cfg, package, build_dir)


def fix(package_dir=None):
    if package_dir is None:
        package_dir = {'': '.'}
    build_package_dir = init_build_package_dir(package_dir)
    build_cfg = eval_build_config()
    build_packages(build_cfg, build_package_dir)
    return build_package_dir
