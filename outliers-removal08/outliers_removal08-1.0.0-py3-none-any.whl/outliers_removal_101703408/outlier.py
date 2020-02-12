# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:40:39 2020

@author: pulki
"""
import pandas as pd
import argparse


def outlier(dataset):
    cols = dataset.shape[1]
    for i in range(1,cols):
        Q1 = dataset.iloc[:,i].quantile(0.25)
        Q3 = dataset.iloc[:,i].quantile(0.75)
        IQR = Q3 - Q1    
        filter = (dataset.iloc[:,i] >= Q1 - 1.5 * IQR) & (dataset.iloc[:,i] <= Q3 + 1.5 *IQR)
        dataset=dataset.loc[filter]
        return dataset

def outlie(file):
    dataset = pd.read_csv(file)
    cols = dataset.shape[1]
    for i in range(1,cols):
        Q1 = dataset.iloc[:,i].quantile(0.25)
        Q3 = dataset.iloc[:,i].quantile(0.75)
        IQR = Q3 - Q1    
        filter = (dataset.iloc[:,i] >= Q1 - 1.5 * IQR) & (dataset.iloc[:,i] <= Q3 + 1.5 *IQR)
        dataset=dataset.loc[filter]
    dataset.to_csv('Modified_data.csv') 

def main(): 
    ap = argparse.ArgumentParser(description='Remove Outliers from the data')
    ap.add_argument('-f', '--Filepath', type=str, required=True, default = None, help='filepath of CSV file', dest='filepath')
    args = ap.parse_args()
    outlie(args.filepath)

    
if __name__ == '__main__':
    main()
