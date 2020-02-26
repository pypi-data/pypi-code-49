"""
MIT License

Copyright (c) 2020 Max Planck Institute of Molecular Physiology

Author: Luca Lusnig (luca.lusnig@mpi-dortmund.mpg.de)
Author: Thorsten Wagner (thorsten.wagner@mpi-dortmund.mpg.de)
Author: Markus Stabrin (markus.stabrin@mpi-dortmund.mpg.de)
Author: Fabian Schoenfeld (fabian.schoenfeld@mpi-dortmund.mpg.de)
Author: Tapu Shaikh (tapu.shaikh@mpi-dortmund.mpg.de)
Author: Adnan Ali (adnan.ali@mpi-dortmund.mpg.de)


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from math import exp
from ridge_detection.helper import getNormal
from ridge_detection import linesUtil
import numpy as np

""" 1/sqrt(2*PI) """
SQRT_2_PI_INV = 0.398942280401432677939946059935

def phi0(x,sigma):
    """
    Integral of the Gaussian function
    :param x:
    :param sigma:
    :return:
    """
    return getNormal(x/sigma)

def phi1(x,sigma):
    """
    The Gaussian function
    :param x:
    :param sigma:
    :return:
    """
    t = x/sigma
    return SQRT_2_PI_INV / sigma * exp(-0.5 * t * t)

def phi2(x,sigma):
    """
    First derivative of the Gaussian function
    :param x:
    :param sigma:
    :return:
    """
    t = x/sigma
    return -x * SQRT_2_PI_INV / pow(sigma, 3.0) * exp(-0.5 * t * t)


"""
Functions to compute the one-dimensional convolution masks of the 0th, 1st, and 2nd derivative of the Gaussian kernel for a certain smoothing level given
by sigma. The mask is allocated by the function and given as the return	 value. The caller must ensure that this memory is freed. The output is
intended to be used as an array with range [-num:num]. Therefore, the caller should add num to the return value. Examples for the calling sequence can be
found in convolve_gauss. Examples for the usage of the masks are given in convolve_rows_gauss and convolve_cols_gauss.
"""
def _compute_gauss_mask_0(sigma):
    """
    :param sigma:
    :return: vector containing the Gaussian smoothing mask
    """
    n = linesUtil.mask_size(linesUtil.MAX_SIZE_MASK_0, sigma)
    h = np.zeros(2 * n + 1)
    for i in list(range(-n+1,n)):
        h[n + i] = phi0(-i + 0.5, sigma) - phi0(-i - 0.5, sigma)
    h[0] = 1.0 - phi0(n - 0.5, sigma)
    h[2 * n] = phi0(-n + 0.5, sigma)
    return n,h

def _compute_gauss_mask_1(sigma):
    """
    :param sigma:
    :return: vector containing the First derivative of Gaussian smoothing mask
    """
    n = linesUtil.mask_size(linesUtil.MAX_SIZE_MASK_1, sigma)
    h = np.zeros(2 * n + 1)
    for i in list(range(-n+1,n)):
        h[n + i] = phi1(-i + 0.5, sigma) - phi1(-i - 0.5, sigma)
    h[0] =  -phi1(n - 0.5, sigma)
    h[2 * n] = phi1(-n + 0.5, sigma)
    return n,h

def _compute_gauss_mask_2(sigma):
    """
    :param sigma:
    :return: vector containing the Second derivative of Gaussian smoothing mask
    """
    n = linesUtil.mask_size(linesUtil.MAX_SIZE_MASK_2, sigma)
    h = np.zeros(2 * n + 1)
    for i in list(range(-n+1,n)):
        h[n + i] = phi2(-i + 0.5, sigma) - phi2(-i - 0.5, sigma)
    h[0] = - phi2(n - 0.5, sigma)
    h[2 * n] = phi2(-n + 0.5, sigma)
    return n,h

"""
Convolve an image with the derivatives of a Gaussian smoothing kernel. Since all of the masks are separable, this is done in two steps in the function
convolve_gauss. Firstly, the rows of the image are convolved by an appropriate one-dimensional mask in convolve_rows_gauss, yielding an
intermediate float-image h. Then the columns of this image are convolved by another appropriate mask in convolve_cols_gauss to yield the final result k.
At the border of the image the gray values are mirrored.
"""

def convolve_rows_gauss(image, mask, n,  h, width, height) :
    """
    Convolve rows gauss
    :param image:
    :param mask:
    :param n:
    :param h:
    :param width:
    :param height:
    :return:
    """
    """ inner region"""

    r_values = np.arange(n, height - n)
    for l in np.repeat(r_values, width) * width + np.tile(np.arange(width), len(r_values)):
        h[l] = np.sum(np.multiply(image[l-n*width:l+(n+1)*width:width],mask[0:2*n+1]))


    """" Border regions """
    for r in list(range(0, n)):
        for c in list(range(0, width)):
            tot = 0.0
            l = r * width + c               # it is lincoord(row, col,width) of linesUtil.py
            for j in list(range(-n, n + 1)):
                tot += (image[linesUtil.lincoord(linesUtil.br(r + j, height), c, width)]) * mask[j + n]
            h[l] = tot
    for r in list(range(height- n, height)):
        for c in list(range(0, width)):
            tot = 0.0
            l = r * width + c
            for j in list(range(-n, n + 1)):
                tot += (image[linesUtil.lincoord(linesUtil.br(r + j, height), c, width)]) * mask[j + n]
            h[l] = tot

def convolve_cols_gauss(h, mask,n, k, width, height):
    """
    Convolve the columns of an image with the derivatives of a Gaussian
    :param h:
    :param mask:
    :param n:
    :param k:
    :param width:
    :param height:
    :return:
    """

    """ inner region"""
    c_values = np.arange(n, width-n)
    h=np.asarray(h)
    for l in np.repeat(c_values, height) * height + np.tile(np.arange(height), len(c_values)):
        k[l] = np.sum(np.multiply(h[l-n:l+n+1],mask[0:2*n+1]))

    """" Border regions """
    for r in list(range(0, height)):
        for c in list(range(0,  n)):
            tot = 0.0
            l = r * width + c
            for j in list(range(-n, n + 1)):
                tot += h[linesUtil.lincoord(r, linesUtil.bc(c + j, width), width)] * mask[j + n]
            k[l] = tot
    for r in list(range(0, height)):
        for c in list(range(width-n,width)):
            tot = 0.0
            l= r * width + c
            for j in list(range(-n, n+1)):
                tot += h[linesUtil.lincoord(r, linesUtil.bc(c + j, width), width)] * mask[j + n]
            k[l] = tot

def convolve_gauss( image, width, height, sigma):
    """
    convolve gauss
    :param image:
    :param width:
    :param height:
    :param sigma:
    :return:
    """
    k = [[0 for ii in range(width * height)] for i in range(5)]
    n0,mask0=_compute_gauss_mask_0(sigma)
    n1, mask1 = _compute_gauss_mask_1(sigma)
    n2, mask2 = _compute_gauss_mask_2(sigma)

    conv_r0 = [0 for ii in range(width * height)]
    conv_r1 = [0 for ii in range(width * height)]
    conv_r2 = [0 for ii in range(width * height)]

    convolve_rows_gauss(image, mask0, n0, conv_r0, width, height)
    convolve_rows_gauss(image, mask1, n1, conv_r1, width, height)
    convolve_rows_gauss(image, mask2, n2, conv_r2, width, height)
    ''' linesUtil.DERIV_R case'''
    convolve_cols_gauss(conv_r1, mask0, n0, k[0], width, height)
    ''' linesUtil.DERIV_C case'''
    convolve_cols_gauss(conv_r0, mask1, n1, k[1], width, height)
    ''' linesUtil.DERIV_RR case'''
    convolve_cols_gauss(conv_r2, mask0, n0, k[2], width, height)
    ''' linesUtil.DERIV_RC case'''
    convolve_cols_gauss(conv_r1, mask1, n1, k[3], width, height)
    ''' linesUtil.DERIV_CC case'''
    convolve_cols_gauss(conv_r0, mask2, n2, k[4], width, height)
    return k