# -*- coding: utf-8 -*-
"""
    Created on sun Feb 16 14:39:30 2020
    
    @author: simran kaur
    """
#importing libraries
import numpy as np
import pandas as pd
import sys
import datawig

def missing(data):

    if data.shape[0]==0:
        return print("empty dataset")
    col_null=data.columns[data.isnull().any()]
    data_out=pd.DataFrame(0,index=np.arange(len(data)),columns=col_null)
    pstatement=[]
    for nul_col in col_null:
        cnull=data[nul_col].isnull()
        cwnull=data[nul_col].notnull()
        imputer=datawig.SimpleImputer(data.columns[data.columns!=nul_col],nul_col,'imputer_model')
        imputer.fit(data[cwnull])
        final=imputer.predict(data[cnull])
        data_out[nul_col]=final[nul_col+'_imputed']
        pstatement.append("number of missing values replaced in "+ str(nul_col) + " is "+ str(final.shape[0]))

data = data.fillna(data_out)
print("\n\n\n")
for i in pstatement:
    print("\n",i)
    return data

def main():
    if len(sys.argv)!=2:
        print("Incorrect parameters.Input format:python <programName> <InputDataFile> <OutputDataFile>")
        exit(1)
    else:
        data=pd.read_csv(sys.argv[1])
        
        missing(data).to_csv(sys.argv[1])

if __name__ == "__main__":
    main()

