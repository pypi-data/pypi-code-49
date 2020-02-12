#!/usr/bin/env python3
# coding: utf-8

import numpy as np


def represent(obj, *args):
    s = ', '.join(repr(x) for x in args)
    return '{}({})'.format(obj.__class__.__name__, s)


def array(a):
    if isinstance(a, np.ndarray):
        return a
    return np.array(a)


_interval_boundaries = {
    '()': 'neither',
    '[]': 'both',
    '[)': 'left',
    '(]': 'right',
}


def interval(*args):
    """
    interval()      ==> (-inf, +inf)
    interval(1)     ==> [1, 1]
    interval(1, 2)  ==> [1, 2]
    interval('()', 1, 2) ==> (1, 2)
    """
    import pandas
    closed = 'both'
    if len(args) == 0:
        lval = -float('inf')
        rval = float('inf')
        closed = 'neither'
    elif len(args) == 1:
        lval = rval = args[0]
    elif len(args) == 2:
        lval, rval = args
        closed = 'both'
    elif len(args) == 3:
        try:
            closed = _interval_boundaries[args[0]]
        except KeyError:
            raise ValueError("boundary must be '[]', '()', '[)' or '(]'")
        lval, rval = args[1:]
    else:
        raise ValueError('wrong number of arguments')
    return pandas.Interval(lval, rval, closed)


# pi / 180.
degree = 0.017453292519943295
