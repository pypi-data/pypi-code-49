import functools
import operator

from . import types
from . import utils


__all__ = ()


def _array(store, data, equate, clean):

    proxy = store.copy()

    for data in data:

        for (index, value) in enumerate(proxy):

            if equate(value, data):

                try:

                    any(value, data)

                except TypeError:

                    pass

                del proxy[index]

                break

        else:

            value = store.create(data)

    if clean:

        for value in proxy:

            store.remove(value)


def array(value, data):

    cls = value.factory

    try:

        table = utils.feel(cls)

    except KeyError:

        equate = operator.eq

    else:

        equate = functools.partial(utils.equate, table = table)

    clean = value.clean

    return _array(value, data, equate, clean)


def _mapping(store, data, identify, clean):

    proxy = store.copy()

    for data in data:

        key = identify(data)

        try:

            value = proxy.pop(key)

        except KeyError:

            value = store.create(key, data)

            continue

        try:

            any(value, data)

        except TypeError:

            pass

    if clean:

        for key in proxy:

            del store[key]


def mapping(value, data):

    cls = value.factory

    table = utils.feel(cls)

    identify = functools.partial(utils.identify, table = table)

    clean = value.clean

    return _mapping(value, data, identify, clean)


def _structure(root, data, table, stop = False, clean = False, fill = False):

    proxy = root.copy()

    for (key, data) in data.items():

        if data is None:

            root[key] = data

            continue

        try:

            field = table[key]

        except KeyError:

            if stop:

                raise

            root[key] = data

            continue

        try:

            cls = utils.resolve(field)

            execute = _get(cls)

        except TypeError:

            execute = None

        value = proxy.pop(key, None)

        if execute and value is None:

            value = field()

            execute(value, data)

        elif execute:

            execute(value, data)

            continue

        else:

            value = field(data)

        root[key] = value

    if clean:

        for key in proxy:

            del root[key]

    if fill:

        accept = (types.Collect, types.Structure)

        for (key, field) in table.items():

            cls = utils.resolve(field)

            if key in root:

                continue

            if not issubclass(cls, accept):

                continue

            root[key] = field()


def structure(value, data, **kwargs):

    table = utils.feel(value)

    return _structure(value.__data__, data, table, **kwargs)


def _get(cls):

    if issubclass(cls, types.Mapping):

        return mapping

    if issubclass(cls, types.Array):

        return array

    if issubclass(cls, types.Structure):

        return structure

    raise TypeError(cls)


def any(value, data, **kwargs):

    execute = _get(value.__class__)

    return execute(value, data, **kwargs)
