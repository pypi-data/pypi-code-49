# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:41:57 2020

@author: eternal_demon
"""

import pandas as pd
import outlier_remover as ore


data=pd.read_csv('data.csv')
ore.oremover(data)
    
