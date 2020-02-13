# -*- coding: utf-8 -*-

"""package benutils
author    Benoit Dubois
copyright FEMTO ENGINEERING, 2019
license   GPL v3.0+
brief     Implement a median filter
"""

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import numpy as np


# =============================================================================
class MedianFilter(QObject):
    """Class MedianFilter, implements a (sliding) median filter of length m.
    """

    outUpdated = pyqtSignal((float,), (str,))
    inUpdated = pyqtSignal((float,), (str,))

    def __init__(self, length=1, ini_value=0.0, state=False, parent=None):
        """The constructor.
        :param length: length of data buffer (int)
        :param ini_value: default value(s) of filter (float or list of float)
        :param state: state of filtering (bool)
        :returns: None
        """
        super().__init__(parent=parent)
        self._ini_value = ini_value
        self._state = state
        self._m = length
        self._idx = 0
        self._out = 0.0
        self._data = np.full([length], ini_value, np.float64)  # FIFO

    def reset(self):
        """Reset filter.
        """
        self._data = np.full([self._m], self._ini_value, np.float64)
        self._idx = 0
        self._out = 0.0

    def set_state(self, state):
        """Set state of filtering: if state is True, output data are
        median filtered else output data are not filtered.
        :param state: state of filtering (bool)
        :returns: None
        """
        if isinstance(state, bool) is False:
            raise TypeError("state is not of bool type")
        self._state = state

    def get_state(self):
        """Get state of filtering: if state is True, output data are
        median filtered else output data are not filtered.
        :returns: state of filtering (bool)
        """
        return self._state

    def set_ini(self, value):
        """Set initial (default) value(s) of filter. Value can be a single
        value i.e. all the internal filter data got the same value or
        an array of the same length of the filter.
        :param value: default value(s) of filter (float or list of float)
        :returns: None
        """
        self._ini_value = value

    def get_ini(self):
        """Get initial (default) value(s) of filter.
        :returns: default value(s) of filter (float or list of float)
        """
        return self._ini_value

    def set_m(self, length):
        """Set filter length.
        :param lentgh: filter length (int)
        :returns: None
        """
        if isinstance(length, int) is False:
            raise TypeError("length is not of int type")
        if length < 1:
            raise AttributeError("length must be >= 1")
        self._data = np.full([length], self._ini_value, np.float64)
        self._m = length
        if self._idx >= length:
            self._idx = length - 1

    def get_m(self):
        """Get filter length.
        :returns: filter length (int)
        """
        return self._m

    def _add_data(self, inp):
        """Add new data into a circular buffer.
        :param inp: new data input value (float)
        :returns: None
        """
        self._data[self._idx] = inp
        self._idx = (self._idx + 1) % self._m

    def _filtering(self):
        """Compute filtered response of data, here median filtering.
        :returns: filtered data (float)
        """
        sorted_ = np.sort(self._data)
        mid_idx = int(self._m / 2)
        if self._m % 2 != 0:
            ret = sorted_[mid_idx]
        else:
            ret = (sorted_[mid_idx-1] + sorted_[mid_idx]) / 2
        return ret

    @pyqtSlot(float)
    @pyqtSlot(str)
    def process(self, inp):
        """Decimation process. Emits 'outUpdated' signal when data is ready
        for output.
        :param inp: new data value (str, float)
        :returns: None
        """
        inp = float(inp)
        # Notify new computation (ie new data at input of PID)
        self.inUpdated[float].emit(inp)
        self.inUpdated[str].emit('{:0.10E}'.format(inp))
        # Add new data
        self._add_data(inp)
        # Compute output value
        if self._state is True:
            self._out = self._filtering()
        else:
            self._out = self._data[-1]
        self.outUpdated[float].emit(self._out)
        self.outUpdated[str].emit('{:0.10E}'.format(self._out))
        return self._out


# =============================================================================
if __name__ == '__main__':

    def print_dec_out(value):
        """Just print value to stdout.
        """
        print(value)

    MED = MedianFilter(3)
    MED.outUpdated[str].connect(print_dec_out)
    X = [2, 80, 6, 3, 3]
    Y = [0, 2, 6, 6, 3]  # For m = 3
    for val in X:
        RET = MED.process(val)
#        GOOD = Y.pop(0)
#        if RET != GOOD:
#            print("Error {} instead of {}".format(RET, GOOD))
