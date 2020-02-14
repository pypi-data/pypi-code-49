# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:10:54 2020

@author: Parteek Sharma
"""
#%%imports
import pandas as pd
import numpy as np
import sys
import datawig
def main():
    filename = sys.argv[1]
    # "E:\Data Analytics (UML002)\projects\project 3\\train.csv"
    # 
    try:
        df = pd.read_csv(filename)  
    except OSError:
        print('cannot open', filename)
        sys.exit(0)



    #%% do the processing

    p = df.columns[df.isnull().any()]
    df_out = pd.DataFrame(0,index = np.arange(len(df)),columns=p)
    
    for tgt in p:
        cells_with_null = df[tgt].isnull()
        cells_without_null = df[tgt].notnull()
        imputer = datawig.SimpleImputer(
            input_columns=df.columns[df.columns != tgt], # column(s) containing information about the column we want to impute
            output_column= tgt, # the column we'd like to impute values for
            output_path = 'imputer_model' # stores model data and metrics
            )
        
        imputer.fit(train_df=df[cells_without_null], num_epochs=15)
        final = imputer.predict(df[cells_with_null])
        df_out[tgt]=final[tgt+'_imputed']
    
        
    df = df.fillna(df_out)
    #%% output
    df.to_csv('output.csv') 
    print("number of missing values replaced: ",df_out.notnull().sum().sum())
    
if __name__=="__main__":
    main()
