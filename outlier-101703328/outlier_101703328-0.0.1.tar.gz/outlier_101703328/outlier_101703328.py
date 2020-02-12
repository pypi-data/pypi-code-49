import numpy as np
import pandas as pd
import seaborn as sns


def outlier_detection(dataset):
    d = dataset.copy()
    q1 = d.quantile(0.25)
    q3 = d.quantile(0.75)
    iqr = q3-q1
    #print(iqr)
    d = d[~((d<(q1-1.5*iqr))| (d>(q3+1.5*iqr))).any(axis=1)]
    print(d)
    r1 = dataset.shape[0]
    r2 = d.shape[0]
    r = r1-r2
    print('Number of rows removed:'+str(r1-r2))

 
