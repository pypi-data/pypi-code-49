# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:46:23 2020

@author: hp
"""

import pandas as pd
import sys
import numpy as np

def missing_values(file1):
    data=pd.read_csv(file1)
    for i in data.columns:
        sum = 0
        for t in data[i].values :
            if(not np.isnan(t)):
                sum = sum + t
            sum = sum/len(data[i].values)
            for j,k in enumerate(data[i].values):
                if np.isnan(k) :
                    data[i][j] = sum
    data.to_csv("MissingValuesRemoved"+file1,index=False)
    
    




        
def main():
    if(len(sys.argv) != 2):
        print("Usage:-  python test.py Data.csv")
    file1=sys.argv[1]
    if(missing_values(file1)==None):
        print("Successfully executed")
        
        
if __name__=='__main__':
    
   main()
    
    
    