import logging
import os

_LOGGER = logging.getLogger(__name__)


def get_terminal_size():
    """query the width of the current terminal
    return a named tuple with "columns" and "lines" as properties.
    """

    val = os.get_terminal_size()

    return val
