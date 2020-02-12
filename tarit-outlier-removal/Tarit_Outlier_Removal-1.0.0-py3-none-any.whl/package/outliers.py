# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:21:35 2020

@author: Tarit
"""
import pandas as pd
import numpy as np
import sys

def remove_outliers(datafile,outfile):

    data=pd.read_csv(datafile)
    rows,cols=data.shape
    ds=data.values
    
    rem=[]
    for i in range(0,cols):
        tcol=[]
        for num in range(0,rows):
            tcol.append(ds[num][i])
        tcol.sort()
        q25,q75=np.percentile(tcol,[25,75])
        inter=q75-q25
        upper=q75+(inter*1.5)
        lower=q25-(inter*1.5)
        for num in range(0,rows):
            if(ds[num][i]>upper or ds[num][i]<lower):
                rem.append(num)
    
    rem1=list(set(rem))
    data=data.drop(rem1)
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
    remove_outliers(datafile,outfile)

       
if __name__=='__main__':  
   main()