# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Size structure member definition."""

from .. import pack
from ._member import Member


def __touchup__(cls, parent):
    index = cls.__variable_size_member_index__

    sized_object = parent[index]
    sized_object_cls = cls.__sized_member_type__

    if isinstance(sized_object, sized_object_cls):
        size = sized_object.nbytes // cls.__ratio__
    else:
        size = len(pack(sized_object_cls, sized_object)) // cls.__ratio__

    return size


class SizeMember(Member):

    """Size structure member definition.

    :param Plum cls: member type
    :param int ratio: number of bytes per increment of member
    :param bool ignore: ignore member during comparisons

    """

    __slots__ = [
        'cls',
        'default',
        'ignore',
        'index',
        'name',
        'ratio',
        'variable_size_member_name',
    ]

    def __init__(self, *, cls=None, ratio=1, ignore=False):
        super(SizeMember, self).__init__(cls=cls, default=None, ignore=ignore)
        self.ratio = ratio
        # filled in by VariableSizeMember definition adjustments
        self.variable_size_member_name = None

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        if self.variable_size_member_name is None:
            raise TypeError(
                f"{self.name!r} member never associated with a variable size member")

        sized_member = members[self.variable_size_member_name]

        if sized_member.default is None:
            default = 0
        else:
            default = sized_member.cls(sized_member.default).nbytes // self.ratio

        namespace = {
            '__default__': default,
            '__ratio__': self.ratio,
            '__variable_size_member_index__': sized_member.index,
            '__sized_member_type__': sized_member.cls,
            '__touchup__': classmethod(__touchup__),
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)

    @property
    def touched_up(self):
        """Indicate if another member may touch up this member.

        :returns: indication
        :rtype: bool

        """
        return True
