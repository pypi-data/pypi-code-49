import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys


def dropper(data,method):
    if(method=='dropr'):
        data.dropna(axis=0,inplace=True)
    else:
        data.dropna(axis=1,inplace=True)        
    return data

def missing_data(data,method):
    for colmn in list(set(data.columns)-set(data._get_numeric_data().columns)):
        f=data[colmn].dropna().mode()[0]
        data[colmn] = data[colmn].fillna(value=f)
    
    for colmn in data._get_numeric_data().columns:
		if method=='mode':
            data[colmn]=data[colmn].fillna(value=data[colmn].mode()[0])      
        elif method=='median':
            data[colmn]=data[colmn].fillna(value=data[colmn].median())
        else:
            data[colmn]=data[colmn].fillna(value=data[colmn].mean())
    return data
 
def handler(filename,m):
	data=pd.read_csv(filename)
	if(m=='dropr' or m=='dropc'):
		data=dropper(data,m)
	else:
		data=missing_data(data,m)
	data.to_csv("output.csv", index=False)

def main():
	handler(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()

		



