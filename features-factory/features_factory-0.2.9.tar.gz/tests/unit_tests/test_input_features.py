import unittest
from datetime import datetime

import numpy as np
import pandas as pd

from features_factory import input_data_error
from features_factory.input_features import InputFeature, ProvidedInputFeatureWithControlOnNaN, BoolInputFeature, \
    IntInputFeature, FloatInputFeature, DateTimeInputFeature, StringInputFeature, CountryCodeInputFeature, \
    DateInputFeature, StringTimestampInputFeature


class TestInputFeature(unittest.TestCase):

    def test_is_input(self):
        self.assertTrue(InputFeature('bubble').is_input())

    def test_get_name(self):
        name = 'bubble'
        feat = InputFeature(name)
        self.assertEqual(name, feat.name())

    def test_verify_input(self):
        feat = InputFeature('bubble')

        df = pd.DataFrame({'bone': [1, 2, 3], 'rock': [4, 5, 6]})
        ie = feat.verify_input(df)
        self.assertFalse(ie.is_empty())
        self.assertTrue(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())

        df = pd.DataFrame({'bone': [1, 2, 3], feat.name(): [4, 5, 6]})
        ie = feat.verify_input(df)
        self.assertTrue(ie.is_empty())
        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())

    def test_get_dependencies_return_an_empty_tuple(self):
        feat = InputFeature('bubble')
        self.assertIsInstance(feat.get_dependencies(), tuple)
        self.assertEqual(0, len(feat.get_dependencies()))

    def test_generate_leaves_column_as_it_is(self):
        feat = InputFeature('bubble')

        bubbles = [1, 2, 3]
        df = pd.DataFrame({feat.name(): bubbles, 'rock': [4, 5, 6]})
        features = feat.generate(df)

        self.assertEqual(bubbles, features.tolist())


class TestInputFeatureWithControlOnNaN(unittest.TestCase):

    def test_if_there_is_a_nan_then_verify_input_returns_false(self):
        feat = ProvidedInputFeatureWithControlOnNaN('bubble')

        df = pd.DataFrame({feat.name(): [1, 2, np.nan], 'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertFalse(ie.is_empty())
        self.assertFalse(ie.has_missing_columns())
        self.assertTrue(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())

        df = pd.DataFrame({feat.name(): [1, 2, None], 'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertFalse(ie.is_empty())
        self.assertFalse(ie.has_missing_columns())
        self.assertTrue(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())

    def test_if_there_is_a_nan_but_nan_are_allowed_then_verify_input_returns_true(self):
        feat = ProvidedInputFeatureWithControlOnNaN('bubble', allow_nan=True)

        df = pd.DataFrame({feat.name(): [1, 2, np.nan], 'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertTrue(ie.is_empty())
        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())

        df = pd.DataFrame({feat.name(): [1, 2, None], 'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertTrue(ie.is_empty())
        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())

    def test_if_there_is_no_nan_then_verify_input_returns_true(self):
        feat = ProvidedInputFeatureWithControlOnNaN('bubble')

        df = pd.DataFrame({feat.name(): [1, 2, 37], 'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertTrue(ie.is_empty())
        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())


class TestSimpleTypeFeature(unittest.TestCase):

    def assert_only_format_is_wrong(self, ie: input_data_error):
        self.assertFalse(ie.is_empty())
        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertTrue(ie.has_columns_with_wrong_format())

    def assert_there_is_no_error(self, ie: input_data_error):
        self.assertTrue(ie.is_empty())
        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())

    def test_bool_type(self):
        feat = BoolInputFeature('bool_flag')

        df = pd.DataFrame({feat.name(): [True, True, False], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [True, 16.7, False], 'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_bool_type_with_nan_allowed(self):
        feat = BoolInputFeature('bool_flag', allow_nan=True)

        df = pd.DataFrame({feat.name(): [True, np.nan, False], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

    def test_int_type(self):
        feat = IntInputFeature('int_number')

        df = pd.DataFrame({feat.name(): [1, 2, 3], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [int(1), 2.5, int(3)], 'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_float_type(self):
        feat = FloatInputFeature('float_number')

        df = pd.DataFrame({feat.name(): [1.3, 2.5, 3.7], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [int(1), int(2), 3.2], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

    def test_datetime_type(self):
        feat = DateTimeInputFeature('datetime')

        df = pd.DataFrame({feat.name(): [datetime(2018, 1, 1), datetime(2018, 1, 2), datetime(2018, 1, 3)],
                           'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [datetime(2018, 1, 1), '2018-01-02', datetime(2018, 1, 3)],
                           'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [datetime(2018, 1, 1), 'bubble', datetime(2018, 1, 3)],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_date_type(self):
        feat = DateInputFeature('date')

        df = pd.DataFrame({feat.name(): [datetime(2018, 1, 1).date(),
                                         datetime(2018, 1, 2).date(),
                                         datetime(2018, 1, 3).date()],
                           'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [datetime(2018, 1, 1).date(),
                                         datetime(2018, 1, 2),
                                         datetime(2018, 1, 3).date()],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [datetime(2018, 1, 1).date(),
                                         '2018-01-02',
                                         datetime(2018, 1, 3).date()],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['2018-01-01',
                                         '2018-01-02',
                                         '2018-01-03'],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_allow_nan_is_compatible_with_type_check_for_date(self):
        """
        when allow_nan=True, NaN values should be accepted and not reported as wrong_format
        :return:
        """
        feat = DateInputFeature('date', allow_nan=True)

        df = pd.DataFrame({feat.name(): [datetime(2018, 1, 1).date(), None, float('nan'), np.nan],
                           'other': [1, 2, 3, 4]})

        se = feat.verify_input(df)
        self.assertTrue(se.is_empty())

    def test_date_type_return_wrong_format_values(self):
        feat = DateInputFeature('date')

        df = pd.DataFrame({feat.name(): [datetime(2018, 1, 1).date(), 'bubble', datetime(2018, 1, 3).date()],
                           'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertIn('bubble', ie.to_string())

    def test_string_type(self):
        feat = StringInputFeature('text')

        df = pd.DataFrame({feat.name(): ['a', 'b', 'c'], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['a', 34, 'c'], 'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_string_type_with_sample_size(self):
        feat = StringInputFeature('text', verification_sample_size=2)

        df = pd.DataFrame({feat.name(): ['a', 'b', 'c'], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['a', 34, 1], 'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_string_type_return_wrong_format_values(self):
        feat = StringInputFeature('text')

        df = pd.DataFrame({feat.name(): ['a', 34, 'c'], 'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertIn('34', ie.to_string())

    def test_allow_nan_is_compatible_with_type_check_for_string(self):
        """
        when allow_nan=True, NaN values should be accepted and not reported as wrong_format
        :return:
        """
        feat = StringInputFeature('text', allow_nan=True)

        df = pd.DataFrame({feat.name(): ['ciao', None, float('nan'), np.nan], 'other': [1, 2, 3, 4]})

        se = feat.verify_input(df)
        self.assertTrue(se.is_empty())

    def test_string_timestamp_type_with_strict_format(self):
        feat = StringTimestampInputFeature('date_as_string', timestamp_format='%Y-%m-%d')

        df = pd.DataFrame({feat.name(): ['2018-01-01',
                                         '2018-01-02',
                                         '2018-01-03'],
                           'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [2018, 45, 3],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['2018-01-01',
                                         2018,
                                         '2018-01-03'],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['2018-01-01',
                                         '2018',
                                         '2018-01-03'],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_string_timestamp_type_without_specific_format(self):
        feat = StringTimestampInputFeature('date_as_string')

        df = pd.DataFrame({feat.name(): ['2018-01-01',
                                         '2018-01-02',
                                         '2018-01-03'],
                           'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): [2018, 45, 3],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['2018-01-01',
                                         2018,
                                         '2018-01-03'],
                           'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['2018-01-01',
                                         '2018',
                                         '2018-01-03'],
                           'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

    def test_allow_nan_is_compatible_with_type_check_for_string_timestamp(self):
        """
        when allow_nan=True, NaN values should be accepted and not reported as wrong_format
        :return:
        """
        feat = StringTimestampInputFeature('date_as_string', allow_nan=True)

        df = pd.DataFrame({feat.name(): ['2018-01-01', None, float('nan'), np.nan], 'other': [1, 2, 3, 4]})

        se = feat.verify_input(df)
        self.assertTrue(se.is_empty())

    def test_string_timestamp_type_return_wrong_format_values(self):
        feat = StringTimestampInputFeature('date_as_string', timestamp_format='%Y-%m-%d')

        df = pd.DataFrame({feat.name(): ['2018-01-01',
                                         '2018',
                                         '2018-01-03'],
                           'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertIn('2018', ie.to_string())

    def test_country_code_type(self):
        feat = CountryCodeInputFeature('country_code')

        df = pd.DataFrame({feat.name(): ['IT', 'DE', 'FR'], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['IT', 'XX', 'FR'], 'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['IT', 34, 'FR'], 'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_country_code_type_with_sample_size(self):
        feat = CountryCodeInputFeature('country_code', verification_sample_size=2)

        df = pd.DataFrame({feat.name(): ['IT', 'DE', 'FR'], 'rock': [1, 2, 3]})
        self.assert_there_is_no_error(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['IT', 'XX', 'JJ'], 'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

        df = pd.DataFrame({feat.name(): ['IT', 34, 'YY'], 'rock': [1, 2, 3]})
        self.assert_only_format_is_wrong(feat.verify_input(df))

    def test_missing_column_for_country_code(self):
        feat = CountryCodeInputFeature('country_code', verification_sample_size=2)
        df = pd.DataFrame({'rock': [1, 2, 3]})
        ie = feat.verify_input(df)
        self.assertTrue(ie.has_missing_columns())

    def test_allow_nan_is_compatible_with_type_check_for_country_code(self):
        """
        when allow_nan=True, NaN values should be accepted and not reported as wrong_format
        :return:
        """
        feat = CountryCodeInputFeature('country_code', allow_nan=True)

        df = pd.DataFrame({feat.name(): ['DE', None, float('nan'), np.nan], 'other': [1, 2, 3, 4]})

        se = feat.verify_input(df)
        self.assertTrue(se.is_empty())

    def test_country_code_type_return_wrong_format_values(self):
        feat = CountryCodeInputFeature('country_code')

        df = pd.DataFrame({feat.name(): ['IT', 'XX', 'FR'], 'rock': [1, 2, 3]})

        ie = feat.verify_input(df)
        self.assertIn('XX', ie.to_string())
