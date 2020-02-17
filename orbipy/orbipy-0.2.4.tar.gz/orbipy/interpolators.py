# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:34:13 2019

@author: stasb
"""

import math
import numpy as np
#from scipy.interpolate import interp1d

class base_interpolator:
    '''
    Root class for all interpolators.
    Calculates mapping from [0, 1] to [0, 1]
    '''
    def __init__(self):
        self.A = 0.0
        self.B = 1.0
        self.a = 0.0
        self.b = 1.0
     
    def __call__(self, x):
        return x

    def AB(self, n):
        return np.linspace(self.A, self.B, n)
    
    def ab(self, n):
        return self(self.AB(n))
    
class ABab_mapper(base_interpolator):
    '''
    Calculates mapping from [A, B] to [a, b].
    interp should be [0,1]->[0,1] interpolator
    '''

    def __init__(self, interp, A=0.0, B=1.0, a=0.0, b=1.0):
        if not isinstance(interp, base_interpolator):
            raise TypeError('interp should be an instance of base_interpolator')
        self.d = B-A
        if math.fabs(self.d) < 1e-16:
            raise RuntimeError('A and B are very close, B-A=%f'%self.d)
        self.A = A
        self.B = B
        self.a = a
        self.b = b
        self.interp = interp
        
    def __call__(self, x):
        x_in = (x - self.A) / self.d
        x_out = self.interp(x_in)
        return self.a*(1-x_out)+self.b*x_out    
        
    def __getattr__(self, attr):
        return getattr(self.interp, attr)


class linear_interpolator(base_interpolator):        
    pass        
    
class log_interpolator(base_interpolator):
    def __init__(self, N=math.e):
        if N <= 0 or N == 1:
            raise ValueError("logarithm base should be >= 0.0 and not equal 1.0")
        self.iN = 1/N
        self.logN = math.log(N)
        self.x0 = self.iN / (1.0 - self.iN)
        self.y0 = -math.log(self.x0) / self.logN
        
    def __call__(self, x):
        return np.log(x+self.x0)/self.logN+self.y0

class flipY_interpolator(base_interpolator):
    def __init__(self, intrp):
        if not isinstance(intrp, base_interpolator):
            raise TypeError('This object is not base_interpolator inherited: %r'%intrp)
        self.intrp = intrp
        
    def __getattr__(self, attr):
        return getattr(self.intrp, attr)

    def __call__(self, x):
        return self.a+self.b-self.intrp(x)
    
class flipX_interpolator(base_interpolator):
    def __init__(self, intrp):
        if not isinstance(intrp, base_interpolator):
            raise TypeError('This object is not base_interpolator inherited: %r'%intrp)
        self.intrp = intrp
        
    def __getattr__(self, attr):
        return getattr(self.intrp, attr)
        
    def __call__(self, x):
        return self.intrp(self.A+self.B-x)

class chain_interpolator(base_interpolator):
    def __init__(self, interpolators):
        if len(interpolators) == 0:
            raise ValueError('No one interpolator passed')
        for intrp in interpolators:
            if not isinstance(intrp, base_interpolator):
                raise TypeError('This object is not base_interpolator inherited: %r'%intrp)
        self.interpolators = interpolators
        
    def __getattr__(self, attr):
        return getattr(self.interpolators[0], attr)

    def __call__(self, x):
        r = x
        for intrp in self.interpolators:
            r = intrp(r)
        return r
