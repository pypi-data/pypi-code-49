#!/usr/bin/env python

""" figures_1.py: Functions for generating the figures numbered 1 """

import inspect
import logging
import math
import os
import re
import time

import classes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import utils.writing_files
from scipy.special import comb
from utils import util

from VEnCode.common_variables import three_donors_cell_list


# region "Figures for paper"
def figure_1(file, file_type, cell_list, combinations_number, samples_to_take, reps, threshold=90,
             expression=1, celltype_exclude=None, not_include=None, multi_plot=True, sample_types="primary cells",
             optional_folder="/Figure 1/Test lines/", include_problems=False):
    # Set up logging:
    logging.basicConfig(filename="./Figure 1/log {}_celltp k_{}.txt".format(len(cell_list), combinations_number),
                        level=logging.DEBUG, format="{asctime} - {levelname} - {message}", filemode='w', style="{")
    logger = logging.getLogger(__name__)
    logger.info("Starting figure_1 function with {} cell types and analysing sets of up to {} "
                "promoters".format(len(cell_list), combinations_number))
    # First, import only the necessary data, remove universal RNA pools and select the desired sample_type:
    start_time = time.time()
    raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                           skiprows=1831, nrows=1000)  # nrows=x if we want to load only a few rows
    data_1 = raw_data.drop(raw_data.index[[0, 1]])
    universal_rna = util.fantom_code_selector(file_type, data_1, "universal", not_include=None)
    data_1.drop(universal_rna, axis=1, inplace=True)
    to_keep = util.fantom_sample_category_selector("sample types - FANTOM5.csv", sample_types)
    data = pd.DataFrame(index=data_1.index.values)
    for sample in to_keep:
        data_temp = data_1.filter(regex=sample)
        data = data.join(data_temp)
    # Exclude some specific, on-demand, celltypes from the data straight away:
    if isinstance(celltype_exclude, list):
        codes_exclude = util.fantom_code_selector(file_type, data, celltype_exclude)
        print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
        data.drop(codes_exclude, axis=1, inplace=True)
    new_ven = {}
    # Starting loop through all cell types:
    for celltype in cell_list:
        print("\n", "Starting {}".format(celltype), sep="-> ")
        if isinstance(celltype_exclude, dict):
            celltype_to_exclude = celltype_exclude.get(celltype)
        else:
            celltype_to_exclude = None
        if not_include is not None:
            not_celltype = not_include.get(celltype)
        else:
            not_celltype = None
        if celltype_to_exclude is not None:
            ven = util.sorted_ven_robustness_test(file, file_type, celltype, combinations_number, samples_to_take, reps,
                                                  threshold=threshold, expression=expression,
                                                  celltype_exclude=celltype_to_exclude,
                                                  not_include=not_celltype, multi_plot=multi_plot, init_data=data,
                                                  optional_folder=optional_folder, include_problems=include_problems)
        else:
            ven = util.sorted_ven_robustness_test(file, file_type, celltype, combinations_number, samples_to_take, reps,
                                                  threshold=threshold, expression=expression,
                                                  celltype_exclude=None,
                                                  not_include=not_celltype, multi_plot=multi_plot, init_data=data,
                                                  optional_folder=optional_folder, include_problems=include_problems)
        for k in ven:
            if k in new_ven:
                new_ven[k].append(ven[k][0])
            else:
                new_ven[k] = [ven[k][0]]
    new_ven_2 = {k: [np.mean(v, dtype=np.float64), np.std(v, dtype=np.float64) / math.sqrt(len(v))] for (k, v) in
                 zip(new_ven.keys(), new_ven.values())}
    # plotting:
    folder = "/Figure 1/"
    file_name = u"/Perc VenC of 1 zero - k={} - {} {}".format(combinations_number, len(cell_list), sample_types)
    file_name_dotplot = u"/Perc VenC of 1 zero_dotplot - k={} - {} {}".format(combinations_number, len(cell_list),
                                                                              sample_types)
    title = "Probability of VEnCode from random promoters sample of size k"
    utils.writing_files.write_dict_to_csv(file_name + ".csv", new_ven_2, folder)
    utils.writing_files.write_dict_to_csv(file_name_dotplot + ".csv", new_ven, folder)
    label = "Average of {} cell types".format(len(cell_list))
    fig, path = util.errorbar_plot(new_ven_2, folder, file_name, label, title=title, multiple=False)
    fig.savefig(path)
    plt.close(fig)
    fig_2, path_2 = util.box_plotting_from_dict(new_ven, file_name_dotplot, folder, title)
    fig_2.savefig(path_2, bbox_inches='tight')
    plt.close(fig_2)
    # finish:
    print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return


def ven_percentage_per_celltype(file, file_type, cell_list, combinations_number, samples_to_take, reps, threshold=90,
                                expression=1, celltype_exclude=None, not_include=None,
                                sample_types="primary cells"):
    # Set up logging:
    folder = "./Percentage/"
    if not os.path.exists(folder):
        os.makedirs(folder)
    log_file = "./Percentage/log {}_cell k_{}.txt".format(len(cell_list), combinations_number)
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format="{asctime} - {levelname} - {message}",
                        filemode='w', style="{")
    logger = logging.getLogger(__name__)
    logger.info("Starting ven_percentage_per_celltype function with {} cell types and analysing sets {} "
                "promoters".format(len(cell_list), combinations_number))
    # First, import only the necessary data, remove universal RNA pools and select the desired sample_type:
    start_time = time.time()
    raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                           skiprows=1831, nrows=1000)  # nrows=x if we want to load only a few rows
    data_1 = raw_data.drop(raw_data.index[[0, 1]])
    universal_rna = util.fantom_code_selector(file_type, data_1, "universal", not_include=None)
    data_1.drop(universal_rna, axis=1, inplace=True)
    to_keep = util.fantom_sample_category_selector("sample types - FANTOM5.csv", sample_types)
    data = pd.DataFrame(index=data_1.index.values)
    for sample in to_keep:
        data_temp = data_1.filter(regex=sample)
        data = data.join(data_temp)
    # Exclude some specific, on-demand, celltypes from the data straight away:
    if isinstance(celltype_exclude, list):
        codes_exclude = util.fantom_code_selector(file_type, data, celltype_exclude)
        print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
        data.drop(codes_exclude, axis=1, inplace=True)
    # Starting loop through all cell types:
    ven_percent = {}
    if not isinstance(cell_list, list):
        cell_list = [cell_list]
    for celltype in cell_list:
        print("\n", "Starting {}".format(celltype), sep="-> ")
        if not_include is not None:
            not_celltype = not_include.get(celltype)
        else:
            not_celltype = None
        codes = util.fantom_code_selector(file_type, data, celltype, not_include=not_celltype)
        print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
        # Applying filters:
        filters = util.df_filter_by_expression_and_percentile(data, codes, expression, 2, threshold)
        # Getting VEnCode percentages:
        try:
            ven = {}
            for i in range(reps):
                c = 0
                for n in range(samples_to_take):
                    if n >= comb(int(filters.shape[0]), combinations_number, exact=False):
                        break
                    sample = filters.sample(n=combinations_number)
                    sample_dropped = sample.drop(codes, axis=1).values
                    c = util.assess_vencode_one_zero(c, sample_dropped)
                ven[i] = (c / samples_to_take) * 100  # could be a list but dicts are faster
                print("Finished rep {0} in celltype = {1}".format(i, celltype))
            ven_values = list(ven.values())
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            break
        ven_percent[celltype] = ven_values
    # plotting:
    folder = "/Percentage/"
    file_name_dotplot = u"/Perc VenC dotplot - k={} - {} {}".format(combinations_number, len(cell_list),
                                                                    sample_types)
    title = "Probability of VEnCode from {} promoters sample of size {}".format(combinations_number, reps)
    utils.writing_files.write_dict_to_csv(file_name_dotplot + ".csv", ven_percent, folder)
    fig, path = util.box_plotting_from_dict(ven_percent, file_name_dotplot, folder, title)
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)
    # finish:
    print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return


def figure_1_non_combinatory_algorithm(file, file_type, cell_list, combinations_number,
                                       threshold=90, expression=1, celltype_exclude=None, not_include=None,
                                       sample_types="primary cells", mode="count", multi=True):
    """
    Returns number/percentage of VEnCodes found for each cell-type (cell_list), at a specific promoter combination
    number.
    :param file: file with promoter/enhancer expression data over
    :param file_type: either "Promoters" or "Enhancers"
    :param cell_list: list of cell types to get VEnCodes from
    :param combinations_number: number of promoters/enhancers that constitute a VEnCode
    :param threshold: Minimum percentage of zeros for promoters to be included in analysis
    :param expression: Minimum promoter expression levels (in queried celltype) to include in analysis
    :param celltype_exclude: List of cell-types to exclude from the data set completely
    :param not_include: Dictionary of list or string of words that allow to exclude similarly named celltypes
    :param sample_types: either "primary cells", "tissues", "cell lines", "time courses" or "fractionations and perturbations"
    :param mode: either "count" or "percentage", to get the total number or the percentage of VEnCodes, respectively
    :param multi: True or False, either do the analysis for multiple combinations numbers or not, respectively
    """

    # Set up logging:
    parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    logging.basicConfig(
        filename=parent_path + "/Figure 1/log {}_celltp k_{}.txt".format(len(cell_list), combinations_number),
        level=logging.DEBUG, format="{asctime} - {levelname} - {message}", filemode='w', style="{")
    logger = logging.getLogger(__name__)
    logger.info("Starting figure_1 function with %s cell types and analysing sets of %s "
                "promoters", len(cell_list), combinations_number)
    # First, import only the necessary data, remove universal RNA pools and select the desired sample_type:
    start_time = time.time()
    raw_data = pd.read_csv(parent_path + "/Files/" + file, sep="\t", index_col=0,
                           skiprows=1831)  # nrows=x if we want to load only a few rows
    data_1 = raw_data.drop(raw_data.index[[0, 1]])
    universal_rna = util.fantom_code_selector(file_type, data_1, "universal", not_include=None)
    data_1.drop(universal_rna, axis=1, inplace=True)
    to_keep = util.fantom_sample_category_selector("sample types - FANTOM5.csv", sample_types)
    data = pd.DataFrame(index=data_1.index.values)
    for sample in to_keep:
        data_temp = data_1.filter(regex=sample)
        data = data.join(data_temp)
    # Exclude some specific, on-demand, cell-types from the data straight away:
    if isinstance(celltype_exclude, list):
        codes_exclude = util.fantom_code_selector(file_type, data, celltype_exclude)
        print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
        data.drop(codes_exclude, axis=1, inplace=True)
    # Starting loop through all cell-types:
    calculated_vencodes = {}

    for celltype in cell_list:
        print("\n", "Starting {}".format(celltype), sep="-> ")
        logger.info("Starting %s", celltype)
        if not_include is not None:
            not_celltype = not_include.get(celltype)
        else:
            not_celltype = None
        codes = util.fantom_code_selector(file_type, data, celltype, not_include=not_celltype)
        print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
        filter_2 = util.df_filter_by_expression_and_percentile(data, codes, expression, 2, threshold)
        filter_2 = filter_2.applymap(lambda x: 0 if x == 0 else 1)
        nodes = util.node_calculator(filter_2.drop(codes, axis=1))
        if multi:
            for number in range(2, combinations_number + 1):
                try:
                    calculated_vencodes[number]
                except KeyError:
                    calculated_vencodes[number] = []
                ven_combinations = util.number_of_combination_from_nodes(nodes, len(filter_2.index), number)
                logger.info("Number of VEnCodes found: %s for k=%s", ven_combinations, number)
                if mode == "count":
                    calculated_vencodes[number].append(ven_combinations)
                elif mode == "percentage":
                    total_comb = comb(len(filter_2.index), combinations_number, exact=False)
                    calculated_vencodes[number] = ven_combinations / total_comb * 100
        else:
            ven_combinations = util.number_of_combination_from_nodes(nodes, len(filter_2.index), combinations_number)
            logger.info("Number of VEnCodes found: %s for k=%s", ven_combinations, combinations_number)
            if mode == "count":
                calculated_vencodes[celltype] = ven_combinations
            elif mode == "percentage":
                total_comb = comb(len(filter_2.index), combinations_number, exact=False)
                calculated_vencodes[celltype] = ven_combinations / total_comb * 100

    # saving in .CSV:
    folder = "/Figure 1/"
    file_name = u"/Abs_perc VEnC - k={} - {} {}".format(combinations_number, len(cell_list), sample_types)
    if multi:
        utils.writing_files.write_dict_to_csv(file_name + ".csv", calculated_vencodes, folder, path="parent")
    else:
        utils.writing_files.write_one_value_dict_to_csv(file_name + ".csv", calculated_vencodes, folder)
    # plotting:
    if multi:
        title = "VEnCode retrieval rate"
        fig, path = util.box_plotting_from_dict(calculated_vencodes, file_name, folder, title, path="parent")
        fig.savefig(path, bbox_inches='tight')
        plt.close(fig)
    else:
        path = parent_path + folder + file_name
        plt.bar(range(len(calculated_vencodes)), calculated_vencodes.values(), align="center", color="burlywood")
        plt.xticks(range(len(calculated_vencodes)), list(calculated_vencodes.keys()))
        plt.savefig(path)

    # finish:
    print("Process Quick finished in %s seconds" % (time.time() - start_time))


class Enhancers:
    def __init__(self, file, names_db, celltype, celltype_exclude=None, not_include=None, partial_exclude=None,
                 sample_types="primary cells"):
        self.parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.names_db = names_db
        self.celltype = celltype
        self.sample_types = sample_types
        self.file_type = "Enhancers"  # may not be needed later when functions become inside enhancers class
        self.database = classes.Enhancers(file, names_db, celltype, celltype_exclude=celltype_exclude,
                                          not_include=not_include, partial_exclude=partial_exclude,
                                          sample_types=sample_types)

    def get_all_vencodes(self, combinations_number, threshold=90, expression=1, mode="count",
                         multi=False, at_least_one=False):
        # set up logging:
        specific_path = "/Figure 1/log {}_celltp k_{}-{}.log".format(len(self.celltype), combinations_number,
                                                                     self.file_type)
        logger = self.database.logging(specific_path)
        logger.info("Starting get_all_vencodes function with %s cell types, analysing sets of %s enhancers with: t"
                    "hreshold=%s and expression=%s",
                    len(self.celltype), combinations_number, threshold, expression)
        logger.debug("Data: %s enhancers and %s samples", self.database.data.shape[0], self.database.data.shape[1])
        logger.info("Cell types to get VEnCodes:")
        for cell, codes in self.database.codes.items():
            logger.info("%s (%s codes) -> %s", cell, len(codes), codes)
        # Start the loop through all expression levels:
        if at_least_one:
            calculated_vencodes = self.database.at_least_one_vencode(self.database, combinations_number, expression,
                                                                     threshold, multi=multi)
        else:
            calculated_vencodes = self.database.non_combinatory_loop(self.database, combinations_number, expression,
                                                                     threshold, multi=multi, mode=mode)
        # saving in .CSV:
        folder = "/Figure 1/"
        file_name = u"/VEnC - k={} {}- {} {}".format(combinations_number, self.file_type, len(self.celltype),
                                                     self.sample_types)
        if multi:
            utils.writing_files.write_dict_to_csv(file_name + ".csv", calculated_vencodes, folder, path="parent")
        else:
            utils.writing_files.write_one_value_dict_to_csv(file_name + ".csv", calculated_vencodes, folder)
        # plotting:
        if multi:
            title = "VEnCode retrieval rate"
            fig, path = util.box_plotting_from_dict(calculated_vencodes, file_name, folder, title, path="parent")
            fig.savefig(path, bbox_inches='tight')
            plt.close(fig)
        else:
            path = self.parent_path + folder + file_name
            plt.bar(range(len(calculated_vencodes)), calculated_vencodes.values(), align="center", color="burlywood")
            plt.xticks(range(len(calculated_vencodes)), list(calculated_vencodes.keys()))
            plt.savefig(path)
        logger.info("Finished")

    def get_all_vencodes_2(self, combinations_number, threshold=90, expression=1, mode="count",
                           multi=False, at_least_one=False):
        # set up logging:
        specific_path = "/Figure 1/log {}_celltp k_{}-{}.log".format(len(self.celltype), combinations_number,
                                                                     self.file_type)
        logger = self.database.logging(specific_path)
        logger.info(
            "Starting get_all_vencodes function with %s cell types, analysing sets of %s enhancers with: threshold=%s "
            "and expression=%s",
            len(self.celltype), combinations_number, threshold, expression)
        logger.debug("Data: %s %s and %s samples", self.database.data.shape[0], self.file_type,
                     self.database.data.shape[1])
        logger.info("Cell types to get VEnCodes:")
        for cell, codes in self.database.codes.items():
            logger.info("%s (%s codes) -> %s", cell, len(codes), codes)
        # Vars for saving in .CSV:
        folder = "/Figure 1/"
        # Start the loop through all expression levels:
        if at_least_one:
            if multi:
                for k in combinations_number:
                    calculated_vencodes = self.database.at_least_one_vencode(self.database, k, expression, threshold)
                    file_name = u"/VEnC - k={} {}- {} {}".format(k, self.file_type,
                                                                 len(self.celltype),
                                                                 self.sample_types)
                    utils.writing_files.write_one_value_dict_to_csv(file_name + ".csv", calculated_vencodes, folder)
            else:
                calculated_vencodes = self.database.at_least_one_vencode(self.database, combinations_number, expression,
                                                                         threshold)
        else:
            calculated_vencodes = self.database.non_combinatory_loop(self.database, combinations_number, expression,
                                                                     threshold, mode=mode)
        # Saving in .CSV
        file_name = u"/VEnC - k={} {}- {} {}".format(combinations_number, self.file_type, len(self.celltype),
                                                     self.sample_types)
        # if multi:
        #     Defs.write_dict_to_csv(file_name + ".csv", calculated_vencodes, folder, path="parent")
        if not multi:
            utils.writing_files.write_one_value_dict_to_csv(file_name + ".csv", calculated_vencodes, folder)
        # plotting:
        # if multi:
        #     title = "VEnCode retrieval rate"
        #     fig, path = Defs.box_plotting_from_dict(calculated_vencodes, file_name, folder, title, path="parent")
        #     fig.savefig(path, bbox_inches='tight')
        #     plt.close(fig)
        if not multi:
            path = self.parent_path + folder + file_name
            plt.bar(range(len(calculated_vencodes)), calculated_vencodes.values(), align="center", color="burlywood")
            plt.xticks(range(len(calculated_vencodes)), list(calculated_vencodes.keys()))
            plt.savefig(path)
        logger.info("Finished")

    def figure_1(self, combinations_number, samples_to_take, reps, threshold=90, expression=1,
                 multi_plot=True, optional_folder="/Figure 1/", include_problems=False):
        # set up logging:
        """

        :param combinations_number:
        :param samples_to_take:
        :param reps:
        :param threshold:
        :param expression:
        :param multi_plot:
        :param optional_folder:
        :param include_problems: True if you want to create files with all cell types that prevent VEnCodes for
        each queried cell type. IMPORTANT: only works with single k, ex: [4]
        :return:
        """
        specific_path = "/Figure 1/log {} {}_celltp k_{}-{}.log".format(inspect.currentframe().f_code.co_name,
                                                                        len(self.celltype), combinations_number,
                                                                        self.file_type)
        logger = self.database.logging(specific_path)
        logger.info("Starting %s function with %s cell types, analysing sets of %s enhancers with: threshold=%s "
                    "and expression=%s", inspect.currentframe().f_code.co_name, len(self.celltype),
                    combinations_number, threshold, expression)
        logger.debug("Data: %s enhancers and %s samples", self.database.data.shape[0], self.database.data.shape[1])
        logger.info("Cell types to get VEnCodes:")
        # Starting loop through all cell types:
        new_ven = {}
        for celltype in self.celltype:
            print("\n", "Starting {}".format(celltype), sep="-> ")
            logger.info("-> Starting %s", celltype)
            codes = self.database.codes.get(celltype)
            ven = self.database.sorted_ven_robustness_test(self.database.data, codes, celltype, combinations_number,
                                                           samples_to_take, reps, self.file_type, threshold=threshold,
                                                           expression=expression, multi_plot=multi_plot,
                                                           folder=optional_folder,
                                                           include_problems=include_problems)
            for k in ven:
                if k in new_ven:
                    new_ven[k].append(ven[k][0])
                else:
                    new_ven[k] = [ven[k][0]]
        new_ven_2 = {k: [np.mean(v, dtype=np.float64), np.std(v, dtype=np.float64) / math.sqrt(len(v))] for (k, v) in
                     zip(new_ven.keys(), new_ven.values())}
        # plotting:
        folder = "/Figure 1/"
        file_name = u"/Perc VenC - k={} {}- {} {}".format(combinations_number, self.file_type, len(self.celltype),
                                                          self.sample_types)
        file_name_dotplot = u"/Perc VenC dotplot - k={} {}- {} {}".format(combinations_number, self.file_type,
                                                                          len(self.celltype), self.sample_types)
        title = "VEnCode retrieval rate"
        utils.writing_files.write_dict_to_csv(file_name + ".csv", new_ven_2, folder, path="parent")
        utils.writing_files.write_dict_to_csv(file_name_dotplot + ".csv", new_ven, folder, path="parent")
        label = "Average of {} cell types".format(len(self.celltype))
        fig, path = util.errorbar_plot(new_ven_2, folder, file_name, label, title=title, multiple=False, path="parent")
        fig.savefig(path)
        plt.close(fig)
        fig_2, path_2 = util.box_plotting_from_dict(new_ven, file_name_dotplot, folder, title, path="parent")
        fig_2.savefig(path_2, bbox_inches='tight')
        plt.close(fig_2)
        # finish:
        logger.info("Finished")
        return


class Promoters:
    def __init__(self, file, celltype, celltype_exclude=None, not_include=None, partial_exclude=None,
                 sample_types="primary cells", second_parser=None, nrows=None):
        self.parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.celltype = celltype
        self.sample_types = sample_types
        self.file_type = "Promoters"  # may not be needed later when functions become inside enhancers class
        self.database = classes.Promoters(file, celltype, celltype_exclude=celltype_exclude,
                                          not_include=not_include, partial_exclude=partial_exclude,
                                          sample_types=sample_types, second_parser=second_parser, nrows=nrows)

    def get_all_vencodes(self, combinations_number, threshold=90, expression=1, mode="count",
                         multi=False, at_least_one=False):
        # set up logging:
        specific_path = "/Figure 1/log {}_celltp k_{}-{}.log".format(len(self.celltype), combinations_number,
                                                                     self.file_type)
        logger = self.database.logging(specific_path)
        logger.info(
            "Starting get_all_vencodes function with %s cell types, analysing sets of %s promoters with: threshold=%s "
            "and expression=%s",
            len(self.celltype), combinations_number, threshold, expression)
        logger.debug("Data: %s %s and %s samples", self.database.data.shape[0], self.file_type,
                     self.database.data.shape[1])
        logger.info("Cell types to get VEnCodes:")
        for cell, codes in self.database.codes.items():
            logger.info("%s (%s codes) -> %s", cell, len(codes), codes)
        # Vars for saving in .CSV:
        folder = "/Figure 1/"
        if isinstance(self.sample_types, list):
            if len(self.sample_types) == 2:
                sample_type = self.sample_types[1]
            else:
                sample_type = self.sample_types[0]
        else:
            sample_type = self.sample_types
        # Start the loop through all expression levels:
        if at_least_one:
            if multi:
                for k in combinations_number:
                    calculated_vencodes = self.database.at_least_one_vencode(self.database, k, expression, threshold)
                    file_name = u"/VEnC - k={} {}- {} {}".format(k, self.file_type,
                                                                 len(self.celltype),
                                                                 sample_type)
                    utils.writing_files.write_one_value_dict_to_csv(file_name + ".csv", calculated_vencodes, folder)
            else:
                calculated_vencodes = self.database.at_least_one_vencode(self.database, combinations_number, expression,
                                                                         threshold)
        else:
            calculated_vencodes = self.database.non_combinatory_loop(self.database, combinations_number, expression,
                                                                     threshold, mode=mode)
        if not multi:
            # Saving in .CSV
            file_name = u"/VEnC - k={} {}- {} {}".format(combinations_number, self.file_type, len(self.celltype),
                                                         sample_type)
            utils.writing_files.write_one_value_dict_to_csv(file_name + ".csv", calculated_vencodes, folder)
        if not multi:
            path = self.parent_path + folder + file_name
            plt.bar(range(len(calculated_vencodes)), calculated_vencodes.values(), align="center", color="burlywood")
            plt.xticks(range(len(calculated_vencodes)), list(calculated_vencodes.keys()))
            plt.savefig(path)
        logger.info("Finished")

    def check_size(self, tpm):
        print("Initial size:", self.database.data.shape, sep=" -> ")
        df = pd.DataFrame()
        for column in self.database.data.columns:
            filtering = self.database.data[column] > tpm
            filtering = self.database.data[filtering]
            final_df = df.append(filtering)
        print("Bigger than {}".format(tpm), final_df.shape, sep=" -> ")

    def check_cell_list(self, no_donors=False):
        """ still incomplete but can help """
        columns = self.database.data.columns.tolist()
        celltypes = []
        for celltype in columns:
            new = celltype.replace("tpm.", "").replace("%20", " ").replace("%28", "(").replace("%29", ")").replace(
                "%2c", ",").replace("%2b", "+")
            if no_donors:
                try:
                    index = new.index(", donor")
                    new = new[:index]
                except ValueError:
                    new = new
                try:
                    index = new.index(", pool")
                    new = new[:index]
                except ValueError:
                    new = new
                celltypes.append(new)
                try:
                    index = new.index(", biol")
                    new = new[:index]
                except ValueError:
                    new = new
                try:
                    index = new.index(" - treated")
                    new = new[:index]
                except ValueError:
                    new = new
                celltypes.append(new)
        if no_donors:
            celltypes = list(set(celltypes))
        print(len(celltypes), celltypes)

    def figure_cancer(self, combinations_number, threshold=90, expression=1):
        # set up logging:
        specific_path = "/Figure Cancer/log {}_celltp k_{}-{}.log".format(len(self.celltype), combinations_number,
                                                                          self.file_type)
        logger = self.database.logging(specific_path)
        logger.info(
            "Starting get_all_vencodes function with %s cell types, analysing sets of %s enhancers with: threshold=%s "
            "and expression=%s",
            len(self.celltype), combinations_number, threshold, expression)
        logger.debug("Data: %s %s and %s samples", self.database.data.shape[0], self.file_type,
                     self.database.data.shape[1])
        logger.info("Cell types to get VEnCodes:")
        for cell, codes in self.database.codes.items():
            logger.info("%s (%s codes) -> %s", cell, len(codes), codes)
        # Vars for saving in .CSV:
        folder = "/Figure Cancer/"
        pass


class Graphs:
    def __init__(self):
        pass

    @staticmethod
    def file_appender_for_heat_map(path, save=True, plot=True):
        # Data prep:
        file_list = util.file_names_to_list(path)
        final = pd.DataFrame()
        for file in file_list:
            data = pd.read_csv(file, sep=";", index_col=None)
            index = re.sub("D:.*for ", "", file)
            index = re.sub(" - 2x.*.csv", "", index)
            data.rename(index={0: index}, inplace=True)
            final = pd.concat((final, data))
            final.fillna(0, inplace=True)
        # optional: Save the file
        if save:
            current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            file_path = current_path + "/Figure 1/All together.csv"
            final.to_csv(file_path, sep=";", na_rep=0)
        # optional: plotting
        if plot:
            fig_1 = plt.figure(1)
            ax1 = fig_1.add_subplot(111, xlabel="Celltypes",
                                    ylabel="Celltypes")  # xticklabels=final.columns, yticklabels=final.index
            img_1 = ax1.imshow(final, interpolation='nearest', cmap="hot")
            # img_1.grid(True)
            plt.colorbar(img_1, orientation="horizontal")
            plt.show()
        pass

    @staticmethod
    def heatmap_from_file(path, orientation="vertical", sep=";", interpolation="None", simple=False, xlabel=None):
        # open file:
        current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        file_path = current_path + path
        file = pd.read_csv(file_path, sep=sep, index_col=0)
        # plotting:
        fig_1 = plt.figure(1, dpi=600)
        if simple:
            ax1 = fig_1.add_subplot(111)
        else:
            ax1 = fig_1.add_subplot(111, xticklabels=file.columns, yticklabels=file.index,
                                    xticks=range(len(file.columns)),
                                    yticks=range(len(file.index)))
        img_1 = ax1.imshow(file, interpolation=interpolation, cmap="hot")
        if xlabel is not None:
            xlabels = xlabel
            ax1.set_xticklabels(xlabels)
        plt.colorbar(img_1, orientation=orientation, aspect=20)
        # Move left and bottom spines outward by 10 points
        ax1.spines['left'].set_position(('outward', 10))
        ax1.spines['bottom'].set_position(('outward', 10))
        # Hide the right and top spines
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        # Only show ticks on the left and bottom spines
        ax1.yaxis.set_ticks_position('left')
        ax1.xaxis.set_ticks_position('bottom')
        # change ticks properties
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=7)
        plt.setp(ax1.yaxis.get_majorticklabels(), fontsize=7)
        # save the figure
        final_path = file_path.replace(".csv", "-") + str(interpolation) + ".png"
        plt.savefig(final_path, bbox_inches='tight', transparent=True, dpi="figure")
        plt.close()


# endregion "Figures for paper"


# region "Global Variables"

# region "Human"
complete_primary_cell_list = ["Adipocyte - breast", "Adipocyte - omental", "Adipocyte - perirenal",
                              "Adipocyte - subcutaneous", "Alveolar Epithelial Cells", "Amniotic Epithelial Cells",
                              "amniotic membrane cells", "Anulus Pulposus Cell", "Astrocyte - cerebellum",
                              "Astrocyte - cerebral cortex", "Basophils", "Bronchial Epithelial Cell",
                              "Cardiac Myocyte", "CD133+ stem cells - adult bone marrow derived",
                              "CD133+ stem cells - cord blood derived",
                              "CD14+ monocyte derived endothelial progenitor cells", "CD14+ Monocytes",
                              "CD14+ CD16- Monocytes", "CD14+ CD16+ Monocytes", "CD14- CD16+ Monocytes",
                              "CD19+ B Cells", "CD34 cells differentiated to erythrocyte lineage", "CD34+ Progenitors",
                              "CD34+ stem cells - adult bone marrow derived", "CD4+ T Cells",
                              "CD4+CD25+CD45RA- memory regulatory T cells", "CD4+CD25+CD45RA+ naive regulatory T cells",
                              "CD4+CD25-CD45RA- memory conventional T cells",
                              "CD4+CD25-CD45RA+ naive conventional T cells", "CD8+ T Cells", "Chondrocyte",
                              "chorionic membrane cells", "Ciliary Epithelial Cells", "common myeloid progenitor CMP",
                              "Corneal Epithelial Cells", "Dendritic Cells - monocyte immature derived",
                              "Dendritic Cells - plasmacytoid", "Endothelial Cells - Aortic",
                              "Endothelial Cells - Artery", "Endothelial Cells - Lymphatic",
                              "Endothelial Cells - Microvascular", "Endothelial Cells - Thoracic",
                              "Endothelial Cells - Umbilical vein", "Endothelial Cells - Vein", "Eosinophils",
                              "Esophageal Epithelial Cells", "Fibroblast - Aortic Adventitial", "Fibroblast - Cardiac",
                              "Fibroblast - Choroid Plexus", "Fibroblast - Conjunctival", "Fibroblast - Dermal",
                              "Fibroblast - Gingival", "Fibroblast - Lung", "Fibroblast - Lymphatic",
                              "Fibroblast - Mammary", "Fibroblast - Periodontal Ligament",
                              "Fibroblast - Pulmonary Artery", "Fibroblast - skin", "Fibroblast - Villous Mesenchymal",
                              "gamma delta positive T cells", "Gingival epithelial cells",
                              "granulocyte macrophage progenitor", "Hair Follicle Dermal Papilla Cells",
                              "Hair Follicle Outer Root Sheath Cells", "Hepatic Sinusoidal Endothelial Cells",
                              "Hepatic Stellate Cells (lipocyte)", "Hepatocyte", "immature langerhans cells",
                              "Intestinal epithelial cells (polarized)", "Iris Pigment Epithelial Cells",
                              "Keratinocyte - epidermal", "Keratinocyte - oral", "Keratocytes", "Lens Epithelial Cells",
                              "Macrophage - monocyte derived", "Mallassez-derived cells", "Mammary Epithelial Cell",
                              "Mast cell", "mature adipocyte", "Melanocyte", "Meningeal Cells",
                              "mesenchymal precursor cell - adipose", "mesenchymal precursor cell - bone marrow",
                              "mesenchymal precursor cell - cardiac", "Mesenchymal stem cells - adipose",
                              "Mesenchymal Stem Cells - amniotic membrane", "Mesenchymal Stem Cells - bone marrow",
                              "Mesenchymal stem cells - hepatic", "Mesenchymal stem cells - umbilical",
                              "Mesenchymal Stem Cells - Vertebral", "Mesenchymal Stem Cells - Wharton Jelly",
                              "Mesothelial Cells", "migratory langerhans cells",
                              "Multipotent Cord Blood Unrestricted Somatic Stem Cells", "Myoblast",
                              "nasal epithelial cells", "Natural Killer Cells", "Neural stem cells", "Neurons",
                              "Neutrophil", "Nucleus Pulposus Cell", "Olfactory epithelial cells",
                              "Oligodendrocyte - precursors", "Osteoblast", "Pancreatic stromal cells", "Pericytes",
                              "Perineurial Cells", "Placental Epithelial Cells",
                              "Preadipocyte - breast", "Preadipocyte - omental", "Preadipocyte - perirenal",
                              "Preadipocyte - subcutaneous", "Preadipocyte - visceral", "promyelocytes",
                              "Prostate Epithelial Cells", "Prostate Stromal Cells", "Renal Cortical Epithelial Cells",
                              "Renal Epithelial Cells", "Renal Glomerular Endothelial Cells", "Renal Mesangial Cells",
                              "Renal Proximal Tubular Epithelial Cell", "Retinal Pigment Epithelial Cells",
                              "salivary acinar cells", "Schwann Cells", "Sebocyte", "Sertoli Cells",
                              "Skeletal Muscle Cells", "Skeletal muscle cells differentiated into Myotubes",
                              "Skeletal Muscle Satellite Cells", "Small Airway Epithelial Cells",
                              "Smooth muscle cells - airway", "Smooth Muscle Cells - Aortic",
                              "Smooth Muscle Cells - Bladder", "Smooth Muscle Cells - Brachiocephalic",
                              "Smooth Muscle Cells - Brain Vascular", "Smooth Muscle Cells - Bronchial",
                              "Smooth Muscle Cells - Carotid", "Smooth Muscle Cells - Colonic",
                              "Smooth Muscle Cells - Coronary Artery", "Smooth Muscle Cells - Esophageal",
                              "Smooth Muscle Cells - Internal Thoracic Artery", "Smooth Muscle Cells - Intestinal",
                              "Smooth Muscle Cells - Prostate", "Smooth Muscle Cells - Pulmonary Artery",
                              "Smooth Muscle Cells - Subclavian Artery", "Smooth Muscle Cells - Tracheal",
                              "Smooth Muscle Cells - Umbilical artery", "Smooth Muscle Cells - Umbilical Vein",
                              "Smooth Muscle Cells - Uterine", "Synoviocyte", "tenocyte", "Trabecular Meshwork Cells",
                              "Tracheal Epithelial Cells", "Urothelial cells"]
complete_primary_non_include_list = {"Adipocyte - breast": "pre", "Adipocyte - omental": "pre",
                                     "Adipocyte - perirenal": "pre", "Adipocyte - subcutaneous": "pre",
                                     "Endothelial Cells - Vein": "Umbilical",
                                     "Renal Epithelial Cells": "Cortical",
                                     "Skeletal Muscle Cells": ["satellite", "differentiated"]}
complete_primary_exclude_list = ["mesenchymal precursor cell - ovarian", "Osteoblast - differentiated",
                                 "Peripheral Blood Mononuclear Cells", "Whole blood"]
complete_primary_jit_exclude_list = {"CD14+ CD16- Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD14+ CD16+ Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD14- CD16+ Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD4+CD25+CD45RA- memory regulatory T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25+CD45RA+ naive regulatory T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25-CD45RA- memory conventional T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25-CD45RA+ naive conventional T cells": ("CD4+ T Cells", "CD25")}

complete_cancer_non_include_list = {"lung adenocarcinoma cell line": "papillary"}

hard_to_get_ven_celltypes_prom = ["Smooth Muscle Cells - Prostate", "Smooth Muscle Cells - Carotid",
                                  "Skeletal Muscle Cells", "Renal Epithelial Cells", "Melanocyte",
                                  "Fibroblast - Periodontal Ligament",
                                  "Fibroblast - Gingival", "Fibroblast - Dermal", "Fibroblast - Cardiac",
                                  "CD8+ T Cells", "CD4+CD25-CD45RA- memory conventional T cells",
                                  "Bronchial Epithelial Cell"]

complete_cancer_cell_type = ['acantholytic squamous carcinoma cell line:HCC1806',
                             'acute lymphoblastic leukemia (B-ALL) cell line:BALL-1',
                             'acute lymphoblastic leukemia (B-ALL) cell line:NALM-6',
                             'acute lymphoblastic leukemia (T-ALL) cell line:HPB-ALL',
                             'acute lymphoblastic leukemia (T-ALL) cell line:Jurkat',
                             'acute myeloid leukemia (FAB M0) cell line:Kasumi-3',
                             'acute myeloid leukemia (FAB M0) cell line:KG-1',
                             'acute myeloid leukemia (FAB M1) cell line:HYT-1',
                             'acute myeloid leukemia (FAB M2) cell line:Kasumi-1',
                             'acute myeloid leukemia (FAB M2) cell line:Kasumi-6',
                             'acute myeloid leukemia (FAB M2) cell line:NKM-1',
                             'acute myeloid leukemia (FAB M3) cell line:HL60',
                             'acute myeloid leukemia (FAB M4) cell line:FKH-1',
                             'acute myeloid leukemia (FAB M4) cell line:HNT-34',
                             'acute myeloid leukemia (FAB M4eo) cell line:EoL-1',
                             'acute myeloid leukemia (FAB M4eo) cell line:EoL-3',
                             'acute myeloid leukemia (FAB M5) cell line:NOMO-1',
                             'acute myeloid leukemia (FAB M5) cell line:P31/FUJ',
                             'acute myeloid leukemia (FAB M5) cell line:THP-1 (fresh)',
                             'acute myeloid leukemia (FAB M5) cell line:U-937 DE-4',
                             'acute myeloid leukemia (FAB M6) cell line:EEB',
                             'acute myeloid leukemia (FAB M6) cell line:F-36E',
                             'acute myeloid leukemia (FAB M6) cell line:F-36P',
                             'acute myeloid leukemia (FAB M7) cell line:MKPL-1',
                             'acute myeloid leukemia (FAB M7) cell line:M-MOK', 'adenocarcinoma cell line:IM95m',
                             'adrenal cortex adenocarcinoma cell line:SW-13', 'adult T-cell leukemia cell line:ATN-1',
                             'alveolar cell carcinoma cell line:SW 1573', 'anaplastic carcinoma cell line:8305C',
                             'anaplastic large cell lymphoma cell line:Ki-JK',
                             'anaplastic squamous cell carcinoma cell line:RPMI 2650',
                             'argyrophil small cell carcinoma cell line:TC-YIK', 'astrocytoma cell line:TM-31',
                             'b cell line:RPMI1788', 'B lymphoblastoid cell line: GM12878 ENCODE',
                             'basal cell carcinoma cell line:TE 354.T', 'bile duct carcinoma cell line:HuCCT1',
                             'bile duct carcinoma cell line:TFK-1',
                             'biphenotypic B myelomonocytic leukemia cell line:MV-4-11',
                             'bone marrow stromal cell line:StromaNKtert', 'breast carcinoma cell line:MCF7',
                             'breast carcinoma cell line:MDA-MB-453',
                             'bronchial squamous cell carcinoma cell line:KNS-62',
                             'bronchioalveolar carcinoma cell line:NCI-H358',
                             'bronchioalveolar carcinoma cell line:NCI-H650',
                             'bronchogenic carcinoma cell line:ChaGo-K-1', 'Burkitt lymphoma cell line:DAUDI',
                             'Burkitt lymphoma cell line:RAJI', 'carcinoid cell line:NCI-H1770',
                             'carcinoid cell line:NCI-H727', 'carcinoid cell line:SK-PN-DW',
                             'carcinosarcoma cell line:JHUCS-1', 'cervical cancer cell line:D98-AH2',
                             'cervical cancer cell line:ME-180', 'cholangiocellular carcinoma cell line:HuH-28',
                             'chondrosarcoma cell line:SW 1353', 'choriocarcinoma cell line:BeWo',
                             'choriocarcinoma cell line:SCH', 'choriocarcinoma cell line:T3M-3',
                             'chronic lymphocytic leukemia cell line:SKW-3',
                             'chronic myeloblastic leukemia cell line:KCL-22',
                             'chronic myelogenous leukemia cell line:K562',
                             'chronic myelogenous leukemia cell line:KU812',
                             'chronic myelogenous leukemia cell line:MEG-A2', 'clear cell carcinoma cell line:JHOC-5',
                             'clear cell carcinoma cell line:TEN', 'colon carcinoma cell line:CACO-2',
                             'colon carcinoma cell line:COLO-320', 'cord blood derived cell line:COBL-a untreated',
                             'diffuse large B-cell lymphoma cell line:CTB-1', 'ductal cell carcinoma cell line:KLM-1',
                             'ductal cell carcinoma cell line:MIA Paca2',
                             'embryonic kidney cell line: HEK293/SLAM untreated', 'embryonic pancreas cell line:1B2C6',
                             'embryonic pancreas cell line:1C3D3', 'embryonic pancreas cell line:1C3IKEI',
                             'embryonic pancreas cell line:2C6', 'endometrial carcinoma cell line:OMC-2',
                             'endometrial stromal sarcoma cell line:OMC-9',
                             'endometrioid adenocarcinoma cell line:JHUEM-1', 'epidermoid carcinoma cell line:A431',
                             'epidermoid carcinoma cell line:Ca Ski', 'epithelioid sarcoma cell line:HS-ES-1',
                             'epithelioid sarcoma cell line:HS-ES-2R', 'epitheloid carcinoma cell line: HelaS3 ENCODE',
                             'Ewing sarcoma cell line:Hs 863.T',
                             'extraskeletal myxoid chondrosarcoma cell line:H-EMC-SS', 'fibrosarcoma cell line:HT-1080',
                             'fibrous histiocytoma cell line:GCT TIB-223', 'gall bladder carcinoma cell line:TGBC14TKB',
                             'gall bladder carcinoma cell line:TGBC2TKB', 'gastric adenocarcinoma cell line:MKN1',
                             'gastric adenocarcinoma cell line:MKN45', 'gastric cancer cell line:AZ521',
                             'gastric cancer cell line:GSS', 'gastrointestinal carcinoma cell line:ECC12',
                             'giant cell carcinoma cell line:LU65', 'giant cell carcinoma cell line:Lu99B',
                             'glassy cell carcinoma cell line:HOKUG', 'glioblastoma cell line:A172',
                             'glioblastoma cell line:T98G', 'glioma cell line:GI-1',
                             'granulosa cell tumor cell line:KGN', 'hairy cell leukemia cell line:Mo',
                             'Hep-2 cells mock treated', 'hepatic mesenchymal tumor cell line:LI90',
                             'hepatoblastoma cell line:HuH-6', 'hepatocellular carcinoma cell line: HepG2 ENCODE',
                             'hepatoma cell line:Li-7', 'hereditary spherocytic anemia cell line:WIL2-NS',
                             'Hodgkin lymphoma cell line:HD-Mar2', 'keratoacanthoma cell line:HKA-1',
                             'Krukenberg tumor cell line:HSKTC', 'large cell lung carcinoma cell line:IA-LM',
                             'large cell lung carcinoma cell line:NCI-H460',
                             'large cell non-keratinizing squamous carcinoma cell line:SKG-II-SF',
                             'leiomyoblastoma cell line:G-402', 'leiomyoma cell line:10964C',
                             'leiomyoma cell line:15242A', 'leiomyoma cell line:15425', 'leiomyosarcoma cell line:Hs 5',
                             'lens epithelial cell line:SRA', 'leukemia, chronic megakaryoblastic cell line:MEG-01',
                             'liposarcoma cell line:KMLS-1', 'liposarcoma cell line:SW 872',
                             'lung adenocarcinoma cell line:A549', 'lung adenocarcinoma cell line:PC-14',
                             'lung adenocarcinoma, papillary cell line:NCI-H441', 'lymphangiectasia cell line:DS-1',
                             'lymphoma, malignant, hairy B-cell cell line:MLMA',
                             'malignant trichilemmal cyst cell line:DJM-1', 'maxillary sinus tumor cell line:HSQ-89',
                             'medulloblastoma cell line:D283 Med', 'medulloblastoma cell line:ONS-76',
                             'melanoma cell line:COLO 679', 'melanoma cell line:G-361', 'meningioma cell line:HKBMM',
                             'merkel cell carcinoma cell line:MKL-1', 'merkel cell carcinoma cell line:MS-1',
                             'mesenchymal stem cell line:Hu5/E18', 'mesodermal tumor cell line:HIRS-BM',
                             'mesothelioma cell line:ACC-MESO-1', 'mesothelioma cell line:ACC-MESO-4',
                             'mesothelioma cell line:Mero-14', 'mesothelioma cell line:Mero-25',
                             'mesothelioma cell line:Mero-41', 'mesothelioma cell line:Mero-48a',
                             'mesothelioma cell line:Mero-82', 'mesothelioma cell line:Mero-83',
                             'mesothelioma cell line:Mero-84', 'mesothelioma cell line:Mero-95',
                             'mesothelioma cell line:NCI-H2052', 'mesothelioma cell line:NCI-H226',
                             'mesothelioma cell line:NCI-H2452', 'mesothelioma cell line:NCI-H28',
                             'mesothelioma cell line:No36', 'mesothelioma cell line:ONE58',
                             'mixed mullerian tumor cell line:HTMMT', 'mucinous adenocarcinoma cell line:JHOM-1',
                             'mucinous cystadenocarcinoma cell line:MCAS', 'myelodysplastic syndrome cell line:SKM-1',
                             'myeloma cell line:PCM6', 'myxofibrosarcoma cell line:MFH-ino',
                             'myxofibrosarcoma cell line:NMFH-1', 'neuroblastoma cell line:CHP-134',
                             'neuroblastoma cell line:NB-1', 'neuroblastoma cell line:NBsusSR',
                             'neuroblastoma cell line:NH-12', 'neuroectodermal tumor cell line:FU-RPNT-1',
                             'neuroectodermal tumor cell line:FU-RPNT-2', 'neuroectodermal tumor cell line:TASK1',
                             'neuroepithelioma cell line:SK-N-MC', 'neurofibroma cell line:Hs 53.T',
                             'NK T cell leukemia cell line:KHYG-1',
                             'non T non B acute lymphoblastic leukemia cell line:P30/OHK',
                             'non-small cell lung cancer cell line:NCI-H1385',
                             'normal embryonic palatal mesenchymal cell line:HEPM',
                             'normal intestinal epithelial cell line:FHs 74 Int',
                             'oral squamous cell carcinoma cell line:Ca9-22',
                             'oral squamous cell carcinoma cell line:HO-1-u-1',
                             'oral squamous cell carcinoma cell line:HSC-3',
                             'oral squamous cell carcinoma cell line:SAS', 'osteoclastoma cell line:Hs 706.T',
                             'osteosarcoma cell line:143B/TK', 'osteosarcoma cell line:HS-Os-1',
                             'pagetoid sarcoma cell line:Hs 925', 'pancreatic carcinoma cell line:NOR-P1',
                             'papillary adenocarcinoma cell line:8505C',
                             'papillotubular adenocarcinoma cell line:TGBC18TKB',
                             'peripheral neuroectodermal tumor cell line:KU-SN',
                             'pharyngeal carcinoma cell line:Detroit 562', 'plasma cell leukemia cell line:ARH-77',
                             'pleomorphic hepatocellular carcinoma cell line:SNU-387',
                             'prostate cancer cell line:DU145', 'prostate cancer cell line:PC-3',
                             'rectal cancer cell line:TT1TKB', 'renal cell carcinoma cell line:OS-RC-2',
                             'renal cell carcinoma cell line:TUHR10TKB', 'retinoblastoma cell line:Y79',
                             'rhabdomyosarcoma cell line:KYM-1', 'rhabdomyosarcoma cell line:RMS-YM',
                             'sacrococcigeal teratoma cell line:HTST', 'schwannoma cell line:HS-PSS',
                             'serous adenocarcinoma cell line:JHOS-2', 'serous adenocarcinoma cell line:SK-OV-3-R',
                             'serous cystadenocarcinoma cell line:HTOA', 'signet ring carcinoma cell line:Kato III',
                             'signet ring carcinoma cell line:NUGC-4', 'small cell cervical cancer cell line:HCSC-1',
                             'small cell gastrointestinal carcinoma cell line:ECC10',
                             'small cell lung carcinoma cell line:DMS 144', 'small cell lung carcinoma cell line:LK-2',
                             'small cell lung carcinoma cell line:NCI-H82', 'small cell lung carcinoma cell line:WA-hT',
                             'small-cell gastrointestinal carcinoma cell line:ECC4', 'somatostatinoma cell line:QGP-1',
                             'spindle cell sarcoma cell line:Hs 132.T',
                             'splenic lymphoma with villous lymphocytes cell line:SLVL',
                             'squamous cell carcinoma cell line:EC-GI-10', 'squamous cell carcinoma cell line:JHUS-nk1',
                             'squamous cell carcinoma cell line:T3M-5', 'squamous cell lung carcinoma cell line:EBC-1',
                             'squamous cell lung carcinoma cell line:LC-1F',
                             'squamous cell lung carcinoma cell line:RERF-LC-AI', 'synovial sarcoma cell line:HS-SY-II',
                             'T cell lymphoma cell line:HuT 102 TIB-162', 'teratocarcinoma cell line:NCC-IT-A3',
                             'teratocarcinoma cell line:NCR-G1', 'teratocarcinoma cell line:PA-1',
                             'testicular germ cell embryonal carcinoma cell line:ITO-II',
                             'testicular germ cell embryonal carcinoma cell line:NEC14',
                             'testicular germ cell embryonal carcinoma cell line:NEC15',
                             'testicular germ cell embryonal carcinoma cell line:NEC8',
                             'thymic carcinoma cell line:Ty-82', 'thyroid carcinoma cell line:KHM-5M',
                             'thyroid carcinoma cell line:TCO-1', 'transitional cell carcinoma cell line:Hs 769',
                             'transitional-cell carcinoma cell line:5637',
                             'transitional-cell carcinoma cell line:JMSU1', 'tridermal teratoma cell line:HGRT',
                             'tubular adenocarcinoma cell line:SUIT-2', 'Wilms tumor cell line:G-401',
                             'Wilms tumor cell line:HFWT', 'xeroderma pigentosum b cell line:XPL 17']
merged_lines_cancer_cells = ["acantholytic squamous carcinoma cell line:HCC1806",
                             "acute lymphoblastic leukemia (B-ALL) cell line",
                             "acute lymphoblastic leukemia (T-ALL) cell line",
                             "acute myeloid leukemia (FAB M0) cell line", "acute myeloid leukemia (FAB M1) cell line",
                             "acute myeloid leukemia (FAB M2) cell line", "acute myeloid leukemia (FAB M3) cell line",
                             "acute myeloid leukemia (FAB M4) cell line", "acute myeloid leukemia (FAB M4eo) cell line",
                             "acute myeloid leukemia (FAB M5) cell line", "acute myeloid leukemia (FAB M6) cell line",
                             "acute myeloid leukemia (FAB M7) cell line", "adenocarcinoma cell line:IM95m",
                             "adrenal cortex adenocarcinoma cell line:SW-13", "adult T-cell leukemia cell line:ATN-1",
                             "alveolar cell carcinoma cell line:SW 1573", "anaplastic carcinoma cell line:8305C",
                             "anaplastic large cell lymphoma cell line:Ki-JK",
                             "anaplastic squamous cell carcinoma cell line:RPMI 2650",
                             "argyrophil small cell carcinoma cell line:TC-YIK", "astrocytoma cell line:TM-31",
                             "b cell line:RPMI1788", "B lymphoblastoid cell line: GM12878 ENCODE",
                             "basal cell carcinoma cell line:TE 354", "bile duct carcinoma cell line",
                             "biphenotypic B myelomonocytic leukemia cell line:MV-4-11",
                             "bone marrow stromal cell line:StromaNKtert", "breast carcinoma cell line",
                             "bronchial squamous cell carcinoma cell line:KNS-62",
                             "bronchioalveolar carcinoma cell line", "bronchogenic carcinoma cell line:ChaGo-K-1",
                             "Burkitt lymphoma cell line", "carcinoid cell line", "carcinosarcoma cell line:JHUCS-1",
                             "cervical cancer cell line", "cholangiocellular carcinoma cell line:HuH-28",
                             "chondrosarcoma cell line:SW 1353", "choriocarcinoma cell line",
                             "chronic lymphocytic leukemia cell line:SKW-3",
                             "chronic myeloblastic leukemia cell line:KCL-22", "chronic myelogenous leukemia cell line",
                             "clear cell carcinoma cell line", "colon carcinoma cell line",
                             "cord blood derived cell line:COBL-a untreated",
                             "diffuse large B-cell lymphoma cell line:CTB-1", "ductal cell carcinoma cell line",
                             "embryonic kidney cell line: HEK293/SLAM untreated", "embryonic pancreas cell line",
                             "endometrial carcinoma cell line:OMC-2", "endometrial stromal sarcoma cell line:OMC-9",
                             "endometrioid adenocarcinoma cell line:JHUEM-1", "epidermoid carcinoma cell line",
                             "epithelioid sarcoma cell line", "epitheloid carcinoma cell line: HelaS3 ENCODE",
                             "Ewing sarcoma cell line:Hs 863",
                             "extraskeletal myxoid chondrosarcoma cell line:H-EMC-SS", "fibrosarcoma cell line:HT-1080",
                             "fibrous histiocytoma cell line:GCT TIB-223", "gall bladder carcinoma cell line",
                             "gastric adenocarcinoma cell line", "gastric cancer cell line",
                             "gastrointestinal carcinoma cell line:ECC12", "giant cell carcinoma cell line",
                             "glassy cell carcinoma cell line:HOKUG", "glioblastoma cell line", "glioma cell line:GI-1",
                             "granulosa cell tumor cell line:KGN", "hairy cell leukemia cell line:Mo",
                             "Hep-2 cells mock treated", "hepatic mesenchymal tumor cell line:LI90",
                             "hepatoblastoma cell line:HuH-6", "hepatocellular carcinoma cell line: HepG2 ENCODE",
                             "hepatoma cell line:Li-7", "hereditary spherocytic anemia cell line:WIL2-NS",
                             "Hodgkin lymphoma cell line:HD-Mar2", "keratoacanthoma cell line:HKA-1",
                             "Krukenberg tumor cell line:HSKTC", "large cell lung carcinoma cell line",
                             "large cell non-keratinizing squamous carcinoma cell line:SKG-II-SF",
                             "leiomyoblastoma cell line:G-402", "leiomyoma cell line", "leiomyosarcoma cell line:Hs 5",
                             "lens epithelial cell line:SRA", "leukemia chronic megakaryoblastic cell line:MEG-01",
                             "liposarcoma cell line", "lung adenocarcinoma cell line",
                             "lung adenocarcinoma papillary cell line:NCI-H441", "lymphangiectasia cell line:DS-1",
                             "lymphoma malignant hairy B-cell cell line:MLMA",
                             "malignant trichilemmal cyst cell line:DJM-1", "maxillary sinus tumor cell line:HSQ-89",
                             "medulloblastoma cell line", "melanoma cell line", "meningioma cell line:HKBMM",
                             "merkel cell carcinoma cell line",
                             "mesenchymal stem cell line:Hu5/E18", "mesodermal tumor cell line:HIRS-BM",
                             "mesothelioma cell line", "mixed mullerian tumor cell line:HTMMT",
                             "mucinous adenocarcinoma cell line:JHOM-1", "mucinous cystadenocarcinoma cell line:MCAS",
                             "myelodysplastic syndrome cell line:SKM-1", "myeloma cell line:PCM6",
                             "myxofibrosarcoma cell line", "neuroblastoma cell line", "neuroectodermal tumor cell line",
                             "neuroepithelioma cell line:SK-N-MC", "neurofibroma cell line:Hs 53",
                             "NK T cell leukemia cell line:KHYG-1",
                             "non T non B acute lymphoblastic leukemia cell line:P30/OHK",
                             "non-small cell lung cancer cell line:NCI-H1385",
                             "normal embryonic palatal mesenchymal cell line:HEPM",
                             "normal intestinal epithelial cell line:FHs 74 Int",
                             "oral squamous cell carcinoma cell line", "osteoclastoma cell line:Hs 706",
                             "osteosarcoma cell line", "pagetoid sarcoma cell line:Hs 925",
                             "pancreatic carcinoma cell line:NOR-P1", "papillary adenocarcinoma cell line:8505C",
                             "papillotubular adenocarcinoma cell line:TGBC18TKB",
                             "peripheral neuroectodermal tumor cell line:KU-SN",
                             "pharyngeal carcinoma cell line:Detroit 562", "plasma cell leukemia cell line:ARH-77",
                             "pleomorphic hepatocellular carcinoma cell line:SNU-387", "prostate cancer cell line",
                             "rectal cancer cell line:TT1TKB", "renal cell carcinoma cell line",
                             "retinoblastoma cell line:Y79", "rhabdomyosarcoma cell line",
                             "sacrococcigeal teratoma cell line:HTST", "schwannoma cell line:HS-PSS",
                             "serous adenocarcinoma cell line", "serous cystadenocarcinoma cell line:HTOA",
                             "signet ring carcinoma cell line", "small cell cervical cancer cell line:HCSC-1",
                             "small cell gastrointestinal carcinoma cell line:ECC10",
                             "small cell lung carcinoma cell line",
                             "small-cell gastrointestinal carcinoma cell line:ECC4", "somatostatinoma cell line:QGP-1",
                             "spindle cell sarcoma cell line:Hs 132",
                             "splenic lymphoma with villous lymphocytes cell line:SLVL",
                             "squamous cell carcinoma cell line", "squamous cell lung carcinoma cell line",
                             "synovial sarcoma cell line:HS-SY-II", "T cell lymphoma cell line:HuT 102 TIB-162",
                             "teratocarcinoma cell line", "testicular germ cell embryonal carcinoma cell line",
                             "thymic carcinoma cell line:Ty-82", "thyroid carcinoma cell line",
                             "transitional cell carcinoma cell line", "tridermal teratoma cell line:HGRT",
                             "tubular adenocarcinoma cell line:SUIT-2", "Wilms tumor cell line",
                             "xeroderma pigentosum b cell line:XPL 17"]

labels = ["CD4+CD25+CD45RA+ naive regulatory T cells, donor1",
          "CD4+CD25-CD45RA- memory conventional T cells, donor1",
          "CD14+ monocytes - treated with BCG, donor1",
          "CD14+ monocytes - treated with IFN + N-hexane, donor1",
          "CD14+ monocytes - treated with Trehalose dimycolate (TDM), donor1",
          "CD14+ monocytes - mock treated, donor1",
          "CD14+ monocytes - treated with Group A streptococci, donor1",
          "CD14+ monocytes - treated with lipopolysaccharide, donor1",
          "CD14+ monocytes - treated with Salmonella, donor1",
          "CD14+ monocytes - treated with Cryptococcus, donor1",
          "CD14+ monocytes - treated with Candida, donor1",
          "CD14+ monocytes - treated with B-glucan, donor1",
          "CD14+ monocytes - treated with BCG, donor2",
          "CD14+ monocytes - treated with IFN + N-hexane, donor2",
          "immature langerhans cells, donor2",
          "CD14+ monocytes - treated with Trehalose dimycolate (TDM), donor2",
          "CD14+ monocytes - mock treated, donor2",
          "CD14+ monocytes - treated with Salmonella, donor2",
          "CD14+ monocytes - treated with Cryptococcus, donor2",
          "CD14+ monocytes - treated with Candida, donor2",
          "CD14+ monocytes - treated with B-glucan, donor2",
          "CD14+ monocytes - treated with IFN + N-hexane, donor3",
          "CD14+ monocytes - mock treated, donor3",
          "CD14+ monocytes - treated with Group A streptococci, donor3",
          "CD14+ monocytes - treated with Salmonella, donor3",
          "CD14+ monocytes - treated with Candida, donor3",
          "CD14+ monocytes - treated with B-glucan, donor3",
          "CD4+CD25-CD45RA+ naive conventional T cells, donor3",
          "CD4+CD25+CD45RA+ naive regulatory T cells, donor3",
          "CD14+ monocytes - treated with Group A streptococci, donor2",
          "CD14+ monocytes - treated with lipopolysaccharide, donor2",
          "migratory langerhans cells, donor1",
          "migratory langerhans cells, donor2",
          "immature langerhans cells, donor1",
          "CD4+CD25+CD45RA- memory regulatory T cells, donor3",
          "CD4+CD25-CD45RA- memory conventional T cells, donor3",
          "CD14+CD16- Monocytes, donor3;CD14+CD16+ Monocytes, donor1",
          "CD14+ monocytes - treated with BCG, donor3",
          "CD14+ monocytes - treated with Trehalose dimycolate (TDM), donor3",
          "CD14+ monocytes - treated with lipopolysaccharide, donor3",
          "CD14+ monocytes - treated with Cryptococcus, donor3",
          "migratory langerhans cells, donor3",
          "CD14-CD16+ Monocytes, donor3",
          "CD14+CD16+ Monocytes, donor3"]

# endregion "Human"

# region "mouse"

mouse_complete_primary_cell_list = ['Atoh+ Inner ear hair cells - organ of corti', 'CD326+ enterocyte',
                                    'CD4+CD25+ regulatory T cells', 'CD4+CD25-CD44- naive conventional T cells',
                                    'CD41+ megakaryocyte control', 'common myeloid progenitor CMP', 'GP2+ M cell',
                                    'granulocyte macrophage progenitor GMP', 'Lgr5 positive intestinal stem cells',
                                    'macrophage, bone marrow derived',
                                    'MC1+Gr1+ myeloid-derived suppressor cells control',
                                    'Mouse Aortic Smooth Muscle cells',
                                    'Mouse Aortic Smooth Muscle cells - differentiated', 'Mouse Astrocytes',
                                    'Mouse Astrocytes - cerebellar', 'Mouse Astrocytes - cerebellar',
                                    'Mouse Astrocytes - hippocampus', 'Mouse Astrocytes - hippocampus',
                                    'Mouse Cardiac Myocytes', 'Mouse Cardiac Myocytes', 'Mouse CD19+ B Cells',
                                    'Mouse CD4+ T Cells', 'Mouse CD8+ T Cells', 'Mouse Embryonic fibroblasts',
                                    'Mouse Granule cells', 'Mouse Granule cells',
                                    'Mouse hepatic Sinusoidal Endothelial Cells',
                                    'Mouse hepatic Stellate Cells (lipocyte)', 'Mouse hepatocyte',
                                    'Mouse Meningeal cells', 'Mouse Mesenchymal stem cells - bone marrow derived',
                                    'Mouse Microglia', 'Mouse Neurons - cortical', 'Mouse Neurons - dorsal spinal cord',
                                    'Mouse Neurons - hippocampal', 'Mouse Neurons - raphe', 'Mouse Neurons - striatal',
                                    'Mouse Neurons - substantia nigra', 'Mouse Neurons - substantia nigra',
                                    'Mouse Neurons - ventral spinal cord', 'Mouse Renal epithelial cells',
                                    'natural helper cells, IL2 treated', 'natural helper cells, IL33 treated',
                                    'natural helper cells, naive', 'Neurons - spiral ganglion',
                                    'neurospheres - enteric neuron derived',
                                    'neurospheres - parasympathetic neuron derived',
                                    'neurospheres - sympathetic neuron derived', 'osteoclast, bone marrow derived',
                                    'Schwann', 'Sox2+ Supporting cells - organ of corti',
                                    'stem cell (cKit+ Sca1- lineage-) KSL']
mouse_complete_primary_non_include_list = {}
mouse_complete_primary_exclude_list = []
mouse_complete_primary_jit_exclude_list = {}

# endregion "Mouse"
# endregion "Global Variables"


# region "Unit Tests"

# region "Promoters"
# figure_1_not_include_list = {"Myoblast": ["myoblast differentiation", "myoblastoma"]}
# figure_1_exclude_list = {"Neurons": "iPS neuron", "Myoblast": "myoblast differentiation"}

# figure_1("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", complete_primary_cell_list, [4], 1000, 2,
#          expression=1,
#          multi_plot=True, not_include=complete_primary_non_include_list, celltype_exclude=complete_primary_exclude_list,
#          include_problems=True)

# get_all_vencodes("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters",
#                                    complete_primary_cell_list, 20, expression=1,
#                                    not_include=complete_primary_non_include_list,
#                                    celltype_exclude=complete_primary_exclude_list, threshold=50, mode="count")

# ven_percentage_per_celltype("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "Adipocyte - perirenal", 4,
#                       1000, 20,expression=1, not_include=complete_primary_non_include_list,
#                       celltype_exclude=complete_primary_exclude_list)

# """
complete_promoters = Promoters("hg19.cage_peak_phase1and2combined_tpm.osc.txt",
                               three_donors_cell_list,
                               celltype_exclude=complete_primary_exclude_list,
                               not_include=complete_cancer_non_include_list,
                               partial_exclude=complete_primary_jit_exclude_list,
                               sample_types="primary cells")

complete_promoters.get_all_vencodes([1, 2, 3, 4, 5], threshold=50, multi=True, at_least_one=True)
complete_promoters.database.codes_to_csv("codes_three_donors.csv", "list", "/Figure 1/Test codes/")
complete_promoters.database.celltypes_to_csv("celltypes_three_donors.csv", "/Figure 1/Test codes/")
# """

""" For figure 1 cancer cell lines:
complete_promoters = Promoters("hg19.cage_peak_phase1and2combined_tpm.osc.txt",
                               merged_lines_cancer_cells,
                               celltype_exclude=complete_primary_exclude_list,
                               not_include=complete_cancer_non_include_list,
                               partial_exclude=complete_primary_jit_exclude_list,
                               sample_types=["primary cells", "cell lines"],
                               second_parser="primary cells")

complete_promoters.get_all_vencodes([1,2,3,4,5], threshold=50, multi=True, at_least_one=True)

# complete_promoters.database.codes_to_csv("codes_merged_cancer_cells.csv", "list", "/Figure 1/Test codes/")
# complete_promoters.database.celltypes_to_csv("celltypes_merged_cancer_cells.csv", "list", "/Figure 1/Test codes/")
"""
# endregion "Promoters"

# region "Enhancers"
# complete_enhancers = Enhancers("human_permissive_enhancers_phase_1_and_2_expression_tpm_matrix.txt",
#                                "Human.sample_name2library_id.txt", complete_primary_cell_list,
#                                celltype_exclude=complete_primary_exclude_list,
#                                not_include=complete_primary_non_include_list,
#                                partial_exclude=complete_primary_jit_exclude_list)
# complete_enhancers.get_all_vencodes_2([1,2,3], threshold=50, multi=True, at_least_one=True)
# complete_enhancers.figure_1([4], 1000, 2, multi_plot=True, include_problems=False)

# mouse
# complete_enhancers = Enhancers("mouse_permissive_enhancers_phase_1_and_2_expression_tpm_matrix.txt",
#                                "Mouse.sample_name2library_id.txt", mouse_complete_primary_cell_list,
#                                celltype_exclude=None,
#                                not_include=None,
#                                partial_exclude=None)
# complete_enhancers.get_all_vencodes_2([1, 2, 3, 4], threshold=50, multi=True, at_least_one=True)

# endregion "Enhancers"

# region "Graphs"

# Graphs.file_appender_for_heat_map("/Figure 1/Prob enha/", save=True, plot=False)
# Graphs.heatmap_from_file("/Figure 1/All together_edit.csv", interpolation="None", simple=True)
# Graphs.heatmap_from_file("/Figure 1/All together.csv", orientation="horizontal", sep=";", simple=True)
# endregion "Graphs"

# endregion "Unit Tests"

# region "TODOs"
# TODO: figure1 for mouse db
# TODO: get at least one vencode for 1<k<x promoters and enhancers: quick method for all celltps and slow for remaining.
# TODO: re-run problems for enhancers and promoters
# TODO: curva percent of vencodes that work on all donors per amount of Donors used (or maybe per percentage of donors
# endregion "TODOs"
