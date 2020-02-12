# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 03:12:30 2020

@author: Tanishq Chopra
"""
import pandas as pd
import numpy as np
import sys

def outliers_rem(datafile,outfile):

    data=pd.read_csv(datafile)
    r,c=data.shape
    ds=data.values
    outlier=[]
    for i in range(0,c):
        temp=[]
        for num in range(0,r):
            temp.append(ds[num][i])
        temp.sort()
        q1,q2=np.percentile(temp,[25,75])
        inter=q2-q1
        upper=q2+(inter*1.5)
        lower=q1-(inter*1.5)
        for num in range(0,r):
            if(ds[num][i]>upper or ds[num][i]<lower):
                outlier.append(num)
    
    outlier=list(set(outlier))
    data=data.drop(outlier)
    data.to_csv(outfile,index=False)
    
def main():
    if len (sys.argv) <2 :
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit (1)
   
    if len(sys.argv)>3:
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit(1)    
    cla=sys.argv
    datafile=str(cla[1])
    outfile=str(cla[2])
    outliers_rem(datafile,outfile)

       
if __name__=='__main__':  
   main()