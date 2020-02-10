"""
Internal module providing access to the inspection result of a job
"""

from typing import Any, Dict
from contextlib import contextmanager

_inspection_result = {"requirements": [], "assertion_failure": None, "points": 0}


def _reset_inspection_result():
    global _inspection_result
    _inspection_result = {"requirements": [], "assertion_failure": None, "points": 0}


def get_inspection_result() -> Dict[str, Any]:
    """
    Retrieve the current inspection result

    :return:                        a dictionary describing the current inspection result
    """
    return _inspection_result


@contextmanager
def new_inspection_result(**kwargs: Any) -> Dict[str, Any]:
    """
    Create a new inspection result for the duration of a with-block

    :param kwargs:                  entries to initialize the inspection result with
    :return:                        the inspection result
    """
    try:
        global _inspection_result
        _inspection_result = {**_inspection_result, **kwargs}
        yield get_inspection_result()
    finally:
        _reset_inspection_result()
