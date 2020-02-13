#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:19:16 2020

@author: sunishka
"""

import numpy as np
import pandas as pd
import sys

if __name__=='__main__':
    try:
        filename=sys.argv[1]
    except:
        print('Argument missing')
        sys.exit(1)
    try:
        df = pd.read_csv(filename)
        df = df.fillna(df.mode().iloc[0])
    except:
        print('Invalid filename')
        sys.exit(1)
    
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3-q1
p = df.shape[0]
df = df[~((df < (q1-1.5*iqr)) | (df > (q3+1.5*iqr))).any(axis=1)]
print('Rows deleted ', p-df.shape[0])
df.to_csv(filename, sep='\t', encoding='utf-8', index=False)
