# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure type view."""

from collections.abc import Sequence

from .._plumview import PlumView

# Attributes __type__, __buffer__, and __offset__ assigned in __init__ of PlumView.
# pylint: disable=no-member


class StructureView(PlumView, Sequence):  # pylint: disable=too-many-ancestors

    """Structure type view."""

    def __add__(self, other):
        return self.get() + other

    def append(self, item):
        """Append object to the end of the list."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support append()")

    def asdict(self):
        """Return structure members in dictionary form.

        :returns: structure members
        :rtype: dict

        """
        return self.get().asdict()

    def clear(self):
        """Remove all items from list."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support clear()")

    def copy(self):
        """Return a shallow copy of the list.

        :returns: shallow copy
        :rtype: list

        """
        return self.get().copy()

    def count(self, item):  # pylint: disable=arguments-differ
        """Return number of occurrences of value.

        :returns: number of occurrences
        :type: int

        """
        return self.get().count(item)

    def __delattr__(self, item):
        raise TypeError(
            f"{self.__class__.__name__!r} does not support attribute deletion")

    def __delitem__(self, key):
        raise TypeError(
            f"{self.__class__.__name__!r} does not support item deletion")

    def __eq__(self, other):
        return self.get() == other

    def extend(self, item):
        """Extend list by appending elements from the iterable."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support extend()")

    def __ge__(self, other):
        return self.get() >= other

    def __getattr__(self, name):
        member_names = self.__type__.__plum_internals__[0]
        try:
            index = member_names.index(name)
        except ValueError:
            # let normal Python AttributeError exception occur
            object.__getattribute__(self, name)

        return self.__getitem__(index)

    def __getitem__(self, index):
        return self.__type__.__plum_internals__[1][index].view(
            self.__buffer__, offset=self.__type__.__offsets__[index] + self.__offset__)

    def __gt__(self, other):
        return self.get() > other

    def __iadd__(self, other):
        raise TypeError(
            f"{self.__class__.__name__!r} does not support in-place addition")

    def __imul__(self, other):
        raise TypeError(
            f"{self.__class__.__name__!r} does not support in-place multiplication")

    def index(self, item):  # pylint: disable=arguments-differ
        """Return first index of value.

        :returns: first index of value
        :type: int

        """
        return self.get().index(item)

    def insert(self, item, index):
        """Insert object before index."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support insert()")

    def __le__(self, other):
        return self.get() <= other

    def __len__(self):
        return len(self.__type__.__plum_names__)

    def __lt__(self, other):
        return self.get() < other

    def __mul__(self, other):
        return self.get() * other

    def pop(self, index=-1):
        """Remove and return item at index (default last)."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support pop()")

    def __radd__(self, other):
        return other + self.get()

    def remove(self, item):
        """Remove first occurrence of value."""
        raise TypeError(
            f"{self.__class__.__name__!r} does not support remove()")

    def reverse(self):
        """Reverse in place."""
        self.set(list(reversed(self.get())))

    def __rmul__(self, other):
        return other * self.get()

    def __setattr__(self, key, value):
        if key in self.__type__.__plum_names__:
            # Attribute name is a structure member, set value of the corresponding view.
            self.__getattr__(key).set(value)
        else:
            # Attribute name is not a structure member, set attribute of this view.
            object.__setattr__(self, key, value)

    def __setitem__(self, index, value):
        self.__getitem__(index).set(value)

    def sort(self):
        """Stable sort in place."""
        self.set(sorted(self.get()))
