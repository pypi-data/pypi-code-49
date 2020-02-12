# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:21:25 2020

@author: praty
"""
import numpy as np
import pandas as pd
import sys

def row_deletion(final_dataset, outliers):
    final_dataset=final_dataset.drop(outliers, axis=0)
    return final_dataset
    
def outlier_computation(dataset_):
    limit=3
    col=len(dataset_.columns)
    rows=len(dataset_.index)
    outliers=[]
    
    for i in range(0,col):
        subset=dataset_.iloc[:,i]
        mean_val=np.mean(subset)
        stan_dev=np.std(subset)
        for j in range(0,rows):
            z_score=(subset[j]-mean_val)/stan_dev
            if(np.abs(z_score)>limit):
                if j not in outliers:
                    outliers.append((j))
                
    final_dataset=pd.DataFrame(dataset_)
    final_dataset=row_deletion(final_dataset, outliers)
    print("The number of rows removed is: ",len(outliers))
    return final_dataset
    

def outlier_deletion(input_file,output_file):
    dataset =pd.read_csv(input_file)
    #The 1st column (serial number) is assumed and is removed by default.
    x = dataset.iloc[:,1:]
    dataset_= pd.DataFrame(x)
    final_dataset=outlier_computation(dataset_)
    print("The updated dataset is stored in",output_file,"in the same directory.")
    final_dataset.to_csv(output_file,index=False)
    

def main():	
	outlier_deletion(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()
