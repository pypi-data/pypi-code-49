"""
    The brain of IR algorithms. This module are resposible to execute one model and return the resulted
    scored document list.
"""
from typing import List

from matchup.structure.Solution import Result
from matchup.structure.weighting.Idf import InverseFrequency
from matchup.structure.weighting.Tf import LogNormalization

from matchup.models.Model import ModelType
from matchup.models.algorithms.Boolean import Boolean
from matchup.models.algorithms.Vector import Vector
from matchup.models.algorithms.Probabilistic import Probabilistic
from matchup.models.algorithms.ExtendedBoolean import ExtendedBoolean

from matchup.presentation.Text import Term


class NoSuchInputException(RuntimeError):
    pass


class NoSuchModelException(RuntimeError):
    pass


class ModelMissingParameters(RuntimeError):
    pass


class Orchestrator:

    def __init__(self, vocabulary):
        self._vocabulary = vocabulary
        self._input = List[Term]

    def search(self, model: ModelType = None, idf=None, tf=None, **kwargs) -> List[Result]:
        """
            Core function. Execute one IR model based in vocabulary and input(query)
        :param model: IR model to execute
        :param idf: IDF class to weighting IR model
        :param tf: TF class to weighting IR model
        :return: list of solution -> (document, score)
        """

        # setting algorithms IDF weighting
        self._vocabulary.tf = tf if tf is not None else LogNormalization()
        self._vocabulary.idf = idf if idf is not None else InverseFrequency()

        model = model if model else ModelType.Vector

        if self._input:
            if model == ModelType.Boolean:
                return self.run_boolean()
            elif model == ModelType.Vector:
                return self.run_vector_space()
            elif model == ModelType.Probabilistic:
                return self.run_probabilistic()
            elif model == ModelType.ExtendedBoolean:
                return self.run_extended_boolean(**kwargs)
            else:
                raise NoSuchModelException("No model algorithm found. Try again!")
        else:
            raise NoSuchInputException("You should to put some search. Try again!")

    @property
    def entry(self) -> List[Term]:
        """
            Property getter entry(user input)
        :return: user input
        """
        return self._input

    @entry.setter
    def entry(self, etr: List[Term]) -> None:
        """
            Setter attribute input.
        :param etr: input terms
        :return: None
        """
        self._input = etr

    def run_boolean(self):
        return Boolean.run(self._input, self._vocabulary)

    def run_vector_space(self):
        return Vector.run(self._input, self._vocabulary)

    def run_probabilistic(self):
        return Probabilistic.run(self._input, self._vocabulary)

    def run_extended_boolean(self, **kwargs):
        P = kwargs.get("P")
        if P:
            ExtendedBoolean.P = float(P)
            return ExtendedBoolean.run(self._input, self._vocabulary)
        else:
            raise ModelMissingParameters("Missing parameter P for Extended Boolean Model")