# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Variable type structure member definition."""

from .._plum import Plum, PlumType
from ._member import Member
from ._type_member import TypeMember


class Varies(Plum, metaclass=PlumType):

    """Variably typed member."""

    # overwritten in subclass (in VariableTypeMember.finalize)
    __default__ = None
    __mapping__ = {}
    __member_name__ = ''
    __type_member_index__ = 0

    # def __new__(cls, value):
    #    return value

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump):
        type_member = parents[-1][cls.__type_member_index__]
        member_cls = cls.__mapping__[type_member]
        item, offset = member_cls.__unpack__(buffer, offset, parents, dump)
        if not isinstance(item, member_cls):
            # always create instance so that it may be re-packed (e.g. don't let
            # both UInt8 and UInt16 types produce int ... coerce into Plum type)
            item = member_cls(item)
        return item, offset

    @classmethod
    def __pack__(cls, buffer, offset, value, parents, dump):
        parent_structure = parents[-1]

        value_type_map = cls.__mapping__

        value_type_key = parent_structure[cls.__type_member_index__]

        value_type = value_type_map[value_type_key]

        return value_type.__pack__(buffer, offset, value, parents, dump)

    __baserepr__ = object.__repr__


class VariableTypeMember(Member):

    """Variable type member definition.

    :param TypeMember type_member: type map member definition
    :param object default: initial value when unspecified
    :param bool ignore: ignore member during comparisons

    """

    __slots__ = [
        'cls',
        'default',
        'ignore',
        'index',
        'name',
        'type_member',
    ]

    def __init__(self, *, type_member, default=None, ignore=False):
        if not isinstance(type_member, TypeMember):
            raise TypeError("invalid 'type_member', must be a 'TypeMember' instance")
        super(VariableTypeMember, self).__init__(cls=Varies, default=default, ignore=ignore)
        self.type_member = type_member

    def adjust_members(self, members):
        """Perform adjustment to other members.

        :param dict members: structure member definitions

        """
        self.type_member.variable_type_member_name = self.name

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        type_map = self.type_member.mapping

        # pylint: disable=unidiomatic-typecheck
        if self.default is not None and type(self.default) not in type_map.values():
            raise TypeError(
                f"invalid default for structure member {self.name!r}, the default's "
                f"type must be a type in the type 'mapping'")

        namespace = {
            '__default__': self.default,
            '__mapping__': self.type_member.mapping,
            '__member_name__': self.name,
            '__type_member_index__': self.type_member.index,
        }

        self.cls = type('Varies', (Varies,), namespace)

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance[self.index]

    def __set__(self, instance, value):
        instance[self.index] = value
        instance[self.type_member.index] = self.type_member.cls.__touchup__(instance)
