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
__date__ = "10/10/2019"


import os
import re
import fabio
from lxml import etree
import json
import io
from typing import Union
from ..scanbase import TomoScanBase
from .utils import get_parameters_frm_par_or_info, extract_urls_from_edf
from ..unitsystem import metricsystem
from ..utils import docstring
import logging

_logger = logging.getLogger(__name__)


class EDFTomoScan(TomoScanBase):
    """
    TomoScanBase instanciation for scan defined from .edf files

    :param scan: path to the root folder containing the scan.
    :type: Union[str,None]
    :param n_frames: Number of frames in each EDF file.
        If not provided, it will be inferred by reading the files.
        In this case, the frame number is guessed from the file name.
    :type: Union[int, None]=None
    """
    _TYPE = 'edf'

    INFO_EXT = '.info'

    ABORT_FILE = '.abo'

    _REFHST_PREFIX = 'refHST'

    _DARKHST_PREFIX = 'dark.edf'

    _SCHEME = 'fabio'

    def __init__(self, scan: Union[str, None], n_frames: Union[int, None]=None):
        TomoScanBase.__init__(self, scan=scan, type_=self._TYPE)

        # data caches
        self._darks = None
        self._flats = None
        self._projections = None
        self.__tomo_n = None
        self.__ref_n = None
        self.__dark_n = None
        self.__dim1 = None
        self.__dim2 = None
        self.__pixel_size = None
        self.__ref_on = None
        self.__scan_range = None
        self._edf_n_frames = n_frames
        self.update()

    @docstring(TomoScanBase.tomo_n)
    @property
    def tomo_n(self) -> Union[None, int]:
        if self.__tomo_n is None:
            self.__tomo_n = EDFTomoScan.get_tomo_n(scan=self.path)
        return self.__tomo_n

    @property
    @docstring(TomoScanBase.dark_n)
    def dark_n(self) -> Union[None, int]:
        if self.__dark_n is None:
            self.__dark_n = EDFTomoScan.get_dark_n(scan=self.path)
        return self.__dark_n

    @property
    @docstring(TomoScanBase.ref_n)
    def ref_n(self) -> Union[None, int]:
        if self.__ref_n is None:
            self.__ref_n = EDFTomoScan.get_ref_n(scan=self.path)
        return self.__ref_n

    @property
    @docstring(TomoScanBase.pixel_size)
    def pixel_size(self) -> Union[None, int]:
        """

        :return: pixel size
        :rtype: float
        """
        if self.__pixel_size is None:
            self.__pixel_size = EDFTomoScan.get_pixel_size(scan=self.path)
        return self.__pixel_size

    @property
    @docstring(TomoScanBase.dim_1)
    def dim_1(self) -> Union[None, int]:
        """

        :return: image dim1
        :rtype: int
        """
        if self.__dim1 is None:
            self.__dim1, self.__dim2 = EDFTomoScan.get_dim1_dim2(scan=self.path)
        return self.__dim1

    @property
    @docstring(TomoScanBase.dim_2)
    def dim_2(self) -> Union[None, int]:
        """

        :return: image dim2
        :rtype: int
        """
        if self.__dim2 is None:
            self.__dim1, self.__dim2 = EDFTomoScan.get_dim1_dim2(scan=self.path)
        return self.__dim2

    @property
    @docstring(TomoScanBase.ff_interval)
    def ff_interval(self) -> Union[None, int]:
        if self.__ref_on is None:
            self.__ref_on = EDFTomoScan.get_ff_interval(scan=self.path)
        return self.__ref_on

    @property
    @docstring(TomoScanBase.scan_range)
    def scan_range(self) -> Union[None, int]:
        if self.__scan_range is None:
            self.__scan_range = EDFTomoScan.get_scan_range(scan=self.path)
        return self.__scan_range

    @property
    @docstring(TomoScanBase.flats)
    def flats(self) -> Union[None, dict]:
        """
        flats are given as a dictionary with index as key and DataUrl as
        value"""
        if self._flats is None:
            self._flats = self.get_refs_url(scan_path=self.path)
        return self._flats

    @docstring(TomoScanBase.is_tomoscan_dir)
    @staticmethod
    def is_tomoscan_dir(directory: str, **kwargs) -> bool:
        return os.path.isfile(EDFTomoScan.get_info_file(directory=directory,
                                                        kwargs=kwargs))

    @staticmethod
    def get_info_file(directory: str, **kwargs) -> str:
        basename = os.path.basename(directory)
        assert basename != ''
        info_file = os.path.join(directory, basename + EDFTomoScan.INFO_EXT)

        if 'src_pattern' in kwargs and kwargs['srx_pattern'] is not None:
            assert 'dest_pattern' in kwargs
            info_file = info_file.replace(kwargs['src_pattern'],
                                          kwargs['dest_pattern'],
                                          1)
        return info_file

    @docstring(TomoScanBase.is_abort)
    def is_abort(self,  **kwargs) -> bool:
        abort_file = os.path.basename(self.path) + self.ABORT_FILE
        abort_file = os.path.join(self.path, abort_file)
        if 'src_pattern' in kwargs and kwargs['src_pattern' is not None]:
            assert 'dest_pattern' in kwargs
            abort_file = abort_file.replace(kwargs['src_pattern'],
                                            kwargs['dest_pattern'])
        return os.path.isfile(abort_file)

    @property
    @docstring(TomoScanBase.darks)
    def darks(self) -> dict:
        if self._darks is None:
            self._darks = self.get_darks_url(scan_path=self.path)
        return self._darks

    @docstring(TomoScanBase.get_proj_angle_url)
    def get_proj_angle_url(self) -> dict:
        # TODO: we might use fabio.open_serie instead
        if self.path is None:
            _logger.warning('no path specified for scan, unable to retrieve'
                            ' the projections')
            return {}
        n_projection = self.tomo_n
        data_urls = EDFTomoScan.get_proj_urls(self.path)
        return TomoScanBase.map_urls_on_scan_range(urls=data_urls,
                                                   n_projection=n_projection,
                                                   scan_range=self.scan_range)

    @docstring(TomoScanBase.update)
    def update(self):
        self.projections = EDFTomoScan.get_proj_urls(self.path, n_frames=self._edf_n_frames)
        self._darks = EDFTomoScan.get_darks_url(self.path)
        self._flats = EDFTomoScan.get_refs_url(self.path)

    @docstring(TomoScanBase.load_from_dict)
    def load_from_dict(self, desc: Union[dict, io.TextIOWrapper]):
        if isinstance(desc, io.TextIOWrapper):
            data = json.load(desc)
        else:
            data = desc
        if not (self._DICT_TYPE_KEY in data and data[self._DICT_TYPE_KEY] == self._TYPE):
            raise ValueError('Description is not an EDFScan json description')

        assert self._DICT_PATH_KEY in data
        self.path = data[self._DICT_PATH_KEY]
        return self

    @staticmethod
    def get_proj_urls(scan: str, n_frames: Union[int, None]=None) -> dict:
        """
        Return the dict of radios / projection for the given scan.
        Keys of the dictionary is the slice number
        Return all the file on the root of scan starting by the name of scan and
        ending by .edf

        :param scan: is the path to the folder of acquisition
        :type: str
        :param n_frames: Number of frames in each EDF file.
            If not provided, it is inferred by reading each file.
        :type: int
        :return: dict of radios files with radio index as key and file as value
        :rtype: dict
        """
        urls = dict({})
        if(scan is None) or not(os.path.isdir(scan)):
            return urls

        if os.path.isdir(scan):
            for f in os.listdir(scan):
                if EDFTomoScan.is_a_proj_path(fileName=f, scanID=scan):
                    gfile = os.path.join(scan, f)
                    index = EDFTomoScan.guess_index_frm_file_name(gfile)
                    urls.update(extract_urls_from_edf(start_index=index,
                                                       file_=gfile,
                                                       n_frames=n_frames))

        return urls

    @staticmethod
    def is_a_proj_path(fileName: str, scanID: str) -> bool:
        """Return True if the given fileName can fit to a Radio name
        """
        fileBasename = os.path.basename(fileName)
        folderBasename = os.path.basename(scanID)

        if fileBasename.endswith(".edf") and fileBasename.startswith(folderBasename):
            localstring = fileName.rstrip('.edf')
            # remove the scan
            localstring = re.sub(folderBasename, '', localstring)
            if 'slice_' in localstring:
                # case of a reconstructed file
                return False
            if 'refHST' in localstring:
                return False
            s = localstring.split('_')
            if s[-1].isdigit():
                # check that the next value is a digit
                return True

        return False

    @staticmethod
    def guess_index_frm_file_name(_file: str) -> Union[None, int]:
        name = _file.rstrip('.edf')
        ic = []
        while name[-1].isdigit():
            ic.append(name[-1])
            name = name[:-1]

        if len(ic) is 0:
            return None
        else:
            orignalOrder = ic[::-1]
            return int(''.join(orignalOrder))

    @staticmethod
    def get_tomo_n(scan: str) -> Union[None, int]:
        return EDFTomoScan.retrieve_information(scan=os.path.abspath(scan),
                                                ref_file=None,
                                                key='TOMO_N',
                                                type_=int,
                                                key_aliases=['tomo_N', 'Tomo_N'])

    @staticmethod
    def get_dark_n(scan:str) -> Union[None, int]:
        return EDFTomoScan.retrieve_information(scan=os.path.abspath(scan),
                                                ref_file=None,
                                                key='DARK_N',
                                                type_=int,
                                                key_aliases=['dark_N', ])

    @staticmethod
    def get_ref_n(scan :str) -> Union[None, int]:
        return EDFTomoScan.retrieve_information(scan=os.path.abspath(scan),
                                                ref_file=None,
                                                key='REF_N',
                                                type_=int,
                                                key_aliases=['ref_N', ])

    @staticmethod
    def get_ff_interval(scan: str) -> Union[None, int]:
        return EDFTomoScan.retrieve_information(scan=os.path.abspath(scan),
                                                ref_file=None,
                                                key='REF_ON',
                                                type_=int,
                                                key_aliases=['ref_On', ])

    @staticmethod
    def get_scan_range(scan: str) -> Union[None, int]:
        return EDFTomoScan.retrieve_information(scan=os.path.abspath(scan),
                                                ref_file=None,
                                                key='ScanRange',
                                                type_=int,
                                                key_aliases=['scanRange', ])

    @staticmethod
    def get_dim1_dim2(scan: str) -> Union[None, tuple]:
        _info_file = os.path.join(scan, os.path.basename(scan) + '.info')
        d1 = EDFTomoScan.retrieve_information(scan=os.path.abspath(scan),
                                              ref_file=None,
                                              key='Dim_1',
                                              key_aliases=['projectionSize/DIM_1'],
                                              type_=int)
        d2 = EDFTomoScan.retrieve_information(scan=os.path.abspath(scan),
                                              ref_file=None,
                                              key='Dim_2',
                                              key_aliases=['projectionSize/DIM_2'],
                                              type_=int)

        return d1, d2

    @staticmethod
    def get_pixel_size(scan: str) -> Union[None, int]:
        if os.path.isdir(scan) is False:
            return None
        value = EDFTomoScan.retrieve_information(scan=scan,
                                                 ref_file=None,
                                                 key='PixelSize',
                                                 type_=float,
                                                 key_aliases=['pixelSize', ])
        if value is None:
            parFile = os.path.join(scan, os.path.basename(scan) + '.par')
            if os.path.exists(parFile):
                try:
                    ddict = get_parameters_frm_par_or_info(parFile)
                except ValueError as e:
                    _logger.error(e)
                if 'IMAGE_PIXEL_SIZE_1'.lower() in ddict:
                    value = float(ddict['IMAGE_PIXEL_SIZE_1'.lower()])
        # for now pixel size are stored in microns.
        # We want to return them in meter
        if value is not None:
            return value * metricsystem.micrometer
        else:
            return None

    @staticmethod
    def get_darks_url(scan_path: str, prefix: str='dark',
                      file_ext: str='.edf') -> dict:
        """

        :param scan_path:
        :type: str
        :param prefix: ref / flat field file prefix
        :type: str
        :param file_ext: ref / flat field file extension
        :type: str
        :return: list of refs as silx's `DataUrl`
        """
        res = {}
        if os.path.isdir(scan_path) is False:
            _logger.error(scan_path + ' is not a directory. Cannot extract '
                                     'DarkHST files')
            return res
        for file_ in os.listdir(scan_path):
            _prefix = prefix
            if prefix.endswith(file_ext):
                _prefix = prefix.rstrip(file_ext)
            if file_.startswith(_prefix) and file_.endswith(file_ext):
                # usuelly the dark file name should be dark.edf, but some
                # darkHSTXXXX remains...
                file_fp = file_.lstrip(_prefix).rstrip(file_ext).lstrip('HST')
                if file_fp == '' or file_fp.isnumeric() is True:
                    index = EDFTomoScan.guess_index_frm_file_name(file_)
                    urls = extract_urls_from_edf(os.path.join(scan_path, file_),
                                                 start_index=index)
                    res.update(urls)
        return res

    @staticmethod
    def get_refs_url(scan_path: str,  prefix: str='refHST',
                     file_ext: str='.edf') -> dict:
        """

        :param scan_path:
        :type: str
        :param prefix: ref / flat field file prefix
        :type: str
        :param file_ext: ref / flat field file extension
        :type: str
        :return: list of refs as silx's `DataUrl`
        """
        res = {}
        if os.path.isdir(scan_path) is False:
            _logger.error(scan_path + ' is not a directory. Cannot extract '
                                      'RefHST files')
            return res

        for file_ in os.listdir(scan_path):
            if file_.startswith(prefix) and file_.endswith(file_ext):
                index = EDFTomoScan.guess_index_frm_file_name(file_)
                file_fp = os.path.join(scan_path, file_)
                urls = extract_urls_from_edf(start_index=index, file_=file_fp)
                res.update(urls)
        return res

    @staticmethod
    def retrieve_information(scan: str, ref_file: Union[str, None], key: str,
                             type_: type,
                             key_aliases: Union[list, tuple, None] = None):
        """
        Try to retrieve information a .info file, an .xml or a flat field file.

        file.
        Look for the key 'key' or one of it aliases.

        :param scan: root folder of an acquisition. Must be an absolute path
        :param ref_file: the refXXXX_YYYY which should contain information
                         about the scan.
        :param key: the key (information) we are looking for
        :type: str
        :param type_: requestde out type if the information is found
        :type type_: return type if the information is found.
        :param key_aliases: aliases of the key in the different file
        :type: list
        :return: the requested information or None if not found
        """
        info_aliases = [key]
        if key_aliases is not None:
            assert type(key_aliases) in (tuple, list)
            [info_aliases.append(alias) for alias in key_aliases]

        if not os.path.isdir(scan):
            return None

        # 1st look for ref file if any given
        def parseRefFile(filePath):
            header = fabio.open(filePath).header
            for k in key_aliases:
                if k in header:
                    return type_(header[k])
            return None

        if ref_file is not None and os.path.isfile(ref_file):
            try:
                info = parseRefFile(ref_file)
            except IOError as e:
                _logger.warning(e)
            else:
                if info is not None:
                    return info

        # 2nd look for .info file
        def parseInfoFile(filePath):
            def extractInformation(text, alias):
                text = text.replace(alias, '')
                text = text.replace('\n', '')
                text = text.replace(' ', '')
                text = text.replace('=', '')
                return type_(text)

            info = None
            f = open(filePath, "r")
            line = f.readline()
            while line:
                for alias in info_aliases:
                    if alias in line:
                        info = extractInformation(line, alias)
                        break
                line = f.readline()
            f.close()
            return info

        baseName = os.path.basename(scan)
        infoFiles = [os.path.join(scan, baseName + '.info')]
        infoOnDataVisitor = infoFiles[0].replace('lbsram', '')
        # hack to check in lbsram, would need to be removed to add some consistency
        if os.path.isfile(infoOnDataVisitor):
            infoFiles.append(infoOnDataVisitor)
        for infoFile in infoFiles:
            if os.path.isfile(infoFile) is True:
                info = parseInfoFile(infoFile)
                if info is not None:
                    return info

        # 3td look for xml files
        def parseXMLFile(filePath):
            try:
                for alias in info_aliases:
                    tree = etree.parse(filePath)
                    elmt = tree.find("acquisition/" + alias)
                    if elmt is None:
                        continue
                    else:
                        info = type_(elmt.text)
                        if info == -1:
                            return None
                        else:
                            return info
            except etree.XMLSyntaxError as e:
                _logger.warning(e)
                return None

        xmlFiles = [os.path.join(scan, baseName + '.xml')]
        xmlOnDataVisitor = xmlFiles[0].replace('lbsram', '')
        # hack to check in lbsram, would need to be removed to add some consistency
        if os.path.isfile(xmlOnDataVisitor):
            xmlFiles.append(xmlOnDataVisitor)
        for xmlFile in xmlFiles:
            if os.path.isfile(xmlFile) is True:
                info = parseXMLFile(xmlFile)
                if info is not None:
                    return info

        return None
