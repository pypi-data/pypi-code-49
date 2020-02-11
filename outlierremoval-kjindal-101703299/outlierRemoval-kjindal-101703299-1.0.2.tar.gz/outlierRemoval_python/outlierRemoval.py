# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:14:38 2020

@author: Kunal Jindal
"""


import sys
import pandas as pd
import numpy as np

def remove_outlier(dataset,file="Final.csv"):
    data=pd.read_csv(dataset)
    X=data.iloc[:,:-1].values
    Y=data.iloc[:,-1].values
    numOutliers=0
    outliers=[]
    initialRows=X.shape[0]
    
    for i in range(np.shape(X)[1]):
        temp=[]
        for j in range(np.shape(X)[0]):
            temp.append(X[j][i])
        Q1,Q3=np.percentile(temp,[25,75])
       
        IQR=Q3-Q1
        MIN=Q1-(1.5*IQR)
        MAX=Q3+(1.5*IQR)
        for j in range(0,np.shape(X)[0]):
            if(X[j][i]<MIN or X[j][i]>MAX):
                numOutliers+=1
                outliers.append(j)
                
        X=np.delete(X,outliers,axis=0)
        Y=np.delete(Y,outliers,axis=0)
    
    finalRows=X.shape[0]
    deleted=initialRows - finalRows
    col=list(data.columns)
    
    print('Rows removed={}'.format(deleted))
    
    newdata={}
    j=0
    for i in range(len(col)-1):
        newdata[col[i]]=X[:,j]
        j+=1
        
    newdata[col[len(col)-1]]=Y
    new=pd.DataFrame(newdata)    
    new.to_csv(file,index=False)

def main():
    if len (sys.argv) <2 :
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit (1)
    
    if len(sys.argv)>3:
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit(1)    
    
    file1=sys.argv[1]
    final=""
    if len(sys.argv)==3:
        final=sys.argv[2]
    else:
        final="OutlierRemoved"+file1
        
    if(remove_outlier(file1,final)==None):
        print("Successfully executed")

        
if __name__=='__main__':
   main()
        
        