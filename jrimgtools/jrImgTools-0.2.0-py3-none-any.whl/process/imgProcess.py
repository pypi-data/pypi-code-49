# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:38:20 2020

@author: Jerry
"""

from scipy.ndimage.morphology import binary_erosion, generate_binary_structure
def bwperim(BW, dim=3, conn=6):
    # generate_binary_structure and matlab bwperim interpret conn differently
    # Here we keep consist with Matlab function
    # vol = np.bool(vol)    
    BW = BW > 0
    if dim == 2:
        if conn in [4,8]:
            if conn == 4:
                conn = 1
            else:
                conn = 2
    elif dim == 3:
        if conn in [6,18,26]:
            if conn == 6:
                conn = 1
            elif conn == 18:
                conn = 2
            else:
                conn = 3
    # print(dim)
    conn_structure = generate_binary_structure(dim, conn)
    BWErode = binary_erosion(BW, structure=conn_structure)
    BWPeirm = BW ^ BWErode
    return BWPeirm