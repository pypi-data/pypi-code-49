import pandas as pd
import sys
import numpy as np


"""
Created on 9 feburary 2020 
Part of data analytics assignment at Thapar Universty Thapar
@author Kunal Bajaj
@rollno 101703297
"""
def read_file(input_file):
    try:
        return pd.read_csv(input_file)
    except IOError:
        raise Exception("Data file doesn't exist\n")
removed_outliers=[]
def remove_outliers():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    df = read_file(input_file)
    data = pd.DataFrame(df.iloc[:, :-1].values)
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    mean=data.mean(axis=0,skipna=True)
    std=data.std(axis=0,skipna=True)
    for col in data.columns:
        for row in range(len(data.index)):
            if (((data.iloc[row, col]) < (q1[col] - 1.5 * iqr[col])) or (
                    (data.iloc[row, col]) > (q3[col] + 1.5 * iqr[col]))) :
                removed_outliers.append(row)
                continue
            z_score=(data.iloc[row,col]-mean[col])/std[col]
            if z_score>3:
                removed_outliers.append(row)
    print('The number of rows removed:', len(removed_outliers))
    for i in reversed(removed_outliers):
        if i<len(df.index):
            df.drop(df.index[i],inplace = True)

    df.to_csv(output_file, index=False)
if __name__== '__main__':
    remove_outliers()