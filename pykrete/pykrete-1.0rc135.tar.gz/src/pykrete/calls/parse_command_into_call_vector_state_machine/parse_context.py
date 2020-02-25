"""
Running parse context
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""


class ParseContext:
    """keeper of the bridge..."""
    def __init__(self):
        self.last_char = None
        self.__vector = []
        self.__current_arg = []

    def append_last_char_to_current_arg(self):
        """another char in the wall"""
        self.__current_arg.append(self.last_char)

    def flush_current_arg(self):
        """prep for next arg"""
        self._flush_current_arg_to_vector(self.__vector)
        self.__current_arg = []

    def get_vector(self):
        """
        :return: collected vector
        """
        vector = self.__vector.copy()
        self._flush_current_arg_to_vector(vector)
        return vector

    def _flush_current_arg_to_vector(self, vector):
        if self.__current_arg:
            vector.append(''.join(self.__current_arg[:-1]))

    def __str__(self):
        return f'{self.__vector}'
