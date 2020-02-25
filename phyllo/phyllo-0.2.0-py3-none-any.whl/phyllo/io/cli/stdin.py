"""Handle line input from stdin."""

# Builtins

import logging
from ast import literal_eval

# Packages

logger = logging.getLogger(__name__)


try:
    import readline
    readline.set_history_length(64)
except ImportError:
    logger.warning('Console input readline capabilities are not available on this platform.')


# Parsing

def eval_literal(input_string):
    """Evaluate an input string as a Python literal."""
    if input_string == '':
        return None
    try:
        return literal_eval(input_string)
    except (SyntaxError, ValueError):
        logger.exception(
            'Invalid input. Only Python literal structures (strings, bytes, '
            'numbers, tuples, lists, dicts, sets, booleans, and None) are allowed.'
        )


def input_literal(prompt):
    """Get console input of literal values and structures."""
    try:
        input_string = input(prompt)
    except EOFError:
        raise KeyboardInterrupt
    return eval_literal(input_string)
