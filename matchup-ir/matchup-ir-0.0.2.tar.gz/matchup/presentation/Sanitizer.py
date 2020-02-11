"""
    Module responsible to configure the document representation.
"""

import re
import unicodedata

from typing import List, Set

from matchup.presentation.Text import Term, Line


class Sanitizer:
    def __init__(self, *, stopwords_path: str):
        self._stopwords_path = stopwords_path
        self._stopwords = self.import_stopwords()

    def import_stopwords(self) -> Set[str]:
        """
            Retrieve stopwords from memory
        :return: set of stopwords
        """
        with open(self._stopwords_path, encoding='utf-8') as file:
            self._stopwords = {line.strip() for line in file}
        return self._stopwords

    @staticmethod
    def _remove_special_chars_lower(word: str) -> str:
        """
            Given an word, this function clean this string, removing the special chars
        :param word: string to be sanitized
        :return:
        """
        return re.sub('[^a-zA-Z0-9\n]', '', word).lower()

    @staticmethod
    def index_line(words: List[str], base_line: Line) -> List[Term]:
        """
            This function index one line, clean all words and returning all words sanitized
            The list must be sorted by occurrence in text!
        :param words: base-line stripped and without stopwords
        :param base_line: line to be sanitized
        :return: list of indexed words : list(Term)
        """

        # importante para o find funcionar
        base_line_stripped = Sanitizer.strip_accents(base_line.content)

        indexed_words = []

        acc_value = 0
        for word in words:

            word_position = base_line_stripped[acc_value::].find(word)
            acc_value += word_position

            position = str(base_line.number) + "-" + str(acc_value)

            word_sanitized = Sanitizer._remove_special_chars_lower(word)

            if word_sanitized:
                # salvo a palavra minúscula e a posição de ocorrência dentro da linha
                indexed_words.append(Term(word_sanitized, position))

        return indexed_words

    def sanitize_line(self, line: str, number_line: int) -> List[Term]:
        """
            This function sanitize one line. The number is basically for presentation
        :param line: Complete line to be processed
        :param number_line: number of line
        :return:
        """
        base_line = Line(line, number_line)

        line_cleaned = base_line.content.strip()
        line_cleaned = self.strip_accents(line_cleaned)

        words = line_cleaned.split()
        filtered = filter(lambda word: word.lower() not in self._stopwords, words)  # remove stopwords
        # dado a lista de palavras filtradas e a linha original : retorna um indexador de termos
        indexed = Sanitizer.index_line(list(filtered), base_line)
        return indexed  # lista de termos

    @property
    def stopwords_path(self) -> str:
        """
            Property that get the stopwords file path
        :return: Complete stopwords file path
        """
        return self._stopwords_path

    @stopwords_path.setter
    def stopwords_path(self, stopwordspath: str) -> None:
        """
            Property setter stopwords path
        :param stopwordspath: New stopwords path
        :return: None
        """
        self._stopwords_path = stopwordspath

    @staticmethod
    def strip_accents(text: str) -> str:
        """
            Strip accents of one text
        :param text: old text
        :return: text sanitized
        """
        text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
        return str(text)

