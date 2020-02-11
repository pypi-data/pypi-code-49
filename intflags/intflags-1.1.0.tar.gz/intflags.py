"""
intflags
========

The simplest way to create bit-flags.

Basic usage:

    >>> import intflags
    >>> x, y, z = intflags.get(3)
    >>> flags = x | y
    >>> y in flags
    True
    >>> z in flags
    False
    >>> int(y)
    2

In a class:

    >>> class MyFlags:
    ...     A, B, C, D = intflags.get(4)
    ...
    >>> flags = MyFlags.A | MyFlags.D
    >>> new = flags - MyFlags.D
    >>> MyFlags.D in new
    False
    >>> new == MyFlags.A
    True

"""

__all__ = ["get"]
__author__ = "SeparateRecords <me@rob.ac>"
__copyright__ = "(c) Robert Cooper, 2020"
__version__ = "1.1.0"

from itertools import count

# The global namespace index to ensure no two sets of flags have the same ns.
# This will be incremented by ``get()`` with every call.
_NS_IDX = count()


class _Flag:
    def __init__(self, i, ns):
        """Create a flag with value ``i`` and namespace ``ns``."""
        self._i = i
        self._ns = ns

    @property
    def ns(self):
        return self._ns

    def _new(self, i):
        return type(self)(i, self.ns)

    def __eq__(self, other):
        try:
            return int(self) == int(other) and self.ns == other.ns
        except AttributeError:
            return NotImplemented

    def __contains__(self, other):
        if other.ns != self.ns:
            return False

        value = int(self) & int(other)
        return bool(value)

    def __or__(self, other):
        if other.ns != self.ns:
            msg = "Flags must share a namespace to create a union."
            raise ValueError(msg)

        value = int(self) | int(other)
        return self._new(value)

    def __add__(self, other):
        return self.__or__(other)

    def __sub__(self, other):
        if other.ns != self.ns:
            raise ValueError("Flags must share a namespace to be subtracted.")

        value = int(self) & ~int(other)
        return self._new(value)

    def __index__(self):
        return self._i

    def __str__(self):
        return str(self._i)

    def __repr__(self):
        return "<{0.__class__.__qualname__} ({0}, ns={0.ns})>".format(self)


def get(n):
    """Create ``n`` flags in the same namespace.
    
    If ``n == 1``, a single flag is returned (not as an iterable).
    """
    ns = next(_NS_IDX)

    if n == 1:
        return _Flag(1, ns)

    return [_Flag(2 ** i, ns) for i in range(0, n)]
