import unittest

import pandas as pd

from pandas.testing import assert_frame_equal

from features_factory.composed_features import ComposedFeature
from features_factory.input_features import IntInputFeature, BoolInputFeature
from features_factory.one_component_features import OneComponentFeature
from features_factory.stack import Stack
from features_factory.stack_error import StackError


class TestStack(unittest.TestCase):

    class SumOrDiff(ComposedFeature):
        def __init__(self, name: str, abs1_feat, abs2_feat, bool1_feat):
            super().__init__(name, (abs1_feat, abs2_feat, bool1_feat))
            self.abs1 = abs1_feat
            self.abs2 = abs2_feat
            self.bool1 = bool1_feat

        def generate(self, df: pd.DataFrame, **kwargs) -> pd.Series:
            return df.apply(lambda row: row[self.abs1.name()] + row[self.abs2.name()]
                                        if row[self.bool1.name()]
                                        else row[self.abs1.name()] - row[self.abs2.name()], axis=1)

    def test_accepts_only_features(self):
        feats = Stack()

        with self.assertRaises(RuntimeError):
            # noinspection PyTypeChecker
            feats.add(1)

        with self.assertRaises(RuntimeError):
            # noinspection PyTypeChecker
            feats.add('miao')

        with self.assertRaises(RuntimeError):
            # noinspection PyTypeChecker
            feats.add(pd.DataFrame({'A': [1, 2], 'B': [3, 4]}))

    def test_len(self):
        feats = Stack()
        self.assertEqual(0, len(feats))

    def test_insert(self):
        feats = Stack()
        feats.add(IntInputFeature('int1'))
        feats.add(BoolInputFeature('bool1'))

        self.assertEqual(2, len(feats))

    def test_insert_accepts_duplicate_feature_names(self):
        feats = Stack()
        feats.add(IntInputFeature('int1'))
        feats.add(BoolInputFeature('bool1'))
        feats.add(IntInputFeature('int1'))

        self.assertEqual(3, len(feats))

    def test_remove_using_feature_object(self):
        feats = Stack()
        feats.add(IntInputFeature('int1'))
        bool1 = BoolInputFeature('bool1')
        feats.add(bool1)

        feats.remove(bool1)
        self.assertEqual(1, len(feats))

    def test_clear(self):
        feats = Stack()
        feats.add(IntInputFeature('int1'))
        feats.add(BoolInputFeature('bool1'))

        feats.clear()
        self.assertEqual(0, len(feats))

    def test_get_list_of_feature_names(self):
        feats = Stack()
        feats.add(IntInputFeature('int1'))
        feats.add(BoolInputFeature('bool1'))

        self.assertCountEqual(['int1', 'bool1'], feats.names())

    def test_it_is_possible_to_iterate_through_the_features(self):
        feats = Stack()
        feats.add(IntInputFeature('int1'))
        feats.add(BoolInputFeature('bool1'))

        for feat in feats:
            feat.name()

    def test_it_is_possible_to_init_with_list_of_features(self):
        feats = Stack([IntInputFeature('int1'), BoolInputFeature('bool1'), IntInputFeature('int1')])
        self.assertEqual(3, len(feats))

    def test_can_check_df_for_all_features(self):
        feats = Stack([IntInputFeature('int1'), BoolInputFeature('bool1'), IntInputFeature('int2')])

        # correct df
        df = pd.DataFrame({'int1': [1, 2, 3], 'bool1': [True, False, False], 'int2': [4, 5, 6],
                           'float1': [0, 0.5, 1]})
        feats.verify(df)

        # incorrect df
        df = pd.DataFrame({'int1': [1, 2, 3], 'bool1': [True, False, False], 'int2': [4, 5.1, 6],
                           'float1': [0, 0.5, 1]})
        self.assert_error_is_only_in_input_date(feats.verify(df))

        df = pd.DataFrame({'int1': [1, 2, 3], 'bool1': [True, 2, False], 'int2': [4, 5, 6],
                           'float1': [0, 0.5, 1]})
        self.assert_error_is_only_in_input_date(feats.verify(df))

        df = pd.DataFrame({'int1': [1, 2, 3], 'bool1': [True, False, False], 'int3': [4, 5, 6],
                           'float1': [0, 0.5, 1]})
        self.assert_error_is_only_in_input_date(feats.verify(df))

        df = pd.DataFrame({'int1': [1, 2, 3], 'bool1': [True, False, False], 'int3': [4, 5, 6],
                           'float1': [0, 0.5, 1]})
        self.assert_error_is_only_in_input_date(feats.verify(df))

        df = pd.DataFrame({'int1': [1, None, 3], 'bool1': [True, False, False], 'int3': [4, 5, 6],
                           'float1': [0, 0.5, 1]})
        self.assert_error_is_only_in_input_date(feats.verify(df))

    def assert_error_is_empty(self, bbe: StackError):
        self.assertTrue(bbe.is_empty())

    def assert_error_is_both_in_dependencies_and_input_data(self, bbe):
        self.assertFalse(bbe.is_empty())
        self.assertFalse(bbe.get_input_data_error().is_empty())
        self.assertFalse(bbe.get_dependencies_error().is_empty())

    def assert_error_is_only_in_dependencies(self, bbe: StackError):
        self.assertFalse(bbe.is_empty())
        self.assertTrue(bbe.get_input_data_error().is_empty())
        self.assertFalse(bbe.get_dependencies_error().is_empty())

    def assert_error_is_only_in_input_date(self, bbe: StackError):
        self.assertFalse(bbe.is_empty())
        self.assertFalse(bbe.get_input_data_error().is_empty())
        self.assertTrue(bbe.get_dependencies_error().is_empty())

    def test_can_check_all_features_with_interdependencies(self):
        # --- construction of a collection of interdependent features

        bool1 = BoolInputFeature('bool1')
        int1 = IntInputFeature('int1')
        int2 = IntInputFeature('int2')

        abs1 = OneComponentFeature('abs1', int1, lambda x: abs(x))
        abs2 = OneComponentFeature('abs2', int2, lambda x: abs(x))

        sumdiff = TestStack.SumOrDiff('sum_or_diff', abs1, abs2, bool1)

        # --- first stack of checks, with a df that is always valid

        df = pd.DataFrame({'bool1': [True, True, False],
                           'int1': [1, 2, 3],
                           'int2': [4, 5, 6]})

        feats = Stack([bool1, int1, int2, abs1, abs2, sumdiff])
        self.assert_error_is_empty(feats.verify(df))

        feats = Stack([bool1, int1, int2, abs1, abs2])
        self.assert_error_is_empty(feats.verify(df))

        feats = Stack([bool1, int1, int2, abs2, sumdiff])
        self.assert_error_is_only_in_dependencies(feats.verify(df))

        feats = Stack([int1, int2, abs1, abs2])
        self.assert_error_is_empty(feats.verify(df))

        feats = Stack([int1, int2, abs1, abs2, sumdiff])
        self.assert_error_is_only_in_dependencies(feats.verify(df))

        feats = Stack([bool1, int1, abs1, abs2, sumdiff])
        self.assert_error_is_only_in_dependencies(feats.verify(df))

        feats = Stack([int1])
        self.assert_error_is_empty(feats.verify(df))

        # --- second stack of checks, with a df that is not always valid

        df = pd.DataFrame({'int1': [1, 2, 3]})

        feats = Stack([bool1, int1, int2, abs1, abs2, sumdiff])
        self.assert_error_is_only_in_input_date(feats.verify(df))

        feats = Stack([bool1, int1, int2, abs1, abs2])
        self.assert_error_is_only_in_input_date(feats.verify(df))

        feats = Stack([bool1, int1, int2, abs2, sumdiff])
        self.assert_error_is_both_in_dependencies_and_input_data(feats.verify(df))

        feats = Stack([int1, int2, abs1, abs2])
        self.assert_error_is_only_in_input_date(feats.verify(df))

        feats = Stack([int1, int2, abs1, abs2, sumdiff])
        self.assert_error_is_both_in_dependencies_and_input_data(feats.verify(df))

        feats = Stack([bool1, int1, abs1, abs2, sumdiff])
        self.assert_error_is_both_in_dependencies_and_input_data(feats.verify(df))

        feats = Stack([int1])
        self.assert_error_is_empty(feats.verify(df))

    def test_insert_into_compute_the_features_correctly(self):
        # --- construction of a collection of interdependent features

        bool1 = BoolInputFeature('bool1')
        int1 = IntInputFeature('int1')
        int2 = IntInputFeature('int2')

        abs1 = OneComponentFeature('abs1', int1, lambda x: abs(x))
        abs2 = OneComponentFeature('abs2', int2, lambda x: abs(x))

        sumdiff = TestStack.SumOrDiff('sum_or_diff', abs1, abs2, bool1)

        # --- dataset

        df = pd.DataFrame({'bool1': [True, True, False],
                           'int1': [1, -2, 3],
                           'int2': [-4, 5, -6]})

        # --- check insert_into
        feats = Stack([bool1, int1, int2, abs1, abs2, sumdiff])
        df = feats.insert_into(df)
        self.assertEqual([True, True, False], df[bool1.name()].tolist())
        self.assertEqual([1, -2, 3], df[int1.name()].tolist())
        self.assertEqual([-4, 5, -6], df[int2.name()].tolist())
        self.assertEqual([1, 2, 3], df[abs1.name()].tolist())
        self.assertEqual([4, 5, 6], df[abs2.name()].tolist())
        self.assertEqual([5, 7, -3], df[sumdiff.name()].tolist())

        # --- check insert_into, changing the order
        feats = Stack([sumdiff, bool1, int2, abs2, abs1, int1])
        df = feats.insert_into(df)
        self.assertEqual([True, True, False], df[bool1.name()].tolist())
        self.assertEqual([1, -2, 3], df[int1.name()].tolist())
        self.assertEqual([-4, 5, -6], df[int2.name()].tolist())
        self.assertEqual([1, 2, 3], df[abs1.name()].tolist())
        self.assertEqual([4, 5, 6], df[abs2.name()].tolist())
        self.assertEqual([5, 7, -3], df[sumdiff.name()].tolist())

    def test_filter_out_subgroups_with_insufficient_data(self):
        # --- construction of a collection of interdependent features
        bool1 = BoolInputFeature('bool1')
        int1 = IntInputFeature('int1')
        int2 = IntInputFeature('int2')

        abs1 = OneComponentFeature('abs1', int1, lambda x: abs(x))
        abs2 = OneComponentFeature('abs2', int2, lambda x: abs(x))

        sumdiff = TestStack.SumOrDiff('sum_or_diff', abs1, abs2, bool1)

        # --- dataset

        df = pd.DataFrame({'bool1': [True, True, True, True, True, True, True, False, False, False],
                           'int1': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3],
                           'int2': [0, 0, 0, 1, 1, 1, 2, 2, 2, 3]})

        # --- check filter
        feats = Stack([bool1, int1, int2])

        df, valid_keys, dropped_keys = feats.filter_out_input_subgroups_smaller_than_n(df, 2)

        expected_df = pd.DataFrame({'bool1': [True, True, True, True, True],
                                    'int1': [1, 1, 1, 2, 2],
                                    'int2': [0, 0, 0, 1, 1]}, index=[0, 1, 2, 4, 5])

        assert_frame_equal(expected_df, df)

        expected_valid_keys = ((True, 1, 0), (True, 2, 1))
        self.assertCountEqual(expected_valid_keys, valid_keys)

        expected_invalid_keys = ((True, 1, 1), (True, 2, 2), (False, 2, 2), (False, 3, 2), (False, 3, 3))
        self.assertCountEqual(expected_invalid_keys, dropped_keys)

    def test_filter_out_subgroups_with_insufficient_data_raise_exception_if_columns_are_missing(self):
        # --- construction of a collection of interdependent features
        bool1 = BoolInputFeature('bool1')
        int1 = IntInputFeature('int1')
        int2 = IntInputFeature('int2')

        abs1 = OneComponentFeature('abs1', int1, lambda x: abs(x))
        abs2 = OneComponentFeature('abs2', int2, lambda x: abs(x))

        sumdiff = TestStack.SumOrDiff('sum_or_diff', abs1, abs2, bool1)

        # --- dataset

        df = pd.DataFrame({'bool1': [True, True, True, True, True, True, True, False, False, False],
                           'int1': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3],
                           'int2': [0, 0, 0, 1, 1, 1, 2, 2, 2, 3]})

        # --- check filter
        feats = Stack([bool1, int1, int2, abs1, abs2, sumdiff])

        with self.assertRaises(RuntimeError):
            feats.filter_out_input_subgroups_smaller_than_n(df, 2)

    def test_add(self):
        bool1 = BoolInputFeature('bool1')
        int1 = IntInputFeature('int1')
        int2 = IntInputFeature('int2')

        feats1 = Stack([bool1, int1, int2])

        abs1 = OneComponentFeature('abs1', int1, lambda x: abs(x))
        abs2 = OneComponentFeature('abs2', int2, lambda x: abs(x))

        feats2 = Stack([abs1, abs2])

        feats_sum = feats1 + feats2

        self.assertCountEqual([bool1.name(), int1.name(), int2.name(),
                               abs1.name(), abs2.name()],
                              feats_sum.names())

    def test_add_features_with_dependencies_does_not_create_problems(self):
        int1 = IntInputFeature('int1')
        abs1 = OneComponentFeature('abs1', int1, lambda x: abs(x))

        feats1 = Stack()
        feats1.add(int1)
        feats1.add(abs1)

        self.assertCountEqual([int1, abs1], feats1)

    def test_with_dependencies(self):
        int1 = IntInputFeature('int1')
        abs1 = OneComponentFeature('abs1', int1, lambda x: abs(x))
        stack = Stack([abs1])

        self.assertCountEqual([abs1], stack)
        self.assertCountEqual([int1, abs1], stack.with_dependencies())

    def test_subscript_access(self):
        int1 = IntInputFeature('int1')
        int2 = IntInputFeature('int2')
        stack = Stack([int1, int2])

        self.assertEqual(int1, stack[0])
        self.assertEqual(int2, stack[1])

        self.assertNotEqual(int2, stack[0])
        self.assertNotEqual(int1, stack[1])

    def test_with_input_features_only(self):
        int1 = IntInputFeature('int1')
        abs1 = OneComponentFeature('abs1', int1, lambda x: abs(x))
        stack = Stack([int1, abs1])

        self.assertCountEqual([int1], stack.with_input_features_only())
