# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:46:31 2020

@author: Sunvir
"""

import pandas as pd
import numpy as np
import csv
import sys
def main():
    try:
        file1=open(sys.argv[1],"rb")
        temp=pd.read_csv(file1)
        ds=temp.iloc[:,:].values
        rows,cols=ds.shape
        c=0
        nr=list(temp)
        for i in range(0,cols):
            l=[]
            d=[]
            for j in range(0,ds.shape[0]):
                l.append(ds[j][i])   
            l.sort()
            q1,q3=np.percentile(l,[25,75])
            iqr=q3-q1
            for j in range(0,ds.shape[0]):
                if (ds[j][i]<q1-iqr*1.5) or (ds[j][i]>q3+iqr*1.5):
                    c=c+1
                    d.append(j)
            ds=np.delete(ds,d,axis=0)
           
           
        with open(sys.argv[2],'w',newline='') as f:
                wr = csv.writer(f, dialect='excel')
                wr.writerow(nr)
                np.savetxt(f, ds, delimiter=",")
        f.close()
        print(c,"rows have been deleted")
        print("Open",sys.argv[2],"to check out the new file")
    except:
        if(len(sys.argv)!=3):
            print('ERROR: Please provide two csv files')
        else:
            print('ERROR')

if __name__ == '__main__':
    main()
         
