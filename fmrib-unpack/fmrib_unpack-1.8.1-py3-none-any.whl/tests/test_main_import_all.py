#!/usr/bin/env python
#
# test_main_import_all.py -
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#

import textwrap  as tw

import numpy as np

import pandas as pd

import funpack.main as main

from . import (patch_logging,
               tempdir,
               gen_test_data)


@patch_logging
def test_main_import_all():

    with tempdir():

        gen_test_data(10, 20, 'data.tsv')

        main.main('-nb out.tsv data.tsv'.split())
        baseline = pd.read_csv('out.tsv', delimiter='\t', index_col=0)

        main.main('--import_all -nb -ow out.tsv data.tsv'.split())
        passthru = pd.read_csv('out.tsv', delimiter='\t', index_col=0)
        assert np.all(baseline == passthru)

        main.main('-v 1:3 --import_all -nb -ow out.tsv data.tsv'.split())
        dropvars = pd.read_csv('out.tsv', delimiter='\t', index_col=0)
        exp = baseline.loc[:, ['1-0.0', '2-0.0', '3-0.0']]
        assert np.all(dropvars == exp)

        main.main('-v 3:-1:1 --import_all -nb -ow out.tsv data.tsv'.split())
        ordered = pd.read_csv('out.tsv', delimiter='\t', index_col=0)
        exp = baseline.loc[:, ['3-0.0', '2-0.0', '1-0.0']]
        assert np.all(ordered == exp)


        vartable = tw.dedent("""
        ID\tType\tDescription\tDataCoding\tNAValues\tRawLevels\tNewLevels\tParentValues\tChildValues\tClean
        3
        4
        5
        """).strip()

        with open('variables.tsv', 'wt') as f:
            f.write(vartable)

        main.main('-r -nb -vf variables.tsv --import_all -ow out.tsv data.tsv'.split())
        ordered = pd.read_csv('out.tsv', delimiter='\t', index_col=0)
        exp = baseline.loc[:, ['3-0.0', '4-0.0', '5-0.0']]
        assert np.all(ordered == exp)


@patch_logging
def test_main_import_all_variable_removed():

    data = tw.dedent("""
    f.eid\t1-0.0\t2-0.0
    1\t5\t10
    2\t6\t
    3\t7\t
    4\t8\t
    5\t9\t
    6\t10\t
    7\t11\t
    8\t12\t
    9\t13\t
    10\t14\t
    """).strip()

    with tempdir():
        with open('data.tsv', 'wt') as f:
            f.write(data)

        main.main('-ia -v 1:2 -sp -apr all removeIfSparse(minpres=5) '
                  'out.tsv data.tsv'.split())

        got = pd.read_csv('out.tsv', delimiter='\t', index_col=0)
        assert np.all(got.index == np.arange(1, 11))
        assert got.columns == ['1-0.0']
        assert np.all(got['1-0.0'] == np.arange(5, 15))



@patch_logging
def test_main_importAll_column_patterns():

    data = tw.dedent("""
    eid,col1,column2,col3
    1,11,21,31
    2,12,22,32
    3,13,23,33
    4,14,24,34
    5,15,25,35
    """).strip()

    with tempdir():
        with open('data.txt', 'wt') as f:
            f.write(data)

        main.main('-nb -ia -co column2 -co col3 out1.txt data.txt'.split())
        main.main('-nb -ia -co col?             out2.txt data.txt'.split())

        got1 = pd.read_csv('out1.txt', delimiter='\t', index_col=0)
        got2 = pd.read_csv('out2.txt', delimiter='\t', index_col=0)

        assert np.all(got1.columns == ['column2', 'col3'])
        assert np.all(got2.columns == ['col1',    'col3'])


def test_main_import_all_variables_column_patterns():

    data = tw.dedent("""
    eid,1-0.0,2-0.0,3-0.0,col4
    1,11,21,31,41
    2,12,22,32,42
    3,13,23,33,43
    4,14,24,34,44
    5,15,25,35,45
    """).strip()

    with tempdir():
        with open('data.txt', 'wt') as f:
            f.write(data)

        main.main('-nb -ia -v 3 -v 2 -v 1 -co col4 out.txt data.txt'.split())

        exp = pd.read_csv('data.txt', delimiter=',',  index_col=0)
        got = pd.read_csv('out.txt',  delimiter='\t', index_col=0)

        with open('out.txt') as f:
            hdr = f.readline().strip()

        assert hdr == '\t'.join(['eid', 'col4', '3-0.0', '2-0.0', '1-0.0'])

        exp = exp[['col4', '3-0.0', '2-0.0', '1-0.0']]
        assert (exp == got).all().all()
