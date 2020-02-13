import numpy as np
from scipy import integrate


def f(xyz,t, sigma,beta,lambd):
    x, y, z = xyz
    return [sigma * (y-x), beta * x - y - x*z, -lambd* z+ x*y]

def Trace(**kwargs):

    t = kwargs.get('t', np.linspace(0, 20, 5000))
    xyz = kwargs.get('xyz', [1,1,1])
    sigma=kwargs.get('sigma', 10)
    beta =kwargs.get('beta', 28)
    lambd=kwargs.get('lambd', 8/3)

    trace = integrate.odeint(f, xyz, t, args=(sigma, beta, lambd))
    return trace
