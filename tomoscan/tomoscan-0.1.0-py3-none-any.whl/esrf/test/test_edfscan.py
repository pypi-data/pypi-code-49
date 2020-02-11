# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
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
# ###########################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "24/01/2017"

import unittest
import logging
import tempfile
import numpy
import fabio.edfimage
from tomoscan.test.utils import UtilsTest
from tomoscan.esrf.mock import MockEDF
from tomoscan.esrf.edfscan import EDFTomoScan
from tomoscan.scanbase import TomoScanBase
from tomoscan.scanfactory import ScanFactory
import collections
import json
import shutil
import os
import silx.io.utils

logging.disable(logging.INFO)


class TestTomoBaseHashable(unittest.TestCase):
    """Make sure EDFTomoScan is hashable"""
    def setUp(self):
        self._folder = tempfile.mkdtemp()
        MockEDF.fastMockAcquisition(self._folder, n_radio=100)

    def tearDown(self):
        shutil.rmtree(self._folder)

    def test_is_hashable(self):
        tomo_base = TomoScanBase(scan=self._folder, type_='toto')
        self.assertTrue(isinstance(tomo_base, collections.Hashable))
        tomo_scan = EDFTomoScan(self._folder)
        self.assertTrue(isinstance(tomo_scan, collections.Hashable))


class TestScanFactory(unittest.TestCase):
    """Make sure the Scan factory is correctly working. Able to detect the valid
    scan type for a given file / directory
    """
    def test_no_scan(self):
        scan_dir = tempfile.mkdtemp()
        with self.assertRaises(ValueError):
            ScanFactory.create_scan_object(scan_dir)

    def test_scan_edf(self):
        scan_dir = UtilsTest.getDataset('test10')
        scan = ScanFactory.create_scan_object(scan_dir)
        self.assertTrue(isinstance(scan, EDFTomoScan))


class TestDarksFlats(unittest.TestCase):
    """unit test for the FTSerieReconstruction functions"""
    def setUp(self):
        def saveData(data, _file, folder):
            file_desc = fabio.edfimage.EdfImage(data=data)
            file_desc.write(os.path.join(folder, _file))

        unittest.TestCase.setUp(self)
        self.folderTwoFlats = tempfile.mkdtemp()
        self.folderOneFlat = tempfile.mkdtemp()

        self.darkData = numpy.arange(100).reshape(10, 10)
        self.flatField_0 = numpy.arange(start=10, stop=110).reshape(10, 10)
        self.flatField_600 = numpy.arange(start=-10, stop=90).reshape(10, 10)
        self.flatField = numpy.arange(start=0, stop=100).reshape(10, 10)

        # save configuration one
        saveData(self.darkData, 'darkHST.edf', self.folderTwoFlats)
        saveData(self.flatField_0, 'refHST_0000.edf', self.folderTwoFlats)
        saveData(self.flatField_600, 'refHST_0600.edf', self.folderTwoFlats)

        # save configuration two
        saveData(self.darkData, 'dark.edf', self.folderOneFlat)
        saveData(self.flatField, 'refHST.edf', self.folderOneFlat)

        self.acquiOneFlat = EDFTomoScan(self.folderOneFlat)
        self.acquiTwoFlats = EDFTomoScan(self.folderTwoFlats)

    def tearDown(self):
        for f in (self.folderOneFlat, self.folderTwoFlats):
            shutil.rmtree(f)
        unittest.TestCase.tearDown(self)

    def testDarks(self):
        self.assertTrue(isinstance(self.acquiOneFlat.darks, dict))
        self.assertEqual(len(self.acquiOneFlat.darks), 1)
        self.assertTrue(isinstance(self.acquiTwoFlats.darks, dict))
        self.assertEqual(len(self.acquiTwoFlats.darks), 1)

        self.assertTrue(
            numpy.array_equal(silx.io.utils.get_data(self.acquiOneFlat.darks[0]),
                              self.darkData)
        )
        self.assertTrue(
            numpy.array_equal(silx.io.utils.get_data(self.acquiTwoFlats.darks[0]),
                                                     self.darkData)
        )

    def testFlats(self):
        # check one flat file with two ref
        self.assertEqual(len(self.acquiOneFlat.flats), 1)
        self.assertTrue(isinstance(self.acquiOneFlat.flats[0], silx.io.url.DataUrl))

        data = silx.io.utils.get_data(self.acquiOneFlat.flats[0])
        numpy.array_equal(data, self.flatField)

        # check two flat files
        self.assertTrue(
            numpy.array_equal(silx.io.utils.get_data(self.acquiTwoFlats.flats[600]),
                              self.flatField_600)
        )
        self.assertTrue(
            numpy.array_equal(silx.io.utils.get_data(self.acquiTwoFlats.flats[0]),
                              self.flatField_0)
        )
        self.assertTrue(12 not in self.acquiTwoFlats.flats)


class TestProjections(unittest.TestCase):
    """Test that the """
    def setUp(self) -> None:
        self.folder = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    def testProjectionNoExtra(self):
        mock = MockEDF(scan_path=self.folder, n_radio=10, n_extra_radio=0)
        mock.end_acquisition()
        scan = EDFTomoScan(scan=self.folder)
        self.assertEqual(len(scan.projections), 10)

    def testProjectionUpdate(self):
        mock = MockEDF(scan_path=self.folder, n_radio=10, n_ini_radio=3)
        scan = EDFTomoScan(scan=self.folder)
        self.assertEqual(len(scan.projections), 3)
        mock.add_radio()
        self.assertEqual(len(scan.projections), 3)
        scan.update()
        self.assertEqual(len(scan.projections), 4)
        self.assertTrue(isinstance(scan.projections[0], silx.io.url.DataUrl))

    def testProjectionWithExtraRadio(self):
        mock = MockEDF(scan_path=self.folder, n_radio=11, n_extra_radio=2,
                       scan_range=180)
        mock.end_acquisition()
        scan = EDFTomoScan(scan=self.folder)
        self.assertEqual(len(scan.projections), 11+2)
        proj_angle_dict = scan.get_proj_angle_url()
        self.assertEqual(len(proj_angle_dict), 11+2)
        self.assertTrue(90 in proj_angle_dict)
        self.assertTrue(180 in proj_angle_dict)
        self.assertTrue('90(1)' in proj_angle_dict)
        self.assertTrue('0(1)' in proj_angle_dict)
        self.assertTrue(360 not in proj_angle_dict)


class TestScanValidatorFindFiles(unittest.TestCase):
    """Function testing the getReconstructionsPaths function is correctly
    functioning"""

    DIM_MOCK_SCAN = 10

    N_RADIO = 20
    N_RECONS = 10
    N_PAG_RECONS = 5

    def setUp(self):
        # create scan folder
        self.path = tempfile.mkdtemp()
        MockEDF.mockScan(scanID=self.path,
                         nRadio=self.N_RADIO,
                         nRecons=self.N_RECONS,
                         nPagRecons=self.N_PAG_RECONS,
                         dim=self.DIM_MOCK_SCAN)
        basename = os.path.basename(self.path)

        # add some random files
        for _file in ('45gfdgfg1.edf', '465slicetest1.edf', 'slice_ab.edf'):
            with open(os.path.join(self.path, basename + _file), "w+") as ofile:
                ofile.write('test')

    def tearDown(self):
        if os.path.isdir(self.path):
            shutil.rmtree(self.path)

    def testGetRadioPaths(self):
        nFound = len(EDFTomoScan.get_proj_urls(self.path))
        self.assertTrue(nFound == self.N_RADIO)


class TestRadioPath(unittest.TestCase):
    """Test static method getRadioPaths for EDFTomoScan"""
    def test(self):
        files = [
          'essai1_0008.edf',
          'essai1_0019.edf',
          'essai1_0030.edf',
          'essai1_0041.edf',
          'essai1_0052.edf',
          'essai1_0063.edf',
          'essai1_0074.edf',
          'essai1_0085.edf',
          'essai1_0096.edf',
          'essai1_.par',
          'refHST0100.edf',
          'darkend0000.edf',
          'essai1_0009.edf',
          'essai1_0020.edf',
          'essai1_0031.edf',
          'essai1_0042.edf',
          'essai1_0053.edf',
          'essai1_0064.edf',
          'essai1_0075.edf',
          'essai1_0086.edf',
          'essai1_0097.edf',
          'essai1_.rec',
          'essai1_0000.edf',
          'essai1_0010.edf',
          'essai1_0021.edf',
          'essai1_0032.edf',
          'essai1_0043.edf',
          'essai1_0054.edf',
          'essai1_0065.edf',
          'essai1_0076.edf',
          'essai1_0087.edf',
          'essai1_0098.edf',
          'essai1_slice_1023.edf',
          'essai1_0001.edf',
          'essai1_0011.edf',
          'essai1_0022.edf',
          'essai1_0033.edf',
          'essai1_0044.edf',
          'essai1_0055.edf',
          'essai1_0066.edf',
          'essai1_0077.edf',
          'essai1_0088.edf',
          'essai1_0099.edf',
          'essai1_slice.info',
          'essai1_0001.par',
          'essai1_0012.edf',
          'essai1_0023.edf',
          'essai1_0034.edf',
          'essai1_0045.edf',
          'essai1_0056.edf',
          'essai1_0067.edf',
          'essai1_0078.edf',
          'essai1_0089.edf',
          'essai1_0100.edf',
          'essai1_slice.par',
          'essai1_0002.edf',
          'essai1_0013.edf',
          'essai1_0024.edf',
          'essai1_0035.edf',
          'essai1_0046.edf',
          'essai1_0057.edf',
          'essai1_0068.edf',
          'essai1_0079.edf',
          'essai1_0090.edf',
          'essai1_0101.edf',
          'essai1_slice.xml',
          'essai1_0003.edf',
          'essai1_0014.edf',
          'essai1_0025.edf',
          'essai1_0036.edf',
          'essai1_0047.edf',
          'essai1_0058.edf',
          'essai1_0069.edf',
          'essai1_0080.edf',
          'essai1_0091.edf',
          'essai1_0102.edf',
          'essai1_.xml',
          'essai1_0004.edf',
          'essai1_0015.edf',
          'essai1_0026.edf',
          'essai1_0037.edf',
          'essai1_0048.edf',
          'essai1_0059.edf',
          'essai1_0070.edf',
          'essai1_0081.edf',
          'essai1_0092.edf',
          'essai1_0103.edf',
          'histogram_essai1_slice',
          'essai1_0005.edf',
          'essai1_0016.edf',
          'essai1_0027.edf',
          'essai1_0038.edf',
          'essai1_0049.edf',
          'essai1_0060.edf',
          'essai1_0071.edf',
          'essai1_0082.edf',
          'essai1_0093.edf',
          'essai1_0104.edf',
          'machinefile',
          'essai1_0006.edf',
          'essai1_0017.edf',
          'essai1_0028.edf',
          'essai1_0039.edf',
          'essai1_0050.edf',
          'essai1_0061.edf',
          'essai1_0072.edf',
          'essai1_0083.edf',
          'essai1_0094.edf',
          'essai1_.cfg',
          'pyhst_out.txt',
          'essai1_0007.edf',
          'essai1_0018.edf',
          'essai1_0029.edf',
          'essai1_0040.edf',
          'essai1_0051.edf',
          'essai1_0062.edf',
          'essai1_0073.edf',
          'essai1_0084.edf',
          'essai1_0095.edf'
          ]

        nbRadio = 0
        for f in files:
            nbRadio += EDFTomoScan.is_a_proj_path(f, 'essai1_')
        self.assertTrue(nbRadio == 105)


class TestScanBaseJSON(unittest.TestCase):
    """Test save / load to / for, json files"""
    def setUp(self):
        self.scan_folder = tempfile.mkdtemp()
        self.json_folder = tempfile.mkdtemp()

    def tearDown(self):
        for folder in (self.scan_folder, self.json_folder):
            shutil.rmtree(folder)

    def testEmptyJson(self):
        """Test behavior if we try to load from empty json stream"""
        _file = os.path.join(self.json_folder, 'json_file.json')
        with open(_file, 'w') as outfile:
            json.dump({}, outfile)

        with open(_file, 'r') as outfile:
            with self.assertRaises(ValueError):
                ScanFactory.create_from_json(outfile)

        scan_to_update = EDFTomoScan(scan=None)
        with open(_file, 'r') as outfile:
            with self.assertRaises(ValueError):
                scan_to_update.load_from_dict(outfile)


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestScanFactory, TestDarksFlats,
               TestScanValidatorFindFiles, TestRadioPath, TestProjections,
               TestTomoBaseHashable):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
