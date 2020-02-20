# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:25:32 2020

@author: Keshav Bansal
"""

import pandas as pd
import numpy as np
#from seaborn import heatmap
def missing_val(file):
    train=pd.read_csv(file)
    r=train.shape[0]
    for i in range(train.shape[1]-1,-1,-1):
        if train.iloc[:,i].value_counts().shape[0] > 0.25*r:
            train.drop(train.columns[i],axis=1,inplace=True)
    c=train.shape[1]
    #heatmap(train.isnull(),yticklabels=False,cbar=False)
    
    col_dict={}
    col=[i for i in range(0,c)]  
    for i in range(0,c):
        count=train.isnull().iloc[:,i].sum()
        if count>0:
            col_dict[count]=i
            
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.linear_model import LinearRegression
    
    for i in sorted(col_dict.keys()):
        x=train.iloc[:,list(set(col)-set(col_dict.values()))]
        target=train.iloc[:,col_dict[i]]
        idx=[j for j in range(target.shape[0]-1,-1,-1) if target.isnull().iloc[j]]
        #x.drop(x.index[idx], inplace=True)
        #target.drop(target.index[idx], inplace=True)
        labelencoder=LabelEncoder()
        cat_cols=list(set(x.columns)-set(x._get_numeric_data().columns))
        for j in cat_cols:
            x[j]=labelencoder.fit_transform(x[j])
    
        onehotencoder=OneHotEncoder(categorical_features=[x.columns.get_loc(j) for j in cat_cols])
        x=onehotencoder.fit_transform(x).toarray()
        x_pred=[x[j] for j in idx]
        for j in idx:
            x=np.delete(x,j,axis=0)
        target.drop(target.index[idx], inplace=True)    
        if type(target.iloc[0])==str:
            dtc=DecisionTreeClassifier()
            dtc.fit(x,target)
            y_pred=dtc.predict(x_pred)
        else:
            regressor=LinearRegression()
            regressor.fit(x,target)
            y_pred=regressor.predict(x_pred)
        
        for j in range(len(idx)):
                train.iat[idx[j],col_dict[i]]=y_pred[j]
                print("[",idx[j],",",col_dict[i],"] = ",y_pred[j])
        del col_dict[i]

def main():
    file=input("Dataframe: ")
    missing_val(file)
        