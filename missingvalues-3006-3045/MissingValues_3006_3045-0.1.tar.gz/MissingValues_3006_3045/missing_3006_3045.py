# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:08:44 2020

@author: aarus
"""
import numpy as np
import pandas as pd
import sys

from sklearn.impute import SimpleImputer

def missing(inputFile,outputfile):
    
    try:
        data=pd.read_csv(inputFile) 
    except FileNotFoundError:
        raise Exception("File does not exist")
        
    head=data.columns
    columns_null=data.columns[data.isnull().any()] #looking for columns having null values
    print("Columns having null values are-",columns_null)
    for i in columns_null:
        null_cells=data[i].isnull()
        count=sum(null_cells)
        print(i," has ",count," missing values")
    imputer=SimpleImputer(strategy='median') 
    #https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
    imputer.fit_transform(data)  #fitting and transforming
    data=pd.DataFrame(imputer.transform(data))  #making dataframe
    data.columns=head  #giving names to the columns as in main dataset
    data.to_csv(outputfile,index=False)
    print("missing values are successfully handled in the output file entered by you")

if(len(sys.argv)<3):
	    raise Exception("Less inputs given")

if(len(sys.argv)>3):
	    raise Exception("More inputs given")
argList=sys.argv  #picking values from command line
infile=argList[1]   #input file
outfile=argList[2]  #output file
missing(infile,outfile) #calling function