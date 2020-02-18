"""
Base class for parsing states
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from abc import abstractmethod

from .parse_context import ParseContext


class ParsingState:
    """Parsing state
    """
    _whitespace_chars = [' ', '\t']
    _quote_chars = ['\'', '"']

    def __init__(self, context: ParseContext):
        self._context = context

    def parse_and_get_next_state(self, current_char):
        """
        :param current_char: parsed character
        :return: next state
        """
        self._on_new_char(current_char)
        if self.__is_known_char(current_char):
            return self.__get_known_next_step(current_char)
        return self.__get_real_default_step()

    def get_vector(self):
        """
        :return: collected vector
        """
        return self._context.get_vector()

    def __str__(self):
        return f'State is {self.__class__.__name__}'

    def _on_new_char(self, char):
        self._context.last_char = char

    @abstractmethod
    def _get_default_next_state(self):
        """
        :return: either a state-class type, which will be used to create the default next step
         (if no char in the below dict is matched), or None which means the current state remains
          in effect
        """

    @abstractmethod
    def _get_dict_of_chars_to_new_states(self):
        """
        :return: dict where the values are wither a state-class type, which will be used to create
         the next step is that key is matched, or None which means the current state will remain in
          effect
        """

    def __is_known_char(self, char):
        return char in self._get_dict_of_chars_to_new_states().keys()

    def __get_known_next_step(self, char):
        next_state = self._get_dict_of_chars_to_new_states()[char]
        return self.__get_real_next_step(next_state)

    def __get_real_default_step(self):
        next_state = self._get_default_next_state()
        return self.__get_real_next_step(next_state)

    def __get_real_next_step(self, next_step):
        return next_step(self._context) if next_step else self
