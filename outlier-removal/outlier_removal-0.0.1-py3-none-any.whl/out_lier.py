# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:44:01 2020

@author: DELL
"""

import sys
import numpy as np
import pandas as pd
def main():
    script=sys.argv[0]
    filename=sys.argv[1]
    filename1=sys.argv[2]
    x=pd.read_csv(filename)
    y=x.as_matrix()
    print(y)
    (r,c)=y.shape
    for k in range(0,c):
        a=[]
        for i in range(0,r):
            a.append(y[i][k])
        a.sort()
        '''df=pd.DataFrame(a)'''
        q1=np.quantile(a,q=0.25)
        q3=np.quantile(a,q=0.75)
        iqr=q3-q1
        min1=q1-1.5*iqr
        max1=q3+1.5*iqr
        print(min1)
        print(max1)
        print(q1,q3,iqr)
        for i in range(0,r):
            if (a[i]<int(min1)):
                x.drop(x.index[i])
            if (a[i]>int(max1)):
                x.drop(x.index[i])
    x.to_csv(filename1)
main()
        

