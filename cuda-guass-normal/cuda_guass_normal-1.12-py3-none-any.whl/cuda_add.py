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

def cuda_add(nump1):
    leng1 = len(nump1)
    nThreads = 1024
    nBlocks = 68
    c1 = np.zeros((68, 1))
    input_num = np.float64(nump1.copy(order='C'))
    N = np.int32(leng1)
    cuda_add1(drv.InOut(input_num), drv.InOut(c1), N,
              block=(nThreads, 1, 1), grid=(nBlocks, 1))
    result = sum(c1)
    return(result[0])