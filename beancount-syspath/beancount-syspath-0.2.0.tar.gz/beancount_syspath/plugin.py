# License: The MIT License
# Copyright (c) 2020 Aetf

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
'''
Beancount Plugin

Append configured paths to sys.path
'''
import sys
import ast
from pathlib import Path
from collections import namedtuple

__author__ = 'Aetf <aetf@unlimited-code.works>'

__plugins__ = ['run']


DEFAULT_CONFIG = {
    'append': [],
    'prepend': [],
    'normalize_to_root': True,
}


def normalize_path(p, root):
    if Path(p).is_absolute():
        return p
    return str((root / p).resolve(strict=False))


def _run(entries, options_map, obj):
    '''Modify sys.path'''

    cfg = {}
    cfg.update(DEFAULT_CONFIG)
    cfg.update(obj)

    append = cfg['append']
    prepend = cfg['prepend']
    if cfg['normalize_to_root']:
        root = Path(options_map['filename']).parent
        append = [normalize_path(p, root) for p in append]
        prepend = [normalize_path(p, root) for p in prepend]

    sys.path[0:0] = prepend
    sys.path.extend(append)

    print(f'new syspath is {sys.path}')
    return entries, []


def run(entries, options_map, config_str):
    '''Modify sys.path'''
    obj = ast.literal_eval(config_str)
    if not isinstance(obj, dict):
        raise ValueError('Invalid plugin configuration: should be a single dict.')
    return _run(entries, options_map, obj)


DeprecationError = namedtuple('DeprecationError', 'source message entry')


def run_legacy(funcname, entries, options_map, config_str):
    paths = ast.literal_eval(config_str)
    if not isinstance(paths, list):
        raise ValueError('Invalid plugin configuration: should be a single list.')

    entries, errors = _run(entries, options_map, {
        funcname: paths
    })
    errors.append(DeprecationError(
        {
            'filename': f'<beancount_syspath.{funcname}>',
            'lineno': 0,
        },
        f'beancount_syspath.{funcname} is deprecated, please use beancount_syspath.plugin instead.',
        None
    ))

    return entries, errors
