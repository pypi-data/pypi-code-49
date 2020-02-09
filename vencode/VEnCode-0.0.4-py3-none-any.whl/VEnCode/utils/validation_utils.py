from VEnCode import internals
from VEnCode import common_variables as cv


def get_data_to_validate(cell_type, file_name=None, **kwargs):
    """
    Gets the data used to validate, based on the target cell type.
    :return: internals.OutsideData object with the data that can be used to validate the cell type
    """

    enhancer_atlas_lines = {"acute myeloid leukemia (FAB M3) cell line": "HL-60",
                            "neuroepithelioma cell line:SK-N-MC": "SK-N-MC", "CD14+ Monocytes": "CD14+",
                            "CD19+ B Cells":"CD19+", "CD34+ stem cells - adult bone marrow derived": "CD34+",
                            "CD4+ T Cells": "CD4+", "CD8+ T Cells": "CD8+",
                            "acute lymphoblastic leukemia (T-ALL) cell line:Jurkat": "Jurkat",
                            "lung adenocarcinoma cell line:A549": "A549",
                            "colon carcinoma cell line:CACO-2" : "Caco-2",
                            "chronic myelogenous leukemia cell line:K562": "K562",
                            "breast carcinoma cell line:MCF7": "MCF-7",
                            "Burkitt lymphoma cell line:RAJI": "Raji",
                            "CD133+ stem cells": "CD133+",
                            "epitheloid carcinoma cell line: HelaS3 ENCODE": "Hela-S3",
                            "embryonic kidney cell line: HEK293/SLAM untreated": "HEK293"}

    optional = kwargs.get("optional", None)
    positions = kwargs.get("positions", None)
    splits = kwargs.get("splits")

    if cell_type == "hIPS":
        return internals.BarakatTS2018Data(data="core")
    elif cell_type == "hepatocellular carcinoma cell line: HepG2 ENCODE":
        if optional == "enhancer_atlas":
            return internals.Fasta("EnhancerAtlas-HepG2")
        elif optional == "both":
            data = internals.InoueF2017Data()
            data.join_data_sets(internals.Fasta("EnhancerAtlas-HepG2"))
            return data
        else:
            return internals.InoueF2017Data()
    elif cell_type == "B lymphoblastoid cell line: GM12878 ENCODE":
        if optional == "enhancer_atlas":
            return internals.Fasta("EnhancerAtlas-GM12878-Blymph")
        elif optional == "both":
            data = internals.Bed("WangX2018")
            data.join_data_sets(internals.Fasta("EnhancerAtlas-GM12878-Blymph"))
            return data
        else:
            return internals.Bed("WangX2018")
    elif cell_type == "prostate cancer cell line":
        return internals.BroadPeak("LiuY2017")
    elif cell_type == "small cell lung carcinoma cell line":
        if optional == "ChristensenCL2014":
            return internals.ChristensenCL2014Data()
        elif optional == "DennySK2016":
            return internals.BroadPeak("DennySK2016")
        elif optional == "both":
            return [internals.BroadPeak("DennySK2016"), internals.ChristensenCL2014Data()]
    elif cell_type == "small cell lung carcinoma cell line:NCI-H82":
        return internals.ChristensenCL2014Data(data="H82")
    elif cell_type in enhancer_atlas_lines:
        return internals.Fasta("EnhancerAtlas-{}".format(enhancer_atlas_lines.get(cell_type)))
    elif "singlecell" in cell_type:
        return internals.Csv(source=file_name, positions=positions, splits=splits)
    else:
        raise AttributeError("Cell Type {} to get validated VEnCodes still not supported".format(cell_type))


def status_parsed(cell_type):
    """
    Chooses whether the VEnCode module uses already parsed data sets or has to parse from the beginning.
    :param cell_type: cell type to analyse.
    :return: Boolean True or False
    """
    if cell_type in ("hIPS", "small cell lung carcinoma cell line:NCI-H82", "CD133+ stem cells"):
        return False
    elif cell_type in cv.primary_cell_list or cell_type in cv.cancer_celltype_list:
        return True
    elif cell_type in cv.cancer_donors_list:
        return False
    else:
        raise AttributeError("Cell Type {} to get validated VEnCodes still not supported".format(cell_type))