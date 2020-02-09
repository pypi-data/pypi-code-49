#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" validations.py: Objects and methods to use for cross validating results taken from FANTOM5 data analysis. """

import os
import sys

import pandas as pd
from tqdm import tqdm

from VEnCode.internals import BarakatTS2018Data, InoueF2017Data, ChristensenCL2014Data, BroadPeak, Bed

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals_extensions
from VEnCode.common_variables import primary_cell_list
from VEnCode.utils import dir_and_file_handling as dhs
from VEnCode.utils import general_utils as gen_util
from VEnCode.utils import pandas_utils as pd_util
from VEnCode.utils import exceptions


class Validator:
    """
    Validation methods between already generated VEnCodes and an external set of enhancers.
    - Enhancer data set must have a the following columns: "Chromosome" and "range", corresponding to the genomic
    location of each enhancer. (hg19 coordinates)
    """

    def __init__(self, cell_type, data_type, algorithm, n_regulatory_elements, number_vencodes=1, parsed=False,
                 thresholds=(), sample_type=None):
        self._results = None
        self._match_percentages = []
        self.average_match_percentage = None
        try:
            data = internals_extensions.GettingVencodes(cell_type, data_type, algorithm, n_regulatory_elements,
                                                        number_vencodes, parsed, thresholds, sample_type)
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
    """

    def __init__(self, database, algorithm="sampling", parsed=True, **kwargs):
        self.database = database
        self.algorithm, self.parsed = algorithm, parsed
        self._sample_type(**kwargs)
        self.data = self._data_handler(**kwargs)
        self.results = pd.DataFrame()

    def _sample_type(self, **kwargs):
        try:
            self.sample_type = kwargs["sample_type"]
        except KeyError:
            self.sample_type = None

    def _data_handler(self, **kwargs):
        if self.database == "BarakatTS2018":
            data = BarakatTS2018Data(**kwargs)
        elif self.database == "InoueF2017":
            data = InoueF2017Data()
        elif self.database == "DennySK2016":
            data = BroadPeak(self.database)
        elif self.database == "ChristensenCL2014":
            data = ChristensenCL2014Data(**kwargs)
        elif self.database == "WangX2018":
            data = Bed(self.database)
        elif self.database == "LiuY2017":
            data = BroadPeak(self.database)
        else:
            raise AttributeError("Wrong Cross-Validation data")
        return data

    def _validator(self, celltype, sample_type=None):
        try:
            validator = Validator(celltype, "enhancers", self.algorithm, 4, parsed=self.parsed,
                                  number_vencodes=200, sample_type=sample_type)
        except exceptions.NoVencodeError as e:
            raise e
        return validator

    def _filename(self):
        filename = "validation - {}".format(self.algorithm)
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

    def __init__(self, database, algorithm, parsed=True, celltype=None, **kwargs):
        super().__init__(database, algorithm, parsed=parsed, **kwargs)
        self.celltype = celltype
        self._validate()

    def _validate(self):
        validator = self._validator(celltype=self.celltype, sample_type=self.sample_type)
        validator.calculate_match_percentage(self.data.data, source=self.data.data_source)
        self.results = validator.results

    def _filename(self):
        filename = "validation {} - {}".format(self.celltype, self.algorithm)
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
            celltypes_to_cycle = [ctp for ctp in primary_cell_list if ctp not in celltypes_no_vencodes_sampling]
        return celltypes_to_cycle

    def _validate(self):
        for celltype in tqdm(self.celltypes_to_cycle, desc="Completed: "):
            try:
                validator = self._validator(celltype, sample_type=self.sample_type)
            except exceptions.NoVencodeError:
                continue
            validator.calculate_match_percentage(self.data.data, source=self.data.data_source)
            validator.results.rename(columns={'Percentage_Match': celltype}, inplace=True)
            celltype_data = validator.results[celltype].reset_index(drop=True)
            self.results = pd.concat([self.results, celltype_data], axis=1)

    def _filename(self):
        filename = "validation control {} - {}".format("all celltypes", self.algorithm)
        return filename


