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
from ridge_detection.params import Params
from ridge_detection.helper import normalizeImg, INTEGER_8BIT_MAX, INTEGER_8BIT_MIN
from ridge_detection.basicGeometry import Junction,Line,getIndexByID
from ridge_detection import linesUtil
from copy import deepcopy
from ridge_detection.slopeOverlapResolver import resolve
from ridge_detection.position import detect_lines
import numpy as np
from operator import attrgetter
from math import floor,ceil


def skeletonize_lines(contour):
    """
    The founded lines could have extra pixel due to some approximation. This situation leads to recognize
    these pixels as junction in the stripper project

    example of lines with extra pixel:
                                        ***    ********
                                           ****     *********
    example of skeletonize line
                                        ***    ********
                                           ****        ******
    :param contour: list of lines
    :return:
    """
    for l in contour:
        list_remove = list()
        prev_col = l.col[0]
        prev_row = l.row[0]
        for index in range(1, l.num - 1, 2):
            next_col = l.col[index + 1]
            next_row = l.row[index + 1]
            if (l.col[index] == prev_col and l.row[index] == next_row) or (
                    l.col[index] == next_col and l.row[index] == prev_row):
                list_remove.append(index)
            prev_row = next_row
            prev_col = next_col
        for p in list_remove[::-1]:
            l.col.pop(p)
            l.row.pop(p)
        l.num = len(l.col)


def smart_cast_row_and_col(contour):
    """
    Cast to integer the values of col and row  in function of their decimal values. if >0.5 it ceil to 1 otherwise to 0.
    I need to do that because the int cast is always a floor operation. As consequence [0.0001,1] and [0.999,1] are
    cat to [0,0] both, that situation leads to have lock in a line
    :param contour: list of line
    :return:
    """
    for l in contour:
        for i in range(len(l.row)):
            if l.row[i] < 0.5:
                l.row[i] = 0
            elif 1 > l.row[i] > 0.5:
                l.row[i] = 1
            else:
                l.row[i] = floor(l.row[i]) if l.row[i] % int(l.row[i]) < 0.5 else ceil(l.row[i])
            if l.col[i] < 0.5:
                l.col[i] = 0
            elif 1 > l.col[i] > 0.5:
                l.col[i] = 1
            else:
                l.col[i] = floor(l.col[i]) if l.col[i] % int(l.col[i]) < 0.5 else ceil(l.col[i])


class LineDetector:
    alreadyProcessedJunctionPoints = set()
    junctions = list()
    _lines = list()

    def __init__(self, params=None):
        """
        Set the params used in the code. It accepted the path to the config file or the class Params
        :param params:
        """
        if isinstance(params, Params):
            self.params = params
        elif isinstance(params, str) or isinstance(params, dict):
            self.params = Params(params)
        else:
            print("ERROR: The input has to be an instance of the class 'Params' or a path to the config file. (lineDetector.py->LineDetector.__init__)")
            logging.error(" The input has to be an instance of the class 'Params' or a path to the config file. (lineDetector.py->LineDetector.__init__)")
            exit(-1)

        """
         in the code are 2 array class of the class junction and line
         since in python  the array class not exist, we fake it in the following way:
         -) declare them as private list in this way the 'frame' java variable will be the index value of the list ... 
         -) create "add new element" function where I check if it is the appropriate class istance
         -) create "select element" function to select an element 
         """

    def __str__(self):
        return self.params.__str__()

    def detectLines(self,img):
        """
        Look for the contours line in the image. It returns all the found line and insert all of them in the "self._lines" variable
        :param img: has to be a numpy array
        :return:
        """
        self.junctions = []  #todo come gestire frame???  new Junctions(ip.getSliceNumber());
        self._lines = self.get_lines(img)
        return self._lines


    def addAdditionalJunctionPointsAndLines(self,lines):
        if not (isinstance(lines, list) and isinstance(lines[0], Line)):
            print("ERROR: In 'lineDetector.addAdditionalJunctionPointsAndLines', the 'lines' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.addAdditionalJunctionPointsAndLines)")
            logging.error(" In 'lineDetector.addAdditionalJunctionPointsAndLines', the 'lines' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.addAdditionalJunctionPointsAndLines)")
            exit(-1)

        father_frame = self.junctions[0].father_frame if len(self.junctions)>0 else None
        for i in range(len(self.junctions)):
            splitPoint = deepcopy(self.junctions[i])
            if i not in self.alreadyProcessedJunctionPoints:
                """ Find Junctions with the same position as the split point """
                junctionsWithTheSamePosition = [splitPoint]
                self.alreadyProcessedJunctionPoints.add(i)
                for j in range(i+1, len(self.junctions)):
                    if j not in self.alreadyProcessedJunctionPoints:
                        junc2 = self.junctions[j]
                        if abs(junc2.x - splitPoint.x) < 0.01 and abs(junc2.y - splitPoint.y) < 0.01:
                            self.alreadyProcessedJunctionPoints.add(j)
                            junctionsWithTheSamePosition.append(junc2)

                """ Connect all lines which are connected with the processed line also with each other (new junctions point) """
                connectedWithProcessedLine = [j.lineCont2 for j in junctionsWithTheSamePosition ]
                connectedWithProcessedIndex =[j.cont2 for j in junctionsWithTheSamePosition ]

                for j in range(len(connectedWithProcessedLine)):
                    for k in range(j+1, len(connectedWithProcessedLine)):
                        self.junctions.append( Junction(cont1=connectedWithProcessedIndex[j], cont2=connectedWithProcessedIndex[k], pos=connectedWithProcessedLine[j].getStartOrdEndPosition(splitPoint.x, splitPoint.y),
                                                        x =splitPoint.x, y=splitPoint.y, lineCont1=connectedWithProcessedLine[j], lineCont2=connectedWithProcessedLine[k], father_frame=father_frame ))
                        self.alreadyProcessedJunctionPoints.add(len(self.junctions) - 1)

                """ Split the line in two line at the split point if it is not at the end or beginning of the line """
                l1 = splitPoint.lineCont1
                pos = splitPoint.pos
                isClosedContour = l1.col[0] == l1.col[l1.num - 1] and l1.row[0] == l1.row[l1.num - 1]
                if isClosedContour is True:
                    l1.cont_class= linesUtil.COUNTOUR_DICT["cont_closed"]
                    l1.cont_class=self.reconstructContourClass(l1, l1.num, l1.getStartOrdEndPosition(splitPoint.x, splitPoint.y))

                if pos!=0 and pos != (l1.num - 1) and not isClosedContour:
                    """ All data up to pos (included) """
                    keepLength = pos + 1
                    keepAsymmetry = [0 for i in range(keepLength)]
                    keepIntensity = [0 for i in range(keepLength)]
                    keepAngle = [0 for i in range(keepLength)]
                    keepWidth_l = [0 for i in range(keepLength)]
                    keepWidth_r = [0 for i in range(keepLength)]

                    """ All data from pos (included) """
                    splitSize = l1.num - pos
                    splitAsymmetry = [0 for i in range(splitSize)]
                    splitIntensity = [0 for i in range(splitSize)]
                    splitAngle = [0 for i in range(splitSize)]
                    splitWidth_l = [0 for i in range(splitSize)]
                    splitWidth_r = [0 for i in range(splitSize)]

                    """ Copy data """

                    if self.params.get_estimate_width():
                        if self.params.get_correct_position():
                            keepAsymmetry = deepcopy(l1.asymmetry[0:keepLength])
                            splitAsymmetry = deepcopy(l1.asymmetry[pos:pos+splitSize])
                            keepIntensity = deepcopy(l1.intensity[0:keepLength])
                            splitIntensity = deepcopy(l1.intensity[pos:pos+splitSize])
                        keepAngle = deepcopy(l1.angle[0:keepLength])
                        splitAngle = deepcopy(l1.angle[pos:pos+splitSize])
                        keepWidth_l = deepcopy(l1.width_l[0:keepLength])
                        splitWidth_l = deepcopy(l1.width_l[pos:pos+splitSize])
                        keepWidth_r = deepcopy(l1.width_r[0:keepLength])
                        splitWidth_r = deepcopy(l1.width_r[pos:pos+splitSize])

                    keepCol = deepcopy(l1.col[0:keepLength])
                    splitCol = deepcopy(l1.col[pos:pos+splitSize])
                    keepRow = deepcopy(l1.row[0:keepLength])
                    splitRow = deepcopy(l1.row[pos:pos+splitSize])
                    keepResponse = deepcopy(l1.response[0:keepLength])
                    splitResponse = deepcopy(l1.response[pos:pos+splitSize])

                    """ generate new line"""
                    lNew = Line()
                    lNew.angle = splitAngle
                    lNew.asymmetry = splitAsymmetry
                    lNew.col = splitCol
                    lNew.row = splitRow
                    lNew.response = splitResponse
                    lNew.intensity = splitIntensity
                    lNew.width_l = splitWidth_l
                    lNew.width_r = splitWidth_r
                    lNew.num = splitSize
                    lNew.cont_class=l1.cont_class
                    lNew.frame=l1.frame
                    lines.append(lNew)
                    newID=lNew.getID()

                    """ Update junctions """

                    """ Add additional junction points for the split point """
                    lineIds = set() # All IDs which are connected at this junction point
                    for j in junctionsWithTheSamePosition:
                        lineIds.add(j.lineCont1.getID())
                        lineIds.add(j.lineCont2.getID())


                    for id in lineIds:
                        connectWithLineID = getIndexByID(lines,id)
                        connectWith = lines[connectWithLineID]

                        self.junctions.append( Junction(cont1=len(lines)-1, cont2= connectWithLineID, pos=lNew.getStartOrdEndPosition(splitPoint.x, splitPoint.y), x=splitPoint.x, y=splitPoint.y, lineCont1=lNew,
                                                lineCont2=connectWith, father_frame=father_frame))
                        self.alreadyProcessedJunctionPoints.add(len(self.junctions) - 1)

                    """ Update following junctions point """
                    for j in range(len(self.junctions)):

                        if self.junctions[j].cont1 == splitPoint.cont1 and self.junctions[j].pos > splitPoint.pos:
                            self.junctions[j].cont1 = getIndexByID(lines, newID)
                            self.junctions[j].lineCont1 = lNew
                            self.junctions[j].pos = self.junctions[j].pos - splitPoint.pos

                        m= self.minDistance(self.junctions[j].lineCont2, self.junctions[j].x, self.junctions[j].y)
                        if self.junctions[j].cont2 == splitPoint.cont1 and int(m[1]) > splitPoint.pos:
                            self.junctions[j].cont2 = getIndexByID(lines, newID)
                            self.junctions[j].lineCont2=lNew

                    """ udate line1 ... overwrite line data"""
                    l1.angle = keepAngle
                    l1.asymmetry = keepAsymmetry
                    l1.col = keepCol
                    l1.row = keepRow
                    l1.response = keepResponse
                    l1.intensity = keepIntensity
                    l1.width_l = keepWidth_l
                    l1.width_r = keepWidth_r
                    l1.num = keepLength

                    """ Update position of splitpoint """
                    splitPoint.pos = l1.getStartOrdEndPosition(splitPoint.x, splitPoint.y)
                    lines[splitPoint.cont1] = l1




    def fixJunctions(self,lines):
        if not (isinstance(lines, list) and isinstance(lines[0], Line)):
            print("ERROR: In 'lineDetector.fixJunctions', the 'lines' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.fixJunctions)")
            logging.error(" In 'lineDetector.fixJunctions', the 'lines' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.fixJunctions)")
            exit(-1)

        """ For some reason, the x and y coordinates are permuted """
        for j in self.junctions:
            swap = j.x
            j.x=j.y
            j.y=swap

        # IN ALL MY TESTS, HENCE STARTING FROM THE VERY BEGINNING, I NEVER USED IT. ANYWAY IT SEEMS TO BE USEFULL ONLY IN THE JAVA VERSION
        """
        father_frame = self.junctions[0].father_frame if len(self.junctions)>0 else None
        newJunctions = list()          # list of junction having the same fatherframe of the self.junctions[*]
        processedJunctions = list()    # it is a list of  java.Point2D.Float --> hence a list of list of 2 float elements called x,y -->  processedJunctions[i].x processedJunctions[i].y

        for i in range(len(self.junctions)):
            junc = self.junctions[i]
            mainLine = None     # obj Line, i do not init it because the IDAssign method
            mainLineIndex = -1
            mainLinePos = -1
            secondaryLines = list()     # list of Line
            secondaryLineIndex = list() # list of integer
            secondaryLinePos = list()  # list of integer

            #process each junction-position only once
            if [junc.x,junc.y] not in processedJunctions:
                processedJunctions.append([junc.x,junc.y] )

                # find the secondary line and the main line
                for j in range(len(lines)):
                    l=lines[j]
                    mindist = self.minDistance(l, junc.x, junc.y)

                    if mindist[0]<0.1:
                        # The point is on the line 
                        if mindist[1] == 0 or mindist[1] == l.num-1:
                            # the start/end junction-point is on the line, it is a secondary line
                            secondaryLines.append(l)
                            secondaryLineIndex.append(j)
                            secondaryLinePos.append(mindist[1])
                        else:
                            # if inside the line, it is the main line
                            if mainLine is not None:
                                if mainLine.getID() == l.getID():
                                    continue
                            mainLine = l
                            mainLineIndex = j
                            mainLinePos = int (mindist[1])


                if mainLine is not None:
                    for j in range(len(secondaryLines)):
                        newJunctions.append( Junction(cont1=mainLineIndex, cont2=secondaryLineIndex[j], pos=mainLinePos, x =junc.x, y=junc.y, lineCont1=None, lineCont2=None, father_frame=father_frame ))
                else:
                    # in some cases there is no main line ... maybe there is a bug in the alghoritm, we are not going to fix it
                    uniqueIDs= set()            # of integer
                    uniqueLines = list()        # of line
                    uniqueLineIndex = list()    # of integer
                    uniqueLinePos = list()      # of integer

                    for  j in range(len(secondaryLines)):
                        if not secondaryLines[j].getID() in uniqueIDs:
                            uniqueIDs.add(secondaryLines[j].getID())
                            uniqueLines.append(secondaryLines[j])
                            uniqueLineIndex.append(secondaryLineIndex[j])
                            uniqueLinePos.append(secondaryLinePos[j])

                    for  j in range(len(uniqueLines)):
                        for k in range(j+1,len(uniqueLines)):
                            newJunctions.append(Junction(cont1=uniqueLineIndex[j], cont2=uniqueLineIndex[k], pos=uniqueLinePos[j], x=junc.x,y=junc.y, lineCont1=None, lineCont2=None, father_frame=father_frame))
                            self.alreadyProcessedJunctionPoints.add(len(newJunctions) - 1)

        return newJunctions
        """


    @staticmethod
    def reconstructContourClass(currentClass, num, pos):
        hasJunctionAtStartpoint = pos == 0
        hasJunctionAtEndpoint = pos == num - 1

        if currentClass == linesUtil.COUNTOUR_DICT["cont_no_junc"] and hasJunctionAtStartpoint:
            return linesUtil.COUNTOUR_DICT["cont_start_junc"]
        if currentClass == linesUtil.COUNTOUR_DICT["cont_no_junc"] and hasJunctionAtEndpoint:
            return linesUtil.COUNTOUR_DICT["cont_end_junc"]
        if (currentClass == linesUtil.COUNTOUR_DICT["cont_start_junc"] and hasJunctionAtEndpoint) or (currentClass == linesUtil.COUNTOUR_DICT["cont_end_junc"] and hasJunctionAtStartpoint) or (currentClass ==
                                                                                                                                                                                                linesUtil.COUNTOUR_DICT["cont_closed"] and (hasJunctionAtEndpoint or hasJunctionAtStartpoint)):
            return linesUtil.COUNTOUR_DICT["cont_both_junc"]
        return currentClass



    def fixContours(self,contours):
        if not (isinstance(contours, list) and isinstance(contours[0], Line)):
            print("ERROR: In 'lineDetector.fixContours', the 'contours' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.fixContours)")
            logging.error(" In 'lineDetector.fixContours', the 'contours' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.fixContours)")
            exit(-1)

        index_to_remove =[]
        """ Contours with only a single position cant be valid. """
        for index in range(len(contours)):
            contour = contours[index]
            if contour.num ==1:
                self.deleteJunctions(contours,contour)
                index_to_remove.append(index)
            """ If the results are corrupted, this informationen has to be reconstructed in fixJunctions """
            contours[index].cont_class= linesUtil.COUNTOUR_DICT["cont_no_junc"]

        for i in index_to_remove[::-1]:
            del contours[i]

        """
        This situation happen only in the JAVA code, We manage this situation directly where the problem occurs around line 834 in link.py (i.e.: starting from 'has_to_be_append = True' operation)
        # For some reason the first and the last element are the same. Delete it! 
        if len(contours)>=2:
            if contours[0].getID() == contours[len(contours)-1].getID():
                del contours[len(contours)-1]
        """

    def pruneContours(self,contours, junctions):
        if not (isinstance(junctions, list) and isinstance(junctions[0], Junction)):
            print("ERROR: In 'lineDetector.pruneContours', the 'junctions' input value has to be a list of instances of the class 'Junction'. (lineDetector.py->LineDetector.pruneContours)")
            logging.error(" In 'lineDetector.pruneContours', the 'junctions' input value has to be a list of instances of the class 'Junction'. (lineDetector.py->LineDetector.pruneContours)")
            exit(-1)
        if not (isinstance(contours, list) and isinstance(contours[0], Line)):
            print("ERROR: In 'lineDetector.pruneContours', the 'contours' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.pruneContours)")
            logging.error(" In 'lineDetector.pruneContours', the 'contours' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.pruneContours)")
            exit(-1)

        index_to_remove =[]
        index=0
        for c in contours:
            if c.estimateLength()< self.params.get_minimum_Line_Length()  or c.estimateLength()> self.params.get_maximum_Line_Length()>0:
                self.deleteJunctions(contours,  c)
                index_to_remove.append(index)
            index+=1

        for i in index_to_remove[::-1]:
            del contours[i]



    @staticmethod
    def minDistance( l, x, y):
        """
        Calculate min distance
        :param l:
        :param x:
        :param y:
        :return: 2D-list [0] minimal distance [1] position of minimal distance
        """

        if not isinstance(l, Line):
            print("ERROR: In 'lineDetector.minDistance', the 'l' input value has to be an instance of the class 'Line'. (lineDetector.py->LineDetector.minDistance)")
            logging.error(" In 'lineDetector.minDistance', the 'l' input value has to be an instance of the class 'Line'. (lineDetector.py->LineDetector.minDistance)")
            exit(-1)

        col = np.asarray(l.col)
        row = np.asarray(l.row)
        dist = np.zeros(l.num)
        np.sqrt(np.multiply(col - x, col - x) + np.multiply(row - y, row - y), out=dist)
        m = np.amin(dist)
        return [m, np.where(dist == m)[0][0]]



    def deleteJunctions(self,contours,  c):
        if not (isinstance(contours, list) and isinstance(contours[0], Line)):
            print("ERROR: In 'lineDetector.deleteJunctions', the 'contours' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.deleteJunctions)")
            logging.error(" In 'lineDetector.deleteJunctions', the 'contours' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.deleteJunctions)")
            exit(-1)
        if not isinstance(c, Line):
            print("ERROR: In 'lineDetector.deleteJunctions', the 'c' input value has to be an instance of the class 'Line'. (lineDetector.py->LineDetector.deleteJunctions)")
            logging.error(" In 'lineDetector.deleteJunctions', the 'c' input value has to be an instance of the class 'Line'. (lineDetector.py->LineDetector.deleteJunctions)")
            exit(-1)

        index_to_remove =[]
        index=0

        for junction in self.junctions:
            """ This if() should be removed once cont1 and 2 contain the same info whatever OverlapOption """
            if  self.params.get_overlap_resolution() == "slope":
                if junction.cont1 ==c.getID() or junction.cont2 ==c.getID():
                    index_to_remove.append(index)
                elif contours[junction.cont1].getID() ==c.getID() or contours[junction.cont2].getID() ==c.getID():
                    index_to_remove.append(index)
                index+=1

        for i in index_to_remove[::-1]:
            del self.junctions[i]



    def assignLinesToJunctions(self,lines):
        if not (isinstance(lines, list) and isinstance(lines[0], Line)):
            print("ERROR: In 'lineDetector.assignLinesToJunctions', the 'lines' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.assignLinesToJunctions)")
            logging.error(" In 'lineDetector.assignLinesToJunctions', the 'lines' input value has to be a list of instances of the class 'Line'. (lineDetector.py->LineDetector.assignLinesToJunctions)")
            exit(-1)

        for j in self.junctions:
            j.lineCont1 = lines[j.cont1]
            j.lineCont2 = lines[j.cont2]

        pass

    def get_lines(self,in_img):
        """
        Look for the contours line in the image. It returns all the found line
        :param in_img: image
        :return:
        """
        try:
            cols, rows = in_img.shape
        except AttributeError:
            cols, rows = in_img.size

        self.check_sigma(cols, rows)

        imgpxls2 = np.reshape(in_img, cols*rows)

        #normalize the image to 0:255 that is the same as convert from 32bit to 8bit in imageJ
        if max(imgpxls2)>255 or min(imgpxls2)<0:
            imgpxls2 = normalizeImg(imgpxls2,new_min=INTEGER_8BIT_MIN,new_max=INTEGER_8BIT_MAX,return_Aslist=False)

        contours = list()           # = new Lines(in_img.getSliceNumber());
        detect_lines(image=imgpxls2, width=cols, height=rows, contours=contours, sigma=self.params.get_sigma(), low=self.params.get_lower_Threshold(),
                                high=self.params.get_upper_Threshold(), mode=self.params.get_darkline(), compute_width=self.params.get_estimate_width(),
                                correct_pos=self.params.get_correct_position(), extend_lines=self.params.get_doExtendLine(), junctions=self.junctions)


        self.fixContours(contours)

        self.alreadyProcessedJunctionPoints =set()

        """ 
        Reconstruct solution from junction points. This have to be done, because in raw cases the algorithm corrupts the results. However, I was not able to find that bug
		so I decided to reconstruct the solution from the information which were not be corrupted
		"""
        self.fixJunctions(contours)

        self.assignLinesToJunctions(contours)

        self.addAdditionalJunctionPointsAndLines(contours)

        resultJunction=deepcopy(self.junctions)
        resultJunction.sort(key=attrgetter('pos'))

        """ 
            RECONSTRUCTION OF CONTOUR CLASS
        """

        """ Reset contour class """
        for i in range(len(contours)):
            contours[i].cont_class= linesUtil.COUNTOUR_DICT["cont_no_junc"]

        """ Find closed lines """
        for i in range(len(contours)):
            isClosedContour = contours[i].col[0] == contours[i].col[contours[i].num - 1] and contours[i].row[0] == contours[i].row[contours[i].num - 1]
            if isClosedContour is True:
                contours[i].cont_class= linesUtil.COUNTOUR_DICT["cont_closed"]

        """ Reconstruction contour class """
        for j in resultJunction:
            j.lineCont1.cont_class=self.reconstructContourClass(j.lineCont1.cont_class, j.lineCont1.num, j.pos)
            x = j.lineCont1.getXCoordinates()[j.pos]
            y = j.lineCont1.getYCoordinates()[j.pos]
            j.lineCont2.cont_class=self.reconstructContourClass(j.lineCont2.cont_class, j.lineCont2.num, j.lineCont2.getStartOrdEndPosition(x, y))

        if self.params.get_overlap_resolution() == "slope":
            contours = resolve(contours, resultJunction)

        if self.params.get_minimum_Line_Length() !=0 or self.params.get_maximum_Line_Length() !=0:
            self.pruneContours(contours,resultJunction)
        smart_cast_row_and_col(contours)
        skeletonize_lines(contours)
        return contours


    def check_sigma(self,width, height):
        """
        check if the sigma value is valid
        :param width: width of the image
        :param height: heightof the image
        """
        if self.params.get_sigma() < 0.4:
            print (linesUtil.ERR_SOR + "< 0.4. (lineDetector.py->LineDetector.check_sigma)")
            logging.error(linesUtil.ERR_SOR + "< 0.4. (lineDetector.py->LineDetector.check_sigma)")
            exit(-1)

        min_dim =width if width<height else height

        if linesUtil.mask_size(linesUtil.MAX_SIZE_MASK_2, self.params.get_sigma()) >= min_dim:
            print(linesUtil.ERR_SOR + "too large for image size. (lineDetector.py->LineDetector.check_sigma)")
            logging.error(linesUtil.ERR_SOR + "too large for image size. (lineDetector.py->LineDetector.check_sigma)")
            exit(-1)


    def get_junction(self,index=-1):
        """
        Returns the junction in the 'index' position.
        For default returns the last inserted junction
        :param index: index in the junctions list. -1 means the last inserted junction
        :return: the specified junction
        """
        return self.junctions[index] if len(self.junctions) != 0 and len(self.junctions) < index else None

    def get_line(self,index=-1):
        """
        Returns the line in the 'index' position.
        For default returns the last inserted line
        :param index: index in the lines list. -1 means the last inserted line
        :return: the specified line
        """
        return self._lines[index] if len(self._lines) !=0 and len(self._lines) < index else None
