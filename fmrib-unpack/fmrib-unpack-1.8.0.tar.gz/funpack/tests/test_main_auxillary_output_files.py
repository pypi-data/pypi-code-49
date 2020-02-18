#!/usr/bin/env python
#
# test_main_auxillary_output_files.py -
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#

import textwrap  as tw
import itertools as it
import os.path   as op
import              os

from unittest import mock

import numpy as np

import pandas as pd

import funpack.main       as main
import funpack.custom     as custom
import funpack.expression as expression
import funpack.processing as processing

from . import (patch_logging,
               tempdir,
               gen_DataTable,
               gen_test_data)


@patch_logging
def test_main_icd10():
    with tempdir():
        codings = tw.dedent("""
        coding\tmeaning\tnode_id\tparent_id
        a10\ta desc\t5\t0
        b20\tb desc\t1\t5
        c30\tc desc\t3\t5
        d40\td desc\t4\t3
        e50\te desc\t2\t1
        """).strip()

        data = tw.dedent("""
        eid,1-0.0
        1,a10
        2,b20
        3,c30
        4,d40
        5,e50
        """)

        exp = tw.dedent("""
        code\tvalue\tdescription\tparent_descs
        a10\t5\ta desc\t
        b20\t1\tb desc\t[a desc]
        c30\t3\tc desc\t[a desc]
        d40\t4\td desc\t[a desc] [c desc]
        e50\t2\te desc\t[a desc] [b desc]
        """).strip()

        with open('icd10.tsv', 'wt') as f: f.write(codings)
        with open('data.tsv',  'wt') as f: f.write(data)

        with mock.patch('funpack.hierarchy.getHierarchyFilePath',
                        return_value='icd10.tsv'):
            main.main('-cl 1 codeToNumeric(\'icd10\') '
                      '-imf icd10_mappings.tsv out.tsv data.tsv'
                      .split())

        with open('icd10_mappings.tsv', 'rt') as f:
            got = f.read().strip()

        assert exp == got



@patch_logging
def test_main_unknown_vars():

    vartable = tw.dedent("""
    ID\tType\tDescription\tDataCoding\tNAValues\tRawLevels\tNewLevels\tParentValues\tChildValues\tClean
    1
    2
    3
    4
    5
    """).strip()

    exp = tw.dedent("""
    name\tfile\tclass\tprocessed\texported
    6-0.0\t{file}\tunknown\t{}\t{}
    7-0.0\t{file}\tunknown\t{}\t{}
    8-0.0\t{file}\tunknown\t{}\t{}
    9-0.0\t{file}\tunknown\t{}\t{}
    10-0.0\t{file}\tunknown\t{}\t{}
    1-0.0\t{file}\tunprocessed\t{}\t{}
    2-0.0\t{file}\tunprocessed\t{}\t{}
    3-0.0\t{file}\tunprocessed\t{}\t{}
    4-0.0\t{file}\tunprocessed\t{}\t{}
    5-0.0\t{file}\tunprocessed\t{}\t{}
    """).strip()

    def check(fname, *fmtargs, **fmtkwargs):

        drop = fmtkwargs.pop('drop', [])

        cexp = exp.split('\n')

        for d in drop:
            cexp = [l for l in cexp if not l.startswith('{}-'.format(d))]
        cexp = '\n'.join(cexp)

        with open(fname, 'rt') as f:
            got = f.read().strip()

        print('exp', cexp.format(*fmtargs, **fmtkwargs))
        print('got')
        print( got)

        assert got == cexp.format(*fmtargs, **fmtkwargs)

    with tempdir() as td:

        fullfile = op.realpath(op.join(td, 'data.tsv'))

        gen_test_data(10, 50, 'data.tsv')
        with open('variables.tsv', 'wt') as f:
            f.write(vartable)

        # don't use --import_all -
        # no file generated
        main.main('-ow -nb '
                  '-vf variables.tsv '
                  '-uf unknowns.tsv '
                  'out.tsv data.tsv'.split())
        assert not op.exists('unknowns.tsv')

        main.main('-ow -nb '
                  '-vf variables.tsv '
                  '-uf unknowns.tsv '
                  '--import_all '
                  'out.tsv data.tsv'.split())

        check('unknowns.tsv',
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              file=fullfile)
        os.remove('unknowns.tsv')

        # still generated if we use --remove_unknown
        main.main('-ow -nb '
                  '-vf variables.tsv '
                  '-uf unknowns.tsv '
                  '--import_all '
                  '--remove_unknown '
                  'out.tsv data.tsv'.split())
        check('unknowns.tsv',
              1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              file=fullfile)
        os.remove('unknowns.tsv')

        # some unknowns exported, some dropped
        main.main('-ow -nb '
                  '-vf variables.tsv '
                  '-uf unknowns.tsv '
                  '-v 3:7 '
                  '--import_all '
                  'out.tsv data.tsv'.split())
        check('unknowns.tsv',
              1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
              1, 0, 1, 0, 1, 1, 1, 1, 1, 1,
              file=fullfile)
        os.remove('unknowns.tsv')

        # some unknowns
        # failed processing
        data2 = pd.read_csv('data.tsv', delimiter='\t', index_col=0)
        data2.loc[1:45, '6-0.0'] = np.nan
        data2.loc[5:,   '8-0.0'] = np.nan
        data2.to_csv('data2.tsv', sep='\t')
        fullfile2 = op.realpath(op.join(td, 'data2.tsv'))
        main.main('-ow -nb -n -n '
                  '-sp '
                  '-apr 6 removeIfSparse(minpres=20) '
                  '-apr 8 removeIfSparse(minpres=20) '
                  '-vf variables.tsv '
                  '-uf unknowns.tsv '
                  '--import_all '
                  'out.tsv data2.tsv'.split())
        check('unknowns.tsv',
              0, 0, 1, 1, 0, 0, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              file=fullfile2)
        os.remove('unknowns.tsv')

        # known vars with
        # processing omitted
        main.main('-ow -nb -n -n '
                  '-sp '
                  '-nv 1 1,2,3 '
                  '-vf variables.tsv '
                  '-uf unknowns.tsv '
                  '--import_all '
                  'out.tsv data.tsv'.split())
        check('unknowns.tsv',
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              file=fullfile,
              drop=[1])
        os.remove('unknowns.tsv')



@patch_logging
def test_main_description_file():

    vartable = tw.dedent("""
    ID\tType\tDescription\tDataCoding\tNAValues\tRawLevels\tNewLevels\tParentValues\tChildValues\tClean
    1\t\tvar one
    2\t\tvar two
    3\t\tvar three
    4
    """).strip()

    proctable = tw.dedent("""
    Variable\tProcess
    1\tmyprocess
    2\tmyprocess(metaproc='mymetaproc')
    """)

    @custom.processor()
    def myprocess(dtable, vids):
        columns = it.chain(*[dtable.columns(v) for v in vids])

        add     = []
        addvid  = []
        addmeta = []

        for col in columns:
            series = dtable[:, col.name]
            col.metadata = col.vid + 20

            newseries = pd.Series(series + 5, name=col.name + '_a')
            dtable[:, col.name] = dtable[:, col.name] + 3

            add    .append(newseries)
            addvid .append(col.vid)
            addmeta.append({'metadata' : col.vid + 40})

        return [], add, addvid, addmeta

    @custom.metaproc()
    def mymetaproc(dtable, vid, val):
        return str(val) + ' metaprocced'

    with tempdir():
        with open('vartable.tsv',  'wt') as f: f.write(vartable)
        with open('proctable.tsv', 'wt') as f: f.write(proctable)

        gen_test_data(4, 10, 'data.tsv')

        main.main('-nb -vf vartable.tsv -pf proctable.tsv '
                  '-def descriptions.tsv '
                  'out.tsv data.tsv'.split())

        inp   = pd.read_csv('data.tsv',         delimiter='\t', index_col=0)
        got   = pd.read_csv('out.tsv',          delimiter='\t', index_col=0)
        descs = pd.read_csv('descriptions.tsv',
                            delimiter='\t',
                            index_col=0,
                            header=None,
                            names=('column', 'description'))

        assert all(got.columns == ['1-0.0', '1-0.0_a',
                                   '2-0.0', '2-0.0_a',
                                   '3-0.0', '4-0.0'])

        assert (got['1-0.0']   == (inp['1-0.0'] + 3)).all()
        assert (got['1-0.0_a'] == (inp['1-0.0'] + 5)).all()
        assert (got['2-0.0']   == (inp['2-0.0'] + 3)).all()
        assert (got['2-0.0_a'] == (inp['2-0.0'] + 5)).all()
        assert (got['3-0.0']   == (inp['3-0.0']))    .all()
        assert (got['4-0.0']   == (inp['4-0.0']))    .all()

        assert descs.loc['1-0.0',   'description'] == 'var one (21)'
        assert descs.loc['1-0.0_a', 'description'] == 'var one (41)'
        assert descs.loc['2-0.0',   'description'] == 'var two (22)'
        assert descs.loc['2-0.0_a', 'description'] == 'var two (42 metaprocced)'
        assert descs.loc['3-0.0',   'description'] == 'var three (0.0)'
        assert descs.loc['4-0.0',   'description'] == 'n/a (0.0)'


def test_main_summary_file():
    class A:
        pass
    with tempdir():
        data = np.random.randint(1, 10, (10, 4))
        dt   = gen_DataTable(data)
        vt   = dt.vartable

        args = A()
        args.summary_file = 'summary.tsv'

        vt.at[1, 'RawLevels']    = [1, 2, 3]
        vt.at[1, 'NewLevels']    = [3, 2, 1]
        vt.at[2, 'NAValues']     = [1, 2, 3, 4]
        vt.at[3, 'ParentValues'] = [expression.Expression('v1 == 0')]
        vt.at[3, 'ChildValues']  = [0]
        vt.at[4, 'Clean']        = {
            'flattenHierarchical' :
            processing.Process('cleaner', 'flattenHierarchical', (), {})}

        main.doSummaryExport(dt, args)

        sum = pd.read_csv('summary.tsv', delimiter='\t', index_col=0)

        assert sum.at[1, 'RawLevels']    == str(vt.at[1, 'RawLevels'])
        assert sum.at[1, 'NewLevels']    == str(vt.at[1, 'NewLevels'])
        assert sum.at[2, 'NAValues']     == str(vt.at[2, 'NAValues'])
        assert sum.at[3, 'ParentValues'] == str(vt.at[3, 'ParentValues'])
        assert sum.at[3, 'ChildValues']  == str(vt.at[3, 'ChildValues'])
        assert sum.at[4, 'Clean']        == '[{}]'.format(
            str(vt.at[4, 'Clean']['flattenHierarchical']))
