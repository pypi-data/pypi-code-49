"""The simplest way to create bit-flags.

Basic usage
-----------

    >>> import intflags
    >>> x, y, z = intflags.get(3)
    >>> flags = x | y
    >>> y in flags
    True
    >>> z in flags
    False
    >>> int(y)
    2

In a class
----------

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

# ISC License
#
# Copyright (c) 2020, Robert "SeparateRecords" Cooper
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

__all__ = ["IntFlag", "get"]
__author__ = "SeparateRecords <me@rob.ac>"
__copyright__ = "(c) Robert Cooper, 2020"
__version__ = "2.0.0"

from itertools import count


class IntFlag(int):
    """Create an int flag, optionally using a namespace."""

    def __new__(cls, i, ns=None):
        instance = super().__new__(cls, i)
        instance.ns = ns
        return instance

    def check(self, other):
        try:
            return self.ns == other.ns
        except AttributeError:
            return False

    def make(self, i):
        return type(self)(i, self.ns)

    def __eq__(self, other):
        try:
            return int(self) == int(other) and self.ns == other.ns
        except AttributeError:
            return NotImplemented

    def __contains__(self, other):
        if not self.check(other):
            return False
        return bool(self & other)

    def __or__(self, other):
        if not self.check(other):
            msg = "Flags must share a namespace to create a union."
            raise ValueError(msg)
        return self.make(int.__or__(self, other))

    def __add__(self, other):
        return self.__or__(other)

    def __sub__(self, other):
        if not self.check(other):
            raise ValueError("Flags must share a namespace to be subtracted.")

        value = self & ~other
        return self.make(value)

    def __str__(self):
        return str(int(self))

    def __repr__(self):
        return "<Flag [{0}, ns={0.ns}]>".format(self)


# The global namespace index to ensure no two sets of flags have the same ns.
# This will be incremented by ``get()`` with every call.
_NS_IDX = count()


def get(n, use_ns=True):
    """Create ``n`` flags in the same namespace, optionally with a leading sentinel.

    If ``n == 1``, a single flag is returned (not as an iterable).
    """
    ns = next(_NS_IDX) if use_ns else None

    if n == 1:
        return IntFlag(1, ns)

    return [IntFlag(2 ** i, ns) for i in range(0, n)]
