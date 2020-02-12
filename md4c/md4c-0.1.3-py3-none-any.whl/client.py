
from . import types
from . import binds
from . import flags
from . import helpers


__all__ = ('load', 'Client')


lib = None


def load(path):

    """
    Load the library.

    .. note::

        Must be called at least once before any further usage of this module.
    """

    global lib

    if not lib:

        lib = binds.load(path)


class Client:

    __slots__ = ('_store',)

    _version = 0

    def __init__(self, **options):

        self._store = binds.create(
            flags = flags.Dialect.commonmark,
            **options,
            api_version = self._version
        )

    def parse(self, value):

        """
        Parse `value` with `struct`\'s callbacks.
        """

        size = len(value)

        value = value.encode()

        return helpers.c_call(lib.md_parse, value, size, self._store, 0)
