# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 19:00:19 2020

@author: eternal_demon
"""

import pandas as pd
import numpy as np
import sys
import csv

def oremover(fileName):
    data = pd.DataFrame(pd.read_csv(fileName))
    rows=len(data.iloc[:,0])        
    #data=data.sort_values(by=rows)
    q1,q3=np.percentile(data,[25,75])
    iqr=q3-q1
    lowbound=q1-(1.5*iqr)
    uppbound=q3+(1.5*iqr)
    
    datanew=[]
    for i in range(0,rows):
        if(data.iloc[i,0]>=lowbound and data.iloc[i,0]<=uppbound):
            datanew=np.append(datanew,data.iloc[i,0])
        
        else:
             continue
    count=len(datanew)
    count=rows-count
    print("Original Data is :")
    print(data.iloc[:,0])
    print("New Data is :")
    print(datanew)
    print("No of Rows removed are ", + count)


