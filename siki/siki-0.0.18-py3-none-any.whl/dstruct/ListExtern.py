# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: May 10, 2018
# LastChg: Feb 19, 2020


def intersection(setA, setB):
    """
    intersection of two lists with basic datatype
    """
    setC = []
    for item in setA:
        if item in setB:
            setC.append(item)
    return setC


def union(setA, setB):
    """
    union of two lists with basic datatype
    """
    setC = []
    setC.extend(setA)
    for item in setA:
        if item in setB:
            setB.remove(item)
    setC.extend(setB)
    return setC


def remove_sets(bigset, subset):
    """
    remove items of subset B from big set
    """
    setC = []
    setC.extend(bigset)
    for item in subset:
        if item in bigset:
            setC.remove(item)
    return setC


def clear(sets):
    """
    clear all element from a list
    """
    del sets
    sets = []