# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 08, 2018
# Modifi: May 08, 2018


def check_null_params(**dics):
    """
    checking the input parameters, filter out the nulls
    """
    if len(dics) > 0:
        nullkeys = []
        for key, val in dics.items():
            if val is None:
                nullkeys.append(key)
        return len(nullkeys) > 0, nullkeys
    return False, None