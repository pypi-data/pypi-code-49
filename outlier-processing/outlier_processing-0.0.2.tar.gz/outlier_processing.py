# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:03:00 2020

@author: kbansal_be17
"""

import numpy as np
import pandas as pd

def outlier_goback(dataset,threshold=1.4):
    #dataset=pd.read_csv(file)
    nrows=dataset.shape[0]
    ncol=dataset.shape[1]
    #indexes=[]
    count=0
    for i in range(1,ncol):
        mean=dataset.mean(axis=0)[i]
        std=dataset.std(axis=0)[i]
        for j in range(nrows-1,-1,-1):
            if (abs(dataset.iloc[j][i]-mean))/std > threshold:
                #indexes.append(j)
                dataset.drop(dataset.index[j],inplace=True)
                nrows-=1
                count+=1
        #print(indexes)
    print("Records with outliers: ", count)
            
def main():
    file=pd.read_csv(input("Dataframe: "))
    outlier_goback(file)



