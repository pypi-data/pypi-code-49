import math
import collections
import weakref

from . import cache
from . import utils


__all__ = ('Collect', 'Array', 'Mapping', 'StructureMeta', 'Structure')


class Collect:

    """
    Manager for building and limiting collections.

    :param func factory:
        Used for creating new values with incoming data.
    :param int limit:
        Forget old values when adding new ones that exceed this.
    :param bool clean:
        Whether to clear all values before bulk-updating with new ones.
    """

    def __init__(self, factory, *, limit = math.inf, clean = True):

        self._factory = factory

        self._limit = limit

        self._clean = clean

    @property
    def factory(self):

        return self._factory

    @property
    def limit(self):

        return self._limit

    @limit.setter
    def limit(self, value):

        self._limit = value

    @property
    def clean(self):

        return self._clean

    def _unique(self):

        raise NotImplementedError

    def _ensure(self):

        if not len(self) == self._limit:

            return

        key = self._unique()

        del self[key]

    def create(self, data):

        self._ensure()

        value = self._factory(data)

        return value

    def __repr__(self):

        return f'<{self.__class__.__name__}({len(self)})>'


class Array(Collect, list):

    """.."""

    def _unique(self):

        return 0

    def create(self, data):

        value = super().create(data)

        self.append(value)

        return value


class Mapping(Collect, dict):

    """.."""

    def _unique(self):

        return next(iter(self))

    def create(self, key, data):

        value = super().create(data)

        self.__setitem__(key, value)

        return value

#:
missing = type(
    'missing',
    (),
    {
        '__slots__': (),
        '__bool__': False.__bool__,
        '__iter__': ().__iter__,
        '__doc__': 'Signal for data that could be there but is not.'
    }
)()


class StructureMeta(cache.Entry.__class__):

    def __getattr__(self, key):

        table = utils.feel(self)

        try:

            value = table[key]

        except KeyError as error:

            raise AttributeError(*error.args) from None

        return value


_memories = collections.defaultdict(weakref.WeakValueDictionary)


class Structure(cache.Entry, metaclass = StructureMeta):

    """
    Updates with incoming data and returns :class:`missing` on unwarranted
    attribute access.

    :param dict data:
        Information to store.
    :param bool direct:
        Keep the data or a copy of it.
    :param bool cache:
        Memoize this class against the first :func:`~.utils.identify` value.
        Cache-able instance creation will always return the same object, and
        just update old data with new.
    """

    __slots__ = ('__weakref__',)

    def __new__(cls,
                data = None,
                direct = False,
                *,
                cache = False,
                **kwargs):

        memory = _memories[cls]

        cache = cache and not data is None

        if cache:

            table = utils.feel(cls)

            try:

                primary = utils.identify(data, table = table)

            except ValueError:

                primary = None

            self = memory.get(primary)

        else:

            self = None

        if not self:

            self = super().__new__(cls)

            if cache and primary:

                memory[primary] = self

            root = data if direct else None

            # NOTE overwrite cls' __init__
            super().__init__(self, root, direct)

        if not (data is None or direct):

            from . import updates

            updates.structure(self, data, **kwargs)

        return self

    def __init__(self, *args, **kwargs):

        pass

    def __getattr__(self, key):

        try:

            value = super().__getattr__(key)

        except AttributeError:

            table = utils.feel(self.__class__)

            if key in table:

                return missing

            raise

        return value

    def __hash__(self):

        value =  utils.identify(self)

        return hash(value)
