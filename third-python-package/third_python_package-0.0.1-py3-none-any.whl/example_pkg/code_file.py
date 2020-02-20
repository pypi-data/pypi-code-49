#importing libraries
import numpy as np
import pandas as pd

#defining record deletion function
def record_deletion(in_file, out_file):
    dataset = pd.read_csv(in_file)
    dataset = dataset.apply(pd.to_numeric, errors='coerce')
    new_dataset = dataset.dropna()
    new_dataset.to_csv(out_file, index=False)
    
#defining record replacement function
def record_replacement(in_file, out_file):
    dataset = pd.read_csv(in_file)
    dataset = dataset.apply(pd.to_numeric, errors='coerce')
    new_dataset = dataset.fillna(dataset.mean())
    new_dataset.to_csv(out_file, index=False)
