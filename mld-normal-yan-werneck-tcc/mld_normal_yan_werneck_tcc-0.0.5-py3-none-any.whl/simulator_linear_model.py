import numpy as np
from scipy import stats
import pymc3


def gerador_dados_dinamicos(m0, w_a, w_b, v_a, v_b, sample_size = 1000):
    with pymc3.Model():
        w = pymc3.distributions.InverseGamma("w", alpha = w_a, beta = w_b)
        V = pymc3.distributions.InverseGamma("V", alpha = v_a, beta = v_b)
    
    u = np.zeros(sample_size)
    y = np.zeros(sample_size)
    u[0] = m0
    for iteration in range(1,sample_size):
        u[iteration] = u[iteration-1] + stats.norm.rvs(loc = 0, scale = np.sqrt(w.random()))
        y[iteration] = u[iteration] + stats.norm.rvs(loc = 0, scale = np.sqrt(V.random()))
    return y, u