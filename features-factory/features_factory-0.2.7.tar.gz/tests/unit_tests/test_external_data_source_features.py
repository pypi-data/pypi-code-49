import unittest

import numpy as np
import pandas as pd

from features_factory.external_data_source_features import ValueFromExternalDfFeature, ExternalDfMissesNecessaryColumns
from features_factory.input_features import IntInputFeature


class TestValueFromExternalDfFeature(unittest.TestCase):

    def test_merging_with_external_df_to_obtain_kpi(self):
        feat_a = IntInputFeature(name='feat_a')
        feat_b = IntInputFeature(name='feat_b')
        lbl_kpi = 'kpi'
        external_df = pd.DataFrame({feat_a.name(): [1, 1, 2],
                                    feat_b.name(): [0, 1, 2],
                                    lbl_kpi: ['a', 'b', 'c']})
        kpi = ValueFromExternalDfFeature(name=lbl_kpi, dependencies=[feat_a, feat_b], external_df=external_df,
                                         external_value_column=lbl_kpi)

        df = pd.DataFrame({feat_a.name(): [2, 2, 2, 1, 1, 1], feat_b.name(): [2, 1, 0, 0, 1, 2]})
        df = kpi.insert_into(df=df)

        self.assertIn(lbl_kpi, df.columns)
        self.assertListEqual(df[lbl_kpi].to_list(), ['c', np.nan, np.nan, 'a', 'b', np.nan])

    def test_merging_with_external_df_missing_column_to_merge_on(self):
        feat_a = IntInputFeature(name='feat_a')
        feat_b = IntInputFeature(name='feat_b')
        lbl_kpi = 'kpi'
        external_df = pd.DataFrame({feat_a.name(): [1, 1, 2],
                                    lbl_kpi: ['a', 'b', 'c']})

        with self.assertRaises(ExternalDfMissesNecessaryColumns):
            ValueFromExternalDfFeature(name=lbl_kpi, dependencies=[feat_a, feat_b], external_df=external_df,
                                       external_value_column=lbl_kpi)

    def test_merging_with_external_df_missing_column_to_keep(self):
        feat_a = IntInputFeature(name='feat_a')
        feat_b = IntInputFeature(name='feat_b')
        lbl_kpi = 'kpi'
        external_df = pd.DataFrame({feat_a.name(): [1, 1, 2],
                                    feat_b.name(): [0, 1, 2]})

        with self.assertRaises(ExternalDfMissesNecessaryColumns):
            ValueFromExternalDfFeature(name=lbl_kpi, dependencies=[feat_a, feat_b], external_df=external_df,
                                       external_value_column=lbl_kpi)
