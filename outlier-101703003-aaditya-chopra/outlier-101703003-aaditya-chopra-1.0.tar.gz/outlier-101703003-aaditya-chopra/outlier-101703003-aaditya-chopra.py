# -*- coding: utf-8 -*-
"""
Created on SAT Feb 8 14:17:26 2020

@author: Aaditya Chopra
"""

import pandas as pd
import argparse

def outlie(file):
    dframe = pd.read_csv(file)
    column = dframe.shape[1]
    for i in range(1,column):
        quee = dframe.iloc[:,i].quantile(0.75)
        que = dframe.iloc[:,i].quantile(0.25)
        IQR = quee - que    
        filter = (dframe.iloc[:,i] >= que - 1.5 * IQR) & (dframe.iloc[:,i] <= quee + 1.5 *IQR)
        dframe=dframe.loc[filter]
    dframe.to_csv('Modified_data.csv') 

def main(): 
    ap = argparse.ArgumentParser(description='Remove Outliers')
    ap.add_argument('-f', '--Filepath', type=str, required=True, default = None, help='filepath of CSV file', dest='filepath')
    args = ap.parse_args()
    outlie(args.filepath)

    
if __name__ == '__main__':
    main()
