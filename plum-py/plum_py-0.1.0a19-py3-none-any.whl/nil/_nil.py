# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Do not interpret bytes."""

from .._plum import Plum
from ._niltype import NilType


class Nil(Plum, metaclass=NilType):

    """Do not interpret bytes."""

    __nbytes__ = 0

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump):
        try:
            dump.cls = cls
        except AttributeError:
            pass  # dump must be None
        else:
            dump.value = 'nil'

        return nil, offset

    @classmethod
    def __pack__(cls, buffer, offset, value, parents, dump):
        if value not in [nil, None]:
            if dump:
                dump.value = value
            raise TypeError('value must be plum.nil or None')

        if dump:
            dump.cls = cls
            dump.value = 'nil'

        return offset

    def __str__(self):
        return 'Nil()'

    def __baserepr__(self):
        return 'Nil()'

    def __repr__(self):
        return self.__baserepr__()

    def __eq__(self, other):
        return (other is self) or (other is None)

    def __ne__(self, other):
        return (other is not self) and (other is not None)


Nil.__module__ = 'plum'  # FUTURE - do this for every type

nil = Nil()
