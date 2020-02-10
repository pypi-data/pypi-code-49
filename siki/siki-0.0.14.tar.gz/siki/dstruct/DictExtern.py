# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 10, 2018
# Modifi: May 10, 2018


class extdict(dict):

    def intersection(self, setA, setB):
        """
        intersection of two dictionaries with basic datatype
        """
        setC = {}
        for key, value in setA.items():
            if key in setB and setB[key] == value:
                setC[key] = value
        return setC


    def union(self, setA, setB):
        """
        union of two dictionaries with basic datatype
        """
        setC = {}
        for key, value in setA.items():
            setC[key] = value
        for key, value in setB.items():
            setC[key] = value
        return setC


    def remove_sets(self, bigset, subset):
        """
        remove sub set from big set
        """
        bigset_copy = bigset.copy()
        setC = intersection(bigset, subset)
        for key in setC.keys():
            bigset_copy.pop(key)
        setC.clear()
        return bigset_copy


    def findout_subsets(self, bigset, sub_keylist):
        """
        findout sub dictionary of a dictionary with given list of keys.
        """
        output = {}
        for key in sub_keylist:
            if key in bigset.keys():
                output[key] = bigset[key]
        return output


    def extend_list(self, keylist):
        """
        given a list, and extend the list to a dictionary type, with all values are set to None
        """
        output = {}
        for key in keylist:
            output[key] = None
        return output