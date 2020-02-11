# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:04:52 2020

@author: Nidhi Alipuria
"""


#defining the function
def topsis(data,impact,list_formed):
    #importing the libraries
    import numpy as np
    import math as ms
    
    #converting in the data set
    df=np.array(data)
    
    #taking the values in the matrix
    for i in range(0,len(df[0])):
        for j in range(0,len(df)):
            df[j][i]=df[j][i]*list_formed[i]
    
    #getting the suare root of the sum of square values(column wise)
    summition=[]
    z=0
    for i in range(len(df[0])):
        z=0
        for j in range(len(df)):
            z=z+(df[j][i]**2)#square is taken to work on positve values
    summition.append(ms.sqrt(z))#filling the array by the square root of the value
    
    #normalisation of the values in the given data set in column wise
    for i in range(len(df[0])):
        for j in range (len(df)):
            df[j][i]=float(df[j][i]/(summition[i]));#explicit type casting to float
    
    #V_positive and v_negative values are calculated
    
    v_positive=[]
    v_negative=[]
    
    for i in range(len(df[0])):
        maximum_x=-1;
        minimum_x=1000;
        for j in range(len(df)):
            if(df[j][i]>maximum_x):
                maximum_x=df[j][i]
            elif(df[j][i]<minimum_x):
                minimum_x=df[j][i]
                if(impact[i]=='+'):
                    v_positive.append(maximum_x)
                    v_negative.append(minimum_x)
                else:
                    v_positive.append(minimum_x)
                    v_negative.append(maximum_x)
    
    #s_plus and s_minus values are calculted
    s_plus=[]
    s_minus=[]
    for i in range(len(df)):
        best_option=0
        worst_option=0
        for j in range (len(df[0])):
            best_option=best_option+(df[j][i]-v_positive[j])**2
            worst_option=worst_option+(df[j][i]-v_negative[j])**2
       
        s_plus.append(ms.sqrt(best_option))
        s_minus.append(ms.sqrt(worst_option))
    
    #getting the performance score values
    performance=[]
    for i in range(0,len(s_minus)):
        performance.append((s_minus[i])/(s_plus+s_minus));
    #now sort in descending order means high performed product/option are ranked less
    ranking=sorted(performance,reverse=True)
    ranks=[(ranking.index(k)+1) for k in performance]
    print(ranks)
    

import sys
import pandas as pd
def main():
    print(sys.argv)
    weights=[float(i) for i in sys.argv[2].split(',')]
    data=pd.read_csv(sys.argv[1]).values
    b=sys.argv[3].split(',')
    topsis(data,weights,b)

if __name__=="__main__":
    main()
    
    