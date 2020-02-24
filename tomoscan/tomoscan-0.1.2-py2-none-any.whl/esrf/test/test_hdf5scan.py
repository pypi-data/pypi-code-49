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
"""Unit test for the scan defined at the hdf5 format"""

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "16/09/2019"

import unittest
import shutil
import os
import tempfile
from tomoscan.test.utils import UtilsTest
from tomoscan.esrf.hdf5scan import HDF5TomoScan
import numpy


class HDF5TestBaseClass(unittest.TestCase):
    """base class for hdf5 unit test"""
    def get_dataset(self, hdf5_dataset_name):
        dataset_file = os.path.join(self.test_dir, hdf5_dataset_name)
        o_dataset_file = UtilsTest.getH5Dataset(folderID=hdf5_dataset_name)
        shutil.copy(src=o_dataset_file, dst=dataset_file)
        return dataset_file

    def setUp(self) -> None:
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.test_dir)


class TestHDF5Scan(HDF5TestBaseClass):
    """Basic test for the hdf5 scan"""
    def setUp(self) -> None:
        super(TestHDF5Scan, self).setUp()
        self.dataset_file = self.get_dataset('data_test2.h5')
        self.scan = HDF5TomoScan(self.dataset_file)

    def testGeneral(self):
        """some general on the HDF5Scan """
        self.assertEqual(self.scan.master_file, self.dataset_file)
        self.assertEqual(self.scan.path, os.path.dirname(self.dataset_file))
        self.assertEqual(self.scan.type, 'hdf5')
        _dict = self.scan.to_dict()
        scan2 = HDF5TomoScan.from_dict(_dict)
        self.assertEqual(scan2.path, self.scan.path)
        radios_urls = self.scan.get_proj_angle_url()
        self.assertEqual(len(radios_urls), 100)
        url_1 = radios_urls[0]
        self.assertTrue(url_1.is_valid())
        self.assertFalse(url_1.is_absolute())
        self.assertEquals(url_1.scheme(), 'silx')

    def testProjections(self):
        projections = self.scan.projections
        self.assertEqual(len(projections), 100)
        proj_1 = projections[0]
        self.assertEqual(proj_1.file_path(),
                         '../../../../../../users/opid19/W:/clemence/visualtomo/data_test2/tomo0001/tomo_0000.h5')
        self.assertEqual(proj_1.data_slice(), ('0',))
        self.assertTrue(100 not in projections)

    @unittest.skip('no valid hdf5 acquisition defined yet')
    def testDark(self):
        n_dark = 20
        self.assertEqual(self.scan.dark_n, n_dark)
        with self.assertRaises(NotImplementedError):
            self.scan.darks

    def testFlats(self):
        with self.assertRaises(NotImplementedError):
            flats = self.scan.flats
        n_ref = 21
        self.assertEqual(self.scan.ref_n, n_ref)

        # for now not implemented
        # not implemented at the moment
        data = numpy.arange(2048*2048)
        data.reshape(2048, 2048)
        # not implemented at the moment
        self.assertEqual(self.scan.ff_interval, 21)

    def testAxisUtils(self):
        self.assertEqual(self.scan.scan_range, 360)
        self.assertEqual(self.scan.tomo_n, 100)
        # self.assertEqual(self.scan.dim_1, 2048)
        # self.assertEqual(self.scan.dim_2, 2048)

        proj0_file_path = '../../../../../../users/opid19/W:/clemence/visualtomo/data_test2/tomo0001/tomo_0000.h5'
        radios_urls_evolution = self.scan.get_proj_angle_url()
        self.assertEquals(len(radios_urls_evolution), 100)
        self.assertEquals(radios_urls_evolution[0].file_path(), proj0_file_path)
        self.assertEquals(radios_urls_evolution[0].data_slice(), ('0',))
        self.assertEquals(radios_urls_evolution[0].data_path(), '/entry_0000/measurement/pcoedge64/data')

    def testDarkRefUtils(self):
        self.assertEqual(self.scan.tomo_n, 100)
        self.assertEqual(self.scan.pixel_size[1], 6.5)


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestHDF5Scan, ):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
