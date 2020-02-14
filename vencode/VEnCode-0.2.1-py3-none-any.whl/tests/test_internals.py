#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os
import unittest

import numpy as np
import pandas as pd

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals
from VEnCode import common_variables as cv
from VEnCode.utils import dir_and_file_handling as dh


class DataTpmTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.celltypes_total = ["Hepatocyte", "Adipocyte - breast"]
        cls.celltype_analyse = "Adipocyte - breast"


class FilenameHandlerTest(DataTpmTest):
    @unittest.skip
    def test_custom(self):
        file_type = "custom"
        database = internals.DataTpm(file=file_type, nrows=4)
        self.assertEqual(os.path.isfile(database._file_path), True)

    def test_filename(self):
        file_type = cv.test_promoter_file_name
        database = internals.DataTpm(file=file_type, nrows=4)
        self.assertEqual(os.path.isfile(database._file_path), True)

    def test_parsed(self):
        file_type = "parsed"
        database = internals.DataTpm(file=file_type, nrows=4)
        database.make_data_celltype_specific(self.celltype_analyse)
        self.assertEqual(os.path.isfile(database._file_path), True)


class RawDataTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_promoters = internals.DataTpm(file=cv.test_promoter_file_name, nrows=4, keep_raw=True)
        cls.database_enhancers = internals.DataTpm(file=cv.test_enhancer_file_name, nrows=4, keep_raw=True,
                                                   data_type="enhancers")

    def test_open(self):
        self.assertEqual(isinstance(self.database_promoters.raw_data, pd.DataFrame), True)

    def test_open_enhancers(self):
        self.assertEqual(isinstance(self.database_enhancers.raw_data, pd.DataFrame), True)

    def test_nrows(self):
        self.assertEqual(self.database_promoters.raw_data.shape[0], 4)

    def test_nrows_enhancers(self):
        self.assertEqual(self.database_enhancers.raw_data.shape[0], 4)

    def test_ncols(self):
        self.assertEqual(self.database_promoters.raw_data.shape[1], 1829)

    def test_ncols_enhancers(self):
        self.assertEqual(self.database_enhancers.raw_data.shape[1], 1827)

    def test_row_names(self):
        expected = ["chr10:100013403..100013414,-", "chr10:100027943..100027958,-",
                    "chr10:100076685..100076699,+", "chr10:100150910..100150935,-"]
        self.assertEqual(self.database_promoters.raw_data.index.values.tolist(), expected)

    def test_row_names_enhancers(self):
        expected = ['chr1:839741-840250', 'chr1:840753-841210', 'chr1:845485-845678', 'chr1:855764-856157']
        self.assertEqual(self.database_enhancers.raw_data.index.values.tolist(), expected)

    def test_col_names_enhancers(self):
        """ Tests if all column tags were converted to proper celltype names"""
        for column_name in self.database_enhancers.raw_data.columns:
            self.assertIn(column_name, self.database_enhancers.names_db["celltypes"].values)


class DataNotParsedTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_promoters = internals.DataTpm(file=cv.test_promoter_file_name, nrows=4)
        cls.database_enhancers = internals.DataTpm(file=cv.test_enhancer_file_name, nrows=4, data_type="enhancers")

    def test_primary_cells_ncols_promoters(self):
        self.assertEqual(self.database_promoters.data.shape[1], 537)

    def test_primary_cells_ncols_enhancers(self):
        self.assertEqual(self.database_enhancers.data.shape[1], 537)


class DataParsedTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        file_type = "parsed"
        cls.database_promoters = internals.DataTpm(file=file_type, nrows=4)
        cls.database_promoters.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_enhancers = internals.DataTpm(file=file_type, nrows=4, data_type="enhancers")
        cls.database_enhancers.make_data_celltype_specific(cls.celltype_analyse)

    def test_primary_cells_ncols_promoters(self):
        self.assertEqual(self.database_promoters.data.shape[1], 155)

    def test_primary_cells_ncols_enhancers(self):
        self.assertEqual(self.database_enhancers.data.shape[1], 155)

    @unittest.skip
    def test_col_names_equal(self):
        proms = set(self.database_promoters.data.columns.tolist())
        enhs = set(self.database_enhancers.data.columns.tolist())
        self.assertEqual(proms, enhs)


class MakeCelltypeSpecificTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_promoters = internals.DataTpm(file=cv.test_promoter_file_name, nrows=4)
        cls.database_promoters.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_enhancers = internals.DataTpm(file=cv.test_enhancer_file_name, nrows=4, data_type="enhancers")
        cls.database_enhancers.make_data_celltype_specific(cls.celltype_analyse)

    def test_donors_promoters(self):
        expected = {'Adipocyte - breast, donor1', 'Adipocyte - breast, donor2'}
        self.assertEqual(expected, set(self.database_promoters.ctp_analyse_donors["Adipocyte - breast"]))

    def test_donors_enhancers(self):
        expected = {'Adipocyte - breast, donor1', 'Adipocyte - breast, donor2'}
        self.assertEqual(expected, set(self.database_enhancers.ctp_analyse_donors["Adipocyte - breast"]))


class MakeCelltypeSpecificParsedTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        file_type = "parsed"
        cls.database_promoters = internals.DataTpm(file=file_type, nrows=4)
        cls.database_promoters.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_enhancers = internals.DataTpm(file=file_type, nrows=4, data_type="enhancers")
        cls.database_enhancers.make_data_celltype_specific(cls.celltype_analyse)

    def test_donors_promoters(self):
        expected = {'tpm.Adipocyte%20-%20breast%2c%20donor1.CNhs11051.11376-118A8',
                    'tpm.Adipocyte%20-%20breast%2c%20donor2.CNhs11969.11327-117E4'}
        self.assertEqual(expected, set(self.database_promoters.ctp_analyse_donors["Adipocyte - breast"]))

    def test_donors_enhancers(self):
        expected = {'Adipocyte - breast, donor1', 'Adipocyte - breast, donor2'}
        self.assertEqual(expected, set(self.database_enhancers.ctp_analyse_donors["Adipocyte - breast"]))


class MergeDonorsPrimaryTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_promoters = internals.DataTpm(file=cv.test_promoter_file_name, nrows=4)
        cls.database_promoters.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_promoters.merge_donors_primary()
        cls.database_enhancers = internals.DataTpm(file=cv.test_enhancer_file_name, nrows=4, data_type="enhancers")
        cls.database_enhancers.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_enhancers.merge_donors_primary()

    def test_merged_promoters_cols(self):
        self.assertEqual(self.database_promoters.data.shape[1], 155)

    def test_merged_enhancers_cols(self):
        self.assertEqual(self.database_enhancers.data.shape[1], 155)

    # @unittest.skip
    def test_col_names_equal(self):
        data_promoters = set(self.database_promoters.data.columns.tolist())
        data_enhancers = set(self.database_enhancers.data.columns.tolist())
        self.assertEqual(data_promoters, data_enhancers)


class FilterByTargetTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_promoters = internals.DataTpm(file=cv.test_promoter_file_name, nrows=10)
        cls.database_promoters.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_promoters.merge_donors_primary()
        cls.database_enhancers = internals.DataTpm(file=cv.test_enhancer_file_name, nrows=10, data_type="enhancers")
        cls.database_enhancers.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_enhancers.merge_donors_primary()

    def test_above_threshold_promoters(self, threshold=1):
        _temp = self.database_promoters.data[self.database_promoters.ctp_analyse_donors[self.celltype_analyse]] \
            .values.tolist()
        expected = [i for i in _temp if (all(f >= threshold for f in i))]
        self.database_promoters.filter_by_target_celltype_activity(threshold=threshold, binarize=False)
        to_test = self.database_promoters.data[self.database_promoters.ctp_analyse_donors[self.celltype_analyse]] \
            .values.tolist()
        self.assertEqual(expected, to_test)

    def test_above_threshold_enhancers(self, threshold=0.15):
        _temp = self.database_enhancers.data[self.database_enhancers.ctp_analyse_donors[self.celltype_analyse]] \
            .values.tolist()
        expected = [i for i in _temp if (all(f >= threshold for f in i))]
        self.database_enhancers.filter_by_target_celltype_activity(threshold=threshold, binarize=False)
        to_test = self.database_enhancers.data[self.database_enhancers.ctp_analyse_donors[self.celltype_analyse]] \
            .values.tolist()
        self.assertEqual(expected, to_test)


class FilterBySparsenessTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_promoters = internals.DataTpm(file=cv.test_promoter_file_name, nrows=10)
        cls.database_promoters.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_promoters.merge_donors_primary()
        cls.database_promoters.filter_by_reg_element_sparseness(threshold=50)
        cls.database_enhancers = internals.DataTpm(file=cv.test_enhancer_file_name, nrows=100, data_type="enhancers")
        cls.database_enhancers.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_enhancers.merge_donors_primary()
        cls.database_enhancers.filter_by_reg_element_sparseness(threshold=50)

    def test_ctp_still_in_df_promoters(self):
        condition = all([x for x in self.database_promoters.ctp_analyse_donors[
            self.celltype_analyse] if x in self.database_promoters.data.columns.tolist()])
        self.assertTrue(condition)

    def test_ctp_still_in_df_enhancers(self):
        condition = all([x for x in self.database_enhancers.ctp_analyse_donors[
            self.celltype_analyse] if x in self.database_enhancers.data.columns.tolist()])
        self.assertTrue(condition)

    def test_number_cols_promoters(self):
        self.assertEqual(10, self.database_promoters.data.shape[0])

    def test_number_cols_enhancers(self):
        self.assertEqual(87, self.database_enhancers.data.shape[0])

    def test_percentile_col_not_in_df(self):
        column = "Percentile_col"
        condition = column in self.database_promoters.data.columns.tolist()
        self.assertFalse(condition)


class DefineNonTargetCelltypesInactivityTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_promoters = internals.DataTpm(file=cv.test_promoter_file_name, nrows=10)
        cls.database_promoters.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_promoters.merge_donors_primary()
        cls.database_promoters.filter_by_target_celltype_activity(threshold=1)
        cls.database_promoters.define_non_target_celltypes_inactivity(threshold=0.3)
        cls.database_enhancers = internals.DataTpm(file=cv.test_enhancer_file_name, nrows=10, data_type="enhancers")
        cls.database_enhancers.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_enhancers.merge_donors_primary()
        cls.database_enhancers.filter_by_target_celltype_activity(threshold=0.15)
        cls.database_enhancers.define_non_target_celltypes_inactivity(threshold=0)

    def test_if_int_promoters(self):
        self.assertFalse([True for item in self.database_promoters.data.dtypes if item != np.int64])

    def test_if_int_enhancers(self):
        self.assertFalse([True for item in self.database_enhancers.data.dtypes if item != np.int64])

    def test_no_bigger_than_one_promoters(self):
        result = pd.eval("self.database_promoters.data.values > 1")
        self.assertFalse(np.any(result))

    def test_no_bigger_than_one_enhancers(self):
        result = pd.eval("self.database_enhancers.data.values > 1")
        self.assertFalse(np.any(result))


class SortSparsenessTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_promoters = internals.DataTpm(file=cv.test_promoter_file_name, nrows=20)
        cls.database_promoters.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_promoters.merge_donors_primary()
        cls.database_promoters.filter_by_target_celltype_activity(threshold=1)
        cls.database_promoters.define_non_target_celltypes_inactivity(threshold=0)
        cls.database_promoters.sort_sparseness()
        cls.database_enhancers = internals.DataTpm(file=cv.test_enhancer_file_name, nrows=50, data_type="enhancers")
        cls.database_enhancers.make_data_celltype_specific(cls.celltype_analyse)
        cls.database_enhancers.merge_donors_primary()
        cls.database_enhancers.filter_by_target_celltype_activity(threshold=0.15)
        cls.database_enhancers.define_non_target_celltypes_inactivity(threshold=0)
        cls.database_enhancers.sort_sparseness()

    def test_sort_promoters(self):
        self.database_promoters.data["Sum"] = self.database_promoters.data.sum(axis=1)
        counter = 0
        previous_row = None
        for row_sum in self.database_promoters.data["Sum"].values:
            if previous_row is None or row_sum >= previous_row:
                counter += 1
                previous_row = row_sum
        self.assertEqual(counter, 3)

    def test_sort_enhancers(self):
        self.database_enhancers.data["Sum"] = self.database_enhancers.data.sum(axis=1)
        counter = 0
        previous_row = None
        for row_sum in self.database_enhancers.data["Sum"].values:
            if previous_row is None or row_sum >= previous_row:
                counter += 1
                previous_row = row_sum
        self.assertEqual(counter, 5)


class RemoveCelltypeTest(DataTpmTest):
    def setUp(self):
        self.cage_primary = internals.DataTpm(file="parsed", nrows=4)
        self.cage_primary.make_data_celltype_specific(self.celltype_analyse)

    def test_remove_hepatocyte(self):
        self.cage_primary.remove_celltype("Hepatocyte")
        with self.assertRaises(KeyError):
            test = self.cage_primary.data["Hepatocyte"]

    def test_incorrect_celltype(self):
        self.cage_primary.remove_celltype("Hipatocytes")
        condition = not self.cage_primary.data["Hepatocyte"].empty
        self.assertTrue(condition)


class RemoveElementTest(DataTpmTest):
    def setUp(self):
        self.cage_primary = internals.DataTpm(file="parsed", nrows=4)
        self.cage_primary.make_data_celltype_specific(self.celltype_analyse)
        self.elements = ['chr10:100027943..100027958,-', 'chr10:100174900..100174956,-']

    def test_remove_elements(self):
        self.cage_primary.remove_element(self.elements)
        with self.assertRaises(KeyError):
            test = self.cage_primary.data.loc[self.elements]

    def test_incorrect_elements(self):
        self.cage_primary.remove_celltype("test incorrect RE")
        condition = not self.cage_primary.data.loc[self.elements].empty
        self.assertTrue(condition)


class AddCelltypeTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # main data
        cls.cage_primary = internals.DataTpm(file=cv.test_promoter_file_name, nrows=20)
        # copies for all different tests
        cls.cage_cancer = cls.cage_primary.copy(deep=True)
        cls.cage_tissue = cls.cage_primary.copy(deep=True)
        cls.cage_primary_rescue = cls.cage_primary.copy(deep=True)
        # adding a cancer celltype
        cls.cage_cancer.add_celltype("small cell lung carcinoma cell line", file=cv.test_promoter_file_name,
                                     sample_types="cell lines", data_type="promoters")
        # adding a tissue celltype
        # cls.cage_tissue.add_celltype("pituitary gland", file=cv.test_promoter_file_name,
        #                              sample_types="tissues", data_type="promoters")
        # adding a primary celltype after having removed from the data set
        cls.cage_primary_rescue.remove_celltype("Keratocytes", merged=False)
        cls.cage_primary_rescue.add_celltype("Keratocytes", file=cv.test_promoter_file_name,
                                             sample_types="primary cells", data_type="promoters")

    def test_merging(self):
        expected = ['small cell lung carcinoma cell line:LK-2', 'small cell lung carcinoma cell line:WA-hT',
                    'small cell lung carcinoma cell line:DMS 144', 'small cell lung carcinoma cell line:NCI-H82']
        for i in expected:
            with self.subTest(i=i):
                self.assertIn(i, self.cage_cancer.data.columns)

    def test_celltype_only_added(self):
        expected_difference = ['small cell lung carcinoma cell line:LK-2', 'small cell lung carcinoma cell line:WA-hT',
                               'small cell lung carcinoma cell line:DMS 144',
                               'small cell lung carcinoma cell line:NCI-H82']
        difference = set(self.cage_cancer.data.columns.values) - set(self.cage_primary.data.columns.values)
        self.assertCountEqual(expected_difference, difference)

    def test_any_nan(self):
        self.assertFalse(self.cage_cancer.data.isnull().values.any())

    def test_adding_back_primary(self):
        self.cage_primary.sort_columns()
        self.cage_primary_rescue.sort_columns()
        self.assertEqual(self.cage_primary, self.cage_primary_rescue)


class EqualTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        file_type = "parsed"
        cls.data = internals.DataTpm(file=file_type, nrows=4)
        cls.data.make_data_celltype_specific(cls.celltype_analyse)
        cls.data2 = cls.data.copy(deep=True)
        cls.data2.sample_type = "test"
        cls.data3 = cls.data.copy(deep=True)
        cls.data3.data.iloc[0, 0] = 3
        cls.data4 = cls.data.copy(deep=True)

    def test_unequal_arg(self):
        condition = self.data == self.data2
        self.assertFalse(condition)

    def test_unequal_data(self):
        condition = self.data == self.data3
        self.assertFalse(condition)

    def test_equal_data(self):
        condition = self.data == self.data4
        self.assertTrue(condition)


class CopyTest(DataTpmTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        file_type = "parsed"
        cls.data = internals.DataTpm(file=file_type, nrows=4)
        cls.data.make_data_celltype_specific(cls.celltype_analyse)

    def setUp(self):
        self.data2 = self.data.copy(deep=False)
        self.data3 = self.data.copy(deep=True)

    def test_shallow_creation(self):
        self.assertEqual(self.data, self.data2)

    def test_shallow_equal_data(self):
        condition = self.data.data.equals(self.data2.data)
        self.assertTrue(condition)

    def test_deep_creation(self):
        self.assertEqual(self.data, self.data3)

    def test_deep_equal_data(self):
        condition = self.data.data.equals(self.data3.data)
        self.assertTrue(condition)

    def test_change_arg_shallow(self):
        self.data2.target_ctp = "test"
        self.assertNotEqual(self.data, self.data2)

    def test_change_arg_deep(self):
        self.data3.target_ctp = "test"
        self.assertNotEqual(self.data, self.data3)

    def test_change_data_shallow(self):
        self.data2.data.iloc[1, 1] = "test"
        self.assertEqual(self.data, self.data2)

    def test_change_data_deep(self):
        self.data3.data.iloc[1, 1] = "test"
        self.assertNotEqual(self.data, self.data3)


class SortColumnsTest(DataTpmTest):
    def setUp(self):
        file_type = "parsed"
        self.cage_tpm = internals.DataTpm(file=file_type, nrows=4)
        self.cage_tpm.make_data_celltype_specific(self.celltype_analyse)
        self.cols = self.cage_tpm.data.columns.tolist()

    def test_sort_alphabetically(self):
        self.cage_tpm.sort_columns()
        cols = self.cage_tpm.data.columns.tolist()
        for i in (self.cols, sorted(self.cols, key=str.lower)):
            condition = (i == cols)
            with self.subTest(i=i):
                if i == self.cols:
                    self.assertFalse(condition)
                else:
                    self.assertTrue(condition)

    def test_values_remain(self):
        before = self.cage_tpm.data["Urothelial cells"].values.tolist()
        self.cage_tpm.sort_columns()
        after = self.cage_tpm.data["Urothelial cells"].values.tolist()
        self.assertEqual(before, after)

    def test_sort_to_first(self):
        celltype = "Urothelial cells"
        before = self.cage_tpm.data.columns.tolist().index(celltype)
        self.cage_tpm.sort_columns(col_to_shift=celltype, pos_to_move=0)
        after = self.cage_tpm.data.columns.tolist().index(celltype)
        condition = (before != after) and (after == 0)
        self.assertTrue(condition)


class VenCodesHepatocyteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.celltype_analyse = "Hepatocyte"
        cls.data = internals.DataTpm(file="parsed", nrows=None)
        cls.data.make_data_celltype_specific(cls.celltype_analyse)


class HepatocyteHeuristicTest(VenCodesHepatocyteTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.data.filter_by_target_celltype_activity(threshold=1)
        cls.data.define_non_target_celltypes_inactivity(threshold=0)
        cls.data.sort_sparseness()

    def setUp(self):
        self.vencodes = internals.Vencodes(self.data, algorithm="heuristic", number_of_re=4)

    def test_first_vencode(self):
        self.vencodes.next(amount=1)
        expected = ['chr15:85427903..85427915,+', 'chr16:72094548..72094561,-', 'chr14:94914994..94915003,-',
                    'chr12:57828590..57828604,+']
        self.assertCountEqual(expected, self.vencodes.vencodes[0])

    def test_second_vencode(self):
        self.vencodes.next(amount=1)
        vencode = self.vencodes.next(amount=1)
        expected = ['chr15:85427903..85427915,+', 'chr16:72094548..72094561,-', 'chr14:94914994..94915003,-',
                    'chr11:61297083..61297101,-']
        for i in (self.vencodes.vencodes[1], vencode[0]):
            with self.subTest(i=i):
                self.assertCountEqual(expected, i)

    def test_if_correct_vencodes(self):
        self.vencodes.next(amount=3)
        for vencode_data in self.vencodes.get_vencode_data(method="return"):
            vencode_data.drop(self.vencodes.celltype_donors, axis=1, inplace=True)
            with self.subTest(i=vencode_data.index.values.tolist()):
                condition = self.vencodes._assess_vencode_one_zero_boolean(vencode_data)
                self.assertTrue(condition)

    def test_e_values_created(self):
        self.vencodes.next(amount=2)
        self.vencodes.determine_e_values()
        maximum = 100
        minimum = 0
        for i in self.vencodes.e_values.values():
            with self.subTest(i=i):
                self.assertTrue(maximum >= i >= minimum)


class HepatocyteSamplingTest(VenCodesHepatocyteTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.data.filter_by_target_celltype_activity(threshold=1)
        cls.data.define_non_target_celltypes_inactivity(threshold=0)
        cls.data.sort_sparseness()

    def setUp(self):
        self.vencodes = internals.Vencodes(self.data, algorithm="sampling", number_of_re=4, n_samples=10000)

    def test_vencode(self):
        self.vencodes.next(amount=1)
        expected = ['chr15:85427903..85427915,+', 'chr16:72094548..72094561,-', 'chr14:94914994..94915003,-',
                    'chr12:57828590..57828604,+']
        self.assertCountEqual(expected, self.vencodes.vencodes[0])

    def test_second_vencode(self):
        self.vencodes.next(amount=1)
        self.vencodes.next(amount=1)
        expected = 4
        self.assertEqual(expected, len(self.vencodes.vencodes[1]))

    def test_if_correct_vencodes(self):
        self.vencodes.next(amount=3)
        for vencode_data in self.vencodes.get_vencode_data(method="return"):
            vencode_data.drop(self.vencodes.celltype_donors, axis=1, inplace=True)
            with self.subTest(i=vencode_data.index.values.tolist()):
                condition = self.vencodes._assess_vencode_one_zero_boolean(vencode_data)
                self.assertTrue(condition)


class VenCodesAdipocyteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.celltype_analyse = "Adipocyte - breast"
        cls.data = internals.DataTpm(file="parsed", nrows=None)
        cls.data.make_data_celltype_specific(cls.celltype_analyse)
        cls.data.filter_by_target_celltype_activity(threshold=1)
        cls.data.define_non_target_celltypes_inactivity(threshold=0)
        cls.data.sort_sparseness()

    def setUp(self):
        self.vencodes = internals.Vencodes(self.data, algorithm="heuristic", number_of_re=4)

    def test_first_vencode(self):
        vencode = self.vencodes.next(amount=1)
        expected = ["chr5:42175384..42175396,-", "chr6:72596184..72596196,+", "chr6:11532480..11532521,+",
                    "chr12:109568972..109568988,+"]
        for i in (self.vencodes.vencodes[0], vencode[0]):
            with self.subTest(i=i):
                self.assertCountEqual(expected, i)

    def test_second_vencode(self):
        self.vencodes.next(amount=1)
        vencode = self.vencodes.next(amount=1)
        expected = ["chr5:42175384..42175396,-", "chr6:72596184..72596196,+", "chr12:109568972..109568988,+",
                    "chr7:112614228..112614232,+"]
        for i in (self.vencodes.vencodes[1], vencode[0]):
            with self.subTest(i=i):
                self.assertCountEqual(expected, i)

    def test_if_correct_vencodes(self):
        self.vencodes.next(amount=3)
        for vencode_data in self.vencodes.get_vencode_data(method="return"):
            vencode_data.drop(self.vencodes.celltype_donors, axis=1, inplace=True)
            with self.subTest(i=vencode_data.index.values.tolist()):
                condition = self.vencodes._assess_vencode_one_zero_boolean(vencode_data)
                self.assertTrue(condition)

    def test_e_values_created(self):
        self.vencodes.next(amount=2)
        self.vencodes.determine_e_values()
        maximum = 100
        minimum = 0
        for i in self.vencodes.e_values.values():
            with self.subTest(i=i):
                self.assertTrue(maximum >= i >= minimum)


class VenCodesKeratocytesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.celltype_analyse = "Keratocytes"
        cls.data = internals.DataTpm(file="parsed", nrows=None)
        cls.data.make_data_celltype_specific(cls.celltype_analyse)
        cls.data.filter_by_target_celltype_activity(threshold=1)
        cls.data.define_non_target_celltypes_inactivity(threshold=0)
        cls.data.sort_sparseness()

    def setUp(self):
        self.vencodes = internals.Vencodes(self.data, algorithm="heuristic", number_of_re=4)

    def test_first_vencode(self):
        vencode = self.vencodes.next(amount=1)
        expected = ['chr4:111536708..111536738,-', 'chr5:79331164..79331177,+', 'chr15:41786065..41786081,+',
                    'chr17:56081185..56081244,-']
        for i in (self.vencodes.vencodes[0], vencode[0]):
            with self.subTest(i=i):
                self.assertCountEqual(expected, i)

    def test_second_vencode(self):
        self.vencodes.next(amount=1)
        vencode = self.vencodes.next(amount=1)
        expected = ['chr4:111536708..111536738,-', 'chr5:79331164..79331177,+', 'chr15:41786065..41786081,+',
                    'chr7:6501803..6501823,-']
        for i in (self.vencodes.vencodes[1], vencode[0]):
            with self.subTest(i=i):
                self.assertCountEqual(expected, i)

    def test_vencode_different_node(self):
        vencodes = self.vencodes.next(amount=2)
        self.assertTrue(len(vencodes) == 2)

    def test_if_correct_vencodes(self):
        self.vencodes.next(amount=3)
        for vencode_data in self.vencodes.get_vencode_data(method="return"):
            vencode_data.drop(self.vencodes.celltype_donors, axis=1, inplace=True)
            with self.subTest(i=vencode_data.index.values.tolist()):
                condition = self.vencodes._assess_vencode_one_zero_boolean(vencode_data)
                self.assertTrue(condition)

    def test_e_values_created(self):
        self.vencodes.next(amount=2)
        self.vencodes.determine_e_values()
        maximum = 100
        minimum = 0
        for i in self.vencodes.e_values.values():
            with self.subTest(i=i):
                self.assertTrue(maximum >= i >= minimum)


class VenCodesBronchialEpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.celltype_analyse = "Bronchial Epithelial Cell"
        cls.data = internals.DataTpm(file="parsed", nrows=None)
        cls.data.make_data_celltype_specific(cls.celltype_analyse)
        cls.data.filter_by_target_celltype_activity(threshold=1)
        cls.data.define_non_target_celltypes_inactivity(threshold=0)
        cls.data.sort_sparseness()

    def setUp(self):
        self.vencodes = internals.Vencodes(self.data, algorithm="heuristic", number_of_re=4)

    def test_first_vencode(self):
        self.vencodes.next(amount=1)
        self.assertFalse(self.vencodes.vencodes)


class VencodesMethodsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = internals.DataTpm(file="parsed", sample_types="primary cells", data_type="promoters", nrows=20000)
        cls.data.make_data_celltype_specific("Hepatocyte")
        cls.data.filter_by_target_celltype_activity(threshold=1)
        cls.data.filter_by_reg_element_sparseness(threshold=0)
        cls.data.define_non_target_celltypes_inactivity(threshold=0)
        cls.data.sort_sparseness()
        cls.vencodes = internals.Vencodes(cls.data, algorithm="heuristic", number_of_re=4, stop=3)
        cls.vencodes.next(amount=2)

    def test_view_vencodes(self):
        self.vencodes.view_vencodes(method="write", snapshot=30)
        folder_path = self.vencodes._parent_path
        file_path_1 = os.path.join(folder_path, "Hepatocyte_heat_map.png")
        file_path_2 = os.path.join(folder_path, "Hepatocyte_heat_map-1.png")
        for i in (file_path_1, file_path_2):
            with self.subTest(i=i):
                self.assertTrue(os.path.exists(i))
                dh.remove_file(i)

    def test_get_vencodes_write(self):
        self.vencodes.get_vencode_data(method="write")
        folder_path = self.vencodes._parent_path
        file_path_1 = os.path.join(folder_path, "Hepatocyte_vencode.csv")
        file_path_2 = os.path.join(folder_path, "Hepatocyte_vencode-1.csv")
        for i in (file_path_1, file_path_2):
            with self.subTest(i=i):
                self.assertTrue(os.path.exists(i))
                dh.remove_file(i)

    def test_get_vencodes_return(self):
        vencodes = self.vencodes.get_vencode_data(method="return")
        expected = (pd.DataFrame, (4, 156))
        for vencode_data in vencodes:
            properties = (type(vencode_data), vencode_data.shape)
            with self.subTest(i=vencode_data):
                self.assertEqual(properties, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
