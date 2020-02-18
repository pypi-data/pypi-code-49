"""
Parse command into call vector
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from .parse_command_into_call_vector_state_machine import get_starting_state


def parse_command_into_call_vector(cmd):
    """Parse command into a call-vector

    :param cmd: The command
    :return: The call vector
    """
    return _run_state_machine_loop_and_get_vector_from_end_state(cmd)


def _run_state_machine_loop_and_get_vector_from_end_state(cmd):
    state = get_starting_state()
    for char in cmd:
        state = state.parse_and_get_next_state(char)
    return state.parse_and_get_next_state(' ').get_vector()
