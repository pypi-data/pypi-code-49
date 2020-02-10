"""
number.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from .any import AnyLike

from abc import ABCMeta
import numpy as np


# NumberLike class
class NumberLike(AnyLike, metaclass=ABCMeta):
    """
    Something that is ``NumberLike`` is something that is singular and numerical

    Note: this class is not implemented. Don't create an instance, because it doesn't do anything.
    """

    # Needed to trick PyCHarm
    # noinspection PyMissingConstructor
    def __init__(self):
        raise NotImplementedError


# Register subclasses
NumberLike.register(int)
NumberLike.register(float)
NumberLike.register(bool)
NumberLike.register(np.int)
NumberLike.register(np.float)
NumberLike.register(np.bool)
