"""
Machine's states
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from abc import abstractmethod

from .parsing_state import ParsingState


class BetweenArguments(ParsingState):
    """Transitions:
    quote -> start quoted argument
    whitespace -> keep looking
    all other -> start unquoted argument
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, context):
        super().__init__(context)
        self.__transitions_from_chars_to_new_states =\
            self.__make_transitions_from_whitespace_and_quote_chars_to_new_states()

    def _get_default_next_state(self):
        return InAnUnquotedArgument

    def _get_dict_of_chars_to_new_states(self):
        return self.__transitions_from_chars_to_new_states

    def __make_transitions_from_whitespace_and_quote_chars_to_new_states(self):
        transitions_from_chars_to_new_states =\
            self.__make_transitions_from_whitespace_chars_to_same_state()
        transitions_from_chars_to_new_states.update(
            self.__make_transitions_from_quote_chars_to_quoted_arg())
        return transitions_from_chars_to_new_states

    def __make_transitions_from_quote_chars_to_quoted_arg(self):
        return {char: InAQuotedArgument for char in self._quote_chars}

    def __make_transitions_from_whitespace_chars_to_same_state(self):
        return {char: None for char in self._whitespace_chars}


class _InAnArgument(ParsingState):
    """Transitions:
    ending character -> argument ends
    all other -> argument continues
    """
    def __init__(self, context):
        super().__init__(context)
        self._context.flush_current_arg()
        self.__chars_to_new_states =\
            self.__make_transitions_from_non_argument_chars_to_between_arguments_state()

    def _on_new_char(self, char):
        super()._on_new_char(char)
        self._context.append_last_char_to_current_arg()

    def _get_default_next_state(self):
        return None

    def _get_dict_of_chars_to_new_states(self):
        return self.__chars_to_new_states

    def __make_transitions_from_non_argument_chars_to_between_arguments_state(self):
        return {char: BetweenArguments for char in self._get_non_argument_chars()}

    @abstractmethod
    def _get_non_argument_chars(self):
        """
        :return: a list of characters which mark the and of the argument
        """


class InAnUnquotedArgument(_InAnArgument):
    """Don't quote me on that"""
    def __init__(self, context):
        super().__init__(context)
        context.append_last_char_to_current_arg()

    def _get_non_argument_chars(self):
        return self._whitespace_chars


class InAQuotedArgument(_InAnArgument):
    """And you can quote me on that"""
    def __init__(self, context):
        self.__quote_char = [context.last_char]
        super().__init__(context)

    def _get_non_argument_chars(self):
        return self.__quote_char
