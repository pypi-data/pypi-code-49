"""
State machine's entry point
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from .states import BetweenArguments
from .parsing_state import ParsingState
from .parse_context import ParseContext


def get_starting_state() -> ParsingState:
    """
    :return: state at start position
    """
    return BetweenArguments(ParseContext())
