from abc import ABC
from math import log
from collections import defaultdict


class IDFFactory:
    @staticmethod
    def create_idf_by_str(value: str) -> "IDF":
        if value.lower() == 'unary':
            return Unary()
        elif value.lower() == 'inversefrequency':
            return InverseFrequency()
        elif value.lower() == 'inversefrequencysmooth':
            return InverseFrequencySmooth()
        elif value.lower() == 'inversefrequencymax':
            return InverseFrequencyMax()
        elif value.lower() == 'probabilisticinversefrequency':
            return ProbabilisticInverseFrequency()


class IDF(ABC):

    def __init__(self):
        self._structure = defaultdict(float)

    def __repr__(self):
        string = ""
        for key in self._structure:
            string += f"{key} : {self._structure[key]}\n"
        return string

    def generate(self, vocabulary) -> None:
        """
            Generate the idf for all keywords in a vocabulary
        :param vocabulary: Vocabulary object
        :return: None
        """
        ...

    def take(self, *, value: int = 0, reverse: bool = True):
        """
            Take the first 'value' elements of IDF dict
        :param value:
        :param reverse : asc or desc.
        :return:
        """
        if value != 0:
            return sorted(self._structure.items(), key=lambda v: v[1], reverse=reverse)[:value]
        return sorted(self._structure.items(), key=lambda v: v[1], reverse=reverse)

    def __getitem__(self, item: str) -> float:
        """
            Overload operator [] on idf structure
        :param item: keyword (document)
        :return: float idf value
        """
        return self._structure[item]


class Unary(IDF):

    def __init__(self):
        super(Unary, self).__init__()

    def generate(self, vocabulary):
        """
            Model to calculate IDF based in unary weight (1)
        :param vocabulary: structure to generate IDF
        :return: None
        """
        for key in vocabulary.keys:
            self._structure[key] = 1


class InverseFrequency(IDF):

    def __init__(self):
        super(InverseFrequency, self).__init__()

    def generate(self, vocabulary):
        """
             Model to calculate IDF based in inverse frequency : log N / ni
        :param vocabulary:  structure to generate IDF
        :return: None
        """
        for key in vocabulary.keys:
            self._structure[key] = log(len(vocabulary.file_names) / vocabulary.get_number_docs_by_keyword(key), 10)


class InverseFrequencySmooth(IDF):

    def __init__(self):
        super(InverseFrequencySmooth, self).__init__()

    def generate(self, vocabulary):
        """
            Model to calculate IDF based in inverse frequency smooth : log 1 + N / ni
        :param vocabulary: structure to generate IDF
        :return: None
        """
        for key in vocabulary.keys:
            self._structure[key] = \
                log(1 + (len(vocabulary.file_names) / vocabulary.get_number_docs_by_keyword(key)), 10)


class InverseFrequencyMax(IDF):

    def __init__(self):
        super(InverseFrequencyMax, self).__init__()

    def generate(self, vocabulary):
        """
                Model to calculate IDF based in max inverse frequency  : log 1 + max ni / ni
        :param vocabulary:  structure to generate IDF
        :return: None
        """
        all_number_docs_by_keyword = [vocabulary.get_number_docs_by_keyword(key) for key in vocabulary.keys]
        max_ni = max(all_number_docs_by_keyword)

        for key in vocabulary.keys:
            self._structure[key] = \
                log(1 + (max_ni / vocabulary.get_number_docs_by_keyword(key)), 10)


class ProbabilisticInverseFrequency(IDF):

    def __init__(self):
        super(ProbabilisticInverseFrequency, self).__init__()

    def generate(self, vocabulary) -> None:
        """
            Model to calculate IDF based in probabilistic inverse frequency : log N - ni / ni
        :param vocabulary: structure to generate IDF
        :return: None
        """
        for key in vocabulary.keys:
            self._structure[key] = \
                log((len(vocabulary.file_names) - vocabulary.get_number_docs_by_keyword(key))
                    / vocabulary.get_number_docs_by_keyword(key), 10)

