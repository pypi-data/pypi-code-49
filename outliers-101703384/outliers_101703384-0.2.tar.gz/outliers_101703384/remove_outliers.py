# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:47:20 2020

@author: Parteek Sharma
"""
import pandas as pd
import numpy as np
from scipy import stats
import sys

def delete_outliers(ds,z_val=3):
    if ds.ndim>2:
        out_ds = ds[(np.abs(stats.zscore(ds)) < z_val).all(axis=1)]
    else:
        out_ds = ds[(np.abs(stats.zscore(ds)) < z_val)]
    return (out_ds,len(ds)-len(out_ds))            


def main():
    filename = sys.argv[1]
    try:
        data = pd.read_csv(filename)
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
    (data,count) = delete_outliers(data)
    
    try:
        data.to_csv("out.csv",index=False)
        print("number of rows deleted: ",count)    
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
if __name__=="__main__":
    main()