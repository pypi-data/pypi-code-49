from collections import defaultdict, Counter, namedtuple

from Bio import SeqIO
from Bio.Alphabet import generic_dna
import numpy as np

VERSION = 0.1

HXB2_LOS_ALAMOS_ID = 'B.FR.83.HXB2_LAI_IIIB_BRU.K03455'


def parse_breakpoints(bp_files):
    """
    Parses jpHMM-compatible breakpoint file(s) (such as recombination.txt) into a dictionary.
    The file should have the following format:

    =====================
    # optional-comment
    # ...
    # optional-comment

    >sequence_id_1 optional-text-to-be-ignored
    start_position_1_1	end_position_1_1	subtype_1_1
    ...
    start_position_1_n1	end_position_1_n1	subtype_1_n1

    >sequence_id_2 optional-text-to-be-ignored
    start_position_2_1	end_position_2_1	subtype_2_1/subtype_2_2
    ...
    =====================

    The start and end breakpoint positions are inclusive, and 1-based.
    The start-end intervals should cover all the sequence,
    therefore start_position_i_1 is always 1 and end_position_i_ni is the length of the sequence i.
    If subtype_i_k is the same ad subtype_i_l then this subtype appears several times in this sequence
    (including intervals k and l).
    If several subtypes are specified for an interval, e.g. subtype_i_k/subtype_i_l,
    it means that any of them could correspond to this interval.


    :param bp_files: path to jpHMM-compatible breakpoint file(s) (such as recombination.txt)
    :type bp_files: list(str) or str
    :return: mapping between sequences ids and a mapping of subtypes to breakpoint interval list:
        {id: {subtype: [(start, stop), ...], ...}, ..}
    :rtype: dict
    """
    id2subtype2interval = {}
    if isinstance(bp_files, str):
        bp_files = [bp_files]
    for bp_file in bp_files:
        with open(bp_file, 'r') as f:
            name = None
            for line in f:
                line = line.strip('\n').strip()
                if not line or line.startswith('#'):
                    continue
                if line.startswith('>'):
                    if name:
                        id2subtype2interval[name] = subtype2interval
                    name = line.split(' ')[0].strip()[1:]
                    subtype2interval = defaultdict(list)
                else:
                    start, stop, subtypes = line.split('\t')
                    for subtype in subtypes.split('/'):
                        subtype2interval[subtype].append((int(start), int(stop)))
            if name:
                id2subtype2interval[name] = subtype2interval
    return id2subtype2interval


def breakpoints2bitmasks(id2subtype2interval, generalise_subtypes=True):
    """
    Converts breakpoint dictionary to a bitmask dictionary,
    with each subtype represented by a boolean array where True correspond to the subtype interval positions.
    For example, the following breakpoints
    >CRF
    1	3	A
    4	5	B
    correspond to the following bitmasks:
    A 1 1 1 0 0
    B 0 0 0 1 1

    :param id2subtype2interval: mapping between sequences ids and a mapping of subtypes to breakpoint interval list:
        {id: {subtype: [(start, stop), ...], ...}, ..}
    :type id2subtype2interval: dict
    :param generalise_subtypes: if True the more specific subtypes (e.g. A1, A2)
        will be replaced by more generic ones (e.g. A).
    :type generalise_subtypes: bool
    :return: mapping between sequences ids and a mapping of subtypes to bitmasks (represented as boolean numpy arrays):
        {id: {subtype: bitmask, ...}, ..}
    :rtype: dict
    """

    id2st2bitmask = {}
    for name, subtype2intervals in id2subtype2interval.items():
        subtype2bitmask = defaultdict(lambda: np.zeros(max(max(stop for (start, stop) in intervals)
                                                           for intervals in subtype2intervals.values()), dtype=bool))
        for subtype, intervals in subtype2intervals.items():
            if generalise_subtypes and len(subtype) == 2 and subtype[1].isdigit() and subtype[0].isalpha():
                subtype = subtype[0]
            for (start, stop) in intervals:
                subtype2bitmask[subtype][start - 1: stop] = 1
        id2st2bitmask[name] = subtype2bitmask
    return id2st2bitmask


def expand_crfs(id2subtype2bitmask, crf2st2bitmask):
    """
    Replaces CRFs bitmasks with their corresponding primary subtype bitmasks.

    For example if a CRF corresponds to the following recombination:
    >CRF
    1	3	A
    4	5	B
    and a sequence has the following bitmask mapping:
    A   1 0 0 0 0
    C   0 0 0 0 1
    CRF 0 1 1 1 0
    the replacement will transform it to:
    A   1 1 1 0 0
    B   0 0 0 1 0
    C   0 0 0 0 1


    :param id2subtype2bitmask: mapping between sequences ids and a mapping of subtypes to bitmasks
        (represented as boolean numpy arrays): {id: {subtype: bitmask, ...}, ..}
    :type id2subtype2bitmask: dict
    :param crf2st2bitmask: mapping between CRF ids and a mapping of subtypes to bitmasks
        (represented as boolean numpy arrays): {id: {subtype: bitmask, ...}, ..}
    :return: crf2st2bitmask: dict
    """
    for name, st2bm in id2subtype2bitmask.items():
        crfs = [_ for _ in st2bm.keys() if _.startswith('CRF')]
        while crfs:
            for crf in crfs:
                bm = st2bm[crf]
                for st, bitmask in crf2st2bitmask[crf].items():
                    intersection = bitmask & bm
                    if np.any(intersection):
                        st2bm[st] |= intersection
                del st2bm[crf]
            crfs = [_ for _ in st2bm.keys() if _.startswith('CRF')]


def get_reference_coordinates(aln_file, reference_id=HXB2_LOS_ALAMOS_ID):
    """
    Finds the coordinates (0-based) of reference sequence in the aligned file,
    e.g. if the reference sequence is AACCGT and it is aligned as --AA-CC-G-T-,
    its positions are [2, 3, 5, 6, 8, 10].
    Also returns the length of the initial sequence (n) and of the alignment (n_gappy).

    :param aln_file: path to the alignment file in fasta format.
    :type aln_file: str
    :param reference_id: id of the reference sequence in the alignment
    :type reference_id: str
    :return: Coordinates object with the filed coordinates containing the coordinates,
        n containing the reference sequence length (without gaps), and n_gappy containing the alignment length.
    :rtype: collections.namedtuple
    """
    ref = None
    for rec in SeqIO.parse(aln_file, 'fasta', alphabet=generic_dna):
        if reference_id == rec.id:
            ref = rec
            break

    gappy_seq = str(ref.seq)
    n_gappy = len(gappy_seq)
    n = len(gappy_seq.replace('-', ''))
    position_shift = [i for (i, c) in enumerate(gappy_seq) if c != '-']
    Coordinates = namedtuple('Coordinates', ['coordinates', 'n', 'n_gappy'])
    return Coordinates(coordinates=position_shift, n=n, n_gappy=n_gappy)


def parse_aligned_coordinates(jphmm_msas):
    """
    Parses the jpHMM alignment file(s) (alignment_to_msa.txt), into a dictionary containing a mapping of sequence ids to
    the coordinates (0-based) of them aligned,
    e.g. if the reference seq1 sequence is AACCGT and the alignment_to_msa.txt contains:
    >seq1
    3 4 6 7 9 11
    it means that it should be aligned as --AA-CC-G-T... (where ... contains as many gaps as the alignment length requires),
    and its parsed (0-based) positions are [2, 3, 5, 6, 8, 10].

    :param jphmm_msas: path to jpHMM-produced alignment file(s) (such as alignment_to_msa.txt)
    :type jphmm_msas: list(str) or str
    :return: sequence id to coordinate list mapping
    :rtype: dict
    """
    id2pos = {}
    if isinstance(jphmm_msas, str):
        jphmm_msas = [jphmm_msas]
    for in_msa in jphmm_msas:
        with open(in_msa, 'r') as f:
            id = None
            for line in f.readlines():
                line = line.strip('\n').strip()
                if line.startswith('#') or not line:
                    continue
                if line.startswith('>'):
                    id = line[1:].strip()
                    continue
                id2pos[id] = [(int(_) - 1) for _ in line.split(' ')]
    return id2pos


def shift_bitmask(id2subtype2bitmask, id2coordinates, n_gappy, gap_fill=1):
    """
    Realignes the bitmasks in a mapping according to specified coordinates
    (e.g. adds gaps to the bitmasks filled according to gap_fill parameter, either with 1s or 0s).

    For example, a sequence with a bitmask
    A   1 1 1 0 0
    B   0 0 0 1 1
    and the following (0-based) coordinates in the alignment of length (n_gappy) 10:
    2 3 4 7 8
    will get the realigned bitmask of (gaps filled with 0s):
    A   0 0 1 1 1 0 0 0 0 0
    B   0 0 0 0 0 0 0 1 1 0


    :param id2subtype2bitmask: mapping between sequences ids and a mapping of subtypes to bitmasks
        (represented as boolean numpy arrays): {id: {subtype: bitmask, ...}, ..}
    :type id2subtype2bitmask: dict
    :param id2coordinates: sequence id to its coordinate list (positions in the alignment) mapping
    :type id2coordinates: dict
    :param n_gappy: length of the alignment
    :type n_gappy: int
    :param gap_fill: what to fill the gaps in the aligned bitmasks with: 0 or 1
    :type gap_fill: int (0 or 1)
    :return: mapping between sequences ids and insertion lengths
        (specified by the number of coordinates equal to -1 (5'-Insertion) and n_gappy (3'-Insertion)),
        plus modifies the input bitmask mapping
    :rtype: dict
    """
    id2insertion_length = Counter()
    for name, subtype2bitmask in id2subtype2bitmask.items():
        shifted_positions = id2coordinates[name]
        insertion_start = 0
        for _ in shifted_positions:
            if -1 == _:
                insertion_start += 1
            else:
                break
        insertion_end = 0
        for _ in reversed(shifted_positions):
            if n_gappy == _:
                insertion_end += 1
            else:
                break
        id2insertion_length[name] += insertion_end + insertion_start
        shifted_positions = shifted_positions[insertion_start: len(shifted_positions) - insertion_end]
        for st, bitmask in list(subtype2bitmask.items()):
            gappy_bitmask = np.ones(n_gappy, dtype=bool) if gap_fill else np.zeros(n_gappy, dtype=bool)
            gappy_bitmask[shifted_positions] = bitmask[insertion_start: len(bitmask) - insertion_end]
            if not np.any(gappy_bitmask):
                del subtype2bitmask[st]
            else:
                subtype2bitmask[st] = gappy_bitmask
    return id2insertion_length


def save_bitmask(id2st2bitmask, out_file):
    """
    Saves a bitmask mapping to a file, in the following format:

    ========================
    >>sequence_id_1
    subtype_1	pos_1_1 pos_1_2 ... pos_1_n
    ...
    subtype_m	pos_m_1 pos_m_2 ... pos_m_n

    >>sequence_id_2
    ...
    ========================
    where pos_i_j is 1 if subtype_i is detected at the position j and 0 otherwise. All-zero masks are omitted.

    :param id2subtype2bitmask: mapping between sequences ids and a mapping of subtypes to bitmasks
        (represented as boolean numpy arrays): {id: {subtype: bitmask, ...}, ..}
    :type id2subtype2bitmask: dict
    :param out_file: path to the file where the bitmask should be saved.
    :type out_file: str
    """
    with open(out_file, 'w+') as f:
        for name in sorted(id2st2bitmask.keys()):
            f.write('>>{}\n'.format(name))
            subtype2bitmask = id2st2bitmask[name]
            for st in sorted(subtype2bitmask.keys()):
                f.write('{}\t{}\n'.format(st, ' '.join(str(int(_)) for _ in subtype2bitmask[st])))


def parse_bitmask(bp_file):
    """
    Reads a bitmask mapping from a file to a dictionary. The file should be in the following format:

    ========================
    >>sequence_id_1
    subtype_1	pos_1_1 pos_1_2 ... pos_1_n
    ...
    subtype_m	pos_m_1 pos_m_2 ... pos_m_n

    >>sequence_id_2
    ...
    ========================
    where pos_i_j is 1 if subtype_i is detected at the position j and 0 otherwise. All-zero masks are omitted.

    :param bp_file: path to the file where the bitmask mapping is stored.
    :type bp_file: str
    :return: mapping between sequences ids and a mapping of subtypes to bitmasks
        (represented as boolean numpy arrays): {id: {subtype: bitmask, ...}, ..}
    :rtype: dict
    """
    id2st2bitmask = {}
    with open(bp_file, 'r') as f:
        name = None
        for line in f:
            line = line.strip('\n').strip()
            if not line:
                continue
            if line.startswith('>>'):
                if name:
                    id2st2bitmask[name] = st2bps
                name = line[2:]
                st2bps = {}
            else:
                st, mask = line.split('\t')
                st2bps[st] = np.array([bool(int(_)) for _ in mask.split(' ')])
        if name:
            id2st2bitmask[name] = st2bps
    return id2st2bitmask

