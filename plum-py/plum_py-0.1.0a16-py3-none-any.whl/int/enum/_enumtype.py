# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Integer enumeration type metaclass."""

from enum import EnumMeta
from .. import IntType


class EnumType(IntType, EnumMeta):

    """Integer enumeration type metaclass.

    Create custom |Enum| subclass.

    :param int nbytes: number of bytes
    :param str byteorder: ``'big'`` or ``'little'``
    :param bool signed: signed integer

    For example:

        >>> from plum.int.enum import Enum
        >>> class Enum24(Enum, nbytes=3, byteorder='big'):
        ...     A = 1
        ...     B = 2
        ...     C = 3
        ...
        >>>

    """

    __unpack_int__ = False

    @classmethod
    def __prepare__(mcs, name, bases, nbytes=None, byteorder=None, signed=None, strict=None):
        # pylint: disable=arguments-differ
        # pylint: disable=unused-argument
        # pylint: disable=too-many-arguments
        return super().__prepare__(name, bases)

    def __new__(mcs, name, bases, namespace, nbytes=None, byteorder=None, signed=None, strict=None):
        # pylint: disable=signature-differs
        # pylint: disable=arguments-differ
        # pylint: disable=too-many-arguments
        # pylint: disable=unused-argument
        return super().__new__(mcs, name, bases, namespace,
                               nbytes=nbytes, byteorder=byteorder, signed=signed)

    def __init__(cls, name, bases, namespace, nbytes=None, byteorder=None, signed=None,
                 strict=None):
        # pylint: disable=too-many-arguments

        if strict is None:
            strict = cls.__strict_enum__

        assert strict in {True, False}

        cls.__strict_enum__ = strict

        super().__init__(name, bases, namespace,
                         nbytes=nbytes, byteorder=byteorder, signed=signed)
