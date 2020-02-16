import enum
import itertools
import functools
import collections

from . import types
from . import utils


__all__ = ('New', 'Key', 'field')


class New:

    """
    Convenience source for new :class:`~.types.Structure` classes.

    .. code-block:: py

        >>> new = New()
        >>> new.Animal
        '<Animal>'
    """

    __slots__ = ('__data', '__make')

    __space = {'__slots__': ()}

    def __init__(self, root = types.Structure):

        self.__data = {}

        self.__make = lambda key: type(key, (root,), self.__space)

    def __getattr__(self, key):

        try:

            value = self.__data[key]

        except KeyError:

            value = self.__data[key] = self.__make(key)

        return value


class Key(str):

    """
    Key(level, value)

    Signifies a table key.

    :param int level:
        Determines importance. For example, setting it to ``0`` would imply
        this is the primary key, ``1`` could be used for recognising, and ``2+``
        for more trivial reasons.
    :param str value:
        The name of the key.
    """

    __slots__ = ('_level',)

    def __new__(cls, level, value):

        self = super().__new__(cls, value)

        self._level = level

        return self

    @property
    def level(self):

        return self._level


class Table(dict):

    """
    Concentrates instructions on how to handle :class:`Structure`\s.
    """

    __slots__ = ('_groups', '_extra')

    def __init__(self, data, extra = {}):

        check = lambda key: key.level

        groups = collections.defaultdict(list)

        for (level, keys) in itertools.groupby(data, key = check):

            groups[level].extend(keys)

        self._groups = groups

        self.update(data)

        self._extra = extra

    @property
    def groups(self):

        return self._groups

    @property
    def extra(self):

        return self._extra


@functools.lru_cache(None)
def field(cls, *args, **kwargs):

    """
    Signifies a table field.

    .. code-block:: py

        Table(
            {
                Key(0, 'id'): field(str),
                Key(1, 'users'): field(Mapping, new.User)
            }
        )
    """

    return functools.partial(cls, *args, **kwargs)
