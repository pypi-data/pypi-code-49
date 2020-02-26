import unittest
from typing import Tuple
from unittest.mock import MagicMock

import pandas as pd
from pandas.util.testing import assert_frame_equal

from features_factory.feature_archetype import FeatureArchetype
from features_factory.input_data_error import InputDataError


class TestBaseFeature(unittest.TestCase):

    class Feature(FeatureArchetype):

        def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
            ie = InputDataError()
            if 'A' not in df.columns:
                ie.add_missing_column('A')
            if 'B' not in df.columns:
                ie.add_missing_column('B')
            return ie

        def get_dependencies(self) -> Tuple:
            return tuple()

        def generate(self, df: pd.DataFrame, **kwargs) -> pd.Series:
            return df['A'] + df['B']

    def test_when_call_insert_into_raise_exception_if_required_columns_are_missing(self):
        example_feature = TestBaseFeature.Feature('example_feature')

        # these should run without raising any exception
        example_feature.insert_into(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}))
        example_feature.insert_into(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}))

        with self.assertRaises(RuntimeError):
            example_feature.insert_into(pd.DataFrame({'A': [1, 2, 3], 'C': [4, 5, 6]}))

        with self.assertRaises(RuntimeError):
            example_feature.insert_into(pd.DataFrame({'D': [1, 2, 3], 'C': [4, 5, 6]}))

        with self.assertRaises(RuntimeError):
            example_feature.insert_into(pd.DataFrame({'B': [1, 2, 3], 'C': [4, 5, 6], 'Z': [7, 8, 9]}))

    def test_insert_into_writes_values_correctly(self):
        example_feature = TestBaseFeature.Feature('example_feature')

        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

        features = example_feature.generate(df)
        df = example_feature.insert_into(df)

        self.assertTrue(all(features == df[example_feature.name()]))
        self.assertTrue(all(df.columns == ['A', 'B', example_feature.name()]))

    def test_insert_into_column_can_overwrite_a_column(self):
        example_feature = TestBaseFeature.Feature('A')

        original_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

        features = example_feature.generate(original_df)
        df = example_feature.insert_into(original_df)

        self.assertTrue(all(df['A'] == features))
        self.assertFalse(all(df['A'] == original_df['A']))

    def test_insert_into_leaves_the_original_df_unchanged(self):
        example_feature = TestBaseFeature.Feature('example_feature')

        original_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        copy_original_df = original_df.copy()
        df = example_feature.insert_into(original_df)

        self.assertTrue(example_feature.name() in df)
        self.assertFalse(example_feature.name() in original_df)
        assert_frame_equal(original_df, copy_original_df)

    def test_verify_dependencies(self):
        # --- mock a feature that depend on two features with the same name
        example_feature = TestBaseFeature.Feature('example_feature')
        dep1 = TestBaseFeature.Feature('dep1')
        dep2 = TestBaseFeature.Feature('dep2')
        dep3 = TestBaseFeature.Feature('dep3')
        example_feature.get_dependencies = MagicMock()
        example_feature.get_dependencies.return_value = (dep1, dep2)
        # --- when verify the _dependencies find the missing _dependencies
        de = example_feature.verify_dependencies((dep1, dep1))
        found_missing_dependencies = de.get_missing_dependency_of_victim(example_feature.name())
        self.assertCountEqual((dep2.name(), ), found_missing_dependencies)

        de = example_feature.verify_dependencies((dep2, ))
        found_missing_dependencies = de.get_missing_dependency_of_victim(example_feature.name())
        self.assertCountEqual((dep1.name(),), found_missing_dependencies)

        de = example_feature.verify_dependencies((dep1, dep2, dep2))
        found_missing_dependencies = de.get_missing_dependency_of_victim(example_feature.name())
        self.assertEqual(0, len(found_missing_dependencies))

        de = example_feature.verify_dependencies((dep3, ))
        found_missing_dependencies = de.get_missing_dependency_of_victim(example_feature.name())
        self.assertCountEqual((dep1.name(), dep2.name()), found_missing_dependencies)
