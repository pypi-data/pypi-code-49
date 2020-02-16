"""
types.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from abc import ABCMeta
import numpy as np
import pandas as pd

# Contents
__all__ = [
    'ListLike'
]


# ListLike class
class ListLike(metaclass=ABCMeta):
    """
    Something that is ``ListLike`` is something that can be coerced into a 1-dimensional list. This includes lists,
    sets, tuples, numpy.ndarray, and pandas.Series.

    Note: this class is not implemented. Don't create an instance, because it doesn't do anything.
    """

    # Needed to trick PyCharm
    def __init__(self, data):
        self.shape = None

    # Needed to trick PyCharm
    def __getitem__(self, item):
        raise NotImplementedError

    # Needed to trick PyCharm
    def __iter__(self):
        raise NotImplementedError

    # Needed to trick PyCharm
    def __len__(self):
        raise NotImplementedError

    # Register subclass as ArrayLike
    @classmethod
    def register(cls, subclass):
        """
        Registers a new subclass as ``ListLike``

        Parameters
        ----------
        subclass : class
            Subclass to register as ``ListLike``
        """

        # noinspection PyCallByClass
        ABCMeta.register(cls, subclass)


# Register subclasses
ListLike.register(list)
ListLike.register(set)
ListLike.register(tuple)
ListLike.register(np.ndarray)  # TODO is there a way to specify only 1D numpy arrays?
ListLike.register(pd.Series)
