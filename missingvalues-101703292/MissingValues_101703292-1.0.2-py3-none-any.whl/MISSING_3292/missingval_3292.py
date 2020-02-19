import pandas as pd
import sys
import numpy as np

if(len(sys.argv) != 2):
    print("Usage:-  python test.py Data.csv")
else:
    try:
        data = pd.read_csv(sys.argv[1])

        for i in data.columns:
            sum = 0
            for t in data[i].values :
                if(not np.isnan(t)):
                    sum = sum + t
            sum = sum/len(data[i].values)
            for j,k in enumerate(data[i].values):
                if np.isnan(k) :
                    data[i][j] = sum
        print("REPLACED MISSING VALUES WITH MEAN")
        print(data.to_string())
    except:
        print("Your dataset should not have categorical data")

