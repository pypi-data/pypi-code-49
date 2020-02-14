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


import logging
from math import sqrt
from ridge_detection.linesUtil import MODE_LIGHT
from ridge_detection.basicGeometry import Line, Junction
from ridge_detection.convol import convolve_gauss
from ridge_detection.link import compute_contours

from ridge_detection.helper import DEBUGGING

"""
The pixel boundaries need to be enlarged slightly since in practice it frequently happens for neighboring pixels a and b that pixel a says a maximum
lies within pixel b and vice versa. This presents no problem since linking algoritm will take care of this.
"""
PIXEL_BOUNDARY = 0.6

def solve_linear(a, b):
    """
    Solve the linear equation a*x+b=0 and return the result in t and the number of solutions in num.
    :param a:
    :param b:
    :return: the result and the number of solution
    """
    if a==0:
        return None,0
    return -b/a, 1


def compute_eigenvals( dfdrr, dfdrc, dfdcc, eigval, eigvec):
    """
    Compute the eigenvalues and eigenvectors of the Hessian matrix given by dfdrr, dfdrc, and dfdcc, and sort them in descending order according to their absolute values
    :param dfdrr:
    :param dfdrc:
    :param dfdcc:
    :param eigval:
    :param eigvec:
    :return:
    """
    """Compute the eigenvalues and eigenvectors of the Hessian matrix"""
    c = 1.0
    s = 0.0
    e1 = dfdrr
    e2 = dfdcc
    if dfdrc!=0.0:
        theta = 0.5 * (dfdcc - dfdrr) / dfdrc
        t = 1.0 / (abs(theta) + sqrt(theta * theta + 1.0))
        if theta < 0.0:
            t = -t
        c = 1.0 / sqrt(t * t + 1.0)
        s = t * c
        e1 = dfdrr - t * dfdrc
        e2 = dfdcc + t * dfdrc
    n1 = c
    n2 = -s

    """If the absolute value of an eigenvalue is larger than the other, put that eigenvalue into first position. If both are of equal absolute value, put the negative one first."""
    if abs(e1) > abs(e2):
        eigval[0] = e1
        eigval[1] = e2
        eigvec[0][0] = n1
        eigvec[0][1] = n2
        eigvec[1][0] = -n2
        eigvec[1][1] = n1
    elif abs(e1) < abs(e2):
        eigval[0] = e2
        eigval[1] = e1
        eigvec[0][0] = -n2
        eigvec[0][1] = n1
        eigvec[1][0] = n1
        eigvec[1][1] = n2
    else:
        if e1 < e2:
            eigval[0] = e1
            eigval[1] = e2
            eigvec[0][0] = n1
            eigvec[0][1] = n2
            eigvec[1][0] = -n2
            eigvec[1][1] = n1
        else:
            eigval[0] = e2
            eigval[1] = e1
            eigvec[0][0] = -n2
            eigvec[0][1] = n1
            eigvec[1][0] = n1
            eigvec[1][1] = n2



def compute_line_points(ku, ismax, ev, nx, ny, px, py, width, height, low, high, mode):
    """
    For each point in the image determine whether there is a local maximum of the second directional derivative in the direction (nx[l],ny[l]) within the
    pixels's boundaries. If so, set ismax[l] to 2 if the eigenvalue ev[l] is larger than high, to 1 if ev[l] is larger than low, and to 0 otherwise.
    Furthermore, put the sub-pixel position of the maximum into (px[l],py[l]). The parameter mode determines whether maxima (dark lines points) or minima
    (bright line points) should be selected. The partial derivatives of the image are input as ku[].
    :param ismax:           variable byte
    :param ev:
    :param nx:
    :param ny:
    :param px:
    :param py:
    :param width:
    :param height:
    :param low:
    :param high:
    :param mode:
    :return:
    """
    k = [0, 0, 0, 0, 0]
    eigval = [0, 0]
    eigvec = [[0,0], [0,0]]
    for r in list(range(0,height)):
        for c in list(range(0, width)):
            l= r * width + c               # it is lincoord(row, col,width) of linesUtil.py
            k[0] = ku[0][l]
            k[1] = ku[1][l]
            k[2] = ku[2][l]
            k[3] = ku[3][l]
            k[4] = ku[4][l]
            compute_eigenvals(k[2], k[3], k[4], eigval, eigvec)
            val = -eigval[0] if mode == MODE_LIGHT else eigval[0]
            if val>0.0:
                ev[l] = float(val)
                n1 = eigvec[0][0]
                n2 = eigvec[0][1]
                a = k[2] * n1 * n1 + 2.0 * k[3] * n1 * n2 + k[4] * n2 * n2
                b = k[0] * n1 + k[1] * n2
                t,num= solve_linear(a, b)
                if num != 0:
                    p1 = t * n1
                    p2 = t * n2
                    if abs(p1) <= PIXEL_BOUNDARY and abs(p2) <= PIXEL_BOUNDARY:
                        if val >= low:
                            ismax[l] = 2 if val >= high else 1
                        nx[l] = float(n1)
                        ny[l] = float (n2)
                        px[l] = float (r + p1)
                        py[l] = float (c + p2)



def detect_lines(image, width, height, contours,  sigma, low, high, mode, compute_width, correct_pos, extend_lines, junctions):
    """
    :param image:
    :param width:
    :param height:
    :param contours:
    :param sigma:
    :param low:
    :param high:
    :param mode:
    :param compute_width:
    :param correct_pos:
    :param extend_lines:
    :param junctions:
    :return:            since 'num_result' was by reference it returns it --> used is num_result=detect_lines(....,num_result,...)
    """
    from ridge_detection.width import compute_line_width

    if not isinstance(contours,list) or (len(contours) > 0 and not isinstance(contours[0],Line)):
        print("ERROR : The 'contours' input value has to be a list of instances of the class 'Line'. (position.py->detect_lines)")
        logging.error(" The 'contours' input value has to be a list of instances of the class 'Line'. (position.py->detect_lines)")
        exit(-1)
    if not isinstance(junctions, list) or (len(junctions) > 0 and not isinstance(junctions[0], Junction)):
        print("ERROR: The 'junctions' input value has to be a list of instances of the class 'Junction'. (position.py->detect_lines)")
        logging.error(" The 'junctions' input value has to be a list of instances of the class 'Junction'. (position.py->detect_lines)")
        exit(-1)

    k=convolve_gauss(image,width,height,sigma)


    ismax = [0 for i in range(width * height)]       # it was a byte[]
    ev = [0 for i in range(width * height)]
    n1 = [0 for i in range(width * height)]
    n2 = [0 for i in range(width * height)]
    p1 = [0 for i in range(width * height)]
    p2 = [0 for i in range(width * height)]

    compute_line_points(k, ismax, ev, n1, n2, p1, p2, width, height, low, high, mode)

    num_result = compute_contours(ismax, ev, n1, n2, p1, p2, k[0], k[1], contours, sigma, extend_lines, mode, width, height, junctions)
    if DEBUGGING is True:
        logging.debug ("output contours")
        for c in contours:
            logging.debug (str(c))
    if compute_width is True:
        compute_line_width(k[0], k[1], width, height, sigma, mode, correct_pos, contours)
    return num_result