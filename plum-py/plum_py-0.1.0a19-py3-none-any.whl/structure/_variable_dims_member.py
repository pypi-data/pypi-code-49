# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Variable dimensions array structure member definition."""

from ..int import Int
from ._member import Member
from ._dims_member import DimsMember


def __unpack_single__(cls, buffer, offset, parents, dump):
    dims = (int(parents[-1][cls.__dims_member_index__]), )
    # None -> no parents
    return cls.__original_unpack__(buffer, offset, None, dump, dims)


def __unpack_multi__(cls, buffer, offset, parents, dump):
    dims = tuple(int(d) for d in parents[-1][cls.__dims_member_index__])
    # None -> no parents
    return cls.__original_unpack__(buffer, offset, None, dump, dims)


class VariableDimsMember(Member):

    """Variable dimensions array structure member definition.

    :param DimsMember dims_member: array dimensions member name
    :param Plum cls: undimensioned array base class
    :param object default: initial value when unspecified
    :param bool ignore: ignore member during comparisons

    """

    __slots__ = [
        'cls',
        'default',
        'dims_member',
        'ignore',
        'index',
        'name',
        'setter',
    ]

    def __init__(self, *, dims_member, cls=None, default=None, ignore=False):
        if not isinstance(dims_member, DimsMember):
            raise TypeError("invalid 'dims_member', must be a 'DimsMember' instance")

        self.dims_member = dims_member

        super(VariableDimsMember, self).__init__(
            cls=cls, default=default, ignore=ignore, setter=self.set_structure_value)

    def adjust_members(self, members):
        """Perform adjustment to other members.

        :param dict members: structure member definitions

        """
        self.dims_member.array_member_index = self.index

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        dims_cls = self.dims_member.cls

        single_dim = issubclass(dims_cls, Int)

        namespace = {
            '__default__': self.default,
            '__dims_member_index__': self.dims_member.index,
            '__unpack__': classmethod(
                __unpack_single__ if single_dim else __unpack_multi__),
            '__original_unpack__': self.cls.__unpack__,
        }

        if single_dim:
            dims = (None,)
        else:
            dims = [None] * dims_cls.__dims__[0]

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace, dims=dims)

    def set_structure_value(self, structure, value):
        """Set structure array member and update structure dimensions member.

        Set new value in structure array member. Set structure dimensions member
        with dimensions of new value.

        """
        structure[self.index] = value
        structure[self.dims_member.index] = self.dims_member.default(structure)
