# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 08:09:55 2020

@author: Jerry
"""
from utils import safeDivide
import numpy as np
def dice(seg1, seg2):
    seg1 = seg1 > 0
    seg2 = seg2 > 0
    # union = (seg1+seg2)>0
    # intersect = (seg1*seg2)>0
    # return (2*np.sum(seg1*seg2)) / (np.sum(seg1)+np.sum(seg2))
    return safeDivide(2*np.sum(seg1*seg2), np.sum(seg1)+np.sum(seg2))
    

def dicePerSlice(seg1, seg2, sliceDim=0):
    """
    

    Parameters
    ----------
    seg1 : Numpy ndarray
        Should have shape [D, H, W].
    seg2 : Numpy ndarray
        DESCRIPTION.
    sliceDim : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    slc = [slice(None)]*3
    # dices = np.nan*np.ones(seg1.shape[sliceDim])
    dices = np.zeros(seg1.shape[sliceDim])
    for sliceIdx in range(seg1.shape[sliceDim]):
        slc[sliceDim] = slice(sliceIdx,sliceIdx+1)
        dices[sliceIdx] = dice(seg1[tuple(slc)], seg2[tuple(slc)])
        
    return dices