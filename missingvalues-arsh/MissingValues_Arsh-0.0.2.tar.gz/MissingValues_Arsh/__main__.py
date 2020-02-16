

import pandas as pd
import sys



filename = sys.argv[-1]    
missing_values = ["n/a", "na", "--"]
dataset = pd.read_csv(filename, na_values = missing_values)
print("Missing Values: ")
print(dataset.isnull().sum())
print("Processing")
    
dataset = dataset.fillna(dataset.mean())
print("Missing Values: ")
print(dataset.isnull().sum())
print(dataset)
    
