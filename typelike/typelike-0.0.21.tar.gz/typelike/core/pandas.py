"""
pandas.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from .any import AnyLike

from abc import ABCMeta
import pandas as pd


# Pandas class
class Pandas(AnyLike, metaclass=ABCMeta):
    """
    ``Pandas`` is pandas.Series and pandas.DataFrame

    Note: this class is not implemented. Don't create an instance, because it doesn't do anything.
    """

    # Needed to trick PyCharm
    # noinspection PyMissingConstructor
    def __init__(self):
        self.shape = None
        raise NotImplementedError


# Register subclasses
Pandas.register(pd.DataFrame)
Pandas.register(pd.Series)

AnyLike.register(Pandas)
