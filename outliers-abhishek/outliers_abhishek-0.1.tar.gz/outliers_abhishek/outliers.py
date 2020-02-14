# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:59:30 2020

@author: gogoa_000
"""

import pandas as pd
import sys

def outliers(data):
    
    if data.shape[0]==0:
        return print("empty dataset")
    lbound=[]
    ubound=[]
    quant=data.quantile([.25,.75],axis=0)
    for i in range(data.shape[1]):
        iqr_val=quant.iloc[1,i]-quant.iloc[0,i]
        lbound.append(quant.iloc[0,i]-(1.5*iqr_val))
        ubound.append(quant.iloc[1,i]+(1.5*iqr_val))
    
    row_delete=[]
    for r in range(data.shape[0]):
        for c in range(data.shape[1]):
            if data.iloc[r,c]<lbound[c] or data.iloc[r,c]>ubound[c]:
                row_delete.append(r)
                break
    data=data.drop(row_delete)    
    print("Total rows deleted are ",len(row_delete))
    return data    

def main():
    # Checking proper inputs on command prompt
    if len(sys.argv)!=3:
        print("Incorrect parameters.Input format:python <programName> <InputDataFile> <OutputDataFile>")
        exit(1)
    else:
        # Importing dataset
        data=pd.read_csv(sys.argv[1])

        outlier(data).to_csv(sys.argv[2])
        
if __name__ == "__main__":
    main()