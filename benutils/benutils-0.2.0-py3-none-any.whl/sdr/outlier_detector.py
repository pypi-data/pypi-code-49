# -*- coding: utf-8 -*-

"""package benutils
author    Benoit Dubois
copyright FEMTO ENGINEERING, 2018
license   GPL v3.0+
brief     Outlier detector
details   Detect outlier samples in a serie using 'deviation from mean'
          algorithm. Outlier samples are spotted by generation of the
          signal "data_valid". In 'reject mode', if outlier is detected,
          signal is generated AND sample is rejected i.e. output remains
          unmodified.
"""

import numpy as np
import signalslot as ss


DATA_CHECK_ARRAY_LENGTH = 10
MONITORING_MODE, REJECT_MODE = 0, 1


def check_deviation_from_mean(data, datas, sigma=1.0):
    """Outlier detector: detect if a value deviate from the mean.
    :param data: data to check (ndarray)
    :param datas: reference serie (ndarray)
    :param sigma: confidence interval in number of sigma (float)
    :returns: True if data is correct else False (bool)
    """
    mean = np.mean(datas)
    std = np.std(datas)
    if data > mean + std * sigma:
        return False
    return True


class OutlierDetector():
    """Class OutlierDetector
    """

    data_checked = ss.Signal(['flag'])  # New data have been checked
    outUpdated = ss.Signal(['value'])   # New data availlable at output

    def __init__(self, mode=MONITORING_MODE,
                 length=DATA_CHECK_ARRAY_LENGTH,
                 ini_value=0.0):
        """The constructor.
        :param mode: Behavior with outliers, monitoring or reject (int)
        :param length: length of the data buffer (int)
        :returns: None
        """
        self._idx = 0
        self._mode = MONITORING_MODE
        self._ini_value = ini_value
        self._m = length
        self._data = np.full([length], ini_value, np.float64)  # FIFO

    def reset(self, **kwargs):
        """Reset.
        :returns: None
        """
        self._data = np.full([self._m], self._ini_value, np.float64)
        self._idx = 0

    def set_ini(self, value):
        self._ini_value = value

    def get_ini(self):
        return self._ini_value

    def set_mode(self, mode):
        """Set mode.
        :param mode: Behavior with outliers, monitoring or reject (int)
        :returns: None
        """
        self._mode = mode

    def get_mode(self):
        """Get mode
        :returns: mode (int)
        """
        return self._mode

    def set_m(self, length):
        """Set filter length.
        :param length: length of the data buffer (int)
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
        :returns: length of data the buffer (int)
        """
        return self._m

    def process(self, value, **kwargs):
        """Check data validity
        :param value: new data value (float)
        :returns: None
        """
        inp = float(value)
        if check_deviation_from_mean(inp, self._data, sigma=9.0) is False:
            self.data_checked.emit(flag=False)
            if self._mode == MONITORING_MODE:
                self.outUpdated.emit(value=inp)
        else:
            self.data_checked.emit(flag=True)
            self.outUpdated.emit(value=inp)
        # Update data buffer
        self._data[self._idx] = inp
        self._idx = (self._idx + 1) % self._m
