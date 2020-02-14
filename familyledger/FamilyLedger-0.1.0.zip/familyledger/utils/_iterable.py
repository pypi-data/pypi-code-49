"""
A module containing utilities for searching and manipulating iterables.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
from operator import attrgetter


def first_true(iterable, default=None, pred=None):
    """Returns the first true value from an iterable or a default value.
    
    Args:
        iterable: any iterable.
        pred: a function returning truthy or falsy.
        default: a default value.
    
    Supplying a function acting as a predicate via the ``pred`` argument will 
    use that function for truth testing. If ``pred`` is None, items in the 
    iterable are directly checked as truthy. If no truthy value is found, a 
    default is returned.
    """
    return next(filter(pred, iterable), default)


def index_or_none(seq, value):
    """Returns the index of a value in an iterable if present, otherwise None.
    
    Args:
        seq: iterable.
        value: value.
    """
    index = next((i for i, item in enumerate(seq) if item == value), None)
    return index


def multisort_by_attribute(inplace, sortspecs):
    """In-place sorts nested attributed sequences by multiple attributes.
    
    Example:
        >>> from collections import namedtuple
        >>> Vehicle = namedtuple('Vehicle', ['make', 'model', 'year', 'owner'])
        >>> car_park = [
        ...     Vehicle('Mercedes', 'F500', 2003, 'longbottom'),
        ...     Vehicle('BMW', 'X3', 2012, 'malfoy'), 
        ...     Vehicle('Maclaren', 'F1', 2003, 'voldemort'),
        ...     Vehicle('Bugatti', 'Veyron', 2009, 'potter')]
        >>> sortspecs = (
        ...     ('year', True),
        ...     ('make', False),
        ...     ('model', False),
        ...     ('owner', False))
        >>> multisort_by_attribute(car_park, sortspecs)
        >>> import pprint
        >>> pp = pprint.PrettyPrinter()
        >>> pp.pprint(car_park)
        [Vehicle(make='BMW', model='X3', year=2012, owner='malfoy'),
         Vehicle(make='Bugatti', model='Veyron', year=2009, owner='potter'),
         Vehicle(make='Maclaren', model='F1', year=2003, owner='voldemort'),
         Vehicle(make='Mercedes', model='F500', year=2003, owner='longbottom')]
    
    Args:
        inplace: iterable containing sequences with one or more attributes.
        sortspecs: tuples of attribute name and a sorting reverse flag.
    """
    for key, is_reverse in reversed(sortspecs):
        inplace.sort(key=attrgetter(key), reverse=is_reverse)
    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
