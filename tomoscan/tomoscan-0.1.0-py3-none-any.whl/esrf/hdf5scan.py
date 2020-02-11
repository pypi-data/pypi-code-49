# coding: utf-8
#/*##########################################################################
# Copyright (C) 2016-2020 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#############################################################################*/


__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "09/08/2018"


from ..scanbase import TomoScanBase
import json
import io
import os
import h5py
import numpy
from silx.io.url import DataUrl
from tomoscan.utils import docstring
import logging

_logger = logging.getLogger(__name__)


class HDF5TomoScan(TomoScanBase):
    """
    This is the implementation of a TomoBase class for an acquisition stored
    in a HDF5 file.

    For now several property of the acquisition is accessible thought a getter
    (like get_scan_range) and a property (scan_range).

    This is done to be compliant with TomoBase instantiation. But his will be
    replace progressively by properties at the 'TomoBase' level

    :param scan: scan directory or scan masterfile.h5
    :type: Union[str,None]
    """
    _TYPE = 'hdf5'

    _DEFAULT_ENTRY = '1_tomo'

    _PROJ_PATH = 'measurement/pcoedge64:image'

    _SCAN_META_PATH = 'scan_meta/technique/scan'

    _DET_META_PATH = 'scan_meta/technique/detector'

    _SCHEME = 'silx'

    def __init__(self, scan, entry=None):
        # if the user give the master file instead of the scan dir...
        if scan is not None:
            if os.path.isfile(scan):
                self.master_file = scan
                scan = os.path.dirname(scan)
            else:
                self.master_file = os.path.join(scan, os.path.basename(scan))
                if os.path.exists(self.master_file + '.hdf5'):
                    self.master_file = self.master_file + '.hdf5'
                else:
                    self.master_file = self.master_file + '.h5'
        else:
            self.master_file = None

        super(HDF5TomoScan, self).__init__(scan=scan, type_=HDF5TomoScan._TYPE)

        self._entry = entry or HDF5TomoScan._DEFAULT_ENTRY
        # for now the default entry is 1_tomo but should change with time

        # data caches
        self._projections = None
        self._tomo_n = None
        # number of projections / radios
        self._dark_n = None
        # number of dark image made during acquisition
        self._ref_n = None
        # number of flat field made during acquisition
        self._ref_on = None
        # when the last flat field is process
        self._scan_range = None
        # scan range, in degree
        self._dim_1, self._dim_2 = None, None
        # image dimensions
        self._pixel_size = None
        # pixel dimensions (tuple)

    @docstring(TomoScanBase.is_tomoscan_dir)
    @staticmethod
    def is_tomoscan_dir(directory, **kwargs):
        master_file_base = os.path.join(directory, os.path.basename(directory))
        if os.path.exists(master_file_base + '.hdf5'):
            return True
        else:
            return os.path.exists(master_file_base + '.h5')

    @docstring(TomoScanBase.is_abort)
    def is_abort(self, **kwargs):
        # for now there is no abort definition in .hdf5
        return False

    @staticmethod
    def from_dict(_dict):
        scan = HDF5TomoScan(scan=None)
        scan.load_from_dict(_dict=_dict)
        return scan

    @docstring(TomoScanBase.load_from_dict)
    def load_from_dict(self, _dict):
        """

        :param _dict:
        :return:
        """
        if isinstance(_dict, io.TextIOWrapper):
            data = json.load(_dict)
        else:
            data = _dict
        if not (self._DICT_TYPE_KEY in data and data[self._DICT_TYPE_KEY] == self._TYPE):
            raise ValueError('Description is not an EDFScan json description')

        assert self._DICT_PATH_KEY in data
        self.path = data[self._DICT_PATH_KEY]
        return self

    @property
    @docstring(TomoScanBase.projections)
    def projections(self):
        if self._projections is None or len(self._projections) != self.tomo_n:
            self.update()
        return self._projections

    @projections.setter
    def projections(self, projections):
        self._projections = projections

    @property
    @docstring(TomoScanBase.darks)
    def darks(self):
        raise NotImplementedError('ref path not defined yet for hdf5')

    @property
    @docstring(TomoScanBase.flats)
    def flats(self):
        raise NotImplementedError('ref path not defined yet for hdf5')

    @docstring(TomoScanBase.update)
    def update(self):
        """update list of radio and reconstruction by parsing the scan folder
        """
        if not os.path.exists(self.master_file):
            return
        self.projections = self._get_projections_url()
        # TODO: update darks and flats too

    @docstring(TomoScanBase.get_proj_angle_url)
    def _get_projections_url(self):
        """

        :param path:
        :return: list of url
        """
        if self.master_file is None or not os.path.exists(self.master_file):
            return
        with h5py.File(self.master_file, 'r') as h5_file:
            urls = {}
            if (self._entry in h5_file and
                    HDF5TomoScan._PROJ_PATH in h5_file[self._entry]):
                image = h5_file[self._entry][HDF5TomoScan._PROJ_PATH]
                def get_reader(extension):
                    extension = extension.lower()
                    if extension == 'edf':
                        return 'fabio'
                    elif extension == 'hdf5':
                        return 'silx'
                    else:
                        mess = ' '.join(('extension', extension,
                                         'unrecognized to define a reader'))
                        _logger.warning(mess)
                        return None

                for i_slice, slice_data in enumerate(image):
                    # if fit hdf5 mock
                    if isinstance(slice_data, numpy.ndarray) and slice_data.ndim == 2:
                        data_path = '/'.join((self._entry, self._PROJ_PATH))
                        silx_url = DataUrl(file_path=self.master_file,
                                           data_path=data_path,
                                           data_slice=(i_slice,),
                                           scheme='silx')
                    else:
                        # if fit the bcu prototype
                        scheme = get_reader(slice_data[1])
                        file_path = slice_data[4]
                        data_path = '/'.join((slice_data[3], 'measurement', 'pcoedge64', 'data'))
                        slice_number = slice_data[2]
                        silx_url = DataUrl(file_path=file_path, data_path=data_path,
                                           data_slice=(slice_number,), scheme=scheme)
                    urls[i_slice] = silx_url
            return urls

    @docstring(TomoScanBase.tomo_n)
    @property
    def tomo_n(self):
        if self._tomo_n is None and self.master_file and os.path.exists(self.master_file):
            with h5py.File(self.master_file) as h5_file:
                self._tomo_n = h5_file[self._entry][self._SCAN_META_PATH]['tomo_n'][()]
        return self._tomo_n

    @docstring(TomoScanBase.dark_n)
    @property
    def dark_n(self):
        if self._dark_n is None and self.master_file and os.path.exists(self.master_file):
            with h5py.File(self.master_file) as h5_file:
                self._dark_n = h5_file[self._entry][self._SCAN_META_PATH]['dark_n'][()]
        return self._dark_n

    @docstring(TomoScanBase.ref_n)
    @property
    def ref_n(self):
        if self._ref_n is None and self.master_file and os.path.exists(self.master_file):
            with h5py.File(self.master_file, 'r') as h5_file:
                self._ref_n = h5_file[self._entry][self._SCAN_META_PATH]['ref_n'][()]
        return self._ref_n

    @docstring(TomoScanBase.ff_interval)
    @property
    def ff_interval(self):
        if self._ref_on is None and self.master_file and os.path.exists(self.master_file):
            with h5py.File(self.master_file, 'r') as h5_file:
                self._ref_on = h5_file[self._entry][self._SCAN_META_PATH]['ref_n'][()]
        return self._ref_on


    @docstring(TomoScanBase.scan_range)
    @property
    def scan_range(self):
        if self._scan_range is None and self.master_file and os.path.exists(self.master_file):
            with h5py.File(self.master_file, 'r') as h5_file:
                self._scan_range = h5_file[self._entry][self._SCAN_META_PATH]['scan_range'][()]
        return self._scan_range

    @property
    def dim_1(self):
        if self._dim_1 is None and self.master_file and os.path.exists(self.master_file):
            with h5py.File(self.master_file, 'r') as h5_file:
                self._dim_1 = h5_file[self._entry][self._DET_META_PATH]['size'][0]
        return self._dim_1

    @property
    def dim_2(self):
        if self._dim_2 is None and self.master_file and os.path.exists(self.master_file):
            with h5py.File(self.master_file, 'r') as h5_file:
                self._dim_2 = h5_file[self._entry][self._DET_META_PATH]['size'][()][1]
        return self._dim_2

    @property
    def pixel_size(self):
        if self._pixel_size is None and self.master_file and os.path.exists(self.master_file):
            with h5py.File(self.master_file) as h5_file:
                self._pixel_size = h5_file[self._entry][self._DET_META_PATH]['pixel_size'][()]
        return self._pixel_size

    @docstring(TomoScanBase.get_proj_angle_url)
    def get_proj_angle_url(self) -> dict:
        can_compute = True
        scan_range = self.scan_range
        if scan_range is None:
            _logger.warning('unable to deduced scan range so unable to'
                            'compute projection angles')
            can_compute = False
        projection_urls = self.projections
        if projection_urls is None or len(projection_urls) == 0:
            _logger.warning('unable to retrieve projection')
            can_compute = False
        tomo_n = self.tomo_n
        if tomo_n is None:
            _logger.warning('unable to find the theoretical number of'
                            'projection')
            can_compute = False

        if can_compute is False:
            return None
        else:
            return TomoScanBase.map_urls_on_scan_range(urls=projection_urls,
                                                       n_projection=tomo_n,
                                                       scan_range=scan_range)
