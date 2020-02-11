"""
    Represents the Query of the IR service, composite for :
        sanitizer, orquestrator and answer
"""

from matchup.presentation.Sanitizer import Sanitizer
from matchup.models.Orchestrator import Orchestrator, ModelType
from matchup.structure.Solution import Solution


class NoSuchAnswerException(RuntimeError):
    pass


class Query:
    def __init__(self, *, vocabulary):
        self._sanitizer = Sanitizer(stopwords_path=vocabulary.stopwords_path)
        self._orquestrator = Orchestrator(vocabulary)
        self._answer = list()  # List[Term]

    def ask(self, answer: str = None) -> None:
        """
            Make query since a command line prompt.
        :return: None
        """
        if not answer:
            message = "{0}\n{1: >18}".format(25*"= ", "Consulta: ")
            answer = input(message)
            self._answer = self._sanitizer.sanitize_line(answer, 1)
        else:
            number_line = 1
            text = answer.split("\n")
            terms = []
            for line in text:
                terms += self._sanitizer.sanitize_line(line, number_line)  # linha -> [(palavra, posicao)]
                number_line += 1
            self._answer = terms

        self._orquestrator.entry = self._answer

    @property
    def search_input(self):
        return self._answer

    def search(self, *, model: ModelType = None, idf=None, tf=None, **kwargs) -> Solution:
        """
            Receive an IR model and execute the query based in user answer and the vocabulary.
        :param model: ModelType that represents the IR model
        :param idf: Describe the class  of IDF
        :param tf: Describe the class of TF
        :return: list of solution -> (document, score)
        """
        results = self._orquestrator.search(model, idf, tf, **kwargs)
        return Solution(results)
