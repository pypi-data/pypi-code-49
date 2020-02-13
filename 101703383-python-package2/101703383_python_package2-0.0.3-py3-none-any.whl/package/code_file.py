#importing libraries
import numpy as np
import pandas as pd

def outliers_removal(in_file, out_file):
    
    dataset = pd.read_csv(in_file)
    
    #calculating 25th and 75th percentile
    Q1 = dataset.quantile(0.25)
    Q3 = dataset.quantile(0.75)
    
    #calculating Inter Quartile range
    IQR = Q3 - Q1
    
    new_dataset = dataset[((dataset >= (Q1 - 1.5 * IQR)) &(dataset <= (Q3 + 1.5 * IQR))).all(axis=1)]
    
    new_dataset.to_csv(out_file, index=False)
    print('The no of rows removed:',len(dataset) - len(new_dataset))
