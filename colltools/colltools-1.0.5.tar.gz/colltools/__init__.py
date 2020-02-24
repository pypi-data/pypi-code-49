""" Helper function for processing data from collections

    This module provides functions to iterate over collections in specialized manner not
    currently supported by `standard Python library`_.

    .. _standard python library:
        https://docs.python.org/3.6/library/itertools.html
"""

from typing import Iterable, Iterator, List, Any, Type, Dict


def batch(iterable: Iterable[Any], step: int) -> Iterator[List[Any]]:
    """ Iterate over `iterable` and group items into batches size of `step`.

        This method is intended to be used in cases where you need to split a stream of data into
        batches of smaller size. For example when storing huge amount to database in batches of 1000
        items. It will create an iterator that gives you a list of items in each iteration of size
        `step`. Last iteration will yield list of all remaining items.

        Example:
            >>> for i in batch(range(8), 3): print(i)
            [0, 1, 2]
            [3, 4, 5]
            [6, 7]
    """
    if not isinstance(step, int):
        raise TypeError(f'Step has to be an integer. {type(step)} given.')
    if step <= 0:
        raise IndexError(f'Step has to be larger than 0, {step} given.')
    items = []
    for i in iterable:
        items.append(i)
        if len(items) == step:
            yield items
            items = []
    if items:
        yield items


class MembersDescriptor(): # pylint: disable=too-few-public-methods
    """ Attribute descriptor for variable `__member__` of `NameRegistry`.

        Returns a dictionary of <name:instance> of all instances provided by that class and all
        subclasses.
    """

    def __get__(self, obj: None, cls: Type['NameRegistry']) -> Dict[str, 'NameRegistry']:
        """ Called by Python when accessing attribute `__members__` of class `NameRegistry`. """
        if not cls.__items__:
            items = {}
            for name in getattr(cls, '__values__', []):
                items[name] = cls(name) # values from class itself
            for subclass in cls.__subclasses__():
                items.update(subclass.__members__) # values from subclasses
            cls.__items__ = items
        return cls.__items__


class NameRegistry:
    """ Instance registry of enumerated values.

        Subclasses of NameRegistry create one instance of itself for each value in class attribute
        __values__. Instances can be returned using ResourceType.get() method which makes sure to
        return the same instance for the same name.

        All subclasses of NameRegistry also provide access to instance of all their subclasses.

        Goal of this class is to provide alternative enumeration implementation compatible with
        SQLAlchemy Enum type.
    """

    __items__: Dict[str, 'NameRegistry'] = {}
    __members__ = MembersDescriptor()

    def __init__(self, name: str):
        """ Create new instance NameRegistry object.

            Validates that name is listed in __values__.
            Should not be called by user code.
        """
        if name not in getattr(self, '__values__', []):
            raise KeyError(f'Name {name} is not listed as allowed.')
        self.name = name

    @classmethod
    def get(cls: Type['NameRegistry'], name: str) -> 'NameRegistry':
        """ Returns instance with specified name.

            Raises KeyError when instance with given name doesn't exist.
        """
        return cls.__members__[name]

    def __repr__(self) -> str:
        """ Returns string representation of an instance. """
        return f'<{self.__class__.__name__}:{self.name}>'
