import unittest

import numpy as np
import pandas as pd
import utils.directory_handlers
import utils.writing_files
from utils import util

from VEnCode.utils import pandas_utils as pdutil


class FilterByExpressionAndPercentileTest(unittest.TestCase):
    # TODO: finish this test
    def setUp(self):
        """Produce some filtered data sets."""
        data_pre = np.fromfunction(lambda x, y: np.sin(x) * np.tan(y) * x * 10, (400, 154))
        for array in data_pre:
            array[array < 0] = 0
        self.data = pd.DataFrame(data_pre)
        self.data.columns = self.data.columns.astype(str)
        print(self.data)

    def test_one(self):
        prediction = (199, 154)
        result = util.df_filter_by_expression_and_percentile(self.data, "90", 1, 2, threshold=90)
        print(result)
        self.assertEqual(prediction, result.shape, msg="Result not expected")


class FilterByExpression(unittest.TestCase):
    def setUp(self):
        """Produce a pandas DataFrame for testing."""
        data_pre = {"names": ["one", "two", "three", "four"],
                    "col1": [0, 1.4, 20, 0], "col2": [0, 14.6, 0, 1], "col3": [0, 0, 0.1, 0.01],
                    "col4": [0, 0.0091, 0, 0]}
        self.test_pandas_df = pd.DataFrame(data=data_pre).set_index("names").astype("float")

    def test_expression_one(self):
        test = util.df_filter_by_expression(self.test_pandas_df, "col1", 1)
        prediction = ["two", "three"]
        self.assertEqual(test.index.values.tolist(), prediction)

    def test_expression_zero_one(self):
        test = util.df_filter_by_expression(self.test_pandas_df, "col3", 0.1)
        prediction = ["three"]
        self.assertEqual(test.index.values.tolist(), prediction)

    def test_expression_zero_zero_one(self):
        test = util.df_filter_by_expression(self.test_pandas_df, "col3", 0.01)
        prediction = ["three", "four"]
        self.assertEqual(test.index.values.tolist(), prediction)

    def test_multi_codes(self):
        test = util.df_filter_by_expression(self.test_pandas_df, ["col1", "col2"], 1)
        prediction = ["two"]
        self.assertEqual(test.index.values.tolist(), prediction)


class AssessVencodeOneZeroBooleanTest(unittest.TestCase):
    def setUp(self):
        """ Define some samples to assess if VEnCode. """
        data_pre = {"names": ["one", "two", "three", "four"],
                    "col1": [0, 1, 1, 0], "col2": [0, 1, 0, 1], "col3": [0, 0, 1, 1],
                    "col4": [0, 1, 0, 0]}
        self.test_pandas_df = pd.DataFrame(data=data_pre).set_index("names").astype("float")

    def test_threshold_zero_success(self):
        test = util.assess_vencode_one_zero_boolean(self.test_pandas_df, threshold=0)
        self.assertTrue(test, msg="Result not expected")

    def test_threshold_zero_fail(self):
        pdutil.multi_set_data_frame(self.test_pandas_df, (("one", "col1"), ("four", "col1")), 1)
        test = util.assess_vencode_one_zero_boolean(self.test_pandas_df, threshold=0)
        self.assertFalse(test, msg="Result not expected")

    def test_threshold_zero_one_success(self):
        pdutil.multi_set_data_frame(self.test_pandas_df, (("one", "col1"), ("four", "col1")), 0.1)
        test = util.assess_vencode_one_zero_boolean(self.test_pandas_df, threshold=0.1)
        self.assertTrue(test, msg="Result not expected")

    def test_threshold_zero_one_fail(self):
        pdutil.multi_set_data_frame(self.test_pandas_df, (("one", "col1"), ("four", "col1")), 1)
        test = util.assess_vencode_one_zero_boolean(self.test_pandas_df, threshold=0.1)
        self.assertFalse(test, msg="Result not expected")

    def test_threshold_zero_zero_one_success(self):
        pdutil.multi_set_data_frame(self.test_pandas_df, (("one", "col1"), ("four", "col1")), 0.01)
        test = util.assess_vencode_one_zero_boolean(self.test_pandas_df, threshold=0.01)
        self.assertTrue(test, msg="Result not expected")

    def test_threshold_zero_zero_one_fail(self):
        pdutil.multi_set_data_frame(self.test_pandas_df, (("one", "col1"), ("four", "col1")), 0.1)
        test = util.assess_vencode_one_zero_boolean(self.test_pandas_df, threshold=0.01)
        self.assertFalse(test, msg="Result not expected")


class CombinationsFromNestedListTest(unittest.TestCase):
    # TODO: finish this test
    def setUp(self):
        """Start by creating several lists to test"""
        self.lst1 = ["aa", "bb", "cc"]
        self.lst2 = ["aa", ["bb", "cc"]]
        self.lst3 = ["aa", ["bb", ["cc"]]]
        self.lst4 = ["aa", ["bb", ["cc", "dd"]]]
        self.lst5 = ["aa", ["bb", ["cc", ["dd"]]]]
        self.lst6 = ["aa", ["bb", ["cc", ["dd", "ee"]]]]

    def general_testing(self):
        """
        runs normal function
        """
        for i in util.combinations_from_nested_lists(self.lst1):
            print(i)


class TestMakingWritingFiles:
    def test_dicts(self):
        results_dict = {"aa": [1,2], "bb": [2,4]}
        results_directory = utils.directory_handlers.check_if_and_makefile(r"/example/testing dicts",
                                                                           path_type="parent")
        # Util.check_if_and_makedir(results_directory)
        utils.writing_files.write_dict_to_csv(results_directory, results_dict, deprecated=False)

if __name__ == "__main__":
    unittest.main()

    """
    test = TestFiles_in_folder_to_csv()
    test.test_file_creation()
    

    test = TestCFNL(lst6)
    test.general_testing()
    """
