# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:38:16 2020

@author: admin
"""

import pandas as pd
import sys


def remMV():
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
    return;
