# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 19:00:19 2020

@author: eternal_demon
"""

import pandas as pd
import numpy as np

def oremover(data):
    
    data=np.array(data)
    rows=len(data)
    count=0
    #data=data.sort_values(by=rows)
    q1,q3=np.percentile(data,[25,75])
    iqr=q3-q1
    lowbound=q1-(1.5*iqr)
    uppbound=q3+(1.5*iqr)
    
    j=0
    datanew=np.array([])
    for i in range(rows):
        if(data[i]>=lowbound and data[i]<=uppbound):
            datanew=np.append(datanew,data[i])
            count=count+1
            j=j+1

        else:
             continue
    count=rows-count
    print(datanew)
    print(count)
    