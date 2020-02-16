# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:51:47 2020

@author: Anurag Agarwal
"""

import pandas as pd
import numpy as np
import sys
import datawig

def main():
    filename = sys.argv[1]
    try:
        df = pd.read_csv(filename)  
    except OSError:
        print('cannot open', filename)
        sys.exit(0)

    x = df.columns[df.isnull().any()]
    df_out = pd.DataFrame(0,index = np.arange(len(df)),columns=x)
    
    for i in x:
        with_null = df[i].isnull()
        without_null = df[i].notnull()
        imputer = datawig.SimpleImputer(input_columns=df.columns[df.columns != i], 
            output_column= i, 
            output_path = 'imputer_model')
        
        imputer.fit(train_df=df[without_null], num_epochs=15)
        final = imputer.predict(df[with_null])
        df_out[i]=final[i+'_imputed']


    df = df.fillna(df_out)
    df.to_csv('output.csv') 
    print("number of missing values replaced: ",df_out.notnull().sum().sum())
    
if __name__=="__main__":
    main()
