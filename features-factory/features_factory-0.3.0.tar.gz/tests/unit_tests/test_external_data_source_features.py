import unittest

import numpy as np
import pandas as pd

from features_factory.external_data_source_features import ValueFromExternalDfFeature, ExternalDfMissesNecessaryColumns
from features_factory.input_features import IntInputFeature


class TestValueFromExternalDfFeature(unittest.TestCase):

    def setUp(self):
        self.feat_a = IntInputFeature(name='feat_a')
        self.feat_b = IntInputFeature(name='feat_b')
        self.lbl_kpi = 'kpi'
        self.external_df = pd.DataFrame({self.feat_a.name(): [1, 1, 2],
                                         self.feat_b.name(): [0, 1, 2],
                                         self.lbl_kpi: ['a', 'b', 'c']})
        self.kpi = ValueFromExternalDfFeature(name=self.lbl_kpi,
                                              dependencies=[self.feat_a, self.feat_b],
                                              external_df=self.external_df)
        self.df = pd.DataFrame({self.feat_a.name(): [2, 2, 2, 1, 1, 1],
                                self.feat_b.name(): [2, 1, 0, 0, 1, 2]})

    def test_merging_with_external_df_to_obtain_kpi(self):
        df = self.kpi.insert_into(df=self.df)

        self.assertIn(self.lbl_kpi, df.columns)
        self.assertListEqual(df[self.lbl_kpi].to_list(), ['c', np.nan, np.nan, 'a', 'b', np.nan])

    def test_merging_with_external_df_missing_column_to_merge_on(self):
        external_df = self.external_df.drop(columns=[self.feat_b.name()])

        with self.assertRaises(ExternalDfMissesNecessaryColumns) as context:
            ValueFromExternalDfFeature(name=self.lbl_kpi,
                                       dependencies=[self.feat_a, self.feat_b],
                                       external_df=external_df)

        self.assertIn(self.feat_b.name(), str(context.exception))

    def test_merging_with_external_df_missing_column_to_keep(self):
        external_df = self.external_df.drop(columns=[self.kpi.name()])

        with self.assertRaises(ExternalDfMissesNecessaryColumns) as context:
            ValueFromExternalDfFeature(name=self.lbl_kpi,
                                       dependencies=[self.feat_a, self.feat_b],
                                       external_df=external_df)

        self.assertIn(self.lbl_kpi, str(context.exception))

    def test_passing_df_with_already_target_column_returns_a_non_empty_input_error(self):
        self.df[self.lbl_kpi] = [None] * len(self.df)
        ie = self.kpi.verify_input(self.df)

        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())
        self.assertTrue(ie.has_columns_that_would_be_overwritten())
        self.assertIn(self.lbl_kpi, ie.to_string())
