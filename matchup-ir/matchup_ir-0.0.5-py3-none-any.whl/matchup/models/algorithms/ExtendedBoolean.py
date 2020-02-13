from math import pow

from typing import List
from collections import defaultdict

from matchup.presentation.Text import Term
from matchup.models.Model import IterModel
from matchup.structure.Vocabulary import Vocabulary

from matchup.models.algorithms.Vector import Vector


class ExtendedBoolean(IterModel):

    P = 0.0

    @staticmethod
    def run(query: List[Term], vocabulary: Vocabulary):
        IterModel.initialize_occurrences(query, vocabulary)
        IterModel.initialize_pointers()

        IterModel._term_occurrences = Vector.process_documents(query, vocabulary)

        scores = defaultdict(float)

        while not Vector.stop():
            doc = IterModel.lowest_doc()
            doc_repr = Vector.process_doc(doc)
            scores[doc] = ExtendedBoolean.generate_scores(doc_repr, len(query))

        scores = sorted(scores.items(), key=lambda v: v[1], reverse=True)
        return IterModel.cast_solution(scores)

    @classmethod
    def generate_scores(cls, doc_repr, m) -> float:
        score = 0.0
        for key in doc_repr:
            score += pow((1 - doc_repr[key]), cls.P)

        compensation = m - len(doc_repr)
        if compensation:
            score += compensation

        score /= m
        score = pow(score, 1/cls.P)
        return 1.0 - score






