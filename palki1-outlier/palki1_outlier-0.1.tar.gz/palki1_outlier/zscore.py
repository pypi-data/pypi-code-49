# -*- coding: utf-8 -*-
"""
Spyder Editor


"""

#importing the library
import pandas as pd
import numpy as np

def z_score(input_file,output_file):
    dataset=pd.read_csv(input_file)
    df=dataset.iloc[:,1:]
    
    for i,row in df.iterrows():
        threshold=3
        mean_value=np.mean(row)
        sd=np.std(row)
        
        for value in row:
            z_score=(value-mean_value)/(sd)
           
            #if absolute(positive value) is greater than threshold value then we will drop that row
            if(np.abs(z_score)>threshold):
                dataset=dataset.drop(df.index[i])
            
    dataset.to_csv(output_file,index=False)
    t=len(df)-len(dataset)
    print("rows removed from the received from the original file :",t)
    
import sys 

def main():
    dataset=pd.read_csv(sys.argv[1]).values
    newdata=sys.argv[2]
    z_score(dataset,newdata)
    
if __name__=="__main__":
     main()