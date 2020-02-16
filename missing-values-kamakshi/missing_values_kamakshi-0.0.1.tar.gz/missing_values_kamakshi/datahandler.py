# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:47:22 2020

@author: kamakshi_behl
"""



import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def datahandler(filename):
    data=pd.DataFrame(pd.read_csv(filename))
    print("Data to be operated is ")
    print(data)
    headerlist=data.columns
    # headerlist.append(data.iloc[0:0,:])
    data_to_be_operated=data.iloc[0:,:]
    #Change the strategy type according to your need out of mean,median,most_frequent and constant
    
    imp=SimpleImputer(missing_values=np.nan,strategy='median')
    imp.fit_transform(data)
    data=pd.DataFrame(imp.transform(data_to_be_operated))
    print("New Data is ")
    print(data)
    data.columns=headerlist
    data.to_csv('data_new.csv',index=False)
    print('New data has been successfully transported to file named data_new.csv')
