# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:16:30 2018

@author: maria
"""

import numpy as np
import math
from .events import event_detector, eventY
from .mapper import mapper

class differential_correction:
    '''
    differential_correction class itroduce differential
    correction method: 
        ds = Phi(t0,t)*ds0,
        where:
        Phi(t0,t) - State Transition Matrix from t0 to t,
        ds0 - variation of state at t0,
        ds - variation of state at t.
        
    Thus, ds0 = Phi(t0,t)**(-1)*ds.
    This set of equations can be solved partially when some
    assumptions is made.
    
    For example, to find halo orbits one can assume:
        vx(t), vz(t) should be zero (target),
        and x(t0), vy(t0) will vary
    
    Then correction will be calculated as:
        
        m = [[Phi[3,0], Phi[3,4]], [Phi[5,0], Phi[5,4]]]
        -1/vy(t)*dot([[ax(t)],[az(t)]],[Phi[1,0], Phi[1,4]])
        
        dx = inv(m)*(-[vx(t),vz(t)])
        
    '''
    presets = {
                'halo': {'target':('vx','vz'),
                         'vary':('x','z','vy'), 
                         'event': eventY()},
                'axial':{'target':('z','vx'),
                         'vary':('vy','vy','vz'),
                         'event':eventY(count=2)}
                }
    
    def __init__(self, model,
                 target=('vx','vz'),
                 vary=('x','z','vy'),
                 event=None,
                 iterations=30, 
                 tol=1e-12,
                 ftol=1e-12,
                 maxt=100*np.pi):
        self.target = target
        self.vary = vary
        self.rows = np.array([mapper.col2idx(c)-1 for c in target], dtype=int)
        self.cols = np.array([mapper.col2idx(c)-1 for c in vary], dtype=int)
        self.iterations = iterations
        self.tol = tol
        self.ftol = ftol
        self.maxt = maxt
        if event is None:
            self.event = differential_correction.presets['halo']['event']
        else:
            self.event = event
        self.model = model
        self.it = 0
        
    @classmethod
    def from_preset(cls, model,
                    preset='halo',
                    iterations=30, 
                    tol=1e-12,
                    ftol=1e-12,
                    maxt=100*np.pi):
        if preset not in differential_correction.presets:
            raise RuntimeError("Can't find differential correction preset: %s"%preset)
        return cls(model, **differential_correction.presets[preset],
                   iterations=iterations, tol=tol, ftol=ftol, maxt=maxt)

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        if not model.stm:
            raise ValueError('Differential correction needs state-transition matrix (STM)')
        self._model = model
        self._detector = event_detector(self._model, [self.event], self.tol)
          
    def shoot(self, s0, alpha=0):
        
        rads = math.radians(alpha)
        self.it = 0
        s = self._model.get_zero_state()
        s[:s0.shape[0]] = s0
        #s = s0.copy()
        r = self.rows
        rT = r[:,np.newaxis]
        c = self.cols[np.newaxis,:]
        
        sn = math.sin(rads)
        cs = math.cos(rads)
        rot = np.array([[cs, sn]]).T
        
        while self.it < self.iterations:
            _, evout = self._detector.prop(s, 0., self.maxt, ret_df=False)
            
            if len(evout) == 0:
                raise RuntimeError('Event unreachable: %r'%self.event)
            
            ev = evout[-1, 4:] # i(0), cnt(1), trm(2), t(3), x(4), y(5), z(6), ...
            xf = ev[:6]
            if math.fabs(xf[r[0]]) < self.ftol and math.fabs(xf[r[1]]) < self.ftol:
                break
            dxdt = self._model.right_part(0., ev, self._model.constants)
            Phi = ev[6:42].reshape(6, 6)
            
            Phi1 = Phi[rT, c]
            Phi2 = np.hstack((Phi1[:,[0,1]]@rot, Phi1[:,[2]]))
            Phi3 = np.hstack((Phi[1,c[:,[0,1]]]@rot, Phi[1, c[:,[2]]]))
            m = Phi2 - 1/dxdt[1] * dxdt[rT]@Phi3
            dd = np.linalg.inv(m)@(-xf[rT])
            dx = np.empty((3,1))
            dx[0] = dd[0,0]*cs
            dx[1] = dd[0,0]*sn
            dx[2] = dd[1,0]
            s[c.T] += dx
#            print(dx)

            self.it += 1

        if self.it >= self.iterations:
            raise RuntimeError("Unable to converge")

        return s
        
    # deprecated
    def find_halo(self, s0, fixed='z0', ret_it=False, ftol=1e-12):
        i = 0
        s = s0.copy()
        while i < self.iterations:
            _, evout = self._detector.prop(s, 0., 700*np.pi, ret_df=False)
#            print(evout[-1, 2])
            ev = evout[-1, 4:] # i(0), cnt(1), trm(2), t(3), x(4), y(5), z(6), ...
            xf = ev[:6]
#            print(xf)
            if math.fabs(xf[3]) < ftol and math.fabs(xf[5]) < ftol:
                break
#            print('shape:', ev.shape)
            dxdt = self._model.right_part(0., ev, self._model.constants)
#            print(xf, dxdt)
            Phi = ev[6:42].reshape(6, 6)
        
            if fixed == 'x0':
                # A = np.array([[Phi[3,2], Phi[3,4]], [Phi[5,2], Phi[5,4]]])
                m = np.array([[Phi[3,2], Phi[3,4]], [Phi[5,2], Phi[5,4]]])\
                -1/dxdt[1]*np.array([[dxdt[3]],[dxdt[5]]])@np.array([Phi[1,2], Phi[1,4]], ndmin=2)
                dx = np.linalg.solve(m, -xf[[3,5]])
                s[[2,4]] += dx
                
            if fixed == 'z0':
                m = np.array([[Phi[3,0], Phi[3,4]], [Phi[5,0], Phi[5,4]]])\
                -1/dxdt[1]*np.array([[dxdt[3]],[dxdt[5]]])@np.array([Phi[1,0], Phi[1,4]], ndmin=2)
#                print(m)
                dx = np.linalg.solve(m, -xf[[3,5]])
#                print(dx)
                s[[0,4]] += dx 
    
            i += 1
        if i < self.iterations:
            pass
#            print("Converged i =", i, "halo", s)
        else:
            raise RuntimeError("Unable to converge")
#            print("Hasn't converged")
        if ret_it:
            return s, i
        return s
    
    
    # deprecated
    def find_axial(self, s0, retIt=False, verbose=False, ftol=1e-12):
        detector = event_detector(self._model, [eventY(count=2)], self.tol)
#        dt = 0
        i = 0
        while i < self.iterations:
#            lst_xf = []
            evout = []
            s = s0.copy()
            _, evout = detector.prop(s, 0, 700*np.pi, ret_df=False)
            ev = evout[-1, 4:] # i(0), cnt(1), trm(2), t(3), x(4), y(5), z(6), ...
            xf = ev[:6]
            dxdt = self._model.right_part(0., ev, self._model.constants)
            Phi = ev[6:42].reshape(6, 6)
            
            if abs(xf[2]) < ftol and abs(xf[3]) < ftol:
                break

            m = np.array([[Phi[2,4], Phi[2,5]], [Phi[3,4], Phi[3,5]]])\
            -1/dxdt[1]*np.array([[dxdt[2]],[dxdt[3]]])@np.array([Phi[1,4], Phi[1,5]], ndmin=2)

            dx = np.linalg.inv(m)@(-xf[[2,3]])
            s0[[4,5]] += dx 

            i += 1
        if verbose:
            if i < self.iterations:
                print("Converged i =", i, "axial", s0)    
            else:
                print("Hasn't converged")
        if retIt:
            return s0.copy(), i
        return s0.copy()
    
    