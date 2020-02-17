# Cuda Library
from numba import cuda
import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule
from math import sqrt
import numpy as np
from array import array
import pandas as pd

from .__init__ import *


def cuda_var(nump1, nump2, mean_vec, yl):
    leng1, ncol = nump1.shape
    result = np.zeros((ncol, 1))
    weight_np = np.zeros((ncol, 1))
    nThreads = 1024
    nBlocks = 68
    c1 = np.zeros((68, 1))

    for i in range(0, ncol):
        input_num = np.float64(nump1[:, i].copy(order='C'))
        weight_np = np.float64(nump2.copy(order='C'))
        N = np.int32(leng1)
        mean1 = mean_vec[i]
        cuda_var1(drv.InOut(input_num), mean1, drv.InOut(c1), drv.InOut(
            weight_np), N, block=(nThreads, 1, 1), grid=(nBlocks, 1))
        result[i] = sum(c1)*leng1/((leng1-1)*yl)
    return(result)