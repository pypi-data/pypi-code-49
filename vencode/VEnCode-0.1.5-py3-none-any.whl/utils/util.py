#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" util.py: Functions module for the VEnCode project """
import glob
import itertools as iter
import logging
import math
import os
import random
import re
import statistics as stats
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.special import comb

pd.options.mode.chained_assignment = None  # default='warn'


# region VEnCode generating functions

def reform_vencode_n_combinations_of_k(threshold, data_frame, code, celltype, db_type, k, n, others_df=None,
                                       write_file=False):
    c = 0
    dictionary = {}
    success = False
    for i in reversed(range(1, 5)):
        if i == 4 and threshold < 100:
            pass
        elif i < 4 and threshold == 100:
            pass
        else:
            print("Searching for vencode of %s non-spec zeros in threshold = %s" % (i, threshold))
            for combo in iter.combinations(data_frame.index.values, k):
                df2 = data_frame.loc[list(combo)].copy()
                assess_if_vencode = np.any(df2.drop(code, axis=1).values == 0, axis=0)
                if all(assess_if_vencode):
                    zeros = []
                    for y in df2.drop(code, axis=1).T.values:
                        zeros.append(y.tolist().count(0))
                    mask_zeros = list(value < i for value in zeros)
                    if np.any(mask_zeros):
                        pass
                    else:
                        if others_df is not None:
                            df4 = pd.concat([df2, others_df], axis=1, join_axes=[df2.index])
                            df_to_write = df4.dropna()
                            assess_replicates = np.all(df_to_write[others_df.columns.values].values >= 1)
                            if assess_replicates:
                                name = ", ".join(combo)
                                print("vencode of %s!" % i)
                                c += 1
                                success = True
                                if write_file:
                                    if not os.path.exists("./VenCodes/" + db_type + "/" + celltype.replace(":", "_")):
                                        os.makedirs("./VenCodes/" + db_type + "/" + celltype.replace(":", "_"))
                                    df_to_write.to_csv(
                                        "./VenCodes/" + db_type + "/" + celltype.replace(":",
                                                                                         "_") + "/" + "%s_Ven_%s.csv" % (
                                            celltype, c), sep=";")
                                else:
                                    dictionary[name] = df_to_write
                                    p = pd.Panel(dictionary)
                                    print(p)
                            else:
                                pass
                        else:
                            df_to_write = df2.dropna()
                            name = ", ".join(combo)
                            c += 1
                            success = True
                            if write_file:
                                if not os.path.exists("./VenCodes/" + db_type + "/" + celltype.replace(":", "_")):
                                    os.makedirs("./VenCodes/" + db_type + "/" + celltype.replace(":", "_"))
                                df_to_write.to_csv(
                                    "./VenCodes/" + db_type + "/" + celltype.replace(":",
                                                                                     "_") + "/" + "%s_Ven_%s.csv" % (
                                        celltype, c), sep=";")
                            else:
                                dictionary[name] = df_to_write
                                p = pd.Panel(dictionary)
                                print(p)
                else:
                    pass
                if n:
                    if c == n:
                        break
                else:
                    pass
        if n:
            if c == n:
                break
    return success


def full_vencodes_count_combinations_for_graph(filter_1, celltypes, others_df, x=None, y=None, k=4, s=5):
    if celltypes is None:
        pass
    elif celltypes:
        percent = {}
        avg = []
        percent[celltypes] = []
        for i in range(s):
            sample = filter_1.sample(frac=x, n=y)
            c = 0
            for combo in iter.combinations(sample.index.values, k):
                df2 = sample.loc[list(combo)]
                assess_if_vencode = np.any(df2.drop(celltypes, axis=1).values == 0, axis=0)
                if all(assess_if_vencode):
                    if len(others_df.index) != 0:
                        df4 = pd.concat([df2, others_df], axis=1, join_axes=[df2.index])
                        df_to_assess = df4.dropna()
                        assess_replicates = np.all(df_to_assess[others_df.columns.values].values >= 2)
                        if assess_replicates:
                            c += 1
                        else:
                            pass
                    else:
                        c += 1
                else:
                    pass
            avg.append(c)
        avg = stats.mean(avg)
        total_comb = comb(len(sample.index), k, exact=False)
        percent[type].append(avg / total_comb * 100)
        return percent


def vencode_percent_sampling(codes, celltype, filters, combinations_number, samples_to_take, reps,
                             include_problems=False):
    """
        Returns  a dictionary containing the percentage of VEnCodes found per k combinations, calculated by sampling
        the df rows for samples_to_take number of times and reps number or repetitions.
        """
    k_ven_percent = {}
    if include_problems: problems = {}
    for number in combinations_number:
        try:
            ven = {}
            for i in range(reps):
                c = 0
                for n in range(samples_to_take):
                    if n >= comb(int(filters.shape[0]), len(combinations_number), exact=False):
                        break
                    sample = filters.sample(n=number)
                    sample_dropped = sample.drop(codes, axis=1).values
                    if include_problems:
                        c, problems = assess_vencode_one_zero_plus_problems(c, sample.drop(codes, axis=1), problems)
                    else:
                        c = assess_vencode_one_zero(c, sample_dropped)
                ven[i] = (c / samples_to_take) * 100
                print("Finished rep {0} for k = {1} in celltype = {2}".format(i, number, celltype))
            ven_values = list(ven.values())
            means = np.mean(ven_values, dtype=np.float64)
            st_error = np.std(ven_values, dtype=np.float64) / math.sqrt(len(ven_values))
            k_ven_percent[number] = [means, st_error]
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            break
    if include_problems:
        return k_ven_percent, problems
    else:
        return k_ven_percent


def vencode_percent_sampling_monte_carlo(codes, filters, combinations_number, vens_to_take, reps,
                                         vencodes=False,
                                         stop_at=50000):
    """
    Returns a dictionary containing the percentage of VEnCodes found per n combinations of k promoters,
    calculated by sampling the df rows for samples_to_take number of times and reps number or repetitions.
    """
    col_list = filters.drop(codes, axis=1).columns.values
    try:
        ven = {}
        e_values = []
        for i in range(reps):
            n = 0
            breaker = 0  # Used to break the while loop in case the cell type has no VEnCodes.
            while n < vens_to_take:
                sample = filters.sample(n=combinations_number)
                sample_dropped = sample.drop(codes, axis=1).values
                assess_if_vencode = np.any(sample_dropped == 0, axis=0)
                if all(assess_if_vencode):
                    n += 1
                    e_value = vencode_mc_simulation(sample.drop(codes, axis=1), col_list)
                    if vencodes:
                        name = "threshold_" + str(vencodes) + " ven_" + str(n)
                        ven[name] = [sample.index.values.tolist(), e_value]
                    e_values.append(e_value)
                else:
                    breaker += 1
                    if breaker > stop_at:
                        print("\nCouldn't find enough VEnCodes!", end="\n\n")
                        break
        print("e_values: ", e_values)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        e_values, ven = (0, 0)  # function will always return, but in this case with a critical warning.
    if vencodes:
        return e_values, ven
    else:
        return e_values


# endregion

# region Other VEnCode functions


def assess_vencode_one_zero_boolean(sample, threshold=0):  # moved to internals.py
    """
    Returns True if sample represents a VEnCodes for a celltype not in "sample". It assumes VEnCodes when all
    other celltypes have at least one promoter not expressing. It's the quickest VEnCode counting algorithm.
    """
    if threshold == 0:
        assess_if_vencode = np.any(sample == 0, axis=0)  # list of True if column has any 0
    elif threshold > 0:
        assess_if_vencode = np.any(sample <= threshold, axis=0)
    else:
        raise ValueError("Threshold for VEnCode assessment is not valid.")
    return all(assess_if_vencode)  # if all columns are True (contain at least one 0), then is VEn


def assess_vencode_one_zero(counter, sample):
    """
    Returns the number of VEnCodes for a sample. It assumes VEnCodes when all other celltypes have at least one
    promoter not expressing. It's the quickest VEnCode counting algorithm.
    """
    assess_if_vencode = np.any(sample == 0, axis=0)
    if all(assess_if_vencode):
        counter += 1
    else:
        pass
    return counter


def assess_vencode_one_zero_plus_problems(counter, sample, problems):
    """
    Returns the number of VEnCodes for a sample. It assumes VEnCodes when all other celltypes have at least one
    promoter not expressing. It's the quickest VEnCode counting algorithm.
    """
    assess_if_vencode = np.any(sample.values == 0, axis=0)
    if all(assess_if_vencode):
        counter += 1
    else:
        for i in sample.columns.values:
            if not assess_if_vencode[sample.columns.values.tolist().index(i)]:
                if not i in problems:
                    problems[i] = 1
                else:
                    problems[i] += 1
    return counter, problems


def vencode_mc_simulation(data, col_list, reps=100):  # moved to internals.py
    """
    :param data: pandas data frame of promoter expression per celltype without the celltype of interest.
    :param col_list: columns of celltypes/donors without the celltype of interest.
    :return: e_values, that is, the average number of random changes done to the data that breaks the vencode.
    """
    index_list = data.index.values
    simulator = 0
    global_counter_list = []
    while simulator < reps:
        vencode = True
        local_counter = 0
        mc_df = data.copy()
        while vencode:
            col = random.choice(col_list)
            index = random.choice(index_list)
            if mc_df.loc[index][col] == 0:
                local_counter += 1
                mc_df.set_value(index, col, 1)  # TODO: deprecated, test .at[index, col] = 1
                a = mc_df[col].tolist()
                try:
                    b = a.index(
                        0)  # searches for at least one 0 in that column. If there's no 0, it's not a VEnCode.
                except ValueError:
                    vencode = False
                    global_counter_list.append(local_counter)
            else:
                pass
        simulator += 1
    global_counter = np.mean(global_counter_list, dtype=np.float64)
    return global_counter


def node_calculator(dataframe, at_least_one=False):
    promoter_nodes = {}
    promoters = dataframe.index.values
    for promoter in promoters:
        cols = dataframe.loc[promoter] != 0
        cols = dataframe.columns[cols]
        new_df = dataframe[cols].drop(promoter, axis=0)
        nodes = (new_df == 0).all(axis=1)
        node_count = np.sum(nodes)
        if node_count > 0:
            promoter_nodes[promoter] = node_count
            if at_least_one:
                return promoter_nodes
        else:
            pass
        dataframe.drop(promoter, axis=0, inplace=True)
    return promoter_nodes


def number_of_combination_from_nodes(node_dict, n, r):
    combinations = 0
    if r > 2:
        for i in node_dict.keys():
            nodes = node_dict[i]
            combinations += (comb((n - 2), (r - 2), exact=False) * nodes) - comb(nodes,
                                                                                 2)  # see triangular numbers
            # reminder: I took "* (n - 3)" from the end of equation
            n -= 1  # this removes the current promoter for the next promoter's calculations
    elif r == 2:
        combinations = sum(node_dict.values())
    else:
        raise Exception("Combinations number not recognized!")
    return combinations


def sorted_ven_robustness_test(file, file_type, celltype, combinations_number, samples_to_take, reps,
                               threshold=90,
                               expression=1, celltype_exclude=None, not_include=None, multi_plot=False,
                               init_data=None,
                               sample_types="primary cells", optional_folder=None, include_problems=False):
    if init_data is None:
        start_time = time.time()
        raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                               skiprows=1831)  # nrows=x if we want to load only a few rows
        data_1 = raw_data.drop(raw_data.index[[0, 1]])
        universal_rna = fantom_code_selector(file_type, data_1, "universal", not_include=None)
        data_1.drop(universal_rna, axis=1, inplace=True)
        to_keep = fantom_sample_category_selector("sample types - FANTOM5.csv", sample_types)
        data = pd.DataFrame(index=data_1.index.values)
        for sample in to_keep:
            data_temp = data_1.filter(regex=sample)
            data = data.join(data_temp)
    else:
        data = init_data
    codes = fantom_code_selector(file_type, data, celltype, not_include=not_include)
    print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
    if celltype_exclude is not None:
        codes_exclude = fantom_code_selector(file_type, data, celltype_exclude)
        try:
            for code in codes:
                codes_exclude = [x for x in codes_exclude if x != code]
        except ValueError:
            pass
        print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
        data.drop(codes_exclude, axis=1, inplace=True)
    if not isinstance(combinations_number, list):
        combinations_number_list = range(1, combinations_number + 1)
    else:
        combinations_number_list = combinations_number
    if isinstance(expression, list):
        k_ven_percent = {}
        for item in expression:
            print("Starting: Expression >= {0}".format(item))
            filter_2 = df_filter_by_expression_and_percentile(data, codes, item, 2, threshold)
            k_ven_percent_2, problems = vencode_percent_sampling(codes, celltype, filter_2,
                                                                 combinations_number_list,
                                                                 samples_to_take, reps,
                                                                 include_problems=include_problems)
            k_ven_percent[item] = k_ven_percent_2
        folder = "/Percentage/"
        file_name = u"/Perc VenC - 1 zero - {1:s} - {2:s} - expression from {4} to {5} - {3:d}x {0:d} samples of k".format(
            samples_to_take, file_type, celltype, reps, expression[0], expression[len(expression) - 1])
        title = "Probability of VEnCode from random promoters sample of size k \n {0:s}".format(
            celltype)
        if celltype_exclude is not None:
            if isinstance(celltype_exclude, list):
                file_name += " - excluding {} celltypes".format(len(celltype_exclude))
                title += " - excluding {} celltypes".format(len(celltype_exclude))
            else:
                file_name += " - excluding {0}".format(celltype_exclude)
                title += " - excluding {0}".format(celltype_exclude)
        # Defs.write_dict_to_csv(file_name + ".csv", k_ven_percent, folder, multi_express=True)
        fig, path = errorbar_plot(k_ven_percent, folder, file_name, label=celltype, title=title, multiple=True)
        fig.savefig(path)
    else:
        filter_2 = df_filter_by_expression_and_percentile(data, codes, expression, 2, threshold)
        k_ven_percent, problems = vencode_percent_sampling(codes, celltype, filter_2, combinations_number_list,
                                                           samples_to_take,
                                                           reps, include_problems=include_problems)
        folder = "/Percentage/"
        file_name = u"/VEnC - {1:s} - {2:s} - exp bigger or = {4:d} - {3:d}x {0:d} samples of k".format(
            samples_to_take, file_type, celltype, reps, expression)
        title = "Probability of VEnCode from sample of size k \n {0:s} expression >= {1:d}".format(
            celltype, expression)
        if celltype_exclude is not None:
            if isinstance(celltype_exclude, list):
                # file_name += " - excluding {} celltypes".format(len(celltype_exclude))
                title += " - excluding {} celltypes".format(len(celltype_exclude))
            else:
                # file_name += " - excluding {0}".format(celltype_exclude)
                title += " - excluding {0}".format(celltype_exclude)
        if not multi_plot:  # multi_plot is there in case this function is used to generate other plots after.
            if optional_folder is not None:
                folder = optional_folder
            # writing_files.write_dict_to_csv(file_name + ".csv", k_ven_percent, folder) -Disabled because circular imp
            fig, path = errorbar_plot(k_ven_percent, folder, file_name, label=celltype, title=title)
            fig.savefig(path)
        if include_problems:
            logging.info("{}: {}".format(celltype, problems))
            new_file_name = u"/Problems for {} - {}x {} samples of k".format(celltype, reps, samples_to_take)
            # writing_files.write_dict_to_csv(new_file_name + ".csv", problems, folder) -Disabled because circular imp
    if not multi_plot:
        plt.close(fig)
    if init_data is None:
        print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return k_ven_percent


# endregion

# region Data frame specific functions


def df_row_percentage_of_zeros_calculator(data_frame, celltype):
    """ Returns a df containing one extra column with the percentage of zeros for each row. Slow function"""
    percent_list = []
    data_frame_new = data_frame.copy()
    for index, series in data_frame.drop(celltype, axis=1).iterrows():
        x = 0
        for p in series.values.tolist():
            if p == 0:
                x += 1
            else:
                pass
        percent = percentage(x, len(data_frame_new.columns))
        percent_list.append(percent)
    column_label = "percentage_of_zeros"
    data_frame_new[column_label] = percent_list
    return data_frame_new, column_label


def df_percentile_calculator(data_frame, celltype, start_percent, define_percentile=False):   # note: migrated to pandas_utils.py
    """
    Returns a df with one extra column containing the value of the data at percentile start_percent and the label
    of such column.
    """
    if define_percentile:
        column_label = "Percentile {}".format(start_percent)
    else:
        column_label = "Percentile_col"
    data_frame[column_label] = np.percentile(data_frame.drop(celltype, axis=1).values, start_percent, axis=1)
    return data_frame, column_label


def df_filter_by_expression(data, codes, expression):  # note: migrated to pandas_utils.py
    """ Returns a df containing only the rows which value is >= than expression for all columns in codes """
    # data_filtered = data.copy()
    if isinstance(codes, (list, tuple, np.ndarray)):
        for item in codes:
            data = data[data[item] >= expression]
    else:
        data = data[data[codes] >= expression]
    return data


def df_filter_by_column_value(data_frame, column, value=0):  # note: migrated to pandas_utils.py
    """ Returns a df containing only the rows that present a value = 0 for the column "column" """
    data_filtered = data_frame[data_frame[column] == value]
    return data_filtered


def df_filter_by_expression_and_percentile(data, codes, expression, amount, threshold=None):
    """
     Returns a df after applying a filter by rows which expression >= x, or both a filter by expression and
     filter by rows which the xth percentile (x == threshold) is 0.
    """
    filter_1 = df_filter_by_expression(data, codes, expression)
    logging.info("After filter 1: %s promoters", filter_1.shape[0])
    if amount == 1:
        return filter_1
    elif amount == 2:
        with_percentile, column_name = df_percentile_calculator(filter_1, codes, threshold)
        filter_2 = df_filter_by_column_value(with_percentile, column_name)
        while filter_2.shape[0] < 50 and threshold > 5:
            threshold -= 5
            with_percentile, column_name = df_percentile_calculator(filter_1, codes, threshold)
            filter_2 = df_filter_by_column_value(with_percentile, column_name)
        if filter_2.shape[0] >= 50:
            logging.info("After filter 2: %s promoters at threshold %s", filter_2.shape[0], threshold)
            filter_2.drop(column_name, axis=1, inplace=True)
            return filter_2
        else:
            print("Filter 2 didn't produce sufficient results even at percentile {}".format(threshold))
            filter_1.drop(column_name, axis=1, inplace=True)
            return filter_1
    else:
        raise Exception("Amount of filters not valid")


def df_filter_by_percentile(data, codes, threshold):
    """ Returns a df after filtering rows for those which xth percentile (x == threshold) is 0. """
    with_percentile, column_name = df_percentile_calculator(data, codes, threshold)
    filter_2 = df_filter_by_column_value(with_percentile, column_name)
    while filter_2.shape[0] < 50 and threshold > 5:
        threshold -= 5
        with_percentile, column_name = df_percentile_calculator(data, codes, threshold)
        filter_2 = df_filter_by_column_value(with_percentile, column_name)
    if filter_2.shape[0] >= 50:
        print("After filter 2: ", filter_2.shape[0], "at threshold", threshold)
        logging.info("After filter 2: %s promoters at threshold %s", filter_2.shape[0], threshold)
        filter_2.drop(column_name, axis=1, inplace=True)
        return filter_2, threshold
    else:
        print("Filter 2 didn't produce sufficient results even at percentile {}".format(threshold))
        return


def df_regex_searcher(string, database): # Note: migrated to pandas_utils.py
    """ Returns a df containing only the columns which contain the string somewhere in its label """
    regular = ".*" + string.replace(" ", ".*").replace("+", "%2b").replace(":", "%3a").replace("(",
                                                                                               "%28").replace(
        ")", "%29").replace("/", "%2f") + ".*"
    idx = database.columns.str.contains(regular, flags=re.IGNORECASE, regex=True, na=False)
    regex_filtered_df = database.loc[:, idx]
    return regex_filtered_df


def df_minimal_regex_searcher(string, database): # Note: migrated to pandas_utils.py
    """ Returns a df containing only the columns which contain the string somewhere in its label
    Used for enhancer data set. """
    expression = ".*" + string.replace(" ", ".*").replace("+", "\+") + ".*"
    idx = database.columns.str.contains(expression, flags=re.IGNORECASE, regex=True, na=False)
    regex_filtered_df = database.loc[:, idx]
    return regex_filtered_df

# endregion

# region FANTOM5 database specific functions


def fantom_code_selector(type, db, celltype, not_include=None):
    """
    Returns a list containing the column labels which contain the queried string. works for 2 different databases:
    Enhancers and promoters.
    """
    if type == "Enhancers":
        parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "/Files/"
        lines_and_codes = pd.read_csv(parent_path + db, sep="\t", index_col=1, header=None, names=["celltypes"])
        regular = ".*" + celltype + ".*"
        idx = lines_and_codes.celltypes.str.contains(regular, flags=re.IGNORECASE, regex=True, na=False)
        codes_df = lines_and_codes[idx]
        codes = codes_df.index.values
    elif type == "Promoters":
        if isinstance(celltype, list):
            codes = []
            for item in celltype:
                codes_df = df_regex_searcher(item, db)
                codes.append(codes_df.columns.values)
            codes = [item for sublist in codes for item in sublist]
        else:
            codes_df = df_regex_searcher(celltype, db)
            codes = codes_df.columns.values
        if not_include is not None:
            if isinstance(not_include, list):
                not_codes = []
                for item in not_include:
                    not_codes_df = df_regex_searcher(item, codes_df)
                    not_codes.append(not_codes_df.columns.values)
                not_codes = [item for sublist in not_codes for item in sublist]
            else:
                not_codes_df = df_regex_searcher(not_include, codes_df)
                not_codes = not_codes_df.columns.values
            codes = list(set(codes) - set(not_codes))
    else:
        raise Exception("Error. Wrong type of database. No codes generated")
    # Test if any code was retrieved:
    try:
        if not codes.tolist():
            raise Exception("No codes for {}!".format(celltype))
    except AttributeError:
        if not isinstance(codes, list):
            raise Exception("No codes for {}!".format(celltype))
    return codes


def fantom_sample_category_selector(sample_types_file, types, path="parent", get="index"):
    """
        Returns a list of cell types to keep/drop from a file containing the list of cell types and a 'Sample category'
        column which determines which cell types to retrieve.
        """
    if not isinstance(types, list): types = [types]
    if path == "parent":
        parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        database = pd.read_csv(parent_path + "/Files/" + sample_types_file, sep=",", index_col=0)
    elif path == "normal":
        database = pd.read_csv("./Files/" + sample_types_file, sep=",", index_col=0)
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


# endregion

# region Plotting


def box_plotting_from_dict(dictionary, fig_name, folder, title, keys_horizontal=False, path="normal"):
    if path == "parent":
        current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    elif path == "normal":
        current_path = os.getcwd()
    else:
        raise Exception("path name not recognized!")
    path = current_path + folder + fig_name
    plt.style.use('ggplot')
    keys = sorted(dictionary.keys())
    data = list([dictionary[key] for key in keys])
    fig = plt.figure()
    plt.title(title)
    ax = fig.add_subplot(111)
    if keys_horizontal:
        bp = ax.boxplot(data, patch_artist=True, whis=[5, 95], vert=False)
    else:
        bp = ax.boxplot(data, patch_artist=True, whis=1.5)
    for box in bp['boxes']:
        # change outline color
        box.set(color='#7570b3', linewidth=2)
        # change fill color
        box.set(facecolor='#1b9e77')
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    if keys_horizontal:
        ax.set_yticklabels(keys)
    else:
        ax.set_xticklabels(keys)
    return fig, path


def errorbar_plot(input_data, folder, file_name, label=None, title=None, multiple=False, path="normal"):
    if path == "parent":
        current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    elif path == "normal":
        current_path = os.getcwd()
    else:
        raise Exception("path name not recognized!")
    fig_name = folder + file_name + ".png"
    path = current_path + fig_name
    plt.style.use('bmh')
    fig = plt.figure(1)
    if title:
        plt.title(title)
    ax = fig.add_subplot(111)  # , axisbg='w'
    if multiple:
        if isinstance(input_data, dict):
            data = pd.DataFrame.from_dict(input_data)
            combs = data.index.values
            for column in data.columns.values:
                a = data[column].dropna()
                headers = a.index.values
                means = list([a.values[key][0] for key in range(0, len(a.values))])
                st_error = list([a.values[key][1] for key in range(0, len(a.values))])
                ax.errorbar(headers, means, yerr=st_error, fmt='-o', linewidth=2, markersize=4, label=column)
        else:
            pass
    else:
        if isinstance(input_data, dict):
            headers = list(input_data.keys())
            means = [values[0] for values in input_data.values()]
            st_error = [values[1] for values in input_data.values()]
        else:
            data = pd.read_csv(input_data, decimal=".", sep=";", index_col=False)
            means = data.iloc[0].values
            headers = data.columns.values
            st_error = data.iloc[1].values
        ax.errorbar(headers, means, yerr=st_error, fmt='-o', linewidth=2, markersize=4, label=label)
        combs = headers

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_yscale("linear")
    start_x, end_x = ax.get_xlim()
    start_y, end_y = ax.get_ylim()
    ax.xaxis.set_ticks(np.arange(start_x, end_x + 1, 1))
    ax.set_xlim(start_x - (len(combs) * 0.1), end_x + (len(combs) * 0.1))
    ax.set_ylim(start_y, end_y + (end_y * 0.05))
    for item in ([ax.xaxis.label, ax.yaxis.label] +
                     ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(10)
    if multiple:
        plt.legend(numpoints=1, loc="best", shadow=True, fancybox=True, title="Expression\nthreshold")
    if not multiple:
        plt.legend(numpoints=1, loc="best", shadow=True, fancybox=True)
    return fig, path


# endregion


# region Other functions


def percentage(part, whole):
    return 100 * float(part) / float(whole)


def open_csv(filename):
    raw_data = pd.read_csv("./Files/" + filename, sep=",", index_col=0)
    return raw_data


def remove_all_x_element(element, lst):
    return filter(lambda x: x != element, lst)


def other_lines_sum_generator(data_frame, celltype):
    df1 = data_frame.drop(celltype, 1)
    data_frame["sum"] = df1.sum(axis=1)
    return data_frame


def mean_and_stdev_generator(dict):
    dictionary = {}
    for line, values in dict.items():
        dictionary[line] = []
        means = stats.mean(values)
        stdev = stats.stdev(values)
        dictionary[line] = [means, stdev]
    return dictionary


def file_names_to_list(folder, pattern="*.csv"):
    """ Returns a list with all files of a given file type (pattern) """
    current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    file_path = current_path + folder + pattern
    file_list = glob.glob(file_path)
    return file_list


def possible_dict_to_list(dict_possible):
    if isinstance(dict_possible, dict):
        list_final = [j for i in list(dict_possible.values()) for j in i]
    else:
        list_final = dict_possible
    return list_final


def check_list_index_and_append(lst, index, to_append):
    if isinstance(lst, np.ndarray):
        lst = lst.tolist
    try:
        value = lst[index]
        try:
            value.append(to_append)
        except AttributeError:
            value = [value, to_append]
        lst[index] = value
    except IndexError:
        lst.append(to_append)
    logging.info(lst)
    return lst


def combinations_from_nested_lists(lst):
    """
    Generates tuples with combinations of one element of each list inside the first list.
    :param lst: the list to combine.
    """

    def helper(lst_):
        """
        Helps by allowing it's recursive use to generate a correctly shaped list to then iter.product
        """
        if not any(isinstance(e, list) for e in lst_):
            lst_new.append(lst_)
        else:
            for z in lst_:
                if isinstance(z, list):
                    helper(z)
                else:
                    lst_new.append([z])

    if not any(isinstance(w, list) for w in lst):
        for g in lst:
            yield [g]
    else:
        lst_new = []
        for j in lst:
            if isinstance(j, list):
                helper(j)
            else:
                lst_new.append([j])
        lst = lst_new
        for i in iter.product(*lst):
            yield i


def multi_log(handler, *args, level="info"):
    """ Log multiple arguments in one statement. """
    for arg in args:
        if level == "info":
            handler.info(arg)
        elif level == "debug":
            handler.debug(arg)
        else:
            raise NameError("Argument level={} is not valid".format(level))


def key_with_max_val(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value """
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


# endregion

__author__ = "Andre Macedo"
__copyright__ = "GPL"
__credits__ = ["Andre Macedo", "Alisson Gontijo"]
__license__ = "See Github project"
__version__ = "See Github project"
__maintainer__ = "Andre Macedo"
__email__ = "andre.lopes.macedo@gmail.com"
__status__ = "Development"
