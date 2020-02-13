# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Type map structure member definition."""

from ._member import Member


def __touchup__(cls, parent):
    variable_type_member = parent[cls.__variable_type_member_index__]

    member_type = type(variable_type_member)

    try:
        type_value = cls.__reverse_mapping__[member_type]
    except KeyError:
        types = list(c.__name__ for c in reversed(list(cls.__reverse_mapping__)))

        raise TypeError(
            f'structure member {cls.__variable_type_member_name__!r} must '
            f'be one of the following types: {types}, not {member_type.__name__!r}')

    return type_value


class TypeMember(Member):

    """Structure member holding a type map for another member.

    :param dict mapping: type member value (key) to Plum type (value) mapping
    :param bool ignore: ignore member during comparisons

    """

    __slots__ = [
        'cls',
        'default',
        'ignore',
        'index',
        'mapping',
        'name',
        'variable_type_member_name',
    ]

    def __init__(self, *, mapping, cls=None, ignore=False):
        super(TypeMember, self).__init__(cls=cls, default=None, ignore=ignore)
        self.mapping = mapping
        # filled in by VariableTypeMember definition adjustments
        self.variable_type_member_name = None

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        if self.variable_type_member_name is None:
            raise TypeError(
                f"{self.name!r} member never associated with a variable type member")

        variable_type_member = members[self.variable_type_member_name]

        namespace = {
            '__default__': self.default,
            '__reverse_mapping__': {
                value: key for key, value in reversed(list(self.mapping.items()))},
            '__touchup__': classmethod(__touchup__),
            '__variable_type_member_index__': variable_type_member.index,
            '__variable_type_member_name__': variable_type_member.name,
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)

    @property
    def touched_up(self):
        """Indicate if another member may touch up this member.

        :returns: indication
        :rtype: bool

        """
        return True
