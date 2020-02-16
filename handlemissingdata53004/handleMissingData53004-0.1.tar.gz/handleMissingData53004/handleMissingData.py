# -*- coding: utf-8 -*-
"""
Ashutosh Rattan (53004)
COE6
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import sys

def handleMissing(filename):
    data=pd.DataFrame(pd.read_csv(filename))
    
    SI=SimpleImputer(missing_values=np.nan,strategy='mean') # strategy can be 
    #assigned mean, median etc. Look the function signature for more info.
    
    data=pd.DataFrame(SI.fit_transform(data))# fit computes the 'strategy' 
    #transform applies it on the data, fit_transform() combines these two steps.
    data.to_csv('dataNew.csv',index=False)
    print("New data is saved to file 'dataNew.csv' in this directory")

#handleMissing("data.csv")
if (__name__ == "__main__"):
    handleMissing(sys.argv[1])