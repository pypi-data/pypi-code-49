import os
import traceback

from VEnCode.common_variables import promoter_file_name, enhancer_file_name
import VEnCode.internals_extensions as iext
from VEnCode.utils import dir_and_file_handling as dfh
from VEnCode.utils import validation_utils as val_util


class SetUp:
    """set up some variables: """
    cell_types = ["epitheloid carcinoma cell line: HelaS3 ENCODE", "embryonic kidney cell line: HEK293/SLAM untreated"]
    cell_types_1 = ["CD19+ B Cells", "CD34+ stem cells - adult bone marrow derived",
                    "neuroepithelioma cell line:SK-N-MC", "acute myeloid leukemia (FAB M3) cell line",
                    "hepatocellular carcinoma cell line: HepG2 ENCODE",
                    "B lymphoblastoid cell line: GM12878 ENCODE",
                    "acute lymphoblastic leukemia (T-ALL) cell line:Jurkat", "lung adenocarcinoma cell line:A549",
                    "colon carcinoma cell line:CACO-2", "chronic myelogenous leukemia cell line:K562",
                    "breast carcinoma cell line:MCF7", "Burkitt lymphoma cell line:RAJI"]
    sample_type = "cell lines"
    data_type = "enhancers"
    algorithm = "sampling"
    k = 4
    number_vencodes_to_get = 200

    data_set = "both"

    # Paths to export data:
    path_out_ven = os.path.join(
        "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/"
        "3-Vencode/Fantom5/Validations/enhancer_atlas_HelaHek_pooled.csv")

    # Next ones you may not need to change:
    non_target_celltypes_inactivity = 0
    if data_type == "enhancers":
        target_celltype_activity = 0.1
    elif data_type == "promoters":
        target_celltype_activity = 0.5
    else:
        raise AttributeError("data_type - {} - currently not supported".format(data_type))

    if algorithm == "heuristic":
        reg_element_sparseness = 0
    elif algorithm == "sampling":
        reg_element_sparseness = 90  # For some, you probably have to reduce sparseness to 0.
    else:
        raise AttributeError("Algorithm - {} - currently not supported".format(algorithm))


set_up = SetUp()
thresholds = (
    set_up.non_target_celltypes_inactivity, set_up.target_celltype_activity, set_up.reg_element_sparseness)

if __name__ == "__main__":
    results = {}
    for cell_type in set_up.cell_types:
        try:
            assay = iext.Assay(set_up.data_set, cell_type=cell_type, data_type=set_up.data_type,
                               n_regulatory_elements=set_up.k, number_vencodes=set_up.number_vencodes_to_get,
                               algorithm=set_up.algorithm, parsed=val_util.status_parsed(cell_type),
                               thresholds=thresholds, n_samples=10000, sample_type=set_up.sample_type)
            percent = [int(i) for i in assay.results["Percentage_Match"].values.tolist()]
            results[cell_type] = [percent.count(0), percent.count(25), percent.count(50), percent.count(75),
                                  percent.count(100)]
            dfh.write_dict_to_csv(set_up.path_out_ven, results, deprecated=False, method="w")
        except Exception:
            traceback.print_exc()
            continue
