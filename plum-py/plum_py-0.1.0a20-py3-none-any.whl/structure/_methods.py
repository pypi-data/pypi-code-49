# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Special methods for Structure subclasses with defined members."""

from .._plumview import PlumView


def asdict(self):
    """Return structure members in dictionary form.

    :returns: structure members
    :rtype: dict

    """
    names, _types = self.__names_types__
    return dict(zip(names, self))


def __pack__(cls, buffer, offset, value, parents, dump):
    # pylint: disable=too-many-branches
    names, types = cls.__names_types__

    if isinstance(value, PlumView):
        # read all members at once
        value = value.get()

    if isinstance(value, dict):
        value = cls(**value)

    try:
        if len(names) != len(value):
            raise ValueError(
                f'invalid value, '
                f'{cls.__name__!r} pack expects an iterable of length {len(names)}, '
                f'got an iterable of length {len(value)}')
    except TypeError:
        raise TypeError(
            f'invalid value, '
            f'{cls.__name__!r} pack expects an iterable of length {len(names)}, '
            f'got a non-iterable')

    if parents is None:
        parents = [value]
    else:
        parents.append(value)

    try:
        if dump:
            dump.cls = cls

            for i, (name, value_cls) in enumerate(zip(names, types)):
                offset = value_cls.__pack__(
                    buffer, offset, value[i], parents, dump.add_record(access=f'[{i}] (.{name})'))
        else:
            for i, value_cls in enumerate(types):
                offset = value_cls.__pack__(buffer, offset, value[i], parents, None)
    finally:
        parents.pop()

    return offset


def __setattr__(self, name, value):
    # get the attribute to raise an exception if invalid name
    getattr(self, name)
    object.__setattr__(self, name, value)
