"""
    First abstraction that represents IR models
        Model, IterModel
"""

import abc

from enum import Enum
from typing import List
from collections import defaultdict

from matchup.structure.Solution import Result
from matchup.structure.Vocabulary import Vocabulary
from matchup.presentation.Text import Term


class ModelType(Enum):
    Boolean = 1,
    Vector = 2,
    Probabilistic = 3,
    ExtendedBoolean = 4

    @classmethod
    def get_type(cls, value: str) -> "ModelType":
        if value.lower() == 'boolean':
            return cls.Boolean
        elif value.lower() == 'vector':
            return cls.Vector
        elif value.lower() == 'probabilistic':
            return cls.Probabilistic
        elif value.lower() == 'extendedboolean':
            return cls.ExtendedBoolean


class NoSuchModelException(RuntimeError):
    pass


class ModelExecutionError(RuntimeError):
    pass


class Model(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def run(query: List[Term], vocabulary: Vocabulary):
        """
            Define the principal method of IR models.
        :param query: List of all entry terms
        :param vocabulary: Vocabulary pre-processed
        :return:
        """
        ...

    @staticmethod
    def cast_solution(structure: List[tuple]) -> List[Result]:
        return [Result(item[0], round(item[1], 3)) for item in structure]


"""
    Describe one variation of Model classes : IterModel classes have some funcionalities for help his works
    Pointers and occurrences are implemented here.
"""


class IterModel(Model):

    _term_occurrences = defaultdict(list)
    _pointers = defaultdict(int)

    @staticmethod
    @abc.abstractmethod
    def run(query: List[Term], vocabulary: Vocabulary):
        """
            Define the principal method of IR models.
        :param query: List of all entry terms
        :param vocabulary: Vocabulary pre-processed
        :return:
        """
        ...

    @staticmethod
    def initialize_occurrences(query: List[Term], vocabulary: Vocabulary) -> None:
        """
            Create another data structure _term_occurrences that represents the vocabulary wiith just query
            keywords.
        :param query: original query
        :param vocabulary: original vocabulary
        :return: None
        """
        for key in query:
            if key.word in vocabulary:
                IterModel._term_occurrences[key.word] = vocabulary[key.word]

    @staticmethod
    def initialize_pointers() -> None:
        """
            Initialize pointers to model algorithm
        :return: None
        """
        for query_term in IterModel._term_occurrences.keys():
            IterModel._pointers[query_term] = 0

    @classmethod
    def lowest_doc(cls) -> str:
        """
            Return the lowest doc pointer by pointers
        :return: lowest document
        """
        # print("candidates : ", end='')
        lowest = None
        for key in cls._term_occurrences.keys():
            try:
                doc = cls._term_occurrences[key][cls._pointers[key]].doc()
                # print(doc + " ", end='')
                if lowest and doc < lowest:
                    lowest = doc
                elif not lowest:
                    lowest = doc
            except ValueError:
                continue
            except IndexError:
                continue
        # print(".")
        return lowest
