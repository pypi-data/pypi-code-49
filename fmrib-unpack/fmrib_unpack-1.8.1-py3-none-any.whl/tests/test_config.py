#!/usr/bin/env python
#
# test_config.py -
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#

import os.path as op

from unittest import mock

import funpack.config as config
import funpack.custom as custom

from . import clear_plugins

@clear_plugins
def test_parseArgs_fixPath():

    custom.registerBuiltIns()

    fullpath = op.normpath(
        op.join(op.dirname(__file__), '..',
                'configs', 'fmrib', 'variables_clean.tsv'))
    relpath  = op.join('fmrib', 'variables_clean.tsv')
    dotpath  = 'fmrib.variables_clean'

    argv = ['-vf', fullpath,
            '-vf', relpath,
            '-vf', dotpath, 'output',  'input']

    args = config.parseArgs(argv)[0]

    assert args.variable_file == [fullpath, fullpath, fullpath]

@clear_plugins
def test_num_jobs():

    custom.registerBuiltIns()

    with mock.patch('multiprocessing.cpu_count', return_value=99):
        assert config.parseArgs('-nj -1 out in'.split())[0].num_jobs == 99
        assert config.parseArgs('-nj -5 out in'.split())[0].num_jobs == 99

    assert config.parseArgs('-nj 0 out in'.split())[0].num_jobs == 1
    assert config.parseArgs('-nj 1 out in'.split())[0].num_jobs == 1
    assert config.parseArgs('-nj 5 out in'.split())[0].num_jobs == 5
