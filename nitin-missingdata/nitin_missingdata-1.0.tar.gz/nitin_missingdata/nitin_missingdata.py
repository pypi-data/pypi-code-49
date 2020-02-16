# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 08:22:41 2020

@author: Dell
"""
import pandas as pd
import numpy as np
import datawig
import sys

#defining function to find the missing values 

def nitin_missingdata(dataset):
    
    #checking for empty dataset
    if (dataset.shape[0]==0):
        return print("No data value in the dataset")
    
    #checking for null values in the columns
    nullcolumns= dataset.columns[dataset.isnull().any()]
    #values to be replaced in place of the NaN
    fillingdata=pd.DataFrame(0,index=np.arange(len(dataset)),columns=nullcolumns)
    
    for target in nullcolumns:
      cells_with_null=dataset[target].isnull()
      cells_without_null=dataset[target].notnull()
      
      imputer=datawig.SimpleImputer(
              #columns containing information about the column we want to impute
              input_columns=dataset.columns[dataset.columns!=target],
              #column  for which we have to impute the values 
              output_column=target,
              #stores model data and its metrics
              output_path='imputer_model' 
              )
      #fitting the imputer model with non null columns 
      imputer.fit(train_df=dataset[cells_without_null],num_epochs=15)
      #predicting from the imputer model for the columns with null values 
      predicted=imputer.predict(dataset[cells_with_null])
      
      fillingdata[target]=predicted[target+'_imputed']
     
    
        
    #appending the dataset by replacing the NaN values with the values computed with the help of the imputer model 
    dataset=dataset.fillna(fillingdata)
    
    print("number of missing values replaced: ",fillingdata.notnull().sum().sum())
    
    return dataset

def main():
    #checking inputs given 
    if len(sys.argv)!=2:
        print("Incorrect parameters...Input format:- python <Program_name> <Inputdatafile> <Outputdatafile>")
        exit(1)
    else:
        # import dataset
        dataset=pd.read_csv(sys.argv[1])
        #calling missing values function
        nitin_missingdata(dataset).to_csv(sys.argv[1])
        
if __name__ == "__main__":
    main()
    


    
        
        