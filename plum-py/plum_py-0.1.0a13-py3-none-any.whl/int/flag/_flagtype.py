# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Integer flag type metaclass."""

from ..enum import EnumType


class FlagType(EnumType):

    """Integer flag type metaclass.

    Create custom |Flag| subclass.

    :param int nbytes: number of bytes
    :param str byteorder: ``'big'`` or ``'little'``

    For example:

        >>> from plum.int.flag import Flag
        >>> class MyFlags(Flag, nbytes=1, byteorder='little'):
        ...     RED = 1
        ...     GREEN = 2
        ...     BLUE = 4
        ...
        >>>

    """

    @classmethod
    def __prepare__(mcs, name, bases, nbytes=None, byteorder=None):
        # pylint: disable=arguments-differ
        # pylint: disable=unused-argument
        # pylint: disable=too-many-arguments
        return super().__prepare__(name, bases)

    def __new__(mcs, name, bases, namespace, nbytes=None, byteorder=None):
        # pylint: disable=signature-differs
        # pylint: disable=too-many-arguments
        return super().__new__(mcs, name, bases, namespace,
                               nbytes=nbytes, byteorder=byteorder, signed=False)

    def __init__(cls, name, bases, namespace, nbytes=None, byteorder=None):
        # pylint: disable=too-many-arguments
        super().__init__(name, bases, namespace,
                         nbytes=nbytes, byteorder=byteorder, signed=False)
