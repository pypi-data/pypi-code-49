# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 

@author: ashu
"""
#Made by Ashutosh Gupta 101703118
import numpy as np  #importing necessary libraries
import pandas as pd
import sys
def remove_outliers(infile, outfile):

    dataset = pd.read_csv(infile)  #reading dataset	
    data = dataset.iloc[:,1:]  
    threshold=1.5
    for i, row in data.iterrows():
        mean = np.mean(row)   #calculating mean
        std = np.std(row)       #calculating standard deviation
        for value in row:
            z_score = (value-mean)/std    #calculating z-score
            if np.abs(z_score)>threshold:
                dataset = dataset.drop(data.index[i]) #dropping record
                break
            
    dataset.to_csv(outfile, index=False)     #output to csv
    print ('The number of rows removed:',len(data) - len(dataset)) #printing no. of rows removed


argList=sys.argv  # picking values from command line
infile=argList[1]   #input file
outfile=argList[2]  #output file

remove_outliers(infile,outfile) #calling function

