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

def cuda_correlation(nump1, nump2, var_name):
    leng1, ncol = nump1.shape
    result = np.zeros((ncol,ncol))
    weight_np = np.zeros((ncol,1))
    nThreads = 1024
    nBlocks = 68
    total = cuda_add(nump2)
    mean_vec = cuda_mean(nump1, nump2, total)
    var_vec = cuda_var(nump1, nump2, mean_vec, total)
    for i in range(0, ncol):
        for j in range(i, ncol):
            c1 = np.zeros((68,1))
            input_num1 = np.float64(nump1[:, i].copy(order='C'))
            input_num2 = np.float64(nump1[:, j].copy(order='C'))
            weight_np = np.float64(nump2.copy(order='C'))
            N = np.int32(leng1)
            mean1 = mean_vec[i]
            mean2 = mean_vec[j]
            cuda_covar1(drv.InOut(input_num1), mean1, drv.InOut(c1), drv.InOut(
            weight_np), drv.InOut(input_num2), mean2, N, block=(nThreads, 1, 1), grid=(nBlocks, 1))
            result[i,j] = sum(c1)*leng1/((leng1-1)*total)
            result[j,i] = sum(c1)*leng1/((leng1-1)*total)
            result[i,j] = result[i,j]/sqrt(var_vec[i]*var_vec[j])
            if(i==j): continue
            result[j,i] = result[j,i]/sqrt(var_vec[i]*var_vec[j])
    
    result_pd = pd.DataFrame(data = result, columns = var_name, index = var_name)
    return(result_pd)