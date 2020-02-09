import logging
import time

import matplotlib.pyplot as plt
import pandas as pd

import utils.writing_files
from utils import util


# region "Figures for paper"
def figure_2(file, file_type, cell_list, combinations_number, vens_to_take, reps, threshold=90,
             expression=1, celltype_exclude=None, not_include=None, multi_plot=False, init_data=None,
             sample_types="primary cells", get_vencodes=False):
    # Set up logging:
    logging.basicConfig(
        filename="./Figure 2/{}/log {}_celltp {}_VEn.txt".format(file_type, len(cell_list), vens_to_take),
        level=logging.DEBUG, format="{asctime} - {levelname} - {message}", filemode='w', style="{")
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


# endregion "Figures for paper"

# region "Global TODOs"

# endregion "Global TODOs"

# region "Global Variables"
# note: complete_primary_cell_list is OUTDATED. Check figures_1.py file for updated version.
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
# figure_2_small_list = ["Dendritic monocyte", "Myoblast", "Oligodendrocyte", "Iris", "Basophils",
#                        "Dendritic plasmacytoid", "Mature adipocyte"]

# endregion "Global variables"


# region "Unit Tests"
if __name__ == "__main__":
    # region Timeit!
    # from timeit import Timer
    # args = ""
    # t = Timer(lambda: insert_function(args))
    # print(t.timeit(5))
    # endregion

    figure_2("hg19.cage_peak_phase1and2combined_tpm.osc.txt", "Promoters", complete_primary_cell_list, 4, 20, 1,
             expression=1,
             get_vencodes=False, celltype_exclude=complete_primary_exclude_list,
             not_include=complete_primary_non_include_list)
# endregion "Unit Tests"
