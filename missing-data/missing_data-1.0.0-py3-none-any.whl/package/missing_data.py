import pandas as pd
import sys


def missing_data():
    filename = sys.argv[-1]    
    missing_values = ["n/a", "na", "--"]
    dataset = pd.read_csv(filename, na_values = missing_values)
    print("Missing data: ")
    print(dataset.isnull().sum())
    print("Processing data")
    
    dataset = dataset.fillna(dataset.mean())
    print("Missing data: ")
    print(dataset.isnull().sum())
    print(dataset)
    return;
