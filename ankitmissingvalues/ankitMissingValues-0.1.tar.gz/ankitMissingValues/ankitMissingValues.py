# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:39:12 2020

@author: Ankit
"""

import pandas as pd
import numpy as np
import sys
from sklearn.impute import SimpleImputer

def missing_values(inputfile,outputfile):
    dataset=pd.read_csv(inputfile)
    head=dataset.columns
    columns_null=dataset.columns[dataset.isnull().any()] #looking for columns having null values
    print("Columns having null values are-",columns_null)
    for target in columns_null:
        null_cells=dataset[target].isnull()
        count=sum(null_cells)
        print(target," has ",count," missing values")
    imputer=SimpleImputer(strategy='median') #strategy can be changed
    #for learning about SimpleImputer more-https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
    imputer.fit_transform(dataset)  #fitting and transforming
    data=pd.DataFrame(imputer.transform(dataset))  #making dataframe
    data.columns=head  #giving names to the columns as in main dataset
    data.to_csv(outputfile,index=False)
    print("Success")


argList=sys.argv  #picking values from command line
infile=argList[1]   #input file
outfile=argList[2]  #output file
missing_values(infile,outfile) #calling function