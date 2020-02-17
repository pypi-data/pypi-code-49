# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:31:16 2019

@author: stasb
"""

from .models import crtbp3_custom_model
from numba import compiler, types
import numpy as np # do not remove - crtbp_ode uses it
import math # do not remove - crtbp_ode uses it
import warnings

class base_model_builder:
    pass

class crtbp3_model_builder(base_model_builder):
    '''
    
    Example
    -------
    
    model_events = [op.eventVX(), op.eventY()]

    mb = op.crtbp3_model_builder(stm=True, events=model_events,
                                 a=1e-6, c=5e-4)
    
    # This model will be sensitive to vx==0 and y=0 events
    # and generate states frequently near this events.
    cmodel = mb.buid_model()

    '''
    
    
    _header_code = \
'''
def crtbp_ode(t, s, constants):
    
    # initialization and pre calculations
    
    mu2 = constants[0]
    mu1 = 1 - mu2
    
    x = s[0]
    y = s[1]
    z = s[2]
    vx = s[3]
    vy = s[4]
    vz = s[5]
    
    ds = np.empty(%d)
    
    yz2 = y * y + z * z;
    xmu2 = x + mu2
    xmu1 = x - mu1

    r1 = (xmu2**2 + yz2)**0.5
    r2 = (xmu1**2 + yz2)**0.5
    r13, r15 = r1**(-3), r1**(-5)
    r23, r25 = r2**(-3), r2**(-5)
'''

    _main_code = \
'''
    # main ode calculation
    
    mu12r12 = (mu1 * r13 + mu2 * r23);

    ax =  2. * vy + x - (mu1 * xmu2 * r13 + mu2 * xmu1 * r23);
    ay = -2. * vx + y - mu12r12 * y;
    az =              - mu12r12 * z;

    ds[0] = vx
    ds[1] = vy
    ds[2] = vz
    ds[3] = ax
    ds[4] = ay
    ds[5] = az
'''        
    _stm_code =\
'''
    # stm calculation
    
    stm0 = np.ascontiguousarray(s[6:42]).reshape(6,6)

    Uxx = 1. - mu12r12 + 3*mu1*xmu2**2*r15 + 3*mu2*xmu1**2*r25
    Uxy = 3*mu1*xmu2*y*r15 + 3*mu2*xmu1*y*r25
    Uxz = 3*mu1*xmu2*z*r15 + 3*mu2*xmu1*z*r25
    Uyy = 1. - mu12r12 + 3*mu1*y**2*r15 + 3*mu2*y**2*r25
    Uyz = 3*mu1*y*z*r15 + 3*mu2*y*z*r25
    Uzz = -mu12r12 + 3*mu1*z**2*r15 + 3*mu2*z**2*r25
    
    A = np.array(((0.,  0.,  0.,   1., 0., 0.),
                  (0.,  0.,  0.,   0., 1., 0.),
                  (0.,  0.,  0.,   0., 0., 1.),
                  (Uxx, Uxy, Uxz,  0., 2., 0.),
                  (Uxy, Uyy, Uyz, -2., 0., 0.),
                  (Uxz, Uyz, Uzz,  0., 0., 0.)))

    stm1 = np.dot(A,stm0)
    ds[6:42] = stm1.ravel()
'''
    _event_header =\
'''
    # event perception
    
    def impulse(x, a, c, d):
        c2 = 2*c**2
        return -a*d*x*math.exp(-math.fabs(x)**d/c2)/c2
'''

    _event_code =\
'''
    %s
    ds[%d] = impulse(val%03d, %e, %e, %e)
'''

    _unsupported_event_code =\
'''
    ds[%d] = 0.0
'''
    
    _footer_code = \
'''
    return ds    
''' 
    
    def __init__(self, stm=False, events=[], 
                 a=1e-5, c=1e-5, d=1.5):
        
        self.events = events
        self.stm = stm
        
        state_size = 6 + (36 if stm else 0) + len(events)
        
        self.code = '' + self._header_code%state_size + self._main_code
        
        if stm:
            self.code += self._stm_code
        
        # events
        if events:
            self.code += self._event_header
            
            for i, event in enumerate(events):
                if type(event) == dict:
                    e = event['event']
                    a1, c1, d1 = event.get('a', a), event.get('c', c), event.get('d', d)
                else:
                    e = event
                    a1, c1, d1 = a, c, d

                if not hasattr(e, 'to_code'):
                    warnings.warn("Event %r does not have to_code method"%e)
                    self.code += self._unsupported_event_code%(-(len(events)-i))
                else:
                    self.code += self._event_code%(e.to_code(i), -(len(events)-i), i, a1, c1, d1)

        self.code += self._footer_code
            
        exec(compile(self.code, 'crtbp_ode_generated', mode='exec'))
        self.py_ode = locals()['crtbp_ode']
        self.right_part = \
        compiler.compile_isolated(self.py_ode,
                          [types.double, types.double[:], types.double[:]], 
                          return_type=types.double[:]).entry_point
                                  
    def build_model(self, 
                    const_set=None,
                    integrator=None,
                    solout=None):
        return crtbp3_custom_model(right_part=self.right_part,
                                   ev_size=len(self.events),
                                   integrator=integrator, 
                                   solout=solout, 
                                   stm=self.stm)                              
