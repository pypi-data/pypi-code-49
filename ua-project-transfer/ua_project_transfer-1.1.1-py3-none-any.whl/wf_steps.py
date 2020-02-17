"""A json-like master list of workflows and steps."""
# NOTE: Change these values to your workflows and steps in your environment.

WF_STEPS = {
    "dev": {
        "agena": {
            "cells": ("Agena Genotyping SAS", "Make Dilution Plate"),
            "gdna": ("Agena- Genotyping (Just Agena part)", "Agena- PCR")},
        "bioanalyzer": {
            "DNA": ("DNA Bioanalyzer Service", "Bioanalyzer Service DNA"),
            "RNA": ("RNA Bioanalyzer Service", "Bioanalyzer Service RNA")},
        "cla": {
            "cells": (
                "Cell Line Authentication v3", "ProK and Cook Samples"),
            "gdna": ("Cell Auth gDNA", "Autosomal STR PP16")},
        "extraction": {
            "DNA": ("DNA Extraction Multi", "Sort Extraction Samples"),
            "RNA": ("RNA Extraction", "Sort Extraction Samples RNA")},
        "frag": {
            "4dye": (
                "Fragment Analysis",
                "Capillary Electrophoresis- 4DYE"),
            "5dye": (
                "Fragment Analysis",
                "Capillary Electrophoresis- 5DYE")},
        "gce": {
            "a_samples":
                ("Geneticure- Agena Genotyping", "Make Dilution Plate"),
            "b_samples":
                ("Geneticure- Sample Storage", "Sample Storage B-swab")},
        "hvs": {
            "clean_pcr": (
                "HVS- High Volume Sequencing", "HVS PCR Clean Up"),
            "quant_norm": (
                "HVS- High Volume Sequencing", "HVS Fluorometric Quant"),
            "multi": (
                "HVS- High Volume Sequencing", "Sort HVS Submissions"),
            "default": (
                "HVS- High Volume Sequencing", "HVS Cycle Sequencing")},
        "lvs": ("LVS- Low Vol Seq", "LVS Sample Setup"),
        "nanostring": ("DNA Extraction Multi", "Sort Extraction Samples"),
        "quant": {
            "gdna": ("DNA Extraction Multi", "Sort Extraction Samples"),
            "post": ("DNA Extraction Multi", "DNA Extraction Robotic")},
        "ribotyping": ("DNA Extraction Multi", "Sort Extraction Samples"),
        "tgm": ("TGM Initiate Batch", "ProK and Cook Samples")
    },
    "prod": {
        "bioanalyzer": {
            "DNA": ("DNA Bioanalyzer Service", "Bioanalyzer Service DNA"),
            "RNA": (
                "RNA Bioanalyzer Service", "Bioanalyzer Service RNA")},
        "cla": {
            "cells": ("CLA Cell Line Auth.", "Sort Extraction Samples"),
            "gdna": ("CLA Cell Line Auth.", "Autosomal STR PP16")},
        "extraction": {
            "DNA": ("DNAExtraction", "Sort Extraction Samples"),
            "RNA": ("RNA Extraction", "Sort Extraction Samples RNA")},
        "frag": {
            "GS1200": ("FRAG- Fragment Analysis", "CE- 5DYE GS1200"),
            "4dye": ("FRAG- Fragment Analysis", "CE- 4DYE"),
            "5dye": ("FRAG- Fragment Analysis", "CE- 5DYE")},
        "gce": {
            "a_samples":
                (
                    "Geneticure- Mass Array Genotyping",
                    "Sort Extraction Samples"),
            "b_samples":
                ("Geneticure- Sample Storage", "Sample Storage B-swab")},
        "hvs": {
            "clean_pcr": (
                "HVS- High Volume Sequencing", "HVS PCR Clean Up"),
            "quant_norm": (
                "HVS- High Volume Sequencing", "HVS Fluorometric Quant"),
            "multi": (
                "HVS- High Volume Sequencing", "Sort HVS Submissions"),
            "default": (
                "HVS- High Volume Sequencing", "HVS Cycle Sequencing")},
        "lvs": ("LVS- Low Vol Seq", "LVS Sample Setup"),
        "nanostring": ("Nanostring", "Sort Extraction Samples RNA"),
        "quant": {
            "gdna": ("DNA quant_v2", "DNA QC gDNA Fluorometric"),
            "post": ("Post PCR Quant", "HVS Fluorometric Quant")},
        "ribotyping": ("DNAExtraction", "Sort Extraction Samples"),
        "tgm": ("TGM Initiate Batch", "ProK and Cook Samples")
    }
}
