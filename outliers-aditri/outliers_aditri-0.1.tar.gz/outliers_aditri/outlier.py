# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:15:28 2020

@author: DELL
"""
# Importing relevant datasets
import pandas as pd
import sys

def find_outlier(data):
    
    if data.shape[0] == 0:
        return print("Error: Empty Dataset")
    lower_bound = list()
    upper_bound = list()
    quant = data.quantile([0.25,0.75],axis=0)
    num_rows = data.shape[0]
    num_cols = data.shape[1]
    for i in range(num_cols):
        q1, q3 = quant.iloc[1,i],quant.iloc[0,i]
        iqr_val = q1 - q3
        l = quant.iloc[0,i]-(1.5*iqr_val)
        u = quant.iloc[1,i]+(1.5*iqr_val)
        lower_bound.append(l)
        upper_bound.append(u)
    
    deleted_rows = list()
    for r in range(num_rows):
        for c in range(num_cols):
            if data.iloc[r,c]<lower_bound[c] or data.iloc[r,c]>upper_bound[c]:
                deleted_rows.append(r)
                #break
    data = data.drop(deleted_rows)    
    print("Total rows deleted are ",len(deleted_rows))
    return data    

def main():
    # Checking proper inputs on command prompt
    if len(sys.argv)!=3:
        print("Incorrect parameters.Input format:python <programName> <InputDataFile> <OutputDataFile>")
        exit(1)
    else:
        # Importing dataset
        data=pd.read_csv(sys.argv[1])

        find_outlier(data).to_csv(sys.argv[2])
        
if __name__ == "__main__":
    main()
        