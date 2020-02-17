# Cuda Library
from numba import cuda
import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule
from math import sqrt
import numpy as np
from array import array
import pandas as pd


from .cuda_add import * 
from .cuda_mean import * 
from .cuda_var import *

from .__init__ import *


def guass_normal(nump1, nump2, nump3):
    leng1, ncol = nump1.shape
    weight_np = nump3
    total = cuda_add(weight_np)
    mean_vec = cuda_mean(nump2, weight_np, total)
    var_vec = cuda_var(nump2, weight_np, mean_vec, total)
    result = np.zeros((leng1, ncol))
    for i in range(0, ncol):
        result[:, i] = (nump1[:, i]-mean_vec[i])/sqrt(var_vec[i]+0.001)
    return(result)