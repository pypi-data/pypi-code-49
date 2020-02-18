# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:38:44 2019

@author: knoerk
"""


import numpy as np
import pandas as pd
from plotnine import *
import pickle as pk
import glob
from lmfit import minimize, Parameters

class fit_g0_g1():
    '''
    Function to extract the parameters g0 and g1 from gas exchange parameters following
    the approch of medlyn et al (2011)
    '''
    
    def __init__(self,ID):
        self.ID=ID
        self.params = Parameters()
        self.params.add('g1', min= 0.00001, max=100)
        self.params.add('g0', min=0.00001,max=10)
        self.out=None
        self.predicted=None
    
    def residual(self,params,VPD, A, ca,GH2O):
        g1 = params['g1'].value
        g0 = params['g0'].value

        GH2Omodel =1000*( g0+(1+g1/np.sqrt(VPD))*(A/ca))
        
        return (GH2O-GH2Omodel)
    
    
    def fit(self,VPD, A, ca, GH2O,**kwargs):
        #self.nan_policy=nan_policy
        self.VPD=VPD
        #self.method=method
        self.A=A
        self.ca=ca
        self.GH2O=GH2O
        self.out = minimize(self.residual, self.params, args=(self.VPD, self.A,self.ca,self.GH2O), **kwargs)
        self.predicted= 1000*(self.out.params['g0']+(1+self.out.params['g1']/np.sqrt(self.VPD))*(self.A/self.ca))
        
        
if __name__ == "__main__":
    
    
    VPD=np.array([1,2,3,4])
    A=np.array([2,4,6,8])
    ca=np.array([100,200,300,400])
    GH2O=np.array([50,100,200,400])
    
    g=fit_g0_g1('example')
    g.fit(VPD,A,ca,GH2O,method='leastsq',nan_policy='omit',calc_covar=False)
       
    df=pd.DataFrame(zip(g.predicted,g.GH2O),columns=['predGH2O','GH2O'])
    p=ggplot(df,aes(x='GH2O',y='predGH2O'))
    p+=geom_point()
    p.draw()
    