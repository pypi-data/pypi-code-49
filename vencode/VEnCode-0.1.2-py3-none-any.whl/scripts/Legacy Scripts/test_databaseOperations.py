import unittest

import classes
import pandas as pd

from VEnCode.utils import pandas_utils as pdutil


class SampleCategorySelectorTest(unittest.TestCase):
    def setUp(self):
        """Define"""
        pass


class EvalueNormalizerTest(unittest.TestCase):
    def setUp(self):
        """Define a few normalized e-values."""
        self.excess = []
        self.near_maximum = []
        self.zero = []
        self.fifty_percent = None

        def small_database(n=80, k=4):
            """tests a small sized db"""
            self.excess.append(classes.Promoters.e_value_normalizer(1000, n, k))
            self.near_maximum.append(classes.Promoters.e_value_normalizer(98, n, k))
            self.zero.append(classes.Promoters.e_value_normalizer(0, n, k))

        def standard_database(n=154, k=4):
            """tests a standard sized db"""
            self.excess.append(classes.Promoters.e_value_normalizer(1000, n, k))
            self.near_maximum.append(classes.Promoters.e_value_normalizer(160, n, k))
            self.zero.append(classes.Promoters.e_value_normalizer(0, n, k))

        def large_database(n=800, k=8):
            """tests a large sized db"""
            self.excess.append(classes.Promoters.e_value_normalizer(3000, n, k))
            self.near_maximum.append(classes.Promoters.e_value_normalizer(2620, n, k))
            self.zero.append(classes.Promoters.e_value_normalizer(0, n, k))

        def database_cut_half():
            """tests a database when it's half full row- or column-wise"""
            cut_rows = classes.Promoters.e_value_normalizer(25.3866, 200, 4)
            cut_cols = classes.Promoters.e_value_normalizer(117.1372, 200, 4)
            self.fifty_percent = (cut_rows, cut_cols)

        small_database(), standard_database(), large_database(), database_cut_half()

    def test_more_than_hundred_percent(self):
        """When raw e-values reach more than the maximum predicted by the model, should return 100."""
        for e_value in self.excess:
            self.assertEqual(e_value, 100)

    def test_around_hundred_percent(self):
        """When raw e-values are near or at the maximum predicted by the model, should return 100 +/-10."""
        for e_value in self.near_maximum:
            self.assertGreater(e_value, 90)
            self.assertLessEqual(e_value, 100)

    def test_e_value_zero(self):
        """ When raw e-values are zero, should normalize to zero"""
        for e_value in self.zero:
            self.assertEqual(e_value, 0)

    def test_fifty_percent(self):
        """ When database is about half full (row- or column-wise) should normalize to a predictable number"""
        for e_value, expected in zip(self.fifty_percent, (12.8831, 59.4446)):
            self.assertAlmostEqual(e_value, expected, places=3)


class NodeBasedVencodeGetterTest(unittest.TestCase):
    def setUp(self):
        """First, define initial shared data"""
        data_pre = {"names": ["one", "two", "three", "four", "five"],
                    "col1": [0, 1, 1, 0, 1], "col2": [0, 1, 0, 1, 1], "col3": [0, 0, 1, 1, 0],
                    "col4": [0, 1, 0, 0, 1]}
        self.data = pd.DataFrame(data=data_pre).set_index("names")
        self.breaks = {}
        for item in range(1, 4):
            self.breaks["breaker_" + str(item)] = 0

    def test_one_first(self):
        self.one = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [["one"]]
        self.assertEqual(result, self.one, msg="Result not expected")

    def test_one_not_first(self):
        self.data.at["one", "col1"] = 1
        pdutil.multi_set_data_frame(self.data, (("three", "col1"), ("three", "col3")), 0)
        self.one = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [["three"]]
        self.assertEqual(result, self.one, msg="Result not expected")

    def test_one_many(self):
        pdutil.multi_set_data_frame(self.data, (("three", "col1"), ("three", "col3")), 0)
        df = pd.DataFrame.from_dict({"six": [0, 0, 0, 0]}, orient="index")
        df.columns = self.data.columns
        self.data = pd.concat([self.data, df])
        self.one = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [["one", "three", "six"]]
        self.assertEqual(result, self.one, msg="Result not expected")

    def test_two_contiguous(self):
        pdutil.multi_set_data_frame(self.data, (("one", "col1"), ("four", "col1")), 1)
        self.data.at["two", "col1"] = 0
        self.two = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [["one", ["two"]]]
        self.assertEqual(result, self.two, msg="Result not expected")

    def test_two_non_contiguous(self):
        self.data.at["one", "col1"] = 1
        self.two = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [["one", ["four"]]]
        self.assertEqual(result, self.two, msg="Result not expected")

    def test_two_many(self):
        self.data.at["one", "col1"] = 1
        self.data.at["two", "col1"] = 0
        self.two = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [["one", ["two", "four"]]]
        self.assertEqual(result, self.two, msg="Result not expected")

    def test_three_contiguous(self):
        pdutil.multi_set_data_frame(self.data, (("one", "col2"), ("one", "col3")), 1)
        self.three = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [['one', ['two', ['three']]]]
        self.assertEqual(result, self.three, msg="Result not expected")

    def test_three_non_contiguous(self):
        pdutil.multi_set_data_frame(self.data, (("one", "col1"), ("one", "col4"), ("four", "col4")), 1)
        self.three = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [['one', ['two', ['three', ['four']]]]]
        self.assertEqual(result, self.three, msg="Result not expected")
        """
        Note for this result:
        Even with a solution of a combination of 3 instead of four [['one', ['three', ['four']]]], our algorithm will 
        first find the solution of four due to searching "two" first. This, of course only happens when searching for
        combinations of up to 4. If we set the search for "k" up to 3, we then get the solution:
        [['one', ['three', ['four']]]]
        """
        self.three_new = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=3)
        result = [['one', ['three', ['four']]]]
        self.assertEqual(result, self.three_new, msg="Result not expected")

    def test_four_contiguous(self):
        pdutil.multi_set_data_frame(self.data, (("one", "col1"), ("one", "col4"), ("four", "col4")), 1)
        self.four = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [['one', ['two', ['three', ['four']]]]]
        self.assertEqual(result, self.four, msg="Result not expected")

    def test_four_non_contiguous(self):
        pdutil.multi_set_data_frame(self.data, (("one", "col1"), ("one", "col4"), ("four", "col4"),
                                                ("two", "col3"), ("one", "col3")), 1)
        self.four = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4)
        result = [['one', ['three', ['four', ['five']]]]]
        self.assertEqual(result, self.four, msg="Result not expected")

    def test_with_breaks(self):
        """
        Here we test the ability of stopping the iteration short. If left unchecked, it would have found the solution:
        [['one', ['four', ['five']]]] first, but by putting a cap of value 2 in the search, node "one" will only
        search until "one + three + Any", not sufficient for a VEnCode of k=3 with this data. So, the algorithm must
        continue to node "two", then finding the below described solution.
        """
        pdutil.multi_set_data_frame(self.data, (("one", "col1"), ("one", "col2"), ("one", "col3")), 1)
        self.data.at["five", "col2"] = 0
        result = [['two', ['three', ['four']]]]
        self.with_breaks = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=3,
                                                                       breaks=self.breaks, stop=2)
        self.assertEqual(result, self.with_breaks, msg="Result not expected")

    def test_skipping(self):
        """
        Here we skip row "two" from the analysis, simulating a previous run where promoter "two" was already used.
        We use the same set up as test_three_non_contiguous.
        """
        pdutil.multi_set_data_frame(self.data, (("one", "col1"), ("one", "col4"), ("four", "col4")), 1)
        self.three = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=4, skip=["two"])
        result = [['one', ['three', ['four']]]]
        self.assertEqual(result, self.three, msg="Result not expected")

    def test_skipping_with_breaks(self):
        """
        Here we skip row "one" from the analysis, simulating a previous run where promoter "one" was already used.
        We use the same set up as test_with_breaks, which means that testing stops after a set amount.
        """
        pdutil.multi_set_data_frame(self.data, (("one", "col1"), ("one", "col2"), ("one", "col3")), 1)
        self.data.at["five", "col2"] = 0
        result = [['two', ['three', ['four']]]]
        result_2 = []
        three = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=3, skip=["one"],
                                                            breaks=self.breaks, stop=1)
        three_2 = classes.Promoters.node_based_vencode_getter(self.data, combinations_number=3, skip=["two"],
                                                              breaks=self.breaks, stop=2)
        to_assert = ((result, three), (result_2, three_2))
        for i in to_assert:
            with self.subTest(i=i):
                self.assertEqual(i[0], i[1], msg="Result not expected")

    def test_multiple_vencodes(self):
        pass


class SamplingMethodVencodeGetter(unittest.TestCase):
    def setUp(self):
        """First, define initial shared data"""
        data_pre = {"names": ["one", "two", "three", "four", "five"],
                    "col1": [0, 1, 1, 0, 1], "col2": [0, 1, 0, 1, 1], "col3": [0, 0, 1, 1, 0],
                    "col4": [0, 1, 0, 0, 1]}
        self.data = pd.DataFrame(data=data_pre).set_index("names")

    def test_one(self):
        self.one = classes.Promoters.sampling_method_vencode_getter(self.data,
                                                                    combinations_number=1).index.values.tolist()
        result = ["one"]
        self.assertCountEqual(result, self.one, msg="Result not expected")

    def test_two(self):
        self.data.at["one", "col1"] = 1
        self.two = classes.Promoters.sampling_method_vencode_getter(self.data,
                                                                    combinations_number=2).index.values.tolist()
        result = ["one", "four"]
        self.assertCountEqual(result, self.two, msg="Result not expected")


class PrepSortTest(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':  # run tests if called from command-line
    unittest.main()
