#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" validation.py: file used to cross-validate VEnCodes found using the FANTOM5 data set. """

import os
import sys
file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals
import VEnCode.internals_extensions as iext


cell_types = {"hips_assay": "hIPS", "hepG2_assay": "hepatocellular carcinoma cell line: HepG2 ENCODE",
              "sclc_chr_accessibility_assay": "small cell lung carcinoma cell line",
              "sclc_assay": "small cell lung carcinoma cell line", "h82_assay": "small cell lung carcinoma cell line",
              "b_lymph_assay": "B lymphoblastoid cell line- GM12878 ENCODE",
              "du145_assay": "prostate cancer cell line:DU145",
              "pc_3_assay": "prostate cancer cell line:PC-3"}

"""
# Barakat TS, 2018 assays:
# hips_assay = iext.Assay("BarakatTS2018", "sampling", celltype="hIPS", data="core", parsed=False)
validate_with = internals.BarakatTS2018Data(data="core")
hips_assay_val = iext.Assay("BarakatTS2018", "sampling", celltype="hIPS", data="core", parsed=False,
                            validate_with=validate_with)
hips_assay_val.to_csv()


# Inoue F, 2017 assays:
hepG2_assay = iext.Assay("InoueF2017", "sampling", celltype="hepatocellular carcinoma cell line: HepG2 ENCODE")
hepG2_assay.to_csv()

validate_with = internals.InoueF2017Data()
hepG2_assay_val = iext.Assay("InoueF2017", "sampling", celltype="hepatocellular carcinoma cell line: HepG2 ENCODE",
                             validate_with=validate_with)
hepG2_assay_val.to_csv()


# Denny SK, 2016 assays:
sclc_chr_accessibility_assay = iext.Assay("DennySK2016", "sampling",
                                          celltype="small cell lung carcinoma cell line")


# Wang X, 2018 assays:
b_lymph_assay = iext.Assay("WangX2018", "sampling", celltype="B lymphoblastoid cell line: GM12878 ENCODE")
b_lymph_assay.to_csv()

validate_with = internals.Bed("WangX2018")
b_lymph_assay_val = iext.Assay("WangX2018", "sampling", celltype="B lymphoblastoid cell line: GM12878 ENCODE",
                               validate_with=validate_with)
b_lymph_assay_val.to_csv()


# Christensen CL, 2014 assays:
h82_assay = iext.Assay("ChristensenCL2014", "sampling", celltype="small cell lung carcinoma cell line:NCI-H82",
                       data="H82", parsed=False)
h82_assay.to_csv()

validate_with = internals.ChristensenCL2014Data(data="H82")
h82_assay_val = iext.Assay("ChristensenCL2014", "sampling", celltype="small cell lung carcinoma cell line:NCI-H82",
                       data="H82", parsed=False, validate_with=validate_with)
h82_assay_val.to_csv()

h82_controls = iext.NegativeControl("ChristensenCL2014", "sampling", data="H82")
h82_controls.to_csv()


# Liu Y, 2017 assays:
du145_assay = iext.Assay("LiuY2017", "sampling", celltype="prostate cancer cell line:DU145", parsed=False)
du145_assay.to_csv()

pc_3_assay = iext.Assay("LiuY2017", "sampling", celltype="prostate cancer cell line:PC-3", parsed=False)
pc_3_assay.to_csv()

prostate_cancer_assay = iext.Assay("LiuY2017", "sampling", celltype="prostate cancer cell line", parsed=True)
prostate_cancer_assay.to_csv()

validate_with = internals.BroadPeak("LiuY2017")
du145_assay_val = iext.Assay("LiuY2017", "sampling", celltype="prostate cancer cell line:DU145", parsed=False,
                             validate_with=validate_with)
du145_assay_val.to_csv()

validate_with = internals.BroadPeak("LiuY2017")
pc_3_assay_val = iext.Assay("LiuY2017", "sampling", celltype="prostate cancer cell line:PC-3", parsed=False,
                            validate_with=validate_with)
pc_3_assay_val.to_csv()
"""
validate_with = internals.BroadPeak("LiuY2017")
prostate_cancer_assay_val = iext.Assay("LiuY2017", "sampling", cell_type="prostate cancer cell line", parsed=True,
                                       validate_with=validate_with)
prostate_cancer_assay_val.to_csv()
"""
lncap_controls = iext.NegativeControl("LiuY2017", "sampling")
lncap_controls.to_csv()
"""