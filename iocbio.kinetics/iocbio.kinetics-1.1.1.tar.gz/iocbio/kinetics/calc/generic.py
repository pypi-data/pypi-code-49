# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
# General types used by analyzers

from collections import namedtuple
from PyQt5.QtCore import pyqtSignal, QObject


class XYData(object):
    """Class for representing x,y dataset

    Can be used with numerical arrays to carry experimental or
    calculated datasets, or any other types. In addition to numerical
    arrays, it is used to transfer axis names and units.

    Attributes
    ----------
    x : any type
    y : any type

    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Stats:
    """Class for representing statistics result

    Used to transfer results of some calculation (statistics) from
    analyzers to tables showing them.

    Attributes
    ----------
    human : str
      Description of the statistical value. For example, 'Respiration rate'
    value : float
      Value of the statistics
    unit : str
      Units of the statistics
    """

    def __init__(self, human, unit, value):
        self.human = human
        self.unit = unit
        self.value = value


class AnalyzerGeneric(object):
    """Base class for all analyzers

    This is a base class that is used by all analyzers.

    Parameters
    ----------
    x : numpy.array
      Experimental data, x axis
    y : numpy.array
      Experimental data, values (y axis)

    Attributes
    ----------
    axisnames : iocbio.kinetics.calc.generic.XYData
      XYData consisting of two strings with the axis names
    axisunits : iocbio.kinetics.calc.generic.XYData
      XYData consisting of two strings with the axis units
    calc : iocbio.kinetics.calc.generic.XYData
      Is expected to be filled with the calculated approximation after the fit. Used by GUI when plots are shown
    composer : bool
      True if the analyzer is of Composer type (consisting of several analyzers)
    experiment : iocbio.kinetics.calc.generic.XYData
      Experimental data points. Used by GUI when plots are shown
    stats : dict
      Dictionary with statistics. Dictionary keys are used internally for sorting when shown in the table, values are of :class:Stats type.
    """

    def __init__(self, x, y):
        self.experiment = XYData(x, y)
        self.calc = XYData(None, None)
        self.axisnames = XYData("undefined", "undefined")
        self.axisunits = XYData("undefined", "undefined")
        self.stats = {}
        self.composer = False

    def update_data(self, x, y):
        """Update experimental data"""
        
        self.experiment = XYData(x, y)

class AnalyzerGenericSignals(QObject):
    """Helper class that can be used as a signal attribute for analyzers"""
    sigUpdate = pyqtSignal()
