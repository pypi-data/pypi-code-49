#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" internals.py: Classes module for the VEnCode project """

import os
import random
import re
import tkinter as tk
from tkinter import filedialog
from copy import copy, deepcopy
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
from Bio import SeqIO
from collections import Counter

import VEnCode.utils.dir_and_file_handling as d_f_handling
from VEnCode import common_variables as cv
from VEnCode.utils import general_utils as gen_util, pandas_utils as pd_util


class DataTpm:
    """
    An Object representing the initial database with some universal data treatment and with optional
    filtering methods
    """

    def __init__(self, file="custom", sample_types="primary cells", data_type="promoters", keep_raw=False, nrows=None,
                 files_path="native"):
        self._file, self.sample_type, self.data_type, self._nrows = file, sample_types, data_type, nrows
        self.target_ctp, self.ctp_analyse_donors, self.ctp_not_include, self.data = None, None, None, None
        self._file_path = None
        if files_path == "native":
            self._parent_path = os.path.join(str(Path(__file__).parents[0]), "Files")
        elif files_path == "outside":
            self._parent_path = os.path.join(str(Path(__file__).parents[2]), "Files")
        else:
            self._parent_path = files_path

        if sample_types in ("cell lines", "tissues"):
            celltype_exclude = None
        elif sample_types == "primary cells":
            celltype_exclude = cv.primary_exclude_list
        else:
            celltype_exclude = None

        if self._file != "parsed":
            self.ctp_exclude = celltype_exclude
            self._file_path = self._filename_handler()
            self.sample_type_file = pd.read_csv(os.path.join(self._parent_path, cv.sample_type_file), sep=",",
                                                index_col=0,
                                                engine="python")
            if data_type == "promoters":
                skiprows = 1831
                if self._nrows is not None:
                    self._nrows += 2
            else:
                skiprows = None
            self.raw_data = pd.read_csv(self._file_path, sep="\t", index_col=0,
                                        skiprows=skiprows, nrows=self._nrows, engine="python")
            if data_type == "promoters":
                if self._nrows is not None:
                    self._nrows -= 2
                self._raw_data_promoters()
            elif data_type == "enhancers":
                self.names_db = pd.read_csv(os.path.join(self._parent_path, cv.enhancer_names_db), sep="\t",
                                            index_col=1,
                                            header=None, names=["celltypes"], engine="python")
                self._raw_data_enhancers()
            else:
                raise AttributeError("data_type argument is not supported")
            self.raw_data.apply(pd.to_numeric, downcast='float')  # optimizes memory usage by downcasting to lower float
            if sample_types in ("primary cells", "cell lines", "cancer", "time courses", "tissues"):
                self.data = self._raw_data_cleaner()
            else:
                self.data = self.raw_data
            if not keep_raw:
                self.raw_data = None
        else:
            pass

    def __eq__(self, other):
        """Allows to check equality between two DataTpm objects"""
        if isinstance(other, DataTpm):
            args_list = [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
            for arg in args_list:
                arg_self, arg_other = "self." + arg, "other." + arg
                if isinstance(eval(arg_self), pd.DataFrame):
                    try:
                        condition = eval(arg_self + ".equals(" + arg_other + ")")
                    except ValueError:
                        cols = eval(arg_self + ".columns.values.tolist()") == eval(arg_other
                                                                                   + ".columns.values.tolist()")
                        rows = eval(arg_self + ".index.values.tolist()") == eval(arg_other
                                                                                 + ".index.values.tolist()")
                        condition = cols and rows
                    except AttributeError as e:
                        print(e)
                        return False
                    if not condition:
                        return False
                    else:
                        continue
                try:
                    if eval(arg_self + "==" + arg_other):
                        continue
                except ValueError:
                    return False
                else:
                    return False
            return True
        return False

    def _filename_handler(self):
        if self._file == "custom":
            root = tk.Tk()
            root.withdraw()
            file_path = tk.filedialog.askopenfilename()
        elif re.search(r"\....", self._file[-4:]):
            file_path = os.path.join(self._parent_path, self._file)
        elif self._file == "parsed":
            celltype_name = self.target_ctp.replace(":", "-").replace("/", "-")
            file_path = os.path.join(self._parent_path, "Dbs", f"{celltype_name}_tpm_{self.data_type}-1.csv")
        else:
            raise AttributeError
        return file_path

    def _raw_data_promoters(self):
        self.raw_data.drop(self.raw_data.index[:2], inplace=True)

    def _raw_data_enhancers(self):
        column_names = {}
        for column_code in self.raw_data.columns.values.tolist():
            try:
                column_names[column_code] = self.names_db.loc[column_code, "celltypes"]
            except KeyError:
                pass
        self.raw_data.rename(columns=column_names, inplace=True)

    def _raw_data_cleaner(self):
        data_1 = self.raw_data.copy()
        universal_rna = self._code_selector(data_1, "universal", not_include=None)
        data_1.drop(universal_rna, axis=1, inplace=True)
        if self.data_type == "promoters":
            to_keep = self._sample_category_selector()
        else:
            to_keep = self._sample_category_selector(get="name")
        data = pd.DataFrame(index=data_1.index.values)
        for sample in to_keep:
            if self.data_type == "promoters":
                data_temp = data_1.filter(regex=sample)
                column_name = self.sample_type_file.loc[sample, "Name"]
                try:
                    data_temp.columns = [column_name]
                except ValueError:
                    column_name = [column_name + ", tech_rep1", column_name + ", tech_rep2"]
                    data_temp.columns = column_name
            else:
                try:
                    data_temp = data_1.loc[:, sample]
                except KeyError:
                    data_temp = pd_util.df_minimal_regex_columns_searcher(sample, data_1)
            try:
                data = data.join(data_temp)
            except ValueError:
                continue
        # Exclude some specific, on-demand, cell-types from the data straight away:
        if self.ctp_exclude is not None:
            codes_exclude = self._code_selector(data, self.ctp_exclude, not_include=None, regex=False)
            data.drop(codes_exclude, axis=1, inplace=True)
        return data

    def _sample_category_selector(self, get="index"):
        """
        Returns a list of cell types to keep/drop from a file containing the list of cell types and a
        'Sample category' column which determines which cell types to retrieve.
        """
        types = self.sample_type
        if not isinstance(types, list):
            types = [types]
        database = self.sample_type_file.copy()
        try:
            possible_types = database["Sample category"].drop_duplicates().values.tolist()
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            raise
        assert all(
            sample in possible_types for sample in types), "Sample type is not valid.\nValid sample types: {}" \
            .format(possible_types)
        celltypes = []
        for sample in types:
            selected = database[database["Sample category"] == sample]
            if get == "index":
                for value in selected.index.values:
                    celltypes.append(value)
            elif get == "name":
                for value in selected["Name"].tolist():
                    celltypes.append(value)
            else:
                pass
        return celltypes

    def _code_selector(self, data, celltype, not_include=None, to_dict=False, regex=True):
        """ Selects celltype codes from database using their general name. """
        if isinstance(celltype, str):  # celltype can be provided as a list or string
            celltype = [celltype]
        codes = []
        code_dict = {}
        for item in celltype:
            codes_df = pd_util.df_regex_columns_searcher(item,
                                                         data) if regex else pd_util.df_minimal_regex_columns_searcher(
                item,
                data)

            if to_dict:
                code_dict[item] = codes_df.columns.values.tolist()
            else:
                codes.append(codes_df.columns.values)
        if not to_dict:
            codes = [item for sublist in codes for item in sublist]  # make one list from nested lists of codes

        if not_include is not None:  # remove some codes that regex might have not been able to differentiate
            for key, values in not_include.items():
                if key not in code_dict.keys():
                    continue
                codes_df = data[code_dict.get(key)]
                not_codes = self._not_include_code_getter(values, codes_df)
                code_dict[key] = list(set(code_dict[key]) - set(not_codes))

        if to_dict:
            codes = code_dict
        self._code_tester(codes, celltype)
        return codes

    @staticmethod
    def _not_include_code_getter(not_include, data_frame):
        if isinstance(not_include, list):
            not_include_codes = []
            for item in not_include:
                not_codes_item = pd_util.df_regex_columns_searcher_list(item, data_frame)
                not_include_codes.append(not_codes_item)
            not_include_codes = [item for sublist in not_include_codes for item in sublist]
        else:
            not_include_codes = pd_util.df_regex_columns_searcher_list(not_include, data_frame)
        return not_include_codes

    @staticmethod
    def _code_tester(codes, celltype, codes_type="list"):
        """ Tests if any codes were generated """
        if codes_type == "list":
            if not codes:
                raise Exception("No codes for {}!".format(celltype))
        elif codes_type == "dict":
            if bool([a for a in codes.values() if a == []]):
                print([item for item, value in codes.items() if not value])
                raise Exception("Some celltypes might not have had codes generated!")
        elif codes_type == "ndarray":
            if codes.size == 0:
                raise Exception("No codes for {}!".format(celltype))
        else:
            raise Exception("Wrong codes type to test for the generation of codes!")

    def copy(self, deep=True):
        """
        Method to generate a shallow, or deep copy of DataTpm object

        :param bool deep: True if deep copy.
        :return: a copy of the DataTpm object
        """
        if deep:
            return deepcopy(self)
        else:
            return copy(self)

    def sort_columns(self, col_to_shift=None, pos_to_move=None):
        """
        Sorts columns alphabetically
        """
        if not col_to_shift or pos_to_move:
            cols = sorted(self.data.columns, key=str.lower)
            self.data = self.data.reindex(cols, axis=1)
        else:
            arr = self.data.columns.values
            idx = self.data.columns.get_loc(col_to_shift)
            if idx == pos_to_move:
                pass
            elif idx > pos_to_move:
                arr[pos_to_move + 1: idx + 1] = arr[pos_to_move: idx]
            else:
                arr[idx: pos_to_move] = arr[idx + 1: pos_to_move + 1]
            arr[pos_to_move] = col_to_shift
            self.data.columns = arr

    def make_data_celltype_specific(self, target_celltypes,
                                    supersets=cv.primary_cells_supersets):
        """
        Determines donors of interest to analyse later. For previous parsed files, opens the specific file
        for that celltype.

        :param target_celltypes: the celltype to target for analysis
        :param dict not_include: codes necessary to exclude some non-target celltypes that get caught by regex motif
        :param dict supersets: when a celltype is a subset of other, we must remove that superset celltype to analyse
        the subset.
        """
        if self.sample_type == "cell lines":
            self.ctp_not_include = cv.cancer_not_include_codes
        elif self.sample_type == "primary cells":
            self.ctp_not_include = cv.primary_not_include_codes
        elif self.sample_type == "time courses":
            self.ctp_not_include = cv.time_courses_not_include_codes
        else:
            self.ctp_not_include = None
        if isinstance(target_celltypes, dict):  # to deal with situations such as mesothelioma cell line
            target_ctp_in_data = list(target_celltypes.values())[0]
        else:
            target_ctp_in_data = target_celltypes

        if self._file == "parsed":
            if isinstance(target_celltypes, dict):
                self.target_ctp = list(target_celltypes.keys())[0]
            else:
                self.target_ctp = target_celltypes
            self._file_path = self._filename_handler()
            self.data = pd.read_csv(self._file_path, sep=";", index_col=0,
                                    skiprows=None, nrows=self._nrows, engine="python")
            self.ctp_analyse_donors = self._code_selector(self.data, target_ctp_in_data,
                                                          not_include=self.ctp_not_include,
                                                          to_dict=True, regex=True)
            # enhancers might need regex to be False:
            if isinstance(target_ctp_in_data, str):
                target_ctp_in_data = [target_ctp_in_data]
            else:
                target_ctp_in_data = target_ctp_in_data
            for celltype in target_ctp_in_data:
                if not self.ctp_analyse_donors[celltype]:
                    self.ctp_analyse_donors = self._code_selector(self.data, target_ctp_in_data,
                                                                  not_include=self.ctp_not_include,
                                                                  to_dict=True, regex=False)
                    break
                else:
                    continue
            if isinstance(target_celltypes, dict):
                temp_dict = {self.target_ctp: list(
                    gen_util.flatten_irregular_nested_lists(list(self.ctp_analyse_donors.values())))}
                self.ctp_analyse_donors = temp_dict

        else:
            self.ctp_analyse_donors = self._code_selector(self.data, target_ctp_in_data,
                                                          not_include=self.ctp_not_include,
                                                          to_dict=True, regex=False)
            if isinstance(target_celltypes, dict):  # to deal with situations such as mesothelioma cell line
                self.target_ctp = list(target_celltypes.keys())[0]
                temp_dict = \
                    {self.target_ctp: list(
                        gen_util.flatten_irregular_nested_lists(list(self.ctp_analyse_donors.values())))}
                self.ctp_analyse_donors = temp_dict
            else:
                self.target_ctp = target_celltypes
        if supersets and self.target_ctp in supersets.keys():
            self.data.drop(supersets[self.target_ctp], axis=1, inplace=True)

    def merge_donors_primary(self, exclude_target=True):
        """
        Applies a more conservative, but faster approach to data set mining:
        cell type columns are created by merging all donors for that cell type. The value for the merged column
        corresponds the average of all donors.
        """
        if self._file == "parsed":
            return
        codes = self._code_selector(self.data, cv.primary_cell_list, not_include=cv.primary_not_include_codes,
                                    to_dict=True, regex=False)
        if exclude_target:
            codes.pop(self.target_ctp, None)
        data_merged = pd.DataFrame(index=self.data.index.values, columns=[key for key in codes.keys()])
        if exclude_target:
            data_merged = pd.concat([data_merged, self.data[self.ctp_analyse_donors[self.target_ctp]]], axis=1)
        for code, donors in codes.items():
            celltypes_averaged = self.data[donors].apply(np.mean, axis=1)
            data_merged[code] = celltypes_averaged
        self.data = data_merged
        return

    def filter_by_target_celltype_activity(self, threshold=1, donors="all", binarize=True):
        """
        Applies a filter to the Data, retaining only the regulatory elements that are expressed in the celltype of
        interest at >= x TPM, x being the threshold variable.

        :param Union[int, float] threshold: TPM value used to filter the data.
        :param list donors: used to select only a few donors out of all from target celltype.
        :param binarize: Convert target cell type expression to 0 and 1, for values below or above the threshold,
        respectively
        """
        celltype_target = self.ctp_analyse_donors[self.target_ctp]
        if isinstance(celltype_target, (list, tuple, np.ndarray)):
            if donors == "all":
                for donor in celltype_target:
                    self.data = self.data[self.data[donor] >= threshold]
            else:
                for i in donors:
                    donor = celltype_target[i]
                    self.data = self.data[self.data[donor] >= threshold]
        else:
            self.data = self.data[self.data[celltype_target] >= threshold]
        if binarize:
            try:
                self.data[celltype_target] = self.data[celltype_target].applymap(lambda x: 0 if x <= threshold else 1)
            except AttributeError:
                self.data[celltype_target] = self.data[celltype_target].apply(lambda x: 0 if x <= threshold else 1)

    def filter_by_reg_element_sparseness(self, threshold=90):
        """
        Applies a filter to the Data, retaining only the regulatory elements in which xth percentile (x being the
        threshold variable) value is 0 (that is: not expressed).
        This filter will, then, retain only the REs with most 0 TPM for all celltypes.

        :param int threshold: percentile value used to filter the data.
        """
        self.data, column_name = pd_util.df_percentile_calculator(self.data,
                                                                  self.ctp_analyse_donors[self.target_ctp],
                                                                  threshold)
        rows_to_keep = self.data[column_name] == 0
        while sum(rows_to_keep) < 50 and threshold > 5:
            threshold -= 5
            self.data.drop(column_name, axis=1, inplace=True)
            self.data, column_name = pd_util.df_percentile_calculator(self.data,
                                                                      self.ctp_analyse_donors[self.target_ctp],
                                                                      threshold)
            rows_to_keep = self.data[column_name] == 0
        if sum(rows_to_keep) >= 50:
            self.data = pd_util.df_filter_by_column_value(self.data, column_name, value=0)
            self.data.drop(column_name, axis=1, inplace=True)
        else:
            self.data.drop(column_name, axis=1, inplace=True)

    def define_non_target_celltypes_inactivity(self, threshold=0):
        """
        Converts the data to binary (0 - inactive; 1- active) given a threshold.
        :param threshold: Maximum TPM non-target cell types should have to be considered inactive.
        """
        celltypes_nontarget = self.data.columns.difference(self.ctp_analyse_donors[self.target_ctp])
        try:
            self.data[celltypes_nontarget] = self.data[celltypes_nontarget].applymap(
                lambda x: 0 if x <= threshold else 1)
        except AttributeError:
            self.data[celltypes_nontarget] = self.data[celltypes_nontarget].apply(
                lambda x: 0 if x <= threshold else 1)

    def sort_sparseness(self):
        """ Sorts the data by descending sparsest RE """
        self.data["sum"] = self.data.drop(self.ctp_analyse_donors[self.target_ctp], axis=1).sum(
            axis=1)  # create a extra column with the sum of 1s for each row (promoter)
        self.data.sort_values(["sum"], inplace=True)  # sort promoters based on the previous sum. Descending order
        self.data.drop(["sum"], axis=1, inplace=True)  # now remove the sum column

    def add_celltype(self, celltypes, file="custom", sample_types="cell lines",
                     data_type="promoters"):
        """
        Adds expression data for celltypes from other data sets (with similar regulatory element information)

        :param celltypes: celltypes to merge with database
        :param file:
        :param sample_types:
        :param data_type:
        """
        if sample_types == "cell lines":
            supersets = None
        elif sample_types == "primary cells":
            supersets = cv.primary_cells_supersets
        else:
            not_include = None
            supersets = None
        if isinstance(celltypes, str):
            celltypes = [celltypes]
        elif isinstance(celltypes, dict):  # to deal with situations such as mesothelioma cell line
            celltypes = list(celltypes.values())[0]
        if isinstance(file, DataTpm):
            data_new = file.copy()
        else:
            data_new = DataTpm(file=file, sample_types=sample_types, data_type=data_type,
                               nrows=self._nrows)
        data_copy = data_new.copy(deep=True)
        for celltype in celltypes:
            data_new.make_data_celltype_specific(celltype, supersets=supersets)
            data_new.data = data_new.data[data_new.ctp_analyse_donors[celltype]]
            self.data = pd.concat([self.data, data_new.data], axis=1)
            data_new = data_copy.copy(deep=True)

    def remove_celltype(self, celltypes, merged=True):
        """
        Removes a specific celltype from data

        :param celltypes: celltype/s to remove. int or list-type
        :param merged: If the data has been previously merged into celltypes, True. If columns represent donors, False.
        """

        def _remove(to_remove):
            try:
                self.data.drop(to_remove, axis=1, inplace=True)
            except (ValueError, KeyError) as e:
                print("Celltype not removed due to: {}".format(e.args[0]))

        if not merged:
            celltypes_dict = self._code_selector(self.data, celltypes, not_include=self.ctp_not_include,
                                                 to_dict=True, regex=False)
            celltypes = [sub_item for item in list(celltypes_dict.values()) for sub_item in item]
        _remove(celltypes)

    def remove_element(self, elements):
        """
        Removes a specific celltype from data

        :param elements: regulatory element/s to remove. int or list-type
        """
        try:
            self.data.drop(elements, axis=0, inplace=True)
        except ValueError as e:
            print("Regulatory elements not removed due to: {}".format(e.args[0]))

    def drop_target_ctp(self):
        if isinstance(self.target_ctp, list):
            for target in self.target_ctp:
                try:
                    self.data.drop(self.ctp_analyse_donors[target], axis=1, inplace=True)
                except:
                    continue
        else:
            self.data.drop(self.ctp_analyse_donors[self.target_ctp], axis=1, inplace=True)


class Vencodes:
    """
    An Object representing the VEnCodes found for a specific celltype
    """

    def __init__(self, data_object, algorithm, number_of_re=4, n_samples=10000, stop=5, second_data_object=None,
                 using=None):
        """
        :param DataTpm data_object: Must be made celltype specific before calling this method.
        :param str algorithm: algorithm to find VEnCodes. Currently accepted: heuristic, sampling
        :param int n_samples: number of times to try finding a VEnCode. Used only if algorithm = "sampling"
        :param int stop: number of promoters to test per node level. Used only if algorithm = "heuristic
        """
        self._data_object, self.algorithm, self.k = data_object.copy(), algorithm, number_of_re
        self.celltype_donors = self._data_object.ctp_analyse_donors[data_object.target_ctp]
        self.problems, self.vencodes, self.e_values = None, [], {}
        self._parent_path = os.path.join(str(Path(__file__).parents[2]), "VEnCodes")

        self.celltype_donors_data = self._data_object.data[self.celltype_donors]
        self.data = self._data_object.data.copy(deep=True)
        self._data_object.data.drop(self.celltype_donors, axis=1, inplace=True)

        if second_data_object:
            self.second_data_object = second_data_object.copy()
        else:
            self.second_data_object = None

        if self.algorithm is "heuristic":
            self.stop = stop
            self.vencodes_generator = self._heuristic_method_vencode_getter()
        elif self.algorithm is "sampling":
            self.n_samples = n_samples
            self.vencodes_generator = self._sampling_method_vencode_getter(using=using)

    def next(self, amount=1, add_problems=False):
        """
        Call this function to generate the next VEnCode. The VEnCode is appended to the variable self.vencodes, or
        can be returned as a variable.

        :param int amount: number of vencodes to get.
        :return: a list containing the desired amount of vencodes.
        """
        num = 0
        vencode_list = []
        while num < amount:
            duplicate = False
            try:
                vencode = next(self.vencodes_generator)
            except StopIteration:
                return
            if self.vencodes:
                for previous_ven in self.vencodes:
                    if set(previous_ven) == set(vencode):
                        duplicate = True
            if not duplicate:
                num += 1
            if not duplicate and vencode:
                self.vencodes.append(vencode)
                vencode_list.append(vencode)
            else:
                continue
        return vencode_list

    def determine_e_values(self, repetitions=100):
        """
        Call this function to generate e-values for the current VEnCodes. E-values will be stored in the variable
        called e_values. Method applied to calculate e-values is a Monte-Carlo simulation.

        :param int repetitions: number of times each vencode is evaluated to get the average value.
        """

        if self.vencodes is None:
            print("No VEnCodes found yet. Try generating new VEnCodes first with .next()")
            return
        for vencode in self.vencodes:
            if isinstance(vencode[0], list):
                vencode_tuple = tuple([tuple(item) for item in vencode])
                if vencode_tuple in self.e_values.keys():
                    continue
                else:
                    e_value_raw, k = self._e_value_calculator_two_data_sets(vencode, repetitions)
            else:
                vencode_tuple = tuple(vencode)
                if vencode_tuple in self.e_values.keys():
                    continue
                else:
                    e_value_raw = self._e_value_calculator(vencode, repetitions)
                    k = None
            e_value = self._e_value_normalizer(e_value_raw, k=k)
            self.e_values[vencode_tuple] = e_value

    def export(self, *args, **kwargs):
        """
        Call this method to export vencode related values to a .csv file.

        exporting e-values:
        - use "e-values" in the args to export the e-values.
        - Use:
        >> e-values = path
        to define a specific path for the file. (must be a complete path)

        :param args: "e-values", "TPP" or a list/tuple with both.
        :param kwargs: optional args to apply, see description.
        """

        if "e-values" in args and "TPP" not in args:
            path = kwargs.get("path")
            self._export_e_values(path)

        if "e-values" in args and "TPP" in args:
            path = kwargs.get("path")
            self._export_e_values_tpp(path)

    def get_vencode_data(self, method="return", path=None):
        """
        Call this function to get the VEnCode data in .csv format (method="write") or just printed in terminal
        (method="print"), or both (method="both").
        Alternatively, it can return the data to a variable (method="return").

        :param str method: how to retrieve the data.
        :param str path: path to write a file to store the VEnCode data.
        """
        vencodes = []
        for vencode in self.vencodes:
            if method in ("print", "both"):
                print(self.data.loc[vencode])
            if method in ("write", "both"):
                if path is None:
                    path = self._parent_path
                else:
                    pass
                file_name = "{}_vencode".format(self._data_object.target_ctp)
                file_name = d_f_handling.str_replace_multi(
                    file_name, {":": "-", "*": "-", "?": "-", "<": "-", ">": "-", "/": "-"})
                file_path = d_f_handling.check_if_and_makefile(file_name, path=path, file_type=".csv")
                self.data.loc[vencode].to_csv(file_path, sep=';')
                print("File stored in {}".format(file_path))
            elif method == "return":
                vencodes.append(self.data.loc[vencode])
        if method == "return":
            return vencodes

    def view_vencodes(self, method="print", interpolation="nearest", path=None, snapshot=None):
        """
        Call this function to get an heat map visualization of the vencodes.

        :param str method: "print" to get visualization on terminal. "write" to write to a file. "both" for both.
        :param str interpolation: method for heat map interpolation
        :param str path: Optional path for the file.
        :param int snapshot: Number of celltypes to show in heat map. False gets all but may hinder visualization.
        """
        for vencode in self.vencodes:
            self._heatmap(vencode, method=method, interpolation=interpolation, path=path, snapshot=snapshot)

    def next_heuristic2_vencode(self, second_data_object, amount=1):

        """
        Call this function to generate the next VEnCode, possibly hybrid enhancer-promoter VEnCode.
        The VEnCode is appended to the variable self.vencodes.
        :param second_data_object:
        """

        # TODO: needs to get the minimum number of second promoter/enhancers as possible. rn is getting k second RE
        self.second_data_object = second_data_object.copy()
        self.second_data_object.drop_target_ctp()
        sparsest = self._data_object.data.head(n=self.k)
        mask = sparsest != 0
        cols = sparsest.columns[np.all(mask.values, axis=0)].tolist()
        cols_target = second_data_object.ctp_analyse_donors[second_data_object.target_ctp]
        data_problem_cols = second_data_object.data[cols + cols_target]
        second_data_object.data = data_problem_cols
        if self.algorithm == "heuristic":
            vencode_heuristic2 = Vencodes(second_data_object, algorithm="heuristic", number_of_re=self.k,
                                          stop=self.stop)
            vencode_heuristic2.next(amount=amount)
        else:
            raise AttributeError("Algorithm - {} - currently not supported".format(self.algorithm))
        if vencode_heuristic2.vencodes:
            for vencode_second in vencode_heuristic2.vencodes:
                vencode = [sparsest.index.values.tolist(), vencode_second]
                self.vencodes.append(vencode)

    def heuristic2_vencode(self):  # TODO: must implement this within _node_based_algorithm

        """
        Call this function to generate the next VEnCode, possibly hybrid enhancer-promoter VEnCode.
        The VEnCode is appended to the variable self.vencodes.
        """
        # TODO: needs to get the minimum number of second promoter/enhancers as possible. rn is getting k second RE
        sparsest = self._data_object.data.head(n=self.k)
        mask = sparsest != 0
        cols = sparsest.columns[np.all(mask.values, axis=0)].tolist()
        cols_target = self.second_data_object.ctp_analyse_donors[self.second_data_object.target_ctp]
        data_problem_cols = self.second_data_object.data[cols + cols_target]
        self.second_data_object.data = data_problem_cols
        if self.algorithm == "heuristic":
            vencode_heuristic2 = Vencodes(self.second_data_object, algorithm="heuristic", number_of_re=self.k,
                                          stop=self.stop)
            vencode_heuristic2.next()
        else:
            raise AttributeError("Algorithm - {} - currently not supported".format(self.algorithm))
        if vencode_heuristic2.vencodes:
            vencode = [sparsest.index.values.tolist(), vencode_heuristic2.vencodes]
            self.vencodes.append(vencode)

    def _sampling_method_vencode_getter(self, threshold=0,
                                        skip_sparsest=False, using=None):
        """
        Function that searches for a VEnCode in data by the sampling method. Please note that it retrieves a DataFrame
        containing the entire sample. This is the reason why it only retrieves one VEnCode.

        :param int threshold: minimum expression threshold that counts to consider a promoter inactive.
        :param bool skip_sparsest: Allows user to skip first check - check if sparsest REs already constitute a VEnCode.
        :return: a list with the promoters that constitute a VEnCode.
        """
        if not skip_sparsest:
            # try first to see if sparsest REs aren't already a VEnCode:
            sparsest = self._data_object.data.head(n=self.k)
            if self._assess_vencode_one_zero_boolean(sparsest, threshold=threshold):
                yield sparsest.index.values.tolist()
        i = 0

        if using is not None:  # allows user to force some REs to be in the VEnCode
            use = self._data_object.data.loc[using]
            if isinstance(using, list):
                n = self.k - len(using)
            else:
                n = self.k - 1
        else:
            n = self.k

        while i < self.n_samples:
            try:
                sample = self._data_object.data.sample(n=n)  # take a sample of n promoters
            except ValueError as e:  # Combinations number could be larger than number of RE available.
                print("Combinations number (k) is probably larger than the number of RE available. {}".format(
                    e.args))
                break
            if using is not None:
                try:
                    sample.loc[using] = use
                except KeyError:
                    sample = pd.concat([sample, use])
            if self._assess_vencode_one_zero_boolean(sample, threshold=threshold):  # assess if VEnCode
                yield sample.index.values.tolist()
                i = 0
            else:
                i += 1

    def _heuristic_method_vencode_getter(self):
        """
        Function that searches for a VEnCode in data by the heuristic method.
        """
        breaks = {}  # this next section creates a dictionary to update with how many times each node is cycled
        for item in range(1, self.k):
            breaks["breaker_" + str(item)] = 0
        generator = self._node_based_algorithm(breaks=breaks)
        while True:
            try:
                vencode_list = next(generator)
            except StopIteration:
                break
            if vencode_list:
                vencode_list = [item for sublist in vencode_list for item in sublist]
                for i in gen_util.combinations_from_nested_lists(vencode_list):
                    vencode = self._fill_vencode_list(list(i))
                    yield vencode  # We give the first vencode here
                    if len(i) == self.k:
                        continue
                    for prom_sparse in self._data_object.data.index.values:
                        if prom_sparse in vencode:
                            continue
                        for prom_filled in reversed(vencode):
                            if prom_filled in i:
                                continue
                            vencode_copy = vencode.copy()
                            vencode_copy.remove(prom_filled)
                            vencode_copy.append(prom_sparse)
                            yield vencode_copy
            else:
                break
        yield []

    def _node_based_algorithm(self, promoter=False, counter=1, skip=(),
                              breaks=None, data=None):
        """
        Uses node-based approach to search for vencodes in data.

        :param str promoter: Previous promoter name(founder node if first time calling this function).
        :param int counter: Counter is equal to the depth of the current node.
        :param (tuple, list) skip: the promoters to skip when finding a VEnCode.
        :param dict breaks: Dictionary containing keys for the different levels of breaks (one per each combination number)
        and values corresponding to how many times each combination already cycled. dict type
        :return: The VEnCode, in list type, if the algorithm found one.
        """

        def sort_sparseness(data_):
            """
            Sort data by sum of rows
            :param pd.DataFrame data_: data to sort
            """
            data_["sum"] = data_.sum(axis=1)  # create a extra column with the sum of 1s for each row (promoter)
            data_.sort_values(["sum"], inplace=True)  # sort promoters based on the previous sum. Descending order
            data_.drop(["sum"], axis=1, inplace=True)

        vencode_promoters_list = []
        if data is None:
            data_frame = self._data_object.data.copy()
        else:
            data_frame = data
        data_frame.drop(skip, axis=0, inplace=True,
                        errors="ignore")  # drop the promoters previously used to generate vencodes
        if promoter:
            cols = data_frame.loc[promoter] != 0  # create a mask where True marks the celltypes in which the previous
            # node is still expressed
            cols = data_frame.columns[cols]  # apply that mask, selecting the columns that are True
            data_frame = data_frame[cols].drop(promoter,
                                               axis=0)  # apply the selection and take the prom out of the dataframe
            vencode_promoters_list.append(promoter)

        nodes = (data_frame == 0).all(
            axis=1)  # Check if any VEnCode - if any other promoter have 0 expression in all cells
        vencode_node_count = np.sum(nodes)  # if any True (VEnCode) the "True" becomes 1 and sum gives num VEnCodes
        if vencode_node_count > 0:
            vencode_list = data_frame[nodes].index.values.tolist()
            vencode_promoters_list.append(vencode_list)
            yield vencode_promoters_list  # found at least one VEnCode so it can return a successful answer
            vencode_promoters_list = []

        else:  # if in previous node could not get a definite VEnCode, re-start search with next node
            if self.second_data_object:
                pass
            sort_sparseness(data_frame)
            promoters = data_frame.index.values  # get an array of all the promoters, to cycle
            counter = counter  # counter is defined with previous counter for recursive use of this function
            counter_thresholds = [i for i in range(2, (self.k + 1))]  # set maximum number for counter
            # loop the next area until number of nodes in combination exceeds num of desired proms in comb for VEnCode
            while counter < self.k:
                counter += 1  # updates the counter as it will enter the next node depth
                promoters_in_use = (prom for prom in promoters if prom not in skip)
                for prom in promoters_in_use:  # cycle the promoters
                    # region "early quit if loop is taking too long"
                    if breaks is not None and counter in counter_thresholds:
                        breaker_index = str(counter_thresholds.index(counter) + 1)
                        breaks["breaker_" + breaker_index] += 1
                        if breaks[
                            "breaker_" + breaker_index] > self.stop:  # here, we only test x promoters per node level
                            breaks["breaker_" + breaker_index] = 0
                            yield []
                    # endregion "early quit if loop is taking too long"
                    check_if_ven = self._node_based_algorithm(promoter=prom, skip=skip, counter=counter, breaks=breaks,
                                                              data=data_frame)
                    try:
                        vencode_possible = next(check_if_ven)
                    except StopIteration:
                        yield []
                    if vencode_possible:
                        vencode_promoters_list.append(vencode_possible)
                        yield vencode_promoters_list
                        vencode_promoters_list = []
            else:
                vencode_promoters_list = []
            yield vencode_promoters_list

    def _fill_vencode_list(self, vencode_list):
        """
        Given an incomplete list of x REs that make up a VEnCode, it fills the list up, up to y VEnCodes (
        y = RE combinations number), based on next sparse REs.

        :param list vencode_list: a list containing the promoters necessary to establish a vencode.
        :return: A list of y REs that comprise a VEnCode, where y = combinations number.
        """
        assert len(vencode_list) <= self.k, "vencode list len is bigger than wanted RE number"
        if len(vencode_list) == self.k:
            return vencode_list
        for prom in self._data_object.data.index.values:  # next we'll fill the vencode with the top sparse REs
            if prom in vencode_list:
                continue
            vencode_list.append(prom)
            if len(vencode_list) == self.k:
                break
        return vencode_list

    def _e_value_calculator(self, vencode, reps):
        """
        Preps the data to be used in Monte Carlo simulation.

        :param list vencode: one of the VEnCodes found.
        :param int reps: number of times each vencode is evaluated to get the average value.
        :return: e-value, that is, the average number of random changes done to the data that breaks the vencode.
        """

        vencode_data = self._data_object.data.loc[vencode]
        e_value = self.vencode_mc_simulation(vencode_data, reps=reps)
        return e_value

    def _e_value_calculator_two_data_sets(self, vencode, reps):
        """
        Preps the data to be used in Monte Carlo simulation. Used for heuristic2 algorithm.

        :param list vencode: one of the VEnCodes found.
        :param int reps: number of times each vencode is evaluated to get the average value.
        :return: e-value, that is, the average number of random changes done to the data that breaks the vencode.
        """

        vencode_first_data = self._data_object.data.loc[vencode[0]]
        vencode_second_data = self.second_data_object.data.loc[vencode[1]]
        vencode_data = pd.concat([vencode_first_data, vencode_second_data], axis=0)
        e_value = self.vencode_mc_simulation(vencode_data, reps=reps)
        return e_value, vencode_data.shape[0]

    def _heatmap(self, vencode, method="print", interpolation="nearest", path=None, snapshot=None):
        data = self.data.loc[vencode]
        labels = data.index.values
        if snapshot is not None:
            values = eval("data.values[:, -{}:]".format(snapshot))
        else:
            values = data.values
        pylab.imshow(values, interpolation=interpolation, cmap=plt.cm.Reds)
        pylab.yticks(range(values.shape[0]), labels)
        # Print or save to file:
        if not method == "print":
            if path is None:
                path = self._parent_path
            else:
                pass
            file_name = "{}_heat_map".format(self._data_object.target_ctp)
            file_path = d_f_handling.check_if_and_makefile(file_name, path=path, file_type=".png")
        else:
            file_path = None
        if method == "write":
            pylab.savefig(file_path, bbox_inches="tight")
            print("Image stored in {}".format(file_path))
        elif method == "print":
            pylab.show()
        elif method == "both":
            pylab.savefig(file_path, bbox_inches="tight")
            print("Image stored in {}".format(file_path))
            pylab.show()
        else:
            raise AttributeError("method argument is not recognized")

    @staticmethod
    def vencode_mc_simulation(data, reps=100):
        """
        Simulates turning 0s to 1s over a data set and asks if the data still represents a VEnCode.

        :param pd.DataFrame data: Data frame of promoter expression per celltype without the celltype of interest.
        :param int reps: number of simulations to run.
        :return: e_values, that is, the average number of random changes done to the data that breaks the vencode.
        """
        col_list = data.columns.values
        index_list = data.index.values
        simulator = 0
        local_counter_list = []
        while simulator < reps:
            vencode = True
            local_counter = 0
            data_mutable = data.copy()
            while vencode:
                col = random.choice(col_list)
                index = random.choice(index_list)
                if data_mutable.loc[index, col] == 0:
                    local_counter += 1
                    data_mutable.at[index, col] = 1
                    a = data_mutable[col].tolist()
                    try:
                        a.index(0)  # searches for at least one 0 in that column. If there's no 0, it's not a VEnCode.
                    except ValueError:
                        vencode = False
                        local_counter_list.append(local_counter)
                else:
                    pass
            simulator += 1
        global_counter = np.mean(local_counter_list, dtype=np.float64)
        return global_counter

    def _e_value_normalizer(self, e_value_raw, k=None):
        """
        Normalizes the e-value due to disparity in number of celltypes

        :param e_value_raw: value to normalize
        :return: normalized e-value
        """
        if k is None:
            k = self.k

        coefs = {"a": -164054.1, "b": 0.9998811, "c": 0.000006088948, "d": 1.00051, "m": 0.9527, "e": -0.1131}
        e_value_expected = (coefs["m"] * k + coefs["e"]) * self._data_object.data.shape[1] ** (
                coefs["d"] + ((coefs["a"] - coefs["d"]) / (1 + (k / coefs["c"]) ** coefs["b"])))
        e_value_norm = (e_value_raw / e_value_expected) * 100
        if e_value_norm < 100:
            return e_value_norm
        else:
            return 100

    @staticmethod
    def _assess_vencode_one_zero_boolean(sample, threshold=0):
        """
        Returns True if sample represents a VEnCodes for a celltype not in "sample". It assumes VEnCodes when all
        other celltypes have at least one promoter not expressing. It's the quickest VEnCode assessing algorithm.
        """
        if threshold == 0:
            assess_if_vencode = np.any(sample == 0, axis=0)  # list of True if column has any 0
        elif threshold > 0:
            assess_if_vencode = np.any(sample <= threshold, axis=0)
        else:
            raise ValueError("Threshold for VEnCode assessment is not valid.")
        return all(assess_if_vencode)  # if all columns are True (contain at least one 0), then is VEn

    def _export_e_values(self, path=None):
        """
        Call this method to export E-values to a .csv file.
        Use path to define a specific path for the file. (must be a complete path)
        :param str path: Complete path to store the file.
        """
        if not self.e_values:
            self.determine_e_values()
        if path is None:
            path = self._parent_path
        file_name = "{}_evalues".format(self._data_object.target_ctp)
        file_name = d_f_handling.str_replace_multi(
            file_name, {":": "-", "*": "-", "?": "-", "<": "-", ">": "-", "/": "-"})
        file_path = d_f_handling.check_if_and_makefile(file_name, path=path, file_type=".csv")
        d_f_handling.write_one_value_dict_to_csv(file_path, self.e_values)
        print("File stored in: {}".format(file_path))


class OutsideData:
    """
    Base class for all data from outside sources.
    """

    def __init__(self, folder=None):
        if folder is None:
            folder = "Validation_files"
        self.data_path = os.path.join(str(Path(__file__).parents[2]), "Files", folder)
        self._data_source = None
        self.data = None

    @property
    def data_source(self):
        """
        File name of the data.
        :return: File name of the data
        """
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        if value.endswith((".broadPeak", ".BED", ".txt", ".FASTA", ".fasta", ".csv")):
            self._data_source = value
        else:
            if value == "DennySK2016":
                self._data_source = "GSE81255_all_merged.H14_H29_H52_H69_H82_H88_peaks.broadPeak"
            elif value == "InoueF2017":
                self._data_source = "supp_gr.212092.116_Supplemental_File_2_liverEnhancer_design.tsv"
            elif value == "BarakatTS2018":
                self._data_source = ["Barakat et al 2018 - Core and Extended Enhancers.csv",
                                     "Barakat et al 2018 - Merged Enhancers.csv"]
            elif value == "ChristensenCL2014":
                self._data_source = ["1-s2.0-S1535610814004231-mmc3_GLC16.csv",
                                     "1-s2.0-S1535610814004231-mmc3_H82.csv",
                                     "1-s2.0-S1535610814004231-mmc3_H69.csv"]
            elif value == "WangX2018":
                self._data_source = "41467_2018_7746_MOESM4_ESM.txt"
            elif value == "LiuY2017":
                self._data_source = "GSE82204_enhancer_overlap_dnase.txt"
            elif value.startswith("EnhancerAtlas-"):
                self._data_source = "{}.fasta".format(value.split("-", 1)[1])
            else:
                raise AttributeError("Source {} still not implemented".format(value))

    def join_data_sets(self, data_set):
        """
        Joins the data from this source with data from a different source. The result is a filtered data set with
        just the genomic coordinates that are overlapping in both data sets.
        :param data_set: the data set to merge with.
        """
        union = {"Chromosome": [], "range": []}
        for index, row in self.data.iterrows():
            range1 = row.range
            data2_filter_chr = data_set.data[data_set.data["Chromosome"] == row.Chromosome]
            range2_list = data2_filter_chr["range"].tolist()
            for range2 in range2_list:
                condition = gen_util.partial_subset_of_span(range1, range2)
                if condition:
                    temp_chr, temp_rng = union["Chromosome"], union["range"]
                    temp_chr.append(row.Chromosome)
                    temp_rng.append(self._range_union(range1, range2))
                    union["Chromosome"] = temp_chr
                    union["range"] = temp_rng
                    break
        df = pd.DataFrame.from_dict(union)
        self.data = df

    @staticmethod
    def _range_union(range1, range2):
        values = [x for x in range1]
        values2 = [y for y in range2]
        values += values2
        range_union = [min(values), max(values)]
        return range_union

    def _open_csv_file(self, file_name, sep=";", header="infer", usecols=None, names=None):
        file_path = os.path.join(self.data_path, file_name)
        file_data = pd.read_csv(file_path, sep=sep, header=header, engine="python", usecols=usecols, names=names)
        return file_data

    def _merge_cell_type_files(self):
        enhancer_data_merged = None
        for source in self.data_source:
            enhancer_data = self._open_csv_file(source)
            if enhancer_data_merged is not None:
                enhancer_data_merged = pd.concat([enhancer_data_merged, enhancer_data])
            else:
                enhancer_data_merged = enhancer_data
        return enhancer_data_merged

    def _create_range(self):
        self.data["range"] = [[row.Start, row.End] for index, row in self.data.iterrows()]


class BarakatTS2018Data(OutsideData):
    """
    Data from Barakat, et al., Cell Stem Cell, 2018.
    Parsed to use in VEnCode validation studies.

    How to use: data = internals.BarakatTS2018Data(**kwargs)
    kwargs can be empty, or used to get only part of the data, by using the kwarg: data="core" for example.
    data available are: core and extended enhancers, merged enhancers. Check Barakat, et al., Cell Stem Cell, 2018.
    """

    def __init__(self, source="BarakatTS2018", **kwargs):
        super().__init__()
        self.data_source = source

        try:
            source_partial = kwargs["data"]
            enhancer_file = next((s for s in self.data_source if source_partial.lower() in s.lower()), None)
            self.data = self._open_csv_file(enhancer_file)
        except KeyError:
            self.data = self._merge_cell_type_files()

        gen_util.clean_whitespaces(self.data, "Start", "End")
        pd_util.columns_to_numeric(self.data, "Start", "End")
        self._create_range()


class InoueF2017Data(OutsideData):
    """
        Data from Inoue F, et al., Genome Res., 2017.
        Parsed to use in VEnCode validation studies.

        How to use: data = internals.InoueF2017Data()
        """

    def __init__(self, source="InoueF2017"):
        super().__init__()
        self.data_source = source
        self.data = self._open_csv_file(self.data_source, sep="\t", header=None, names=["temp", "sequence"])
        self._data_cleaner()

    @staticmethod
    def search_between_brackets(string):
        """
        Gets all text between the first [] in a string.
        :param string: String to search for text.
        :return: All text between []
        """
        try:
            return re.search("(?<=\[)(.*)(?=\])", string).group(1)
        except AttributeError:
            pass

    def _genome_location_to_cols(self):
        self.data[["Chromosome", "temp"]] = self.data.temp.str.split(":", expand=True)
        self.data[["Start", "End"]] = self.data.temp.str.split("-", expand=True)
        self.data = self.data[["Chromosome", "Start", "End"]]

    def _genome_location_cleaner(self):
        self.data["temp"] = self.data["temp"].apply(self.search_between_brackets)
        self.data.drop_duplicates("temp", inplace=True)
        self.data.dropna(inplace=True)

    def _data_cleaner(self):
        self._genome_location_cleaner()
        self._genome_location_to_cols()
        pd_util.columns_to_numeric(self.data, "Start", "End")
        self._create_range()


class ChristensenCL2014Data(OutsideData):
    """
    Parses data from Christensen CL, et al., Cancer Cell, 2014, to use in VEnCode validation studies.

    How to use: data = internals.ChristensenCL2014Data(**kwargs)
    kwargs can be empty, or used to get only part of the data, by using the kwarg: data="H82" for example.
    data available are: GLC16, H82, and H69.
    """

    def __init__(self, source="ChristensenCL2014", **kwargs):
        super().__init__()
        self.data_source = source

        try:
            source_partial = kwargs["data"]
            enhancer_file = next((s for s in self.data_source if source_partial.lower() in s.lower()), None)
            self.data = self._open_csv_file(enhancer_file)
        except KeyError:
            self.data = self._merge_cell_type_files()

        self._data_cleaner()

    def _sort_data(self):
        self.data.sort_values(by=["Start"], inplace=True)

    def _data_cleaner(self):
        self._sort_data()
        self.data.rename({"Chrom": "Chromosome", "Stop": "End"}, axis='columns', inplace=True)
        self._create_range()


class BroadPeak(OutsideData):
    """
    Parses data from BroadPeak files to use in VEnCode validation studies.

    How to use: data = internals.BroadPeak(source)
    source can be any source described in baseclass, or a filename ending in .broadPeak
    """

    def __init__(self, source=False):
        super().__init__()
        self.data_source = source
        names = ["Chromosome", "Start", "End", "Name", "Score", "Strand", "SignalValue",
                 "pValue", "qValue"]
        use_cols = range(0, len(names))
        self.data = self._open_csv_file(self.data_source, sep="\t", header=None, usecols=use_cols,
                                        names=names)
        self._data_cleaner()

    def _data_cleaner(self):
        self.data = self.data[["Chromosome", "Start", "End", "Score"]]
        self._create_range()


class Bed(OutsideData):
    """
    Parses data from BED files to use in VEnCode validation studies.

    How to use: data = internals.Bed(source)
    source can be any source described in baseclass, or a filename ending in .BED
    """

    def __init__(self, source=False):
        super().__init__()
        if source:
            self.data_source = source
        names = ["Chromosome", "Start", "End"]
        use_cols = range(0, len(names))
        self.data = self._open_csv_file(self.data_source, sep="\t", header=None, usecols=use_cols,
                                        names=names)

        self._data_cleaner()

    def _data_cleaner(self):
        self.data = self.data[["Chromosome", "Start", "End"]]
        self._create_range()


class Fasta(OutsideData):
    """
    Parses data from FASTA files to use in VEnCode validation studies.

    How to use: data = internals.Fasta(source)
    source can be any source described in baseclass, or a filename ending in .Fasta, .Fa, .txt, etc.
    """

    def __init__(self, source=False):
        super().__init__()
        if source:
            self.data_source = source
        file_path = os.path.join(self.data_path, self.data_source)
        fasta_sequences = SeqIO.parse(open(file_path), 'fasta')
        self._data_cleaner(fasta_sequences)

    def _data_cleaner(self, sequences):
        array = None
        for fasta in sequences:
            name = fasta.id
            name = name.split(':')
            chromosome, locations = name[0], name[1].split("-")
            start, end = locations[0], locations[1]
            end = re.match(r"[0-9]+", end).group()
            info = [[chromosome, start, end]]
            try:
                array = np.append(array, info, axis=0)
            except ValueError:
                array = np.array(info)
        columns = ["Chromosome", "Start", "End"]
        self.data = pd.DataFrame(array, columns=columns)
        pd_util.columns_to_numeric(self.data, "Start", "End")
        self._create_range()


class Csv(OutsideData):
    """
        Parses data from CSV files to use in VEnCode validation studies.

        How to use: data = internals.Csv(source)
        source can be any source described in baseclass, or a filename ending in .csv.
        """

    def __init__(self, source=False, positions=(0, 0, 0, 1), splits=(":", "-")):
        super().__init__(folder="Single Cell analysis")
        if source:
            self.data_source = source
        self.data = self._open_csv_file(self.data_source, sep=";")
        self._data_cleaner(positions, splits)
        pd_util.columns_to_numeric(self.data, "Start", "End")
        self._create_range()

    def _data_cleaner(self, positions, splits):
        data_final = pd.DataFrame()
        columns = ["Chromosome", "Start", "End", "tpm"]
        split_count = 0
        for item, count in Counter(positions).items():
            if count > 1:
                data_to_split = self.data.iloc[:, item]
                for i in range(count - 1):
                    data_temp = data_to_split.str.split(splits[split_count], n=1, expand=True)
                    if columns[split_count] not in data_final.columns:
                        data_final[columns[split_count]] = data_temp[0]
                    if count == i+2:
                        data_final[columns[split_count + 1]] = data_temp[1]
                    else:
                        data_final[columns[split_count + 1]] = data_temp[1].str.split(splits[split_count + 1], n=1,
                                                                                      expand=True)[0]
                    split_count += 1
            else:
                position = positions.index(item)
                data_final[columns[position]] = self.data.iloc[:, item]
        self.data = data_final


class DataTpmValidated(DataTpm):
    """
    This class provides methods to develop a data set with chromosome coordinates intercepted
    with those of validate_with, which we call validated regulatory elements.

    How to use: After initializing, filter data with validated REs by calling the "filter_validated" method.
    """

    def __init__(self, validate_with, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate_with = validate_with

    def select_validated(self):
        """
        Main method to filter the REs in the data, leaving in the data only those that match the external data set.
        """
        df_range = self._regulatory_elements_range()
        self._interception(df_range, self.validate_with.data, self.data)

    def merge_external_cell_type(self, cell_type):
        df_range = self._regulatory_elements_range()
        self.data = self._interception(df_range, self.validate_with.data, self.data)
        validate_with = self._interception(self.validate_with.data, df_range, self.validate_with.data)
        if self.data.shape[0] == validate_with.shape[0]:
            validate_with.index = self.data.index
            self.data[cell_type] = validate_with["tpm"]
        else:
            self.data[cell_type] = pd.Series(data=[50]*len(self.data.index), index=self.data.index)

    def _interception(self, data1, data2, data_updated):
        mask = self._mask(data1, data2)
        data_updated = data_updated.loc[mask]
        return data_updated

    def _regulatory_elements_range(self):
        df_temp = pd.DataFrame()
        df_temp["Id"] = self.data.index
        df_temp[["Chromosome", "temp"]] = df_temp.Id.str.split(":", expand=True)
        df_temp[["Start", "End"]] = df_temp.temp.str.split("-", expand=True)
        df_temp = df_temp[["Chromosome", "Start", "End"]]
        pd_util.columns_to_numeric(df_temp, "Start", "End")
        df_temp["range"] = [[row.Start, row.End] for index, row in df_temp.iterrows()]
        return df_temp

    @staticmethod
    def _mask(df, df2):
        mask = []
        for index, row in df.iterrows():
            range1 = row.range
            data2_filter_chr = df2[df2["Chromosome"] == row.iloc[0]]
            range2_list = data2_filter_chr["range"].tolist()
            switch = False
            for range2 in range2_list:
                condition = gen_util.partial_subset_of_span(range1, range2)
                if condition:
                    mask.append(True)
                    switch = True
                    break
            if not switch:
                mask.append(False)
        return mask
