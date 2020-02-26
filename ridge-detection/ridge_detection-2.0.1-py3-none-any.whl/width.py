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
from ridge_detection.helper import Offset
from numpy import sign
from math import ceil,sqrt,sin,cos,floor
from ridge_detection.basicGeometry import Line
from ridge_detection.linesUtil import COUNTOUR_DICT,MODE_LIGHT,lincoord,br,bc
from ridge_detection.correct import Correction,Correct,get_ctableh4CorrectObj
from ridge_detection.convol import phi2
from ridge_detection.position import solve_linear, compute_eigenvals

"""
This constant is introduced because for very narrow lines the facet model width detection scheme sometimes extracts the line width too narrow. Since
the correction function has a very steep slope in that area, this will lead to lines of almost zero width, especially since the bilinear interpolation in
correct.c will tend to overcorrect. Therefore it is wise to make the extracted line width slightly larger before correction.
"""
LINE_WIDTH_COMPENSATION = 1.05

""" Minimum line width allowed (used for outlier check in fix_locations()) """
MIN_LINE_WIDTH = 0.1

""" Maximum contrast allowed (used for outlier check in fix_locations()) """
MAX_CONTRAST = 275.0


def bresenham(nx,  ny,  px,  py,  length,  line ):
    """
    Modified Bresenham algorithm. It returns in line all pixels that are intersected by a half line less than length away from the point (px,py) aint
    the direction (nx,ny). The point (px,py) must lie within the pixel of the origin, i.e., fabs(px) <= 0.5 and fabs(py) <= 0.5.
    :param nx:
    :param ny:
    :param px:
    :param py:
    :param length:
    :param line: It has a list of Offset obj
    :return: the number of the points founded (NB: in the java code was the fake reference param "num_points"
    """
    if isinstance(line,list) and len(line)> 0:
        for l in line:
            if not isinstance(l,Offset):
                print("ERROR: The input 'line' has to be a not empty list of instances of the class 'Offset'. (width.py->bresenham)")
                logging.error("ERROR: The input 'line' has to be a not empty list of instances of the class 'Offset'. (width.py->bresenham)")
                exit(-1)
    else:
        print("ERROR: The input 'line' has to be a not empty list of instances of the class 'Offset'. (width.py->bresenham)")
        logging.error("ERROR: The input 'line' has to be a not empty list of instances of the class 'Offset'. (width.py->bresenham)")
        exit(-1)
    x = 0
    y = 0
    dx = abs(nx)
    dy = abs(ny)
    s1 = int(sign(nx))
    s2 = int(sign(ny))
    px *= s1
    py *= s2
    xchg = 0
    if dy > dx:
        t = dx
        dx = dy
        dy = t
        t = px
        px = py
        py = t
        xchg = 1


    maxit = int (ceil(length * dx))
    e = (0.5 - px) * dy / dx - (0.5 - py)
    n = 0

    for i in list(range(maxit+1)):
        line[n].x = x
        line[n].y = y
        n +=1

        while e >= -1e-8:
            if xchg != 0:
                x += s1
            else:
                y += s2
            e-=1
            if e > -1:
                line[n].x = x
                line[n].y = y
                n+=1
        if xchg != 0:
            y += s2
        else:
            x += s1
        e += dy / dx

    return n


def fill_gaps(master=[], slave1=[], slave2=[], cont=None):
    """
    Fill gaps in the arrays master, slave1, and slave2, i.e., points where
	master=0, by interpolation (interior points) or extrapolation (end points). The array master will usually be the width of the line, while slave1 and
	slave2 will be values that depend on master[i] being 0, e.g., the gradient at each line point. The arrays slave1 and slave2 can be NULL.
    :param master:
    :param slave1:
    :param slave2:
    :param cont:
    :return:
    """
    if not isinstance(master,list) or not isinstance(slave1,list) or not isinstance(slave2,list):
        print ( "ERROR: The input 'master', 'slave1', and 'slave2' have to be vector. (width.py->fill_gaps)")
        logging.error ( "The input 'master', 'slave1', and 'slave2' have to be vector. (width.py->fill_gaps)")
        exit(-1)
    if not isinstance(cont, Line):
        print("ERROR: The 'cont' param has to be an instance of the class 'Line'. (width.py->fill_gaps)")
        logging.error("ERROR: The 'cont' param has to be an instance of the class 'Line'. (width.py->fill_gaps)")
        exit(-1)

    num_points = cont.num
    j=None          # I do not like this but I cannot change it and be sure that the behaviour will be the same

    for i in list(range(num_points)):
        if master[i] == 0:
            for j in list(range(i+1,num_points)):
                if master[j] > 0:
                    break
            if j is None:
                break
            m_s = 0
            m_e = 0
            s1_s = 0
            s1_e = 0
            s2_s = 0
            s2_e = 0
            if i>0 and j<num_points-1:
                s = i
                e = j - 1
                m_s = master[(s - 1)]
                m_e = master[(e + 1)]
                if len(slave1) >0:
                    s1_s = slave1[(s - 1)]
                    s1_e = slave1[(e + 1)]
                if len(slave2) > 0:
                    s2_s = slave2[(s - 1)]
                    s2_e = slave2[(e + 1)]
            elif i>0:
                s = i
                e = num_points - 2
                m_s = master[(s - 1)]
                m_e = master[(s - 1)]
                master[(e + 1)] = m_e
                if len(slave1) > 0:
                    s1_s = slave1[(s - 1)]
                    s1_e = slave1[(s - 1)]
                    slave1[(e + 1)] = s1_e
                if len(slave2) > 0:
                    s2_s = slave2[(s - 1)]
                    s2_e = slave2[(s - 1)]
                    slave2[(e + 1)] = s2_e
            elif j<num_points-1:
                s = 1
                e = j - 1
                m_s = master[(e + 1)]
                m_e = master[(e + 1)]
                master[(s - 1)] = m_s
                if len(slave1) > 0:
                    s1_s = slave1[(e + 1)]
                    s1_e = slave1[(e + 1)]
                    slave1[(s - 1)] = s1_s
                if len(slave2) > 0:
                    s2_s = slave2[(e + 1)]
                    s2_e = slave2[(e + 1)]
                    slave2[(s - 1)] = s2_s
            else:
                s = 1
                e = num_points - 2
                m_s = master[(s - 1)]
                m_e = master[(e + 1)]
                if len(slave1) > 0:
                    s1_s = slave1[(s - 1)]
                    s1_e = slave1[(e + 1)]
                if len(slave2) > 0:
                    s2_s = slave2[(s - 1)]
                    s2_e = slave2[(e + 1)]

            arc_len = 0
            for  k in list(range(s,e+2)):
                d_r = cont.row[k] - cont.row[(k - 1)]
                d_c = cont.col[k] - cont.col[(k - 1)]
                arc_len += sqrt(d_r * d_r + d_c * d_c)

            l=0
            for k in list(range(s, e + 1)):
                d_r = cont.row[k] - cont.row[(k - 1)]
                d_c = cont.col[k] - cont.col[(k - 1)]
                l += sqrt(d_r * d_r + d_c * d_c)
                master[k] = (arc_len - l) / arc_len * m_s + l/ arc_len * m_e
                if len(slave1) > 0:
                    slave1[k] = (arc_len - l) / arc_len * s1_s + l / arc_len * s1_e
                if len(slave2) > 0:
                    slave2[k] = (arc_len - l) / arc_len * s2_s + l / arc_len * s2_e
            i=j                                                                         #todo: verificalo, in python nn ha senso ... cosa voleva fare? ha valore in java? Se si cambia primo loop in un while



def fix_locations( width_l,  width_r,  grad_l,  grad_r,  pos_x, pos_y,  correction,  contr,  asymm,  sigma,  mode, correct_pos, cont) :
    """
    Correct the extracted line positions and widths. The algorithm first closes gaps in the extracted data width_l, width_r, grad_l, and grad_r to provide
	meaningful input over the whole line. Then the correction is calculated. After this, gaps that have been introduced by the width correction are again
	closed. Finally, the position correction is applied if correct_pos is set. The results are returned in width_l, width_r, and cont
    :param width_l:
    :param width_r:
    :param grad_l:
    :param grad_r:
    :param pos_x:
    :param pos_y:
    :param correction:
    :param contr:
    :param asymm:
    :param sigma:
    :param mode:
    :param correct_pos:
    :param cont:
    :return:
    """
    if not isinstance(cont, Line):
        print("ERROR: The 'cont' param has to be an instance of the class 'Line'.")
        logging.error("ERROR: The 'cont' param has to be an instance of the class 'Line'.")
        exit(-1)

    w_est,r_est, w_est, r_est, w_real, h_real, corr, w_strong, w_weak, weak_is_r = 0,0,0,0,0,0,0,0,0,0

    fill_gaps(width_l, grad_l, slave2=[], cont=cont)
    fill_gaps(width_r, grad_r, slave2=[], cont=cont)

    num_points = cont.num
    """ Calculate true line width, asymmetry, and position correction """
    if correct_pos is True:
        """ Do not correct the position of a junction point if its width is found by interpolation, i.e., if the position could be corrected differently for each junction point, thereby destroying the junction."""
        correct_start = ((cont.cont_class == COUNTOUR_DICT["cont_no_junc"] or cont.cont_class == COUNTOUR_DICT["cont_end_junc"] or cont.cont_class == COUNTOUR_DICT["cont_closed"])
            and (width_r[0] > 0 and width_l[0] > 0))
        correct_end = ((cont.cont_class == COUNTOUR_DICT["cont_no_junc"] or cont.cont_class ==
                          COUNTOUR_DICT["cont_start_junc"] or cont.cont_class == COUNTOUR_DICT["cont_closed"])
                         and (width_r[(num_points - 1)] > 0 and width_l[(num_points - 1)] > 0))

        """ Calculate the true width and assymetry, and its corresponding correction for each line point"""
        precalculated_ctable4Correct_obj=get_ctableh4CorrectObj()
        for i in list(range(num_points)):
            if width_r[i] > 0 and width_l[i] > 0:
                w_est = (width_r[i] + width_l[i]) * LINE_WIDTH_COMPENSATION
                if grad_r[i] <= grad_l[i]:
                    r_est = grad_r[i] / grad_l[i]
                    weak_is_r = True
                else:
                    r_est = grad_l[i] / grad_r[i]
                    weak_is_r = False
                correctObj =Correct(precalculated_ctable4Correct_obj)
                correctionObj = Correction(w_est, r_est, w_real, h_real, corr, w_strong, w_weak)
                correctObj.line_corrections(sigma, correctionObj)
                w_real=correctionObj.w/LINE_WIDTH_COMPENSATION
                corr = correctionObj.correction / LINE_WIDTH_COMPENSATION
                width_r[i] = w_real
                width_l[i] = w_real
                if weak_is_r is True:
                    asymm[i] = correctionObj.h
                    correction[i] = -corr
                else:
                    asymm[i] = -correctionObj.h
                    correction[i] = corr

        fill_gaps(width_l, correction, asymm, cont)
        for i in list(range(0,num_points)):
            width_r[i] = width_l[i]

        """ Adapt the correction for junction points if necessary """
        if  not correct_start:
            correction[0] = 0
        if not correct_end:
            correction[(num_points - 1)] = 0

        for i in list(range(0, num_points)):
            px = pos_x[i]
            py = pos_y[i]
            nx = cos(cont.angle[i])
            ny = sin(cont.angle[i])
            px = px + correction[i] * nx
            py = py + correction[i] * ny
            pos_x[i] = px
            pos_y[i] = py

    """ Update the position of a line and add the extracted width """
    cont.width_l = [float for i in range(num_points)]
    cont.width_r = [float for i in range(num_points)]
    for i in list(range(0, num_points)):
        cont.width_l[i] = width_l[i]
        cont.width_r[i] = width_r[i]
        cont.row[i] = pos_x[i]
        cont.col[i] = pos_y[i]

    """  Now calculate the true contrast """
    if correct_pos is True:
        cont.asymmetry = [float for i in range(num_points)]
        cont.intensity = [float for i in range(num_points)]
        for i in list(range(0, num_points)):
            response = cont.response[i]
            asymmetry = abs(asymm[i])
            correct = abs(correction[i])
            width = cont.width_l[i]
            contrast = 0 if width<MIN_LINE_WIDTH else (response / abs(phi2(correct + width, sigma) + (asymmetry - 1) * phi2(correct - width, sigma)))
            if contrast>MAX_CONTRAST:
                contrast = 0
            contr[i] = contrast

        fill_gaps(contr, slave1=[], slave2=[], cont=cont)
        for i in list(range(0, num_points)):
            cont.asymmetry[i] = asymm[i]
            cont.intensity[i] = contr[i] if mode == MODE_LIGHT else -contr[i]



def compute_line_width(dx, dy, width, height, sigma, mode, correct_pos, contours):
    """
    Extract the line width by using a facet model line detector on an image of the absolute value of the gradient
    :param dx:
    :param dy:
    :param width:
    :param height:
    :param sigma:
    :param mode:
    :param correct_pos:
    :param contours:
    :return:
    """
    if (not isinstance(contours, list) or len(contours) == 0 ) or not isinstance(contours[0], Line):
        print("ERROR: The 'contours' input value has to be a list of instances of the class 'Line'. (width.py->compute_line_width)")
        logging.error("ERROR: The 'contours' input value has to be a list of instances of the class 'Line'. (width.py->compute_line_width)")
        exit(-1)

    eigvec = [[0,0], [0,0]]
    eigval = [0, 0]

    max_num_points =max([contour.num for contour in contours])


    width_l = [0 for i in range(max_num_points)]
    width_r = [0 for i in range(max_num_points)]
    grad_l = [0 for i in range(max_num_points)]
    grad_r = [0 for i in range(max_num_points)]
    pos_x = [0 for i in range(max_num_points)]
    pos_y = [0 for i in range(max_num_points)]
    grad = [0 for i in range(width * height)]

    length = 2.5 * sigma
    line = [Offset() for i in range( int (ceil(length * 3)) )]

    """ Compute the gradient image """
    for r in list(range(0, height)):
        for c in list(range(0, width)):
            l=r * width + c               # it is lincoord(row, col,width) of linesUtil.py
            grad[l] = sqrt(dx[l] * dx[l] + dy[l] * dy[l])

    for cont in contours:
        num_points = cont.num
        for j in list(range(0, num_points)):
            px = cont.row[j]
            py = cont.col[j]
            pos_x[j] = px
            pos_y[j] = py
            r = int(floor(px + 0.5))
            c = int(floor(py + 0.5))
            nx = cos(cont.angle[j])
            ny = sin(cont.angle[j])

            """ Compute the search line """
            num_line =bresenham(nx, ny, 0.0, 0.0, length, line)
            width_r[j] = width_l[j] = 0

            """ Look on both sides of the line """
            for d_r in [-1,1]:
                for k in list(range(0, num_line)):
                    x = br(r + d_r * line[k].x, height)
                    y = bc(c + d_r * line[k].y, width)
                    i1 = grad[lincoord(br(x - 1, height), bc(y - 1, width), width)]
                    i2 = grad[lincoord(br(x - 1, height), y, width)]
                    i3 = grad[lincoord(br(x - 1, height), bc(y + 1, width), width)]
                    i4 = grad[lincoord(x, bc(y - 1, width), width)]
                    i5 = grad[r * width + c] ## it is lincoord(row, col,width) of linesUtil.py
                    i6 = grad[lincoord(x, bc(y + 1, width), width)]
                    i7 = grad[lincoord(br(x + 1, height), bc(y - 1, width), width)]
                    i8 = grad[lincoord(br(x + 1, height), y, width)]
                    i9 = grad[lincoord(br(x + 1, height), bc(y + 1, width), width)]
                    t1 = i1 + i2 + i3
                    t2 = i4 + i5 + i6
                    t3 = i7 + i8 + i9
                    t4 = i1 + i4 + i7
                    t5 = i2 + i5 + i8
                    t6 = i3 + i6 + i9
                    dr = (t3 - t1) / 6
                    dc = (t6 - t4) / 6
                    drr = (t1 - 2 * t2 + t3) / 6
                    dcc = (t4 - 2 * t5 + t6) / 6
                    drc = (i1 - i3 - i7 + i9) / 4
                    compute_eigenvals(2 * drr, drc, 2 * dcc, eigval, eigvec)
                    val = -eigval[0]
                    if val > 0.0:
                        n1 = eigvec[0][0]
                        n2 = eigvec[0][1]
                        a = 2.0 * (drr * n1 * n1 + drc * n1 * n2 + dcc * n2 * n2)
                        b = dr * n1 + dc * n2
                        t,num= solve_linear(a, b)
                        if num != 0:
                            p1 = t * n1
                            p2 = t * n2
                            if abs(p1) <= 0.5 and abs(p2) <= 0.5:
                                """ Project the maximum point position perpendicularly onto the search line """
                                b = nx * (px - (r + d_r * line[k].x + p1)) + ny * (py - (c + d_r * line[k].y + p2))
                                t,num = solve_linear(1, b)
                                d = (-i1 + 2 * i2 - i3 + 2 * i4 + 5 * i5 + 2 * i6 - i7 + 2 * i8 - i9) / 9
                                if d_r ==1 :
                                    grad_r[j] = d + p1 * dr + p2 * dc + p1 * p1 * drr + p1 * p2 * drc + p2 * p2 * dcc
                                    width_r[j] = abs(t)
                                else:
                                    grad_l[j] = d + p1 * dr + p2 * dc + p1 * p1 * drr + p1 * p2 * drc + p2 * p2 * dcc
                                width_l[j] = abs(t)
                                break

        correct = [0 for i in range(max_num_points)]
        contrast = [0 for i in range(max_num_points)]
        asymm = [0 for i in range(max_num_points)]
        fix_locations(width_l, width_r, grad_l, grad_r, pos_x, pos_y, correct, contrast, asymm, sigma, mode, correct_pos, cont)
