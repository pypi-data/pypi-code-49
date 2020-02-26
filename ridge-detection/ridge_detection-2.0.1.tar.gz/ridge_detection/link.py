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



from ridge_detection.helper import Offset,threshold
from math import pi,floor,atan2,sqrt, ceil, cos,sin
from ridge_detection import linesUtil
from ridge_detection.basicGeometry import Line, Junction, Region
from operator import attrgetter
import logging
from ridge_detection.helper import DEBUGGING

MAX_ANGLE_DIFFERENCE = pi / 6.0
DOUBLE_MAX_VALUE_JAVA= 1.7976931348623157E308
"""
This table contains the three appropriate neighbor pixels that the linking algorithm must examine. 
It is indexed by the octant the current line angle lies in, e.g., 0 if the angle in degrees lies within [-22.5,22.5].
"""
dirtab= [ [ [ 1, 0 ], [ 1, -1 ], [ 1, 1 ] ], [ [ 1, 1 ], [ 1, 0 ], [ 0, 1 ] ],
			[ [ 0, 1 ], [ 1, 1 ], [ -1, 1 ] ], [ [ -1, 1 ], [ 0, 1 ], [ -1, 0 ] ], [ [ -1, 0 ], [ -1, 1 ], [ -1, -1 ] ],
			[ [ -1, -1 ], [ -1, 0 ], [ 0, -1 ] ], [ [ 0, -1 ], [ -1, -1 ], [ 1, -1 ] ],
			[ [ 1, -1 ], [ 0, -1 ], [ 1, 0 ] ] ]

""" This table contains the two neighbor pixels that the linking algorithm should examine and mark as processed in case there are double responses """
cleartab =  [ [ [ 0, 1 ], [ 0, -1 ] ], [ [ -1, 1 ], [ 1, -1 ] ],
			[ [ -1, 0 ], [ 1, 0 ] ], [ [ -1, -1 ], [ 1, 1 ] ], [ [ 0, -1 ], [ 0, 1 ] ], [ [ 1, -1 ], [ -1, 1 ] ],
			[ [ 1, 0 ], [ -1, 0 ] ], [ [ 1, 1 ], [ -1, -1 ] ] ]

class Crossref:
    """
    Storage the Crossref variables, it is the Correction.java code
    This data structure facilitates the quick search for the next possible starting point of a line. An array of crossrefs will be accumulated and
    sorted according to its value. x and y are the coordinates of a point in the image. When this point has been processed it will be marked as done.
    """
    def __init__(self,x=None, y=None, value=None, done=None):
        self.x = x
        self.y = y
        self.value = value
        self.done = done

    def compareTo(self, crossref0):
        if not isinstance(crossref0, Crossref):
            print("ERROR: The input of 'Crossref.compareTo' has to be an instance of the class 'Crossref'. (link.py->detect_lines)")
            logging.error(" The input of 'Crossref.compareTo' has to be an instance of the class 'Crossref'.(link.py->detect_lines)")
            exit(-1)
        if self.value > crossref0.value:
            return  -1
        elif self.value < crossref0.value:
            return  1
        return 0

    def __str__(self):
        return "x: "+str(self.x)+"\ty: "+str(self.y)+"\tvalue: "+str(self.value)+"\tdone: "+str(self.done)

def interpolate_response( resp, x, y, px, py, width, height):
    """
    Compute the response of the operator with sub-pixel accuracy by using the facet model to interpolate the pixel accurate responses
    :param resp:
    :param x:
    :param y:
    :param px:
    :param py:
    :param width:
    :param height:
    :return:
    """
    i1 = resp[linesUtil.lincoord(linesUtil.br(x - 1, height), linesUtil.bc(y - 1, width), width)]
    i2 = resp[linesUtil.lincoord(linesUtil.br(x - 1, height), y, width)]
    i3 = resp[linesUtil.lincoord(linesUtil.br(x - 1, height), linesUtil.bc(y + 1, width), width)]
    i4 = resp[linesUtil.lincoord(x, linesUtil.bc(y - 1, width), width)]
    i5 = resp[linesUtil.lincoord(x, y, width)]
    i6 = resp[linesUtil.lincoord(x, linesUtil.bc(y + 1, width), width)]
    i7 = resp[linesUtil.lincoord(linesUtil.br(x + 1, height), linesUtil.bc(y - 1, width), width)]
    i8 = resp[linesUtil.lincoord(linesUtil.br(x + 1, height), y, width)]
    i9 = resp[linesUtil.lincoord(linesUtil.br(x + 1, height), linesUtil.bc(y + 1, width), width)]
    t1 = i1 + i2 + i3
    t2 = i4 + i5 + i6
    t3 = i7 + i8 + i9
    t4 = i1 + i4 + i7
    t5 = i2 + i5 + i8
    t6 = i3 + i6 + i9
    d = (-i1 + 2 * i2 - i3 + 2 * i4 + 5 * i5 + 2 * i6 - i7 + 2 * i8 - i9) / 9
    dr = (t3 - t1) / 6
    dc = (t6 - t4) / 6
    drr = (t1 - 2 * t2 + t3) / 6
    dcc = (t4 - 2 * t5 + t6) / 6
    drc = (i1 - i3 - i7 + i9) / 4
    xx = px - x
    yy = py - y
    return d + xx * dr + yy * dc + xx * xx * drr + xx * yy * drc + yy * yy * dcc


def closest_point(lx,  ly,  dx,  dy,  px,  py):
    """
    Calculate the closest point to (px,py) on the line (lx,ly) + t*(dx,dy)
    :param lx:
    :param ly:
    :param dx:
    :param dy:
    :param px:
    :param py:
    :return:
    """
    mx = px - lx
    my = py - ly
    den = dx * dx + dy * dy
    nom = mx * dx + my * dy
    tt = nom/den if den!=0 else 0
    return lx + tt * dx, ly + tt * dy, tt


def interpolate_gradient(gradx, grady, px, py, width):
    """
    Interpolate the gradient of the gradient images gradx and grady with width width at the point (px,py) using linear interpolation
    :param gradx:
    :param grady:
    :param px:
    :param py:
    :param width:
    :return:
    """
    gix = floor(px)
    giy = floor(py)
    gfx = px % 1.0
    gfy = py % 1.0
    gpos = linesUtil.lincoord(gix, giy, width)
    gx1 = gradx[gpos]
    gy1 = grady[gpos]
    gpos = linesUtil.lincoord(gix + 1, giy, width)
    gx2 = gradx[gpos]
    gy2 = grady[gpos]
    gpos = linesUtil.lincoord(gix, giy + 1, width)
    gx3 = gradx[gpos]
    gy3 = grady[gpos]
    gpos = linesUtil.lincoord(gix + 1, giy + 1, width)
    gx4 = gradx[gpos]
    gy4 = grady[gpos]
    return ((1 - gfy) * ((1 - gfx) * gx1 + gfx * gx2) + gfy * ((1 - gfx) * gx3 + gfx * gx4)), ((1 - gfy) * ((1 - gfx) * gy1 + gfx * gy2) + gfy * ((1 - gfx) * gy3 + gfx * gy4))


def compute_contours(ismax, eigval,  normx, normy, posx,  posy, gradx, grady, contours, sigma, extend_lines,mode, width, height,junctions):
    """
    This function links the line points into lines. The input to this function are the response of the filter, i.e., the second directional derivative along
    (nx[l],ny[l]), contained in eigval[l], and the sub-pixel position of each line point, contained in (px[l],py[l]). The parameters low and high are the
    hysteresis thresholds for the linking, while width and height are the dimensions of the five float-images. The linked lines are returned in result, and the number of lines detected is returned in num_result
    :param self:
    :param ismax:
    :param eigval:
    :param normx:
    :param normy:
    :param posx:
    :param posy:
    :param gradx:
    :param grady:
    :param contours:
    #:param num_result: era passata per riferimento e quindi la ho eliminata
    :param sigma:
    :param extend_lines:
    :param mode:
    :param width:
    :param height:
    :param junctions:
    :return:
    """

    """
    stuff to know.
    Since it allocated the memory before inserting a new junc,line etc he had some variables like num_pnt to know how many elements eh had in the list in a given moment.
    We do that in real time without allocating extra memory hence we do not need this extra variable but we used len(obj) e.g. num_pnt==len(row)
    """
    from ridge_detection.width import bresenham
    i,k,j,m=0,0,0,0
    num_junc,num_cont = 0, 0
    end_angle, end_resp=0,0
    cont = []
    junc = []
    """The image indx is an index into the table of all pixels that possibly could be starting points for new lines. It is used to quickly determine the next starting point of a line"""
    indx = [0 for ii in range(width * height)]

    """ The image label contains information on the pixels that have been processed by the linking algorithm"""
    label = [0 for ii in range(width * height)]

    """ Select all pixels that can be starting points for lines """
    seg = Region()
    threshold(ismax, 2, width, height, seg)

    """ Count the number of possible starting points """
    area = 0
    for i in range(seg.num):
        area += seg.get_line(i).ce - seg.get_line(i).cb + 1

    """ Create the index of possible starting points """
    cross=list()
    for i in range(seg.num):
        rl= seg.get_line(i)
        for y in list(range(rl.cb,rl.ce+1)):
            pos =  rl.r * width + y               # it is lincoord(row, col,width) of linesUtil.py
            cross.append(Crossref(x=rl.r, y=y, value=eigval[pos], done = False))

    """
    https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python. I use this python sort to simulate the "Crossref.java -> compareTo function used in java.util.Arrays.sort(cross) 
    """
    cross.sort(key=attrgetter('value'), reverse=True)

    if DEBUGGING is True:
        logging.debug("stampa valori dei crossRef:")
        for index,crossref in enumerate(cross):
            logging.debug(str(index)+"\t"+str(crossref))

    for i in range(area):
        indx[linesUtil.lincoord(cross[i].x, cross[i].y, width)] = i + 1

    """ Link lines points"""
    indx_max,nextalpha,diff,diff2 = 0,0,0,0
    x,y = 0,0
    while True:
        row = list()
        col = list()
        angle = list()
        resp = list()
        """ Contour class unknown at this point; therefore assume both ends free """
        cls = linesUtil.COUNTOUR_DICT["cont_no_junc"]
        while indx_max < area and cross[indx_max].done:
            indx_max+=1

        """ Stop if no feasible starting point exists. """
        if indx_max == area:
            break
        maxx = cross[indx_max].x
        maxy = cross[indx_max].y
        if cross[indx_max].value == 0.0:
            break

        """ Add starting point to the line """
        pos =  maxx * width + maxy               # it is lincoord(row, col,width) of linesUtil.py
        label[pos] = num_cont + 1
        if not indx[pos] == 0:
            cross[(indx[pos] - 1)].done = True
        row.append(posx[pos])
        col.append( posy[pos])
        """Select line direction"""
        nx = -normy[pos]
        ny = normx[pos]

        alpha = atan2(ny, nx)
        if alpha < 0.0:
            alpha += 2.0 * pi
        if alpha >= pi:
            alpha -= pi

        octant = int (floor(4.0 / pi * alpha + 0.5)) % 4

        """ 
        Select normal to the line. The normal points to the right of the line as the line is traversed from 0 to num-1. Since the points are sorted in reverse
		order before the second iteration, the first beta actually has to point to the left of the line!
		"""
        beta = alpha + pi / 2.0
        if beta >= 2.0 * pi:
            beta -= 2.0 * pi
        angle.append( beta)
        resp.append(interpolate_response(eigval, maxx, maxy, posx[pos], posy[pos], width, height))

        """ Mark double responses as processed """
        for ii in [0,1]:
            nextx = maxx + cleartab[octant][ii][0]
            nexty = maxy + cleartab[octant][ii][1]
            if nextx < 0 or nextx >= height or nexty < 0 or nexty >= width:
                continue
            nextpos = linesUtil.lincoord(nextx, nexty, width)
            if ismax[nextpos] > 0:
                nx = -normy[nextpos]
                ny = normx[nextpos]
                nextalpha = atan2(ny, nx)
                if nextalpha < 0.0:
                    nextalpha += 2.0 * pi
                if nextalpha >= pi:
                    nextalpha -= pi
                diff = abs(alpha - nextalpha)
                if diff >= pi / 2.0:
                    diff = pi - diff
                if diff < MAX_ANGLE_DIFFERENCE:
                    label[nextpos] = num_cont + 1
                    if not indx[nextpos] == 0:
                        cross[(indx[nextpos] - 1)].done = True

        for it in [1,2]:
            if it ==1:
                """ Search along the initial line direction in the first iteration """
                x = maxx
                y = maxy
                pos = linesUtil.lincoord(x, y, width)
                nx = -normy[pos]
                ny = normx[pos]
                alpha = atan2(ny,nx)
                if alpha < 0.0:
                    alpha += 2.0 * pi
                if alpha >= pi:
                    alpha -= pi
                last_octant = int(floor(4.0 / pi * alpha + 0.5)) % 4
                last_beta = alpha + pi/ 2.0
                if last_beta >= 2.0 * pi:
                    last_beta -= 2.0 * pi
            else:
                """ Search in the opposite direction in the second iteration """
                x = maxx
                y = maxy
                pos = linesUtil.lincoord(x, y, width)
                nx = -normy[pos]
                ny = normx[pos]
                alpha = atan2(ny, nx)
                if alpha < 0.0:
                    alpha += 2.0 * pi
                if alpha >= pi:
                    alpha -= pi
                last_octant = int(floor(4.0 / pi * alpha + 0.5)) % 4 + 4
                last_beta = alpha + pi / 2.0
                if last_beta >= 2.0 * pi:
                    last_beta -= 2.0 * pi


            if it==2:
                """ Sort the points found in the first iteration in reverse """
                row.reverse()
                col.reverse()
                angle.reverse()
                resp.reverse()


            """ Now start adding appropriate neighbors to the line """
            while True:
                """ Orient line direction w.r.t. the last line direction. """
                pos = x * width + y               # it is lincoord(row, col,width) of linesUtil.py
                nx = -normy[pos]
                ny = normx[pos]
                px = posx[pos]
                py = posy[pos]
                """ Orient line direction w.r.t. the last line direction """
                alpha = atan2(ny,nx)
                if alpha < 0.0:
                    alpha += 2.0 * pi
                if alpha >= pi:
                    alpha -= pi
                octant = int(floor(4.0 / pi * alpha + 0.5)) % 4
                if octant ==0:
                    if 3<= last_octant <= 5 :
                        octant = 4
                if octant ==1:
                    if 4<= last_octant <= 6 :
                        octant = 5
                if octant ==2:
                    if 4<= last_octant <= 7 :
                        octant = 6
                if octant ==3:
                    if  last_octant ==0 or last_octant>=6:
                        octant = 7
                last_octant = octant

                """ Determine appropriate neighbor """
                nextismax = False
                nexti = 1
                mindiff = DOUBLE_MAX_VALUE_JAVA
                for i in [0,1,2]:
                    nextx = x + dirtab[octant][i][0]
                    nexty = y + dirtab[octant][i][1]
                    if nextx < 0 or nextx >= height or nexty < 0 or nexty >= width:
                        continue
                    nextpos =  nextx * width + nexty               # it is lincoord(row, col,width) of linesUtil.py
                    if ismax[nextpos] == 0:
                        continue

                    dx = posx[nextpos] - px
                    dy = posy[nextpos] - py
                    dist = sqrt(dx * dx + dy * dy)
                    nx = -normy[nextpos]
                    ny = normx[nextpos]
                    nextalpha = atan2(ny,nx)
                    if nextalpha < 0.0:
                        nextalpha += 2.0 * pi
                    if nextalpha >= pi:
                        nextalpha -= pi
                    diff = abs(alpha - nextalpha)
                    if diff >= pi / 2.0:
                        diff = pi - diff
                    diff += dist
                    if diff < mindiff :
                        mindiff = diff
                        nexti = i
                    if not ismax[nextpos] == 0:
                        nextismax = True

                """ Mark double responses as processed """
                for i in [0,1]:
                    nextx = x + cleartab[octant][i][0]
                    nexty = y + cleartab[octant][i][1]
                    if nextx < 0 or nextx >= height or nexty < 0 or nexty >= width:
                        continue
                    nextpos = nextx * width + nexty               # it is lincoord(row, col,width) of linesUtil.py
                    if ismax[nextpos] > 0:
                        nextalpha = atan2(normx[nextpos], -normy[nextpos])
                        if nextalpha < 0.0:
                            nextalpha += 2.0 * pi
                        if nextalpha >= pi:
                            nextalpha -= pi
                        diff = abs(alpha - nextalpha)
                        if diff >= pi / 2.0:
                            diff = pi - diff
                        if diff < MAX_ANGLE_DIFFERENCE:
                            label[nextpos] = num_cont + 1
                            if indx[nextpos] != 0:
                                cross[(indx[nextpos] - 1)].done = True

                """ Have we found the end of the line? """
                if not nextismax:
                    break
                """ If not, add the neighbor to the line """
                x += dirtab[octant][nexti][0]
                y += dirtab[octant][nexti][1]


                """
                29/08/2019
                https://github.com/thorstenwagner/ij-ridgedetection/issues/37
                There is a known bug in the java implementation. when it allocates more memory at the 'resp' array ln613-617 it set to 0 all the old value of the vector.
                It will be fixed BUT now I'm just translating the code and I want to reproduce the same results ... I introduce the bug in the code 
                """

                pos =  x * width + y               # it is lincoord(row, col,width) of linesUtil.py
                row.append( posx[pos])
                col.append( posy[pos])


                """ * Orient normal to the line direction w.r.t. the last normal."""
                nx = normx[pos]
                ny = normy[pos]
                beta = atan2(ny,nx)
                if beta < 0.0:
                    beta += 2.0 * pi
                if beta >= pi:
                    beta -= pi
                diff1 = abs(beta - last_beta)
                if diff1 >= pi:
                    diff1 = 2.0 * pi - diff1
                diff2 =abs(beta+pi-last_beta)
                if diff2>=pi:
                    diff2 = 2*pi-diff2
                if diff1 < diff2:
                    angle.append( beta)
                    last_beta = beta
                else:
                    angle.append( beta + pi)
                    last_beta = beta + pi

                resp.append(interpolate_response(eigval, x, y, posx[pos], posy[pos], width, height))

                """ If the appropriate neighbor is already processed a junction point is found """
                if label[pos] > 0:

                    """  Look for the junction point in the other line. """
                    k = label[pos] - 1
                    if k == num_cont:
                        """ Line intersects itself """
                        for j in range(len(row)):
                            if row[j]==posx[pos] and col[j]==posy[pos]:
                                if j==0:
                                    """contour is closed"""
                                    cls = linesUtil.COUNTOUR_DICT["cont_closed"]
                                    row.reverse()
                                    col.reverse()
                                    angle.reverse()
                                    resp.reverse()
                                    it =2
                                else:
                                    if it==2:
                                        """ Determine contour class """
                                        cls = linesUtil.COUNTOUR_DICT["cont_both_junc"] if cls == linesUtil.COUNTOUR_DICT["cont_start_junc"] else linesUtil.COUNTOUR_DICT["cont_end_junc"]
                                        """ Index j is the correct index """
                                        junc.append( Junction(cont1=num_cont, cont2=num_cont, pos=j, x =posx[pos], y=posy[pos]) )
                                    else:
                                        """ Determine contour class """
                                        cls = linesUtil.COUNTOUR_DICT["cont_start_junc"]
                                        """ 
                                        Index len(row)-1-j is the correct index since the line is going to be sorted in reverse 
                                        """
                                        junc.append( Junction(cont1=num_cont, cont2=num_cont, pos= len(row) - 1 - j, x =posx[pos], y=posy[pos]) )
                                    num_junc += 1
                                break
                        """ Mark this case as being processed for the algorithm below """
                        j= -1
                    else:
                        for j in range(cont[k].num):
                            if  len(cont)>k and len(cont[k].row )>0 and len(cont[k].col )>0 and cont[k].row[j] == posx[pos] and cont[k].col[j] == posy[pos]:
                                break
                            """ If no point can be found on the other line a double response must have occured. In this case, find the nearest point on the other line and add it to the current line"""
                        if j==cont[k].num:
                            mindist=DOUBLE_MAX_VALUE_JAVA
                            j= -1
                            for l in range(cont[k].num):
                                dx = posx[pos] - cont[k].row[l]
                                dy = posy[pos] - cont[k].col[l]
                                dist = sqrt(dx * dx + dy * dy)
                                if dist<mindist:
                                    mindist=dist
                                    j=l
                            """ Add the point with index j to the current line """
                            """
                            29/08/2019
                            https://github.com/thorstenwagner/ij-ridgedetection/issues/37
                            There is a known bug in the java implementation. when it allocates more memory at the 'resp' array ln768-772 it set to 0 all the old value of the vector.
                            It will be fixed BUT now I'm just translating the code and I want to reproduce the same results ... I introduce the bug in the code 
                            """

                            row.append( cont[k].row[j])
                            col.append(cont[k].col[j])
                            beta = cont[k].angle[j]
                            if beta >= pi:
                                beta -= pi
                            diff1 = abs(beta - last_beta)
                            if diff1 >= pi:
                                diff1 = 2.0 * pi - diff1
                            diff2 = abs(beta + pi - last_beta)
                            if diff2 >= pi:
                                diff2 = 2.0 * pi - diff2
                            if diff1 < diff2:
                                angle.append( beta)
                            else:
                                angle.append(beta + pi)
                            resp.append( cont[k].response[j])

                    """ Add the junction point only if it is not one of the other line's endpoints """
                    if 0<j<cont[k].num:
                        """ Determine contour class """
                        if it ==1:
                            cls = linesUtil.COUNTOUR_DICT["cont_start_junc"]
                        elif cls == linesUtil.COUNTOUR_DICT["cont_start_junc"]:
                            cls= linesUtil.COUNTOUR_DICT["cont_both_junc"]
                        else:
                            cls = linesUtil.COUNTOUR_DICT["cont_end_junc"]
                        """ Add the new junction """
                        junc.append(Junction(cont1=k, cont2=num_cont, pos=j, x=row[-1], y=col[-1]))
                        num_junc += 1
                    break

                label[pos]=num_cont+1
                if not indx[pos]==0:
                    cross[(indx[pos] - 1)].done = True

        if len(row)>1:
            """ Only add lines with at least two points """
            cont.append(Line(num=len(row), row = row, col = col, angle = angle, response = resp, cont_class=cls))
            num_cont +=1
        else:
            """ Delete the point from the label image; we can use maxx and maxy as the coordinates in the label image in this case """
            for i in [-1,0,1]:
                for j in [-1, 0, 1]:
                    pos = linesUtil.lincoord(linesUtil.br(maxx + i, height), linesUtil.bc(maxy + j, width), width)
                    if label[pos] == num_cont+1:
                        label[pos]=0

    """ Now try to extend the lines at their ends to find additional junctions """
    if extend_lines is True:
        """ Sign by which the gradient has to be multiplied below """
        s =1 if mode == linesUtil.MODE_LIGHT else -1
        length = 2.5*sigma
        max_line = int (ceil(length * 3))
        line = [Offset() for ii in range(max_line)]
        exty = [0 for ii in range(max_line)]
        extx = [0 for ii in range(max_line)]
        for i,tmp_cont in enumerate(cont):
            num_pnt = tmp_cont.num
            if tmp_cont.num == 1:
                continue
            if tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_closed"]:
                continue
            trow = tmp_cont.row
            tcol = tmp_cont.col
            tangle = tmp_cont.angle
            tresp = tmp_cont.response

            """ Check both ends of the line (it==-1: start, it==1: end) """
            for it in [-1,  1]:
                """ Determine the direction of the search line. This is done by using the normal to the line (angle). Since this normal may point to the left of the line (see
                below) we have to check for this case by comparing the normal to the direction of the line at its respective end point """
                if it == -1:
                    """ start point of the line"""
                    if tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_start_junc"] or tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_both_junc"] :
                        continue
                    dx = trow[1] - trow[0]
                    dy = tcol[1] - tcol[0]
                    alpha = tangle[0]
                    nx = cos(alpha)
                    ny = sin(alpha)
                    if nx * dy - ny * dx < 0:
                        """ Turn the normal by +90 degrees """
                        mx = -ny
                        my = nx
                    else:
                        """ Turn the normal by -90 degrees """
                        mx = ny
                        my = -nx
                    px = trow[0]
                    py = tcol[0]
                    response = tresp[0]
                else:
                    """ end point of the line"""
                    if tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_end_junc"] or tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_both_junc"] :
                        continue
                    dx = trow[(num_pnt - 1)] - trow[(num_pnt - 2)]
                    dy = tcol[(num_pnt - 1)] - tcol[(num_pnt - 2)]
                    alpha = tangle[(num_pnt - 1)]
                    nx = cos(alpha)
                    ny = sin(alpha)
                    if nx * dy - ny * dx < 0:
                        """Turn the normal by -90 degrees"""
                        mx = ny
                        my = -nx
                    else:
                        """Turn the normal by +90 degrees"""
                        mx = -ny
                        my = nx
                    px = trow[(num_pnt - 1)]
                    py = tcol[(num_pnt - 1)]
                    response = tresp[(num_pnt - 1)]

                """ Determine the current pixel and calculate the pixels on the search line """
                x = int (floor(px + 0.5))
                y = int (floor(py + 0.5))
                dx = px - x
                dy = py - y
                num_line = bresenham(mx, my, dx, dy, length, line)

                """ Now determine whether we can go only uphill (bright lines) or downhill (dark lines) until we hit another line"""
                num_add = 0
                add_ext = False
                for k in range(num_line):
                    nextx = x + line[k].x
                    nexty = y + line[k].y
                    nextpx, nextpy, t = closest_point(px, py, mx, my, nextx, nexty)

                    """ Ignore points before or less than half a pixel away from the true end point of the line """
                    if t<=0.5:
                        continue

                    """ Stop if the gradient can't be interpolated any more or if the next point lies outside the image """
                    if nextpx < 0 or nextpy < 0 or nextpx >= height - 1 or nextpy >= width - 1 or nextx < 0 or nexty < 0 or nextx >= height or nexty >= width:
                        break
                    gx,gy=interpolate_gradient(gradx, grady, nextpx, nextpy, width)

                    """ Stop if we can't go uphill anymore. This is determined by the dot product of  the line direction and the gradient. If it is smaller than 0 we go downhill (reverse for dark lines) """
                    nextpos = nextx * width + nexty               # it is lincoord(row, col,width) of linesUtil.py
                    if s * (mx * gx + my * gy) < 0 and label[nextpos] == 0:
                        break

                    """ Have we hit another line? """
                    if label[nextpos] > 0:
                        m = label[nextpos] - 1
                        """ Search for the junction point on the other line """
                        mindist = DOUBLE_MAX_VALUE_JAVA
                        j= -1
                        for l in range(cont[m].num):
                            dx = nextpx - cont[m].row[l]
                            dy = nextpy - cont[m].col[l]
                            dist = sqrt(dx * dx + dy * dy)
                            if dist<mindist:
                                mindist = dist
                                j = l

                        """ This should not happen... But better safe than sorry... """
                        if mindist>3:
                            break
                        extx[num_add] = cont[m].row[j]
                        exty[num_add] = cont[m].col[j]
                        end_resp = cont[m].response[j]
                        end_angle = cont[m].angle[j]
                        beta = end_angle
                        if beta >= pi:
                            beta -= pi
                        diff1 = abs(beta - alpha)
                        if diff1 >= pi:
                            diff1 = 2.0 * pi - diff1
                        diff2 = abs(beta + pi - alpha)
                        if diff2 >= pi:
                            diff2 = 2.0 * pi - diff2
                        end_angle = beta if diff1 < diff2 else beta + pi
                        num_add += 1
                        add_ext = True
                        break
                    else:
                        extx[num_add] = nextpx
                        exty[num_add] = nextpy
                        num_add+=1

                if add_ext is True:
                    """ Make room for the new points """
                    num_pnt+=num_add

                    if it == -1:
                        """ Move points on the line up num_add places"""
                        trow = [0 for i in range(num_add)] + trow
                        tcol = [0 for i in range(num_add)] + tcol
                        tangle = [0 for i in range(num_add)] + tangle
                        tresp = [0 for i in range(num_add)] + tresp

                        """ Insert points at the beginning of the line. """
                        for index in range(num_add):
                            trow[index] = extx[(num_add - 1 - index)]
                            tcol[index] = exty[(num_add - 1 - index)]
                            tangle[index] = alpha
                            tresp[index] =  response

                        tangle[0] = end_angle
                        tresp[0] =end_resp
                        """ Adapt indices of the previously found junctions """
                        for k in range(len(junc)):
                            if junc[k].cont1 == i:
                                junc[k].pos += num_add
                    else:
                        """ Insert points at the end of the line """
                        for k in range(num_add):
                            trow.append( extx[k])
                            tcol.append(exty[k])
                            tangle.append(alpha)
                            tresp.append(response)
                        tangle[(num_pnt - 1)] = end_angle
                        tresp[(num_pnt - 1)] = end_resp

                    tmp_cont.row = trow
                    tmp_cont.col = tcol
                    tmp_cont.angle = tangle
                    tmp_cont.response = tresp
                    tmp_cont.num = num_pnt


                    """ Add the junction point only if it is not one of the other line's endpoints """
                    if 0< j < cont[m].num - 1:
                        if it == -1:
                            if tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_end_junc"]:
                                tmp_cont.cont_class= linesUtil.COUNTOUR_DICT["cont_both_junc"]
                            else:
                                tmp_cont.cont_class= linesUtil.COUNTOUR_DICT["cont_start_junc"]
                        else:
                            if tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_start_junc"]:
                                tmp_cont.cont_class= linesUtil.COUNTOUR_DICT["cont_both_junc"]
                            else:
                                tmp_cont.cont_class= linesUtil.COUNTOUR_DICT["cont_end_junc"]

                        index_trow= 0
                        index_tcol =0
                        if it != -1:
                            index_trow = num_pnt - 1
                            index_tcol = num_pnt - 1
                        junc.append(Junction(cont1=m, cont2=i, pos=j, x=trow[index_trow], y=tcol[index_tcol]))
                        num_junc+=1

                    """ overwrite the che cont of tmp_cont"""
                    cont[i] = tmp_cont


    """ 
    Done with linking. Now split the lines at the junction points 
    NB:
        I modified a lot of logic.
    """
    junc.sort(key=attrgetter('pos'))
    for i in range(0,num_junc,k if k>0 else 1):
        j =junc[i].cont1
        tmp_cont = cont[ j ]
        num_pnt = tmp_cont.num
        """  Count how often line j needs to be split """
        counter=0
        for index in range(num_junc):
            if i + index < num_junc and junc[(i + index)].cont1 == j :
                counter+=1

        if counter ==1 and len(tmp_cont.row)>num_pnt-1 and len(tmp_cont.col)>num_pnt-1 and tmp_cont.row[0] == tmp_cont.row[(num_pnt - 1)] and tmp_cont.col[0] == tmp_cont.col[(num_pnt - 1)]:
            """ If only one junction point is found and the line is closed it only needs to be rearranged cyclically, but not split """
            begin = junc[i].pos
            trow = tmp_cont.row
            tcol = tmp_cont.col
            tangle = tmp_cont.angle
            tresp = tmp_cont.response
            tmp_cont.row = [0 for ii in range(num_pnt)]
            tmp_cont.col = [0 for ii in range(num_pnt)]
            tmp_cont.angle = [0 for ii in range(num_pnt)]
            tmp_cont.response = [0 for ii in range(num_pnt)]

            for l in range(num_pnt):
                pos = begin+l
                """ Skip starting point so that it is not added twice """
                if pos >= num_pnt:
                    pos = begin + l - num_pnt + 1
                tmp_cont.row[l] = trow[pos]
                tmp_cont.col[l] = tcol[pos]
                tmp_cont.angle[l] = tangle[pos]
                tmp_cont.response[l] = tresp[pos]
            """ Modify contour class """
            tmp_cont.cont_class= linesUtil.COUNTOUR_DICT["cont_both_junc"]
        else:
            """ Otherwise the line has to be split """
            for l in range(counter):
                """
                I CHANGED MASSIVELY THE CODE. Because that the cont_class could be different, compared to the java code.
                See https://github.com/thorstenwagner/ij-ridgedetection/issues/39
                In the Java code we have at least 100 value in the 'junc' variable, that are init with default values.
                These values are "really" filled starting from the last position, hence in some case could be that
                in this assignment https://github.com/thorstenwagner/ij-ridgedetection/blob/master/src/main/java/de/biomedical_imaging/ij/steger/Link.java#L1202 it assignes the default values instead of a real value
                This situation could lead to unexpected behavior.
                """
                begin = 0 if l == 0 else junc[(i + l - 1)].pos
                end = 0
                if l == counter:
                    end = tmp_cont.num - 1
                elif l != counter and i+l>0:    # workaround. The idea is to avoid to consider the same starting junction
                    end = junc[(i + l)].pos


                if end==begin and counter>1:
                    """ Do not add one point segments """
                    continue

                """ select contour class"""
                cls = linesUtil.COUNTOUR_DICT["cont_both_junc"]
                if l == 0:
                    if tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_start_junc"] or tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_both_junc"]:
                        cls= linesUtil.COUNTOUR_DICT["cont_both_junc"]
                    else:
                        cls= linesUtil.COUNTOUR_DICT["cont_end_junc"]
                elif l==counter:
                    if tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_end_junc"] or tmp_cont.cont_class == linesUtil.COUNTOUR_DICT["cont_both_junc"]:
                        cls= linesUtil.COUNTOUR_DICT["cont_both_junc"]
                    else:
                        cls= linesUtil.COUNTOUR_DICT["cont_start_junc"]

                """ 
                Becuase a weird implementation in the java code I cannot figure out always a valid value for 'end'. it leads to duplicate values in the cont. 
                It happens in the java code too (but over differents values.
                To avoid it I implemented this check
                """
                has_to_be_append = True
                for c in cont:
                    if tmp_cont.row ==c.row:
                        has_to_be_append =False
                        tmp_cont.cont_class=cls
                        break

                if has_to_be_append is True:
                    cont.append(Line( num=len(tmp_cont.row), row = tmp_cont.row, col = tmp_cont.col, angle = tmp_cont.angle, response = tmp_cont.response, cont_class=cls))
                    num_cont+=1

            #cont[j] = cont[--num_cont]; i d not need it becuase it sorted a 100elemetns vector where all are defualt value and just the last 2 not. Here I append the new element, hence they are already in the correct position

    """ Finally, check whether all angles point to the right of the line """
    for i in range(num_cont):
        tmp_cont = cont[i]
        num_pnt = tmp_cont.num
        if num_pnt > 1:
            trow = tmp_cont.row
            tcol = tmp_cont.col
            tangle = tmp_cont.angle

            """ One point of the contour is enough to determine the orientation """
            k = int((num_pnt - 1) / 2)

            if len(tangle)>k and len(trow)>k+1 and len(tcol)>k+1:
                """ The next few lines are ok because lines have at least two points """
                dx = trow[(k + 1)] - trow[k]
                dy = tcol[(k + 1)] - tcol[k]
                nx = cos(tangle[k])
                ny = sin(tangle[k])

                """ If the angles point to the left of the line they have to be adapted. The orientation is determined by looking at the z-component of the cross-product of (dx,dy,0) and (nx,ny,0) """
                if nx * dy - ny * dx < 0:
                    for j in range(num_pnt):
                        tangle[j] += pi
                        if tangle[j]  >= 2*pi:
                            tangle[j] -= 2*pi

    for c in cont:
        if c is not None and c.cont_class is not None:
            c.frame=contours[0].father_frame if len(contours)>0 else None
            contours.append(c)

    for jun in junc:
        if jun is not None and not(jun.cont1==0 and jun.cont2==0):
            junctions.append(jun)

    return num_cont

