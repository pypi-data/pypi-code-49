import os
from collections import defaultdict

import numpy as np
import pandas as pd

from jphmm_tools import parse_breakpoints, breakpoints2bitmasks, shift_bitmask, expand_crfs, \
    parse_aligned_coordinates, \
    parse_bitmask, get_reference_coordinates, HXB2_LOS_ALAMOS_ID, VERSION

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
HIV1_BREAKPOINTS = os.path.join(DATA_DIR, 'HIV1.breakpoints')

COMPATIBLE_SUBTYPE_COL = 'compatible_subtypes'
SUBTYPE_JPHMM_COL = 'subtype_jpHMM'


def get_subtypes(jphmm_msas, jphmm_recs, gappy_breakpoint_bitmask_file=None,
                 breakpoint_file=HIV1_BREAKPOINTS, aln_file=None,
                 reference_id=HXB2_LOS_ALAMOS_ID, slack=0, generalise_subtypes=True):
    """
    Converts the jpHMM output files to a dataframe containing two columns: one with the subtypes detected by jpHMM,
    and the other with the compatible subtypes (e.g. including different CRFs).

    :param jphmm_msas: path(s) to jpHMM-produced alignment file(s) (such as alignment_to_msa.txt)
    :type jphmm_msas: list(str) or str
    :param jphmm_recs: path(s) to jpHMM-produced breakpoint file(s) (such as recombination.txt)
    :type jphmm_recs: list(str) or str
    :param gappy_breakpoint_bitmask_file: (optional) path to the file containing bitmask for the CRF breakpoints,
        aligned. If not specified, breakpoint_file and aln_file must be specified.
    :type gappy_breakpoint_bitmask_file: str
    :param breakpoint_file: (optional) path to the file CRF breakpoint interval file.
        Must be specified together with the alignment file used by jpHMM.
        Otherwise, gappy_breakpoint_bitmask_file must be specified.
    :type breakpoint_file: str
    :param aln_file: (optional) path to the alignment file used by jpHMM.
        Must be specified together if breakpoint_file is used to specify CRF breakpoints.
    :param reference_id: (optional) need to be specified if aln_file+breakpoint_file are used to specify CRF breakpoints.
        The id of the sequences used as the reference for the breakpoint coordinates (HXB2 most probably) in the aln_file.
    :type reference_id: str
    :param slack: (optional, default is 0) number of nucleotides for which the wrong subtype
        can be ignored while matching CRFs.
    :type slack: int
    :param generalise_subtypes: if True the more specific subtypes (e.g. A1, A2)
        will be replaced by more generic ones (e.g. A).
    :type generalise_subtypes: bool
    :return: dataframe with sequence ids as indices and two columns,
        corresponding to the jpHMM detected subtypes inside each sequence and to the compatible subtypes and CRFs.
    :rtype: pandas.DataFrame
    """

    if gappy_breakpoint_bitmask_file is None:
        if breakpoint_file is None or aln_file is None:
            raise ValueError('Either the gappy breakpoint bitmask file '
                             'or the breakpoint file + the alignment file (used for jpHMM subtyping) must be specified')
        crf2st2bitmask, n_gappy = get_gappy_breakpoints(breakpoint_file, aln_file, reference_id,
                                                        generalise_subtypes=generalise_subtypes)
    else:
        crf2st2bitmask = parse_bitmask(gappy_breakpoint_bitmask_file)
        n_gappy = get_length(crf2st2bitmask)

    id2insertion_length, id2n, id2st2bitmask = jphmm2bitmask(crf2st2bitmask, jphmm_msas, jphmm_recs, n_gappy,
                                                             generalise_subtypes=generalise_subtypes)

    df = pd.DataFrame(columns=[SUBTYPE_JPHMM_COL, COMPATIBLE_SUBTYPE_COL])
    for name, st2bitmask in id2st2bitmask.items():
        length = id2n[name]
        ins_length = id2insertion_length[name]
        if length < ins_length:
            df.loc[name, SUBTYPE_JPHMM_COL] = None
            continue

        subtypes = set(st2bitmask.keys())
        df.loc[name, SUBTYPE_JPHMM_COL] = ','.join(sorted(subtypes))

        potential_subtypes = []
        if len(subtypes) == 1:
            potential_subtypes.extend(subtypes)

        for crf, crf_st2bitmask in crf2st2bitmask.items():
            if subtypes - set(crf_st2bitmask.keys()):
                continue
            incompatible = False
            for st, bitmask in st2bitmask.items():
                if np.any(bitmask & ~crf_st2bitmask[st]):
                    if slack:
                        incompatible_len = sum((bitmask & ~crf_st2bitmask[st]).astype(int))
                        if incompatible_len <= slack:
                            continue
                    incompatible = True
                    break
            if not incompatible:
                potential_subtypes.append(crf)
        df.loc[name, COMPATIBLE_SUBTYPE_COL] = '/'.join(sorted(potential_subtypes))

    return df


def get_gappy_breakpoints(breakpoint_file, aln_file, reference_id=HXB2_LOS_ALAMOS_ID, generalise_subtypes=True):
    """
    Converts a CRF breakpoint interval file and the alignment file used by jpHMM
    into an aligned breakpoint bitmask mapping.

    :param breakpoint_file: (optional) path to the file CRF breakpoint interval file.
        Must be specified together with the alignment file used by jpHMM.
        Otherwise, gappy_breakpoint_bitmask_file must be specified.
    :type breakpoint_file: str
    :param aln_file: (optional) path to the alignment file used by jpHMM.
        Must be specified together if breakpoint_file is used to specify CRF breakpoints.
    :param reference_id: (optional) need to be specified if aln_file+breakpoint_file are used to specify CRF breakpoints.
        The id of the sequences used as the reference for the breakpoint coordinates (HXB2 most probably) in the aln_file.
    :type reference_id: str
    :param generalise_subtypes: if True the more specific subtypes (e.g. A1, A2)
        will be replaced by more generic ones (e.g. A).
    :type generalise_subtypes: bool
    :return: mapping between CRF ids and a mapping of subtypes to breakpoint interval list (aligned):
        {id: {subtype: [(start, stop), ...], ...}, ..}
    :rtype: dict
    """
    crf2st2bitmask = breakpoints2bitmasks(parse_breakpoints(breakpoint_file), generalise_subtypes=generalise_subtypes)
    expand_crfs(crf2st2bitmask, crf2st2bitmask)

    position_shift, n, n_gappy = get_reference_coordinates(aln_file, reference_id=reference_id)
    shift_bitmask(crf2st2bitmask, defaultdict(lambda: position_shift), n_gappy)

    return crf2st2bitmask, n_gappy


def jphmm2bitmask(crf2st2bitmask, jphmm_msas, jphmm_recs, n_gappy, generalise_subtypes=True):
    """
    Converts a jpHMM output breakpoint interval (e.g. recombination.txt) and alignment (e.g. aignment_to_msa.txt) file(s)
    into an aligned breakpoint bitmask mapping.

    :param crf2st2bitmask: mapping between CRF ids and a mapping of subtypes to breakpoint interval list (aligned):
        {id: {subtype: [(start, stop), ...], ...}, ..}
    :type crf2st2bitmask: dict
    :param jphmm_msas: path to jpHMM-produced alignment file(s) (such as alignment_to_msa.txt)
    :type jphmm_msas: list(str) or str
    :param jphmm_recs: path to jpHMM-produced breakpoint file(s) (such as recombination.txt)
    :type jphmm_recs: list(str) or str
    :param n_gappy: length of the alignment
    :type n_gappy: int
    :param generalise_subtypes: if True the more specific subtypes (e.g. A1, A2)
        will be replaced by more generic ones (e.g. A).
    :type generalise_subtypes: bool
    :return: tuple of mappings of sequence ids to (1) lengths of (5'- plus 3'-) insertions detected by jpHMM,
        (2) lengths of the sequences, (3) mapping of subtypes to breakpoint interval list (aligned):
        {subtype: [(start, stop), ...], ...}
    :rtype: tuple(dict)
    """
    id2st2interval = parse_breakpoints(jphmm_recs)
    id2n = {name: max(max(stop for (start, stop) in intervals) for intervals in st2intervals.values())
            for name, st2intervals in id2st2interval.items()}
    id2st2bitmask = breakpoints2bitmasks(id2st2interval, generalise_subtypes=generalise_subtypes)
    id2pos = parse_aligned_coordinates(jphmm_msas)
    id2insertion_length = shift_bitmask(id2st2bitmask, id2pos, n_gappy, gap_fill=0)
    expand_crfs(id2st2bitmask, crf2st2bitmask)
    return id2insertion_length, id2n, id2st2bitmask


def get_length(crf2subtype2bitmask):
    """
    Calculates the alignment length for the breakpoint bitmask mapping.

    :param crf2subtype2bitmask: mapping between CRF ids and a mapping of subtypes to breakpoint interval list (aligned):
        {id: {subtype: [(start, stop), ...], ...}, ..}
    :type crf2subtype2bitmask: dict
    :return: alignment length
    :rtype: int
    """
    return len(next(iter(next(iter(crf2subtype2bitmask.values())).values())))


def main():
    """
    Entry point, calling :py:func:`jphmm_tools.aligner.get_subtypes` with command-line arguments,
    then saving the result to a file.

    :return: void
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Extracts sequence subtype information from the jpHMM (http://jphmm.gobics.de) output.",
        prog='jphmm_subtype')

    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=VERSION))

    jphmm_group = parser.add_argument_group('jpHMM-output-file-related arguments')
    jphmm_group.add_argument('--jphmm_msas', nargs='+', type=str,
                             help="Path(s) to jpHMM-produced alignment file(s) (such as alignment_to_msa.txt).")
    jphmm_group.add_argument('--jphmm_recs', nargs='+', type=str,
                             help="Path(s) to jpHMM-produced breakpoint file(s) (such as recombination.txt).")

    bp_group = parser.add_argument_group('CRF-breakpoint-related arguments')
    bp_group.add_argument('--gappy_breakpoint_bitmask_file', required=False, type=str,
                          help="Path to the file containing bitmask for the CRF breakpoints, aligned."
                               " If not specified, --breakpoint_file and --aln_file must be specified.")
    bp_group.add_argument('--breakpoint_file', required=False, default=HIV1_BREAKPOINTS, type=str,
                          help="Path to the file CRF breakpoint interval file."
                               " Must be specified together with the alignment file used by jpHMM."
                               " Otherwise, --gappy_breakpoint_bitmask_file must be specified.")
    bp_group.add_argument('--aln_file', required=False, type=str,
                          help="Path to the alignment file used by jpHMM."
                               " Must be specified together if --breakpoint_file is used to specify CRF breakpoints.")
    bp_group.add_argument('--reference_id', required=False, default=HXB2_LOS_ALAMOS_ID, type=str,
                          help="Need to be specified if --aln_file + --breakpoint_file are used to specify CRF breakpoints."
                               " The id of the sequences used as the reference for the breakpoint coordinates "
                               "(HXB2 most probably) in the --aln_file")

    tune_group = parser.add_argument_group('Fine-tuning arguments')
    tune_group.add_argument('--slack', default=0, type=int,
                            help="Number of nucleotides for which the wrong subtype can be ignored while matching CRFs.")
    tune_group.add_argument('--generalise_subtypes', action='store_true',
                            help="Replace the more specific subtypes (e.g. A1, A2) by more generic ones (e.g. A).")

    out_group = parser.add_argument_group('Output arguments')
    out_group.add_argument('--out_tab', required=True, type=str,
                           help="Path to the file where the tab-separated table "
                                "with the subtype infromation will be stored.")

    params = parser.parse_args()
    tab = params.out_tab

    params = vars(params)
    del params['out_tab']
    get_subtypes(**params).to_csv(tab, sep='\t', index_label='id')


if '__main__' == __name__:
    main()
