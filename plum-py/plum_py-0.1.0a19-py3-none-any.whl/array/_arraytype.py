# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Array type metaclass."""

from functools import reduce
from operator import mul

from .._plum import Plum, SizeError
from .._plumtype import PlumType

GREEDY_DIMS = (None,)


class ArrayInitError(Exception):

    """Array initialization error."""


class ArrayType(PlumType):

    """Array type metaclass.

    Create custom |Array| subclass.

    :param PlumType item_cls: array item type
    :param dims: array dimension
    :type dims: tuple of int or None

     For example:

            >>> from plum.array import Array
            >>> from plum.int.little import UInt16
            >>> class MyArray(Array, item_cls=UInt16, dims=(10,)):
            ...     pass
            ...
            >>>

    """

    def __new__(mcs, name, bases, namespace, item_cls=None, dims=None):
        # pylint: disable=too-many-arguments, unused-argument
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace, item_cls=None, dims=None):
        # pylint: disable=too-many-arguments
        super().__init__(name, bases, namespace)

        if item_cls is None:
            item_cls = cls.__item_cls__

        assert issubclass(item_cls, Plum)

        if dims is None:
            dims = cls.__dims__

        dims = tuple(None if d is None else int(d) for d in dims)
        if None in dims:
            nbytes = None
        else:
            assert all(d > 0 for d in dims)

            try:
                nbytes = item_cls.nbytes
            except SizeError:
                nbytes = None
            else:
                nbytes *= reduce(mul, dims)

        cls.__dims__ = dims
        cls.__item_cls__ = item_cls
        cls.__nbytes__ = nbytes

    def __make_instance__(cls, iterable, dims=None, idims=0, index=''):
        # pylint: disable=too-many-branches
        if dims is None:
            dims = list(cls.__dims__)
            clsname = cls.__name__
        else:
            clsname = 'Array'

        this_dim = dims[idims]

        if idims < len(dims) - 1:
            item_cls = cls
            if iterable is None:
                if this_dim is None:
                    iterable = []
                else:
                    iterable = [None] * this_dim
        else:
            item_cls = cls.__item_cls__
            if iterable is None:
                if this_dim is None:
                    iterable = []
                else:
                    iterable = [item_cls() for _ in range(this_dim)]

        self = list.__new__(cls, iterable)
        list.__init__(self, iterable)

        if this_dim is None:
            dims[idims] = len(self)
        elif len(self) != this_dim:
            invalid_dimension = (
                f'expected length of item{index} to be {this_dim} '
                f'but instead found {len(self)}')
            raise ArrayInitError(invalid_dimension)

        for i, item in enumerate(self):
            if item_cls is cls:
                item = item_cls.__make_instance__(item, dims, idims + 1, index + f'[{i}]')
            list.__setitem__(self, i, item)

        self.__class_name__ = clsname  # for repr

        return self

    def __call__(cls, iterable=None):
        # pylint: disable=no-value-for-parameter
        return cls.__make_instance__(iterable)
