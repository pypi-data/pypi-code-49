# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:47:20 2020

@author: Rohan Bawa
"""
import numpy as np
import sys

def remove_outliers(data):
    q1, q3= np.percentile(data,[25,75])
    iqr=q3-q1
    lower_bound = q1 -(1.5 * iqr) 
    upper_bound = q3 +(1.5 * iqr)
    count = 0
    for i in range(len(data)-1,0,-1):
        if data[i]<lower_bound or data[i]>upper_bound:
            data=np.delete(data,i)
            count = count + 1
    return (data,count)
        
def main():
    #Input 
    filename=sys.argv[1]
    try:
        data = np.genfromtxt(filename, delimiter=',')    
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
    
     (data,deleted) = remove_outliers.remove_outliers(data)
    print(len(data))
    filename = sys.argv[2]
    try:
        np.savetxt(filename,data, delimiter=',')
        print("number of rows deleted: ",deleted)    
    except OSError:
        print('cannot open', filename)
        sys.exit(0)