# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Array dimension structure member definition."""

from ._member import Member
from ..int import Int


def __touchup_single__(cls, parent):
    return len(parent[cls.__array_member_index__])


def __touchup_multi__(cls, parent):
    array = parent[cls.__array_member_index__]
    dims = []
    for _ in range(cls.__dims__[0]):
        dims.append(len(array))
        array = array[0]

    return dims


class DimsMember(Member):

    """Array dimension structure member definition.

    :param Plum cls: member type
    :param bool ignore: ignore member during comparisons

    """

    __slots__ = [
        'default',
        'name',
        'cls',
        'ignore',
        'index',
        'array_member_name',
    ]

    def __init__(self, *, cls=None, ignore=False):
        super(DimsMember, self).__init__(cls=cls, default=None, ignore=ignore)
        self.array_member_name = None  # filled in by VariableDimsMember

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        if self.array_member_name is None:
            raise TypeError(
                f"{self.name!r} member never associated with a variable dims array member")

        array_member = members[self.array_member_name]
        default_array = array_member.default

        if issubclass(self.cls, Int):
            if default_array is None:
                default_array_dims = 0
            else:
                default_array_dims = len(default_array)
        elif default_array is None:
            default_array_dims = [0] * self.cls.__dims__[0]
        else:
            default_array_dims = []
            for _ in range(self.cls.__dims__[0]):
                default_array_dims.append(len(default_array))
                default_array = default_array[0]

        namespace = {
            '__array_member_index__': array_member.index,
            '__default_array_dims__': default_array_dims,
            '__touchup__': classmethod(
                __touchup_single__ if issubclass(self.cls, Int) else __touchup_multi__),
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)

    @property
    def touched_up(self):
        """Indicate if another member may touch up this member.

        :returns: indication
        :rtype: bool

        """
        return True
