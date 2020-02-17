"""Module to check or manipulate various types."""
import collections
import six


def is_iterable(obj):
    """Return True if object is iterable, but is not a string."""
    return (isinstance(obj, collections.Iterable) and not
            isinstance(obj, six.string_types))
