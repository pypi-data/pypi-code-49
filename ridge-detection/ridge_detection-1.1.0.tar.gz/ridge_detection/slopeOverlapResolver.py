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
from ridge_detection.basicGeometry import Line,Junction
from math import sqrt
from copy import deepcopy
from ridge_detection.linesUtil import COUNTOUR_DICT

"""
NB:
    ArrayList --> list of python list
    HashMap --> python dictionary 
    HashSet --> python set
    
    In java set represents a generic "set of values" (i.e. a java interface) and hash set is a set where the elements are not sorted or ordered
        for more info see https://stackoverflow.com/questions/5139724/whats-the-difference-between-hashset-and-set
    HashMap is similar to HashSet --> https://beginnersbook.com/2014/08/hashset-vs-hashmap-java/
        for more info --> https://www.java67.com/2013/01/difference-between-set-list-and-map-in-java.html
"""
FLOAT_MAX_VALUE_JAVA = 3.4028235E38
"""Sigma for deciding if two floats are 'close enough'"""
SIGMA = 2.0
""" Length from junction point to use in line segment calculation. Smaller distances are more subject to variance, while larger distances """
SLOPE_DIST = 5
"""
 When considering the portion of a line segment to use in straightness comparisons, we take the longest segment possible within the following
 tolerance. A value of  1 would require perfect straightness. 
 """
STRAIGHT_TOLERANCE = 1.02

def resolve(originalLines, junctions):
    """

    :param originalLines: List of Line
    :param junctions:   list of Junction
    :return:
    """
    if not (isinstance(originalLines,list) and isinstance(originalLines[0],Line)):
        print("ERROR: In 'SlopeOvelapResolver.resolve', the 'originalLines' input value has to be a list of instances of the class 'Line'. (slopeOverlapResolver.py->resolve)")
        logging.error(" In 'SlopeOvelapResolver.resolve', the 'originalLines' input value has to be a list of instances of the class 'Line'. (slopeOverlapResolver.py->resolve)")
        exit(-1)
    if not (isinstance(junctions,list) and (len(junctions)>0 and isinstance(junctions[0],Junction)) or len(junctions)==0) :
        print("ERROR: In 'SlopeOvelapResolver.resolve', the 'junctions' input value has to be a list of instances of the class 'Junction'. (slopeOverlapResolver.py->resolve)")
        logging.error(" In 'SlopeOvelapResolver.resolve', the 'junctions' input value has to be a list of instances of the class 'Junction'. (slopeOverlapResolver.py->resolve)")
        exit(-1)


    enclosedLines = set()   # set() of Line objs
    nWayIntersections = []  # it will be treated as list of list of Line obj
    findOverlap(enclosedLines, nWayIntersections, junctions)

    startIntersections = dict() # the key will be a Line obj, the value a list of Line value
    endIntersections = dict()  # the key will be a Line obj, the value a list of Line value
    buildIntersectionMaps(originalLines, enclosedLines, startIntersections, endIntersections)

    lineMerges = []  # it will be treated as list of list of Line obj

    """ find enclosed merges """
    buildMergeList_A(lineMerges, enclosedLines, startIntersections, endIntersections)

    """ find n-way intersections """
    buildMergeList_B(lineMerges, nWayIntersections)

    """ perform the actual merges. This will also populate the lineMap with mappings from original to merged lines """
    lineMap = dict()  # key,value will be a Line obj
    resolvedLines = buildResolvedList(originalLines, lineMerges, lineMap) # it will be a list of Line

    """ use lineMap to update references in original junction points the updatedJunctions list will be populated so we can further process any updated junctions"""
    updatedJunctions = updateJunctions(junctions, lineMap) # it will be a set of Junction

    """ Remove any Junctions that are no longer valid """
    pruneJunctions(junctions, updatedJunctions)

    """ update the intersection points of each surviving Junction in UpdatedJunctions """
    updateContourClasses(updatedJunctions)
    return resolvedLines




def findOverlap(enclosed, nway, junctions):
    """
    Step 1: find enclosed lines (lines with a junction at both start and end point)
    :param enclosed: lines with a junction at both start and end. it is a set() of Line objs
    :param nway: it is s list of list of Line obj
    :param junctions:
    :return:
    """

    if not (isinstance(junctions,list) and (len(junctions)>0 and isinstance(junctions[0],Junction)) or len(junctions)==0) :
        print("ERROR: In 'SlopeOvelapResolver.findOverlap', the 'junctions' input value has to be a list of instances of the class 'Junction'.  (slopeOverlapResolver.py->findOverlap)")
        logging.error(" In 'SlopeOvelapResolver.findOverlap', the 'junctions' input value has to be a list of instances of the class 'Junction'.  (slopeOverlapResolver.py->findOverlap)")
        exit(-1)

    """ Remember if a Junction is located at the start or end point of a Line """
    startMatches = dict() # the key will be a Line obj, the value a list of Line value
    endMatches = dict()  # the key will be a Line obj, the value a list of Line value
    tSections = set()

    """ These enclosed lines will be treated as areas of overlap """
    for j in junctions:
        """ check if this junction sits on the start or end of either of its lines """
        if matchesStart(j, j.lineCont1):
            startMatches.update({j.lineCont1: j})
        if matchesStart(j, j.lineCont2):
            startMatches.update({j.lineCont2: j})
        if matchesEnd(j, j.lineCont1):
            endMatches.update({j.lineCont1: j})
        if matchesEnd(j, j.lineCont2):
            endMatches.update({j.lineCont2: j})


    for k in startMatches.keys():       # OK enclosed.addAll(startMatches.keySet())
        enclosed.add(k)
    for k in endMatches.keys():       # OK tSections.addAll(endMatches.keySet())
        tSections.add(k)

    enclosed=enclosed.intersection(tSections) # OK enclosed.retainAll(endMatches.keySet()) --> see https://www.geeksforgeeks.org/set-retainall-method-in-java-with-example/

    """ tSections will contain lines that intersect at the same point as 2+ other lines none of which are enclosed """
    tSections=tSections-enclosed
    lineSets=[]     # it is NOT a set, it will be treated as list of list of Line obj. It is the same of 'nway' -->  List<List<Line>> lineSets = new ArrayList<List<Line>>()

    """ Build our list of intersecting sets """
    for l1 in tSections:
        found = False
        """ search all line sets until we find an intersection with the current line """
        for i in range(len(lineSets)):
            if found is True:
                break
            intersects_lines =lineSets[i]
            for j in range(len(intersects_lines)):
                l2 = intersects_lines[j]
                """ 
                NB: 
                    we do not need to take the extra step of ensuring all  lines intersect at the same point (instead of some intersecting at  the start
					and some at the end, creating chains) because we have already filtered out the "enclosed" segments that would have arisen from that style of overlap
				"""
                if intersectsLine(l1,l2,SIGMA):
                    found=True
                    intersects_lines.append(l1)

            """ if no match, start new list"""
            if found is False:
                lineSets.append([l1])

    """ populate nWay intersection list """
    for intersects_lines2 in lineSets:
        if len(intersects_lines2)>2:
            nway.append(intersects_lines2)

    """ clean up enclosed lines.. any enclosed line that intersects with another enclosed line at BOTH ends should be removed """
    pruneEnclosed = True
    while pruneEnclosed:
        pruneEnclosed = False
        toRemove = None # it will be a Line obj
        for l1 in enclosed:
            foundStartMatch = False
            foundEndMatch = False
            for l2 in enclosed:
                if l1==l2:
                    continue
                elif intersectsStart(l1, l2, SIGMA):
                    foundStartMatch = True
                elif intersectsEnd(l1, l2, SIGMA):
                    foundEndMatch = True
                if foundEndMatch is True and foundStartMatch is True:
                    break

            """ found a line to prune remove it and restart """
            if foundEndMatch is True and foundStartMatch is True:
                toRemove=l1
                pruneEnclosed = True

        if toRemove is not None:
            if isinstance(toRemove,list) is False:
                toRemove = [toRemove]
            enclosed=enclosed-set(toRemove)




def buildIntersectionMaps(lines, enclosedLines, startIntersections, endIntersections):
    """
    Step 2: for each enclosed line, we want to map to the sets of all other lines with one intersection at the start, and all lines with one intersection at the end.
    :param lines:    List of Line
    :param enclosedLines:  set() of Line objs
    :param startIntersections: dict where key will be a Line obj, the value a list of Line value
    :param endIntersections: dict where key will be a Line obj, the value a list of Line value
    :return:
    """
    for l1 in enclosedLines:
        for l2 in lines:
            if l2==l1:
                continue
            elif intersectsStart(l1, l2, SIGMA):
                startIntersections.update({l1: l2})
            elif intersectsEnd(l1, l2, SIGMA):
                endIntersections.update({l1: l2})


def buildMergeList_A(lineMerges, enclosedLines, startIntersections, endIntersections):
    """
    Step 3a: With all mapped combinations determined, we determine the combinations that best preserve slope/straightness.
    :param lineMerges:  list of list of Line obj
    :param enclosedLines: set() of Line objs
    :param startIntersections: dict where key will be a Line obj, the value a list of Line value
    :param endIntersections: dict where key will be a Line obj, the value a list of Line value
    :return:
    """

    for enclosed in enclosedLines:
        """ 1. first compute points of interest. We separate them by count in case there are not even pairings """
        startPoints = []    # list of list of float
        endPoints = []      # list of list of float
        startLines = startIntersections.get(enclosed)
        endLines = endIntersections.get(enclosed)
        enclosedStart = [enclosed.getXCoordinates()[0], enclosed.getYCoordinates()[0]]
        enclosedEnd = [enclosed.getXCoordinates()[-1], enclosed.getYCoordinates()[-1]]
        if not isinstance(startLines, list):
            startLines = [startLines] if startLines is not None else []
        if not isinstance(endLines, list):
            endLines = [endLines] if endLines is not None else []
        for l in startLines:
            startPoints.append(getInterceptPoint(enclosedStart, l))
        for l in endLines:
            endPoints.append(getInterceptPoint(enclosedEnd, l))

        """ 2. for each line in the small set, find the line in the large set that would create the straightest merge. """
        while len(startLines) >0 and len(endLines)>0:
            startIndex = 0
            endIndex = 0
            minStraightness = FLOAT_MAX_VALUE_JAVA
            toMerge = [] # is a list of Line objs
            for i in range(len(startLines)):
                for j in range(len(endLines)):
                    straightness = straightCalc([startPoints[i], enclosedStart, enclosedEnd, endPoints[j]])
                    if straightness<minStraightness:
                        startIndex = i
                        endIndex = j
                        minStraightness = straightness

            """ Create the merge set and merge it on lineMerges"""
            del startLines[startIndex]
            del endLines[endIndex]

            if len(startLines)>0:
                toMerge+=startLines

            toMerge.append(enclosed)

            if len(endLines) > 0:
                toMerge+=endLines

            lineMerges.append(toMerge)

            """remove the selected points"""
            del(startPoints[startIndex])
            del (endPoints[endIndex])

        """ Unmatched lines are treated as singletons """
        unmatched  = startLines if len(startLines)>0 else endLines
        for line in unmatched:
            if not isinstance(line, list):
                line=[line]
            lineMerges.append(line)

    """ Clean up the merges If the end of one merge == the start of another, those merges are joined together """
    i,j=0,0
    while j<len(lineMerges):
        list1 = lineMerges[i]
        list2 = lineMerges[j]
        if list1[0] == list2[len(list2)-1]:
            del lineMerges[i]
            del list1[0]
            list2+=list1
            i=0
            j=1
        elif list2[0] == list1[len(list1)-1]:
            del lineMerges[i]
            del list2[0]
            list1+=list2
            i=0
            j=1
        else:
            j+=1
            if j== len(lineMerges):
                i+=1
                j=i+1




def buildMergeList_B(lineMerges, nWayIntersections):
    """
    Step 3b: The process for determining merges from N-way merges is to find the point where each line intersects, then compute the straightness of each potential merge and take the straightest
    :param lineMerges: list of list of Line obj
    :param nWayIntersections: it will be treated as list of list of Line obj
    :return:
    """
    for iSection in nWayIntersections: # iSection is a list of Line objs
        junction=[float,float]
        testLine=iSection[0]
        index =0
        if intersectsEnd(testLine, iSection.get(1), SIGMA) is True:
            index = testLine.num-1
        junction[0] = testLine.getXCoordinates()[index]
        junction[1] = testLine.getYCoordinates()[index]

        """ 2. Pair lines based on their straightness Merge sets are added as pairs or unpaired singleton lines """
        while len(iSection)>1:
            merge = [] # is a list of Line objs
            idx1,idx2=0,0
            minStraightness=FLOAT_MAX_VALUE_JAVA

            """ Find the merge with most straightness in our set of lines """
            for i in range(len(iSection)):
                icept = getInterceptPoint(junction, iSection.get(i))
                for j in range(i+1,len(iSection)):
                    jcept = getInterceptPoint(junction, iSection.get(j))
                    curStraightness = straightCalc([icept, junction, jcept])
                    if curStraightness<minStraightness:
                        minStraightness=curStraightness
                        idx1 = i
                        idx2 = j
            """ Add merged pair and remove from lists """
            merge+=[iSection[idx1],iSection[idx2]]
            del iSection[idx2]
            del iSection[idx1]
            lineMerges.append(merge)

        if  len(iSection)==1:
            lineMerges.append(iSection)



def buildResolvedList(originalLines, lineMerges, lineMap):
    """
    resolve merged line list
    :param originalLines:  List of Line
    :param lineMerges: list of list of Line obj
    :param lineMap: dict  # key,value will be a Line obj
    :return:
    """
    father_frame = originalLines[0].father_frame
    finalLines = set(originalLines)
    for toMerge in lineMerges:  # it is a list of line
        """ remove the individual, unmerged lines """
        a=set(toMerge)
        finalLines = finalLines-set(toMerge)
        newSize,frame = 0,0
        for l in toMerge:
            frame = l.frame
            newSize+=l.num

        """ build and add the merged line """
        merged = None
        if len(toMerge)==1:
            merged=toMerge[0]
        else:
            merged = Line(num=newSize)
            """ Assume the lines are now standing alone or no longer intersect on terminal ends and thus are "no_junc" class. This will be updated later after the Junction points are reassessed """
            merged.cont_class=COUNTOUR_DICT["cont_no_junc"]
            merged.frame=frame

            """ get the enclosed line """
            pos = 0
            for i in range(len(toMerge)):
                line =toMerge[i]
                adjacent = toMerge[i+1] if i==0 else toMerge[i-1]
                num = line.num
                fillArray(line, adjacent, i == 0, merged.angle, pos, line.angle, num)
                fillArray(line, adjacent, i == 0, merged.asymmetry, pos, line.asymmetry, num)
                fillArray(line, adjacent, i == 0, merged.col, pos, line.col, num)
                fillArray(line, adjacent, i == 0, merged.row, pos, line.row, num)
                fillArray(line, adjacent, i == 0, merged.response, pos, line.response, num)
                fillArray(line, adjacent, i == 0, merged.intensity, pos, line.intensity, num)
                fillArray(line, adjacent, i == 0, merged.width_l, pos, line.width_l, num)
                fillArray(line, adjacent, i == 0, merged.width_r, pos, line.width_r, num)
                pos+=num

                """ map the original line to the merged """
                lineMap.update({line:merged})

        finalLines.add(merged)


    for l in finalLines:
        l.father_frame=father_frame

    return finalLines


def updateJunctions(junctions, lineMap):
    """
    Look through all {@link Junction}s. If either of the lines has been merged, the Junction is updated to reference the merged line. Returns the set of all such modified Junctions
    :param junctions:
    :param lineMap: it is a dict. key,value are Line
    :return:
    """
    #todo: I cannot real understand the behaviour of this function without running it in the java console. it'd be buggy
    updated = set()
    for junction in junctions:
        toUpdate=False
        mergedLine =lineMap.get(junction.lineCont1)
        if mergedLine is not None:
            toUpdate=True
            junction.lineCont1=mergedLine
            junction.cont1=mergedLine.getID()

        mergedLine =lineMap.get(junction.lineCont2)
        if mergedLine is not None:
            junction.lineCont2=mergedLine
            junction.cont2=mergedLine.getID()
            toUpdate = True

        if toUpdate is True:
            updated.add(junction)

    return updated

def pruneJunctions(junctions, updatedJunctions):
    """
    Remove all redundant {@link Junction}s from the list. This includes Junctions with two references to the same line (because their lines were merged) and
	cases where multiple Junctions refer to the same lines as each other and occupy the same physical position
    :param junctions: all the junctions
    :param updatedJunctions:
    :return: None.
    """
    jMap=dict()  # key = string value = Junction
    index=0
    index_to_remove =[]
    for j in updatedJunctions:
        key=getKey(j)
        """ 
        Remove Junctions with references to the same Line OR Remove Junctions of the same two lines at the same x,y point """
        if j.cont1 == j.cont2 or key in jMap :
            index_to_remove.append(index)
        else:
            """ Keep the junction and register it as "the" definitive junction for its two lines at this point """
            jMap.update({key:j})
        index+=1

    """ remove the junctions"""
    for i in index_to_remove[::-1]:
        del junctions[i]

    """ Update the updatedJunctions set by removing all Junction instances that have been removed from the master Junctions collection """
    updatedJunctions.intersection(junctions) # OK updatedJunctions.retainAll(junctions)--> see https://www.geeksforgeeks.org/set-retainall-method-in-java-with-example/

def updateContourClasses(updatedJunctions):
    """
    For each {@link Junction} in the provided set, update the Junction's {@link Junction#pos}, {@link Junction#isNonTerminal}, and each line's {@link LinesUtil.contour_class} as appropriate.
    :param updatedJunctions:
    :return:
    """
    for j in updatedJunctions:
        """ process both lines. For isNonTerminal to be updated, the junction point can't be on either line's terminals. We only update the pos of the Junction on the first line """
        j.isNonTerminal = processLine(j, j.lineCont1, True) and  processLine(j, j.lineCont2, False)

def processLine(j,line,updatePos =False):
    """
    Iterate over the points of the line and find the pos of the junction If pos is 0 or line.length, update the line's contour class If this is the first line, set the Junction's pos to match If this junction doesn't sit on either line's terminals, set the Junction's isNonTerminal to true
    :param j:
    :param line:
    :param updatePos: if true, update the pos of the given Junction
    :return: True if the junction point was NOT on the start or end terminal of the given line
    """
    if not isinstance(line, Line):
        print("ERROR: In 'SlopeOvelapResolver.processLine', the 'line' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->processLine)")
        logging.error(" In 'SlopeOvelapResolver.processLine', the 'line' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->processLine)")
        exit(-1)
    if not isinstance(j, Junction):
        print("ERROR: In 'SlopeOvelapResolver.processLine', the 'j' input value has to be an instance of the class 'Junction'.(slopeOverlapResolver.py->processLine)")
        logging.error(" In 'SlopeOvelapResolver.processLine', the 'j' input value has to be an instance of the class 'Junction'.(slopeOverlapResolver.py->processLine)")
        exit(-1)
    pos = None
    x = line.getXCoordinates()
    y = line.getYCoordinates()
    """ loop over all points of the line, or until we find the point of intersection with the junction """
    for i in range(line.num):
        if x[i] == j.x and y[i] == j.y:
            pos=i
            break

    """ update the Junction position if requested """
    if updatePos is True:
        j.pos = pos

    """ update contour class if appropriate Nothing can supersede 'cont_both_junc'"""
    if line.cont_class != COUNTOUR_DICT["cont_both_junc"]:

        if pos == 0:
            """ If this line is already an 'end_junc', upgrade it to a 'both'"""
            new_contour= COUNTOUR_DICT["cont_both_junc"] if line.cont_class == COUNTOUR_DICT["cont_end_junc"] else COUNTOUR_DICT["cont_start_junc"]
            line.cont_class=new_contour
        elif pos==line.num-1:
            """ If this line is already a "start_junc", upgrade it to a "both" """
            new_contour = COUNTOUR_DICT["cont_both_junc"] if line.cont_class == COUNTOUR_DICT["cont_start_junc"] else COUNTOUR_DICT["cont_end_junc"]
            line.cont_class=new_contour

    """ Check the position of the junction within the line """
    return not(pos == 0 or pos == line.num - 1)

def straightCalc(points):
    """
    Compute the striaghtness between a list of points. This is done by comparing distances: {@code ((p1 + p2) + (p2 + 3)) / (p3 + p1)} The closer the value is to 1, the straighter the line
    NB: it is called with 4 points in 'buildMergeList_A'
    :param points:
    :return:
    """
    ideal = dist(points[0], points[-1])
    s=0
    for i in range(1,len(points)):
        s+= dist(points[i - 1], points[i])
    return s/ideal

def dist(p1,p2):
    """
    return the distance between 2 points
    :param p1:
    :param p2:
    :return:
    """
    return sqrt(pow((p2[0] - p1[0]), 2) + pow((p2[1] - p1[1]), 2))

def fillArray(line, adjacent, adjacentIsNext, target, pos, source, length):
    """
    Copy to the target at the given position. Use the source array if it is non-null. Otherwise fill with 0's
    :param line: the line
    :param adjacent: the adjacent line
    :param adjacentIsNext: True if the adjacent is the next line
    :param target:
    :param pos:
    :param source:
    :param length:
    :return:
    """
    if not isinstance(line, Line):
        print("ERROR: In 'SlopeOvelapResolver.fillArray', the 'line' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->fillArray)")
        logging.error(" In 'SlopeOvelapResolver.fillArray', the 'line' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->fillArray)")
        exit(-1)
    if source is None or source == []:
        target[pos:pos+length] = [0 for i in range(length)]     #todo: I faked Arrays.fill. Test if it works properly
    else:
        """ 
        If the adjacent (reference) line is the next line in the sequence, then we reverse the array if our current line's head is its intersection
		point. If the reference line is the previous line in the sequence, we reverse the array if our current line's tail is its intersection point
		"""
        if (adjacentIsNext and intersectsStart(line, adjacent, SIGMA)) or (not adjacentIsNext and intersectsEnd(line, adjacent, SIGMA)):
            """ reverse the source array """
            for i in range(len(source)-1,-1,-1):
                pos+=1
                target[pos]=source[1]
        else:
            """ oriented appropriately """
            target = deepcopy(source[pos:length])



def getInterceptPoint(p1, query):
    """
    Helper method to get the point at {@code SLOPE_DIST} positions away from the intercept point between the query line and given point
    :param p1:
    :param query:
    :return:
    """
    if not isinstance(query, Line):
        print("ERROR: In 'SlopeOvelapResolver.getInterceptPoint', the 'query' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->fillArray)")
        logging.error("In 'SlopeOvelapResolver.getInterceptPoint', the 'query' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->fillArray)")
        exit(-1)
    return findLongestPath(query, distance=0, points=[p1])

def findLongestPath(query, distance, points):
    """
    Recursive helper method. Iteratively searches to the next {@link #SLOPE_DIST} position in the query line. As long as this point maintains straightness
	within {@link #STRAIGHT_TOLERANCE}, and we haven't gone past the query line boundaries, recursion continues
    :param query:
    :param distance:
    :param points: it is a List<float[]> ... hence I treat it as a list of 2D list --> [[x,y],....,[xn,yn]]
    :return:
    """
    if not isinstance(query, Line):
        print("ERROR: In 'SlopeOvelapResolver.findLongestPath', the 'query' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->findLongestPath)")
        logging.error(" In 'SlopeOvelapResolver.findLongestPath', the 'query' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->findLongestPath)")
        exit(-1)

    p1= points[0]    #original point to test

    """ Incrementally check the next position """
    distance +=SLOPE_DIST

    """ Determine the position to check based on whether the query line intersects with p1 at its start or end """
    pos = min(distance, query.num - 1)  if abs(p1[0] - query.getXCoordinates()[0]) < SIGMA and abs(p1[1] - query.getYCoordinates()[0]) < SIGMA else max(0, query.num - 1)
    p2=[query.getXCoordinates()[pos], query.getYCoordinates()[pos]]

    """ if our position has reached the start (or end) of the query line, return p2 """
    if pos == 0 or pos == query.num - 1:
        return p2

    """ If we still have a straight enough line, recurse to the next position """
    points.append(p2)
    if straightCalc(points) <= STRAIGHT_TOLERANCE:
        return findLongestPath(query, distance, points)

    return points[len(points)-2]

def intersectsLine(l1,l2, threshold):
    """
    :param l1:
    :param l2:
    :param threshold:
    :return: true if the two specified lines intersect at their start or end points
    """
    if not isinstance(l1, Line):
        print("ERROR: In 'SlopeOvelapResolver.intersectLine', the 'l1' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->intersectsLine)")
        logging.error("In 'SlopeOvelapResolver.intersectLine', the 'l1' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->intersectsLine)")
        exit(-1)
    if not isinstance(l2, Line):
        print("ERROR: In 'SlopeOvelapResolver.intersectLine', the 'l2' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->intersectsLine)")
        logging.error("In 'SlopeOvelapResolver.intersectLine', the 'l2' input value has to be an instance of the class 'Line'. (slopeOverlapResolver.py->intersectsLine)")
        exit(-1)
    return intersectsStart(l1, l2, threshold) or intersectsEnd(l1, l2, threshold)

def intersectsStart(target, query, threshold):
    """
    Helper method to determine if the query line intersects with the target at  its start terminal
    :param target:
    :param query:
    :param threshold:
    :return:
    """
    if not isinstance(target, Line):
        print("ERROR: In 'SlopeOvelapResolver.intersectsStart', the 'target' input value has to be an instance of the class 'Line'.")
        logging.error(" In 'SlopeOvelapResolver.intersectsStart', the 'target' input value has to be an instance of the class 'Line'.")
        exit(-1)
    if not isinstance(query, Line):
        print("ERROR: In 'SlopeOvelapResolver.intersectsStart', the 'query' input value has to be an instance of the class 'Line'.")
        logging.error(" 'SlopeOvelapResolver.intersectsStart', the 'query' input value has to be an instance of the class 'Line'.")
        exit(-1)
    tStart = getPoint(target, 0)
    qStart = getPoint(query, 0)
    qEnd = getPoint(query, query.num - 1)
    return intersects(tStart, qStart, threshold) or intersects(tStart, qEnd, threshold)

def intersectsEnd(target, query, threshold):
    """
    Helper method to determine if the query line intersects with the target at its end terminal
    :param target:
    :param query:
    :param threshold:
    :return:
    """
    if not isinstance(target, Line):
        print("ERROR: In 'SlopeOvelapResolver.intersectsEnd', the 'target' input value has to be an instance of the class 'Line'.")
        logging.error(" In 'SlopeOvelapResolver.intersectsEnd', the 'target' input value has to be an instance of the class 'Line'.")
        exit(-1)
    if not isinstance(query, Line):
        print("ERROR: In 'SlopeOvelapResolver.intersectsEnd', the 'query' input value has to be an instance of the class 'Line'.")
        logging.error(" In 'SlopeOvelapResolver.intersectsEnd', the 'query' input value has to be an instance of the class 'Line'.")
        exit(-1)
    tEnd = getPoint(target, target.num - 1)
    qStart = getPoint(query, 0)
    qEnd = getPoint(query, query.num - 1)
    return intersects(tEnd, qStart, threshold) or intersects(tEnd, qEnd, threshold)

def intersects(tEnd,qEnd,threshold):
    """

    :param tEnd:
    :param qEnd:
    :param threshold:
    :return: if the distance between two points is within the given threshold
    """
    return abs(qEnd[0] - tEnd[0]) < threshold and abs(qEnd[1] - tEnd[1]) < threshold

def getKey(junction):
    """
    Builds a unique key identifying a given {@link Junction} based on the two associated lines, and the Junction's position
    :param junction:
    :return:
    """
    if not isinstance(junction, Junction):
        print("ERROR: In 'SlopeOvelapResolver.getKey',the 'junction' input value has to be an instance of the class 'Junction'.")
        logging.error(" In 'SlopeOvelapResolver.getKey',the 'junction' input value has to be an instance of the class 'Junction'.")
        exit(-1)
    return  str(min(junction.cont1, junction.cont2))+str(max(junction.cont1, junction.cont2))+str(junction.x)+str(junction.y)

def getPoint(target, i):
    """
    Helper method to return the x and y coordinates of the point at the specified index of a given line
    :param target:
    :param i:
    :return:
    """
    if not isinstance(target, Line):
        print("ERROR: In 'SlopeOvelapResolver.getPoint', the 'target' input value has to be an instance of the class 'Line'.")
        logging.error(" In 'SlopeOvelapResolver.getPoint', the 'target' input value has to be an instance of the class 'Line'.")
        exit(-1)
    return [target.getXCoordinates()[i],target.getYCoordinates()[i]]

def matchesStart(junction,line):
    """
    Helper method to determine if a junction sits on the start point of a line
    :param junction:
    :param line:
    :return:
    """
    if not isinstance(line, Line):
        print("ERROR: In 'SlopeOvelapResolver.matchesStart', the 'line' input value has to be an instance of the class 'Line'.")
        logging.error(" In 'SlopeOvelapResolver.matchesStart', the 'line' input value has to be an instance of the class 'Line'.")
        exit(-1)
    if not isinstance(junction, Junction):
        print("ERROR: In 'SlopeOvelapResolver.matchesStart', tThe 'junction' input value has to be an instance of the class 'Junction'.")
        logging.error(" In 'SlopeOvelapResolver.matchesStart', tThe 'junction' input value has to be an instance of the class 'Junction'.")
        exit(-1)
    return line.getXCoordinates()[0] == junction.x and line.getYCoordinates()[0] == junction.y

def matchesEnd(junction,line):
    """
    Helper method to determine if a junction sits on the end point of a line
    :param junction:
    :param line:
    :return:
    """
    if not isinstance(line, Line):
        print("ERROR: In 'SlopeOvelapResolver.matchesEnd', the 'line' input value has to be an instance of the class 'Line'.")
        logging.error(" In 'SlopeOvelapResolver.matchesEnd', the 'line' input value has to be an instance of the class 'Line'.")
        exit(-1)
    count = line.num - 1
    return line.getXCoordinates()[count] == junction.x and line.getYCoordinates()[count] == junction.y



