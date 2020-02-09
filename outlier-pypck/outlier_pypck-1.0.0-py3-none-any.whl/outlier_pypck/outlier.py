import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import sys


def z_score(data_z):
    z = np.abs(stats.zscore(data_z))
    data_z= data_z[(z < 3).all(axis=1)]
    data_z.to_csv("output.csv", index=False)
    return len(data_z)

def IQR(data_iqr):
    Q1 =data_iqr.quantile(0.25)
    Q3 = data_iqr.quantile(0.75)
    IQR = Q3 - Q1
    data_out = data_iqr[~((data_iqr < (Q1 - 1.5 * IQR)) |(data_iqr> (Q3 + 1.5 * IQR))).any(axis=1)]
    data_out.to_csv("output.csv", index=False)
    return len(data_out)

def outlier(filename,method):
	d =pd.read_csv(filename)
	x = d.iloc[:,:-1]
	data= pd.DataFrame(x)
	val=0
	if(method=="z_score"):
	    val=z_score(data)
	elif(method=="IQR"):
	    val=IQR(data)

	if(val==0):
	    print("Please enter a valid method.(z_score or IQR)")
	else:
	    diff=len(data)-val
	    print("Number of rows removed = "+str(diff))


def main():	
	outlier(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()

		



