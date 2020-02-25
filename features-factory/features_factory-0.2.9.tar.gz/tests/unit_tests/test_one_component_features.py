import unittest
from datetime import datetime

import pandas as pd

from features_factory.input_features import DateTimeInputFeature, StringInputFeature
from features_factory.one_component_features import MonthFromDateFeature, DateTimeFromStringFeature, \
    DateFromStringFeature, RenamedFeature, WeekdayFromDateFeature


class TestRenamedFeature(unittest.TestCase):

    def test_verify_df_column_name_changed(self):
        feat = StringInputFeature('whatever')
        renamed_feat = RenamedFeature('whenever', feat)

        df = pd.DataFrame({feat.name(): [1, 2, 3],
                           'spam': [4, 5, 6]})
        new_df = renamed_feat.insert_into(df)

        self.assertCountEqual([feat.name(), 'spam'], df.columns)
        self.assertCountEqual([renamed_feat.name(), feat.name(), 'spam'], new_df.columns)


class TestDateTimeFromStringFeature(unittest.TestCase):

    def test_verify_input_data(self):
        date_as_string = StringInputFeature('whatever')
        feat = DateTimeFromStringFeature('timestamp', date_as_string)

        df = pd.DataFrame({'ajo': [1, 2, 4], 'yooooo': ['abra', 'cada', 'bra']})
        ie = feat.verify_input(df)
        self.assertFalse(ie.is_empty())

        df = pd.DataFrame({date_as_string.name(): ['2018-1-11 15:00',
                                                   '2018-1-18',
                                                   '2018-1-21 15:03:46',
                                                   '24-7-2019'],
                           'yooooo': ['abra', 'cada', 'bra', 'ket']})
        ie = feat.verify_input(df)
        self.assertTrue(ie.is_empty())

    def test_get_dependencies_returns_a_tuple_with_one_feature(self):
        date_as_string = StringInputFeature('whatever')
        feat = DateTimeFromStringFeature('timestamp', date_as_string)

        self.assertIsInstance(feat.get_dependencies(), tuple)
        self.assertEqual(1, len(feat.get_dependencies()))
        self.assertEqual(date_as_string, feat.get_dependencies()[0])

    def test_generate_provides_correct_values(self):
        date_as_string = StringInputFeature('whatever')
        feat = DateTimeFromStringFeature('timestamp', date_as_string)

        df = pd.DataFrame({date_as_string.name(): ['2018-1-11 15:00',
                                                   '2018-1-18',
                                                   '2018-1-21 15:03:46',
                                                   '24-7-2019'],
                           'yooooo': ['abra', 'cada', 'bra', 'ket']})

        df = date_as_string.insert_into(df)
        date_time = feat.generate(df)
        self.assertEqual([datetime(2018, 1, 11, 15), datetime(2018, 1, 18),
                          datetime(2018, 1, 21, 15, 3, 46), datetime(2019, 7, 24)], date_time.tolist())


class TestDateFromStringFeature(unittest.TestCase):

    def test_verify_input_data(self):
        date_as_string = StringInputFeature('whatever')
        feat = DateFromStringFeature('date', date_as_string)

        df = pd.DataFrame({'ajo': [1, 2, 4], 'yooooo': ['abra', 'cada', 'bra']})
        ie = feat.verify_input(df)
        self.assertFalse(ie.is_empty())

        df = pd.DataFrame({date_as_string.name(): ['2018-1-11 15:00',
                                                   '2018-1-18',
                                                   '2018-1-21 15:03:46',
                                                   '24-7-2019'],
                           'yooooo': ['abra', 'cada', 'bra', 'ket']})
        ie = feat.verify_input(df)
        self.assertTrue(ie.is_empty())

    def test_get_dependencies_returns_a_tuple_with_one_feature(self):
        date_as_string = StringInputFeature('whatever')
        feat = DateFromStringFeature('date', date_as_string)

        self.assertIsInstance(feat.get_dependencies(), tuple)
        self.assertEqual(1, len(feat.get_dependencies()))
        self.assertEqual(date_as_string, feat.get_dependencies()[0])

    def test_generate_provides_correct_values(self):
        date_as_string = StringInputFeature('whatever')
        feat = DateFromStringFeature('date', date_as_string)

        df = pd.DataFrame({date_as_string.name(): ['2018-1-11 15:00',
                                                   '2018-1-18',
                                                   '2018-1-21 15:03:46',
                                                   '24-7-2019'],
                           'yooooo': ['abra', 'cada', 'bra', 'ket']})

        df = date_as_string.insert_into(df)
        date_time = feat.generate(df)
        self.assertEqual([datetime(2018, 1, 11, 15).date(), datetime(2018, 1, 18).date(),
                          datetime(2018, 1, 21, 15, 3, 46).date(), datetime(2019, 7, 24).date()], date_time.tolist())


class TestMonthFeature(unittest.TestCase):

    def test_verify_input_data(self):
        shipping_date = DateTimeInputFeature('shipping_date')
        feat = MonthFromDateFeature('shipping_month', shipping_date)

        df = pd.DataFrame({'ajo': [1, 2, 4], 'yooooo': ['abra', 'cada', 'bra']})
        ie = feat.verify_input(df)
        self.assertFalse(ie.is_empty())

        df = pd.DataFrame({shipping_date.name(): [datetime(2018, 1, 11),
                                                  datetime(2018, 1, 18),
                                                  datetime(2018, 1, 21)],
                           'yooooo': ['abra', 'cada', 'bra']})
        ie = feat.verify_input(df)
        self.assertTrue(ie.is_empty())

    def test_get_dependencies_returns_a_tuple_with_one_feature(self):
        shipping_date = DateTimeInputFeature('shipping_date')
        feat = MonthFromDateFeature('shipping_month', shipping_date)

        self.assertIsInstance(feat.get_dependencies(), tuple)
        self.assertEqual(1, len(feat.get_dependencies()))
        self.assertEqual(shipping_date, feat.get_dependencies()[0])

    def test_generate_provides_correct_values(self):
        shipping_date = DateTimeInputFeature('shipping_date')
        feat = MonthFromDateFeature('shipping_month', shipping_date)

        df = pd.DataFrame({shipping_date.name(): [datetime(2018, 1, 11),
                                                  datetime(2018, 7, 18),
                                                  datetime(2018, 3, 21)],
                           'yooooo': ['abra', 'cada', 'bra']})

        df = shipping_date.insert_into(df)
        months = feat.generate(df)
        self.assertEqual([1, 7, 3], months.tolist())


class TestWeekdayFeature(unittest.TestCase):

    def test_verify_input_data(self):
        shipping_date = DateTimeInputFeature('shipping_date')
        feat = WeekdayFromDateFeature('shipping_weekday', shipping_date)

        df = pd.DataFrame({'ajo': [1, 2, 4], 'yooooo': ['abra', 'cada', 'bra']})
        ie = feat.verify_input(df)
        self.assertFalse(ie.is_empty())

        df = pd.DataFrame({shipping_date.name(): [datetime(2018, 1, 11),
                                                  datetime(2018, 1, 18),
                                                  datetime(2018, 1, 21)],
                           'yooooo': ['abra', 'cada', 'bra']})
        ie = feat.verify_input(df)
        self.assertTrue(ie.is_empty())

    def test_get_dependencies_returns_a_tuple_with_one_feature(self):
        shipping_date = DateTimeInputFeature('shipping_date')
        feat = WeekdayFromDateFeature('shipping_weekday', shipping_date)

        self.assertIsInstance(feat.get_dependencies(), tuple)
        self.assertEqual(1, len(feat.get_dependencies()))
        self.assertEqual(shipping_date, feat.get_dependencies()[0])

    def test_generate_provides_correct_values(self):
        shipping_date = DateTimeInputFeature('shipping_date')
        feat = WeekdayFromDateFeature('shipping_weekday', shipping_date)

        df = pd.DataFrame({shipping_date.name(): [datetime(2019, 2, 18),
                                                  datetime(2019, 2, 22),
                                                  datetime(2019, 2, 24)],
                           'yooooo': ['abra', 'cada', 'bra']})

        df = shipping_date.insert_into(df)
        weekdays = feat.generate(df)
        self.assertEqual([0, 4, 6], weekdays.tolist())
