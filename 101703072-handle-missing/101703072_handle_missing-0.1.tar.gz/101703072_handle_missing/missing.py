# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:16:33 2020

@author: Anish
"""

import numpy as np
import pandas as pd
import sys
import datawig

def missing(dataset):
    
    if dataset.shape[0]==0:
        return print("empty dataset")
    columns_with_null_val=dataset.columns[dataset.isnull().any()]
    dataset_filled_val=pd.DataFrame(0,index=np.arange(len(dataset)),columns=columns_with_null_val)
    missing_value_count=list()
    for target in columns_with_null_val:
        null_cells=dataset[target].isnull()
        filled_cells=dataset[target].notnull()
        imputer=datawig.SimpleImputer(dataset.columns[dataset.columns!=target],target,'imputer_model') 
        imputer.fit(dataset[filled_cells])
        predicted=imputer.predict(dataset[null_cells])
        dataset_filled_val[target]=predicted[target+'_imputed']
        missing_value_count.append("number of missing values replaced in "+ str(target) + " is "+ str(predicted.shape[0]))

    dataset = dataset.fillna(dataset_filled_val)  
    for i in missing_value_count:
        print("\n\n",i)
    return dataset    

def main():
    # Checking proper inputs on command prompt
    if len(sys.argv)!=2:
        print("Incorrect parameters.Input format:python <programName> <InputDataFile> <OutputDataFile>")
        exit(1)
    else:
        # Importing dataset
        dataset=pd.read_csv(sys.argv[1])
        missing(dataset).to_csv(sys.argv[1])
        
if __name__ == "__main__":
    main()