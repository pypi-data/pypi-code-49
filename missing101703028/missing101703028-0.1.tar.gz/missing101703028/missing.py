import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import sys

def file(input_file):
    try:
        return pd.read_csv(input_file)
    except IOError:
        raise Exception("Data file doesn't exist\n")

def main():
    filename = sys.argv[1]
    data=file(filename)
    imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
    data=pd.DataFrame(imputer.fit_transform(data))
    data.to_csv('new_data.csv',index=False)
    print("New data is saved to file 'new_data.csv'.")
