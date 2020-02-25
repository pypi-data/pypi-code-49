import os
import unittest

import pandas as pd

from features_factory.input_features import StringInputFeature, DateInputFeature


class Test(unittest.TestCase):

    def test(self):
        path_to_shpm = os.path.join(os.path.dirname(__file__), 'data-sample.csv')
        df = pd.read_csv(path_to_shpm, nrows=1)
        col_names_found = set(df.columns.values)
        col_names_min = {'A', 'B', 'C', 'D',
                         'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'L'}
        col_diff = col_names_min.difference(col_names_found)
        self.assertEqual(0, len(col_diff))

        type_dict = {'A': 'int', 'B': 'int',
                     'C': 'int', 'D': 'int',
                     'L': 'str'}
        df2 = pd.read_csv(path_to_shpm, dtype=type_dict)
        df2['m'] = pd.to_datetime(df2['M'], format='%Y%m%d') \
            .apply(lambda x: x.date())

        # input features that I want to verify
        text = StringInputFeature('L', allow_nan=True)
        date = DateInputFeature('m', allow_nan=True)

        # verification should not return errors
        ie = text.verify_input(df2)
        self.assertTrue(ie.is_empty())

        ie = date.verify_input(df2)
        self.assertTrue(ie.is_empty())
