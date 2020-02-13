# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure member definition."""

from .._plum import PlumType


class Member:

    """Structure member definition.

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
    ]

    def __init__(self, *, cls=None, default=None, ignore=False):

        if cls is not None and not isinstance(cls, PlumType):
            raise TypeError("'cls' must be a Plum type")

        self.cls = cls
        self.default = default
        self.ignore = ignore
        self.name = None  # assigned during structure class construction
        self.index = None  # assigned during structure class construction

    def finish_initialization(self, index, name, annotations):
        """Set member name and type.

        :param int index: member index
        :param str name: member name
        :param dict annotations: subclass type annotations

        """
        self.index = index

        if self.name is not None:
            raise TypeError(
                f"invalid structure member {name!r} definition, "
                f"{type(self).__name__}() instance can not be shared "
                f"between structure members")

        self.name = name

        if self.cls is None:
            cls = annotations.get(name, None)

            if cls is None:
                raise TypeError(
                    f"missing structure member {name!r} type, either specify a "
                    f"Plum type using the 'cls' argument or as a type annotation")

            if not isinstance(cls, PlumType):
                raise TypeError(
                    f"invalid structure member {name!r} type, specify a Plum type "
                    f"using the 'cls' argument")

            self.cls = cls

        return self

    def adjust_members(self, members):
        """Perform adjustment to other members.

        :param dict members: structure member definitions

        """

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """

    @property
    def touched_up(self):
        """Indicate if another member may touch up this member.

        :returns: indication
        :rtype: bool

        """
        return hasattr(self.cls, '__touchup__')
