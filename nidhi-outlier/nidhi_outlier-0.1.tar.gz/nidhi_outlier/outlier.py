# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:48:43 2020

@author: Nidhi Alipuria
"""
#importing the library
import pandas as pd
import numpy as np

def remove_outlier(received_csv_file,out_csv_file):
    
    #reding the input file recived from the user
    data=pd.read_csv(received_csv_file)
    
    #extracting entire rows of a column
    df=data.iloc[:,1:]
    
    for i,row in df.iterrows():
        
        #defining threshhold value
        threshold=3
        
        #calculating the mean_of_the_values
        mean_of_the_values=np.mean(row)
        
        #calculating the standard deviation
        standard_deviation=np.std(row)
        
        #iteration over each row
        for val in row:
            Z_value=(val-mean_of_the_values)/(standard_deviation)
           
            #if absolute(positive value) is greater than threshold value then we will drop that row
            if(np.abs(Z_value)>threshold):
                data=data.drop(df.index[i])
                
            
    #saving the calculted result back into data set named as out_csv_file
    data.to_csv(out_csv_file,index=False)
    t=len(df)-len(data)
    print("rows removed from the received from the original file :",t)     
import sys 

def main():
    dataset=pd.read_csv(sys.argv[1]).values
    newdataset=sys.argv[2]
    remove_outlier(dataset,newdataset)
    
if __name__=="__main__":
     main()