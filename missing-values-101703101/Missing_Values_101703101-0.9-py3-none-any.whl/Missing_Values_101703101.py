# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:53:00 2020

@author: Arpit Singla
"""

import pandas as pd
import numpy as np
import datawig
import sys

def missing_values_arpit(incsv_file, outcsv_file):
    try:
        dataset = pd.read_csv(incsv_file)  
    except OSError:
        print('cannot open', incsv_file)
        sys.exit(0)
    
    columns_null=dataset.columns[dataset.isnull().any()]
    dataset_filled=pd.DataFrame(0,index=np.arange(len(dataset)),columns=columns_null)
    missing_value_count=list()
    
    for col in columns_null:
        null_cells=dataset[col].isnull()
        filled_cells=dataset[col].notnull()
        imputer=datawig.SimpleImputer(
                dataset.columns[dataset.columns!=col],
                col,
                'imputer_model') 
        imputer.fit(dataset[filled_cells])
        predicted=imputer.predict(dataset[null_cells])
        dataset_filled[col]=predicted[col+'_imputed']
        missing_value_count.append("number of missing values replaced in "+ str(col) + " is "+ str(predicted.shape[0]))

    dataset = dataset.fillna(dataset_filled)
    dataset.to_csv(outcsv_file)
    
    #print("number of missing values replaced: ",dataset_filled.notnull().sum().sum())
    
    for i in missing_value_count:
        print("\n\n",i)

if __name__ == '__main__':
    print('EXPECTED ARGUMENTS TO BE IN ORDER : python <Program Name> <InputFile.csv> <OutputFile.csv>')
    # runs if and only if it contains atleast inputfile, output file
    if len(sys.argv) == 3:
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        missing_values_arpit(read_file, write_file)
    # report for incorrect order of arguments passed
    else:
        print('PLEASE PASS ARGUMENTS IN ORDER : python <Program Name> <InputFile.csv> <OutputFile.csv>')
