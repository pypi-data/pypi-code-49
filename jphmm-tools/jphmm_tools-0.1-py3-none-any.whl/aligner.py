import numpy as np
from Bio import SeqIO
from Bio.Alphabet import generic_dna

from jphmm_tools.__init__ import parse_aligned_coordinates, VERSION


def align(jphmm_msas, in_fas, out_aln, aln_len):
    """
    Aligns input sequences according to the jpHMM (http://jphmm.gobics.de) output.

    :param jphmm_msas: path(s) to jpHMM-produced alignment file(s) (such as alignment_to_msa.txt)
    :type jphmm_msas: list(str) or str
    :param in_fas: path(s) to fasta file(s) containing sequences to be aligned
    :type in_fas: str
    :param out_aln: path where to save the output alignment file (in fasta format)
    :type out_aln: str
    :param aln_len: length of the alignment
    :type aln_len: int
    """

    id2pos = parse_aligned_coordinates(jphmm_msas)

    with open(out_aln, 'w') as f:
        if isinstance(in_fas, str):
            in_fas = [in_fas]
        for in_fa in in_fas:
            for rec in SeqIO.parse(in_fa, 'fasta', alphabet=generic_dna):
                positions = id2pos[rec.id]
                if positions:
                    aligned_seq = np.array(['-'] * aln_len)
                    seq = list(str(rec.seq))
                    insertion_beginning = sum(1 for _ in positions if _ == -1)
                    insertion_end = sum(1 for _ in positions if _ == aln_len)
                    aligned_seq[positions[insertion_beginning: (len(positions) - insertion_end)]] \
                        = seq[insertion_beginning: (len(seq) - insertion_end)]
                    f.write('>{}\n{}\n'.format(rec.id, ''.join(aligned_seq)))


def main():
    """
    Entry point, calling :py:func:`jphmm_tools.aligner.align` with command-line arguments.

    :return: void
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Aligns input sequences according to the jpHMM (http://jphmm.gobics.de) output.",
        prog='jphmm_align')

    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=VERSION))

    parser.add_argument('--jphmm_msas', nargs='+', type=str,
                        help="Path(s) to jpHMM-produced alignment file(s) (such as alignment_to_msa.txt).")
    parser.add_argument('--in_fas', nargs='+', type=str,
                        help="Path(s) to fasta file(s) containing sequences to be aligned.")
    parser.add_argument('--out_aln', required=True, type=str,
                        help="Path where to save the output alignment file (in fasta format).")
    parser.add_argument('--aln_len', required=True, type=int,
                        help="Length of the alignment.")

    params = parser.parse_args()

    align(**vars(params))


if '__main__' == __name__:
    main()
