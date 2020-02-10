# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 10, 2018
# Modifi: May 10, 2018

class extlist(list):
    def intersection(self, setA, setB):
        """
        intersection of two lists with basic datatype
        """
        setC = []
        for item in setA:
            if item in setB:
                setC.append(item)
        return setC


    def union(self, setA, setB):
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


    def remove_sets(self, bigset, subset):
        """
        remove items of subset B from big set
        """
        setC = []
        setC.extend(bigset)
        for item in subset:
            if item in bigset:
                setC.remove(item)
        return setC


    def clear(self, sets):
        """
        clear all element from a list
        """
        del sets
        sets = []


    def clone(self, sets):
        """
        clone a copy of set, return the dumplicated list of set
        """
        _list = list(sets)
        return _list