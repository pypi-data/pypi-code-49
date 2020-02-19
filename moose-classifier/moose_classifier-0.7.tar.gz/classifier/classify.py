# This file is part of classifier
#
#    classifier is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    classifier is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with classifier.  If not, see <http://www.gnu.org/licenses/>.
"""Classify sequences by grouping alignment output with taxonomy names

Optional grouping by specimen and query sequences

Positional arguments
++++++++++++++++++++

alignments
==========

A csv file with columns **qseqid**, **sseqid**, **pident**, and optional
columns **qstart**, **qend**, **qlen**, **qcovs** or **mismatch**.  With
column **qcovs** will be appended or replaced when the **qstart**,
**qend** and **qlen** columns are present.  The **mismatch** column is used
with the ``--best-n-hits`` switch. Additional columns may be present if a
header is provided and will automatically be appended to detailed output.

.. note:: If no header present user must specify one of the alignment input
          header-less options.

seq_info
========

A csv file with minimum columns **seqname** and **tax_id**.  Additional
columns will be included in the detailed output.

lineages
========

A csv file with columns **tax_id**, **rank** and **tax_name**, plus at least
one additional rank column(s) creating a taxonomic tree such as **species**,
**genus**, **family**, **class**, **pylum**, **kingdom** and/or **root**.
The rank columns also give an order of specificity from right to left,
least specific to most specific respectively.

Optional input
++++++++++++++

rank-thresholds
===============

TODO

copy-numbers
============

Below is an *example* copy numbers csv with the required columns:

    ====== ==================== ======
    tax_id tax_name             count
    ====== ==================== ======
    155977 Acaryochloris        2.00
    155978 Acaryochloris marina 2.00
    434    Acetobacter          5.00
    433    Acetobacteraceae     3.60
    ====== ==================== ======

weights
=======

Headerless file containing two columns specifying the seqname (clustername) and
weight (or number of sequences in the cluster).

Output
++++++

out
===

A csv with columns and headers as in the example below:

    =========== =============== ======================================
     specimen    assignment_id   assignment
    =========== =============== ======================================
      039_3      0               Pseudomonas mendocina;Pseudonocardia
      039_3      1               Rhizobiales
      039_3      2               Alcaligenes faecalis*
      039_3      3               [no blast result]
    =========== =============== ======================================

    ======= ============= =============
     low     max_percent   min_percent
    ======= ============= =============
     95.00   99.02         95.74
     95.00   98.91         95.31
     99.00   100.00        99.00

    ======= ============= =============

    ================= ======= =========== ===========
     condensed_rank   reads   pct_reads   clusters
    ================= ======= =========== ===========
     species          6       35.29       1
     genus            5       29.41       1
     species          5       29.41       1
                      1       5.88        1
    ================= ======= =========== ===========

details-out
===========

Original alignment input plus breakdown of assignments.

Internal functions
------------------

Known bugs
----------

Tax_ids of valid alignment (that meet their rank thresholds) may be
assigned tax_ids of a higher threshold that *could* represent invalid tax_ids
(tax_ids that may *not* have passed the rank threshold).

TODO: generate rank thresholds based on lineages input
"""
import argparse
import bz2
import classifier.lineages
import csv
import gzip
import itertools
import logging
import lzma
import math
import numpy
import pandas as pd
import pkg_resources
import operator
import os
import sys
import tarfile

ASSIGNMENT_TAX_ID = 'assignment_tax_id'

ALIGNMENT_DTYPES = {
    'accession': str,
    'assignment_id': str,
    'assignment_rank': str,
    'assignment_tax_id': str,
    'assignment_tax_name': str,
    'bitscore': float,
    'condensed_id': str,
    'evalue': float,
    'gapopen': int,
    'pident': float,
    'length': int,
    'mismatch': float,
    'pident': float,
    'qaccver': float,
    'qcovhsp': float,
    'qcovs': float,
    'qend': int,
    'qlen': int,
    'qseqid': str,
    'qstart': int,
    'rank': str,
    'saccver': str,
    'send': int,
    'specimen': str,
    'sseqid': str,
    'sstart': int,
    'staxid': str,
    'tax_id': str,
    'tax_name': str
}

ALIGNMENT_CONVERT = {
    'qaccver': 'qseqid',
    'saccver': 'sseqid'
}

OUTPUT_COLS = [
    'specimen', 'assignment_id', 'assignment',
    'best_rank', 'max_percent', 'min_percent',
    'min_threshold', 'reads', 'clusters', 'pct_reads']

DETAILS_COLS = [
    'specimen', 'assignment_id', 'tax_name', 'rank', 'assignment_tax_name',
    'assignment_rank', 'pident', 'tax_id', ASSIGNMENT_TAX_ID,
    'condensed_id', 'qseqid', 'sseqid', 'starred', 'assignment_threshold']


def setup_logging(namespace):
    """
    """
    log = opener(namespace.log, 'a')
    loglevel = {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG,
    }.get(namespace.verbosity, logging.DEBUG)
    if namespace.verbosity > 1:
        logformat = '%(levelname)s classifier %(message)s'
    else:
        logformat = 'classifier %(message)s'
    logging.basicConfig(stream=log, format=logformat, level=loglevel)


def main(argv=sys.argv[1:]):
    namespace = build_parser().parse_args(args=argv)
    setup_logging(namespace)
    return action(namespace)


def action(args):
    output_cols = list(OUTPUT_COLS)
    details_cols = list(DETAILS_COLS)
    logging.info('loading alignments ' + str(args.alignments))
    aligns = opener(args.alignments)
    header = aligns.buffer.peek().split(b'\n')[0]  # may not work on all OSs
    if b'\t' in header:
        sep = '\t'
    else:
        sep = ','
    if args.columns:
        conv = ALIGNMENT_CONVERT
        names = [conv.get(c, c) for c in args.columns.split(sep)]
    elif all(c in header for c in [b'qseqid', b'sseqid', b'pident']):
        names = None
    else:
        #  blast std
        names = ['qseqid', 'sseqid', 'pident', 'length',
                 'mismatch', 'gapopen', 'qstart', 'qend',
                 'sstart', 'send', 'evalue', 'bitscore']
    aligns = pd.read_csv(
        aligns,
        dtype=ALIGNMENT_DTYPES,
        names=names,
        sep=sep)

    # specimen grouping
    if args.specimen_map:
        spec_map = pd.read_csv(
            args.specimen_map,
            names=['specimen', 'qseqid', 'weight'],
            usecols=['specimen', 'qseqid', 'weight'],
            dtype={'qseqid': str, 'specimen': str, 'weight': float},
            header=None)
        spec_map = spec_map.drop_duplicates().set_index('qseqid')
        aligns = aligns.join(spec_map, on='qseqid', how='outer')
        # reset index to handle qseqids representing multiple clusters
        aligns = aligns.reset_index(drop=True)
        aligns['weight'] = aligns['weight'].fillna(1.0)
        imissing = aligns['specimen'].isna()
        aligns.loc[imissing, 'specimen'] = aligns[imissing]['qseqid']
    elif args.specimen:
        # all sequences are of one specimen
        aligns['specimen'] = args.specimen
        aligns['weight'] = 1.
    else:
        # each qseqid is its own specimen
        aligns['specimen'] = aligns['qseqid']  # by qseqid
        aligns['weight'] = 1.

    if aligns.empty:
        '''
        Return just the output headers if no data exists
        '''
        pd.DataFrame(columns=output_cols).to_csv(args.out, index=False)
        if args.details_out:
            pd.DataFrame(columns=details_cols).to_csv(
                args.details_out,
                index=False)
        return

    # get a set of qseqids for identifying [no blast hits] after filtering
    qseqids = aligns[['specimen', 'qseqid', 'weight']].drop_duplicates()

    '''
    Remove query sequences with no alignment information.
    These will be added back later but we do not want to
    confuse these with alignment results filtered by joins.
    '''
    aligns = aligns[aligns['sseqid'].notnull()]

    '''
    Load seq_info as a bridge to the sequence lineages.  Additional
    columns can be specified to be included in the details-out file
    such as accession number
    '''
    if 'staxid' in aligns.columns:
        aligns = aligns.rename(columns={'staxid': 'tax_id'})
    elif args.seq_info:
        logging.info('reading ' + args.seq_info)
        seq_info = read_seqinfo(args.seq_info, set(aligns['sseqid'].tolist()))
        # TODO: make a note that sseqid is a required column in the alignments!
        aligns_len = len(aligns)
        logging.info('joining')
        aligns = aligns.join(seq_info, on='sseqid', how='inner')
        len_diff = aligns_len - len(aligns)
        if len_diff:
            logging.warning('{} subject sequences dropped without '
                            'records in seq_info file'.format(len_diff))
    else:
        raise ValueError('missing either staxid column or seq_info.csv file')

    '''
    load the full lineages table.  Rank specificity as ordered from
    left (less specific) to right (more specific)
    '''
    if args.lineages:
        logging.info('reading ' + args.lineages)
        lineages = read_lineages(args.lineages, set(aligns['tax_id'].tolist()))
    else:
        tis = set(aligns['tax_id'].tolist())
        tree = build_lineages(tis, args.taxdump, args.tax_url)
        if args.no_rank_suffix:
            tree.expand_ranks(args.no_rank_suffix)
        else:  # we will want root (no rank) no matter what
            tree.include_root()
        lineages = pd.DataFrame(
            data=tree.root.get_lineages(tree.ranks),
            columns=['tax_id', 'tax_name', 'rank'] + tree.ranks)
    lineages = lineages.set_index('tax_id').dropna(axis='columns', how='all')

    if args.lineages_out:
        lineages.to_csv(args.lineages_out)

    ranks = lineages.columns.tolist()
    ranks = ranks[ranks.index('root'):]

    # now combine just the rank columns to the alignment results
    aligns_len = len(aligns)
    logging.info('joining with alignments')
    aligns = aligns.join(
        lineages[['tax_name', 'rank'] + ranks], on='tax_id', how='inner')
    len_diff = aligns_len - len(aligns)
    if len_diff:
        msg = '{} subject sequences dropped without records in lineages file'
        logging.warning(msg.format(len_diff))

    if args.rank_thresholds:
        rank_thresholds = load_rank_thresholds(args.rank_thresholds, ranks)
        rank_thresholds = rank_thresholds.groupby(level=0, sort=False).last()
        # remove ranks not in thresholds
        ranks = [r for r in ranks if r in rank_thresholds.columns]
    else:
        if 'species' in ranks:
            ispecies = ranks.index('species')
        else:
            ispecies = len(ranks) - 1
        rank_thresholds = {}
        for i, r in enumerate(ranks):
            if i <= ispecies:
                rank_thresholds[r] = 0.0
            else:
                rank_thresholds[r] = 100.0
        rank_thresholds = pd.DataFrame(
            data=rank_thresholds, columns=ranks, index=['1'])
        rank_thresholds.index.name = 'tax_id'

    # TODO: remove ranks with same threshold as lower/better rank

    rank_thresholds_cols = ['{}_threshold'.format(c) if c in ranks else c
                            for c in rank_thresholds.columns]
    rank_thresholds.columns = rank_thresholds_cols

    # joining rank thresholds file
    aligns = join_thresholds(
        aligns, rank_thresholds, ranks[::-1])

    # assign assignment tax ids based on pident and thresholds
    logging.info('selecting best alignments for classification')
    aligns_len = float(len(aligns))

    valid_hits = aligns.groupby(
        by=['specimen', 'qseqid'], group_keys=False)
    valid_hits = valid_hits.apply(select_valid_hits, ranks[::-1])

    if args.hits_below_threshold:
        """
        Store all the hits to append to aligns details later
        """
        hits_below_threshold = aligns[~aligns.index.isin(valid_hits.index)]

    aligns = valid_hits

    if not aligns.empty:
        aligns_post_len = len(aligns)
        msg = '{} alignments selected for assignment'
        logging.info(msg.format(aligns_post_len))

        # drop unneeded tax and threshold columns to free memory
        # TODO: see if this is necessary anymore since latest Pandas release
        for c in ranks + rank_thresholds_cols:
            aligns = aligns.drop(c, axis=1)

        # join with lineages for tax_name and rank
        aligns = aligns.join(
            lineages[['tax_name', 'rank']],
            rsuffix='_assignment',
            on=ASSIGNMENT_TAX_ID)

        # no join(rprefix) (yet)
        aligns = aligns.rename(
            columns={'tax_name_assignment': 'assignment_tax_name',
                     'rank_assignment': 'assignment_rank'})

        tax_dict = lineages.fillna('').to_dict(orient='index')

        # create condensed assignment hashes by qseqid
        msg = 'condensing group tax_ids to size {}'.format(args.max_group_size)
        logging.info(msg)
        aligns = aligns.groupby(
            by=['specimen', 'qseqid'], sort=False, group_keys=False)
        aligns = aligns.apply(
            condense_ids,
            tax_dict,
            ranks,
            args.max_group_size,
            threshold_assignments=args.threshold_assignments)

        aligns = aligns.join(
            lineages[['rank']], on='condensed_id', rsuffix='_condensed')

        aligns = aligns.rename(columns={'rank_condensed': 'condensed_rank'})

        # star condensed ids if one hit meets star threshold
        by = ['specimen', 'assignment_hash', 'condensed_id']
        aligns = aligns.groupby(
            by=by, sort=False, group_keys=False)
        aligns = aligns.apply(star, args.starred)

        # assign names to assignment_hashes
        aligns = aligns.sort_values(by='assignment_hash')
        logging.info('creating compound assignments')
        aligns = aligns.groupby(
            by=['specimen', 'assignment_hash'], sort=False, group_keys=False)
        aligns = aligns.apply(assign, tax_dict)

        # set this as str to handle na values for [no blast result]s
        aligns['starred'] = aligns['starred'].astype(str)

        # Foreach ref rank:
        # - merge with lineages, extract rank_id, rank_name
        for rank in args.include_ref_rank:
            aligns[rank + '_id'] = aligns.merge(
                lineages, left_on='tax_id',
                right_index=True,
                how='left')[rank].fillna(0)
            aligns[rank + '_name'] = aligns.merge(
                lineages,
                left_on=rank + '_id',
                right_index=True,
                how='left')['tax_name_y']

    # merge qseqids that have no hits back into aligns
    aligns = aligns.merge(qseqids, how='outer')

    # assign seqs that had no results to [no blast_result]
    no_hits = aligns['sseqid'].isnull()
    aligns.loc[no_hits, 'assignment'] = '[no blast result]'
    aligns.loc[no_hits, 'assignment_hash'] = 0
    aligns.loc[no_hits, 'assignment_tax_name'] = None
    aligns.loc[no_hits, 'assignment_rank'] = None
    aligns.loc[no_hits, 'condensed_id'] = None
    aligns.loc[no_hits, 'condensed_rank'] = None
    aligns.loc[no_hits, 'starred'] = None

    # concludes our alignment details, on to output summary
    logging.info('summarizing output')

    # index by specimen and assignment_hash and add assignment column
    index = ['specimen', 'assignment_hash']
    output = aligns[index + ['assignment']].drop_duplicates()
    output = output.set_index(index)

    # assignment level stats
    assignment_stats = aligns.groupby(by=index, sort=False)
    output['max_percent'] = assignment_stats['pident'].max()
    output['min_percent'] = assignment_stats['pident'].min()
    output['min_threshold'] = assignment_stats['assignment_threshold'].min()
    output['best_rank'] = assignment_stats[['condensed_rank']].apply(
        best_rank, ranks)

    # qseqid cluster stats
    weights = aligns[
        ['qseqid', 'specimen', 'assignment_hash',
         'assignment_threshold', 'weight']]
    weights = weights.drop_duplicates().set_index('qseqid')

    cluster_stats = weights[['specimen', 'assignment_hash', 'weight']]
    cluster_stats = cluster_stats.reset_index().drop_duplicates()
    cluster_stats = cluster_stats.groupby(
        by=['specimen', 'assignment_hash'], sort=False)

    output['reads'] = cluster_stats['weight'].sum()
    output['clusters'] = cluster_stats.size()

    # specimen level stats
    specimen_stats = output.groupby(level='specimen', sort=False)
    output['pct_reads'] = specimen_stats['reads'].apply(pct)

    # copy number corrections
    if args.copy_numbers:
        corrections = copy_corrections(args.copy_numbers, aligns)
        output['corrected'] = output['reads'] / corrections
        # reset corrected counts to int before calculating pct_corrected
        output['corrected'] = output['corrected'].apply(math.ceil)
        output['corrected'] = output['corrected'].fillna(1).astype(int)
        # create pct_corrected column
        output['pct_corrected'] = specimen_stats['corrected'].apply(pct)
        output['pct_corrected'] = output['pct_corrected'].map(round_up)
        output_cols.extend(['corrected', 'pct_corrected'])

    # round reads for output
    output['reads'] = output['reads'].apply(round).astype(int)
    output['pct_reads'] = output['pct_reads'].map(round_up)

    # sort output by:
    # 1) specimen -- Data Frame is already grouped by specimen
    # 2) read/corrected count
    # 3) cluster count
    # 4) alpha assignment
    columns = ['corrected'] if args.copy_numbers else ['reads']
    columns += ['clusters', 'assignment']
    output = output.sort_values(by=columns, ascending=False)
    output = output.reset_index(level='assignment_hash')

    # one last groupby and sort on the assignment ids by specimen
    output = output.groupby(level="specimen").apply(assignment_id)

    # output to details.csv.bz2
    if args.details_out:
        # Annotate details with classification columns
        aligns = aligns.merge(output.reset_index(), how='left')

        if not args.details_full:
            """
            by using the assignment_threshold we will get multiple 'largest'
            centroids for --max-group-size combined assignments
            """
            # groupby will drop NA values so we must fill them with 0
            weights['assignment_threshold'] = weights[
                'assignment_threshold'].fillna(0)
            largest = weights.groupby(
                by=['specimen', 'assignment_hash', 'assignment_threshold'],
                sort=False)
            largest = largest.apply(lambda x: x['weight'].nlargest(1))
            largest = largest.reset_index()
            # assignment_threshold will conflict with aligns NA values
            largest = largest.drop('assignment_threshold', axis=1)
            aligns = aligns.merge(largest)

        ref_rank_columns = [rank + '_id' for rank in args.include_ref_rank]
        ref_rank_columns += [rank + '_name' for rank in args.include_ref_rank]
        details_cols += ref_rank_columns

        if args.hits_below_threshold:
            """
            append assignment_thresholds and append to --details-out
            """
            deets_cols = hits_below_threshold.columns
            deets_cols &= set(details_cols)
            hits_below_threshold = hits_below_threshold[list(deets_cols)]
            threshold_cols = ['specimen', 'qseqid', 'assignment_threshold']
            assignment_thresholds = aligns[threshold_cols]
            assignment_thresholds = assignment_thresholds.drop_duplicates()
            hits_below_threshold = hits_below_threshold.merge(
                assignment_thresholds, how='left')
            aligns = pd.concat(
                [aligns, hits_below_threshold], ignore_index=True, sort=False)

        """sort details for consistency and ease of viewing.
        [no blast results] may have irregular aligns.columns
        """
        aligns = aligns.sort_values(by=details_cols)

        aligns.to_csv(
            args.details_out,
            columns=details_cols,
            header=True,
            index=False,
            float_format='%.2f')

    # was required to merge with details above but not needed now
    output = output.drop('assignment_hash', axis=1)

    # output results
    output.to_csv(
        args.out,
        columns=[c for c in output_cols if c in output.columns],
        index=True,
        float_format='%.2f')


def assign(df, tax_dict):
    """Create str assignment based on tax_ids str and starred boolean.
    """
    ids_stars = df.groupby(by=['condensed_id', 'starred']).groups.keys()
    df['assignment'] = compound_assignment(ids_stars, tax_dict)
    return df


def assignment_id(df):
    """Resets and drops the current dataframe's
    index and sets it to the assignment_hash

    assignment_id is treated as a string identifier to account
    for hits in details with no assignment or assignment_id
    """
    df = df.reset_index(drop=True)  # specimen is retained in the group key
    df.index.name = 'assignment_id'
    df.index = df.index.astype(str)
    return df


def best_rank(df, ranks):
    """The rank with the majority associated alignments is considered
    best_rank. In the event of a tie the most specific rank is selected.

    `ranks' are sorted with less specific first for example:

    ['root', 'kingdom', 'phylum', 'order', 'family',
     'genus', 'species_group', 'species']

    so when sorting the indexes the most specific
    rank will be in the iloc[-1] location
    """
    if len(df) == 0:
        # [no blast result]
        return None
    else:
        def specificity(r):
            return ranks.index(r) if r in ranks else -1
        df['specificity'] = df['condensed_rank'].apply(specificity)
        df = df.sort_values(by=['specificity'])
        # most precise rank is at the highest index (-1)
        return df['condensed_rank'].iloc[-1]


def test():
    return build_parser()


def build_lineages(tax_ids, tar, url):
    if tar is None or not os.path.isfile(tar):
        tar = classifier.lineages.get_taxdmp(url)
    with tarfile.open(name=tar, mode='r:gz') as taxdmp:
        logging.info('building lineages from NCBI')
        nodes, names = classifier.lineages.get_data(taxdmp)
        tree = classifier.lineages.Tree(nodes, names)
    tree.root.prune(tax_ids)
    return tree


def build_parser():
    parser = argparse.ArgumentParser()
    # required inputs
    parser.add_argument(
        'alignments',
        default=sys.stdin,
        nargs='?',
        help=('alignment file with query and '
              'subject sequence hits and optional header'))
    parser.add_argument(
        '--seq-info',
        metavar='',
        help='map file seqname to tax_id')

    package_parser = parser.add_argument_group(
        title='logging and version options')
    package_parser.add_argument(
        '-V', '--version',
        action='version',
        version=pkg_resources.get_distribution('classifier').version,
        help='Print the version number and exit')
    package_parser.add_argument(
        '-l', '--log',
        metavar='',
        default=sys.stdout,
        help='Send logging to a file')
    package_parser.add_argument(
        '-v', '--verbose',
        action='count',
        dest='verbosity',
        default=0,
        help='Increase verbosity of screen output '
             '(eg, -v is verbose, -vv more so)')
    package_parser.add_argument(
        '-q', '--quiet',
        action='store_const',
        dest='verbosity',
        const=0,
        help='Suppress output')

    align_parser = parser.add_argument_group(
        title='alignment input header-less options',
        description=('will detect if header with '
                     'qseqid,sseqid,pident else blast6 columns'))
    columns_parser = align_parser.add_mutually_exclusive_group(required=False)
    columns_parser.add_argument(
        '--columns', '-c',
        metavar='',
        help=('specify columns for header-less comma-seperated values'))

    selection_parser = parser.add_argument_group('selection options')
    selection_parser = selection_parser.add_mutually_exclusive_group(
        required=False)
    selection_parser.add_argument(
        '--rank-thresholds',
        metavar='',
        help='Columns [tax_id,ranks...] [%(default)s]')
    selection_parser.add_argument(
        '--top-n-pct',
        metavar='',
        default=25,
        type=float,
        help=('top percent hits sorted by pident, evalue '
              'or bitscore per taxonomy group'))

    assignment_parser = parser.add_argument_group('assignment options')
    assignment_parser.add_argument(
        '--starred',
        metavar='',
        default=100.0,
        type=float,
        help=('Names of organisms for which at least one reference '
              'sequence has pairwise identity with a query sequence of at '
              'least PERCENT will be marked with an asterisk [%(default)s]'))
    assignment_parser.add_argument(
        '--max-group-size',
        metavar='',
        default=3,
        type=int,
        help=('group multiple target-rank assignments that excede a '
              'threshold to a higher rank [%(default)s]'))
    assignment_parser.add_argument(
        '--split-condensed-assignments',
        action='store_true',
        dest='threshold_assignments',
        help=('Group final assignment classifications '
              'before assigning condensed taxonomic ids'))

    # optional inputs
    opts_parser = parser.add_argument_group('other input options')
    opts_parser.add_argument(
        '--copy-numbers',
        metavar='',
        help=('Estimated 16s rRNA gene copy number for each tax_ids '
              '(CSV file with columns: tax_id, count)'))
    opts_group = opts_parser.add_mutually_exclusive_group(required=False)
    opts_group.add_argument(
        '--specimen',
        metavar='',
        help='Single group label for reads')
    opts_group.add_argument(
        '--specimen-map',
        metavar='',
        help='Three column headerless csv file specimen,qseqid,weight')

    # lineage taxonomy source data
    lineage_parser = parser.add_argument_group(
        'lineage and ncbi source options')
    lineage_parser.add_argument(
        '--lineages',
        help='Table defining taxonomic lineages for each taxonomy id')
    lineage_parser.add_argument(
        '--taxdump',
        default='taxdump.tar.gz',
        help='lineages source data [%(default)s]')
    lineage_parser.add_argument(
        '--tax-url',
        default='ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz',
        help='url for downloading taxdump file [%(default)s]')
    lineage_parser.add_argument(
        '--no-rank-suffix',
        help='expand and include no rank taxonomies '
             'with appended string suffix')

    outs_parser = parser.add_argument_group('output options')
    outs_parser.add_argument(
        '--details-full',
        action='store_true',
        help=('do not limit out_details to largest '
              'cluster per assignment [%(default)s]'))
    outs_parser.add_argument(
        '--include-ref-rank',
        action='append',
        default=[],
        metavar='',
        help=('Given a single rank (species,genus,etc), '
              'include each reference '
              'sequence\'s tax_id as ${rank}_id and its taxonomic name as '
              '${rank}_name in details output'))
    outs_parser.add_argument(
        '--hits-below-threshold',
        action='store_true',
        help=('Hits that were below the best-rank threshold '
              'will be included in the details'))
    outs_parser.add_argument(
        '--details-out',
        metavar='',
        help='Optional details of taxonomic assignments')
    outs_parser.add_argument(
        '--lineages-out',
        metavar='',
        help='Output blast input specific lineages file')
    outs_parser.add_argument(
        '-o', '--out',
        metavar='',
        default=sys.stdout,
        help="classification results [default: stdout]")
    return parser


def calculate_pct_references(df, pct_reference):
    '''
    Not used yet.  Given a total number of reference sequences this function
    will divide the sseqids by the reference sequence
    count for a pct_reference.
    '''
    reference_count = df[['tax_id']].drop_duplicates()
    reference_count = reference_count.join(pct_reference, on='tax_id')
    reference_count = reference_count['count'].sum()
    sseqid_count = float(len(df['sseqid'].drop_duplicates()))
    df['pct_reference'] = sseqid_count / reference_count
    return df


def compound_assignment(assignments, lineages):
    """
    Create taxonomic names based on 'assignmnets', which are a set of
    two-tuples: {(tax_id, is_starred), ...} where each tax_id is a key
    into taxdict, and is_starred is a boolean indicating whether at
    least one reference sequence had a parirwise alignment identity
    score meeting some thresholed. 'taxdict' is a dictionary keyed by
    tax_id and returning a dict of taxonomic data corresponding to a
    row from the lineages file. If 'include_stars' is False, ignore
    the second element of each tuple in 'assignments' and do not
    include asterisks in the output names.
    assignments = [(tax_id, is_starred),...]
    lineages = {taxid:lineages}
    Functionality: see format_lineages
    """
    if not lineages:
        raise TypeError('lineages must not be empty or NoneType')

    assignments = ((lineages[i]['tax_name'], a) for i, a in assignments)
    assignments = zip(*assignments)

    return format_lineages(*assignments, asterisk='*')


def condense(assignments,
             lineages,
             ranks,
             floor_rank=None,
             ceiling_rank=None,
             max_size=3,
             rank_thresholds={}):
    """
    assignments = [tax_ids...]
    lineages = {taxid:lineages}

    Functionality: Group items into taxonomic groups given max rank sizes.
    """

    floor_rank = floor_rank or ranks[-1]
    ceiling_rank = ceiling_rank or ranks[0]

    if not lineages:
        raise TypeError('lineages must not be empty or NoneType')

    if floor_rank not in ranks:
        msg = '{} not in ranks: {}'.format(floor_rank, ranks)
        raise TypeError(msg)

    if ceiling_rank not in ranks:
        msg = '{} not in ranks: {}'.format(ceiling_rank, ranks)
        raise TypeError(msg)

    if ranks.index(floor_rank) < ranks.index(ceiling_rank):
        msg = '{} cannot be lower rank than {}'.format(
            ceiling_rank, floor_rank)
        raise TypeError(msg)

    # set rank to ceiling
    try:
        assignments = {a: lineages[a][ceiling_rank] for a in assignments}
    except KeyError:
        error = ('Assignment id not found in lineages.')
        raise KeyError(error)

    def walk_taxtree(groups, ceiling_rank=ceiling_rank, max_size=max_size):
        new_groups = {}

        for a, r in groups.items():
            new_groups[a] = lineages[a][ceiling_rank] or r

        num_groups = len(set(new_groups.values()))

        if rank_thresholds.get(ceiling_rank, max_size) < num_groups:
            return groups

        groups = new_groups

        # return if we hit the floor
        if ceiling_rank == floor_rank:
            return groups

        # else move down a rank
        ceiling_rank = ranks[ranks.index(ceiling_rank) + 1]

        # recurse each branch down the tax # tree
        branches = sorted(groups.items(), key=operator.itemgetter(1))
        for _, g in itertools.groupby(branches, operator.itemgetter(1)):
            g = walk_taxtree(
                dict(g), ceiling_rank, max_size - num_groups + 1)
            groups.update(g)

        return groups

    return walk_taxtree(assignments)


def condense_ids(
        df, tax_dict, ranks, max_group_size, threshold_assignments=False):
    """
    Create mapping from tax_id to its condensed id.  Also creates the
    assignment hash on either the condensed_id or assignment_tax_id decided
    by the --split-condensed-assignments switch.

    By taking a hash of the set (frozenset) of ids the qseqid is given a
    unique identifier (the hash).  Later, we will use this hash and
    assign an assignment name based on either the set of condensed_ids or
    assignment_tax_ids.  The modivation for using a hash rather than
    the actual assignment text for grouping is that the assignment text
    can contains extra annotations that are independent of which
    assignment group a qseqid belongs to such as a 100% id star.
    """
    condensed = condense(
        df[ASSIGNMENT_TAX_ID].unique(),
        tax_dict,
        ranks=ranks,
        max_size=max_group_size)

    condensed = pd.DataFrame(
        list(condensed.items()),
        columns=[ASSIGNMENT_TAX_ID, 'condensed_id'])
    condensed = condensed.set_index(ASSIGNMENT_TAX_ID)

    if threshold_assignments:
        assignment_hash = hash(frozenset(condensed.index.unique()))
    else:
        assignment_hash = hash(frozenset(condensed['condensed_id'].unique()))

    condensed['assignment_hash'] = assignment_hash
    return df.join(condensed, on=ASSIGNMENT_TAX_ID)


def copy_corrections(copy_numbers, aligns, user_file=None):
    copy_numbers = pd.read_csv(
        copy_numbers,
        dtype=dict(tax_id=str, count=float),
        usecols=['tax_id', 'count']).set_index('tax_id')

    # get root out (taxid: 1) and set it as the default correction value

    # set index nan (no blast result) to the default value
    default = copy_numbers.at['1', 'count']
    default_entry = pd.DataFrame(default, index=[None], columns=['count'])
    copy_numbers = copy_numbers.append(default_entry, sort=False)

    # do our copy number correction math
    corrections = aligns[
        [ASSIGNMENT_TAX_ID, 'specimen', 'assignment_hash']]
    corrections = corrections.drop_duplicates()
    corrections = corrections.set_index(ASSIGNMENT_TAX_ID)
    corrections = corrections.join(copy_numbers)
    # any tax_id not present will receive default tax_id
    corrections['count'] = corrections['count'].fillna(default)
    corrections = corrections.groupby(
        by=['specimen', 'assignment_hash'], sort=False)
    corrections = corrections['count'].mean()
    return corrections


def find_tax_id(lineage, valids, ranks):
    """Return the most taxonomic specific tax_id available for the given
    Series.  If a tax_id is already present in valids then return None.
    """
    lineage = lineage[ranks]  # just the remainging higher rank tax_ids
    lineage = lineage[~lineage.isnull()]
    found = lineage.head(n=1)  # best available tax_id
    key = found.index.values[0]
    value = found.values[0]
    return value if value not in valids[key].unique() else None


def format_lineages(names, selectors, asterisk='*'):
    """
    Create a friendly formatted string of lineages names. Names will
    have an asterisk value appended *only* if the cooresponding
    element in the selectors evaluates to True.
    """
    names = itertools.zip_longest(names, selectors)
    names = ((n, asterisk if s else '')
             for n, s in names)  # add asterisk to selected names
    names = set(names)
    names = sorted(names)  # sort by the name plus asterisk
    # group by just the names
    names = itertools.groupby(names, key=operator.itemgetter(0))
    # prefer asterisk names which will be at the bottom
    names = (list(g)[-1] for _, g in names)
    names = (n + a for n, a in names)  # combine names with asterisks
    # assume species names have exactly two words

    def is_species(s):
        return len(s.split()) == 2

    names = sorted(names, key=is_species)
    names = itertools.groupby(names, key=is_species)

    tax = []

    for species, assigns in names:
        if species:
            # take the species word and combine them with a '/'
            assigns = (a.split() for a in assigns)
            # group by genus name
            assigns = itertools.groupby(assigns, key=operator.itemgetter(0))
            assigns = ((k, map(operator.itemgetter(1), g))
                       for k, g in assigns)  # get a list of the species names
            assigns = ('{} {}'.format(k, '/'.join(g))
                       for k, g in assigns)  # combine species names with '/'

        tax.extend(assigns)

    return ';'.join(sorted(tax))


def join_thresholds(df, thresholds, ranks):
    """Thresholds are matched to thresholds by rank id.

    If a rank id is not present in the thresholds then the next specific
    rank id is used all the way up to `root'.  If the root id still does
    not match then a warning is issued with the taxname and the alignment
    is dropped.
    """
    with_thresholds = pd.DataFrame(columns=df.columns)  # temp DFrame

    for r in ranks:
        with_thresholds = with_thresholds.append(
            df.join(thresholds, on=r, how='inner'), sort=False)
        no_threshold = df[~df.index.isin(with_thresholds.index)]
        df = no_threshold

    # issue warning messages for everything that did not join
    if len(df) > 0:
        tax_names = df['tax_name'].drop_duplicates()
        msg = ('dropping alignment `{}\', no valid '
               'taxonomic threshold information found')
        tax_names.apply(lambda x: logging.warning(msg.format(x)))

    return with_thresholds


def load_rank_thresholds(path, usecols):
    """
    Load a rank-thresholds file.  If no argument is specified the default
    rank_threshold_defaults.csv file will be loaded.
    """
    dtypes = {'tax_id': str}
    dtypes.update(zip(usecols, [float] * len(usecols)))
    rank_thresholds = pd.read_csv(path, comment='#', dtype=dtypes)
    rank_thresholds = rank_thresholds.set_index('tax_id')
    drop = [col for col in rank_thresholds.columns if col not in usecols]
    return rank_thresholds.drop(drop, axis=1)


def round_up(x):
    """round up any x < 0.01
    """
    return max(0.01, x)


def select_valid_hits(df, ranks):
    """Return valid hits of the most specific rank that passed their
    corresponding rank thresholds.  Hits that pass their rank thresholds
    but do not have a tax_id at that rank will be bumped to a less specific
    rank id and varified as a unique tax_id.
    """

    for r in ranks:
        assignment_threshold = '{}_threshold'.format(r)
        valid = df[df[assignment_threshold] < df['pident']]

        if valid.empty:
            # Move to higher rank
            continue

        tax_ids = valid[r]
        na_ids = tax_ids.isnull()

        '''
        Occasionally tax_ids will be missing at a certain rank.
        If so use the next less specific tax_id available
        '''
        if na_ids.all():
            continue

        if na_ids.any():
            # bump up missing taxids
            have_ids = valid[tax_ids.notnull()]
            # for each row without a tax_id find the next highest tax_id
            remaining_ranks = ranks[ranks.index(r):]
            found_ids = valid[na_ids].apply(
                find_tax_id, args=(have_ids, remaining_ranks), axis=1)
            tax_ids = have_ids[r].append(found_ids)

        valid[ASSIGNMENT_TAX_ID] = tax_ids
        valid['assignment_threshold'] = valid[assignment_threshold]
        return valid[valid[ASSIGNMENT_TAX_ID].notnull()]

    '''
    we have cycled through all the available ranks and nothing passed
    so we return an empty df
    '''
    df[ASSIGNMENT_TAX_ID] = None
    df['assignment_threshold'] = None
    return pd.DataFrame(columns=df.columns)


def pct(s):
    """Calculate series pct something
    """
    return s / s.sum() * 100


def read_seqinfo(path, ids):
    """
    Iterates through seq_info file only including
    necessary seqname to tax_id mappings
    """
    with opener(path) as infofile:
        seq_info = csv.reader(infofile)
        header = next(seq_info)
        seqname, tax_id = header.index('seqname'), header.index('tax_id')
        seq_info = (row for row in seq_info if row[seqname] in ids)
        seq_info = {row[seqname]: row[tax_id] for row in seq_info}
    return pd.Series(data=seq_info, name='tax_id')


def read_lineages(path, ids):
    """
    Iterates through lineages file only including necessary lineages

    FIXME: tax_ids after first pass can disappear if tax_id rank not in columns
    """
    with opener(path) as taxfile:
        taxcsv = csv.reader(taxfile)
        header = next(taxcsv)
        tax_id, root = header.index('tax_id'), header.index('root')
        taxcsv = (r for r in taxcsv if r[tax_id] in ids)
        tax_ids = set(i for r in taxcsv for i in r[root:] if i != '')
    with opener(path) as taxfile:
        taxcsv = csv.reader(taxfile)
        header = next(taxcsv)
        taxcsv = (r for r in taxcsv if r[tax_id] in tax_ids)
        taxcsv = (map(lambda x: x if x else numpy.nan, r) for r in taxcsv)
        data = [dict(zip(header, r)) for r in taxcsv]
    return pd.DataFrame(data=data, columns=header)


def opener(f, mode='rt'):
    """Factory for creating file objects

    Keyword Arguments:
        - mode -- A string indicating how the file is to be opened. Accepts the
            same values as the builtin open() function.
        - bufsize -- The file's desired buffer size. Accepts the same values as
            the builtin open() function.
    """
    stream = None
    if f is sys.stdout or f is sys.stdin:
        stream = f
    elif f == '-':
        stream = sys.stdin if 'r' in mode else sys.stdout
    elif f.endswith('.bz2'):
        stream = bz2.open(f, mode)
    elif f.endswith('.gz'):
        stream = gzip.open(f, mode)
    elif f.endswith('.xz'):
        stream = lzma.open(f, mode)
    else:
        stream = open(f, mode)
    return stream


def star(df, starred):
    """Assign boolean if any items in the
    dataframe are above the star threshold.
    """
    df['starred'] = df['pident'].apply(lambda x: x >= starred).any()
    return df
