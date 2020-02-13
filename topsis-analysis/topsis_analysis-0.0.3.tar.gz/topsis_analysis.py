# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:22:23 2020
@author: kbansal_be17
"""

import pandas as pd
import math
import sys
def topsis(file,weights,impacts):
    dataset=pd.read_csv(file)
    nrows=dataset.shape[0]
    ncol=dataset.shape[1]
    if len(weights)!=ncol-1 or len(impacts)!=ncol-1:
        sys.exit("IndexError: list index out of range")
        
    best_sol=[]
    worst_sol=[]
    s_best=[]
    s_worst=[]
    performance_score=[]
    idx=0
    for column in range(1,ncol):
        n=0;
        for row in range(0,nrows):
            n+=dataset.iloc[row][column]**2
        n=math.sqrt(n)
        for row in range(0,nrows):
            dataset.iat[row,column]=(dataset.iloc[row][column]/n)*float(weights[column-1])
        if impacts[column-1]=='+':
            best_sol.append(max(dataset.iloc[1:,column]))
            worst_sol.append(min(dataset.iloc[1:,column]))
        elif impacts[column-1]=='-':
            worst_sol.append(max(dataset.iloc[1:,column]))
            best_sol.append(min(dataset.iloc[1:,column]))
        else:
            sys.exit("Impact value should be either '+' or '-'")
    for row in range(0,nrows):
        s_best.append(0)
        s_worst.append(0)
        for column in range(1,ncol):
            s_best[row]+=(dataset.iloc[row][column]-best_sol[column-1])**2
            s_worst[row]+=(dataset.iloc[row][column]-worst_sol[column-1])**2
        s_best[row]=s_best[row]**0.5
        s_worst[row]=s_worst[row]**0.5
        performance_score.append(s_best[row]+s_worst[row])
        if performance_score[row]>performance_score[idx]:
            idx=row
        print(dataset.iloc[row][0],"  ",performance_score[row],'\n')
    print ("Highest performance score: ", dataset.iloc[idx][0])

def main():
    file=input("Dataset: ")
    weights=input("Weights: ").split(',') #[1,2,1,1]
    impacts=input("Impacts: ").split(',') #['-','+','+','-']
    topsis(file,weights,impacts)