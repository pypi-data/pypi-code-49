import pandas as pd
import numpy as np
import sys

if len (sys.argv) != 2 :
    print("Usage: python outlier.py data.csv")
    sys.exit(1)

file_name = sys.argv[1].strip()

def mean_column(data,column_no):
    x = 0
    c = 0
    for i in range(len(data)):
        if not np.isnan(data[i][column_no]):
            x += data[i][column_no]
            c += 1
    return x/c

def handle_missing(file_name):
    data = pd.read_csv(file_name).values.tolist()
    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if np.isnan(data[i][j]):
                data[i][j] = mean_column(data,j)
                count += 1
    pd.DataFrame(data).to_csv(file_name)
    print('No. of Missing Values Replaced :', count)

handle_missing(file_name)