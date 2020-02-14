import pandas as pd
import math
import numpy as np
import sys
import os

def remove_outlier(inputFile,outputFile):
    
    try:
        data=pd.read_csv(inputFile) 
    except FileNotFoundError:
        raise Exception("File does not exist")
        
    row_count=data.shape[0]
    col_count=data.shape[1]
    
    original_rows=len(data)
    
    col=list(data.columns)
    for i in range(0,col_count):

        temp=data.sort_values(col[i])
        m=temp.iloc[:,i].values
        row_count=len(m)
        
        Q1=(m[math.floor((row_count+1)/4)] + m[math.ceil((row_count+1)/4)])/2
        Q3=(m[math.floor(3*(row_count+1)/4)] + m[math.ceil(3*(row_count+1)/4)])/2
        IQR=Q3-Q1
        MIN=Q1-1.5*IQR
        MAX=Q3+1.5*IQR
        
        for j in range(0,row_count):
            if(m[j]>MAX or m[j]<MIN):
                data=data.drop([j])
        data.index=np.arange(0,len(data))
        
    now_rows=len(data)
    removed_rows=original_rows-now_rows
    print("No. of rows removed by IQR method: ",removed_rows)
    
    data.to_csv(outputFile,index=False)
        

def main():
	if(len(sys.argv)<3):
	    raise Exception("Less inputs given")

	if(len(sys.argv)>3):
	    raise Exception("More inputs given")

	inputFile=sys.argv[1]
	outputFile=sys.argv[2]

	exists = os.path.isfile(outputFile)
	if exists:
		raise Exception("Output filename already exists")

	remove_outlier(inputFile,outputFile)

if _name_ == "_main_":
	main()
