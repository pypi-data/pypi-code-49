import numpy as np
from scipy import stats
import pymc3


def gerador_dados_dinamicos(m0, w_a, w_b, v_a, v_b, sample_size = 1000):
    
    w_sample = stats.invgamma.rvs(w_a, scale = w_b, size = 1)
    V_sample = stats.invgamma.rvs(v_a, scale = v_b, size = 1)

    u = np.zeros(sample_size)
    y = np.zeros(sample_size)
    u[0] = m0
    for iteration in range(1,sample_size):
        u[iteration] = u[iteration-1] + stats.norm.rvs(loc = 0, scale = np.sqrt(w_sample))
        y[iteration] = u[iteration] + stats.norm.rvs(loc = 0, scale = np.sqrt(V_sample))
    
    return y, u