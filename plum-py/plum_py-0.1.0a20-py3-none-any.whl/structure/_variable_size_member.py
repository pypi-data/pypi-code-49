# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Variable sized member definition."""

from .._exceptions import ExcessMemoryError
from .._plum import getbytes
from ._member import Member
from ._size_member import SizeMember


def __unpack__(cls, buffer, offset, parents, dump):
    # pylint: disable=too-many-locals

    expected_size_in_bytes = (
        parents[-1][cls.__size_member_index__] - cls.__offset__) * cls.__ratio__

    chunk, offset = getbytes(buffer, offset, expected_size_in_bytes, dump, cls)

    if dump:
        dump.memory = b''

    item, actual_size_in_bytes = cls.__original_unpack__(chunk, 0, parents, dump)

    extra_bytes = chunk[actual_size_in_bytes:]

    if extra_bytes:
        if dump:
            value = '<excess bytes>'
            separate = True
            for i in range(0, len(extra_bytes), 16):
                dump.add_record(separate=separate, value=value, memory=extra_bytes[i:i+16])
                value = ''
                separate = False

        raise ExcessMemoryError(f'{len(extra_bytes)} unconsumed bytes', extra_bytes)

    return item, offset


class VariableSizeMember(Member):

    """Variable sized member definition.

    :param SizeMember size_member: size member definition
    :param Plum cls: member type
    :param object default: initial value when unspecified
    :param bool ignore: ignore member during comparisons

    """

    __slots__ = [
        'cls',
        'default',
        'ignore',
        'index',
        'name',
        'setter',
        'size_member',
    ]

    def __init__(self, *, size_member, cls=None, default=None, ignore=False):
        if not isinstance(size_member, SizeMember):
            raise TypeError("invalid 'size_member', must be a 'SizeMember' instance")
        super(VariableSizeMember, self).__init__(
            cls=cls, default=default, ignore=ignore, setter=self.set_structure_value)
        self.size_member = size_member

    def adjust_members(self, members):
        """Perform adjustment to other members.

        :param dict members: structure member definitions

        """
        self.size_member.variable_size_member_cls = self.cls
        self.size_member.variable_size_member_index = self.index

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        namespace = {
            '__offset__': self.size_member.offset,
            '__ratio__': self.size_member.ratio,
            '__size_member_index__': self.size_member.index,
            '__unpack__': classmethod(__unpack__),
            '__original_unpack__': self.cls.__unpack__,
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)

    def set_structure_value(self, structure, value):
        """Set structure array member and update structure dimensions member.

        Set new value in structure array member. Set structure dimensions member
        with dimensions of new value.

        """
        structure[self.index] = value
        structure[self.size_member.index] = self.size_member.default(structure)
