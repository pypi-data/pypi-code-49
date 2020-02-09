#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" internal_extensions.py: file with extended methods and objects based on internals.py """

import os
from pathlib import Path
import pandas as pd
from tqdm import tqdm
from VEnCode import internals
from VEnCode.utils import exceptions, pandas_utils as pd_util, general_utils as gen_util, dir_and_file_handling as dhs
from VEnCode import common_variables as cv
from VEnCode.utils import validation_utils as val_util


class GettingVencodes:
    """
    thresholds for non target cell type inactivity, target cell type activity and regulatory element sparseness can
    be supplied as a keyword argument: thresholds = (non_target_celltypes_inactivity, target_celltype_activity,
    reg_element_sparseness).
    """

    def __init__(self, cell_type, data_type, algorithm, n_regulatory_elements, n_samples=10000, using=None):
        self.cell_type = cell_type
        self.data_type = data_type
        self.algorithm = algorithm
        self.k = n_regulatory_elements
        self.n_samples = n_samples
        self.using = using

    def _get_sample_type(self, sample_type):
        if sample_type:
            return sample_type

        if self.cell_type in cv.primary_cell_list:
            sample_type = "primary cells"
        elif any([self.cell_type in cancer for cancer in (cv.cancer_celltype_list, cv.cancer_donors_list)]):
            sample_type = "cell lines"
        else:
            parent_path = os.path.join(str(Path(__file__).parents[2]), "Files")
            sample_type_file = pd.read_csv(os.path.join(parent_path, cv.sample_type_file), sep=",",
                                           index_col=0,
                                           engine="python")
            if sample_type_file["Name"].str.contains(self.cell_type).any():
                sample_category = sample_type_file.loc[
                    sample_type_file['Name'].str.contains(self.cell_type), ['Sample category']]
                if len(sample_category["Sample category"].unique()) == 1:
                    sample_type = sample_category["Sample category"][0]
                else:
                    raise exceptions.SampleTypeNotSupported(sample_type, self.cell_type)
            else:
                raise exceptions.SampleTypeNotSupported(sample_type, self.cell_type)
        return sample_type

    def _thresholds(self):
        non_target_celltypes_inactivity = 0
        if self.data_type == "enhancers":
            target_celltype_activity = 0.1
        elif self.data_type == "promoters":
            target_celltype_activity = 0.5
        else:
            raise AttributeError("data_type - {} - currently not supported".format(self.data_type))
        if self.algorithm == "heuristic":
            reg_element_sparseness = 0
        elif self.algorithm == "sampling":
            reg_element_sparseness = 90
        else:
            raise AttributeError("Algorithm - {} - currently not supported".format(self.algorithm))
        return non_target_celltypes_inactivity, target_celltype_activity, reg_element_sparseness

    def _get_thresholds(self, thresholds):
        if thresholds:
            non_target_celltypes_inactivity, target_celltype_activity, reg_element_sparseness = thresholds
        else:
            non_target_celltypes_inactivity, target_celltype_activity, reg_element_sparseness = self._thresholds()
        return non_target_celltypes_inactivity, target_celltype_activity, reg_element_sparseness

    def _get_re_file_name(self):
        if self.data_type == "enhancers":
            file_name = cv.enhancer_file_name
        elif self.data_type == "promoters":
            file_name = cv.promoter_file_name
        else:
            raise AttributeError("data_type - {} - currently not supported".format(self.data_type))
        return file_name

    def _filters(self, data, thresholds):
        non_tgt_ctp_inact, tgt_ctp_act, reg_el_spsness = self._get_thresholds(thresholds)
        data.filter_by_target_celltype_activity(threshold=tgt_ctp_act, binarize=False)
        data.filter_by_reg_element_sparseness(threshold=reg_el_spsness)
        data.define_non_target_celltypes_inactivity(threshold=non_tgt_ctp_inact)
        if self.algorithm != "sampling":
            data.sort_sparseness()
        return data

    def _prepare_data_parsed(self, *args, **kwargs):
        raise NotImplementedError("Please Implement this method")

    def _prepare_data_raw_adding_ctp(self, *args, **kwargs):
        raise NotImplementedError("Please Implement this method")

    def _get_data(self, sample_type, parsed, thresholds):
        sample_type = self._get_sample_type(sample_type)
        if parsed:
            data = self._prepare_data_parsed(sample_type, thresholds)
        else:
            data = self._prepare_data_raw_adding_ctp(sample_type, thresholds)
        return data

    def _get_vencode(self, amount, sample_type, parsed, thresholds, n_samples=10000, using=None):
        data = self._get_data(sample_type, parsed, thresholds)
        if self.algorithm == "sampling":
            vencodes = internals.Vencodes(data, algorithm="sampling", number_of_re=self.k, n_samples=n_samples,
                                          using=using)
        elif self.algorithm == "heuristic":
            vencodes = internals.Vencodes(data, algorithm="heuristic", number_of_re=self.k, stop=3)
        else:
            raise AttributeError("Algorithm '{}' not recognized".format(self.algorithm))
        vencodes.next(amount=amount)
        if vencodes.vencodes:
            return vencodes
        else:
            raise exceptions.NoVencodeError("No VEnCodes found for {}!".format(self.cell_type))


class GetVencodeValidated(GettingVencodes):
    """
    Gets VEnCodes
    thresholds must be a list or tuple with the format:
    (non_target_celltypes_inactivity, target_celltype_activity, reg_element_sparseness)
    """
    def __init__(self, validate_with, number_vencodes=1, parsed=False, sample_type=None, thresholds=(), *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.validate_with = validate_with
        self.vencodes = self._get_vencode(number_vencodes, sample_type, parsed, thresholds, n_samples=self.n_samples,
                                          using=self.using)

    def _prepare_data_parsed(self, sample_type, thresholds):
        data = internals.DataTpmValidated(self.validate_with, file="parsed", sample_types=sample_type,
                                          data_type=self.data_type)
        data.make_data_celltype_specific(self.cell_type)
        data.select_validated()
        data = self._filters(data, thresholds)
        return data

    def _prepare_data_raw_adding_ctp(self, sample_type, thresholds):
        file_name = self._get_re_file_name()
        data = internals.DataTpmValidated(self.validate_with, file=file_name, sample_types="primary cells",
                                          data_type=self.data_type)
        data.merge_donors_primary(exclude_target=False)
        data.add_celltype(self.cell_type, file=file_name, sample_types=sample_type, data_type=self.data_type)
        data.make_data_celltype_specific(self.cell_type)
        data.select_validated()
        data = self._filters(data, thresholds)
        return data


class GetVencode(GettingVencodes):
    def __init__(self, number_vencodes=1, parsed=False, sample_type=None, thresholds=(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vencodes = self._get_vencode(number_vencodes, sample_type, parsed, thresholds, n_samples=self.n_samples)

    def _prepare_data_parsed(self, sample_type, thresholds):
        data = internals.DataTpm(file="parsed", sample_types=sample_type, data_type=self.data_type)
        data.make_data_celltype_specific(self.cell_type)
        data = self._filters(data, thresholds)
        return data

    def _prepare_data_raw_adding_ctp(self, sample_type, thresholds):
        file_name = self._get_re_file_name()
        data = internals.DataTpm(file=file_name, sample_types="primary cells", data_type=self.data_type)
        data.merge_donors_primary(exclude_target=False)
        data.add_celltype(self.cell_type, file=file_name, sample_types=sample_type, data_type=self.data_type)
        data.make_data_celltype_specific(self.cell_type)
        data = self._filters(data, thresholds)
        return data


class GetVencodeExternalData(GettingVencodes):
    """
    Gets VEnCodes
    thresholds must be a list or tuple with the format:
    (non_target_celltypes_inactivity, target_celltype_activity, reg_element_sparseness)
    """
    def __init__(self, validate_with, number_vencodes=1, parsed=False, sample_type=None, thresholds=(), *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.validate_with = validate_with
        self.vencodes = self._get_vencode(number_vencodes, sample_type, parsed, thresholds, n_samples=self.n_samples,
                                          using=self.using)

    def _prepare_data_parsed(self, sample_type, thresholds):
        data = internals.DataTpmValidated(self.validate_with, file="parsed", sample_types="primary cells",
                                          data_type=self.data_type)
        data.make_data_celltype_specific("Hepatocyte")
        data.merge_donors_primary(exclude_target=False)
        # data.add_celltype(self.cell_type, file=file_name, sample_types=sample_type, data_type=self.data_type)
        data.merge_external_cell_type(self.cell_type)
        data = self._filters(data, thresholds)
        return data

    def _prepare_data_raw_adding_ctp(self, sample_type, thresholds):
        file_name = self._get_re_file_name()
        data = internals.DataTpmValidated(self.validate_with, file=file_name, sample_types="primary cells",
                                          data_type=self.data_type)
        data.merge_donors_primary(exclude_target=False)
        data.merge_external_cell_type(self.cell_type)
        data.make_data_celltype_specific(self.cell_type)
        data = self._filters(data, thresholds)
        return data


class Validator:
    """
    Validation methods between already generated VEnCodes and an external set of enhancers.
    - Enhancer data set must have a the following columns: "Chromosome" and "range", corresponding to the genomic
    location of each enhancer. (hg19 coordinates)
    """

    def __init__(self, cell_type, data_type, algorithm, n_regulatory_elements, number_vencodes=1, parsed=False,
                 thresholds=(), n_samples=10000, sample_type=None, validate_with=None):
        self._results = None
        self._match_percentages = []
        self.average_match_percentage = None
        if validate_with is None:
            try:
                data = GetVencode(cell_type=cell_type, data_type=data_type, algorithm=algorithm,
                                  n_regulatory_elements=n_regulatory_elements,
                                  number_vencodes=number_vencodes, parsed=parsed, thresholds=thresholds,
                                  sample_type=sample_type, n_samples=n_samples)
            except exceptions.NoVencodeError as e:
                raise e
        else:
            try:
                data = GetVencodeValidated(validate_with=validate_with, cell_type=cell_type, data_type=data_type,
                                           algorithm=algorithm, n_regulatory_elements=n_regulatory_elements,
                                           number_vencodes=number_vencodes, parsed=parsed, thresholds=thresholds,
                                           sample_type=sample_type)
            except exceptions.NoVencodeError as e:
                raise e
        self.vencodes = data.vencodes.get_vencode_data(method="return")

    @property
    def results(self):
        """
        Cross validation results.
        :return: pd.DataFrame with the results.
        """
        return self._results

    @results.setter
    def results(self, df):
        if isinstance(self._results, type(None)) or self._results.empty:
            self._results = df
        else:
            self._results = pd.concat([self._results, df])

    def _update_match_percentage(self, new_values):
        self._match_percentages.extend(new_values)
        self.average_match_percentage = sum(self._match_percentages) / len(self._match_percentages)

    @staticmethod
    def _vencode_cleaner(vencode):
        vencode["Id"] = vencode.index
        vencode[["Chromosome", "temp"]] = vencode.Id.str.split(":", expand=True)
        vencode[["Start", "End"]] = vencode.temp.str.split("-", expand=True)
        vencode = vencode[["Chromosome", "Start", "End"]]
        pd_util.columns_to_numeric(vencode, "Start", "End")
        return vencode

    def reset_match_percentages(self):
        """
        Call this to reset the results for VEnCode-DataSet matching percentage
        """
        self._match_percentages = []
        self.average_match_percentage = None

    def calculate_match_percentage(self, data, source=None):

        """
        Calculates the percentage of match between the genomic locations of the REs that make up a VEnCode and
        the REs from an outside Data set.
        :param data: Data as pd.DataFrame, formatted as by class OutsideData.
        :param source: Source of the data for special treatment (if supported). So far, supported "Barakat".
        """

        def _update_decision(set_type):
            if source == "BarakatTS2018":
                _update_results_complex(set_type, "Enhancer module")
            elif source == "DennySK2016":
                _update_results_complex(set_type, "Score")
            else:
                _update_results_basic("Subset")

        def _update_results_complex(set_type, *args):
            arg_lst = []
            for arg in args:
                value = data_filter_chr[data_filter_chr.Start == range2[0]][arg].values[0]
                arg_lst.append(value)
            results[index] = [set_type] + arg_lst

        def _update_results_basic(set_type):
            results[index] = [set_type]

        def _create_results_df(*cols):
            vencode_coordinates = vencode.index.tolist()
            to_df = {"VEnCode": ",".join(str(coord) for coord in vencode_coordinates)}
            for idx, val in enumerate(cols):
                values = [item[idx] for item in results.values()]
                to_df[val] = ",".join(str(x) for x in values)
            to_df["Percentage_Match"] = percent_matching_i
            df = pd.DataFrame(to_df, index=[0])
            return df

        percent_matching = []
        # Cycle each VEnCode
        for vencode in self.vencodes:
            vencode = self._vencode_cleaner(vencode)
            results = {}
            for index, row in vencode.iterrows():
                range1 = [row["Start"], row["End"]]
                data_filter_chr = data[data["Chromosome"] == row.iloc[0]]
                range2_list = data_filter_chr["range"].tolist()
                for range2 in range2_list:
                    condition = gen_util.subset_of_span(range1, range2)
                    if condition:
                        _update_decision("Subset")
                        break
                    condition = gen_util.partial_subset_of_span(range1, range2)
                    if condition:
                        _update_decision("Partial subset")
                        break
            percent_matching_i = len(results) / vencode.shape[0] * 100
            if source == "BarakatTS2018":
                results_df = _create_results_df("Match", "Module")
            elif source == "DennySK2016":
                results_df = _create_results_df("Match", "Score")
            else:
                results_df = _create_results_df("Match")
            self.results = results_df
            percent_matching.append(percent_matching_i)
        self._update_match_percentage(percent_matching)


class Assays:
    """
    Pre-designed validation assays: calculate VEnCodes' RE match percentage to an external data set.
    List of external data sets supported:
    - Barakat2018
    - InoueF2017
    - DennySK2016
    - ChristensenCL2014
    - WangX2018
    - LiuY2017
    """

    def __init__(self, database, algorithm="sampling", parsed=True, validate_with=None, cell_type=None, **kwargs):
        self.database, self.celltype = database, cell_type
        self.algorithm, self.parsed, self.validate_with = algorithm, parsed, validate_with
        self.data_type = kwargs.get("data_type", "enhancers")
        self.sample_type = kwargs.get("sample_type", "cell lines")
        self.thresholds = kwargs.get("thresholds", (0, 0.1, 90))
        self.number_vencodes = kwargs.get("number_vencodes", 200)
        self.n_regulatory_elements = kwargs.get("n_regulatory_elements", 4)
        self.n_samples = kwargs.get("n_samples", 10000)
        try:
            self.data = self._data_handler(**kwargs)
        except AttributeError:
            self.data = val_util.get_data_to_validate(self.celltype, optional=self.database)
        self.results = pd.DataFrame()

    def _data_handler(self, **kwargs):
        if self.database == "BarakatTS2018":
            data = internals.BarakatTS2018Data(**kwargs)
        elif self.database == "InoueF2017":
            data = internals.InoueF2017Data()
        elif self.database == "DennySK2016":
            data = internals.BroadPeak(self.database)
        elif self.database == "ChristensenCL2014":
            data = internals.ChristensenCL2014Data(**kwargs)
        elif self.database == "WangX2018":
            data = internals.Bed(self.database)
        elif self.database == "LiuY2017":
            data = internals.BroadPeak(self.database)
        else:
            raise AttributeError("Wrong Cross-Validation data")
        return data

    def _validator(self, celltype):
        try:
            validator = Validator(celltype, self.data_type, self.algorithm, self.n_regulatory_elements, parsed=self.parsed,
                                  number_vencodes=self.number_vencodes, sample_type=self.sample_type,
                                  thresholds=self.thresholds, n_samples=self.n_samples,
                                  validate_with=self.validate_with)
        except exceptions.NoVencodeError as e:
            raise e
        return validator

    def _filename(self):
        if self.validate_with is None:
            filename = "validation {}".format(self.algorithm)
        else:
            filename = "validation {} - {}".format(self.algorithm, "validated")
        return filename

    def to_csv(self, path=None):
        """ Get the results from this validation as a CSV file. """
        if path:
            results_directory = path
        else:
            filename = self._filename()
            results_directory = dhs.check_if_and_makefile(os.path.join("Validations", self.database, filename),
                                                          path_type="parent3")
        self.results.to_csv(results_directory, index=False, sep=";")
        print("Results stored in {}".format(results_directory))


class Assay(Assays):
    """
    Experimental assay.
    supported kwargs:
    - "data" = a str selecting only one external data set for validation, in cases where more than one are merged
    together.
    - "sample_type" = a str corresponding to the FANTOM5 type of sample (primary_cells, cell_types, tissues, etc)
    most of the times not needed because algorithm tries to infer.
    """

    def __init__(self, database, algorithm, parsed=True, validate_with=None, **kwargs):
        super().__init__(database, algorithm, parsed=parsed, validate_with=validate_with, **kwargs)
        self._validate()

    def _validate(self):
        validator = self._validator(celltype=self.celltype)
        validator.calculate_match_percentage(self.data.data, source=self.data.data_source)
        self.results = validator.results

    def _filename(self):
        if self.validate_with is None:
            filename = "{} - {}".format(self.celltype, self.algorithm)
        else:
            filename = "{} - {} - {}".format(self.celltype, self.algorithm, "validated")
        return filename


class NegativeControl(Assays):
    """ Negative control assay: validation assay but with VEnCodes for every primary cell type. """

    def __init__(self, database, algorithm, parsed=True, cell_types_to_test=False, **kwargs):
        super().__init__(database, algorithm, parsed=parsed, **kwargs)
        self.celltypes_to_cycle = self._celltypes_to_cycle(cell_types_to_test)
        self._validate()

    @staticmethod
    def _celltypes_to_cycle(cell_types_to_test):
        if cell_types_to_test:
            celltypes_to_cycle = cell_types_to_test
        else:
            celltypes_no_vencodes_sampling = ['Bronchial Epithelial Cell', 'Cardiac Myocyte',
                                              'CD133+ stem cells - adult bone marrow derived',
                                              'CD133+ stem cells - cord blood derived', 'CD14- CD16+ Monocytes',
                                              'CD14+ CD16- Monocytes', 'CD14+ CD16+ Monocytes',
                                              'CD14+ monocyte derived endothelial progenitor cells', 'CD14+ Monocytes',
                                              'CD19+ B Cells', 'CD34+ Progenitors',
                                              'CD34+ stem cells - adult bone marrow derived',
                                              'CD4+ T Cells', 'CD4+CD25+CD45RA- memory regulatory T cells',
                                              'CD4+CD25+CD45RA+ naive regulatory T cells',
                                              'CD4+CD25-CD45RA- memory conventional T cells',
                                              'CD4+CD25-CD45RA+ naive conventional T cells', 'CD8+ T Cells',
                                              'Chondrocyte',
                                              'common myeloid progenitor CMP', 'Corneal Epithelial Cells',
                                              'Dendritic Cells - monocyte immature derived', 'Eosinophils',
                                              'Esophageal Epithelial Cells', 'Fibroblast - Cardiac',
                                              'Fibroblast - Choroid Plexus',
                                              'Fibroblast - Dermal', 'Fibroblast - Gingival', 'Fibroblast - Lymphatic',
                                              'Fibroblast - Mammary', 'Fibroblast - Periodontal Ligament',
                                              'Fibroblast - skin',
                                              'Fibroblast - Villous Mesenchymal', 'granulocyte macrophage progenitor',
                                              'Hepatic Sinusoidal Endothelial Cells',
                                              'Hepatic Stellate Cells (lipocyte)',
                                              'Intestinal epithelial cells (polarized)', 'Keratocytes', 'Melanocyte',
                                              'Mesenchymal stem cells - adipose',
                                              'Mesenchymal Stem Cells - bone marrow',
                                              'Mesenchymal stem cells - umbilical', 'Neutrophil', 'promyelocytes',
                                              'Schwann Cells',
                                              'Skeletal Muscle Cells', 'Smooth muscle cells - airway',
                                              'Smooth Muscle Cells - Aortic', 'Smooth Muscle Cells - Carotid',
                                              'Smooth Muscle Cells - Pulmonary Artery',
                                              'Smooth Muscle Cells - Tracheal',
                                              'Smooth Muscle Cells - Umbilical Vein', 'Trabecular Meshwork Cells']
            celltypes_to_cycle = [ctp for ctp in cv.primary_cell_list if ctp not in celltypes_no_vencodes_sampling]
        return celltypes_to_cycle

    def _validate(self):
        for celltype in tqdm(self.celltypes_to_cycle, desc="Completed: "):
            try:
                validator = self._validator(celltype)
            except exceptions.NoVencodeError:
                continue
            validator.calculate_match_percentage(self.data.data, source=self.data.data_source)
            validator.results.rename(columns={'Percentage_Match': celltype}, inplace=True)
            celltype_data = validator.results[celltype].reset_index(drop=True)
            self.results = pd.concat([self.results, celltype_data], axis=1)

    def _filename(self):
        filename = "control {} - {}".format("all celltypes", self.algorithm)
        return filename


class CheckElementExpression:
    """
    Use to check Regulatory Element expression in any FANTOM5 cell type.
    """

    def __init__(self, element_list, cell_type, data_type, sample_type=None, parsed=False):
        self.element_list = element_list
        self.cell_type = cell_type
        self.data_type = data_type
        self.data = self._get_data(sample_type, parsed)

    def export_expression_data(self, path=None, specific_ctp=None, method="csv"):
        if specific_ctp == "All":
            pass
        elif isinstance(specific_ctp, list):
            pass
        expression = self._get_expression_data()
        if method == "csv":
            expression.to_csv(path)
        elif method == "print":
            print(expression.values)
        elif method == "return":
            return expression

    def _get_expression_data(self):
        columns = self.data.ctp_analyse_donors[self.data.target_ctp]
        rows = self.element_list
        expression = self.data.data.loc[rows, columns]
        return expression

    def _get_data(self, sample_type, parsed):
        sample_type = self._get_sample_type(sample_type)
        if parsed:
            data = self._prepare_data_parsed(sample_type)
        else:
            data = self._prepare_data_raw(sample_type)
        return data

    def _prepare_data_parsed(self, sample_type):
        data = internals.DataTpm(file="parsed", sample_types=sample_type, data_type=self.data_type)
        data.make_data_celltype_specific(self.cell_type)
        return data

    def _prepare_data_raw(self, sample_type):
        file_name = self._get_re_file_name()
        data = internals.DataTpm(file=file_name, sample_types=sample_type, data_type=self.data_type)
        data.make_data_celltype_specific(self.cell_type)
        return data

    def _get_sample_type(self, sample_type):
        if sample_type:
            return sample_type

        if self.cell_type in cv.primary_cell_list:
            sample_type = "primary cells"
        elif any([self.cell_type in cancer for cancer in (cv.cancer_celltype_list, cv.cancer_donors_list)]):
            sample_type = "cell lines"
        else:
            parent_path = os.path.join(str(Path(__file__).parents[2]), "Files")
            sample_type_file = pd.read_csv(os.path.join(parent_path, cv.sample_type_file), sep=",",
                                           index_col=0,
                                           engine="python")
            if sample_type_file["Name"].str.contains(self.cell_type).any():
                sample_category = sample_type_file.loc[
                    sample_type_file['Name'].str.contains(self.cell_type), ['Sample category']]
                if len(sample_category["Sample category"].unique()) == 1:
                    sample_type = sample_category["Sample category"][0]
                else:
                    raise exceptions.SampleTypeNotSupported(sample_type, self.cell_type)
            else:
                raise exceptions.SampleTypeNotSupported(sample_type, self.cell_type)
        return sample_type

    def _get_re_file_name(self):
        if self.data_type == "enhancers":
            file_name = cv.enhancer_file_name
        elif self.data_type == "promoters":
            file_name = cv.promoter_file_name
        else:
            raise AttributeError("data_type - {} - currently not supported".format(self.data_type))
        return file_name
