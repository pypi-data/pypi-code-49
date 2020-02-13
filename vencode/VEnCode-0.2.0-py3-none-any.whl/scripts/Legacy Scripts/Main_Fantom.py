import utils.writing_files

__author__ = 'Andre Macedo'
import itertools as iter
import logging
import math
import os
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.special import comb

from utils import util


# generating VenCodes:

def enhancers_improved_vencodes(names_db, file, celltype, p=None, k=4, n=None, write_file=False):
    parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "/Files/"
    raw_data = pd.read_csv(parent_path + file, sep="\t", index_col=0)
    codes = util.fantom_code_selector("Enhancers", names_db, celltype)
    if len(codes) == 1:
        filter_1 = util.df_filter_by_expression(raw_data, codes, 1)
        print(filter_1.shape[0])
        threshold = 80
        with_percentage_of_zeros, column_name = util.df_percentile_calculator(filter_1, codes, threshold)
        filter_2 = util.df_filter_by_column_value(with_percentage_of_zeros, column_name)
        if p is not None:
            sorted_1 = filter_2.nlargest(p, codes)
        else:
            sorted_1 = filter_2.sort(codes.tolist(), ascending=False)
        print("starting %s -> threshold = %s" % (codes, threshold))
        util.reform_vencode_n_combinations_of_k(threshold, sorted_1.drop(column_name, 1),
                                                codes, celltype, "Enhancers", k, n, write_file=write_file)
    else:
        for i in range(0, len(codes)):
            filter_1 = raw_data[raw_data[codes[i]] >= 1]
            code = codes[i]
            codes_2 = np.array(codes).tolist()
            codes_2.remove(code)
            cropped = filter_1.drop(codes_2, axis=1)
            print(cropped.shape)
            with_sum = util.other_lines_sum_generator(cropped, code)
            p_probes_sorted_df = with_sum.nsmallest(p, "sum")
            util.reform_vencode_n_combinations_of_k(p_probes_sorted_df.drop("sum", 1), code, "Enhancers", k, n,
                                                    write_file)
    return


def promoters_improved_vencodes(file, celltype, p=None, k=4, n=None, write_file=False):
    start_time = time.time()
    raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                           skiprows=1831)  # , nrows=3000 nrows=x if we want to load only a few rows
    data = raw_data.drop(raw_data.index[[0, 1]])
    codes = util.fantom_code_selector("Promoters", data, celltype)
    print(codes)
    if len(codes) == 1:
        code = codes[0]
        others_df = None
        filter_1 = util.df_filter_by_expression(data, codes, 1)
        threshold = 100
        while threshold > 0:
            with_percentage_of_zeros, column_name = util.df_percentile_calculator(filter_1, codes, threshold)
            filter_2 = util.df_filter_by_column_value(with_percentage_of_zeros, column_name)
            if p is not None:
                sorted_1 = filter_2.nlargest(p, codes)
            else:
                sorted_1 = filter_2.sort(codes.tolist(), ascending=False)
            print("starting %s -> threshold = %s" % (code, threshold))
            success = util.reform_vencode_n_combinations_of_k(threshold, sorted_1.drop(column_name, axis=1),
                                                              code, celltype, "Promoters", k, n, others_df, write_file)
            if not success:
                threshold -= 10
            if success:
                threshold = 0
    else:
        code = codes[0]
        codes_2 = np.array(codes).tolist()
        codes_2.remove(code)
        filter_1 = util.df_filter_by_expression(data, codes, 1)
        threshold = 100
        while threshold > 0:
            with_percentage_of_zeros, column_name = util.df_percentile_calculator(filter_1, codes, threshold)
            filter_2 = util.df_filter_by_column_value(with_percentage_of_zeros, column_name)
            if p is not None:
                sorted_1 = filter_2.nlargest(p, codes)
            else:
                sorted_1 = filter_2.sort(codes.tolist(), ascending=False)
            codes_2_df = sorted_1[codes_2]
            cropped = sorted_1.drop(codes_2, axis=1)
            print("Starting %s -> threshold = %s" % (celltype, threshold))
            success = util.reform_vencode_n_combinations_of_k(threshold, cropped.drop(column_name, axis=1),
                                                              code, celltype, "Promoters", k, n, codes_2_df, write_file)
            if not success:
                threshold -= 10
            if success:
                threshold = 0
    final_success = "success" if success else "failure"
    print("Process finished in %s seconds with %s" % (time.time() - start_time, final_success))
    return


# counting number of VenCodes:

def multiple_ven_robustness_test(file, file_type, celltype, combinations_number, samples_to_take, reps, zeros):
    start_time = time.time()
    raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                           skiprows=1831)  # nrows=x if we want to load only a few rows
    data = raw_data.drop(raw_data.index[[0, 1]])
    codes = util.fantom_code_selector(file_type, data, celltype)
    print(codes)
    code = codes[0]
    codes_2 = np.array(codes).tolist()
    codes_2.remove(code)
    filter_1 = data[data[code] >= 2]
    others_df = filter_1[codes_2]
    k_ven_percent = {}
    for number in combinations_number:
        ven = {}
        for i in range(reps):
            c = 0
            for n in range(samples_to_take):
                sample = filter_1.sample(n=number)
                sample_dropped = sample.drop(codes, axis=1).values
                assess_if_vencode = [list(u).count(0) for u in sample_dropped.T]
                bool1 = [x >= zeros for x in assess_if_vencode]
                if all(bool1):
                    if others_df.index.tolist():
                        pre_df_to_assess = pd.concat([sample, others_df], axis=1, join_axes=[sample.index])
                        df_to_assess = pre_df_to_assess.dropna()
                        assess_replicates = np.all(df_to_assess[others_df.columns.values].values >= 2)
                        if assess_replicates:
                            c += 1
                        else:
                            pass
                    else:
                        c += 1
                    break
                else:
                    pass
            ven[i] = (c / samples_to_take) * 100
        ven_values = list(ven.values())
        means = np.mean(ven_values, dtype=np.float64)
        st_error = np.std(ven_values, dtype=np.float64) / math.sqrt(len(ven_values))
        k_ven_percent[number] = [means, st_error]
    folder = "/Percentage/"
    file_name = u"/Percentage VenCodes of at least {3:d} non-specific zeros from {1:s} and celltype {2:s} with {4:d}x {0:d} samples of k".format(
        samples_to_take, file_type, celltype, zeros, reps)
    title = "Probability of VEnCode from random sample of size k"
    utils.writing_files.write_dict_to_csv(file_name + ".csv", k_ven_percent, folder)
    fig, path = util.errorbar_plot(k_ven_percent, folder, file_name, label=celltype, title=title)
    fig.savefig(path)
    plt.close(fig)
    print("Process finished in %s seconds" % (time.time() - start_time))
    return


def ven_robustness_test(file, file_type, celltype, combinations_number, samples_to_take, reps, expression=2):
    start_time = time.time()
    raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                           skiprows=1831)  # nrows=x if we want to load only a few rows
    data = raw_data.drop(raw_data.index[[0, 1]])
    codes = util.fantom_code_selector(file_type, data, celltype)
    print(codes)
    filter_1 = util.df_filter_by_expression_and_percentile(data, codes, expression, 1)
    k_ven_percent = util.vencode_percent_sampling(codes, celltype, filter_1, combinations_number, samples_to_take,
                                                  reps)
    folder = "/Percentage/"
    file_name = u"/Percentage VenCodes of at least 1 non-specific zeros from {1:s} and celltype {2:s} with {3:d}x {0:d} samples of k".format(
        samples_to_take, file_type, celltype, reps)
    title = "Probability of VEnCode from random sample of size k"
    utils.writing_files.write_dict_to_csv(file_name + ".csv", k_ven_percent, folder)
    fig, path = util.errorbar_plot(k_ven_percent, folder, file_name, label=celltype, title=title)
    fig.savefig(path)
    plt.close(fig)
    print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return


def sorted_ven_robustness_test(file, file_type, celltype, combinations_number, samples_to_take, reps, threshold=90,
                               expression=1, celltype_exclude=None, not_include=None, multi_plot=False, init_data=None,
                               sample_types="primary cells", optional_folder=None, include_problems=False):
    if init_data is None:
        start_time = time.time()
        raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                               skiprows=1831)  # nrows=x if we want to load only a few rows
        data_1 = raw_data.drop(raw_data.index[[0, 1]])
        universal_rna = util.fantom_code_selector(file_type, data_1, "universal", not_include=None)
        data_1.drop(universal_rna, axis=1, inplace=True)
        to_keep = util.fantom_sample_category_selector("sample types - FANTOM5.csv", sample_types)
        data = pd.DataFrame(index=data_1.index.values)
        for sample in to_keep:
            data_temp = data_1.filter(regex=sample)
            data = data.join(data_temp)
    else:
        data = init_data
    codes = util.fantom_code_selector(file_type, data, celltype, not_include=not_include)
    print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
    if celltype_exclude is not None:
        codes_exclude = util.fantom_code_selector(file_type, data, celltype_exclude)
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
            filter_2 = util.df_filter_by_expression_and_percentile(data, codes, item, 2, threshold)
            k_ven_percent_2, problems = util.vencode_percent_sampling(codes, celltype, filter_2,
                                                                      combinations_number_list,
                                                                      samples_to_take, reps, include_problems=include_problems)
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
        fig, path = util.errorbar_plot(k_ven_percent, folder, file_name, label=celltype, title=title, multiple=True)
        fig.savefig(path)
    else:
        filter_2 = util.df_filter_by_expression_and_percentile(data, codes, expression, 2, threshold)
        k_ven_percent, problems = util.vencode_percent_sampling(codes, celltype, filter_2, combinations_number_list,
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
            utils.writing_files.write_dict_to_csv(file_name + ".csv", k_ven_percent, folder)
            fig, path = util.errorbar_plot(k_ven_percent, folder, file_name, label=celltype, title=title)
            fig.savefig(path)
        if include_problems:
            logging.info("{}: {}".format(celltype, problems))
            new_file_name = u"/Problems for {} - {}x {} samples of k".format(celltype, reps, samples_to_take)
            utils.writing_files.write_dict_to_csv(new_file_name + ".csv", problems, folder)
    if not multi_plot:
        plt.close(fig)
    if init_data is None:
        print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return k_ven_percent


# Figures for paper


def figure_1(file, file_type, cell_list, combinations_number, samples_to_take, reps, threshold=90,
             expression=1, celltype_exclude=None, not_include=None, multi_plot=True, sample_types="primary cells",
             optional_folder="/Figure 1/Test lines/", include_problems=False):
    # Set up logging:
    logging.basicConfig(filename="./Figure 1/log {}_celltp k_{}.txt".format(len(cell_list), combinations_number),
                        level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
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
            ven = sorted_ven_robustness_test(file, file_type, celltype, combinations_number, samples_to_take, reps,
                                             threshold=threshold, expression=expression,
                                             celltype_exclude=celltype_to_exclude,
                                             not_include=not_celltype, multi_plot=multi_plot, init_data=data,
                                             optional_folder=optional_folder, include_problems=include_problems)
        else:
            ven = sorted_ven_robustness_test(file, file_type, celltype, combinations_number, samples_to_take, reps,
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


def figure_2(file, file_type, cell_list, combinations_number, vens_to_take, reps, threshold=90,
             expression=1, celltype_exclude=None, not_include=None, multi_plot=False, init_data=None,
             sample_types="primary cells", get_vencodes=False):
    # Set up logging:
    logging.basicConfig(
        filename="./Figure 2/{}/log {}_celltp {}_VEn.txt".format(file_type, len(cell_list), vens_to_take),
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
    logger = logging.getLogger(__name__)
    logger.info("Starting figure_2 function with {} cell types and analysing {} "
                "VEnCodes for their quality".format(len(cell_list), vens_to_take))
    # First, import only the necessary data, remove universal RNA pools and select the desired sample_type:
    if init_data is None:
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
    else:
        data = init_data
    # Exclude some specific, on-demand, celltypes from the data straight away:
    if isinstance(celltype_exclude, list):
        codes_exclude = util.fantom_code_selector(file_type, data, celltype_exclude)
        print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
        data.drop(codes_exclude, axis=1, inplace=True)
    final = {}
    # Starting loop through all cell types:
    for celltype in cell_list:
        print("\n", "Starting {}".format(celltype), sep="-> ")
        if not_include is not None:
            not_celltype = not_include.get(celltype)
        else:
            not_celltype = None
        codes = util.fantom_code_selector(file_type, data, celltype, not_include=not_celltype)
        print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
        if isinstance(celltype_exclude, dict):
            celltype_to_exclude = celltype_exclude.get(celltype)
            codes_exclude = util.fantom_code_selector(file_type, data, celltype_to_exclude)
            try:
                for code in codes:
                    codes_exclude = [x for x in codes_exclude if x != code]
            except ValueError:
                pass
            print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
            data.drop(codes_exclude, axis=1, inplace=True)
        filter_2 = util.df_filter_by_expression_and_percentile(data, codes, expression, 2, threshold)
        if get_vencodes:
            false_negatives, vencodes = util.vencode_percent_sampling_monte_carlo(codes, filter_2, combinations_number,
                                                                                  vens_to_take, reps, vencodes=get_vencodes)
        else:
            false_negatives = util.vencode_percent_sampling_monte_carlo(codes, filter_2, combinations_number,
                                                                        vens_to_take,
                                                                        reps, vencodes=get_vencodes)
        final[celltype] = false_negatives
    print(final)
    folder = "/Figure 2/{}/".format(file_type)
    file_name = u"/VEnCode E-values {} samples {} VEnCodes".format(len(cell_list), vens_to_take)
    title = "VEnCode quality\n"
    utils.writing_files.write_dict_to_csv(file_name + ".csv", final, folder)
    fig_2, path_2 = util.box_plotting_from_dict(final, file_name, folder, title, keys_horizontal=True)
    fig_2.savefig(path_2, bbox_inches='tight')
    plt.close(fig_2)
    #     fig, path = Defs.errorbar_plot(k_ven_percent, folder, file_name, label=celltype, title=title)
    #     fig.savefig(path)
    # if not multi_plot:
    #     plt.close(fig)
    if init_data is None:
        print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return


def figure_3(file, file_type, celltype, vens_to_take, combinations_number=4, sample_types="primary cells", expression=1,
             celltype_exclude=None, not_include=None, threshold=90):
    start_time = time.time()
    raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                           skiprows=1831)  # nrows=x if we want to load only a few rows
    data_1 = raw_data.drop(raw_data.index[[0, 1]])
    universal_rna = util.fantom_code_selector(file_type, data_1, "universal", not_include=None)
    data_1.drop(universal_rna, axis=1, inplace=True)
    to_keep = util.fantom_sample_category_selector("sample types - FANTOM5.csv", sample_types)
    data = pd.DataFrame(index=data_1.index.values)
    for sample in to_keep:
        data_temp = data_1.filter(regex=sample)
        data = data.join(data_temp)
    codes = util.fantom_code_selector(file_type, data, celltype, not_include=not_include)
    try:
        if not codes.tolist():
            raise Exception("No codes for {}!".format(celltype))
    except AttributeError:
        if not isinstance(codes, list):
            raise Exception("No codes for {}!".format(celltype))
    print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
    if celltype_exclude is not None:
        codes_exclude = util.fantom_code_selector(file_type, data, celltype_exclude)
        try:
            for code in codes:
                codes_exclude = [x for x in codes_exclude if x != code]
        except ValueError:
            pass
        print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
        data.drop(codes_exclude, axis=1, inplace=True)
    final_dict = {}
    for i in range(1, len(codes)):
        total_perc_not_ven = []
        partial_dict = {}
        for code in iter.combinations(codes, i):
            code = list(code)
            print("donor:", code, sep="\n", end="\n\n")
            # donors_exclude = [x for x in codes if x != code]
            codes_2 = codes[:]
            for x in code: codes_2.remove(x)
            donors_data = data[codes_2]
            data_2 = data.drop(codes_2, axis=1)
            print("donors to exclude:", *codes_2, sep="\n", end="\n\n")

            filter_2 = util.df_filter_by_expression_and_percentile(data_2, code, expression, 2, threshold)
            n = 0
            partial_perc_not_ven = []
            while n < vens_to_take:
                sample = filter_2.sample(n=combinations_number)
                sample_dropped = sample.drop(code, axis=1).values
                assess_if_vencode = np.any(sample_dropped == 0, axis=0)
                if all(assess_if_vencode):
                    n += 1
                    total = 0
                    counter = 0
                    for column, series in donors_data.loc[sample.index.values].iteritems():
                        total += 1
                        assess_if_not_vencode_donors = np.any(series.values == 0)
                        if assess_if_not_vencode_donors:
                            counter += 1
                    percentage_not_ven = counter / total * 100
                    partial_perc_not_ven.append(percentage_not_ven)
                else:
                    pass
            code_in_string = ' '.join(code)
            partial_dict[code_in_string] = partial_perc_not_ven

            mean = np.mean(partial_perc_not_ven, dtype=np.float64)
            total_perc_not_ven.append(mean)

        if not os.path.exists("./Figure 3/{}/Codes/".format(file_type)):
            os.makedirs("./Figure 3/{}/Codes/".format(file_type))
        folder = "/Figure 3/{}/Codes/".format(file_type)
        file_name = u"/{} Donors".format(i)
        utils.writing_files.write_dict_2_to_csv(file_name + ".csv", partial_dict, folder)

        final_dict[i] = total_perc_not_ven
    print(final_dict)
    if not os.path.exists("./Figure 3/{}/".format(file_type)):
        os.makedirs("./Figure 3/{}/".format(file_type))
    folder = "/Figure 3/{}/".format(file_type)
    file_name = u"/{} Donor not VEnCodes perc - {} VEnCodes".format(celltype, vens_to_take)
    utils.writing_files.write_dict_2_to_csv(file_name + ".csv", final_dict, folder)
    print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return


def figure_3_b(file, file_type, celltype, vens_to_take, combinations_number=4, sample_types="primary cells",
               expression=1, celltype_exclude=None, not_include=None, threshold=90):
    start_time = time.time()
    raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                           skiprows=1831, nrows=3000)  # nrows=x if we want to load only a few rows
    data_1 = raw_data.drop(raw_data.index[[0, 1]])
    universal_rna = util.fantom_code_selector(file_type, data_1, "universal", not_include=None)
    data_1.drop(universal_rna, axis=1, inplace=True)
    to_keep = util.fantom_sample_category_selector("sample types - FANTOM5.csv", sample_types)
    data = pd.DataFrame(index=data_1.index.values)
    for sample in to_keep:
        data_temp = data_1.filter(regex=sample)
        data = data.join(data_temp)
    codes = util.fantom_code_selector(file_type, data, celltype, not_include=not_include)
    try:
        if not codes.tolist():
            raise Exception("No codes for {}!".format(celltype))
    except AttributeError:
        if not isinstance(codes, list):
            raise Exception("No codes for {}!".format(celltype))
    print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
    if celltype_exclude is not None:
        codes_exclude = util.fantom_code_selector(file_type, data, celltype_exclude)
        try:
            for code in codes:
                codes_exclude = [x for x in codes_exclude if x != code]
        except ValueError:
            pass
        print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
        data.drop(codes_exclude, axis=1, inplace=True)

    for code in codes:
        print("donor:", code, sep="\n", end="\n\n")
        codes_2 = [x for x in codes if x != code]
        # codes_2 = codes[:]
        # for x in code: codes_2.remove(x)
        donors_data = data[codes_2]
        data_2 = data.drop(codes_2, axis=1)
        print("donors to exclude:", *codes_2, sep="\n", end="\n\n")

        filter_2 = util.df_filter_by_expression_and_percentile(data_2, code, expression, 2, threshold)

        partial_perc_not_ven = {}
        for i in range(1, (len(codes_2) + 1)):
            for y in iter.combinations(codes_2, i):
                y = list(y)
                string_y = "".join(y)
                counter = 0
                n = 0
                while n < vens_to_take:
                    sample = filter_2.sample(n=combinations_number)
                    sample_dropped = sample.drop(code, axis=1).values
                    assess_if_vencode = np.any(sample_dropped == 0, axis=0)
                    if all(assess_if_vencode):
                        n += 1
                        donors_data_sample = donors_data.loc[sample.index.values]
                        to_assess = donors_data_sample[y]
                        assess_if_not_vencode_donors = np.any(to_assess.values == 0, axis=0)
                        try:
                            if assess_if_not_vencode_donors:
                                counter += 1
                        except:
                            if any(assess_if_not_vencode_donors):
                                counter += 1
                    else:
                        pass
                percentage_not_ven = counter / vens_to_take * 100
                partial_perc_not_ven[string_y] = percentage_not_ven

        if not os.path.exists("./Figure 3-b/{}/".format(file_type)):
            os.makedirs("./Figure 3-b/{}/".format(file_type))
        folder = "/Figure 3-b/{}/".format(file_type)
        find = code.find("donor")
        substring = code[find:(find + 6)]
        file_name = u"/VEnCode for {} - {}".format(substring, celltype)
        utils.writing_files.write_one_value_dict_to_csv(file_name + ".csv", partial_perc_not_ven, folder)

        # code_in_string = ' '.join(code)
        # partial_dict[code_in_string] = partial_perc_not_ven
        #
        # mean = np.mean(partial_perc_not_ven, dtype=np.float64)
        # total_perc_not_ven.append(mean)

    print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return


def figure_3_b2(file, file_type, celltype, vens_to_take, combinations_number=4, sample_types="primary cells",
                expression=1, celltype_exclude=None, not_include=None, threshold=90):
    start_time = time.time()
    raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
                           skiprows=1831)  # nrows=x if we want to load only a few rows
    data_1 = raw_data.drop(raw_data.index[[0, 1]])
    universal_rna = util.fantom_code_selector(file_type, data_1, "universal", not_include=None)
    data_1.drop(universal_rna, axis=1, inplace=True)
    to_keep = util.fantom_sample_category_selector("sample types - FANTOM5.csv", sample_types)
    data = pd.DataFrame(index=data_1.index.values)
    for sample in to_keep:
        data_temp = data_1.filter(regex=sample)
        data = data.join(data_temp)
    codes = util.fantom_code_selector(file_type, data, celltype, not_include=not_include)
    try:
        if not codes.tolist():
            raise Exception("No codes for {}!".format(celltype))
    except AttributeError:
        if not isinstance(codes, list):
            raise Exception("No codes for {}!".format(celltype))
    print("Cell types to get VEnCodes:", *codes, sep="\n", end="\n\n")
    if celltype_exclude is not None:
        codes_exclude = util.fantom_code_selector(file_type, data, celltype_exclude)
        try:
            for code in codes:
                codes_exclude = [x for x in codes_exclude if x != code]
        except ValueError:
            pass
        print("Cell types to exclude:", *codes_exclude, sep="\n", end="\n\n")
        data.drop(codes_exclude, axis=1, inplace=True)

    for code in codes:
        print("donor:", code, sep="\n", end="\n\n")
        codes_2 = [x for x in codes if x != code]
        # codes_2 = codes[:]
        # for x in code: codes_2.remove(x)
        donors_data = data[codes_2]
        data_2 = data.drop(codes_2, axis=1)
        print("donors to exclude:", *codes_2, sep="\n", end="\n\n")
        filter_2 = util.df_filter_by_expression_and_percentile(data_2, code, expression, 2, threshold)

        ven_diagram = {}
        for r in reversed(range(1, (len(codes_2) + 1))):
            for z in iter.combinations(codes_2, r):
                z = list(z)
                string_z = "".join(z)
                ven_diagram[string_z] = []

        n = 0
        while n < vens_to_take:
            sample = filter_2.sample(n=combinations_number)
            sample_dropped = sample.drop(code, axis=1).values
            assess_if_vencode = np.any(sample_dropped == 0, axis=0)
            if all(assess_if_vencode):
                n += 1
                donors_data_sample = donors_data.loc[sample.index.values]
                no_ven = True
                counter = 0
                for i in reversed(range(1, (len(codes_2) + 1))):
                    for y in iter.combinations(codes_2, i):
                        y = list(y)
                        string_y = "".join(y)
                        to_assess = donors_data_sample[y]
                        assess_if_not_vencode_donors = np.any(to_assess.values == 0, axis=0)
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
                        # percentage_ven = counter / vens_to_take * 100
            else:
                pass
        for key in ven_diagram:
            ven_diagram[key] = sum(ven_diagram[key])

        if not os.path.exists("./Figure 3-b2/{}/".format(file_type)):
            os.makedirs("./Figure 3-b2/{}/".format(file_type))
        folder = "/Figure 3-b2/{}/".format(file_type)
        find = code.find("donor")
        substring = code[find:(find + 6)]
        file_name = u"/VEnCode for {} - {}".format(substring, celltype)
        utils.writing_files.write_one_value_dict_to_csv(file_name + ".csv", ven_diagram, folder)

        # code_in_string = ' '.join(code)
        # partial_dict[code_in_string] = partial_perc_not_ven
        #
        # mean = np.mean(partial_perc_not_ven, dtype=np.float64)
        # total_perc_not_ven.append(mean)

    print("Process Quick finished in %s seconds" % (time.time() - start_time))
    return


def ven_perc_per_celltype(file, file_type, cell_list, combinations_number, samples_to_take, reps, threshold=90,
                          expression=1, celltype_exclude=None, not_include=None,
                          sample_types="primary cells"):
    # Set up logging:
    folder = "./Percentage/"
    if not os.path.exists(folder):
        os.makedirs(folder)
    log_file = "./Percentage/log {}_cell k_{}.txt".format(len(cell_list), combinations_number)
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='w')
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


# Starting the show:

if __name__ == "__main__":
    # region Timeit!
    # from timeit import Timer
    # args = ""
    # t = Timer(lambda: insert_function(args))
    # print(t.timeit(5))
    # endregion


    """
    p1 = Process(target=ven_robustness_test, args=("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "Iris", [1, 2, 3, 4], 40000, 10))
    p1.start()
    print("start process 1")
    p2 = Process(target=ven_robustness_test, args=("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "Schwannoma", [1, 2, 3, 4], 40000, 10))
    p2.start()
    print("start process 2")
    p1.join()
    p2.join()
    """
    """
    script, first, second, third = argv
    # percentage_full_vencodes(first, int(second), None, None, int(third))
    # percentage_possible_vencodes(first, int(second), None, None, int(third))
    p1 = Process(target=percentage_possible_vencodes, args=(first, int(second), None, None, int(third)))
    p1.start()
    p2 = Process(target=percentage_full_vencodes, args=(first, int(second), None, None, int(third)))
    p2.start()
    """

# TODOs:


"""Unit tests"""
# cmd: python Main_Fantom.py hg19.cage_peak_phase1and2combined_tpm.osc.txt 4 6

# enhancers_improved_vencodes("abc-cell-gpl570-formatted_v3.csv", "caco2_cell_line:caco2_cell_line", 100, 4, 2, write_file=True)
enhancers_improved_vencodes("Human.sample_name2library_id.txt",
                            "human_permissive_enhancers_phase_1_and_2_expression_tpm_matrix.txt", "iris",
                            k=4, n=1, write_file=True)
# promoters_improved_vencodes("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "iris", n=1, write_file=True)

# percentage_full_vencodes_for_graph("hg19.cage_peak_phase1and2combined_tpm.osc.txt",
#                                 ["langerhans", "iris", "schwannoma"], x=None, y=90, s=5)

# ven_robustness_test("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "iris", 4, 100, 1)
# multiple_ven_robustness_test("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "schwannoma", 4, 100, 1,
#                              1)

# sorted_ven_robustness_test("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "mast cell", 4, 1000, 2,
#                            not_include=["stimulated", "expanded"], celltype_exclude="mast cell")
# sorted_ven_robustness_test("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "Mature adipocyte", 4, 1000, 2,
#                            expression=1, celltype_exclude=["adipocyte differentiation", "adipose tissue", "CNhs13972", "CNhs13973", "CNhs13974", "CNhs13975", "adipogenic"])
# sorted_ven_robustness_test("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "Chondrocyte", 4, 1000, 2,
#                            expression=1, celltype_exclude=False, not_include=["re"])



# region for setting Global Variables
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
                              "Perineurial Cells", "Peripheral Blood Mononuclear Cells", "Placental Epithelial Cells",
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
                              "Tracheal Epithelial Cells", "Urothelial cells", "Whole blood"]
complete_primary_non_include_list = {"Adipocyte - breast": "pre", "Adipocyte - omental": "pre",
                                     "Adipocyte - perirenal": "pre", "Adipocyte - subcutaneous": "pre",
                                     "CD14+ Monocytes": "CD16", "Endothelial Cells - Vein": "Umbilical",
                                     "Renal Epithelial Cells": "Cortical",
                                     "Skeletal Muscle Cells": ["satellite", "differentiated"]}
complete_primary_exclude_list = ["mesenchymal precursor cell - ovarian", "Osteoblast - differentiated"]
# endregion


# region for figure generation

""" Figure 1 """
# figure_1_include_list = ["Myoblast", "Oligodendrocyte", "Iris", "Basophils", "Dendritic plasmacytoid",
#                          "Dendritic monocyte", "Astrocyte", "Astrocyte cerebellum", "Astrocyte cerebral cortex",
#                          "Neurons", "Mature adipocyte", "Chondrocyte", "Corneal epithelial", "Eosinophils",
#                          "Fibroblast cardiac", "Fibroblast dermal", "Fibroblast lung", "Fibroblast lymphatic",
#                          "Fibroblast mammary", "Fibroblast choroid", "Fibroblast gingival", "Gingival epithelial",
#                          "Dermal papilla", "Root sheath", "Hepatocyte", "Hepatic sinusoid endothelial", "Keratinocyte",
#                          "Lens epithelial", "Macrophage monocyte", "Mammary epithelial", "Mast cell", "Meningeal cells",
#                          "Mesothelial cells", "Myoblast", "Natural killer cells", "Neutrophil", "Nucleus pulposus cell",
#                          "Olfactory epithelial", "Osteoblast", "Pericytes", "Perineurial cells", "Placental epithelial",
#                          "Prostate epithelial", "Prostate stromal", "Renal epithelial", "Renal mesangial",
#                          "Retinal epithelial", "Schwann cells", "Sebocyte", "Sertoli cells", "Synoviocyte",
#                          "Trabecular meshwork cells", "Migratory Langerhans cells", "Tenocyte"]

# small_list = ["Myoblast", "Oligodendrocyte", "Iris", "Basophils", "Dendritic plasmacytoid",
#              "Dendritic monocyte", "Mature adipocyte"]

# even_smaller_list = ["Myoblast", "Oligodendrocyte", "Iris", "Basophils"]

# def test_figure1_list(file, file_type, celltypes, combinations_number, samples_to_take, reps, threshold=90,
#                       expression=1, celltype_exclude=None, not_include=None, multi_plot=False, init_data=None,
#                       sample_types="primary cells"):
#     if init_data is None:
#         start_time = time.time()
#         raw_data = pd.read_csv("./Files/" + file, sep="\t", index_col=0,
#                                skiprows=1831, nrows=1000)  # nrows=x if we want to load only a few rows
#         data_1 = raw_data.drop(raw_data.index[[0, 1]])
#         universal_rna = Defs.fantom_code_selector(file_type, data_1, "universal", not_include=None)
#         data_1.drop(universal_rna, axis=1, inplace=True)
#         to_keep = Defs.sample_category_selector("sample types - FANTOM5.csv", sample_types)
#         data = pd.DataFrame(index=data_1.index.values)
#         for sample in to_keep:
#             data_temp = data_1.filter(regex=sample)
#             data = data.join(data_temp)
#     else:
#         data = init_data
#     for celltype in celltypes:
#         # try:
#         codes = Defs.fantom_code_selector(file_type, data, celltype, not_include=not_include)
#         if not codes.tolist():
#             raise Exception("No codes for {}!".format(celltype))
#         # except:
#         #     e = sys.exc_info()[0]
#         #     print("Error: {} for {}".format(e, celltype))
#         print(celltype, codes, sep="\n", end="\n\n")
#     return
#
# test_figure1_list("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", complete_primary_cell_list, 4, 1000,
#  2, expression=1)

# figure_1_not_include_list = {"Myoblast": ["myoblast differentiation", "myoblastoma"]}
# figure_1_exclude_list = {"Neurons": "iPS neuron", "Myoblast": "myoblast differentiation"}

# figure_1("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", complete_primary_cell_list, [4], 1000, 2,
#          expression=1,
#          multi_plot=True, not_include=complete_primary_non_include_list, celltype_exclude=complete_primary_exclude_list,
#          include_problems=True)

""" End figure 1 """

""" Figure 2

# figure_2_include_list = ["Myoblast", "Oligodendrocyte", "Iris", "Basophils", "Dendritic plasmacytoid",
#                          "Dendritic monocyte", "Astrocyte", "Astrocyte cerebellum", "Astrocyte cerebral cortex",
#                          "Neurons", "Mature adipocyte", "Chondrocyte", "Corneal epithelial", "Eosinophils",
#                          "Fibroblast lung", "Fibroblast lymphatic",
#                          "Fibroblast mammary", "Fibroblast choroid",
#                          "Dermal papilla", "Root sheath", "Hepatocyte",
#                          "Lens epithelial", "Macrophage monocyte", "Mammary epithelial", "Mast cell", "Meningeal cells",
#                          "Mesothelial cells", "Myoblast", "Neutrophil",
#                          "Olfactory epithelial", "Pericytes", "Placental epithelial",
#                          "Prostate stromal", "Renal epithelial", "Renal mesangial",
#                          "Retinal epithelial", "Schwann cells", "Sertoli cells", "Synoviocyte",
#                          "Trabecular meshwork cells", "Migratory Langerhans cells", "Tenocyte"]
#
# figure_2_small_list = ["Dendritic monocyte", "Myoblast", "Oligodendrocyte", "Iris", "Basophils", "Dendritic plasmacytoid", "Mature adipocyte"]


figure_2("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", complete_primary_cell_list, 4, 20, 1,
         expression=1,
         get_vencodes=False, celltype_exclude=complete_primary_exclude_list,
         not_include=complete_primary_non_include_list)

 end figure 2 """

""" Figure 3

# figure_3("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "mast cell", 300,
#          not_include=["stimulated", "expanded"], celltype_exclude="mast cell")

figure_3_b2("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "mast cell", 1000,
            not_include=["stimulated", "expanded"], celltype_exclude="mast cell")
"""

# ven_perc_per_celltype("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", "Adipocyte - perirenal", 4,
#                       1000, 20,expression=1, not_include=complete_primary_non_include_list,
#                       celltype_exclude=complete_primary_exclude_list)
# endregion
