import numpy as np
import pandas as pd
import sys

def fix_miss(data):
    if data.shape[0] == 0:
        return print("Error! Empty Dataset")
    r,c=data.shape
    cn=0
    for i in range(r):
        for j in range(c):
            if(np.isnan(data.iloc[i,j])):
                data.iloc[i,j]=np.mean(data)[j]
                cn=cn+1
    print("Total number of missing values fixed: ",cn)
    return data    

def main():
    if len(sys.argv)!=3:
        print("Incorrect input! Input Format: python missing.py <inputFile> <outputFile>")
        exit(1)
    else:
        data=pd.read_csv(sys.argv[1])
        fix_miss(data).to_csv(sys.argv[2], index=False)

if __name__ == "__main__":
    main()