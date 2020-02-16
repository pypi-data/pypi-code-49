import pathing
import collections
import copy


__all__ = ('Entry', 'Cache', 'DBCache')


class Entry:

    """
    :class:`dict`\-like attribute-accessible and read-only representation of
    data.

    .. code-block:: py

        >>> entry = Entry({'name': 'Pup', 'age': 6})
        >>> entry.name
        'Pup'

    Overwite the ``__make__(data)`` for copying with different ``__init__``\s.
    """

    __slots__ = ('__data__',)

    def __init__(self, data = None, direct = False):

        self.__data__ = {} if data is None else data if direct else data.copy()

    def __getitem__(self, key):

        return self.__data__[key]

    def __getattr__(self, key):

        try:

            value = self[key]

        except KeyError as error:

            raise AttributeError(*error.args) from None

        return value

    def __make__(self, data):

        return self.__class__(data, True)

    def __copy__(self):

        data = self.__data__.copy()

        fake = self.__make__(data)

        return fake

    def __deepcopy__(self, memo):

        fake = copy.copy(self)

        data = fake.__data__

        for (key, value) in data.items():

            data[key] = copy.deepcopy(value)

        return fake

    def __repr__(self):

        return f'<{self.__class__.__name__}>'


def update(entry, data):

    """
    Update an :class:`Entry` with the data.
    """

    entry.__data__.update(data)


class Cache(dict):

    """
    Convenient means of managing entries.

    :param int depth:
        Amount of keys required to access entries.
    :param func create:
        Transforms new data to entries.
    :param func update:
        Keeps matching entries up-to-date.

    :var entries:
        Yields all entries.
    """

    __slots__ = ('_depth', '_build',)

    _Build = collections.namedtuple('Build', 'create update')

    def __init__(self, depth, create = Entry, update = update):

        self._depth = depth

        self._build = self._Build(create, update)

    @property
    def depth(self):

        return self._depth

    def iterate(self):

        """
        Yields ``(keys, value)`` pairs.
        """

        yield from pathing.derive(self, min = self._depth, max = self._depth)

    @property
    def entries(self):

        for (keys, value) in self.iterate():

            yield value

    def _make(self, depth):

        return self.__class__(depth, *self._build)

    __final = object()

    def _seek(self, keys, final = __final):

        value = self

        abrupt = final is self.__final

        keys = tuple(keys)

        stop = len(keys) - 1

        generate = enumerate(keys)

        while True:

            yield value

            try:

                (index, key) = next(generate)

            except StopIteration:

                break

            try:

                value = value[key]

            except KeyError:

                if abrupt:

                    return

            else:

                continue

            if index == stop:

                subvalue = final

            else:

                depth = value.depth - 1

                subvalue = self._make(depth)

            value[key] = value = subvalue

    def _wipe(self, keys):

        generate = self._seek(keys)

        values = reversed(tuple(generate))

        skip = object()

        keys = reversed((*keys, skip))

        for (value, key) in zip(values, keys):

            if key is skip:

                yield value

                continue

            yield value.pop(key)

            if len(value):

                break

    def _lead(self, *args, **kwargs):

        (*rest, value) = self._seek(*args, **kwargs)

        return value

    @classmethod
    def _flat(cls, value):

        return tuple(value.entries) if isinstance(value, cls) else (value,)

    def select(self, keys):

        """
        Get all entries against the ``keys``.
        """

        value = self._lead(keys)

        entries = self._flat(value)

        return entries

    def create(self, keys, data):

        """
        Create and hold all entries created from ``data`` against the ``keys``
        and return.
        """

        value = self._build.create(data)

        self._lead(keys, final = value)

        entries = self._flat(value)

        return entries

    def update(self, keys, data):

        """
        Update all entries with ``data`` against the ``keys`` and return.
        """

        entries = self.select(None, keys)

        dummies = copy.deepcopy(entries)

        for entry in entries:

            self._build.update(entry, data)

        pairs = tuple(zip(dummies, entries))

        return pairs

    def delete(self, keys):

        """
        Delete all entries with data against the ``keys`` and return.

        .. note::

            Sub-Caches will be removed as well if they appear empty.
        """

        (value, *rest) = self._wipe(keys)

        entries = self._flat(value)

        return entries

    def place(self, old, new):

        """
        Change the position of whatever is against ``old`` to ``new`` keys.
        """

        (final, *rest) = self._wipe(old)

        self._lead(new, final = final)

    def __repr__(self):

        count = len(tuple(self.entries))

        return f'<{self.__class__.__name__}[{count}]>'


class DBCache(Cache):

    """
    Treats existing funtionality as a database-like proxy.

    :param list[str] primary:
        Names of fields used to resolve primary values.
    """

    __slots__ = ('_primary',)

    def __init__(self, primary, *args, **kwargs):

        depth = len(primary)

        super().__init__(depth, *args, **kwargs)

        self._primary = primary

    @property
    def primary(self):

        return self._primary

    def _make(self, depth):

        return self.__class__(self._primary[:depth], *self._build)

    def query(self, data):

        """
        Get all values agains the ``data``\'s ``primary keys``.

        .. code-block: py

        >>> cache = DBCache(('id', 'age'))
        >>> cache.query({'id': '0', 'name': 'Pup', 'age': 7})
        >>> ('0', 7)
        """

        store = []

        try:

            store.extend(data[key] for key in self._primary)

        except KeyError:

            pass

        return tuple(store)

    def select(self, data, keys = ()):

        result = super().select(keys)

        return result

    def create(self, data, keys = ()):

        if not keys:

            keys = self.query(data)

        result = super().create(keys, data)

        return result

    def update(self, data, keys = ()):

        """
        Will also change the position of respective entries if ``keys`` don't
        match the ``primary`` ones.
        """

        if not keys:

            keys = self.query(data)

        keys = list(keys)

        fresh = keys.copy()

        for (index, name) in enumerate(self._primary):

            try:

                key = data[name]

            except KeyError:

                continue

            try:

                fresh[index] = key

            except IndexError:

                break

        if not fresh == keys:

            self.place(keys, fresh)

            keys = fresh

        result = super().update(keys, data)

        return result

    def delete(self, data, keys = ()):

        result = super().delete(keys)

        return result
