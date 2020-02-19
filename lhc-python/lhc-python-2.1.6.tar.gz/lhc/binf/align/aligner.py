import numpy
import sys

from enum import Enum
from lhc.binf.align.alignment import Alignment
from lhc.binf.align.global_alignment import GlobalAlignment
from lhc.binf.align.local_alignment import LocalAlignment
from lhc.binf.align.semiglobal_alignment import SemiGlobalAlignment
from lhc.binf.align.character_map import CharacterMap

DEFAULT_NUCLEOTIDE_ALPHABET = 'ATGCSWRYKMBVHDN_'

DEFAULT_NUCLEOTIDE_SCORING_MATRIX = numpy.array([
    [ 5, -4, -4, -4, -4,  1,  1, -4, -4,  1, -4, -1, -1, -1, -2, -5],
    [-4,  5, -4, -4, -4,  1, -4,  1,  1, -4, -1, -4, -1, -1, -2, -5],
    [-4, -4,  5, -4,  1, -4,  1, -4,  1, -4, -1, -1, -4, -1, -2, -5],
    [-4, -4, -4,  5,  1, -4, -4,  1, -4,  1, -1, -1, -1, -4, -2, -5],
    [-4, -4,  1,  1, -1, -4, -2, -2, -2, -2, -1, -1, -3, -3, -1, -5],
    [ 1,  1, -4, -4, -4, -1, -2, -2, -2, -2, -3, -3, -1, -1, -1, -5],
    [ 1, -4,  1, -4, -2, -2, -1, -4, -2, -2, -3, -1, -3, -1, -1, -5],
    [-4,  1, -4,  1, -2, -2, -4, -1, -2, -2, -1, -3, -1, -3, -1, -5],
    [-4,  1,  1, -4, -2, -2, -2, -2, -1, -4, -1, -3, -3, -1, -1, -5],
    [ 1, -4, -4,  1, -2, -2, -2, -2, -4, -1, -3, -1, -1, -3, -1, -5],
    [-4, -1, -1, -1, -1, -3, -3, -1, -1, -3, -1, -2, -2, -2, -1, -5],
    [-1, -4, -1, -1, -1, -3, -1, -3, -3, -1, -2, -1, -2, -2, -1, -5],
    [-1, -1, -4, -1, -3, -1, -3, -1, -3, -1, -2, -2, -1, -2, -1, -5],
    [-1, -1, -1, -4, -3, -1, -1, -3, -1, -3, -2, -2, -2, -1, -1, -5],
    [-2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -5],
    [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]])


class Mode(Enum):
    LOCAL = 1
    GLOBAL = 2
    SEMI = 3


class Aligner:

    def __init__(
        self,
        mode: Mode,
        scoring_matrix=DEFAULT_NUCLEOTIDE_SCORING_MATRIX,
        alphabet=DEFAULT_NUCLEOTIDE_ALPHABET
    ):
        if scoring_matrix.shape[0] != len(alphabet):
            raise ValueError('Scoring matrix must be square of alphabet length')
        self.mode = mode
        self.scoring_matrix = scoring_matrix
        self.character_map = CharacterMap(alphabet)

    def align(self, sequence1: str, sequence2: str) -> Alignment:
        end = 0 if self.mode == Mode.LOCAL else -sys.maxsize
        scores = [end, 0, 0, 0]

        alignment = SemiGlobalAlignment(sequence1, sequence2) if self.mode == Mode.SEMI else \
            LocalAlignment(sequence1, sequence2) if self.mode == Mode.LOCAL else \
            GlobalAlignment(sequence1, sequence2)
        s1 = self.character_map.translate(sequence1)
        s2 = self.character_map.translate(sequence2)
        gap = self.character_map.translate('_')[0]
        for i, ci in enumerate(s1):
            for j, cj in enumerate(s2):
                scores[Alignment.DIAG] = alignment.scores[i - 1, j - 1] + self.scoring_matrix[ci, cj]
                scores[Alignment.LEFT] = alignment.scores[i, j - 1] + self.scoring_matrix[gap, cj]
                scores[Alignment.UP] = alignment.scores[i - 1, j] + self.scoring_matrix[ci, gap]
                idx = scores.index(max(scores))
                alignment.set_entry(i, j, scores[idx], idx)
        return alignment
