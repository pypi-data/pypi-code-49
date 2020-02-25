import numpy as np
import unittest

import pandas as pd

from features_factory.input_features import FloatInputFeature
from features_factory.multicomponent_features import MultiComponentFeature


class TestMultiComponentFeature(unittest.TestCase):

    def setUp(self):
        self.a = FloatInputFeature('a')
        self.b = FloatInputFeature('b')
        self.c = FloatInputFeature('c')
        self.d = FloatInputFeature('d')
        self.e = FloatInputFeature('e')

        self.sum_abcde = MultiComponentFeature('sum', [self.a, self.b, self.c, self.d, self.e], lambda r: np.sum(r))

    def test_get_dependencies(self):
        self.assertCountEqual([self.a, self.b, self.c, self.d, self.e], self.sum_abcde.get_dependencies())

    def test_verify_input_when_df_is_ok(self):
        df = pd.DataFrame({self.a.name(): [1., 2.], self.b.name(): [0., 0.], self.c.name(): [0.5, 0.5],
                           self.d.name(): [3., 2.], self.e.name(): [-1., -1.]})
        ie = self.sum_abcde.verify_input(df)
        self.assertTrue(ie.is_empty())

    def test_verify_input_when_df_misses_one_column(self):
        df = pd.DataFrame({self.a.name(): [1., 2.], self.c.name(): [0.5, 0.5],
                           self.d.name(): [3., 2.], self.e.name(): [-1., -1.]})
        ie = self.sum_abcde.verify_input(df)
        self.assertFalse(ie.is_empty())
        self.assertTrue(ie.has_missing_columns())

    def test_insert(self):
        df = pd.DataFrame({self.a.name(): [1., 2.], self.b.name(): [0., 0.], self.c.name(): [0.5, 0.5],
                           self.d.name(): [3., 2.], self.e.name(): [-1., -1.]})

        df = self.sum_abcde.insert_into(df)

        self.assertCountEqual([3.5, 3.5], df[self.sum_abcde.name()].values)
