# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:46:59 2020

@author: Kunal Jindal
"""

import numpy as np
import pandas as pd
import sys
from sklearn.impute import SimpleImputer

def missing(dataset):
    if dataset.shape[0]==0:
        return print("empty dataset")
    else:
        X=dataset.iloc[:,0:3].values
        imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
        imputer = imputer.fit(X[:, 0:3])
        X[:,0:3 ] = imputer.fit_transform(X[:, 0:3]) 
        file={'a':X[:,0],'b':X[:,1],'c':X[:,2]}
        df=pd.DataFrame(file)
        df.to_csv('output.csv', index=False)

def main():
    if len (sys.argv) <2 :
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit (1)
    
    if len(sys.argv)>3:
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit(1)
    else:
        data=pd.read_csv(sys.argv[1]) 
        missing(data)

if __name__ == "__main__":
    main()
