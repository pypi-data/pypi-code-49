import functools
import operator
import math

from . import types


__all__ = ('feel', 'resolve', 'auto', 'locate', 'analyse', 'identify', 'equate',
           'origin', 'hosts')


def feel(value):

    """
    Get the table of the value (or class).
    """

    if not isinstance(value, type):

        value = value.__class__

    from . import tables

    return tables[value]


def resolve(value, full = False):

    if isinstance(value, functools.partial):

        point = value.func

        if full:

            if issubclass(point, types.Collect):

                point = next(iter(value.args))

        return resolve(point)

    return value


def auto(function):

    @functools.wraps(function)
    def wrapper(*args, table = None, **kwargs):

        if not table:

            table = feel(args[0])

        return function(table, *args, **kwargs)

    return wrapper


__foreign = object()


def locate(table, value, level, dive = 0, full = False, extra = False):

    """
    Get all keys and values against the table's level keys.
    """

    default = ()

    skip = not full

    subdive = dive - 1

    for sublevel in sorted(table.groups):

        if sublevel > level:

            break

        allow = sublevel == level

        if extra and allow:

            for apply in table.extra.get(sublevel, default):

                if isinstance(apply, str):

                    data = apply.format(**value)

                else:

                    data = apply(value)

                yield (__foreign, data)

        deny = not allow

        for key in table.groups.get(sublevel, default):

            field = table[key]

            cls = resolve(field)

            try:

                data = value[key]

            except KeyError:

                continue

            try:

                subtable = feel(cls)

            except KeyError:

                if deny and skip:

                    continue

            else:

                if dive:

                    yield from locate(
                        subtable, data, level,
                        subdive, full, extra
                    )

                continue

            yield (key, data)


@auto
def analyse(table, value, level, dive = 0, *, full = False, extra = False):

    """
    Get all values against the table's level keys.
    """

    if isinstance(value, types.Structure):

        value = value.__data__

    for (key, data) in locate(table, value, level, dive = dive, extra = extra):

        yield data


@auto
def identify(table, value, strict = True):

    """
    Get the first means of primary identification.
    """

    generate = analyse(value, 0, math.inf, table = table)

    try:

        value = next(generate)

    except StopIteration:

        if strict:

            raise ValueError('could not resolve identity')

        if isinstance(value, types.Structure):

            value = value.__data__

    return value


@auto
def equate(table, *values):

    """
    Check whether all values are equal.
    """

    execute = functools.partial(identify, table = table, strict = False)

    return operator.eq(*map(execute, values))


@auto
def origin(table, source, target, direct = True):

    """
    Get the first attribute of source that points to the target.

    :param type source:
        Subclass for :class:`~.types.Structure`, used for searching.
    :param type target:
        Class to look for.
    :param bool direct:
        Whether to check for the target or a :class:`~.types.Collect` storing
        it.
    """

    indirect = not direct

    for (key, field) in table.items():

        check = field.func

        if issubclass(check, types.Collect):

            if direct:

                continue

            check = resolve(next(iter(field.args)))

        else:

            if indirect:

                continue

        if check is target:

            break

    else:

        raise ValueError(target)

    return key


def hosts(target, direct = True):

    """
    Get each class against its attribute that points to the value.

    :param type value:
        Class to look for in the plans.
    :param bool direct:
        Whether to check for the value or a :class:`types.Collect` storing it.
    """

    from . import tables

    for (cls, table) in tables.items():

        try:

            key = origin(cls, target, direct = direct)

        except ValueError:

            continue

        yield (cls, key)
