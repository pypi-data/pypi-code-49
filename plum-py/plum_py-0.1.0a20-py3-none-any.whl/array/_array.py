# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as a list of uniformly typed items."""

from .._plum import Plum, getbytes
from ..int.little import UInt8
from ._arraytype import ArrayType, GREEDY_DIMS


class Array(list, Plum, metaclass=ArrayType):

    """Interpret bytes as a list of uniformly typed items.

    :param iterable iterable: items

    """

    # filled in by metaclass
    __dims__ = GREEDY_DIMS
    __item_cls__ = UInt8
    __nbytes__ = None

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump, dims=None, outer_level=True):
        # pylint: disable=too-many-branches,too-many-locals,
        # pylint: disable=too-many-arguments,arguments-differ
        if dims is None:
            dims = cls.__dims__

        if dump and outer_level:
            dump.cls = cls

        self = list()

        if dims == GREEDY_DIMS:
            chunk, offset = getbytes(buffer, offset, cls.__nbytes__, dump, cls)

            _offset = 0
            _limit = None
            _len_chunk = len(chunk)

            i = 0
            item_cls = cls.__item_cls__
            if dump:
                dump.memory = b''
                while _offset < _len_chunk:
                    item, _offset, = item_cls.__unpack__(
                        # None -> no parents
                        chunk, _offset, None, dump.add_record(access=f'[{i}]'))
                    self.append(item)
                    i += 1
            else:
                while _offset < _len_chunk:
                    # None -> no parents
                    item, _offset = item_cls.__unpack__(chunk, _offset, None, dump)
                    self.append(item)
                    i += 1
        elif None in dims:
            raise TypeError(
                'greedy multidimensional array types do not support unpack operation')
        else:
            itemdims = dims[1:]
            if dump:
                if itemdims:
                    for i in range(dims[0]):
                        item, offset = cls.__unpack__(
                            # None -> no parents, False -> not outer level
                            buffer, offset, None, dump.add_record(access=f'[{i}]'),
                            itemdims, False)
                        self.append(item)
                else:
                    item_cls = cls.__item_cls__
                    for i in range(dims[0]):
                        item, offset = item_cls.__unpack__(
                            # None -> no parents
                            buffer, offset, None, dump.add_record(access=f'[{i}]'))
                        self.append(item)
            else:
                if itemdims:
                    for i in range(dims[0]):
                        item, offset = cls.__unpack__(
                            # None -> no parents, False -> not outer level
                            buffer, offset, None, dump, itemdims, False)
                        self.append(item)
                else:
                    item_cls = cls.__item_cls__
                    for i in range(dims[0]):
                        # None -> no parents
                        item, offset = item_cls.__unpack__(buffer, offset, None, dump)
                        self.append(item)

        return self, offset

    @classmethod
    def __pack__(cls, buffer, offset, value, parents, dump, dims=None):
        # pylint: disable=too-many-arguments, arguments-differ, too-many-branches

        if dims is None:
            expected_length, *item_dims = cls.__dims__
        else:
            expected_length, *item_dims = dims

        try:
            actual_length = len(value)
        except TypeError:
            if dump:
                dump.value = value
            raise TypeError(
                f'invalid value, expected iterable of '
                f'{"any" if expected_length is None else expected_length} '
                f'length, got non-iterable')

        if expected_length is not None and actual_length != expected_length:
            if dump:
                for i, item in enumerate(value):
                    dump.add_record(access=f'[{i}]', value=item, separate=(i == expected_length))
            raise TypeError(
                f'invalid value, expected iterable of '
                f'{expected_length} length, got iterable of length {actual_length}')

        if dump:
            if dims is None:  # must be outer level
                dump.cls = cls

            if item_dims:
                for i, item in enumerate(value):
                    offset = cls.__pack__(
                        buffer, offset, item, parents, dump.add_record(access=f'[{i}]'),
                        item_dims)
            else:
                item_cls = cls.__item_cls__
                for i, item in enumerate(value):
                    offset = item_cls.__pack__(
                        buffer, offset, item, parents, dump.add_record(access=f'[{i}]'))
        else:
            if item_dims:
                for item in value:
                    offset = cls.__pack__(
                        buffer, offset, item, parents, None, item_dims)
            else:
                item_cls = cls.__item_cls__
                for item in value:
                    offset = item_cls.__pack__(buffer, offset, item, parents, None)

        return offset

    def __str__(self):
        lst = []
        for item in self:
            try:
                rpr = item.__baserepr__
            except AttributeError:
                rpr = item.__repr__

            lst.append(rpr())

        return f"[{', '.join(lst)}]"

    __baserepr__ = __str__

    def __repr__(self):
        # pylint: disable=no-member
        return f'{self.__class_name__}({self.__baserepr__()})'
