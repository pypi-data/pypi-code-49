import os
import unittest

from cvplotlib import data_source as ds


class CollectionSourceTests(unittest.TestCase):

    def setUp(self):

        self.data = dict(
            metric1=[[
                [0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1, 0.1, 0.1, 0.1, 0.1],
            ]],
            metric2=[[
                [0.2, 0.2, 0.2, 0.2, 0.2],
                [0.2, 0.2, 0.2, 0.2, 0.2],
                [0.2, 0.2, 0.2, 0.2, 0.2],
                [0.2, 0.2, 0.2, 0.2, 0.2],
                [0.2, 0.2, 0.2, 0.2, 0.2],
            ]],
            metric3=[[
                [0.4, 0.4, 0.4, 0.4, 0.4],
                [0.4, 0.4, 0.4, 0.4, 0.4],
                [0.4, 0.4, 0.4, 0.4, 0.4],
                [0.4, 0.4, 0.4, 0.4, 0.4],
                [0.4, 0.4, 0.4, 0.4, 0.4],
            ]],
        )

    # def tearDown(self):
    #     os.unlink(self.data)

    @unittest.skip
    def test_data_read(self):
        source = ds.CollectionDataSource(self.data)
