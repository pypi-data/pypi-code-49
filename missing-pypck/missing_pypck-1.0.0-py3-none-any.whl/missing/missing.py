import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys


def drop(data,method):
    if(method=='dropr'):
        data.dropna(axis=0,inplace=True)
    else:
        data.dropna(axis=1,inplace=True)        
    return data

def missing(data,method):
   # data=pd.read_csv(filename)
    for col in list(set(data.columns) - set(data._get_numeric_data().columns)):
        f = data[col].dropna().mode()[0]
        data[col] = data[col].fillna(value=f)
    
    for col in data._get_numeric_data().columns:
		if method=='mode':
            data[col]=data[col].fillna(value=data[col].mode()[0])      
        elif method=='median':
            data[col]=data[col].fillna(value=data[col].median())
        else:
            data[col]=data[col].fillna(value=data[col].mean())
    return data
 

def handle(filename,m):
	data=pd.read_csv(filename)
	if(m=='dropr' or m=='dropc'):
		data=drop(data,m)
	else:
		data=missing(data,m)
	data.to_csv("output.csv", index=False)

def main():
	handle(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()

		



