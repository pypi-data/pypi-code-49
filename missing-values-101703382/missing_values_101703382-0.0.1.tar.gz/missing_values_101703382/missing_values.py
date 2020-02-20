# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:02:55 2020

@author: Paras Arora
"""
import pandas as pd
import sys
import numpy as np
from sklearn.impute import SimpleImputer
def missing_values(df,newdataset):
    dataset=pd.read_csv(df)
    head=dataset.columns
    cols_null=dataset.columns[dataset.isnull().any()] 
    print("Columns having null values are-",cols_null)
    for target in cols_null:
        null_cells=dataset[target].isnull()
        count=sum(null_cells)
        print(target," has ",count," missing values")
    imputer=SimpleImputer(strategy='mean') #can also change
    imputer.fit_transform(dataset)  #fitting and transforming
    data=pd.DataFrame(imputer.transform(dataset))  #make a dataframe
    data.columns=head  #giving the same names to the columns as in main dataset
    data.to_csv(newdataset)
    print("New file generated")
    

argList=sys.argv  #picking values from command line
df=argList[1]   #input file
newdataset=argList[2]  #output file
missing_values(df,newdataset) #calling function