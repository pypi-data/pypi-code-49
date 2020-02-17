# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 00:53:30 2020

@author: nipunn
"""
def guess_and_fill(input_file):
    """
    Function guesses missing values and fills them
    
    Arguments:
        input_file : Name of the file to be used
        
        returns: dataset after filling missing values by guessing
        
        **Note: The first coloumn is considered as index and discarded
    """
    dataset=pd.read_csv(input_file)
    dataset=dataset.iloc[:,1:]
    m=dataset.shape
    #text_trap = io.StringIO()
    #sys.stdout = text_trap
    new_dataset=remove_rows(input_file,False)
    
    for i in range(0,m[1]):
        x=pd.DataFrame()
        for j in range(0,m[1]):
            if j!=i:
                x=x.append(new_dataset.iloc[:,j])
        y=new_dataset.iloc[:,i]
        x=x.T
        regressor=RandomForestRegressor(n_estimators = 100, random_state = 0)
        regressor.fit(x,y)
        
        for k in range(0,m[0]):
            if np.isnan(dataset.iloc[k,i])==True:
                values=np.array(dataset.iloc[k,:])
                values=values.reshape((1,m[1]))
                values=np.delete(values,obj=[i],axis=1)
                index=np.isnan(values)
                values[index]=0
                dataset.iloc[k,i]=regressor.predict(values)
    
    
    #sys.stdout = sys.__stdout__
    print(dataset)
    return dataset


def remove_rows(input_file,p=True):
    """
    Function removes rows with missing values
    
    Arguments:
        1.input_file : Name of the file to be used
        
        2.print(bool,default: True): Print number of rows removed or not
        
        returns: dataset after removing rows with missing values
    
    **Note: The first coloumn is considered as index and discarded
    """
    
    dataset=pd.read_csv(input_file)
    dataset=dataset.iloc[:,1:]
    m=dataset.shape
    
    rows=[]
    for i in range(0,m[0]):
        for j in range(0,m[1]):
            if np.isnan(dataset.iloc[i,j])==True and i not in rows:
                rows.append(i)
                
                
    new_dataset=pd.DataFrame()
    
    for i in range(0,m[0]):
        if i not in rows:
            new_dataset=new_dataset.append(dataset.iloc[i,:])
    if p==True:        
        print(str(len(rows)) + ' rows removed')
    return new_dataset


def replace_rows(input_file,method='backforth'):
    """
    Function return dataframe after filling missing values in given file
    by choosen method.
    
    It requires following arguments:
    
    1. input_file : Name of the file    
    
    2. method (Default: backforth): method to fill the missing values
        
        a. mean : takes mean of the coloumn and fills the missing value
        b. mode : takes mode of the coloumn and fills the missing value
        c. median : takes median of the coloumn and fills the missing value
        d. asprevious : fills the value same as previous (remains missing if no value is at previous)
        e. asforward : fills the value same as forward (remains missing if no value is at forward)
        f. backforth : fills the value as mean of forward and backward value (chooses forward value if no backward value is present and vice versa)
    
    returns: dataset after filling missing values by chosen method
    
    **Note: The first coloumn is considered as index and discarded
    """
    
    
    dataset=pd.read_csv(input_file)
    dataset=dataset.iloc[:,1:]
    m=dataset.shape
    result=[]
    error=[]
    
    if method=='mean':
        for j in range(0,m[1]):
            values=[]
            for i in range(0,m[0]):
                if np.isnan(dataset.iloc[i,j])==False:
                    values.append(dataset.iloc[i,j])
            result.append(np.mean(values))
    
        for i in range(0,m[0]):
            for j in range(0,m[1]):
                if np.isnan(dataset.iloc[i,j])==True:
                    dataset.iloc[i,j]=result[j]
                
    
    
    
    if method=='mode':
        for j in range(0,m[1]):
            values=[]
            for i in range(0,m[0]):
                if np.isnan(dataset.iloc[i,j])==False:
                    values.append(dataset.iloc[i,j])
            try:
                result.append(st.mode(values))
            except ValueError:
                error.append(j)
                print("Many items of same frquency for coloumn"+str(j)+ ",mode cannot be calculated")
                
        for i in range(0,m[0]):
            for j in range(0,m[1]):
                if np.isnan(dataset.iloc[i,j])==True and j not in error:
                    dataset.iloc[i,j]=result[j]        
        
        if len(error)>0:
            print('Values for Coloumn ',error[0],end=' ')
            for i in range(1,len(error)):
                print(',',error[i],end=' ')
            print('not replaced')
        
    if method=='median':
        for j in range(0,m[1]):
            values=[]
            for i in range(0,m[0]):
                if np.isnan(dataset.iloc[i,j])==False:
                    values.append(dataset.iloc[i,j])
            result.append(np.median(values))
            
        for i in range(0,m[0]):
            for j in range(0,m[1]):
                if np.isnan(dataset.iloc[i,j])==True:
                    dataset.iloc[i,j]=result[j]
    
    if method=='asprevious':
        for i in range(0,m[0]):
            for j in range(0,m[1]):
                if np.isnan(dataset.iloc[i,j])==True:
                    if i-1>=0:
                        dataset.iloc[i,j]=dataset.iloc[i-1,j]
    
    if method=='asforward':
        for i in range(m[0]-1,-1,-1):
            for j in range(0,m[1]):
                if np.isnan(dataset.iloc[i,j])==True:
                    if i+1<m[0]:
                        dataset.iloc[i,j]=dataset.iloc[i+1,j]
    
    if method=='backforth':
        for i in range(0,m[0]):
            for j in range(0,m[1]):
                if np.isnan(dataset.iloc[i,j])==True:
                    if i-1>=0 and i+1<m[0]:
                        dataset.iloc[i,j]=(dataset.iloc[i-1,j]+dataset.iloc[i+1,j])/2
                    elif i+1<m[0]:
                        dataset.iloc[i,j]=dataset.iloc[i+1,j]
                    elif i-1>=0:
                        dataset.iloc[i,j]=dataset.iloc[i-1,j]
    
    
    
    print(dataset)
    return dataset

import numpy as np
import pandas as pd
import statistics as st
import sys
from sklearn.ensemble import RandomForestRegressor 


if __name__ == "__main__":
    if len(sys.argv)>1:
        guess_and_fill(sys.argv[1])
        


