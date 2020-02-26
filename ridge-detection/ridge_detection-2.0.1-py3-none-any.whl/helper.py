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


"""
I inserted the function called from the main:
-) displayContours
-)save_to_disk
Here I collected the following file:
-) Normal.java
-) Threshold.java
-) Offset.java
 """

from math import exp,sin,cos
from ridge_detection.basicGeometry import Region,Chord
from numpy import amax,amin,asarray

import logging
from os import path
from copy import deepcopy
from PIL import Image, ImageDraw
from mrcfile import open as mrcfile_open, new as mrcfile_new

RED_PIXEL_LINE = (255, 0, 0)
GREEN_PIXEL_CONTOUR = (0, 255, 0)
SIZE_RAY_JUNCTION =1

def displayContours(params,result,resultJunction):

    try:
        img=Image.fromarray(mrcfile_open(params.config_path_to_file).data).convert('RGB')
    except ValueError:
        img=Image.open(params.config_path_to_file).convert('RGB')

    pixelMap2 = img.load()
    sizePixelMap2=img.size


    """ plot the lines"""
    if isinstance(result, list) is True:
        for line in result:
            for i,j in zip(line.col,line.row):
                pixelMap2[int(i), int(j)] = RED_PIXEL_LINE

    img_only_lines = deepcopy(img)

    """ plot the contours"""
    if isinstance(result, list) is True:
        for cont in result:
            last_w_l ,last_w_r,px_r,px_l,py_r,py_l = 0,0,0,0,0,0
            for j in range(cont.num):
                px = cont.col[j]
                py = cont.row[j]

                nx = sin(cont.angle[j])
                ny = cos(cont.angle[j])
                if params.get_estimate_width():
                    px_r = px + cont.width_r[j] * nx
                    py_r = py + cont.width_r[j] * ny
                    px_l = px - cont.width_l[j] * nx
                    py_l = py - cont.width_l[j] * ny

                    if last_w_r > 0 and cont.width_r[j] > 0 and sizePixelMap2[0]>int(px_r)+1 and sizePixelMap2[1]>int(py_r)+1:
                        pixelMap2[int(px_r)+1, int(py_r)+1] = GREEN_PIXEL_CONTOUR
                    if last_w_l > 0 and cont.width_l[j] > 0 and sizePixelMap2[0]>int(px_l)+1 and sizePixelMap2[1]>int(py_l)+1:
                        pixelMap2[int(px_l) + 1, int(py_l) + 1] = GREEN_PIXEL_CONTOUR

                    last_w_r = cont.width_r[j]
                    last_w_l = cont.width_l[j]

    """ draw a circle (with ray SIZE_RAY_JUNCTION) centered in each junctions"""
    if params.get_show_junction_points() is True and isinstance(resultJunction, list) is True:
        for junction in resultJunction:
            draw = ImageDraw.Draw(img)
            draw.ellipse((int(junction.x) - SIZE_RAY_JUNCTION, int(junction.y) - SIZE_RAY_JUNCTION, int(junction.x) + SIZE_RAY_JUNCTION, int(junction.y) + SIZE_RAY_JUNCTION), fill = 'blue')
    if params.get_preview() is True:
        img.show()
    return img,img_only_lines


def save_to_disk(img,img_only_lines,folder_save_out):
    outJpg=path.join(folder_save_out,"output.png")
    outJpg_onlyLines = path.join(folder_save_out, "output_only_lines.png")
    outmrc=path.join(folder_save_out,"output.mrc")
    outmrc_onlyLines = path.join(folder_save_out, "output_only_lines.mrc")
    img.save(outJpg)
    logging.info(" desired output image saved in '"+str(outJpg)+"'")
    img_only_lines.save(outJpg_onlyLines)
    logging.info(" only lines output image saved in '"+str(outJpg_onlyLines)+"'")
    with mrcfile_new(outmrc,overwrite=True) as mrc:
        mrc.set_data(asarray(Image.open(outJpg).convert("L")))
        mrc.close()
    logging.info(" desired output MRC saved in '" + str(outmrc) + "'")
    with mrcfile_new(outmrc_onlyLines,overwrite=True) as mrc:
        mrc.set_data(asarray( Image.open(outJpg_onlyLines).convert("L")))
        mrc.close()
    logging.info(" only lines output MRC saved in '" + str(outmrc_onlyLines) + "'")


INTEGER_8BIT_MAX = 255
INTEGER_8BIT_MIN = 0

DEBUGGING = False
""" OFFSET.JAVA"""
class Offset:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y


""" NORMAL.JAVA"""
SQRTPI = 1.772453850905516027
UPPERLIMIT = 20.0
P10 = 242.66795523053175
P11 = 21.979261618294152
P12 = 6.9963834886191355
P13 = -.035609843701815385
Q10 = 215.05887586986120
Q11 = 91.164905404514901
Q12 = 15.082797630407787
Q13 = 1.0
P20 = 300.4592610201616005
P21 = 451.9189537118729422
P22 = 339.3208167343436870
P23 = 152.9892850469404039
P24 = 43.16222722205673530
P25 = 7.211758250883093659
P26 = .5641955174789739711
P27 = -.0000001368648573827167067
Q20 = 300.4592609569832933
Q21 = 790.9509253278980272
Q22 = 931.3540948506096211
Q23 = 638.9802644656311665
Q24 = 277.5854447439876434
Q25 = 77.00015293522947295
Q26 = 12.78272731962942351
Q27 = 1.0
P30 = -.00299610707703542174
P31 = -.0494730910623250734
P32 = -.226956593539686930
P33 = -.278661308609647788
P34 = -.0223192459734184686
Q30 = .0106209230528467918
Q31 = .191308926107829841
Q32 = 1.05167510706793207
Q33 = 1.98733201817135256
Q34 = 1.0
SQRT2 = 1.41421356237309504880

def normalizeImg(img,new_min=INTEGER_8BIT_MIN,new_max=INTEGER_8BIT_MAX,return_Aslist=True):
    """
    Normalize the image. For default it is converted to an 8bit img
    :param img:
    :param new_max:
    :param new_min:
    :param return_Aslist:
    :return:
    """
    m = amin(img)
    res= (new_max - new_min) * ((img - m) / (amax(img) - m)) + new_min
    return res if return_Aslist is False else res.flatten().tolist()

def getNormal(x):
    """
    calculates the normal of x
    :param x:
    :return:
    """
    if x < -UPPERLIMIT:
        return 0.0
    if x > UPPERLIMIT:
        return 1.0

    y = x / SQRT2
    sn = 1

    if y < 0:
        y = -y
        sn = -1

    if y < 0.46875:
        R1 = P10 + P11 * y*y + P12 * y*y*y*y + P13 * pow(y,6)
        R2 = Q10 + Q11 * y*y + Q12 * y*y*y*y + Q13 * pow(y,6)
        erf = y * R1 / R2
        return 0.5 + 0.5 * erf if sn ==1 else 0.5 - 0.5 * erf
    elif y < 4.0:
        R1 = P20 + P21 * y + P22 * y*y + P23 * y*y*y + P24 * y*y*y*y + P25 * pow(y,5) + P26 * pow(y,6) + P27 * pow(y,7)
        R2 = Q20 + Q21 * y + Q22 * y*y + Q23 * y*y*y + Q24 * y*y*y*y + Q25 * pow(y,5) + Q26 * pow(y,6) + Q27 * pow(y,7)
        erfc = exp(-(y*y)) * R1 / R2
        return 1.0 - 0.5 * erfc if sn == 1 else 0.5 * erfc
    else:
        R1 = P30 + P31 *  y*y*y*y + P32 * pow(y,8) + P33 * pow(y,12) + P34 * pow(y,16)
        R2 = Q30 + Q31 * y*y*y*y + Q32 * pow(y,8) + Q33 * pow(y,12) + Q34 * pow(y,16)
        erfc = (exp(-(y*y)) / y) * (1.0 / SQRTPI + R1 / (R2 * y*y))
        return 1.0 - 0.5 * erfc if sn==1 else 0.5 * erfc


""" THRESHOLD JAVA"""
def threshold(image, minimum, width, height, out_region):
    if not isinstance(out_region, Region):
        print("ERROR: The 'out_region' param has to be an instance of the class 'Region'. (helper.py->threshold)")
        logging.error(" The 'out_region' param has to be an instance of the class 'Region'. (helper.py->threshold)")
        exit(-1)
    inside = False
    num = 0
    rl =list()
    for r in list(range(0, height)):
        for c in list(range(0, width)):
            l =  r * width + c               # it is lincoord(row, col,width) of linesUtil.py
            grey = image[l]
            if grey>=minimum:
                if inside is False:
                    inside = True
                    rl.append(Chord(row=r,column_start= c))
            elif inside is True:
                inside = False
                rl[num].ce = c - 1
                num+=1                                                           #todo: e' uguale a (*) --> quindi refactor possibile

        if inside is True:
            inside = False
            rl[num].ce=width-1
            num+=1                                                               #todo: e' uguale a (*) --> quindi refactor possibile

    out_region.add_chords(rl[:num])
    out_region.num =num

