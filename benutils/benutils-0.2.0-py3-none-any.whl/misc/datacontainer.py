# -*- coding: utf-8 -*-

"""package benutils
author    Benoit Dubois
copyright FEMTO ENGINEERING, 2019
license   GPL v3.0+
brief     A container used to handle a set of timestamped data.
"""

import logging
import numpy as np
from collections import namedtuple, OrderedDict
from PyQt5.QtCore import QObject, pyqtSignal


class TimeSerieContainer(QObject):
    """TimeSerieContainer class, a container used to handle a set of
    timestamped data. The timestamps are collected in the dictionnary with
    the key 'time'.
    """

    updated = pyqtSignal()
    new_data = pyqtSignal(object)

    def __init__(self):
        """Init instance.
        :returns: None
        """
        super().__init__()
        self._tsdata = namedtuple('TimeData', 'time tdata')
        self._tsdata.time = np.empty([1, 0])
        self._tsdata.tdata = OrderedDict()

    def __repr__(self):
        return "TimeSerieContainer (({}, {}), {})".format(self.keys(),
                                                          self.get_array(),
                                                          id(self))

    def __str__(self):
        return "TimeSerieContainer ({}, {})".format(self.keys(),
                                                    self.get_array())

    def __iter__(self):
        """Iterator.
        :returns: iterator on the dictionnary of data.
        """
        yield 'time'
        for key in self._tsdata.tdata:
            yield key

    def __len__(self):
        """Standard 'len()' class method.
        :returns: number of items in dictionnary (int)
        """
        return len(self._tsdata.tdata) + 1

    def get_array(self):
        """Return an array containing data of container.
        :returns: an array view of data (numpy array)
        """
        aview = np.array([self.data(key) for key in self], ndmin=2)
        return aview

    def keys(self):
        """Return a list representing keys of container.
        :returns: keys of container (list)
        """
        keys = ['time']
        for key in self._tsdata.tdata:
            keys.append(key)
        return keys

    def values(self):
        """Iterator on value of container.
        :returns: iterator on the values of the dictionnary of data.
        """
        yield self._tsdata.time
        for key in self._tsdata.tdata:
            yield self._tsdata.tdata[key]

    def reset(self):
        """Return to its init state. Alias for clear() method.
        :returns: None
        """
        self.clear()

    def clear(self):
        """Remove all items, except 'time', from the container.
        :returns: None
        """
        self._tsdata.time = np.empty([1, 0], dtype=float)
        self._tsdata.tdata.clear()
        self.updated.emit()

    def clear_data(self):
        """Clear the data but remains dictionary items.
        :returns: None
        """
        self._tsdata.time = np.empty([1, 0], dtype=float)
        for key in self._tsdata.tdata.keys():
            self._tsdata.tdata[key] = np.empty([1, 0], dtype=float)
        self.updated.emit()

    def is_empty(self):
        """Returns True if the container is empty; otherwise returns False.
        :returns: True if thecontainer is empty else False (bool)
        """
        if len(self._tsdata.tdata) != 0:
            return False
        else:
            return True

    def data(self, key=None):
        """Return data from the item indexed by key, if key is None, get of
        whole data (in this case data are formated, timestamp value in the
        first column then the data in ordered order).
        :param key: a unique idendifier in dictionnary (object)
        :returns: data from the item indexed by key or all items (np.array)
        """
        if key is None:
            data_list = [self._tsdata.time]
            for key in self._tsdata.tdata:
                data_list.append(self._tsdata.tdata[key])
            data = np.transpose(np.asarray(data_list))
        elif key is 'time':
            data = self._tsdata.time
        else:
            try:
                data = self._tsdata.tdata[key]
            except KeyError:
                logging.error("Try to get data of unexisting item %r", key)
                raise KeyError
        return data

    def add_sample(self, key, sample):
        """Add sample in the item indexed by key.
        Sample must be "Numpy array compatible".
        :param key: a unique idendifier in dictionnary (object)
        :param sample: sample(s) to add @ queue of item indexed by key (array)
        :returns: None
        """
        if key not in self._tsdata.tdata.keys():
            logging.error("Try to add sample in unexisting item " + str(key))
            raise KeyError
        if key is 'time':
            self._tsdata.time = np.append(self._tsdata.time, sample)
        else:
            self._tsdata.tdata[key] = np.append(self._tsdata.tdata[key],
                                                sample)
        self.new_data.emit(sample)
        self.updated.emit()

    def add_samples(self, samples):
        """Add samples in the container in each item. The number of sample must
        be of the size of the number of item number. Samples must be "Numpy
        array compatible".
        :param samples: samples to add @ queue of eachitem (list)
        :returns: None
        """
        assert len(samples) == len(self._tsdata.tdata) + 1, \
            "Number of samples mismatch the container size"
        self._tsdata.time = np.append(self._tsdata.time, samples[0])
        for sample, key in zip(samples[1:], self._tsdata.tdata):
            self._tsdata.tdata[key] = np.append(self._tsdata.tdata[key],
                                                sample)
        self.new_data.emit(samples)
        self.updated.emit()

    def add_item(self, key):
        """Add an item (identified by 'key') in the dictionnary of data.
        :param key: a unique idendifier in dictionnary (object)
        :returns: None
        """
        self._tsdata.tdata[key] = np.empty([1, 0])

    def remove_item(self, key):
        """Remove an item in the dictionnary of data.
        :param key: a unique idendifier in dictionnary (object)
        :returns: None
        """
        try:
            del self._tsdata.tdata[key]
        except KeyError:
            logging.warning("Try to remove unexisting item: %r", key)


# =============================================================================
if __name__ == "__main__":
    ts = TimeSerieContainer()

    print("ts empty:", ts)

    ts.add_item('c')
    ts.add_item('b')
    ts.add_item('a')
    ts.add_samples([10, 1, 2, 3])
    ts.add_samples([20, 4, 5, 6])
    ts.add_samples([30, 7, 8, 9])

    print("len(ts):", len(ts))

    print("k\t ts.data(k):")
    for k in ts:
        print(k, "\t", ts.data(k))

    print("ts.value:")
    for v in ts.values():
        print(v)

    print("array view 1:\n", ts.get_array())

    print("__repr__(ts):\n", ts.__repr__())

    print("__str__(ts):\n", ts)

    ts_iter = iter(ts)
    print("next(ts_iter)", next(ts_iter))
    print("next(ts_iter)", next(ts_iter))
    print("next(ts_iter)", next(ts_iter))
    print("next(ts_iter)", next(ts_iter))
    try:
        print("next(ts_iter)", next(ts_iter))
    except StopIteration:
        print("StopIteration raised")

    print("remove key 'b'")
    ts.remove_item('b')
    print("array view 2:\n", ts.get_array())

    print("clear data")
    ts.clear_data()
    print("array view 3:\n", ts.get_array())

    print("reset data")
    ts.reset()
    print("array view 4:\n", ts.get_array())
