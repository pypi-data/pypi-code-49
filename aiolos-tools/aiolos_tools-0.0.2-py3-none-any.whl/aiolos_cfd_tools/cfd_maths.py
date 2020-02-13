# python standard library
import logging
# third-party site-packages
import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt
from scipy.misc import derivative
from aiolos_code_instrumentation.timer import timer

log = logging.getLogger(__name__)

def locateIndex(XX,X):

    """
    # =======================================================================#
    #       FUNCTION:         LOCATE(XX,N,X)
    #
    #       DESCRIPTION:     Given an array XX of length N, and given a value
    #                        X, returns a value J such that X is between
    #                        XX(J) and XX(J+1).  XX must be monotonic, either
    #                        increasing or decreasing.  J=0 or J=N is
    #                        returned to indicate that X is out of range.
    #
    #       ARGUMENTS
    #
    #            XX:         Array of Tabulated Data
    #             X:         Value to find the location in the tabulated data
    #
    #       OUTPUTS
    #
    #             J:         Index of XX(J) where XX(J)< X < XX(J+1)
    #
    #      (C) Copyright. 1986-92 Numerical Recipes Software.
    # =======================================================================#
    """
    _ = timer.Timer()
    NN = len(XX)

    # is monotonically increasing
    if not np.all(XX[1:] > XX[:-1]):
        err_msg = "Error in <locateIndex(XX,X)>: independant variable data, X is not monotonically increasing"
        log.error(err_msg)
        raise ValueError(err_msg)
    # is in bounds
    if X < XX[0]:
        err_msg = "Error in <locateIndex(XX,X)>: Out of Bounds. X = %.2f < XX[0] = %.2f" % (X, XX[0])
        log.error(err_msg)
        raise ValueError(err_msg)

    if X > XX[-1]:
        err_msg = "Error in <locateIndex(XX,X)>: Out of Bounds. X = %.2f > XX[-1] = %.2f" % (X, XX[-1])
        log.error(err_msg)
        raise ValueError(err_msg)

    JL = 0
    JU = NN+1
    while (JU-JL > 1):
        JM = int((JU+JL)/2)

        if (((XX[ NN - 1 ] > XX[ 0 ]) and (X > XX[ JM ])) or ((XX[ NN - 1 ] <= XX[ 0 ]) and (X <= XX[ JM ]))):
            JL = JM
        else:
            JU = JM
    return JL

def trapeziodalIntegraion(fx, x, x0=None, x1=None):

    """
    # =======================================================================#
    #
    #       FUNCTION:       trapeziodalIntegraion(fx,x,x0,x1)
    #
    #       DESCRIPTION:    numerical integration of  the data in vector fx = f(x) 
    #                       over the range [x0,x1]. 
    #            
    #                        
    #       ARGUMENTS
    #
    #           :param fx:        <np.ndarray<np.float64> of size nx1> dependant variable data
    #           :param  x:        <np.ndarray<np.float64> of size nx1> independant variable data 
    #           :param x0:        <np.float64> lower limit of integration
    #           :param x1:        <np.float64> upper limit of integration   
    #
    #       OUTPUTS
    #
    #           :result s:        <np.float64> result of integration        
    #
    # =======================================================================#
    """
 
    _ = timer.Timer()
    n = x.size

    # if no bounds given, use full range of x
    if x0 == None:
        x0 = x[0]
    if x1 == None:
        x1 = x[-1]

    # is x monotonically increasing
    if not np.all(x[1:] > x[:-1]):
        err_msg = "Error in <trapeziodalIntegraion(fx,x,x0,x1)>: independant variable data, x is not monotonically increasing"
        log.error(err_msg)
        raise ValueError(err_msg)

    # is x1 > x0
    if not x1 > x0:
        err_msg = "Warning in <trapeziodalIntegraion(fx,x,x0,x1)>: x1 = %.2f less than x0 = %.2f result will be 0.0" % (x1, x0)
        log.warning(err_msg)
        raise ValueError(err_msg)

    s = 0.0 # sum
    for i in range(n-1):
        if x0 <= x[i] <=x1:
            s += (x[i+1]-x[i])*(fx[i+1]+fx[i])/2.0

    return s

def trapeziodalFunctionIntegraion(f, x, x0=None, x1=None):

    """
    # =======================================================================#
    #
    #       FUNCTION:       trapeziodalFunctionIntegraion(f,x,x0,x1)
    #
    #       DESCRIPTION:    numerical integration of the function f(x) 
    #                       over the range [x0,x1]. 
    #            
    #                        
    #       ARGUMENTS
    #
    #           :param fx:        <function> function with one input to be integrated
    #           :param  x:        <np.ndarray<np.float64> of size nx1> independant variable data 
    #           :param x0:        <np.float64> lower limit of integration
    #           :param x1:        <np.float64> upper limit of integration   
    #
    #       OUTPUTS
    #
    #           :result s:        <np.float64> result of integration        
    #
    # =======================================================================#
    """
 
    _ = timer.Timer()
    n = x.size

    # if no bounds given, use full range of x
    if x0 == None:
        x0 = x[0]
    if x1 == None:
        x1 = x[-1]

    # is x monotonically increasing
    if not np.all(x[1:] > x[:-1]):
        err_msg = "Error in <trapeziodalIntegraion(fx,x,x0,x1)>: independant variable data, x is not monotonically increasing"
        log.error(err_msg)
        raise ValueError(err_msg)

    # is x1 > x0
    if not x1 > x0:
        err_msg = "Warning in <trapeziodalIntegraion(fx,x,x0,x1)>: x1 = %.2f less than x0 = %.2f result will be 0.0" % (x1, x0)
        log.warning(err_msg)
        raise ValueError(err_msg)

    s = 0.0 # sum
    for i in range(n-1):
        if x0 <= x[i] <=x1:
            s += (x[i+1]-x[i])*(f(x[i+1])+f(x[i]))/2.0

    return s

def tdmaSolve(A, b):
   
    """

    # =======================================================================#
    #
    #       FUNCTION:           tdmaSolve(A, b)
    #
    #       DESCRIPTION:        Solves the system of equation of [A][x] = [b] 
    #                           for the case where the coefficient matrix [A] 
    #                           is a tridiagonal matrix
    #
    #
    #       ARGUMENTS
    #
    #           :param A:       <np.ndarray<np.float64> of size mxm> coefficient matrix
    #           :param b:       <np.ndarray<np.float64> of size mx1> source term vector
    #
    #
    #       OUTPUTS
    #
    #           :result x:      <np.ndarray<np.float64> of size mx1> results vector
    #
    # =======================================================================#

    """
    _ = timer.Timer()

    m = b.size 

    x = np.zeros(shape=(m,), dtype=np.float64)

    # first row coefficients
    A[0,1] = A[0, 1] / A[0,0]
    b[0] = b[0] / A[0,0]

    # forward elimination
    for i in range(1, m-1):
        d = A[i,i] - A[i-1,i] * A[i,i-1]
        A[i,i+1] = A[i,i+1] / d
        b[i] = (b[i] - A[i,i-1] * b[i-1]) / d

    # last row
    x[-1] = ( b[-1] - A[-1,-2] * b[-2] ) / ( A[-1,-1] - A[-2,-1]*A[-1,-2] ) 

    for i in range(m-2,-1,-1):
        x[i] = -A[i,i+1]*x[i+1] + b[i]

    return x


def NewtonRaphson(f, x, tol=1e-12, MAX_IT=5000):
    """

    # =======================================================================#
    #
    #       FUNCTION:           NewtonRhapson(f, x, tol)
    #
    #       DESCRIPTION:        Computes the zero of f based on an initial guess and
    #                           a defined tolerance based on the Newton-Raphson method 
    #                          
    #       ARGUMENTS
    #
    #           :param f:       <function> input function
    #           :param x:       <float> location of zero (initial guess required)
    #           :param tol:     <float> tolerance (default = 1e-12)
    #           :param MAX_IT:  <int> maximum number of iterations
    #
    #       OUTPUTS
    #
    #           :result x:      <float> zero of funtion f(x)
    #
    # =======================================================================#

    """
    _ = timer.Timer()
    count = 0
    while True:
        count += 1
        x1 = x - f(x)/derivative(func=f, x0=x, dx=1.0, n=1)
        err = np.abs(x1-x)
        x = x1
        if count > MAX_IT:
            err_msg = "Error in <NewtonRaphson(f,x,tol)>: Did not converge after %i iterations" % count
            raise ValueError(err_msg)
        if err < tol:
            log.debug(count)
            return x

def NewtonRaphsonArray(yvect, xvect, x, tol=1e-12, MAX_IT=5000, debug=False):
    """

    # =======================================================================#
    #
    #       FUNCTION:           NewtonRhapsonArray(yvect, xvect, x, tol)
    #
    #       DESCRIPTION:        Computes the zero of the data set (xvect, yvect) using 
    #                           the Newton-Raphson method on a cubic spline interpolation
    #                           of the data
    #                          
    #       ARGUMENTS
    #
    #           :param yvect:   <np.ndarray<np.float64>> array of y=f(x) values
    #           :param xvect:   <np.ndarray<np.float64>> array of x values
    #           :param x:       <float> location of zero (initial guess required)
    #           :param tol:     <float> tolerance (default = 1e-12)
    #           :param MAX_IT:  <int> maximum number of iterations
    #
    #       OUTPUTS
    #
    #           :result x:      <float> zero of funtion f(x)
    #
    # =======================================================================#

    """
    _ = timer.Timer()
    count = 0
    # fit a cubic spline to the data set
    spl = interpolate.splrep(xvect, yvect)
    
    # define a function using the cubic sline
    def f(x):
        return interpolate.splev(x,spl)
    # first derivative
    def dfdx(x):
        return interpolate.splev(x,spl, der=1)
    

    while True:
        
        count += 1
        # Newton-Rhapson Formula
        x1 = x - f(x)/dfdx(x)
        
        err = np.abs(x1-x)
        x = x1

        if count > MAX_IT:
            err_msg = "Error in <NewtonRaphson(f,x,tol)>: Did not converge after %i iterations" % count
            raise ValueError(err_msg)
        if err < tol:
            log.debug(count)
            plt.ioff()
            return x
