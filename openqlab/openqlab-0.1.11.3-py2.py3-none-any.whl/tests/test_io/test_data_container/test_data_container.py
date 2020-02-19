import importlib
import logging
import unittest
import warnings
from copy import deepcopy
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
from tests.test_plots.test_plots_tear_down import TestPlotTearDown

from openqlab import io
from openqlab.io.data_container import DataContainer, MetaDataContainer, _combine_header

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

filedir = Path(__file__).parent
datadir = filedir / "data"


def add_tested_method(func):
    print_flag = False  # change to True if results should be printed to console
    star_count = 60

    def wrapper(*args, **kwargs):
        method = func.__name__[5:]
        TestDataFrameMethods.tested_methods.append(method)
        if print_flag:
            print("\n")
            print("*" * star_count)
            print(f"{func.__name__} :")

        for result in func(*args, method=method, **kwargs):
            if print_flag:
                print(f"{result}\n")
        if print_flag:
            print("*" * star_count)

    return wrapper


class TestDataContainerMeta(unittest.TestCase):
    def test_all_methods_valid(self):
        with warnings.catch_warnings(record=True) as w:
            MetaDataContainer.__new__(
                MetaDataContainer,
                name="DC",
                bases=(pd.DataFrame,),
                clsdict=dict(pd.DataFrame.__dict__),
            )
            print(w)
            if w:
                self.fail("Warning should not appear.")

    def test_missing_method(self):
        MockedMeta = deepcopy(MetaDataContainer)
        MockedMeta.functions = ["MISSING"]
        with self.assertWarns(Warning):
            MockedMeta.__new__(
                MockedMeta,
                name="DC",
                bases=(pd.DataFrame,),
                clsdict=dict(pd.DataFrame.__dict__),
            )


class TestDataContainerBase(unittest.TestCase):
    def setUp(self):
        self.header1 = {"a": "a", "ab": "ab"}
        self.header2 = {"b": "b", "ab": "ab"}
        self.header_combined = {"ab": "ab"}
        self.basedata = {"one": [1, 2, 3], "two": [4, 5, 6]}
        self.nandata = {"one": [1, None, 3], "two": [4, 5, None]}
        self.squaredata = {"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]}
        self.oneeq_column = {"two": [4, 5, 6], "four": [4, 5, 6]}
        self.twoeq_column = {"one": [4, 5, 6], "two": [1, 2, 3]}
        self.uneq_columns = {"three": [1, 2, 3], "four": [4, 5, 6]}
        self.time_index = pd.date_range("2018-04-09", periods=4, freq="12H")
        # caller:
        self.base = DataContainer(self.basedata, header=self.header1)
        self.nan = DataContainer(self.nandata, header=self.header1)
        self.square = DataContainer(self.squaredata, header=self.header1)
        self.time = DataContainer(
            {"A": [1, 2, 3, 4]}, index=self.time_index, header=self.header1
        )
        arrays = [
            np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),
            np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),
        ]
        self.multi = DataContainer(
            np.random.randn(8, 4), index=arrays, header=self.header1
        )
        # other:
        self.oneeq = DataContainer(self.oneeq_column, header=self.header2)
        self.twoeq = DataContainer(self.twoeq_column, header=self.header2)
        self.uneq = DataContainer(self.uneq_columns, header=self.header2)
        self.time2 = DataContainer(
            {"A": [1, 2, 3, 4]}, index=self.time_index, header=self.header2
        )


class TestDataFrameMethods(TestDataContainerBase):
    tested_methods: List[str] = []

    @classmethod
    def setUpClass(cls):
        cls.tested_methods = []

    @classmethod
    def tearDownClass(cls):
        for method in MetaDataContainer.normal_methods:
            if method not in cls.tested_methods:
                warnings.warn(f"'{method}' method not tested", UserWarning)

    def test_magic_methods(self):
        funcs = MetaDataContainer.magic_methods
        for f in funcs:
            base = deepcopy(self.base)
            other = deepcopy(self.oneeq)
            result = DataContainer.__dict__[f](base, other)
            self.assertIsInstance(result, DataContainer)
            self.assertEqual(result.header, {"ab": "ab"})
            yield result

            result = DataContainer.__dict__[f](base, base)
            self.assertIsInstance(result, DataContainer)
            self.assertEqual(result.header, self.header1)
            yield result

    def test_single_parameter_magic_methods(self):
        funcs = MetaDataContainer.single_parameter_magic_methods
        for f in funcs:
            base = deepcopy(self.base)
            result = DataContainer.__dict__[f](base)
            self.assertIsInstance(result, DataContainer)
            self.assertEqual(result.header, self.header1)
            yield result

    def test_computations(self):
        funcs = MetaDataContainer.computations_single
        for f in funcs:
            base = deepcopy(self.base)
            result = DataContainer.__dict__[f](base)
            self.assertIsInstance(result, DataContainer)
            self.assertEqual(result.header, self.header1)
            yield result

    @add_tested_method
    def test_add(self, method):
        result = self.base.__getattr__(method)(self.uneq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, {"ab": "ab"})
        yield result

    @add_tested_method
    def test_append(self, method):
        result = self.base.__getattr__(method)(self.uneq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_join(self, method):
        result = self.base.__getattr__(method)(self.uneq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, {"ab": "ab"})
        yield result

    @add_tested_method
    def test_merge(self, method):
        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, {"ab": "ab"})
        yield result

    @add_tested_method
    def test_combine(self, method):
        result = self.base.__getattr__(method)(
            self.twoeq, lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
        )
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, {"ab": "ab"})
        yield result

        result = self.base.__getattr__(method)(
            self.oneeq,
            lambda s1, s2: s1 if s1.sum() < s2.sum() else s2,
            overwrite=False,
        )
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, {"ab": "ab"})
        yield result

    @add_tested_method
    def test_combine_first(self, method):
        result = self.nan.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, {"ab": "ab"})
        yield result

        result = self.nan.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, {"ab": "ab"})
        yield result

    @add_tested_method
    def test_copy(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_div(self, method):
        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, {"ab": "ab"})
        yield result

    @add_tested_method
    def test_divide(self, method):
        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_dot(self, method):
        result = self.square.__getattr__(method)(self.square.transpose())
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base.transpose())
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_floordiv(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_transpose(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_sub(self, method):
        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_mul(self, method):
        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_astype(self, method):
        result = self.base.__getattr__(method)("int32")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_infer_objects(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_isna(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_isnull(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_notna(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_select_dtypes(self, method):
        result = self.base.__getattr__(method)(include="int64")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(exclude="int64")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_isin(self, method):
        result = self.base.__getattr__(method)([1, 2, 3])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)([2, 4, 6])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_where(self, method):
        result = self.base.__getattr__(method)(self.base >= 2, -self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.base >= 2, -self.uneq, inplace=True)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header_combined)
        yield self.base

    @add_tested_method
    def test_mask(self, method):
        result = self.base.__getattr__(method)(self.base >= 2, -self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.base >= 2, -self.uneq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_query(self, method):
        result = self.base.__getattr__(method)("one >two")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_apply(self, method):
        result = self.base.__getattr__(method)(lambda x: (x - x.mean()) / x.std())
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_applymap(self, method):
        result = self.base.__getattr__(method)(lambda x: len(str(x)))
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_aggregate(self, method):
        result = self.base.__getattr__(method)(["min"])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_agg(self, method):
        result = self.base.__getattr__(method)(["min"])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_transform(self, method):
        result = self.base.__getattr__(method)(lambda x: (x - x.mean()) / x.std())
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_truediv(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_mod(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_pow(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_radd(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_rsub(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_rmul(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_rdiv(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_rtruediv(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_rfloordiv(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_rmod(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_rpow(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @unittest.skip("Removed from Dataframe")
    @add_tested_method
    def test_clip_lower(self, method):
        result = self.square.__getattr__(method)(3)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(3)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @unittest.skip("Removed from Dataframe")
    @add_tested_method
    def test_clip_upper(self, method):
        result = self.square.__getattr__(method)(3)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(3)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_corrwith(self, method):
        result = self.square.__getattr__(method)(self.square)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.base)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(self.oneeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

        result = self.base.__getattr__(method)(self.twoeq)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_eval(self, method):
        result = self.base.__getattr__(method)("combined = one + two")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)("combined = one + two", inplace=True)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header1)
        yield self.base

    @add_tested_method
    def test_add_prefix(self, method):
        result = self.base.__getattr__(method)("column_")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.square.__getattr__(method)("column_")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_add_suffix(self, method):
        result = self.base.__getattr__(method)("column_")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.square.__getattr__(method)("column_")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_at_time(self, method):
        result = self.time.__getattr__(method)("12:00")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_between_time(self, method):
        result = self.time.__getattr__(method)("12:00", "13:00")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.time.__getattr__(method)("13:00", "12:00")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_drop(self, method):
        result = self.base.__getattr__(method)(["two"], axis=1)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)([0, 2])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_drop_duplicates(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(inplace=True)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header1)
        yield self.base

    @add_tested_method
    def test_filter(self, method):
        result = self.base.__getattr__(method)(items=["one", "three"])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_first(self, method):
        result = self.time.__getattr__(method)("2D")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_last(self, method):
        result = self.time.__getattr__(method)("2D")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_head(self, method):
        result = self.base.__getattr__(method)(2)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_tail(self, method):
        result = self.base.__getattr__(method)(2)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_reindex(self, method):
        result = self.base.__getattr__(method)(["first", "second", "third"])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)([0, 1, 2, 3, 4, 5])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_reindex_like(self, method):
        result = self.base.__getattr__(method)(self.time2)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header_combined)
        yield result

    @add_tested_method
    def test_rename(self, method):
        result = self.base.__getattr__(method)(
            index=str, columns={"one": "a", "two": "b"}
        )
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_rename_axis(self, method):
        result = self.base.__getattr__(method)("foo")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_reset_index(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(inplace=True)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header1)
        yield self.base

    @add_tested_method
    def test_sample(self, method):
        result = self.base.__getattr__(method)(2)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_set_axis(self, method):
        result = self.base.__getattr__(method)(
            ["a", "b", "c"], axis="index", inplace=False
        )
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(
            ["a", "b", "c"], axis="index", inplace=True
        )
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header1)
        yield self.base

    @add_tested_method
    def test_set_index(self, method):
        result = self.base.__getattr__(method)("one", inplace=False)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)("one", inplace=True)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header1)
        yield self.base

    @add_tested_method
    def test_take(self, method):
        result = self.base.__getattr__(method)([1, 2])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)([1], axis=1)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_truncate(self, method):
        result = self.base.__getattr__(method)(before=0, after=1)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(before="one", after="one", axis=1)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_dropna(self, method):
        result = self.nan.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_fillna(self, method):
        result = self.nan.__getattr__(method)("None")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.nan.__getattr__(method)(method="ffill")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_replace(self, method):
        result = self.base.__getattr__(method)(2, "Replaced")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(2, "Replaced", inplace=True)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header1)
        yield self.base

    @add_tested_method
    def test_interpolate(self, method):
        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(inplace=True)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header1)
        yield self.base

    @add_tested_method
    def test_pivot(self, method):
        result = self.square.__getattr__(method)(
            index="one", columns="two", values="three"
        )
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_pivot_table(self, method):
        result = self.square.__getattr__(method)(
            index="one", columns="two", values="three"
        )
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_reorder_levels(self, method):
        result = self.multi.__getattr__(method)([1, 0])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_sort_values(self, method):
        result = self.base.__getattr__(method)(by=["one"])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(by=["one"], ascending=False)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(by=["one"], inplace=True)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.base.header, self.header1)
        yield self.base

    @add_tested_method
    def test_sort_index(self, method):
        result = self.square.__getattr__(method)(axis=1, ascending=False)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.square.__getattr__(method)(axis=0, ascending=False)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.square.__getattr__(method)(axis=1, inplace=True, ascending=False)
        self.assertIsInstance(result, type(None))
        self.assertEqual(self.square.header, self.header1)
        yield self.square

    @add_tested_method
    def test_nlargest(self, method):
        result = self.square.__getattr__(method)(2, ["one", "three"])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(2, "one")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_nsmallest(self, method):
        result = self.square.__getattr__(method)(2, ["one", "three"])
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)(2, "one")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_swaplevel(self, method):
        result = self.multi.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_stack(self, method):
        result = self.multi.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_unstack(self, method):
        result = self.multi.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_swapaxes(self, method):
        result = self.multi.__getattr__(method)("index", "columns")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)("index", "columns")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_squeeze(self, method):
        result = self.multi.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_melt(self, method):
        result = self.multi.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.base.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_asfreq(self, method):
        result = self.time.__getattr__(method)("1D")
        # print(f"Result = {result}")
        # self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.time.__getattr__(method)("6H")
        # print(f"Result = {result}")
        # self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_asof(self, method):
        result = self.time.__getattr__(method)(pd.Timestamp("2018-04-09 12:00:00"))
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.time.__getattr__(method)(
            [pd.Timestamp("2018-04-09 12:00:00"), pd.Timestamp("2018-04-10 12:00:00")]
        )
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_shift(self, method):
        result = self.time.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.time.__getattr__(method)(periods=2)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_slice_shift(self, method):
        result = self.time.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.time.__getattr__(method)(periods=2)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_tshift(self, method):
        result = self.time.__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

        result = self.time.__getattr__(method)(periods=2)
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_to_timestamp(self, method):
        result = self.time.to_period(freq="6H").__getattr__(method)()
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_to_period(self, method):
        result = self.time.__getattr__(method)(freq="13H")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_tz_convert(self, method):
        result = self.time.tz_localize("UTC").__getattr__(method)(tz="EST")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    @add_tested_method
    def test_tz_localize(self, method):
        result = self.time.__getattr__(method)(tz="UTC")
        self.assertIsInstance(result, DataContainer)
        self.assertEqual(result.header, self.header1)
        yield result

    def test_pop(self):
        self.base.pop("one")
        result = self.base
        self.assertIsInstance(self.base, DataContainer)
        self.assertEqual(result.header, self.header1)

        self.base.pop("two")
        result = self.base
        self.assertIsInstance(self.base, DataContainer)
        self.assertEqual(result.header, self.header1)


class TestDataContainer(TestDataContainerBase, TestPlotTearDown):
    def test_plot_with_xUnit_and_subplots(self):
        dc = io.read(datadir / "plot_test.csv")
        dc.columns = ["impulse", "error", "amplitude"]
        dc.plot(subplots=True, figsize=(8, 8), grid=True)

    def test__ensure_type(self):
        df = pd.DataFrame()
        self.base._ensure_type(df)

    def test___str__(self):
        expected_string = (
            "------------------------------------------------------------\na : a\nab : "
            "ab\n------------------------------------------------------------\n   one  two\n0    1    "
            "4\n1    2    5\n2    3    6"
        )
        self.assertEqual(str(self.base), expected_string)

    def test_DataContainer(self):
        with self.assertRaises(TypeError):
            DataContainer(self.basedata, header=[1, 2, 3])
            DataContainer(self.basedata, data=self.basedata)
        self.assertRaises(
            TypeError, DataContainer, self.basedata, data=self.basedata
        )  # just to see if other syntax also works
        self.assertEqual(
            DataContainer(self.basedata, header=self.header1).header, self.header1
        )
        result = DataContainer(self.base)
        self.assertEqual(result.header, self.header1)
        result = DataContainer(self.base, header=self.header2)
        self.assertEqual(result.header, self.header2)
        result = DataContainer(self.base, header=self.header2, header_type="Osci")
        self.assertEqual(result.header, self.header2)

    def test_header(self):
        base = deepcopy(self.base)
        try:
            base.header = self.header1
        except Exception:
            self.fail("setting header with dict is raising error unexpectedly!")
        with self.assertRaises(TypeError):
            base.header = [1, 2, 3]
            base.header = (1, 4, 5)
            base.header = DataContainer()

    def test_combine_header(self):
        self.base.header["Info"] = ("Test1", 4, "Test2")
        result = self.base + self.base
        self.assertEqual(result.header, self.base.header)

        self.base.header["Info"] = ["Test1", 4, "Test2"]
        result = self.base + self.base
        self.assertEqual(result.header, self.base.header)

    def test_wrong_json_prefix(self):
        filename = datadir / "test_wrong_json_prefix.json"
        with open(filename) as file:
            result = DataContainer._json_to_header(file)
            self.assertIsNone(result)
            self.assertEqual(0, file.tell())

    def test_wrong_header_to_json(self):
        header = {"string": "test", "boolean": True, "DataContainer": DataContainer()}
        with self.assertRaises(TypeError):
            DataContainer(header=header)._header_to_json()

    def test_wrong_header_type(self):
        expected_message = "'WrongType' is not a valid header_type for <class 'openqlab.io.data_container.DataContainer'>."
        with self.assertRaisesRegex(TypeError, expected_message):
            DataContainer(header_type="WrongType")


class TestImportExport(TestDataContainerBase):
    def test_csv(self):
        filename = datadir / "test.csv"
        self.base.to_csv(filename)
        result = DataContainer.from_csv(filename)
        self.assertIsInstance(result, DataContainer)
        self.assertIsInstance(result.header, dict)
        self.assertEqual(result.header, self.header1)

        data = io.read(datadir / "2010830P_002")
        data.header = {}
        data.to_csv(filename)
        result = DataContainer.from_csv(filename)
        self.assertIsInstance(result, DataContainer)
        self.assertIsInstance(result.header, dict)
        self.assertEqual(result.__repr__(), data.__repr__())

    def test_json(self):
        filename = str(datadir / "test.json")
        self.base.to_json(filename)
        result = DataContainer.from_json(filename)
        self.assertIsInstance(result, DataContainer)
        self.assertIsInstance(result.header, dict)
        self.assertEqual(result.header, self.header1)

        data = io.read(datadir / "2010830P_002")
        data.header = {}
        data.to_json(filename)
        result = DataContainer.from_json(filename)
        self.assertIsInstance(result, DataContainer)
        self.assertIsInstance(result.header, dict)
        self.assertEqual(result.values.__repr__(), data.values.__repr__())


class TestCombineHeader(TestDataContainerBase):
    def test_other_list_of_dict(self):
        list_of_headers = [self.header1, self.header2]
        header = _combine_header(self.header1, list_of_headers)
        self.assertEqual(self.header_combined, header)


if __name__ == "__main__":
    #     suite = unittest.TestLoader().loadTestsFromTestCase(TestDataContainer)
    #     unittest.TextTestRunner(verbosity=2).run(suite)
    #
    unittest.main()
