#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" classes.py: Classes module for the VEnCode project """

import inspect
import itertools as iter
import logging
import os
import re
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy.special import comb
from tqdm import tqdm

import utils.directory_handlers as dhs
import utils.writing_files as writing_files
import utils.util as util
import utils.exception_handlers as ehs


class DatabaseOperations:
    """ A class with classes for each type of database and common methods to all """

    def __init__(self, file, celltype, celltype_exclude=None, not_include=None, sample_types="primary cells",
                 skiprows=None, second_parser=None, nrows=None, log_level="DEBUG", skip_raw_data=False):
        self.file = file
        self.celltype = celltype
        self.celltype_exclude = celltype_exclude
        self.not_include = not_include
        self.log_level = self._set_log_level(log_level)
        self.sample_types = sample_types
        self.second_parser = second_parser
        self.parent_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "Files")
        if not skip_raw_data:
            # First, import only the necessary data
            self.raw_data = pd.read_csv(os.path.join(self.parent_path, self.file), sep="\t", index_col=0,
                                        skiprows=skiprows,
                                        nrows=nrows, engine="python")
        else:
            self.raw_data = pd.read_csv(os.path.join(self.parent_path, self.file), sep="\t", index_col=0,
                                        skiprows=skiprows,
                                        nrows=4, engine="python")

    @staticmethod
    def sample_category_selector(sample_types_file, types, path="parent", get="index"):
        """
        Returns a list of cell types to keep/drop from a file containing the list of cell types and a 'Sample category'
        column which determines which cell types to retrieve.
        """
        if not isinstance(types, list): types = [types]
        if path == "parent":
            parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            database = pd.read_csv(parent_path + "/Files/" + sample_types_file, sep=",", index_col=0, engine="python")
        elif path == "normal":
            database = pd.read_csv("./Files/" + sample_types_file, sep=",", index_col=0)
        else:
            raise Exception("path type is not recognized")
        try:
            possible_types = database["Sample category"].drop_duplicates().values.tolist()
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            raise
        assert all(
            sample in possible_types for sample in types), "Sample type is not valid.\nValid sample types: {}".format(
            possible_types)
        celltypes = []
        for sample in types:
            selected = database[database["Sample category"] == sample]
            if get == "index":
                [celltypes.append(value) for value in selected.index.values]
            elif get == "name":
                [celltypes.append(value) for value in selected["Name"].tolist()]
            else:
                pass
        return celltypes

    @staticmethod
    def dataframe_regex_searcher(string, database):  # NOTE: Moved to pandas_utils.py
        """ Returns a list containing only the columns of a dataframe which contain the string somewhere
        in its label """
        regular = ".*" + string.replace(" ", ".*").replace("+", "%2b") + ".*"
        idx = database.columns.str.contains(regular, flags=re.IGNORECASE, regex=True, na=False)
        regex_filtered_df = database.loc[:, idx]
        regex_filtered = regex_filtered_df.columns.values.tolist()
        return regex_filtered

    @staticmethod
    def _test_codes(codes, celltype, codes_type="list"):
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

    @staticmethod
    def _set_log_level(level):
        """
        Sets level for logging handler based on user input string.
        :param level: string representation of a logging level
        :return: logging module level
        """
        if level.lower() == "critical":
            level = logging.CRITICAL
        elif level.lower() == "error":
            level = logging.ERROR
        elif level.lower() == "warning":
            level = logging.WARNING
        elif level.lower() == "info":
            level = logging.INFO
        elif level.lower() == "debug":
            level = logging.DEBUG
        elif level.lower() == "notset":
            level = logging.NOTSET
        else:
            raise Exception("Invalid logging level")
        return level

    @staticmethod
    def logging(specific_path):
        parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        logging.basicConfig(filename=parent_path + specific_path, level=logging.DEBUG,
                            format="{asctime} - {levelname} - {message}", filemode='w', style="{")
        logger = logging.getLogger(__name__)
        return logger

    @staticmethod
    def sorted_ven_robustness_test(data, codes, celltype, combinations_number, samples_to_take, reps, file_type,
                                   threshold=90, expression=1, multi_plot=False,
                                   include_problems=False, folder="/Figure 1/"):
        if not isinstance(combinations_number, list):
            combinations_number_list = range(1, combinations_number + 1)
        else:
            combinations_number_list = combinations_number
        filter_2 = util.df_filter_by_expression_and_percentile(data, codes, expression, 2, threshold)
        if include_problems:
            k_ven_percent, problems = util.vencode_percent_sampling(codes, celltype, filter_2,
                                                                    combinations_number_list,
                                                                    samples_to_take,
                                                                    reps, include_problems=include_problems)
        else:
            k_ven_percent = util.vencode_percent_sampling(codes, celltype, filter_2, combinations_number_list,
                                                          samples_to_take,
                                                          reps, include_problems=include_problems)
        # Saving to csv or plotting:
        folder = folder
        if not multi_plot:  # multi_plot is there in case this function is used to generate other plots after.
            file_name = u"/VEnC - {1:s} - {2:s} - exp bigger or = {4:d} - {3:d}x {0:d} samples of k".format(
                samples_to_take, file_type, celltype, reps, expression)
            title = "Probability of VEnCode from sample of size k \n {0:s} expression >= {1:d}".format(
                celltype, expression)
            writing_files.write_dict_to_csv(file_name + ".csv", k_ven_percent, folder)
            fig, path = util.errorbar_plot(k_ven_percent, folder, file_name, label=celltype, title=title)
            fig.savefig(path)
        if include_problems:
            logging.info("{}: {}".format(celltype, problems))
            new_file_name = u"/Probs for {} - {}x {} samples of k-{}".format(celltype, reps, samples_to_take,
                                                                             combinations_number)
            writing_files.write_dict_to_csv(new_file_name + ".csv", problems, folder, path="parent")
        return k_ven_percent

    def not_include_code_getter(self, not_include, df):
        if isinstance(not_include, list):
            not_codes = []
            for item in not_include:
                not_codes_item = self.dataframe_regex_searcher(item, df)
                not_codes.append(not_codes_item)
            not_codes = [item for sublist in not_codes for item in sublist]
        else:
            not_codes = self.dataframe_regex_searcher(not_include, df)
        return not_codes

    def non_combinatory_loop(self, class_instance, combinations_number, expression, threshold, multi=False,
                             mode="count"):
        # Start the loop through all cell types:
        calculated_vencodes = {}
        for celltype in self.celltype:
            print("", "Starting {}".format(celltype), sep="-> ")
            logging.info("Starting %s", celltype)
            codes = class_instance.codes.get(celltype)
            filter_2 = util.df_filter_by_expression_and_percentile(class_instance.data, codes, expression, 2,
                                                                   threshold)
            filter_2 = filter_2.applymap(lambda x: 0 if x == 0 else 1)  # change expression to 1 and 0 for quickness
            nodes = util.node_calculator(filter_2.drop(codes, axis=1))  # the time consumer!
            if multi:
                for number in range(2, combinations_number + 1):
                    try:
                        calculated_vencodes[number]
                    except KeyError:
                        calculated_vencodes[number] = []
                    ven_combinations = util.number_of_combination_from_nodes(nodes, len(filter_2.index), number)
                    logging.info("Number of VEnCodes found: %s for k=%s", ven_combinations, number)
                    if mode == "count":
                        calculated_vencodes[number].append(ven_combinations)
                    elif mode == "percentage":
                        total_comb = comb(len(filter_2.index), combinations_number, exact=False)
                        calculated_vencodes[number] = ven_combinations / total_comb * 100
            else:
                ven_combinations = util.number_of_combination_from_nodes(nodes, len(filter_2.index),
                                                                         combinations_number)
                logging.info("Number of VEnCodes found: %s for k=%s", ven_combinations, combinations_number)
                if mode == "count":
                    calculated_vencodes[celltype] = ven_combinations
                elif mode == "percentage":
                    total_comb = comb(len(filter_2.index), combinations_number, exact=False)
                    calculated_vencodes[celltype] = ven_combinations / total_comb * 100
        return calculated_vencodes

    def at_least_one_vencode(self, class_instance, combinations_number, expression, threshold):
        # Start the loop through all cell types:
        vencodes = {}
        for celltype in self.celltype:  # start by cycling through the celltypes to find a VEnCode
            print("", "Starting {}".format(celltype), sep="-> ")
            logging.info("Starting %s", celltype)
            vencodes[celltype] = 0  # init the dict to append a possible VEnCode
            codes = class_instance.codes.get(celltype)  # get codes for this celltype
            try:  # this next section can remove some celltypes from the data just in time before the analysis
                if class_instance.partial_exclude_codes is not None:
                    if celltype in class_instance.partial_exclude_codes.keys():
                        partial_exclude_codes = class_instance.partial_exclude_codes.get(celltype)
                        data_frame = class_instance.data.drop(partial_exclude_codes, axis=1)
                    else:
                        data_frame = class_instance.data
            except AttributeError:
                data_frame = class_instance.data
            try:
                filter_2 = util.df_filter_by_expression_and_percentile(data_frame, codes, expression, 2,
                                                                       threshold)  # apply efficiency filters
            except KeyError:
                data_frame = data_frame.join(class_instance.codes_df[codes])
                filter_2 = util.df_filter_by_expression_and_percentile(data_frame, codes, expression, 2, threshold)
                filter_2.drop(codes, axis=1, inplace=True)
            filter_2 = filter_2.applymap(lambda x: 0 if x == 0 else 1)  # change expression to 1s and 0s for quickness
            filter_2["sum"] = filter_2.sum(axis=1)  # create a extra column with the sum of 1s for each row (promoter)
            filter_2.sort_values(["sum"], inplace=True)  # sort promoters based on the previous sum. Descending order
            to_get_nodes = filter_2.drop(codes + ["sum"], axis=1)  # remove the celltype to analyse and the sum column
            promoters = to_get_nodes.index.values  # get a list (not really a list) of all the promoters, to cycle
            breaks = {}  # this next section creates a dictionary to update with how many times each node is cycled
            for item in range(1, combinations_number):
                breaks["breaker_" + str(item)] = 0
            for promoter in promoters:  # cycle the promoters, starting with these of lower sum of 1s. Founder node.
                """
                Finally, start cycling through nodes - promoters - used one at a time to combine with preceding and 
                subsequent nodes with the purpose of finding a VEnCode - a combination of promoters where 
                for every celltype there's at least one promoter of that combination that does not exhibit any activity
                """
                vencodes_from_nodes = self.at_least_one_node_calculator(to_get_nodes, promoter,
                                                                        combinations_number=combinations_number,
                                                                        breaks=breaks)
                if vencodes_from_nodes > 0:
                    vencodes[celltype] = 1  # if at least one VEnCode was found with the node strategy, return 1
                    break  # and stop the cycling of the founder nodes
                else:
                    to_get_nodes.drop(promoter, axis=0, inplace=True)  # else, drop this founder node and go to next
        return vencodes

    def at_least_one_node_calculator(self, data_frame, promoter, combinations_number=4, counter=1, breaks=None,
                                     get_vencode=False):
        """

        :param data_frame: Data frame containing cage-seq expression profile for several celltypes. Dataframe object
        :param promoter: Previous promoter name(founder node if first time calling this function). str type
        :param combinations_number: Number of combinations of promoters to find VEnCodes. int type
        :param counter: Counter is equal to the depth of the current node. int type
        :param breaks: Dictionary containing keys for the different levels of breaks (one per each combination number)
        and values corresponding to how many times each combination already cycled. dict type
        :param get_vencode: True if you want to return the list of promoters that constitute a VEnCode.
        :return: If the algorithm found a definite VEnCode or not.
        """
        cols = data_frame.loc[promoter] != 0  # create a mask where True marks the celltypes in which the previous
        # node is still expressed
        cols = data_frame.columns[cols]  # apply that mask, selecting the columns that are True
        new_df = data_frame[cols].drop(promoter, axis=0)  # apply the selection and take the prom out of the dataframe
        nodes = (new_df == 0).all(axis=1)  # Check if any VEnCode - if any other promoter have 0 expression in all cells
        node_count = np.sum(nodes)  # if any True (VEnCode) the value of that True becomes 1 and sum gives num VEnCodes
        if get_vencode:
            if isinstance(get_vencode, list):
                get_vencode.append(promoter)
            else:
                get_vencode = [promoter]
        if node_count > 0:
            if not get_vencode:
                return node_count  # found at least one VEnCode so it can return a successful answer
            else:
                return get_vencode
        else:  # if in previous node could not get a definite VEnCode, re-start search with next node
            new_df["sum"] = new_df.sum(axis=1)  # create a extra column with the sum for each row (promoter)
            new_df.sort_values(["sum"], inplace=True)  # sort promoters based on the previous sum. Descending order
            new_df = new_df.drop(["sum"], axis=1)  # now remove the sum column
            counter = counter  # counter is defined with previous counter for recursive use of this function
            counter_thresholds = [i for i in range(2, (combinations_number + 1))]  # set maximum number for counter
            # loop the next area until number of nodes in combination exceeds num of desired proms in comb for VEnCode
            while counter < combinations_number:
                counter += 1  # updates the counter as it will enter the next node depth
                for prom in new_df.index.values:  # next promoter
                    # region "early quit if loop is taking too long"
                    if counter in counter_thresholds:
                        breaker_index = str(counter_thresholds.index(counter) + 1)
                        breaks["breaker_" + breaker_index] += 1
                        if breaks["breaker_" + breaker_index] == 3:  # here, we only test x promoters per node level
                            node_count = 0
                            breaks["breaker_" + breaker_index] = 0
                            return node_count
                    # endregion "early quit if loop is taking too long"
                    node_count = self.at_least_one_node_calculator(new_df, prom,
                                                                   combinations_number=combinations_number,
                                                                   counter=counter, breaks=breaks,
                                                                   get_vencode=get_vencode)
                    try:
                        if node_count > 1:
                            return node_count
                    except TypeError:
                        node_count = 0
                        continue
            return node_count


class Promoters(DatabaseOperations):
    """ A class describing the methods for the promoters database """

    def __init__(self, file, celltype, celltype_exclude=None, not_include=None, partial_exclude=None,
                 sample_types="primary cells", skiprows=1831, second_parser=None, nrows=None, conservative=False,
                 log_level="DEBUG", enhancers=None, ram_saving=True, skip_raw_data=False):
        super().__init__(file, celltype, celltype_exclude=celltype_exclude, not_include=not_include,
                         sample_types=sample_types, skiprows=skiprows, second_parser=second_parser, nrows=nrows,
                         log_level=log_level, skip_raw_data=skip_raw_data)
        self.enhancers = enhancers
        if enhancers:
            self.data_type = "enhancers"
        else:
            self.data_type = "promoters"
        if self.enhancers:
            self.names_db = pd.read_csv(os.path.join(self.parent_path, enhancers), sep="\t", index_col=1, header=None,
                                        names=["celltypes"], engine="python")
            column_names = {}
            for column_code in self.raw_data.columns:
                column_names[column_code] = self.names_db.loc[column_code, "celltypes"]
            self.raw_data.rename(columns=column_names, inplace=True)
        self.data = self._first_parser()
        self.codes = self._code_selector(self.data, self.celltype, not_include=self.not_include,
                                         to_dict=True, regex=False if enhancers else True)
        self.conservative = conservative
        if self.second_parser is not None:
            temp_codes = [x for a in self.codes.values() for x in a]
            self.codes_df = self.data.filter(items=temp_codes)
            self.sample_types = self.second_parser
            self.data = self._first_parser()
            self.data = pd.concat([self.data, self.codes_df], axis=1)
        if partial_exclude and (enhancers is None):
            self.partial_exclude_codes = {}
            for key, value in partial_exclude.items():
                self.partial_exclude_codes[key] = self._code_selector(self.data, value[0], not_include=value[1])
        if ram_saving:
            self.raw_data = None  # for RAM optimization only, remove if raw_data is needed
        if skip_raw_data:
            self.skip_raw_data = skip_raw_data
            self.conservative = False
            self.path_parsed_data = os.path.join(self.parent_path, "Dbs")

    def _first_parser(self):
        data_1 = self.raw_data.drop(self.raw_data.index[[0, 1]])
        universal_rna = self._code_selector(data_1, "universal", not_include=None)
        data_1.drop(universal_rna, axis=1, inplace=True)
        if self.enhancers is None:
            to_keep = self.sample_category_selector("sample types - FANTOM5.csv", self.sample_types)
        else:
            to_keep = self.sample_category_selector("sample types - FANTOM5.csv", self.sample_types, get="name")
        data = pd.DataFrame(index=data_1.index.values)
        for sample in to_keep:
            if self.enhancers is None:
                data_temp = data_1.filter(regex=sample)
            else:
                try:
                    data_temp = data_1.loc[:, sample]
                except KeyError:
                    data_temp = util.df_minimal_regex_searcher(sample, data_1)
            data = data.join(data_temp)
        # Exclude some specific, on-demand, cell-types from the data straight away:
        if self.celltype_exclude is not None:
            codes_exclude = self._code_selector(data, self.celltype_exclude)
            data.drop(codes_exclude, axis=1, inplace=True)
        return data

    def _code_selector(self, db, celltype, not_include=None, to_dict=False, regex=True):
        """ Selects codes from database using """
        if isinstance(celltype, list):
            codes = []
            if to_dict:
                code_dict = {}
            for item in celltype:
                codes_df = util.df_regex_searcher(item, db) if regex else util.df_minimal_regex_searcher(item, db)
                codes.append(codes_df.columns.values)
                if to_dict:
                    code_dict[item] = [code for sublist in codes for code in sublist]
                    codes = []
            if not to_dict:
                codes = [item for sublist in codes for item in sublist]
        else:
            codes_df = util.df_regex_searcher(celltype, db) if regex else util.df_minimal_regex_searcher(celltype, db)
            codes = list(codes_df.columns.values)
            code_dict = {celltype: codes}
        if not_include is not None:
            if isinstance(not_include, dict):
                codes = code_dict
                for key, values in not_include.items():
                    if key not in code_dict.keys():
                        continue
                    codes_df = db[code_dict.get(key)]
                    not_codes = self.not_include_code_getter(values, codes_df)
                    codes[key] = list(set(code_dict[key]) - set(not_codes))
            else:
                not_codes_df = util.df_regex_searcher(not_include,
                                                      codes_df) if regex else util.df_minimal_regex_searcher(
                    not_include, codes_df)
                not_codes = not_codes_df.columns.values
                if not codes:
                    codes = [item for sublist in code_dict.values() for item in sublist]
                codes = list(set(codes) - set(not_codes))
        self._test_codes(codes, celltype)
        return codes

    def merge_donors_into_celltypes(self, exclude=None):
        """
        Applies a more conservative, but faster approach to data set mining:
        cell type columns are created by merging all donors for that cell type. Merging is done by calculating the
        average of all donors.
        :param exclude: celltypes to exclude from this merging.
        """
        if exclude is not None:
            codes = self.codes.copy()
            codes.pop(exclude, None)
            data_merged = pd.DataFrame(index=self.data.index.values, columns=[key for key in codes.keys()])
            data_merged = pd.concat([data_merged, self.data[self.codes[exclude]]], axis=1)
        else:
            codes = self.codes.copy()
            data_merged = pd.DataFrame(index=self.data.index.values, columns=[key for key in codes.keys()])
        for code, donors in codes.items():
            celltypes_averaged = self.data[donors].apply(np.mean, axis=1)
            data_merged[code] = celltypes_averaged
        return data_merged

    # Promoter specific util methods

    def filter_prep_sort_drop_codes(self, codes, threshold_activity, threshold_sparseness, threshold_inactivity=0):
        """

        :param codes: Codes of the cell type to get VEnCode for.
        :param threshold_activity: minimum expression threshold that counts to consider a promoter active
        :param threshold_sparseness:
        :param threshold_inactivity: minimum expression threshold that counts to consider a promoter inactive
        :return: DataFrame without the cell type of interest, filtered by wanted-celltype threshold of expression,
        non-wanted cell type threshold of expression and sparseness. Also, the data has been converted to 1s and 0s.
        """
        try:
            data_filtered = util.df_filter_by_expression_and_percentile(self.data, codes, threshold_activity, 2,
                                                                        threshold_sparseness)
        except KeyError:
            data_frame = pd.concat([self.data, self.codes_df], axis=1)
            data_filtered = util.df_filter_by_expression_and_percentile(data_frame, codes, threshold_activity, 2,
                                                                        threshold_sparseness)
        data_filtered = data_filtered.drop(codes, axis=1, errors="ignore")
        # change expression to 1s and 0s for quickness:
        if threshold_inactivity == 0:
            data_filtered = data_filtered.applymap(lambda x: 0 if x == 0 else 1)
        elif threshold_inactivity > 0:
            data_filtered = data_filtered.applymap(lambda x: 0 if x <= threshold_inactivity else 1)
        else:
            raise ValueError("Threshold for non-wanted cell type expression is not valid.")
        data_final = self.prep_sort(data_filtered)
        return data_final

    @staticmethod
    def prep_sort(data):
        data["sum"] = data.sum(axis=1)  # create a extra column with the sum of 1s for each row (promoter)
        data.sort_values(["sum"], inplace=True)  # sort promoters based on the previous sum. Descending order
        data = data.drop(["sum"], axis=1)  # now remove the sum column
        return data

    # Algorithms

    @staticmethod
    def node_based_vencode_getter(data_frame, promoter=False, combinations_number=4, counter=1, skip=(),
                                  breaks=None, stop=5):
        """

        :param data_frame: Data frame containing cage-seq expression profile for several celltypes. Dataframe object
        :param promoter: Previous promoter name(founder node if first time calling this function). str type
        :param combinations_number: Number of combinations of promoters to find VEnCodes. int type
        :param counter: Counter is equal to the depth of the current node. int type
        :param skip: the promoters to skip when finding a VEnCode. type: tuple or list
        :param breaks: Dictionary containing keys for the different levels of breaks (one per each combination number)
        and values corresponding to how many times each combination already cycled. dict type
        :param stop: integer representing the number of promoters to test per node level
        :return: The VEnCode if the algorithm found one, or False if it didn't find.
        """
        vencode_promoters_list = []
        data_frame = data_frame.copy()
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
            vencode_list = data_frame[nodes].index.values  # change to .index.values.tolist() or list(...index.values)
            if isinstance(vencode_list, np.ndarray):
                vencode_list = vencode_list.tolist()
            vencode_promoters_list.append(vencode_list)
            return vencode_promoters_list  # found at least one VEnCode so it can return a successful answer
        else:  # if in previous node could not get a definite VEnCode, re-start search with next node
            promoters = data_frame.index.values  # get an array of all the promoters, to cycle
            counter = counter  # counter is defined with previous counter for recursive use of this function
            counter_thresholds = [i for i in range(2, (combinations_number + 1))]  # set maximum number for counter
            # loop the next area until number of nodes in combination exceeds num of desired proms in comb for VEnCode
            while counter < combinations_number:
                counter += 1  # updates the counter as it will enter the next node depth
                promoters_in_use = (prom for prom in promoters if prom not in skip)
                for prom in promoters_in_use:  # cycle the promoters
                    # region "early quit if loop is taking too long"
                    if breaks is not None and counter in counter_thresholds:
                        breaker_index = str(counter_thresholds.index(counter) + 1)
                        breaks["breaker_" + breaker_index] += 1
                        if breaks["breaker_" + breaker_index] > stop:  # here, we only test x promoters per node level
                            breaks["breaker_" + breaker_index] = 0
                            return []
                    # endregion "early quit if loop is taking too long"
                    promoter_next = Promoters.node_based_vencode_getter(data_frame, prom,
                                                                        combinations_number=combinations_number,
                                                                        skip=skip, counter=counter, breaks=breaks,
                                                                        stop=stop)
                    if promoter_next:
                        vencode_promoters_list.append(promoter_next)
                        return vencode_promoters_list
            else:
                vencode_promoters_list = []
            return vencode_promoters_list

    @staticmethod
    def fill_vencode_list(promoter_list, vencode_list, combinations_number):
        """
        Given an incomplete list of x REs that make up a VEnCode, it fills the list up, up to y VEnCodes (
        y = RE combinations number), based on next sparse REs.
        :param promoter_list: list of promoters to add to VEnCodes
        :param vencode_list:
        :param combinations_number:
        :return: A list of y REs that comprise a VEnCode, where y = combinations number.
        """
        assert len(vencode_list) <= combinations_number, "vencode list len is bigger than wanted RE number"
        if len(vencode_list) == combinations_number:
            return vencode_list
        for prom in promoter_list:
            if prom in vencode_list:
                continue
            vencode_list.append(prom)
            if len(vencode_list) == combinations_number:
                break
        return vencode_list

    @staticmethod
    def e_value_calculator(vencode_data, reps=100):
        """ Preps the data to be used in Monte Carlo simulation. """
        col_list = vencode_data.columns.values.tolist()
        e_value = util.vencode_mc_simulation(vencode_data, col_list, reps=reps)
        return e_value

    @staticmethod
    def e_value_normalizer(e_value_raw, celltype_number, number_of_re):
        """
        Normalizes the e-value due to disparity in number of celltypes
        :param e_value_raw: value to normalize
        :param celltype_number: number of cell types in data set
        :param number_of_re: number of RE in sample
        :return: normalized e-value
        """
        coefs = {"a": -164054.1, "b": 0.9998811, "c": 0.000006088948, "d": 1.00051, "m": 0.9527, "e": -0.1131}
        e_value_expected = (coefs["m"] * number_of_re + coefs["e"]) * celltype_number ** (
            coefs["d"] + ((coefs["a"] - coefs["d"]) / (1 + (number_of_re / coefs["c"]) ** coefs["b"])))
        e_value_norm = (e_value_raw / e_value_expected) * 100
        if e_value_norm < 100:
            return e_value_norm
        else:
            return 100

    @staticmethod
    def sampling_method_vencode_getter(data, combinations_number=4, to_drop=None, n_samples=100000, threshold=0,
                                       skip_sparsest=True):
        """
        Function that searches for a VEnCode in data by the sampling method. Please note that it retrieves a DataFrame
        containing the entire sample. This is the reason why it only retrieves one VEnCode.
        :param data: Data set to search for VEnCodes
        :param combinations_number:
        :param to_drop:
        :param n_samples:
        :param threshold: minimum expression threshold that counts to consider a promoter inactive.
        :param skip_sparsest: Allows user to skip first check - check if sparsest REs already constitute a VEnCode.
        :return: a Pandas DataFrame with the sample that is a VEnCode.
        """
        if not skip_sparsest:
            # try first to see if sparsest REs aren't already a VEnCode:
            sparsest = data.head(n=combinations_number)
            if util.assess_vencode_one_zero_boolean(sparsest, threshold=threshold):
                return sparsest
        for i in range(n_samples):
            try:
                sample = data.sample(n=combinations_number)  # take a sample of n promoters
            except ValueError:  # Combinations_number could be larger than number of RE available. Then, no VEnCode.
                break
            if to_drop is not None:
                sample = sample.drop(to_drop, axis=1)  # remove it from the data to access VEn
            if util.assess_vencode_one_zero_boolean(sample, threshold=threshold):  # assess if VEnCode
                return sample  # TODO: as of now if only gets the first vencode by sampling, try to use n_vencodes
        return None

    @staticmethod
    def heuristic_method_vencode_getter(data, combinations_number=4, number_vencodes=10, stop=5, logger=logging):
        """
        Function that searches for a VEnCode in data by the heuristic method. It also gives the e-values straight away.
        :param data: Data set to search for VEnCodes
        :param combinations_number:
        :param number_vencodes:
        :param logger:
        :return:
        """
        breaks = {}  # this next section creates a dictionary to update with how many times each node is cycled
        for item in range(1, combinations_number):
            breaks["breaker_" + str(item)] = 0
        skip = []
        vencodes_dict = {}
        for number in range(number_vencodes):
            vencodes_from_nodes = Promoters.node_based_vencode_getter(data,
                                                                      combinations_number=combinations_number,
                                                                      skip=skip,
                                                                      breaks=breaks, stop=5)
            if not vencodes_from_nodes:
                break
            for key, value in breaks.items():
                breaks[key] = 0
            vencodes_incomplete = [item for sublist in vencodes_from_nodes for item in sublist]
            vencodes_dict[number] = vencodes_incomplete
            if not any(isinstance(z, list) for z in vencodes_incomplete):
                for item in vencodes_incomplete:
                    skip.append(item)
            else:
                skip.append(vencodes_incomplete[0])
        promoters = data.index.values.tolist()
        vencodes_evaluated = {}
        logger.debug(vencodes_dict)
        for key, value in vencodes_dict.items():
            logger.debug("Key number {}".format(key))
            logger.debug(value)
            promoters_copy = promoters
            counter = 0
            for i in util.combinations_from_nested_lists(value):
                util.multi_log(logger, "Founder:", i, level="debug")
                vencode = Promoters.fill_vencode_list(promoters_copy, list(i), 4)
                util.multi_log(logger, "Filled:", vencode, level="debug")
                promoters_copy = [item for item in promoters_copy if item not in i]  # delete promoters "i"
                e_value = Promoters.e_value_calculator(data.loc[vencode])
                e_value = Promoters.e_value_normalizer(e_value, data.shape[1], combinations_number)
                vencodes_evaluated[tuple(vencode)] = e_value
                counter += 1
                if counter == number_vencodes:  # sometimes the number of combinations may be too big.
                    logger.info("Break. Only get {} VEnCodes".format(number_vencodes))
                    break
            if not any(isinstance(item, list) for item in value):
                for j in value:
                    try:
                        promoters.remove(j)
                    except ValueError:
                        pass
            else:
                try:
                    promoters.remove(value[0])
                except ValueError:
                    pass
            return vencodes_evaluated

    def logging_proms(self, locals_):
        # Get function name:
        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame, 2)
        func = caller_frame[1][3]
        # Prepare directory:
        folder = "/Logs/"
        parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + folder
        dhs.check_if_and_makedir(parent_path)
        file_directory = dhs.check_if_and_makefile(func, path=parent_path, file_type=".log")
        # Config and start logging
        logging.basicConfig(filename=file_directory, level=logging.DEBUG,
                            format="{asctime} - {levelname} - {message}", filemode='w', style="{")
        logger = logging.getLogger(__name__)
        # Get parameters in string:
        del locals_["self"]
        first_log = " ".join([str(x) + "-" + str(y) for x, y in locals_.items()])
        logger.info(first_log)
        logger.setLevel(self.log_level)
        return logger

    # For figures:

    def ven_diagrams(self, vens_to_take, combinations_number=4, expression=1, threshold=90):
        if isinstance(self.codes, dict):
            codes = [j for i in list(self.codes.values()) for j in i]
        else:
            codes = self.codes
        for code in codes:  # subsequent analysis will be done for each sample (code) separately
            print("donor:", code, sep="\n", end="\n\n")
            codes_2 = [x for x in codes if x != code]
            donors_data = self.data[codes_2]
            data_2 = self.data.drop(codes_2, axis=1)
            print("donors to exclude:", *codes_2, sep="\n", end="\n\n")
            filter_2 = util.df_filter_by_expression_and_percentile(data_2, code, expression, 2, threshold)
            ven_diagram = {"None": []}  # create the final dict to later append VEnCode counts:
            for r in reversed(range(1, (len(codes_2) + 1))):  # create dict keys up front because of append
                for z in iter.combinations(codes_2, r):
                    z = list(z)
                    string_z = "  ".join(z)
                    ven_diagram[string_z] = []
            n = 0
            while n < vens_to_take:
                sample = filter_2.sample(n=combinations_number)  # taking a sample of n RE to assess if VEnCode
                sample_dropped = sample.drop(code, axis=1).values  # dropping code celltype from the sample
                assess_if_vencode = np.any(sample_dropped == 0, axis=0)  # assess if at least 1 zero per column
                if all(assess_if_vencode):  # is RE sample a VEnCode for code?
                    n += 1
                    donors_data_sample = donors_data.loc[sample.index.values]  # locating the n RE in the other codes db
                    no_ven = True  # will change to false to prevent double attribution of VEnCodes to the other codes
                    counter = 0
                    none_counter = 0
                    # start iterator through all possible other codes combinations:
                    for i in reversed(range(1, (len(codes_2) + 1))):
                        for y in iter.combinations(codes_2, i):  # take a combination of i number of other codes
                            y = list(y)
                            string_y = "  ".join(y)
                            to_assess = donors_data_sample[y]
                            assess_if_not_vencode_donors = np.any(to_assess.values == 0, axis=0)
                            # is RE sample not a VEnCode for this comb other codes?
                            try:
                                if assess_if_not_vencode_donors:
                                    pass
                                else:
                                    counter += 1
                                    no_ven = False
                                    break
                            except:
                                if any(assess_if_not_vencode_donors):
                                    pass
                                else:
                                    counter += 1
                                    no_ven = False
                                    break
                        ven_diagram[string_y].append(counter)
                        if not no_ven:
                            break
                    if counter == 0:
                        none_counter += 1
                        ven_diagram["None"].append(none_counter)
                else:
                    pass
            for key in ven_diagram:
                ven_diagram[key] = sum(ven_diagram[key])

            folder = "/Figure 3-b2/cell lines/"
            if not os.path.exists(folder):
                os.makedirs(folder)
            position = codes.index(code) + 1
            file_name = u"/Donor{} - {}".format(position, self.celltype)
            writing_files.write_one_value_dict_to_csv(file_name + ".csv", ven_diagram, folder)

    def statistics_ven_diagram(self, vens_to_test, sampling_number, number_donors, combinations_number=4,
                               expression=1, threshold=90):
        """ To use to generate statistics based on random sampling the data for functions ven_diagram and, especially,
        ven_diagram_interception """
        codes_1 = util.possible_dict_to_list(self.codes)
        number = 0
        ven_diagram_1 = {}
        while number < sampling_number:
            number += 1
            codes = np.random.choice(codes_1, number_donors, replace=False)
            ven_diagram = {}
            for code in codes:
                print("Sample:", code, sep="\n", end="\n\n")
                codes_2 = [x for x in codes if x != code]
                donors_data = self.data[codes_2]
                data_2 = self.data.drop(codes_2, axis=1)
                print("Samples to exclude:", *codes_2, sep="\n", end="\n\n")
                filter_2 = util.df_filter_by_expression_and_percentile(data_2, code, expression, 2, threshold)
                ven_diagram[code] = []
                n = 0
                stop_counter = 0
                while n < vens_to_test:
                    stop_counter += 1
                    sample = filter_2.sample(n=combinations_number)
                    sample_dropped = sample.drop(code, axis=1).values
                    assess_if_vencode = np.any(sample_dropped == 0, axis=0)
                    if all(assess_if_vencode):
                        n += 1
                        donors_data_sample = donors_data.loc[sample.index.values]
                        counter = 0
                        to_assess = donors_data_sample[codes_2]
                        assess_if_not_vencode_donors = np.any(to_assess.values == 0, axis=0)
                        try:
                            if assess_if_not_vencode_donors:
                                pass
                            else:
                                counter += 1
                        except:
                            if any(assess_if_not_vencode_donors):
                                pass
                            else:
                                counter += 1
                        ven_diagram[code].append(counter)
                    if stop_counter > 500000:  # in case there is not enough VEnCodes to check them all
                        break
                ven_diagram[code] = sum(ven_diagram[code]) / stop_counter
                print(n)
            codes_string = ''.join(codes.tolist())
            ven_diagram_1[codes_string] = np.mean(list(ven_diagram.values()))
        print(ven_diagram_1)
        folder = "/Figure 3-b2/cell lines/"
        if not os.path.exists(folder):
            os.makedirs(folder)
        if isinstance(self.celltype, str):
            file_name = u"/stats for {} celltype".format(self.celltype)
        else:
            file_name = u"/stats for {} celltypes".format(len(self.codes))
        writing_files.write_one_value_dict_to_csv(file_name + ".csv", ven_diagram_1, folder)

    def ven_diagram_interception(self, vens_to_test, sampling_number, number_donors, combinations_number=4,
                                 expression=1, threshold=90, custom_celltypes=()):
        if custom_celltypes:
            celltypes_analysis = custom_celltypes
        else:
            celltypes_analysis = self.codes
        for celltype in celltypes_analysis:  # cycle through cell types to get the number of vencodes at the interception of donors/replicates.
            codes_1 = self.codes[celltype]  # get all the donors/replicates for this cell type in a list
            number = 0
            ven_diagram_1 = defaultdict(list)
            while number < sampling_number:  # limit VEnCode testing to sampling_number
                number += 1
                # codes = np.random.choice(codes_1, number_donors, replace=False)
                codes = codes_1
                ven_diagram = {}
                for code in codes:  # start cycling each donor/replicate.
                    print("Sample:", code, sep="\n", end="\n\n")
                    codes_2 = [x for x in codes if x != code]  # list of all other donors/replicates not chosen
                    donors_data = self.data[codes_2]  # subset of the data for not chosen donors/reps
                    data_2 = self.data.drop(codes_2, axis=1)  # subset of data excluding not chosen donors/reps
                    print("Samples to exclude:", *codes_2, sep="\n", end="\n\n")
                    filter_2 = util.df_filter_by_expression_and_percentile(data_2, code, expression, 2,
                                                                           threshold)  # apply filters
                    ven_diagram[code] = []
                    n = 0
                    stop_counter = 0
                    while n < vens_to_test:  # limit VEnCode testing to vens_to_test
                        stop_counter += 1
                        sample = filter_2.sample(n=combinations_number)  # take a sample of n promoters
                        sample_dropped = sample.drop(code, axis=1).values  # remove it from the data to access VEn
                        assess_if_vencode = np.any(sample_dropped == 0, axis=0)  # list of True if column has any 0
                        if all(assess_if_vencode):  # if all columns are True (contain at least one 0), then is VEn
                            n += 1
                            donors_data_sample = donors_data.loc[
                                sample.index.values]  # subset of not chosen donors/reps containing only the sampled promoters
                            counter = 0
                            assess_if_not_vencode_donors = np.any(donors_data_sample.values == 0, axis=0)
                            try:
                                if assess_if_not_vencode_donors:  # if donors/reps don't express all promoters:
                                    pass
                                else:  # if they do, then the VEnCode found is also a VEnCode for the donors/reps
                                    counter += 1
                            except:
                                if any(assess_if_not_vencode_donors):
                                    pass
                                else:
                                    counter += 1
                            ven_diagram[code].append(counter)  # append the value of counter: =1 if VEn, =0 if not.
                        if stop_counter > 500000:  # in case there is not enough VEnCodes to check them all
                            break
                    ven_diagram[code] = (sum(ven_diagram[code]) / n) * 100  # sum the appended values and normalize.
                    print(n)
                codes_string = '-'.join(codes)
                ven_diagram_1[codes_string].append(np.mean(list(ven_diagram.values())))
            print(ven_diagram_1)
            folder = "/Figure 3-b2/"
            if not os.path.exists(folder):
                os.makedirs(folder)
            file_name = u"/interception of {}".format(celltype.replace(":", "-"))
            writing_files.write_one_value_dict_to_csv(file_name + ".csv", ven_diagram_1, folder)
            writing_files.write_dict_to_csv(file_name + "_2.csv", ven_diagram_1, folder, path="parent")

    def inter_donor_percentage_difference(self, vens_to_test, sampling_number, number_donors, combinations_number=4,
                                          expression=1, threshold=90, single_file=False):
        logger = self.logging_proms(locals())
        if not single_file:
            interception_together = {}
        for celltype in self.codes:  # cycle through cell types to get the number of vencodes at the interception of donors/replicates.
            codes_list = self.codes[celltype]  # get all the donors/replicates for this cell type in a list
            counter_samples = 0
            interception_codes = {}
            while counter_samples < sampling_number:  # limit VEnCode testing to sampling_number
                counter_samples += 1
                interception_code = {str(counter_samples): []}
                codes = np.random.choice(codes_list, number_donors,
                                         replace=False)  # redundant, unless for statistics, using random sampling method.
                for i in range(1, number_donors):  # start cycling each combination of number of donors/reps
                    for code in iter.combinations(codes, i):  # start cycling each combination of donor/replicate.
                        code = list(code)
                        logger.info("Sample: {}".format(code))
                        codes_others = [x for x in codes if
                                        x not in code]  # list of all other donors/replicates not chosen
                        data_others = self.data[codes_others]  # subset of the data for not chosen donors/reps
                        data_with_code = self.data.drop(codes_others,
                                                        axis=1)  # subset of data excluding not chosen donors/reps
                        logger.info("Samples to exclude: {}".format(codes_others))
                        data_filtered = util.df_filter_by_expression_and_percentile(data_with_code, code,
                                                                                    expression, 2,
                                                                                    threshold)  # apply filters
                        interception_ven = {str(code): []}
                        n = 0
                        stop_counter = 0
                        while n < vens_to_test:  # limit VEnCode testing to vens_to_test
                            stop_counter += 1
                            sample = data_filtered.sample(n=combinations_number)  # take a sample of n promoters
                            sample_dropped = sample.drop(code, axis=1).values  # remove it from the data to access VEn
                            if util.assess_vencode_one_zero_boolean(sample_dropped):  # assess if VEnCode
                                n += 1
                                sample_donors_data = data_others.loc[
                                    sample.index.values]  # subset of not chosen donors/reps containing only the sampled promoters
                                counter_interceptions = 0
                                assess_if_not_vencode_donors = np.any(sample_donors_data.values == 0, axis=0)
                                try:
                                    if assess_if_not_vencode_donors:  # if donors/reps don't express all promoters:
                                        pass
                                    else:  # if they do, then the VEnCode found is also a VEnCode for the donors/reps
                                        counter_interceptions += 1
                                except:
                                    if any(assess_if_not_vencode_donors):
                                        pass
                                    else:
                                        counter_interceptions += 1
                                interception_ven[str(code)].append(
                                    counter_interceptions)  # append the value of counter: =1 if VEn, =0 if not.
                            if stop_counter > 500000:  # in case there is not enough VEnCodes to check them all
                                break
                        try:
                            interception_ven[str(code)] = (sum(
                                interception_ven[str(code)]) / n) * 100  # sum the appended values and normalize.
                        except ZeroDivisionError:
                            logger.warning("Could not evaluate VEnCodes this time!")
                            continue
                        logger.info("Managed to evaluate {} VEnCodes".format(n))
                        logger.info("And the percentage that were VEnCodes for all donors/replicates were {}".format(
                            interception_ven))
                    try:
                        interception_code[str(counter_samples)].append(np.mean(list(interception_ven.values())))
                    except UnboundLocalError:
                        logger.warning(
                            "Couldn't get VEnCodes to test for combinations of {} donors/reps for celltype: {}".format(
                                i, celltype))
                        continue
                celltype_to_write = celltype + "-" + str(counter_samples)
                interception_codes[celltype_to_write] = interception_code[str(counter_samples)]
                logger.info("Data for rep {} - {}".format(counter_samples, interception_codes))
            if single_file:
                folder = "/Figure 3-b2/cell lines/"
                dhs.check_if_and_makedir(folder)
                file_name = dhs.check_if_and_makefile(
                    folder + u"/interception of {}".format(celltype))
                writing_files.write_one_value_dict_to_csv(file_name, interception_codes, folder)
                logger.info("File generated: {}".format(file_name))
            else:
                interception_together.update(interception_codes)
        folder = "/Figure 3-b2/cell lines/"
        dhs.check_if_and_makedir(folder)
        file_name = u"/interception of {} donors in {} celltypes".format(number_donors, len(self.codes)) + ".csv"
        writing_files.write_one_value_dict_to_csv(file_name, interception_together, folder)
        logger.info("File generated: {}".format(file_name))

    def get_vencodes(self, combinations_number=4, p=None, n=None, write_file=False):
        if isinstance(self.codes, dict):
            codes = [j for i in list(self.codes.values()) for j in i]
        else:
            codes = self.codes
        if len(codes) == 1:
            code = codes[0]
            others_df = None
            try:
                filter_1 = util.df_filter_by_expression(self.data, codes, 1)
            except KeyError:
                self.data = self.data.join(self.codes_df[codes])
                filter_1 = util.df_filter_by_expression(self.data, codes, 1)
                del self.data[codes]
            threshold = 100
            while threshold > 0:
                with_percentage_of_zeros, column_name = util.df_percentile_calculator(filter_1, codes,
                                                                                      threshold)
                filter_2 = util.df_filter_by_column_value(with_percentage_of_zeros, column_name)
                if p is not None:
                    sorted_1 = filter_2.nlargest(p, codes)
                else:
                    sorted_1 = filter_2.sort(codes.tolist(), ascending=False)
                print("starting %s -> threshold = %s" % (code, threshold))
                success = util.reform_vencode_n_combinations_of_k(threshold, sorted_1.drop(column_name, axis=1),
                                                                  code, self.celltype, "Promoters",
                                                                  combinations_number,
                                                                  n, others_df, write_file)
                if not success:
                    threshold -= 10
                if success:
                    threshold = 0
        else:
            code = codes[0]
            codes_2 = np.array(codes).tolist()
            codes_2.remove(code)
            filter_1 = util.df_filter_by_expression(self.data, codes, 1)
            threshold = 100
            while threshold > 0:
                with_percentage_of_zeros, column_name = util.df_percentile_calculator(filter_1, codes,
                                                                                      threshold)
                filter_2 = util.df_filter_by_column_value(with_percentage_of_zeros, column_name)
                if p is not None:
                    sorted_1 = filter_2.nlargest(p, codes)
                else:
                    sorted_1 = filter_2.sort(codes, ascending=False)
                codes_2_df = sorted_1[codes_2]
                cropped = sorted_1.drop(codes_2, axis=1)
                print("Starting %s -> threshold = %s" % (self.celltype, threshold))
                success = util.reform_vencode_n_combinations_of_k(threshold, cropped.drop(column_name, axis=1),
                                                                  code, self.celltype, "Promoters",
                                                                  combinations_number,
                                                                  n, codes_2_df, write_file)
                if not success:
                    threshold -= 10
                if success:
                    threshold = 0

    def vencode_generator(self, celltype, algorithm="heuristic", combinations_number=4, threshold_activity=1,
                          threshold_sparseness=90, threshold_inactivity=0, number_vencodes=8, sampling_samples=10000,
                          ):
        """
        Generates a number of vencodes, deemed the best according to E-value.
        :param celltype: cell type to get VEnCodes for. Str
        :param algorithm: method to get VEnCodes. Currently supporting "sampling", "heuristic", or "both".
        :param combinations_number: number of REs comprising the VEnCodes. Int
        :param threshold_activity: minimum expression level for the celltype to develop VEnCodes. Int
        :param threshold_sparseness: threshold of sparseness to filter the data set with, before VEnCode selection. Int
        :param threshold_inactivity: minimum RE expression to consider as inactive in all ctps not to get VEnCode. Int
        :param number_vencodes: number of VEnCodes to get. Int
        :return: Expression data for all VEnCodes. list/dict of pd.DataFrame object
        """
        logger = self.logging_proms(locals())
        algorithm = algorithm.casefold()
        while True:
            try:
                assert algorithm in ("heuristic", "sampling", "both")
            except AssertionError:
                algorithm = ehs.argument_exception("algorithm", logger=logger)
            else:
                break
        if algorithm == "both": algorithm = ["heuristic", "sampling"]
        if self.conservative:
            self.data = self.merge_donors_into_celltypes(exclude=celltype)
        data = self.filter_prep_sort_drop_codes(self.codes[celltype], threshold_activity, threshold_sparseness,
                                                threshold_inactivity=threshold_inactivity)
        vencodes_final_list = []
        vencodes_heuristic_final = {}
        vencodes_sampling_final = {}
        if "heuristic" in algorithm:
            data_copy = data.copy()
            while True:
                vencodes_heuristic = self.heuristic_method_vencode_getter(data=data_copy,
                                                                          combinations_number=combinations_number,
                                                                          number_vencodes=number_vencodes,
                                                                          logger=logger)
                while len(vencodes_final_list) < number_vencodes:
                    top_valued_vencode = util.key_with_max_val(vencodes_heuristic)
                    vencodes_heuristic_final[top_valued_vencode] = vencodes_heuristic[top_valued_vencode]
                    vencodes_heuristic.pop(top_valued_vencode)
                    vencodes_final_list.append(top_valued_vencode)
                    if not vencodes_heuristic:
                        break
                if len(vencodes_final_list) == number_vencodes:  # make sure we retrieve the wanted number of vencodes
                    break
                else:
                    threshold_sparseness -= 10
                    if threshold_sparseness < 0:
                        break
                    data_copy = self.filter_prep_sort_drop_codes(self.codes[celltype], threshold_activity,
                                                                 threshold_sparseness,
                                                                 threshold_inactivity=threshold_inactivity)
            util.multi_log(logger, "VEnCodes from sampling algorithm: ", vencodes_heuristic_final)
        else:
            pass
        if "sampling" in algorithm:
            for i in range(number_vencodes):
                while True:
                    vencode_sampling = self.sampling_method_vencode_getter(data,
                                                                           combinations_number=combinations_number,
                                                                           n_samples=sampling_samples)
                    promoters = tuple(vencode_sampling.index.tolist())
                    if promoters in vencodes_sampling_final.keys():
                        continue
                    e_value = Promoters.e_value_calculator(vencode_sampling)
                    e_value = Promoters.e_value_normalizer(e_value, data.shape[1], combinations_number)
                    vencodes_sampling_final[promoters] = e_value
                    break
            util.multi_log(logger, "VEnCodes from sampling algorithm: ", vencodes_sampling_final)
        else:
            pass
        if "sampling" in algorithm and "heuristic" in algorithm:
            vencodes = {}
            for item in (["heuristic", vencodes_heuristic_final], ["sampling", vencodes_sampling_final]):
                vencodes[item[0]] = item[1]
            return vencodes

    def best_vencode_generator(self, celltype, combinations_number=4, threshold_activity=1, threshold_sparseness=90,
                               threshold_inactivity=0, number_vencodes=8, random_ven=True, random_unfiltered_ven=False):
        """
        Generates a number of vencodes, deemed the best according to E-value, plus some random VEnCodes if set in
        options.
        :param celltype: cell type to get VEnCodes for. Str
        :param combinations_number: number of REs comprising the VEnCodes. Int
        :param threshold_activity: minimum expression level for the celltype to develop VEnCodes. Int
        :param threshold_sparseness: threshold of sparseness to filter the data set with, before VEnCode selection. Int
        :param threshold_inactivity: minimum RE expression to consider as inactive in all ctps not to get VEnCode. Int
        :param number_vencodes: number of VEnCodes to get. Int
        :param random_ven: add some heterogeneity to the retrieved VEnCodes, include vencode from random sampling. Bool
        :param random_unfiltered_ven: True to add a random VEnCode from a raw data set before filters. Bool
        :return: None
        """
        logger = self.logging_proms(locals())
        if self.conservative:
            self.data = self.merge_donors_into_celltypes(exclude=celltype)
        if self.skip_raw_data:
            filename = os.path.join(self.path_parsed_data, "{}_tpm_{}-1.csv".format(celltype, self.data_type))
            self.data = pd.read_csv(filename, sep=";", index_col=0, engine="python")
        data = self.filter_prep_sort_drop_codes(self.codes[celltype], threshold_activity, threshold_sparseness,
                                                threshold_inactivity=threshold_inactivity)
        vencodes_final_list = []
        vencodes_final_dict = {}
        vencodes_evaluated = self.heuristic_method_vencode_getter(data, combinations_number=combinations_number,
                                                                  number_vencodes=number_vencodes, logger=logger)
        if random_ven:
            vencode_from_sample = self.sampling_method_vencode_getter(data)
            if vencode_from_sample is not None:
                e_value_sampling = self.e_value_calculator(vencode_from_sample)
                e_value_sampling = self.e_value_normalizer(e_value_sampling, data.shape[1], combinations_number)
                vencodes_final_dict[tuple(vencode_from_sample.index.values)] = e_value_sampling
                vencodes_final_list.append(vencode_from_sample.index.values.tolist())
            else:
                logger.info("Random sampling the data yielded no VEnCodes")
        if random_unfiltered_ven:
            vencode_from_sample = self.sampling_method_vencode_getter(self.data, to_drop=self.codes[celltype])
            if vencode_from_sample is not None:
                e_value_sampling = self.e_value_calculator(vencode_from_sample)
                e_value_sampling = self.e_value_normalizer(e_value_sampling, self.data.shape[1], combinations_number)
                vencodes_final_dict[tuple(vencode_from_sample.index.values)] = e_value_sampling
                vencodes_final_list.append(vencode_from_sample.index.values.tolist())
            else:
                logger.info("Random sampling the unsorted data yielded no VEnCodes")
        util.multi_log(logger, "VEnCodes with e-values:", vencodes_evaluated)
        while len(vencodes_final_list) < number_vencodes:
            top_valued_vencode = util.key_with_max_val(vencodes_evaluated)
            vencodes_final_dict[top_valued_vencode] = vencodes_evaluated[top_valued_vencode]
            vencodes_evaluated.pop(top_valued_vencode)
            vencodes_final_list.append(top_valued_vencode)
            if not vencodes_evaluated:
                break
        util.multi_log(logger, vencodes_final_dict)
        # plotting:
        for vencode_to_write, e_values in vencodes_final_dict.items():
            to_csv = self.data.loc[list(vencode_to_write)]
            to_csv = to_csv.applymap(
                lambda x: 0 if x == 0 else 1)  # change expression to 1s and 0s if we don't want the actual numbers.
            file_name = dhs.check_if_and_makefile(os.path.join("VenCodes",
                                                               "{}_{}_ven").format(celltype, self.data_type),
                                                  path_type="parent2")
            with open(file_name, 'a') as f:
                to_csv.to_csv(f, sep=";")
            file_name_e_values = dhs.check_if_and_makefile(os.path.join("VenCodes",
                                                                        "{}_{}_ven_evalues").format(celltype,
                                                                                                    self.data_type),
                                                           path_type="parent2")
            to_write = {vencode_to_write: e_values}
            writing_files.write_dict_to_csv(file_name_e_values, to_write, deprecated=False)
        return

    def find_vencodes_each_celltype(self, combinations_number=tuple(range(1, 11)), threshold_activity=1,
                                    threshold_sparseness=90, threshold_inactivity=0,
                                    method="sampling", n_samples=200000, stop=5):
        """
        Writes a file containing information about VEnCode accessibility for each celltype, where 1 represents a
        VEnCode. e.g.:
                k=  |1|2|3|4|
        Astrocytes: |0|0|1|1|
        Meaning: Astrocytes have VEnCodes when k>=3.

        :param combinations_number: Number of combinations to search for VEnCodes. List
        :param threshold_activity: Minimum RE expression to qualify as active in cell types to get VEnCode. Int
        :param threshold_sparseness: Starting threshold of sparseness. Int
        :param threshold_inactivity: minimum RE expression to consider as inactive in all ctps not to get VEnCode. Int
        :param method: method of searching for VEnCodes. currently supported: sampling or heuristic. str
        :param n_samples: Number of samples to test for VEnCode. Used in sampling method. Int
        :param stop: Number of nodes to test at each level. Used in heuristic method. Int
        """
        logger = self.logging_proms(locals())
        data_copy = self.data.copy()
        results_dict = defaultdict(list)
        if self.conservative:
            self.data = self.merge_donors_into_celltypes()
        for celltype in tqdm(self.celltype, desc="Celltypes"):
            util.multi_log(logger, "Starting:", celltype)
            if self.conservative:
                data_celltype = self.data[celltype]
                self.data.drop(celltype, axis=1, inplace=True)
                self.data = pd.concat([self.data, data_copy[self.codes[celltype]]], axis=1)
            if self.skip_raw_data:
                filename = os.path.join(self.path_parsed_data, "{}_tpm_{}-1.csv".format(celltype, self.data_type))
                self.data = pd.read_csv(filename, sep=";", index_col=0, engine="python")
            data = self.filter_prep_sort_drop_codes(self.codes[celltype], threshold_activity, threshold_sparseness,
                                                    threshold_inactivity=threshold_inactivity)
            for k in combinations_number:
                if method.casefold() == "heuristic":
                    # this next section creates a dictionary to update with how many times each node is cycled
                    breaks = {}
                    for item in range(1, k):
                        breaks["breaker_" + str(item)] = 0
                    skip = []
                    vencodes = self.node_based_vencode_getter(data,
                                                              combinations_number=k, skip=skip,
                                                              breaks=breaks, stop=stop)
                elif method.casefold() == "sampling":
                    vencodes = self.sampling_method_vencode_getter(data, combinations_number=k,
                                                                   n_samples=n_samples, skip_sparsest=False)
                    if isinstance(vencodes, pd.DataFrame):
                        vencodes = True
                else:
                    raise NameError("method name to get VEnCodes not recognized: ", method)
                if not vencodes:
                    results_dict[celltype].append(0)
                else:
                    for v in range((k - combinations_number[0]), len(combinations_number)):
                        results_dict[celltype].append(1)
                    break
            if self.conservative:  # to save RAM space, we spend a bit more time returning self.data to its original.
                self.data.drop(data_copy[self.codes[celltype]], axis=1, inplace=True)
                self.data = pd.concat([self.data, data_celltype], axis=1)
            util.multi_log(logger, celltype, results_dict[celltype])
        return results_dict

    def intra_individual_robustness(self, combinations_number, vens_to_take, reps=1, threshold_sparseness=90,
                                    threshold_activity=1, get_vencodes=False):
        """

        :param combinations_number: Number of combinations to search for VEnCodes. List
        :param vens_to_take:
        :param reps:
        :param threshold_sparseness: Starting threshold of sparseness. Int
        :param threshold_activity: Minimum RE expression to qualify for VEnCode for each celltype. Int
        :param get_vencodes:
        """
        final = {}
        final_vencodes = {}
        base_threshold = threshold_sparseness
        data_copy = self.data.copy()
        if self.conservative:
            self.data = self.merge_donors_into_celltypes()
        # Starting loop through all cell types:
        for cell in tqdm(self.codes):
            threshold_sparseness = base_threshold
            codes = self.codes[cell]
            print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
            if self.conservative:
                data_celltype = self.data[cell]
                self.data.drop(cell, axis=1, inplace=True)
                self.data = pd.concat([self.data, data_copy[self.codes[cell]]], axis=1)
            if self.skip_raw_data:
                filename = os.path.join(self.path_parsed_data, "{}_tpm_{}-1.csv".format(cell, self.data_type))
                self.data = pd.read_csv(filename, sep=";", index_col=0, engine="python")
            filter_1 = util.df_filter_by_expression_and_percentile(self.data, codes, threshold_activity, 1)
            e_values_list = []
            counter = 0
            while len(e_values_list) < vens_to_take:
                filter_2, threshold_sparseness = util.df_filter_by_percentile(filter_1, codes, threshold_sparseness)
                if get_vencodes:
                    e_value_raw, vencodes = util.vencode_percent_sampling_monte_carlo(codes, filter_2,
                                                                                      combinations_number,
                                                                                      vens_to_take, reps,
                                                                                      vencodes=get_vencodes,
                                                                                      stop_at=10000)
                    final_vencodes.update(vencodes)
                else:
                    e_value_raw = util.vencode_percent_sampling_monte_carlo(codes, filter_2, combinations_number,
                                                                            vens_to_take,
                                                                            reps, vencodes=get_vencodes,
                                                                            stop_at=10000)
                try:
                    for item in e_value_raw:
                        e_value_norm = self.e_value_normalizer(item, filter_2.shape[1], combinations_number)
                        e_values_list.append(e_value_norm)
                except:
                    pass
                threshold_sparseness -= 5
                counter += 1
                if threshold_sparseness < 50 or counter == 3:
                    if len(e_values_list) == vens_to_take:
                        break
                    for i in range(len(e_values_list), vens_to_take):
                        e_values_list.append("-")
                    break
            final[cell] = e_values_list
            if self.conservative:  # to save RAM space, we spend a bit more time returning self.data to its original.
                self.data.drop(data_copy[self.codes[cell]], axis=1, inplace=True)
                self.data = pd.concat([self.data, data_celltype], axis=1)

        # folder = "/Figure 2/"
        if get_vencodes:
            # file_name = u"/VEnCodes {} samples {} VEnCodes.csv".format(len(self.codes), vens_to_take)
            # writing_files.write_dict_to_csv(file_name, final_vencodes, folder, path="parent")
            return final_vencodes
        # file_name = u"/VEnCode E-values {} samples {} VEnCodes.csv".format(len(self.codes), vens_to_take)
        # writing_files.write_dict_to_csv(file_name, final, folder, path="parent")
        return final

    def enhancer_promoter_vencodes(self, combinations_number=tuple(range(1, 11)), threshold_activity=1,
                                   threshold_sparseness=90, threshold_inactivity=0, method="sampling",
                                   n_samples=200000, stop=5):
        """
        Objective: Get specific combinations for all (or most) of the cell types in the data set.
        Methods: Try to get VEnCodes for enhancers at a specific combinations_number. If there is no VEnCode,
        find columns (cell types) that are preventing the VEnCode for the combination of sparsest REs and get a promoter that
        is not expressed in those columns (cell types).
        :param combinations_number: Number of combinations to search for VEnCodes. List
        :param threshold_activity: Minimum RE expression to qualify as active in cell types to get VEnCode. Int
        :param threshold_sparseness: Starting threshold of sparseness. Int
        :param threshold_inactivity: minimum RE expression to consider as inactive in all ctps not to get VEnCode. Int
        :param method: method of searching for VEnCodes. currently supported: sampling or heuristic. str
        :param n_samples: Number of samples to test for VEnCode. Used in sampling method. Int
        :param stop: Number of nodes to test at each level. Used in heuristic method. Int
        """
        logger = self.logging_proms(locals())
        results_dict = defaultdict(list)
        for celltype in tqdm(self.celltype, desc="Celltypes"):
            util.multi_log(logger, "Starting:", celltype)
            filename = os.path.join(self.path_parsed_data, "{}_tpm_{}-1.csv".format(celltype, self.data_type))
            filename_promoters = filename.replace("enhancers", "promoters")
            self.data = pd.read_csv(filename_promoters, sep=";", index_col=0, engine="python")
            codes = self._code_selector(self.data, self.celltype, not_include=self.not_include,
                                        to_dict=True, regex=True)
            data_promoters = self.filter_prep_sort_drop_codes(codes[celltype], threshold_activity,
                                                              threshold_sparseness,
                                                              threshold_inactivity=threshold_inactivity)
            self.data = pd.read_csv(filename, sep=";", index_col=0, engine="python")
            data = self.filter_prep_sort_drop_codes(self.codes[celltype], threshold_activity, threshold_sparseness,
                                                    threshold_inactivity=threshold_inactivity)
            for k in combinations_number:
                if method.casefold() == "heuristic":
                    # this next section creates a dictionary to update with how many times each node is cycled
                    breaks = {}
                    for item in range(1, k):
                        breaks["breaker_" + str(item)] = 0
                    skip = []
                    vencodes = self.node_based_vencode_getter(data,
                                                              combinations_number=k, skip=skip,
                                                              breaks=breaks, stop=stop)
                elif method.casefold() == "sampling":
                    vencodes = self.sampling_method_vencode_getter(data, combinations_number=k,
                                                                   n_samples=n_samples, skip_sparsest=False)
                if isinstance(vencodes, pd.DataFrame):
                    vencodes = True
                else:
                    raise NameError("method name to get VEnCodes not recognized: ", method)
                if not vencodes:
                    sparsest = data.head(n=k)
                    mask = sparsest != 0
                    cols = sparsest.columns[np.all(mask.values, axis=0)]
                    sparsest_problems = sparsest[cols]
                    data_promoters_problems = data_promoters[cols]
                    for kay in range(k):
                        ven_promoters = self.sampling_method_vencode_getter(data_promoters_problems,
                                                                            combinations_number=kay,
                                                                            n_samples=n_samples, skip_sparsest=False)
                        if isinstance(ven_promoters, pd.DataFrame):
                            ven_promoters = True
                        if not ven_promoters:
                            continue
                        else:
                            break
                    if not ven_promoters:
                        results_dict[celltype].append(0)
                    else:
                        for v in range((k - combinations_number[0]), len(combinations_number)):
                            results_dict[celltype].append(1)
                        break
                else:
                    for v in range((k - combinations_number[0]), len(combinations_number)):
                        results_dict[celltype].append(1)
                    break
            util.multi_log(logger, celltype, results_dict[celltype])
        return results_dict

    # Tests:

    def test_vencode_data(self, rows, columns=None, to_csv=True, file_name="test"):
        if to_csv:
            if columns:
                self.data.loc[rows, columns].to_csv(file_name, sep=';')
            else:
                if isinstance(rows, tuple):
                    rows = list(rows)
                self.data.loc[rows].to_csv(file_name, sep=';')
        else:
            if columns:
                print(self.data.loc[rows, columns])
            else:
                if isinstance(rows, tuple):
                    rows = list(rows)
                print(self.data.loc[rows])

    def test_code_size(self):
        for cell in self.codes:
            codes = self.codes[cell]
            print(cell, len(codes), sep=": ")

    def test_code_names(self, size=None):
        for cell in self.codes:
            codes = self.codes[cell]
            if size is not None:
                if len(codes) == size:
                    print(cell, codes, sep=": ")
                else:
                    pass
            else:
                print(cell, codes, sep=": ")

    def codes_to_csv(self, file_name, type, folder_name):
        if type == "dict":
            writing_files.write_dict_to_csv(file_name, self.codes, folder_name, path="parent")
        if type == "list":
            codes_list = util.possible_dict_to_list(self.codes)
            writing_files.write_list_to_csv(file_name, codes_list, folder_name, path="parent")

    def celltypes_to_csv(self, file_name, folder_name):
        cell_list = list(self.codes.keys())
        writing_files.write_list_to_csv(file_name, cell_list, folder_name, path="parent")


class Enhancers(DatabaseOperations):
    """ A class describing the methods for the enhancers database """

    # unique to each call of Enhancers
    def __init__(self, file, names_db, celltype, celltype_exclude=None, not_include=None, partial_exclude=None,
                 sample_types="primary cells", second_parser=None, conservative=False, log_level="info", nrows=None):
        super().__init__(file, celltype, celltype_exclude=celltype_exclude, not_include=not_include,
                         sample_types=sample_types, second_parser=second_parser, log_level=log_level, nrows=nrows)
        self.names_db = pd.read_csv(self.parent_path + names_db, sep="\t", index_col=1, header=None,
                                    names=["celltypes"], engine="python")
        self.data, self.filtered_names_db = self.first_parser()
        self.codes = self.code_selector(self.celltype, custom=self.filtered_names_db,
                                        remove="fraction", not_include=self.not_include, to_dict=True)
        if partial_exclude:
            self.partial_exclude_codes = {}
            for key, value in partial_exclude.items():
                self.partial_exclude_codes[key] = self.code_selector(value[0], not_include=value[1])

    def first_parser(self):
        """remove universal RNA pools and select the desired sample_type"""
        samples_universal = self.code_selector("universal")
        data_dropped = self.raw_data.drop(samples_universal, axis=1, inplace=False)
        to_keep = self.sample_category_selector("sample types - FANTOM5.csv", self.sample_types, get="name")
        to_keep_codes = self.code_selector(to_keep, match="normal", remove="fraction")
        data = data_dropped[to_keep_codes]
        # Exclude some specific, on-demand, cell-types from the data straight away:
        if self.celltype_exclude is not None:
            codes_exclude = self.code_selector(self.celltype_exclude)
            data.drop(codes_exclude, axis=1, inplace=True)
            # Exclude and select new found codes from the names_db dataframe, to use in self.codes
            new_names_db = self.names_db.loc[to_keep_codes].drop(codes_exclude, axis=0)
        else:
            new_names_db = self.names_db.loc[to_keep_codes]
        return data, new_names_db

    def code_selector(self, celltype, custom=None, match="regex", remove=None, not_include=None, to_dict=False):
        """ Selects codes from a database containing enhancer style indexes. Input is normal celltype nomenclature """
        if custom is not None:
            lines_and_codes = custom
        else:
            lines_and_codes = self.names_db
        if isinstance(celltype, list):
            codes = []
            if to_dict:
                code_dict = {}
            for item in celltype:
                if match == "regex":
                    regular = ".*" + item.replace(" ", ".*").replace("+", "\+") + ".*"
                    idx = lines_and_codes.celltypes.str.contains(regular, flags=re.IGNORECASE, regex=True, na=False)
                elif match == "normal":
                    idx = lines_and_codes.celltypes.str.contains(item, regex=False, na=False)
                elif match == "exact":
                    idx = [True if item == cell_type else False for cell_type in lines_and_codes.celltypes]
                    pass
                else:
                    raise Exception("Match type is not recognized")
                codes_df = lines_and_codes[idx]
                codes.append(codes_df.index.values)
                if to_dict:
                    code_dict[item] = [code for sublist in codes for code in sublist]
                    codes = []
            if not to_dict:
                codes = [code for sublist in codes for code in sublist]
                codes = list(set(codes))
            if remove is not None:
                to_remove_bool = lines_and_codes.celltypes.str.contains(remove, regex=False, na=False)
                to_remove = lines_and_codes[to_remove_bool]
                to_remove = to_remove.index.values
                # remove all codes containing -remove-
                if to_dict:
                    codes = {}
                    for item, values in code_dict.items():
                        codes[item] = [code for code in values if code not in to_remove]
                else:
                    codes = [code for code in codes if code not in to_remove]
            if not_include is not None:
                if isinstance(not_include, dict):
                    for key, values in not_include.items():
                        if key not in codes.keys():
                            continue
                        values_codes = self.code_selector(values, custom=self.filtered_names_db)
                        not_include_codes = self.not_include_code_getter(values_codes, self.data)
                        codes[key] = list(set(codes[key]) - set(not_include_codes))
                else:
                    values_codes = self.code_selector(not_include, custom=self.filtered_names_db)
                    not_include_codes = self.not_include_code_getter(values_codes, self.data)
                    codes = list(set(codes) - set(not_include_codes))
        else:
            regular = ".*" + celltype.replace(" ", ".*").replace("+", "\+") + ".*"
            idx = lines_and_codes.celltypes.str.contains(regular, flags=re.IGNORECASE, regex=True, na=False)
            codes_df = lines_and_codes[idx]
            codes = codes_df.index.values.tolist()
            if not_include is not None:
                if isinstance(not_include, dict):
                    for key, values in not_include.items():
                        if key not in codes.keys():
                            continue
                        values_codes = self.code_selector(values, custom=self.filtered_names_db)
                        not_include_codes = self.not_include_code_getter(values_codes, self.data)
                        codes[key] = list(set(codes[key]) - set(not_include_codes))
                else:
                    values_codes = self.code_selector(not_include, custom=self.filtered_names_db)
                    not_include_codes = self.not_include_code_getter(values_codes, self.data)
                    codes = list(set(codes) - set(not_include_codes))
        self._test_codes(codes, celltype, codes_type=type(codes).__name__)
        return codes
