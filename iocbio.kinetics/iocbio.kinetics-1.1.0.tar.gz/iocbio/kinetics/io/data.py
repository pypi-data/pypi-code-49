
"""Classes for representing experimental data and carrier for the measured values"""

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
import copy, uuid
import numpy as np


class Carrier:
    """Measured value data carrier

    Used as a carrier for measured values.

    Attributes
    ----------
    name: str
      Name of the measured value. For example, O2
    unit: str
      Unit in which the value has been measured
    data: numpy.array
      Array of values
    """
    
    def __init__(self, name, unit, data):
        self.name = name
        self.unit = unit
        self.data = data


class Data(object):
    """Class for representing recorded data

    Object of this class represents the experimental data and is used
    to initialize all analyzers, split the data into regions of
    interest, and hold event names. It is initially constructed by the
    reader module and later split into regions of interest using its
    methods.

    Parameters
    ----------
    experiment_id : str
      Experiment ID
    data : dict, optional
      Data dictionary consisting of key -> dict(x=xarray, y=ycarrier) where
      key is used to access particular data when calling methods `x` and `y`,
      xarray is its x-argument and ycarrier is measured value represented by
      :class:`Carrier` object.
    xname : str, optional
      Name of x-axis. For example, Time
    xunit : str, optional
      Unit of x-axis
    xlim : tuple, optional
      Tuple (xmin, xmax) defining the range of the x-axis
    comment: str, optional
      Comment regarding experiment
    config : dict, optional
      Data-specific configuration passed from reader to the analyzers
    name : str
      Name of experiment. For example, full path of the imported raw data file.
    time : str
      Time at which experiment was performed. For example, "2020.01.21 16:32"
    type : str
      Specific type of experiment. For example, "Respiration trace measured on Strathkelvin"
    type_generic : str
      Generic type of experiment. For example, "Respiration trace". Notice the difference with `type`.
    data_id : str, optional
      ID of the region of interest. Used if the object represents a slice from
      the full dataset.
    add_range : float, optional
      Used to calculate a range of a new slice when added by the user. Given in fraction (0 to 1)
      of the full data range it is formed from. For example, if the original dataset is measured
      during 100 seconds and add_range is 0.05 then the new slice will be 5 seconds when created by
      user. User can later adjust the slice as required.

    
    Attributes
    ----------
    add_range : float
      Used to calculate a range of a new slice when added by the user. Given in fraction (0 to 1)
      of the full data range it is formed from. For example, if the original dataset is measured
      during 100 seconds and add_range is 0.05 then the new slice will be 5 seconds when created by
      user. User can later adjust the slice as required.
    config : dict
      Data-specific configuration passed from reader to the analyzers
    data_id : str
      ID of the region of interest. Used if the object represents a slice from
      the full dataset.
    experiment_id : str
      Experiment ID
    event_name : str
      Event associated with the data slice
    event_value: float, optional
      Event value (if applicable) associated with the data slice
    name : str
      Name of experiment. For example, full path of the imported raw data file.
    time : str
      Time at which experiment was performed. For example, "2020.01.21 16:32"
    type : str
      Specific type of experiment. For example, "Respiration trace measured on Strathkelvin"
    type_generic : str
      Generic type of experiment. For example, "Respiration trace". Notice the difference with `type`.

    """

    def __init__(self, experiment_id,
                 comment = None,
                 data = {},
                 xname = None,
                 xunit = None,
                 xlim = None,
                 config = {},
                 type = None,
                 type_generic = None,
                 name = None,
                 time = None,
                 data_id = None,
                 add_range=0.05):

        if data_id is None:
            data_id = str(uuid.uuid4())

        self._data = data
        self._xname = xname
        self._xunit = xunit
        self._xlim = xlim
        self.config = config
        self.type = type
        self.type_generic = type_generic
        self.name = name
        self.time = time
        self.experiment_id = experiment_id
        self.data_id = data_id
        self.event_name = None
        self.event_value = None
        self.add_range = add_range
        k = list(self._data.keys())
        if k: self._rep_key = k[0]
        else: self._rep_key = None

    def x(self, name):
        """x-axis values for variable

        Parameters
        ----------
        name: str
          key of the dictionary passed as `data` in the object constructor

        Returns
        -------
        numpy.array
        """
        
        if name is None:
            return self.x(name=self._rep_key)
        return self._data[name]['x']

    def xlim(self):
        """x-axis limits"""
        
        return self._xlim

    @property
    def xname(self):
        """Name of the x-axis"""
        
        return self._xname

    @property
    def xunit(self):
        """Units of x-axis"""
        
        return self._xunit

    def y(self, name):
        """Measured values for variable

        Parameters
        ----------
        name: str
          key of the dictionary passed as `data` in the object constructor

        Returns
        -------
        Carrier
          Carrier with the variable values, name, and units
        """
        
        return self._data[name]['y']

    def keys(self):
        """Variable names supported by the object

        Returns
        -------
        set-like object
          Keys of the dictionary passed as `data` in the object constructor        
        """
        
        return self._data.keys()

    def slice(self, x0, x1, data_id=None, event_name=None, event_value=None):
        """Select a slice from the data

        When selecting a region of interest, this function is called
        to create a new :class:Data that represents this ROI. ROI is
        defined through the range (x0,x1), event, and its ID.

        Parameters
        ----------
        x0 : float
          start of the range on x-axis
        x1 : float
          end of the range on x-axis
        data_id : str, optional
          ID of the region of interest. If not set, it will be generated using uuid.uuid4()
        event_name : str, optional
          Event name
        event_value : float, optional
          Event value

        Returns
        -------
        Data
          Data representing the section of the original data

        """
        
        a = copy.deepcopy(self)
        if data_id is None:
            data_id = str(uuid.uuid4())
        a.data_id = data_id
        a.event_name = event_name
        a.event_value = event_value
        a._xlim = (x0, x1)

        for k in a._data.keys():
            
            i0 = np.argmin(np.abs(self._data[k]['x']-x0))
            i1 = np.argmin(np.abs(self._data[k]['x']-x1))
            a._data[k]['x'] = a._data[k]['x'][i0:i1]
            a._data[k]['y'].data = a._data[k]['y'].data[i0:i1]
        return a

    def new_range(self, x0):
        """Helper method to suggest the range of the new slice"""
        
        minx, maxx = self.xlim()
        w = self.add_range*(maxx-minx)
        return [x0, x0+w]

    def __repr__(self):
        s = 'type: %s; expid: %s; dataid: %s\nx: %s ' % (self.type, self.experiment_id, self.data_id,
                                                         self._xname)
        # if self.x.data is not None: s += "%f..%f" % (self.x.data[0], self.x.data[-1])
        # s += "; data:"
        # for i in self.data:
        #     s += i + " "
        # s += "\nconfig:\n"
        # for k, v in self.config.items():
        #     s += k + ": " + str(v) + "\n"

        return s
