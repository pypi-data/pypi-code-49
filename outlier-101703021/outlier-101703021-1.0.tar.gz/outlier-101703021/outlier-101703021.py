import pandas as pd
import numpy as np
import sys

if len (sys.argv) != 2 :
    print("Usage: python outlier.py data.csv")
    sys.exit(1)

file_name = sys.argv[1].strip()

def remove_outlier(file_name):
    data = pd.read_csv(file_name).values.tolist()
    
    outliers = list()
    mean = np.mean(data)
    std = np.std(data)
      
    for i in data:
        z = (i[0] - mean)/std
        
        if np.abs(z)>3:
            outliers.append(i[0])
            data.remove(i)
    print('Number of rows removed', len(outliers))
    
remove_outlier(file_name)