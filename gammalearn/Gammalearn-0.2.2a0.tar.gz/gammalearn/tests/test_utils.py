import unittest
import h5py
import pkg_resources

import torch
import numpy as np

import gammalearn.utils as utils


class MockLappDataset(object):

    def __init__(self, camera_type, group_by):

        self.camera_type = camera_type
        self.group_by = group_by
        f = h5py.File(pkg_resources.resource_filename(__name__, 'tests/lapp_cleaning.h5'), 'r')
        self.images = f['images']

    def __len__(self):
        return len(self.images)


# def check_list_equality(l1, l2):
#     return l1==l2


class TestFilters(unittest.TestCase):

    def setUp(self):

        self.dset = MockLappDataset('LSTCAM', 'image')
        self.indices_cleaned = [0, 2]

    def test_cleaning_filter(self):
        assert np.array_equal(utils.cleaning_filter(self.dset), self.indices_cleaned)
        # assert check_list_equality(utils.cleaning_filter(self.dset), self.indices_cleaned)
        assert np.sum(self.dset.images[1]) == 0


if __name__ == '__main__':
    unittest.main()
