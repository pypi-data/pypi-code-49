#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" general_util.py: General functions module """

import itertools as iter
import collections


def combinations_from_nested_lists(lst):
    """
    Generates tuples with combinations of one element of each list inside the first list.
    :param lst: the list to combine.
    """

    def helper(lst_):
        """
        Helps by allowing it's recursive use to generate a correctly shaped list to iter.product
        """
        if not any(isinstance(e, list) for e in lst_):
            lst_new.append(lst_)
        else:
            for z in lst_:
                if isinstance(z, list):
                    helper(z)
                else:
                    lst_new.append([z])

    if not any(isinstance(w, list) for w in lst):
        for g in lst:
            yield [g]
    else:
        lst_new = []
        for j in lst:
            if isinstance(j, list):
                helper(j)
            else:
                lst_new.append([j])
        lst = lst_new
        for i in iter.product(*lst):
            yield i


def flatten_irregular_nested_lists(l):
    """
    Flattens lists with sublists inside. sublists can be of multiple nesting levels.
    :param l: list to flatten
    """
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten_irregular_nested_lists(el)
        else:
            yield el


def e_value_normalizer(e_value_raw, k, n_celltypes):
    """
    Normalizes the e-value due to disparity in number of celltypes

    :param e_value_raw: value to normalize
    :param int k: number of rows, in practice it's the number of regulatory elements that give the VEnCode.
    :param int n_celltypes: Number of celltypes in the data (columns)
    :return: normalized e-value
    """
    coefs = {"a": -164054.1, "b": 0.9998811, "c": 0.000006088948, "d": 1.00051, "m": 0.9527, "e": -0.1131}
    e_value_expected = (coefs["m"] * k + coefs["e"]) * n_celltypes ** (
        coefs["d"] + ((coefs["a"] - coefs["d"]) / (1 + (k / coefs["c"]) ** coefs["b"])))
    e_value_norm = (e_value_raw / e_value_expected) * 100
    if e_value_norm < 100:
        return e_value_norm
    else:
        return 100


def subset_of_range(range1, range2):
    """ Asks whether range1 is a subset of range2. Returns True or False respectively. """
    if not range1:
        raise ValueError("{} is empty".format(range1))
    if not range2:
        raise ValueError("{} is empty".format(range2))
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2


def partial_subset_of_range(range1, range2):
    """ Asks whether range1 is a subset of range2. Returns True or False respectively. """
    if not range1:
        raise ValueError("{} is empty".format(range1))
    if not range2:
        raise ValueError("{} is empty".format(range2))
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 or range1[-1] in range2


def subset_of_span(span1, span2):
    """ Asks whether span1 is a subset of span2, or vice versa. Returns True or False. """
    if not span1:
        raise ValueError("{} is empty".format(span1))
    if not span2:
        raise ValueError("{} is empty".format(span2))
    span1_sub_span2 = (span2[0] <= span1[0] <= span2[1]) and (span2[0] <= span1[1] <= span2[1])
    condition = span1_sub_span2 or ((span1[0] <= span2[0] <= span1[1]) and (span1[0] <= span2[1] <= span1[1]))
    return condition


def partial_subset_of_span(span1, span2):
    """ Asks whether span1 is a subset of span2, or vice versa. Returns True or False. """
    if not span1:
        raise ValueError("{} is empty".format(span1))
    if not span2:
        raise ValueError("{} is empty".format(span2))
    span1_sub_span2 = (span2[0] <= span1[0] <= span2[1]) or (span2[0] <= span1[1] <= span2[1])
    condition = span1_sub_span2 or ((span1[0] <= span2[0] <= span1[1]) or (span1[0] <= span2[1] <= span1[1]))
    return condition


def clean_whitespaces(df, *cols):
    """
    Removes all whitespaces from items in one or more pd.Dataframe columns.
    :param df: the Dataframe
    :param cols: the columns to remove whitespaces
    """
    for col in cols:
        df[col] = df[col].str.replace(" ", "")


def str_replace_multi(str_, chars):
    """
    replaces many chars in a string.
    :param str_: string to apply replacements
    :param chars: dict in the form {old char: new char, ...}
    """
    for old, new in chars.items():
        str_ = str_.replace(old, new)
    return str_

