# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:47:20 2020

@author: Rohan Bawa
"""
import numpy as np

def remove_outliers(data)->(np.ndarray,int):
    quantile1, quantile3= np.percentile(data,[25,75])
    iqr=quantile3-quantile1
    lower_bound_val = quantile1 -(1.5 * iqr) 
    upper_bound_val = quantile3 +(1.5 * iqr)
    count = 0
    for i in range(len(data)-1,0,-1):
        if data[i]<lower_bound_val or data[i]>upper_bound_val:
            data=np.delete(data,i)
            count = count + 1
    return (data,count)
        
# return count