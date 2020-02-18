# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:07:57 2020

@author: Jerry
"""
import numpy as np
def safeDivide(a,b, zero_fill = np.nan):
    if len(np.shape(a)) == 0 and len(np.shape(b)) == 0:
        result = zero_fill if abs(b) < 1e-10 else a / b
    elif len(np.shape(a)) == 0 and len(np.shape(b)) != 0:
        result = zero_fill*np.ones(b.shape)
        non_zero_indices = b<1e-10
        result[non_zero_indices] = a / b[non_zero_indices]
    elif len(np.shape(a)) != 0 and len(np.shape(b)) == 0:
        result = zero_fill*np.ones(a.shape) if abs(b)<1e-10 else a/b
    else:
        result = zero_fill*np.ones(a.shape)
        # print(result.shape)
        # non_zero_indices = b!=0
        non_zero_indices = b<1e-10
        # print(result.shape)
        result[non_zero_indices] = a[non_zero_indices] / b[non_zero_indices]
    # result[non_zero_indices] = np.divide(a[non_zero_indices], b[non_zero_indices])
    return result