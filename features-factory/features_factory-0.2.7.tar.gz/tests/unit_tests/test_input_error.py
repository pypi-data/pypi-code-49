import unittest

from features_factory.input_data_error import InputDataError


class TestInputError(unittest.TestCase):

    def test_initially_input_error_has_all_fields_empty(self):
        ie = InputDataError()
        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())

    def test_add_missing_columns(self):
        ie = InputDataError()
        ie.add_missing_column('bubble')
        ie.add_missing_column('bubble')
        ie.add_missing_column('rock')
        self.assertTrue(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())
        self.assertCountEqual(['bubble', 'rock'], ie.get_missing_columns())

    def test_add_column_with_nan(self):
        ie = InputDataError()
        ie.add_column_with_nan('bubble')
        ie.add_column_with_nan('bubble')
        ie.add_column_with_nan('rock')
        self.assertFalse(ie.has_missing_columns())
        self.assertTrue(ie.has_columns_with_nan())
        self.assertFalse(ie.has_columns_with_wrong_format())
        self.assertCountEqual(['bubble', 'rock'], ie.get_columns_with_nan())

    def test_add_column_with_wrong_format(self):
        ie = InputDataError()
        ie.add_column_with_wrong_format('bubble')
        ie.add_column_with_wrong_format('bubble')
        ie.add_column_with_wrong_format('rock')
        self.assertFalse(ie.has_missing_columns())
        self.assertFalse(ie.has_columns_with_nan())
        self.assertTrue(ie.has_columns_with_wrong_format())
        self.assertCountEqual(['bubble', 'rock'], ie.get_columns_with_wrong_format())

    def test_add(self):
        ie1 = InputDataError()
        ie1.add_missing_column('bubble')
        ie1.add_column_with_wrong_format('stone')

        ie2 = InputDataError()
        ie2.add_missing_column('bubble')
        ie2.add_missing_column('rock')
        ie2.add_column_with_nan('wind')

        ie = ie1 + ie2

        # -- verify result of the summation
        self.assertTrue(ie.has_missing_columns())
        self.assertTrue(ie.has_columns_with_nan())
        self.assertTrue(ie.has_columns_with_wrong_format())
        self.assertCountEqual(['bubble', 'rock'], ie.get_missing_columns())
        self.assertCountEqual(['wind'], ie.get_columns_with_nan())
        self.assertCountEqual(['stone'], ie.get_columns_with_wrong_format())

        # --- ie1 and ie2 are unchanged
        self.assertCountEqual(['bubble'], ie1.get_missing_columns())
        self.assertCountEqual([], ie1.get_columns_with_nan())
        self.assertCountEqual(['stone'], ie1.get_columns_with_wrong_format())

        self.assertCountEqual(['bubble', 'rock'], ie2.get_missing_columns())
        self.assertCountEqual(['wind'], ie2.get_columns_with_nan())
        self.assertCountEqual([], ie2.get_columns_with_wrong_format())

    def test_incremental_add(self):
        ie = InputDataError()
        ie.add_missing_column('bubble')
        ie.add_column_with_wrong_format('stone')

        ie1 = InputDataError()
        ie1.add_missing_column('bubble')
        ie1.add_missing_column('rock')
        ie1.add_column_with_nan('wind')

        ie += ie1

        # -- verify result of the summation
        self.assertTrue(ie.has_missing_columns())
        self.assertTrue(ie.has_columns_with_nan())
        self.assertTrue(ie.has_columns_with_wrong_format())
        self.assertCountEqual(['bubble', 'rock'], ie.get_missing_columns())
        self.assertCountEqual(['wind'], ie.get_columns_with_nan())
        self.assertCountEqual(['stone'], ie.get_columns_with_wrong_format())

        # --- ie1 is unchanged
        self.assertCountEqual(['bubble', 'rock'], ie1.get_missing_columns())
        self.assertCountEqual(['wind'], ie1.get_columns_with_nan())
        self.assertCountEqual([], ie1.get_columns_with_wrong_format())

    def test_to_string_contains_involved_names(self):
        ie = InputDataError()
        ie.add_missing_column('bubble')
        self.assertTrue('bubble' in ie.to_string())

        ie = InputDataError()
        ie.add_column_with_nan('bubble')
        self.assertTrue('bubble' in ie.to_string())

        ie = InputDataError()
        ie.add_column_with_wrong_format('bubble')
        self.assertTrue('bubble' in ie.to_string())

    def test_to_string_of_empty_error_contains_word_empty(self):
        ie = InputDataError()
        self.assertTrue('empty' in ie.to_string())

    def test_wrong_format_values_are_provided_in_error_message(self):
        ie = InputDataError()
        ie.add_column_with_wrong_format('bubble', value=37)
        ie.add_column_with_wrong_format('bubble', value='miao')
        ie.add_column_with_wrong_format('rock', value=3.14)
        ie_msg = ie.to_string()
        self.assertIn('37', ie_msg)
        self.assertIn('miao', ie_msg)
        self.assertIn('3.14', ie_msg)
