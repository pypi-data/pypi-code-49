import numpy as np
import pandas as pd

def outlier_nishant(incsv_file, outcsv_file):

    dset = pd.read_csv(incsv_file)
    
    Q1 = dset.quantile(0.25)
    Q3 = dset.quantile(0.75)
    
    IQR = Q3 - Q1
    
    new_dataset = dset[((dset >= (Q1 - 1.5 * IQR)) &(dset <= (Q3 + 1.5 * IQR))).all(axis=1)]
            
    new_dataset.to_csv(outcsv_file, index=False)
    print('The no of rows removed:',len(dset) - len(new_dataset))