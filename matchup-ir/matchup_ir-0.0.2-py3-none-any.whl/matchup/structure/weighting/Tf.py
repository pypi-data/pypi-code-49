from abc import ABC
from math import log
from collections import defaultdict


class TFFactory:
    @staticmethod
    def create_tf_by_str(value: str) -> "IDF":
        if value.lower() == 'binary':
            return Binary()
        elif value.lower() == 'termfrequency':
            return TermFrequency()
        elif value.lower() == 'lognormalization':
            return LogNormalization()


class TF(ABC):

    def __init__(self):
        self._tfs = defaultdict(float)

    def __repr__(self):
        string = ""
        for key in self._tfs:
            string += f"{key} : {self._tfs[key]}\n"
        return string

    def take(self, *,  value: int = 0, reverse: bool = True):
        if value != 0:
            return sorted(self._tfs.items(), key=lambda v: v[1], reverse=reverse)[:value]
        return sorted(self._tfs.items(), key=lambda v: v[1], reverse=reverse)

    def calculate(self, keyword: str, occurrence, vocabulary) -> float:
        """
           Generate TF based in TFType
        :return:float tf
        """
        ...

    @classmethod
    def _fij(cls, occurrence, vocabulary):
        if cls != LogNormalization:
            value = occurrence.frequency / (vocabulary.max_frequency_map[occurrence.doc()])
        else:
            value = occurrence.frequency
        return value

    def _persist(self, key, tf) -> float:
        self._tfs[key] = tf
        return tf


class Binary(TF):

    def __init__(self):
        super(Binary, self).__init__()

    def calculate(self, keyword: str, occurrence, vocabulary):
        """
            Model to calculate TF based in binary values (0,1)
        :return: float tf
        """
        fij = self._fij(occurrence, vocabulary)

        if fij > 0:
            return self._persist((keyword, occurrence.doc()), 1.0)
        else:
            return self._persist((keyword, occurrence.doc()), 0.0)


class TermFrequency(TF):

    def __init__(self):
        super(TermFrequency, self).__init__()

    def calculate(self, keyword: str, occurrence, vocabulary) -> float:
        """
            Model to calculate TF based in fij
        :return: float fij
        """
        fij = self._fij(occurrence, vocabulary)

        return self._persist((keyword, occurrence.doc()), float(fij))


class LogNormalization(TF):

    def __init__(self):
        super(LogNormalization, self).__init__()

    def calculate(self, keyword: str, occurrence, vocabulary) -> float:
        """
            Model to calculate TF based in : 1 + log fij
        :return: float fij
        """
        fij = self._fij(occurrence, vocabulary)
        tf = 1 + log(fij, 2)

        return self._persist((keyword, occurrence.doc()), tf)

