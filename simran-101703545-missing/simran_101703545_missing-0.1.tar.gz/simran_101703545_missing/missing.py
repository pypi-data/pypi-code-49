import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import sys

def missing_values(inputFile):
    data=pd.DataFrame(pd.read_csv(inputFile))
    headerlist=data.columns
    orig_data=data.iloc[0:,:]
    imp=SimpleImputer(missing_values=np.nan,strategy='median')
    imp.fit_transform(data)
    data=pd.DataFrame(imp.transform(orig_data))
    data.columns=headerlist
    data.to_csv('handled_data.csv',index=False)
    print('Missing values have been replaced by median.\nOpen handled_data.csv to check.')

def main():
    missing_values(sys.argv[1])

if(__name__=="__main__"):
    main()

