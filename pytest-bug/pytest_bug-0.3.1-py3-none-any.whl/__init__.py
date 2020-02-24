import pytest

from .__version__ import (
    __version__,
    __author__,
    __author_email__,
    __description__,
    __license__,
    __url__
)


def bug(*args, run=False):
    return pytest.mark.bug(*args, run=run)


__all__ = [
    '__version__',
    '__author__',
    '__author_email__',
    '__description__',
    '__license__',
    '__url__',
    'bug'
]
