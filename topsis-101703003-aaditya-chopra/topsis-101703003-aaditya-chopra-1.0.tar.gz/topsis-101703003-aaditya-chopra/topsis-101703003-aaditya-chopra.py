# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:55:49 2020

@author: Aaditya Chopra
Roll no. - 101703003
"""

import pandas as pd
import math

def transpose(var):
    lis = list()
    for i in range(len(var[0])):
        lis1 = list()
        for j in range(len(var)):
            lis1.append(var[j][i])
        lis.append(lis1)
    return lis

def topsis(dataframe, weights, impact):
    
    data = pd.read_csv(dataframe).iloc[:,1:].values.tolist()
    
    denum = [0]*(len(data[0]))
    for i in range(len(data[0])):
        for j in range(len(data)):
            denum[i] = denum[i] + (data[j][i])^2
        denum[i] = math.sqrt(denum[i])
    
    lis = list()
    for i in range(len(data)):
        w = list()
        for j in range(len(data[0])):
            w.append(data[i][j]/denum[j])
        lis.append(w)
        
    lis1 = list(map(int, weights.strip().split(',')))
    
    if len(lis1)!= len(data[0]):
        raise Exception("weights len not equal to no. of col.")
    
    for i in lis1:
        if i<0:
            raise Exception("Weight not +ve")
    
    w = list()
    
    for i in range(len(lis1)):
        w.append(lis1[i]/sum(lis1))
        
    imp = impact.strip().split(',')
    
    if len(lis1)!= len(data[0]):
        raise Exception("Impact len not equal to no. of col")
        
    for i in imp:
        if i not in ['+','-']:
            raise Exception("Impact not of '+' or '-' signs")
    
    for j in range(len(data[0])):
        for i in range(len(data)):
            lis[i][j] = lis[i][j] * w[j]
    
    lisb, lisw = list(), list()
               
    trp = transpose(lis)
    
    for i in range(len(trp)):
        if imp[i] == '+':
            lisw.append(min(trp[i]))
            lisb.append(max(trp[i]))
        elif imp[i] == '-':
            lisw.append(max(trp[i]))
            lisb.append(min(trp[i]))
    
    p = list()
    
    for i in range(len(lis)):
        sp, sm = 0, 0
        for j in range(len(lis[0])):
            sp = sp + (lis[i][j] - lisb[j])^2
            sm = sm + (lis[i][j] - lisw[j])^2
        sp = math.sqrt(sp)
        sm = math.sqrt(sm)
        p.append(sm/(sp+sm))
    
    ranks = sorted(list(range(1,len(p)+1)))
    prev = sorted(p, reverse = True)
    
    prfmnc = list()
    
    for i in p:
        prfmnc.append([i,ranks[prev.index(i)]])
    
    d = {'rowNo':['Score', 'Rank']}
    for item in range(len(prfmnc)):
        d[item] = prfmnc[item]
    for key, val in d.items():
        print(key, val)
