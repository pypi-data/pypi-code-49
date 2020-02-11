#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 11:17:00 2020

@author: navkiran
"""
import numpy as np
import pandas as pd
import sys

def topsis(decision,weights,impacts):
    decision = np.array(decision).astype(float)
    weights = np.array(weights).astype(float)
    impacts = [char for char in impacts]
    
    nrow = decision.shape[0]
    ncol = decision.shape[1]
    
    # Program will raise appropriate error if these conditions are not met
    assert len(decision.shape) == 2, "Decision matrix must be two dimensional"
    assert len(weights.shape) == 1, "Weights array must be one dimensional"
    assert len(weights) == ncol, "Wrong length of Weights array, should be {}".format(ncol)
    assert len(impacts) == ncol,"Wrong length of Impacts array, should be {}".format(ncol)
    
    # scaling weights
    weights = weights/sum(weights)
    
    # initializing N 
    N = np.zeros((nrow,ncol))
    
    nf = [None]*ncol
    for j in range(ncol):
        nf[j] = np.sqrt(sum((decision[:,j])**2))
    
    # constructing normalized decision matrix
    for i in range(nrow):
        for j in range(ncol):
            N[i][j] = decision[i][j]/nf[j]
    
    # constructing weighted normalized matrix
    W = np.diag(weights)
    V = np.matmul(N,W)
    
    # determination of positive ideal and negative ideal solutions
    u = [max(V[:,j]) if impacts[j] == '+' else min(V[:,j]) for j in range(ncol)]
    l = [max(V[:,j]) if impacts[j] == '-' else min(V[:,j]) for j in range(ncol) ]
    
    # calculating separation measures - distance from best and distance from worst 
    du = [None]*nrow
    dl = [None]*nrow
    
    
    for i in range(nrow):
        du[i] = np.sqrt(sum([(_v - _u)**2 for _v,_u in zip(V[i],u) ]))
    for i in range(nrow):
        dl[i] = np.sqrt(sum([(_v - _l)**2 for _v,_l in zip(V[i],l) ]))
    
    du = np.array(du).astype(float)
    dl = np.array(dl).astype(float)
    
    # calculatingg relative closeness to ideal solution
    score = dl/(dl+du)
    
    # This part is to return a dataframe with results - alternatives with their corresponding score and rank
    index = pd.Series([i+1 for i in range(nrow)])
    score = pd.Series(score)
    ranks = score.rank(ascending = False,method = 'min').astype(int)
    result = pd.concat([index,score, ranks], axis=1)
    result.columns = ['Alternative','Score','Rank']
    result = result.set_index('Alternative')
    return result

