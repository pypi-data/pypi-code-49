#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 01:12:44 2020

@author: diljotsingh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 00:46:37 2020

@author: diljotsingh
"""

# coding: utf-8
import sys
import pandas as pd
import math
import numpy as np
import pandas as pd

class Topsis:
    data = ""
    weights = ""
    impacts = ""
    def __init__(self):
        if (len(sys.argv)<4 ):
            print ("Try This: python topsis.py <InputDataFile> <Weights> <Impacts>")
            print ("Example: python topsis.py myData.csv 1,2,1,1 +,+,-,+ ")
            sys.exit()

        self.data = sys.argv[1]
        self.weights = str(sys.argv[2])
        self.impacts = str(sys.argv[3])
        print ("Example: python topsis.py myData.csv 1,2,1,1 +,+,-,+ ")
        self.topsis()

    def topsis(self):
        print(data)
        file = pd.read_csv(data)
        df = pd.read_csv(data)
        w_list = weights.split(",")
        i_list = impacts.split(",")
        i_list=np.array(i_list)

        w_list = [int(i) for i in w_list]
        sumw=sum(w_list)
        w_list2 = []
        for i in w_list:
            w_list2.append(w_list[i]/sumw)
    
        if(len(df.columns)!=len(w_list)):
            print("Error:Weights are incorrect")
            sys.exit()

        if(len(df.columns)!=len(i_list)):
            print("Error:Impacts are incorrect")
            sys.exit()
    
    
        n=len(df.columns)
        df2=np.array(df)


        ideal_best=[]
        ideal_worst=[]
        for j in range(0,n):
            k = math.sqrt(sum(df2[:,j]*df2[:,j]))
            maxx = 0
            minn = 1 
            for i in range(0,len(df.index)):
                df2[i,j] = (df2[i,j]/k)*w_list2[j]
                if df2[i,j]>maxx:
                    maxx = df2[i,j]
                if df2[i,j]<minn:
                    minn = df2[i,j]
            if i_list[j] == "+":
                ideal_best.append(maxx)
                ideal_worst.append(minn)
            else:
                ideal_best.append(minn)
                ideal_worst.append(maxx)
        
        p = []
        for i in range(0,len(df.index)):
            a = math.sqrt(sum((df2[i]-ideal_worst)*(df2[i]-ideal_worst)))
            b = math.sqrt(sum((df2[i]-ideal_best)*(df2[i]-ideal_best)))
            p.append(a/(a+b))

        print("Best Sample")
        print("Index:"+ str(p.index(max(p))))

Topsis()