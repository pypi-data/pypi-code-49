from lhc.binf.align.aligner import Aligner, Mode, DEFAULT_NUCLEOTIDE_ALPHABET, DEFAULT_NUCLEOTIDE_SCORING_MATRIX
from lhc.binf.align.score import BLOSUM62, BLOSUM_ALPHABET, EDNA_ALPHABET, EDNA_SCORING_MATRIX


def align(sequence1: str, sequence2: str, mode=Mode.GLOBAL):
    return Aligner(mode, DEFAULT_NUCLEOTIDE_SCORING_MATRIX, DEFAULT_NUCLEOTIDE_ALPHABET)\
        .align(sequence1, sequence2)
