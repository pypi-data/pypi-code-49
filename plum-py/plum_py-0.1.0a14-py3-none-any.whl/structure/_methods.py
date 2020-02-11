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
    names, _types, _has_touchups = self.__plum_internals__
    return dict(zip(names, self))


def __pack__(cls, buffer, offset, value, parents, dump):
    # pylint: disable=too-many-branches
    names, types, has_touchups = cls.__plum_internals__

    if isinstance(value, PlumView):
        # read all members at once
        value = value.get()

    if isinstance(value, dict):
        value = cls(**value)
    else:
        try:
            len_item = len(value)
        except TypeError:
            raise TypeError(f'{cls.__name__!r} pack accepts an iterable')

        if (has_touchups and not isinstance(value, cls)) or (len_item != len(types)):
            # create instance to touch up, fill in defaults, or error
            value = cls(*value)

    if parents is None:
        parents = [value]
    else:
        parents.append(value)

    try:
        if dump:
            dump.cls = cls

            for i, (name, value_cls, value_) in enumerate(zip(names, types, value)):
                offset = value_cls.__pack__(
                    buffer, offset, value_, parents, dump.add_record(access=f'[{i}] (.{name})'))
        else:
            for value_cls, value_ in zip(types, value):
                offset = value_cls.__pack__(buffer, offset, value_, parents, None)
    finally:
        parents.pop()

    return offset


def __setattr__(self, name, value):
    # get the attribute to raise an exception if invalid name
    getattr(self, name)
    object.__setattr__(self, name, value)
