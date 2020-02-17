# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:14:44 2019

@author: stasb
"""
import math
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import fminbound, brent
from .interpolators import base_interpolator, linear_interpolator, ABab_mapper
    
class base_line:
    def __init__(self, interp=None):
        if interp is not None:
            if not isinstance(interp, base_interpolator):
                raise TypeError('This object is not base_interpolator inherited: %r'%interp)
        self.interp = interp
    
    def __call__(self, l):
        pass
    
    def length(self):
        pass

    def get_points(self, n):
        if self.interp is not None:
            return self(self.interp.AB(n))
        return self(np.linspace(0.0, 1.0, n))
        
    def translate(self, v):
        return self
    
    def scale(self, s):
        return self

    def scale_at_center(self, s, center):
        return self.translate(-center).scale(s).translate(center)
    
    def get_closest_point(self, p, xtol=1e-5, ret_l=False):
        l1 = fminbound(lambda l:np.sum((self(l)-p)**2), 0., 1., xtol=xtol)
        if ret_l:
            return self(l1), l1
        return self(l1)
    
    def split(self, l):
        if (l < 0.0 or l > 1.0):
            raise ValueError("Parameter l should be in [0, 1] but l=%f"%l)
        
class line_segment(base_line):
    
    def __init__(self, x0, x1, interp=None):
        super().__init__(interp)
        self.x0 = x0
        self.x1 = x1
        
    def __call__(self, l):
        if self.interp is not None:
            li = self.interp(l)
        else:
            li = l
        
        if isinstance(li, np.ndarray):
            return self.x0*(1.0-li[:,None])+self.x1*li[:,None]
        
        return self.x0*(1.0-li)+self.x1*li    

    def length(self):
        return np.linalg.norm(self.x1-self.x0)

    def translate(self, v):
        self.x0 += v
        self.x1 += v
        return self
    
    def scale(self, s):
        self.x0 *= s
        self.x1 *= s
        return self

    def split(self, l):
        super().split(l)
        xl = self(l)
        return (line_segment(self.x0, xl, self.interp),
                line_segment(xl, self.x1, self.interp))
#    def line_segment_intersect(self, line_seg):
#        """ 
#        Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
#        a1: [x, y] a point on the first line
#        a2: [x, y] another point on the first line
#        b1: [x, y] a point on the second line
#        b2: [x, y] another point on the second line
#        """
#        s = np.vstack([self.x0,self.x1,line_seg.x0,line_seg.x1]) # s for stacked
#        h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
#        l1 = np.cross(h[0], h[1])           # get first line
#        l2 = np.cross(h[2], h[3])           # get second line
#        x, y, z = np.cross(l1, l2)          # point of intersection
#        if z == 0:                          # lines are parallel
#            return np.array([float('inf'), float('inf')])
#        return np.array([x/z, y/z])

            
def heading_2d(x1, x2):
    '''
    Calculate angle from point x1 to point x2.
    '''
    dx = x2 - x1
    return math.degrees(math.atan2(dx[1], dx[0]))

def vector_2d(head):
    '''
    Calculate unit vector in head direction.
    '''    
    if isinstance(head, np.ndarray):
        rad = np.radians(head)
        return np.vstack((np.cos(rad),np.sin(rad))).T

    rad = math.radians(head)
    return np.array([math.cos(rad), math.sin(rad)])

class arc_segment(base_line):
    def __init__(self, center, head, fov, r, interp=None):
        super().__init__(interp)
        self.center = center
        self.head = head
        self.fov = fov
        self.r = r
        self.i1d = ABab_mapper(linear_interpolator(), A=0.0, B=1.0, 
                                       a=self.head-self.fov*0.5, 
                                       b=self.head+self.fov*0.5)

    def __call__(self, l):
        if self.interp is not None:
            li = self.interp(l)
        else:
            li = l
        
        heads = self.i1d(li)

        if isinstance(li, np.ndarray):
            return self.center[None,:] + self.r*vector_2d(heads)

        return self.center + self.r*vector_2d(heads)

    def length(self):
        return math.radians(self.fov)*self.r

    def translate(self, v):
        self.center += v
        return self
    
    def scale(self, s):
        self.center *= s
        self.r *= s
        return self            
    
class spline(base_line):
    
    def __init__(self, pts, kind='linear', interp=None, usecols=None):
        super().__init__(interp)
        self.pts = pts
        self.usecols = usecols
        if self.usecols is not None:
            self.cols = self.pts[:, self.usecols]
        else:
            self.cols = self.pts
        self.kind = kind
        self.updated = False
        self._update()
        
    def _update(self):
        c = self.cols
        s = np.sum((c[1:]-c[:-1])**2,axis=1)**0.5
        self._length = np.sum(s)
        self.l = np.concatenate(([0.], s))
        self.l = np.cumsum(self.l)/np.sum(self.l)
        self.i1d = interp1d(self.l, self.pts, kind=self.kind, 
                            axis=0, copy=False, 
                            fill_value='extrapolate')
        self.updated = True
        
    def __call__(self, l):
        if self.updated == False:
            self._update()
        if self.interp is not None:
            li = self.interp(l)
        else:
            li = l

        return self.i1d(li)

    def length(self):
        return self._length
    
    def translate(self, v):
        self.cols += v[None, :]
        self.updated = False
        return self
    
    def scale(self, s):
        self.cols *= s
        self.updated = False
        return self
    
    def split(self, l):
        super().split(l)
        idx = np.where(self.l - l > 0)[0]
        p = self(l)[None, :]
        pts0 = np.vstack((self.pts[:idx], p))
        pts1 = np.vstack((p, self.pts[idx:]))
        return (spline(pts0, self.kind, self.interp, self.usecols), 
                spline(pts1, self.kind, self.interp, self.usecols))        
    
    @classmethod
    def linear(cls, pts, interp=None, usecols=None):
        return cls(pts, kind='linear', interp=interp, usecols=usecols)
    
    @classmethod
    def quad(cls, pts, interp=None, usecols=None):
        return cls(pts, kind='quadratic', interp=interp, usecols=usecols)

    @classmethod
    def cubic(cls, pts, interp=None, usecols=None):
        return cls(pts, kind='cubic', interp=interp, usecols=usecols)
    

def line_segment_intersect(a1, a2, b1, b2, verbose=False):
    '''
    https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
    Answer by Gareth Rees
    '''

    p = a1
    r = a2-a1
    q = b1
    s = b2-b1
    
    rxs = np.cross(r, s)
    qpr = np.cross(q-p, r)
    rr = np.dot(r, r)
    
    if rxs == 0 and qpr == 0: # collinear
        t0 = np.dot(q-p, r)/rr
        t1 = t0 + np.dot(s, r)/rr
        
        t0, t1 = max(min(t0, t1), 0.0), min(max(t0, t1), 1.0)
        
        if verbose:        
            print('Collinear segments', t0, t1)
        return p+(t0+t1)/2*r # center of overlapping segments area
#        return (np.nan, np.nan)
    
    if rxs == 0 and qpr != 0: # parallel
        return np.array([np.inf, np.inf])
    
    # rxs != 0
    t = np.cross(q-p,s)/rxs
    u = qpr / rxs
    if (0. <= t <= 1.) and (0. <= u <= 1.): # intersected!
        print(p, r, t)
        return p+t*r
    else:
        return np.array([np.inf, np.inf]) # do not intersect


def intersections_slow(A, B):
    x11, x21 = np.meshgrid(A[:-1, 0], B[:-1, 0])
    x12, x22 = np.meshgrid(A[1:, 0], B[1:, 0])
    y11, y21 = np.meshgrid(A[:-1, 1], B[:-1, 1])
    y12, y22 = np.meshgrid(A[1:, 1], B[1:, 1])
    
    lst = []
    for a1,a2,b1,b2 in zip(np.vstack((x11.ravel(),y11.ravel())).T, 
                           np.vstack((x21.ravel(),y21.ravel())).T, 
                           np.vstack((x12.ravel(),y12.ravel())).T, 
                           np.vstack((x22.ravel(),y22.ravel())).T):
        r = line_segment_intersect(a1,b1,a2,b2)
        if r[0] != np.inf:
            lst.append(r)
    return np.array(lst)

def intersections(A, B):
    x11, x21 = np.meshgrid(A[:-1, 0], B[:-1, 0])
    x12, x22 = np.meshgrid(A[1:, 0], B[1:, 0])
    y11, y21 = np.meshgrid(A[:-1, 1], B[:-1, 1])
    y12, y22 = np.meshgrid(A[1:, 1], B[1:, 1])
    
    p = np.dstack((x11,y11))
    r = np.dstack((x12,y12)) - p

#    plt.figure()    
#    plt.plot(p[:,:,0], p[:,:,1], '.')
    
    q = np.dstack((x21,y21))
    s = np.dstack((x22,y22)) - q
    
    rxs = np.cross(r, s)
    qpr = np.cross(q-p, r)
    rr = np.sum(r*r, axis=2)#, keepdims=True)
#    rr1 = np.dot(r, np.transpose(r,axes=(0,2,1)))
    
    rxsmask = (rxs == 0)
    qprmask = (qpr == 0)

    ret = []

    mask = rxsmask & qprmask    
    if mask.any():        
        t0 = np.sum((q[mask]-p[mask])*r[mask], axis=2)/rr[mask] #, keepdims=True)
        t1 = t0 + np.sum(s[mask]*r[mask], axis=2)/rr[mask] #, keepdims=True)

        tmin = np.where(t0 <= t1, t0, t1)
        tmax = np.where(t0 >= t1, t0, t1)

        maskt = ((tmin >= 0.0) & (tmin <= 1.0)) | ((tmax >= 0.0) & (tmax <= 1.0))
        
        if maskt.any():
            t0 = np.where(tmin > 0.0, tmin, 0.0)
            t1 = np.where(tmax < 1.0, tmax, 1.0)
            
            t = (t0[maskt, None]+t1[maskt, None])*0.5
            
            ret.append(p[mask][maskt] + r[mask][maskt] * t)

# parallel        
#    mask = rxsmask & np.logical_not(qprmask)
#    if mask.any():
#        z = np.empty((mask.sum(), 2))
#        z[...] = np.inf
#        ret.append(z)
       
    mask = np.logical_not(rxsmask)
    if mask.any():
        t = np.cross(q[mask]-p[mask],s[mask])/rxs[mask]
        u = qpr[mask] / rxs[mask]
        
        tmask = (t >= 0.0) & (t <= 1.0)
        umask = (u >= 0.0) & (u <= 1.0)

        tumask = tmask & umask
        
        if tumask.any():
#            print(p[mask][tumask], r[mask][tumask], t[tumask] )
            ret.append(p[mask][tumask]+r[mask][tumask]*t[tumask, None])
    
    if ret:
        return np.vstack(tuple(ret))
    
    return None

def spline_intersections(A, B, n=100, th=1.0, xtol=1e-5):
    splA = spline.cubic(A)
    splB = spline.cubic(B)

    r = [np.linalg.norm(p - splB.get_closest_point(p)) for p in splA.get_points(n)]
    d = np.gradient(r)
    idx = np.where((d[:-1]<0)&(d[1:]>0))[0]

    def fun(x):
        p = splA(x)
        p1 = splB.get_closest_point(p, xtol=xtol)
        return np.linalg.norm(p - p1)

    br = np.linspace(0., 1., n)

    if idx.shape[0] > 0:
        l = np.array([fminbound(fun, br[i], br[i+1], xtol=xtol, full_output=True) for i in idx])
        print(l)
        mask = (l[:,1] < th)    
        if mask.any():    
            return splA(l[mask,0])
    
    return None
    

#def find_intersections(A, B, debug=False):
#    '''
#    Source
#    ------
#    https://stackoverflow.com/questions/3252194/numpy-and-line-intersections
#    
#    Code
#    ----
#    from numpy import where, dstack, diff, meshgrid
#    
#    def find_intersections(A, B):
#    
#        # min, max and all for arrays
#        amin = lambda x1, x2: where(x1<x2, x1, x2)
#        amax = lambda x1, x2: where(x1>x2, x1, x2)
#        aall = lambda abools: dstack(abools).all(axis=2)
#        slope = lambda line: (lambda d: d[:,1]/d[:,0])(diff(line, axis=0))
#    
#        x11, x21 = meshgrid(A[:-1, 0], B[:-1, 0])
#        x12, x22 = meshgrid(A[1:, 0], B[1:, 0])
#        y11, y21 = meshgrid(A[:-1, 1], B[:-1, 1])
#        y12, y22 = meshgrid(A[1:, 1], B[1:, 1])
#    
#        m1, m2 = meshgrid(slope(A), slope(B))
#        m1inv, m2inv = 1/m1, 1/m2
#    
#        yi = (m1*(x21-x11-m2inv*y21) + y11)/(1 - m1*m2inv)
#        xi = (yi - y21)*m2inv + x21
#    
#        xconds = (amin(x11, x12) < xi, xi <= amax(x11, x12), 
#                  amin(x21, x22) < xi, xi <= amax(x21, x22) )
#        yconds = (amin(y11, y12) < yi, yi <= amax(y11, y12),
#                  amin(y21, y22) < yi, yi <= amax(y21, y22) )
#    
#        return xi[aall(xconds)], yi[aall(yconds)]
#    
#    Parameters
#    ----------
#    
#    A : numpy array of (n,2) shape
#        First points for all line segments
#        
#    B : numpy array of (n,2) shape
#        Second points for all line segments
#    
#    Return
#    ------
#    Intersection points for all line segments
#    
#    Example
#    -------
#    import orbipy as op
#    
#    spline = op.lines.spline.quad(np.array([[0.,0.],[1.,2.],[4.,0.]]))
#    line_seg = op.lines.line_segment(np.array([0.,0.5]),
#                                     np.array([5.,0.5]))
#    ret = op.lines.find_intersections(spline.get_points(10), line_seg.get_points(2))
#    
#    '''
#    # min, max and all for arrays
#    amin = lambda x1, x2: np.where(x1<x2, x1, x2)
#    amax = lambda x1, x2: np.where(x1>x2, x1, x2)
#    aall = lambda abools: np.dstack(abools).all(axis=2)
#    slope = lambda line: (lambda d: d[:,1]/d[:,0])(np.diff(line, axis=0))
#
#    x11, x21 = np.meshgrid(A[:-1, 0], B[:-1, 0])
#    x12, x22 = np.meshgrid(A[1:, 0], B[1:, 0])
#    y11, y21 = np.meshgrid(A[:-1, 1], B[:-1, 1])
#    y12, y22 = np.meshgrid(A[1:, 1], B[1:, 1])
#
#    m1, m2 = np.meshgrid(slope(A), slope(B))
#    
#    # TODO
#    # IF m1==0 or m2==0
#    
#    mask_m1 = (np.abs(m1) > 1e-16) & (m1 != np.inf)
#    mask_m2 = (np.abs(m2) > 1e-16) & (m2 != np.inf)
#    mask_m = mask_m1 | mask_m2
#
#    xi = np.empty_like(x11)
#    xi[...] = np.inf
#    yi = np.empty_like(y11)
#    yi[...] = np.inf
#    
#    if mask_m2.any():
#        m1_ = m1[mask_m2]
#        m2_ = m2[mask_m2]
#        m2inv = 1/m2_
#        xi_ = xi[mask_m2]
#        yi_ = yi[mask_m2]
#        x21_ = x21[mask_m2]
#        x11_ = x11[mask_m2]
#        y21_ = y21[mask_m2]
#        y11_ = y11[mask_m2]
#        
#        yi_[...] = (m1_*(x21_-x11_-m2inv*y21_) + y11_)/(1 - m1_*m2inv)
#        xi_[...] = (yi_ - y21_)*m2inv + x21_
#
##        yi =       (m1 *(x21 -x11 -m2inv*y21 ) + y11 )/(1 - m1 *m2inv)
##        xi =       (yi  - y21 )*m2inv + x21
#    
#    if mask_m1.any():
#        m1inv = 1/m1[mask_m1]
#        yi[mask_m1] = (m2[mask_m1]*(x22[mask_m1]-x12[mask_m1]-m1inv*y22[mask_m1]) + y12[mask_m1])/(1 - m2[mask_m1]*m1inv)
#        xi[mask_m1] = (yi[mask_m1] - y22[mask_m1])*m1inv + x22[mask_m1]
#
#
#
#    xconds = (amin(x11, x12) < xi, xi <= amax(x11, x12), 
#              amin(x21, x22) < xi, xi <= amax(x21, x22) )
#    yconds = (amin(y11, y12) < yi, yi <= amax(y11, y12),
#              amin(y21, y22) < yi, yi <= amax(y21, y22) )
#
#    mask_x = aall(xconds)
#    mask_y = aall(yconds)
#    
#    mask = mask_x & mask_y & mask_m
#    
#    if debug:
#        return xi, yi
#
#    if mask.any():
#        return xi[mask_x & mask_m], yi[mask_y & mask_m]
#    
#    return (np.nan, np.nan)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from .interpolators import ( log_interpolator, 
                                chain_interpolator,
                                flipX_interpolator,
                                flipY_interpolator)

    A, B = 1., 2.
    a, b = 0., 1.
    
    intrp = ABab_mapper(linear_interpolator(), A, B, a, b)
    intrp1 = flipX_interpolator(ABab_mapper(log_interpolator(), A, B, a, b))
    intrp2 = flipY_interpolator(ABab_mapper(log_interpolator(), a, b, A, B))
    
    intrp = chain_interpolator([intrp1, intrp2])
    
    x = np.linspace(A, B, 100)
    y = intrp(x)
    
    plt.figure(figsize=(10,10))
    plt.plot(x, y, '.-')
    
    x0 = np.array([10.,10.])
    x1 = np.array([20.,20.])
    ls = line_segment(x0, x1, log_interpolator(N=10))
    arc = arc_segment(x0, 45., 90., 10., log_interpolator(N=10))
    
    pts = arc.get_points(10)
    #ls.get_points(10)
    #pts[:,1] = -pts[:,1] + np.random.rand(pts.shape[0])*2-1
    
    pwl = spline.linear(pts, flipY_interpolator(log_interpolator(N=10)))
    pts1 = arc.get_points(50)
    
    plt.figure(figsize=(10,10))
    plt.plot(pts[:,0], pts[:,1], '.-')
    plt.plot(pts1[:,0], pts1[:,1], '.r')
    plt.axis('equal')
    
    