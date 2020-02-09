"""
list.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from .any import AnyLike

from abc import ABCMeta
import numpy as np
import pandas as pd


# ListLike class
class ListLike(AnyLike, metaclass=ABCMeta):
    """
    Something that is ``ListLike`` is something that can be coerced into a 1-dimensional list. This includes lists,
    sets, tuples, numpy.ndarray, and pandas.Series.

    Note: this class is not implemented. Don't create an instance, because it doesn't do anything.
    """

    # Needed to trick PyCharm
    # noinspection PyMissingConstructor
    def __init__(self):
        self.shape = None
        raise NotImplementedError


# Register subclasses
ListLike.register(list)
ListLike.register(set)
ListLike.register(tuple)
ListLike.register(np.ndarray)  # TODO is there a way to specify only 1D numpy arrays?
ListLike.register(pd.Series)

AnyLike.register(ListLike)
