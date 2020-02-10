# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure type."""

from .._plum import Plum
from ._structuretype import StructureType
from ._structureview import StructureView


class Structure(list, Plum, metaclass=StructureType):

    """Interpret bytes as a list of uniquely typed items.

    :param iterable iterable: items

    """

    # filled in by metaclass
    __plum_internals__ = (), (), False  # names, types, has_touchups
    __nbytes__ = 0
    __plum_names__ = []

    def __init__(self, *args, **kwargs):
        # pylint: disable=super-init-not-called

        # initializer for anonymous structure (metaclass overrides this
        # when creating subclasses with pre-defined members)
        list.extend(self, args)
        names = [None] * len(args)
        if kwargs:
            list.extend(self, kwargs.values())
            names.extend(kwargs.keys())
        object.__setattr__(self, '__plum_names__', names)

    @classmethod
    def __pack__(cls, buffer, offset, value, parents, dump):
        # pylint: disable=too-many-branches

        # implementation for anonymous structure (metaclass overrides this with
        # _methods.__pack__ when creating subclasses with pre-defined members)

        if dump:
            dump.cls = cls

            if isinstance(value, cls):
                names = value.__plum_names__
            elif isinstance(value, dict):
                names = value.keys()
                value = value.values()
            elif isinstance(value, (list, tuple)):
                names = [None] * len(value)
            else:
                raise TypeError(f'{cls.__name__!r} pack accepts an iterable')

            for i, (name, item) in enumerate(zip(names, value)):
                if name:
                    subdump = dump.add_record(access=f'[{i}] (.{name})')
                else:
                    subdump = dump.add_record(access=f'[{i}]')

                value_cls = type(item)
                if not issubclass(value_cls, Plum):
                    subdump.value = repr(item)
                    subdump.cls = value_cls.__name__ + ' (invalid)'
                    desc = f' ({name})' if name else ''
                    raise TypeError(
                        f'anonymous structure member {i}{desc} not a plum type')

                offset = value_cls.__pack__(buffer, offset, item, parents, subdump)
        else:
            if isinstance(value, dict):
                value = value.values()
            elif not isinstance(value, (list, tuple)):
                raise TypeError(f'{cls.__name__} pack accepts an iterable item')

            for item in value:
                item_cls = type(item)
                if not issubclass(item_cls, Plum):
                    raise TypeError('item in anonymous structure not a plum type instance')

                offset = item_cls.__pack__(buffer, offset, item, parents, None)

        return offset

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump):
        # pylint: disable=too-many-locals
        if parents is None:
            parents = []

        names, types, _has_touchups = cls.__plum_internals__

        self = list.__new__(cls)
        append = list.append

        parents.append(self)

        try:
            if dump:
                dump.cls = cls

                for i, (name, item_cls) in enumerate(zip(names, types)):
                    item, offset = item_cls.__unpack__(
                        buffer, offset, parents,
                        dump.add_record(access=f'[{i}] (.{name})'))
                    append(self, item)
            else:
                for item_cls in types:
                    item, offset = item_cls.__unpack__(buffer, offset, parents, dump)
                    append(self, item)
        finally:
            parents.pop()

        return self, offset

    def __str__(self):
        lst = []
        for name, value in zip(self.__plum_names__, self):
            try:
                rpr = value.__baserepr__()
            except AttributeError:
                rpr = value.__repr__()
            if name is not None:
                rpr = name + '=' + rpr
            lst.append(rpr)

        return f"{type(self).__name__}({', '.join(lst)})"

    __baserepr__ = __str__

    __repr__ = __str__

    @classmethod
    def __view__(cls, buffer, offset=0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
        :param int offset: byte offset

        """
        if not cls.__nbytes__:
            raise TypeError(f"cannot create view for structure {cls.__name__!r} "
                            "with variable size")

        if cls.__plum_internals__[2]:  # has_touchups flags
            raise TypeError(f"cannot create view for structure {cls.__name__!r} "
                            "with member protocol touch-ups")

        return StructureView(cls, buffer, offset)

    def __getattr__(self, name):
        # implementation for anonymous structure (metaclass doesn't bother
        # overriding since its harmless)
        try:
            index = object.__getattribute__(self, '__plum_names__').index(name)
        except (AttributeError, ValueError):
            # AttributeError -> structure instantiated without names
            # ValueError -> name not one used during structure instantiation

            # for consistent error message, let standard mechanism raise the exception
            object.__getattribute__(self, name)
        else:
            return self[index]

    def __setattr__(self, name, value):
        # implementation for anonymous structure (metaclass overrides this
        # when creating subclasses with pre-defined members)
        try:
            index = self.__plum_names__.index(name)
        except ValueError:
            # AttributeError -> unpacking Structure and never instantiated
            # ValueError -> name not one used during structure instantiation
            raise AttributeError(
                f"{type(self).__name__!r} object has no attribute {name!r}")
        else:
            self[index] = value

    def asdict(self):
        """Return structure members in dictionary form.

        :returns: structure members
        :rtype: dict

        """
        # implementation for anonymous structure (metaclass overrides this
        # when creating subclasses with pre-defined members)
        names = self.__plum_names__
        return {k: v for k, v in zip(names, self) if k is not None}

    def append(self, item):
        """Append object to the end of the list."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support append()")

    def clear(self):
        """Remove all items from list."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support clear()")

    def __delattr__(self, item):
        raise TypeError(
            f"{self.__class__.__name__!r} does not support attribute deletion")

    def __delitem__(self, key):
        raise TypeError(
            f"{self.__class__.__name__!r} does not support item deletion")

    def extend(self, item):
        """Extend list by appending elements from the iterable."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support extend()")

    def __iadd__(self, other):
        raise TypeError(
            f"{self.__class__.__name__!r} does not support in-place addition")

    def __imul__(self, other):
        raise TypeError(
            f"{self.__class__.__name__!r} does not support in-place multiplication")

    def insert(self, item, index):
        """Insert object before index."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support insert()")

    def pop(self, index=-1):
        """Remove and return item at index (default last)."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support pop()")

    def remove(self, item):
        """Remove first occurrence of value."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support remove()")

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            if len(self[index]) != len(value):
                raise TypeError(
                    f"{self.__class__.__name__!r} does not support resizing "
                    "(length of value must match slice)")
        super(Structure, self).__setitem__(index, value)
