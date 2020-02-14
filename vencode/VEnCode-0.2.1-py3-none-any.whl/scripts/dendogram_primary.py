#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
dendogram_primary.py: file used to generate hierarchical clustering and subsequent dendograms from FANTOM5
data
"""

import os
import sys

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

from VEnCode import internals
from VEnCode import common_variables as cv
from VEnCode import primary_cell_list

no_ven_prom = ['Bronchial Epithelial Cell', 'CD14+ Monocytes', 'CD4+ T Cells',
               'CD4+CD25+CD45RA+ naive regulatory T cells',
               'CD4+CD25-CD45RA- memory conventional T cells', 'CD8+ T Cells', 'Eosinophils',
               'Esophageal Epithelial Cells',
               'Fibroblast - Cardiac', 'Fibroblast - Dermal', 'Fibroblast - Gingival',
               'Fibroblast - Periodontal Ligament',
               'Fibroblast - skin', 'Melanocyte', 'Neutrophil', 'Skeletal Muscle Cells',
               'Smooth Muscle Cells - Carotid',
               'Smooth Muscle Cells - Prostate', 'Smooth Muscle Cells - Pulmonary Artery']

no_ven_enha = ['Bronchial Epithelial Cell', 'CD4+ T Cells', 'CD4+CD25-CD45RA+ naive conventional T cells',
               'CD4+CD25-CD45RA- memory conventional T cells', 'CD8+ T Cells', 'Cardiac Myocyte', 'Chondrocyte',
               'Dendritic Cells - monocyte immature derived', 'Eosinophils', 'Esophageal Epithelial Cells',
               'Fibroblast - Cardiac', 'Fibroblast - Dermal', 'Fibroblast - Gingival', 'Fibroblast - Lymphatic',
               'Fibroblast - Mammary', 'Fibroblast - Periodontal Ligament', 'Fibroblast - Villous Mesenchymal',
               'Fibroblast - skin', 'Hepatic Sinusoidal Endothelial Cells', 'Keratocytes', 'Melanocyte',
               'Mesenchymal Stem Cells - bone marrow', 'Mesenchymal stem cells - adipose',
               'Mesenchymal stem cells - umbilical', 'Neutrophil', 'Schwann Cells', 'Skeletal Muscle Cells',
               'Smooth Muscle Cells - Aortic', 'Smooth Muscle Cells - Carotid',
               'Smooth Muscle Cells - Pulmonary Artery', 'Smooth muscle cells - airway', 'Trabecular Meshwork Cells',
               'common myeloid progenitor CMP', 'granulocyte macrophage progenitor', 'promyelocytes']

data = internals.DataTpm(file=cv.enhancer_file_name, sample_types="primary cells", data_type="enhancers",
                         files_path="outside")
data.merge_donors_primary(exclude_target=False)

values = data.data.T.values
index = data.data.T.index

clustering = hierarchy.linkage(values, 'single')

dflt_col = "#808080"
dict_leaf_colors = dict()
for i in no_ven_enha:
    dict_leaf_colors[i] = "darkorange"
for c in primary_cell_list:
    if c not in dict_leaf_colors.keys():
        dict_leaf_colors[c] = dflt_col

plt.figure(figsize=(14, 14))
dn = hierarchy.dendrogram(clustering, labels=index, color_threshold=0, above_threshold_color='#333333',
                          leaf_rotation=0, orientation="left")

ax = plt.gca()
ylbls = ax.get_ymajorticklabels()
for lbl in ylbls:
    lbl.set_color(dict_leaf_colors[lbl.get_text()])

plt.savefig("dendo_primary.png", dpi=600, bbox_inches="tight")
