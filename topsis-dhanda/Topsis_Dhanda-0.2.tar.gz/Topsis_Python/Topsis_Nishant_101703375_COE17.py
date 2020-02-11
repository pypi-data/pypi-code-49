# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:06:10 2020

@author: Nishant
"""

import pandas as pd
import numpy as np
import math
import sys

def topsis(argumentlist):
    dataset=pd.read_csv(argumentlist[0])
    dataset=dataset.iloc[:,1:]
    
    for column in dataset:
        x_denominator=math.sqrt(sum(x*x for x in dataset[column]))
        dataset[column]=dataset[column]/x_denominator
    
    weights=list(map(int,argumentlist[1].split(',')))
    weights_per=[float(x)/sum(weights) for x in weights]
    
    t=0
    for column in dataset:
        dataset[column]=dataset[column]*weights_per[t]
        t=t+1
    
    impact=list(argumentlist[2].split(','))
    
    V_pos=[]
    V_neg=[]
    
    i=0
    for column in dataset:
        if impact[i]=='+':
            V_pos.append(max(dataset[column]))
            V_neg.append(min(dataset[column]))
        else :
            V_pos.append(min(dataset[column]))
            V_neg.append(max(dataset[column]))
        i=i+1
        
    p_score={}
    
    for rows in dataset.itertuples(index=False):
        i=0
        eucdist_pos=0
        eucdist_neg=0
        for x in rows:
            eucdist_pos=eucdist_pos+(x-V_pos[i])*(x-V_pos[i])
            eucdist_neg=eucdist_neg+(x-V_neg[i])*(x-V_neg[i])
            i=i+1
        eucdist_pos=math.sqrt(eucdist_pos)
        eucdist_neg=math.sqrt(eucdist_neg)
        p_score[rows]=eucdist_neg/(eucdist_pos+eucdist_neg)
        
    a=list(p_score.values())
    b=sorted(list(p_score.values()),reverse=True)


    ranked_scores=dict()
    for i in range(len(a)):
        ranked_scores[(b.index(a[i]))+1]=a[i]
        b[b.index(a[i])]=-b[b.index(a[i])]


    row_number=list(i+1 for i in range(len(b)))
    a=list(ranked_scores.values())
    rank=list(ranked_scores.keys())
    
    out={'Row Number':row_number, 'Performance Score':a, 'Rank':rank}
    
    output=pd.DataFrame(out)
    print(output)
    
    
        
if __name__ == "__main__":
    sysarglist = sys.argv
    sysarglist.pop(0)
    topsis(sysarglist)
    
    