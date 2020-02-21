"""Landscape module with analyses on sequence space"""

import pandas as pd
import numpy as np
import Levenshtein as Distance
from doc_helper import DocHelper
import logging

Distance.__doc__ = """Accessor to `python-levenshtein` module for distance measure

Common functions:
  - distance(seq1, seq2): levenshtein distance between two sequences
  - hamming(seq1, seq2): hamming distance between two sequences 
"""

peak_doc = DocHelper(
    center_seq=('str', 'center sequence of the peak'),
    seqs=('list-like of str, pd.DataFrame',
          'A list-like (list, np.ndarray, pd.Series) of str for a collect of '
          'sequences in the landscape to survey. Or a pd.DataFrame table with '
          'sequences as indices, samples as columns as quantity measures (e.g. counts'),
    radius=('int', 'radius of the peak for a sequence to be considered as a member, optional'),
    name=('str', 'peak name, optional'),
    dist_to_center=('pd.Series', 'Distance of sequences to the peak center'),
    letterbook_size=('int', 'Size of letter book (A, T, C, F) in the sequence space. Default 4.')
)


class Scope:
    """Simple scope to contain relavent info"""
    def __init__(self, **kwargs):
        if kwargs != {}:
            for key, arg in kwargs.items():
                setattr(self, key, arg)


def _parse_seqs_input(seqs):
    """Convert input seqs to pd.Series or pd.DataFrame if is not"""
    if isinstance(seqs, (list, np.ndarray)):
        return pd.Series(data=seqs, index=seqs)
    elif isinstance(seqs, pd.Series):
        if seqs.index.dtype == 'int':
            # value as seq
            return pd.Series(data=seqs.values, index=seqs.values)
        else:
            # if not int, assume its sequence
            return seqs
    return seqs


def _combination(n, k):
    from math import factorial
    return factorial(n) / (factorial(n - k) * factorial(k))


def _get_peak_coverage(dist_to_center, seq_len, letterbook_size, max_radius):
    """Survey the coverage of peak at the different distances, defined on **hamming distance**

    Number of possible sequence with k distance away to the center is
        C(L, k) * (m - 1)^k
    where C(L, k) is the combination operator to select k positions from L candidates, m is the letter book size
        for DNA and RNA m = 4

    Returns:
        a pd.DataFrame table with index as different distance and columns of 'possible seqs',
          'detected seqs', 'coverage'
    """

    def seq_counter(dist):
        return np.sum(dist_to_center == dist)

    def possible_seq(dist):
        return _combination(n=seq_len, k=dist) * (letterbook_size - 1) ** dist

    dist_list = pd.Series(np.arange(max_radius + 1))
    results = pd.DataFrame({
        'possible seqs': dist_list.apply(possible_seq),
        'detected seqs': dist_list.apply(seq_counter)
    }, index=dist_list)
    results['coverage'] = results['detected seqs'] / results['possible seqs']

    return results


def _get_peak_abun(dist_to_center, max_radius, table, use_relative, center, dist_type):
    """report the (relative) abundance and number of unique sequences with different distances

    Returns:
        Two pd.DataFrame instance. First one is (relative) abundance with distance as indices and samples as columns;
          Second is number of unique sequences detected with same layout
    """

    seq_not_in = table.index[~table.index.isin(dist_to_center.index)]
    if len(seq_not_in) > 0:
        dist_to_center = pd.concat([dist_to_center,
                                    _get_distance(list(seq_not_in), center_seq=center, dist_type=dist_type)])
    dist_list = pd.Series(data=np.arange(max_radius + 1), index=np.arange(max_radius + 1))

    def get_abun(dist):
        candidates = dist_to_center[dist_to_center == dist].index.values
        return table.loc[table.index.isin(candidates), :].sum(axis=0)

    def get_uniq_seq(dist):
        candidates = dist_to_center[dist_to_center == dist].index.values
        return (table.loc[table.index.isin(candidates), :] > 0).sum(axis=0)

    peak_abun = dist_list.apply(get_abun)
    peak_uniq_seq = dist_list.apply(get_uniq_seq)

    if use_relative:
        peak_abun = peak_abun.divide(peak_abun.loc[0])

    return peak_abun, peak_uniq_seq


def _get_distance(seqs, center_seq, dist_type):
    """Update self.dist_to_center with current self.center_seq, self.seqs, and dist_type"""
    from functools import partial

    seqs = _parse_seqs_input(seqs)

    if dist_type == 'hamming':
        logging.info('Calculating distance of seqs to center using hamming distance...')
        dist_to_center = seqs.index.to_series().map(partial(_hamming_dist_to_center, center_seq=center_seq))
    else:
        logging.info('Calculating distance of seqs to center using edit distance...')
        dist_to_center = seqs.index.to_series().map(partial(_edit_dist_to_center, center_seq=center_seq))
    logging.info('  Finished')
    return dist_to_center


def _edit_dist_to_center(seq, center_seq):
    """Get the edit (Levenshtein) distance to center sequence"""
    if isinstance(seq, pd.Series):
        seq = seq.name
    return Distance.distance(center_seq, seq)


def _hamming_dist_to_center(seq, center_seq):
    """Get the hamming distance to the center sequence"""
    if isinstance(seq, pd.Series):
        seq = seq.name
    return Distance.hamming(seq, center_seq)


@peak_doc.compose("""A sequence peak defined on sequence space with edit (Levenshtein) or hamming distance
    - edit (Levenshtein) distance: including insertions and deletions
    - hamming distance: only consider mutations

Attributes:
<<seqs, center_seq, radius, name, dist_type, dist_to_center, letterbook_size>>

Methods:

""")
class Peak(object):

    @peak_doc.compose("""Initialize a Peak
Args:
<<center_seq, seqs, radius, dist_type, letterbook_size>>
""")
    def __init__(self, center_seq, seqs, name=None, radius=None, dist_type='edit',
                 letterbook_size=4):

        self.seqs = _parse_seqs_input(seqs)
        self.center_seq = center_seq
        self.radius = radius
        self.name = name
        if dist_type.lower() not in ['edit', 'levenshtein', 'hamming']:
            logging.error("dist_type should be 'hamming' or 'edit' ('levenshtein')")
            raise ValueError("dist_type should be 'hamming' or 'edit' ('levenshtein')")
        self.dist_type = dist_type.lower()
        self.dist_to_center = None
        self.letterbook_size = letterbook_size
        self.update_distance()

        from .visualization import peak_plot
        from functools import partial

        self.vis = Scope(peak_plot=partial(peak_plot, peak=self))
        self.vis.peak_plot.__doc__ = peak_plot.__doc__

    def update_distance(self):
        self.dist_to_center = _get_distance(seqs=self.seqs, center_seq=self.center_seq, dist_type=self.dist_type)

    @peak_doc.compose(f"""{_get_peak_coverage.__doc__}

Args:
    max_radius (int): maximum distance to survey, if None, will use self.radius
""")
    def peak_coverage(self, max_radius=None):

        if self.dist_to_center is None:
            # calculate distance if haven't
            self.update_distance()

        return _get_peak_coverage(dist_to_center=self.dist_to_center,
                                  seq_len=len(self.center_seq),
                                  letterbook_size=self.letterbook_size,
                                  max_radius=self.radius if max_radius is None else max_radius)

    @peak_doc.compose(f"""{_get_peak_abun.__doc__}

Args:
    max_radius (int): maximum distance to survey, if None, will use self.radius
    table (pd.DataFrame): table of abundance measures with sequences as indices and sample names as columns,
          if None, try to use self.seqs if it is a pd.DataFrame
    use_relative (bool): if True, abundance will be normalized to the center
""")
    def peak_abun(self, max_radius=None, table=None, use_relative=True):

        if self.dist_to_center is None:
            self.update_distance()

        if table is None:
            if isinstance(self.seqs, pd.DataFrame):
                table = self.seqs
            else:
                logging.error('Please indicate abundance table for calculation')
                raise ValueError('Please indicate abundance table for calculation')

        return _get_peak_abun(dist_to_center=self.dist_to_center,
                              max_radius=self.radius if max_radius is None else max_radius,
                              table=table,
                              use_relative=use_relative,
                              center=self.center_seq,
                              dist_type=self.dist_type)


class PeakCollection:
    # TODO: Add validation of input types. e.g. same edit_dist, same center length

    def __init__(self, peaks):
        if isinstance(peaks, list) and isinstance(peaks[0], Peak):
            # list of pre computed peak
            self.peaks = peaks
            self.name = f"Merged peak ({','.join([peak.name for peak in peaks])})"
            self.center_seq = {peak.name: peak.center_seq for peak in peaks}
            self.dist_to_center = pd.DataFrame({peak.name: peak.dist_to_center for peak in peaks}).min(axis=1)
            self.peak_num = len(peaks)
            self.dist_type = peaks[0].dist_type
        else:
            logging.error('Peaks needs to be a list of Peak instances')
            raise ValueError('Peaks needs to be a list of Peak instances')

    def peak_coverage(self, max_radius):
        results = _get_peak_coverage(dist_to_center=self.dist_to_center,
                                     seq_len=len(self.peaks[0].center_seq),
                                     letterbook_size=self.peaks[0].letterbook_size,
                                     max_radius=max_radius)
        results['possible seqs'] = results['possible seqs'] * self.peak_num
        results['coverage'] = results['coverage'] / self.peak_num
        return results

    def peak_abun(self, max_radius, table, use_relative=True):

        return _get_peak_abun(dist_to_center=self.dist_to_center,
                              max_radius=max_radius,
                              table=table,
                              use_relative=use_relative,
                              center=self.center_seq,
                              dist_type=self.dist_type)
