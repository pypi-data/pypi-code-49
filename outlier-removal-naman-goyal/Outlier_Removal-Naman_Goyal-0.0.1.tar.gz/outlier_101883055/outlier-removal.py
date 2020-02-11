# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:55:40 2020

@author: naman
"""

#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

#Function for outlier removal
def outlier_removal(input_file):
    dataset=pd.read_csv(input_file)
    data=dataset.iloc[:,1:]
    
    for n,row in data.iterrows():
        #Defining threshold value
        threshold_value=2.5
        mean=np.mean(row)
        standard_deviation=np.std(row)
        
        for value in row:
            #Calculating z score
            z_score=(value-mean)/standard_deviation
            
            #Removing rows whose z_score> threshold value
            if np.abs(z_score)>threshold_value:
                dataset = dataset.drop(data.index[n])
    
          
    rows_removed=len(data) -len(dataset)
    return rows_removed


def main():
    import sys
    total = len(sys.argv)
    if (total!=2):
        print("ERROR! WRONG NUMBER OF PARAMETERS")
        print("USAGES: $python <programName> <dataset>")
        print('EXAMPLE: $python programName.py data.csv')
        sys.exit(1)
  #  dataset=pd.read_csv(sys.argv[1]).values
    rr=outlier_removal(sys.argv[1])
    print("Number of rows removed are: ",rr)

if __name__=="__main__":
     main()




