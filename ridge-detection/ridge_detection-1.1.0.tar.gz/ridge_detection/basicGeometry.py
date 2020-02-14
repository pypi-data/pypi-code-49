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
Here I collected the following file:
-) Line.java            --> Lines.java is treated as a python list of this object directly in the code that use it i.e. lineDetector obj
-) Chord.java
-) Region.java
-) Junction.java        --> Junctions.java is treated as a python list of this object directly in the code that use it i.e. lineDetector obj

"""
from math import sqrt
import logging

""" 
global variable to manage the counter of the lines. It used the synchronized method. 
I hope this workaround will work otherwise --> http://theorangeduck.com/page/synchronized-python 
"""
id_counter = 0

def get_global_counter():
    global id_counter
    return id_counter

def reset_counter():
    global id_counter
    id_counter = 0


def getIndexByID(lines, id):
    """
    Since I do not have the object "lines" but a list of object Line, this function is faking the 'getIndexByID' function of the Liens obj in lines.java
    :param lines: list of Line obj
    :param id: id of the object Line to search
    :return: the index in the list 'lines' of the searched obj
    """
    for i in range(len(lines)):
        if lines[i].getID()==id:
            return i
    return -1



class Line:
    """
    This class holds one extracted line. The field num contains the number of points in the line. The coordinates of the line points are given in the arrays row and col.
    The array angle contains the direction of the normal to each line point, as measured from the row-axis. Some people like to call the col-axis the x-axis and the row-axis the y-axis, and measure the angle from
    the x-axis. To convert the angle into this convention, subtract PI/2 from the angle and normalize it to be in the interval [0,2*PI). The array response contains the response of the operator,
    i.e., the second directional  derivative in the direction of angle, at each line point. The arrays width_l and width_r contain the width information for each line point if the
    algorithm was requested to extract it; otherwise they are NULL. If the line position and width correction was applied the contents of width_l and width_r will be identical.
    The arrays asymmetry and contrast contain the true asymmetry and contrast of each line point if the algorithm was instructed to apply the width and position correction. Otherwise, they are set to NULL. If
    the asymmetry, i.e., the weaker gradient, is on the right side of the line, the asymmetry is set to a positive value, while if it is on the left side it is set to a negative value.
    """
    """ number of points. """
    num = 0

    """ row coordinates of the line points. """
    row = list()

    """ column coordinates of the line points. """
    col = list()

    """ angle of normal (measured from the row axis). """
    angle = list()
    """ response of line point (second derivative). """
    response = list()

    """ width to the left of the line. """
    width_l = list()

    """ width to the right of the line. """
    width_r= list()

    """ asymmetry of the line point. """
    asymmetry = list()

    """ intensity of the line point. """
    intensity = list()

    """ contour class (e.g., cont_no_junc,cont_start_junc,cont_end_junc,cont_both_junc,cont_closed) """
    cont_class = None             #I adapted this variable because it was an enum class. It has to be an integer, It has to be filled using linesUtil.COUNTOUR_DICT["name_of junc_type"]

    """ The id. """
    _id = None

    """ The frame. """
    frame = 0

    """
    Since in java there is a class Lines that is basically a list of lines plus a variable frame and I have to track this value, I stored it in this variable
     if it is in a list the frame of the list
     """
    father_frame = None

    def __init__(self,  num=None, row = None, col = None, angle = None, response = None, asymmetry = None, intensity = None, width_l = None, width_r = None, cont_class=None):
        self.assignID()
        self.num = 0 if num is None else num
        self.row = row
        self.col = col
        self.angle = angle
        self.response = response
        self.asymmetry = asymmetry
        self.intensity = intensity
        self.width_l = width_l
        self.width_r = width_r
        self.cont_class = cont_class


    def getStartOrdEndPosition(self,x,y):
        """
        :param x:
        :param y:
        :return: the start ord end position
        """
        distStart = sqrt(pow(self.col[0] - x, 2) + pow(self.row[0] - y, 2))
        distEnd = sqrt(pow(self.col[(self.num - 1)] - x, 2) + pow(self.row[(self.num - 1)] - y, 2))
        return 0 if distStart < distEnd else self.num - 1

    def estimateLength(self):
        """
        :return: the estimated length of the line
        """
        length = 0
        for i in list(range(0,self.num)):
            length += sqrt(pow(self.col[i] - self.col[i - 1], 2) + pow(self.row[i] - self.row[i - 1], 2))
        return length

    #http://theorangeduck.com/page/synchronized-python o global??
    def assignID(self):
        global id_counter
        self._id = id_counter
        id_counter +=1

    def getXCoordinates(self):
        return  self.col

    def getYCoordinates(self):
        return  self.row

    def getID(self):
        return self._id

    def __str__(self):
        return "id: "+str(self._id)+"\tcont_class: "+str(self.cont_class)+"\tnum: "+str(self.num)+"\tlen_elements: "+str(len(self.angle))

class Chord:
    """  Storage the chord variables"""
    def __init__(self, row=0, column_start=0, column_end =0):
        self.r = row
        self.ce = column_end
        self.cb = column_start

    def __str__(self):
        """print the value used in the script the variables """
        output = "List of input params:\n"
        output += "\trow coordinate of the chord = " + str(self.r) + "\n"
        output += "\tcolumn coordinate of the start of the chord = " + str(self.cb) + "\n"
        output += "\tcolumn coordinate of the end of the chord  = " + str(self.ce) + "\n"
        return output


class Region:
    """  Storage a region"""

    def __init__(self):
        self.num = 0  # number of chords
        """ Since it has to be a list of Chord I used the same workaround used in 'LineDetector.py for junctions and lines"""
        self._rl = list()

    def add_chord(self, chord):
        if isinstance(chord, Chord):
            self._rl.append(chord)
        else:
            print("ERROR: You have to append to the 'rl' list a 'chord' class variable. (basicGeometry.py->Region.add_chord)")
            logging.error(" You have to append to the 'rl' list a 'chord' class variable. (basicGeometry.py->Region.add_chord)")
            exit(-1)

    def add_chords(self, list_chords):
        """
        insert a bunch of lines to the _rl variables
        :param list_chords: list of chords
        :return:
        """
        if isinstance(list_chords, list):
            for l in list_chords:
                self.add_chord(l)
        else:
            self.add_chord(list_chords)

    def get_all_rl(self):
        """ returns all the chords"""
        return self._rl

    def get_line(self, index=-1):
        """
        Returns the line in the 'index' position.
        For default returns the last inserted chord
        :param index: index in the lines list. -1 means the last inserted line
        :return: the specified chord
        """
        return self._rl[index] if len(self._rl) != 0 and len(self._rl) > index else None



class Junction:
    """
    Storage the junction variables. In the original Java code is a subclass of the "Comparable" class Interface of the Java standard library (that has just the 'compareTo' function)
    """

    """
    Since in java there is a class Junctions that is basically a list of lines plus a variable frame and I have to track this value, I stored it in this variable
     if it is in a list the frame of the list
     """


    def __init__(self, cont1=None, cont2=None, pos=None, x =None, y=None, lineCont1=None, lineCont2=None, isNonTerminal=False, father_frame=None ):
        self.cont1 = cont1  #Index of line that is already processed
        self.cont2 = cont2  #Index of line that runs into cont1
        self.pos = pos #Index of the junction point in cont1
        self.x = x
        self.y = y
        self.isNonTerminal = isNonTerminal
        self.father_frame=father_frame
        if (isinstance(lineCont1,Line) and isinstance(lineCont2,Line)) or (lineCont1 is None and lineCont2 is None):
            self.lineCont1 = lineCont1      #line that is already processed
            self.lineCont2 = lineCont2
        else:
            print("ERROR: The 'lineCont1' and 'lineCont2' input value have to be an instance of the class 'Line' or a 'NoneType'. (basicGeometry.py->Junction.__init__)")
            logging.error(" The 'lineCont1' and 'lineCont2' input value have to be an instance of the class 'Line' or a 'NoneType'. (basicGeometry.py->Junction.__init__)")
            exit(-1)


    def __str__(self):
        """print the value used in the script the variables """
        output = "List of input params:\n"
        output += "\tcont1: Index of line that is already processed = " + str(self.cont1) + "\n"
        output += "\tlineCont1: Line that is already processed = " + self.lineCont1.__str__() + "\n"
        output += "\tpos: Index of the junction point in cont1 = " + str(self.pos) + "\n"

        output += "\tx: row coordinate of the junction point = " + str(self.x) + "\n"
        output += "\ty: column coordinate of the junction point = " + str(self.y) + "\n"

        output += "\tcont2: Index of line that runs into cont1 = " + str(self.cont2) + "\n"
        output += "\tlineCont1: Line that runs into idCont1 = " + self.lineCont2.__str__() + "\n"
        output += "\tisNonTerminal = " + str(self.cont2) + "\n"
        return output


