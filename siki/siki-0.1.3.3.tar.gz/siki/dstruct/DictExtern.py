# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: May 10, 2018
# LastChg: Feb 19, 2020

from siki.basics import Exceptions as excepts


def intersection(setA, setB):
    """
    intersection of two dictionaries with basic datatype
    """
    setC = {}
    for key, value in setA.items():
        if key in setB and setB[key] == value:
            setC[key] = value
    return setC


def union(setA, setB):
    """
    union of two dictionaries with basic datatype
    """
    setC = {}
    for key, value in setA.items():
        setC[key] = value
    for key, value in setB.items():
        setC[key] = value
    return setC


def remove_sets(bigset, subset):
    """
    remove sub set from big set
    """
    bigset_copy = bigset.copy()
    setC = intersection(bigset, subset)
    for key in setC.keys():
        bigset_copy.pop(key)
    setC.clear()
    return bigset_copy


def findout_subsets(bigset, sub_keylist):
    """
    findout sub dictionary of a dictionary with given list of keys.
    """
    output = {}
    for key in sub_keylist:
        if key in bigset.keys():
            output[key] = bigset[key]
    return output


def create_dict_from_keylist(keylist, default=None):
    """
    given a list, and extend the list to a dictionary type, with all values are set to None (default)
    """
    output = {}

    if type(default) is dict:
        raise excepts.InvalidParamException("dict type cannot be set to a new dict value")

    if type(default) is list:
        if len(default) != len(keylist):
            raise excepts.InvalidParamException("default as a list have different length to key list")
        else:
            for i in range(0, len(keylist)):
                output[keylist[i]] = default[i]
            
            # return from two list
            return output
        
    # else, normal cases
    for key in keylist:
        output[key] = default

    # success
    return output


def clear(sets):
    """
    clear all element from a list
    """
    del sets
    sets = {}


if __name__ == "__main__":
    key = ["1", "a", "b", "2", "c"]
    val = [1, 2, 3, 4, 5]

    dict_test = create_dict_from_keylist(key, val)

    print(dict_test)
