#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import argparse
import pandas as pd
import numpy as np


parser = argparse.ArgumentParser(description="""Update allele frequencies in the HaploFreqs table given 
results of the latest HmtDB update. Requires a folder named freqs/ with allele frequencies files 
named in the format var_<continent>_[h|p].csv. New Variab table with updated allele frequencies will 
be saved as new_Variab.csv.""")
parser.add_argument("-m", "--main", dest="main_table", help="""Main table from HmtVar database.""")
parser.add_argument("-v", "--variab", dest="variab_table",
                    help="""Variab table from HmtVar database.""")

args = parser.parse_args()


def update_freqs(freqset: str, all_freq: str):
    """
    Update a specific allele frequency from the results of the latest HmtDB update.
    :param freqset: new allele frequency table from the allele_freqs.py HmtDB script
    :param all_freq: specific allele frequency column to update
    :return:
    """
    df = pd.read_csv(freqset)
    for el in main_df.itertuples():
        new_fr = 0.0

        # SNPs
        if el.alt in ["A", "C", "G", "T"]:
            new_fr = df[df["position"].startwith(f"{el.nt_start}.0")][el.alt].values[0]
        # Deletions
        if el.alt == "d":
            new_fr = df[df["position"].startswith(f"{el.nt_start}.0")]["gap"].values[0]
        # Insertions
        elif el.alt.startswith("."):
            ins_len = len(el.alt.split(".")[1])
            ins_freq = []
            for n in range(1, ins_len + 1):
                ins_pos = float("{}.{}".format(el.nt_start, n))
                ins_nt = el.alt[n]
                try:
                    ins_freq.append(df[df["position"].startswith(ins_pos)][ins_nt].values[0])
                except IndexError:
                    ins_freq.append(df[df["position"].startswith(el.nt_start)][ins_nt].values[0])
            new_fr = np.prod(ins_freq)
        # Ambiguous nucleotides
        else:
            new_fr = df[df["position"].startswith(f"{el.nt_start}.0")]["oth"].values[0]

        haplofreq_df.at[el.Index, all_freq] = new_fr


if __name__ == '__main__':
    # main_df = pd.read_sql("SELECT * FROM Main", "sqlite:///../../mitovar.db")
    main_df = pd.read_csv(args.main_table, na_values="<null>")
    main_df.set_index("id", inplace=True)
    # variab_df = pd.read_sql("SELECT * FROM Variab", "sqlite:///../../mitovar.db")
    haplofreq_df = pd.read_csv(args.variab_table, na_values="<null>")
    haplofreq_df.set_index("id", inplace=True)

    update_freqs("freqs/var_tot_h.csv", "all_freq_h")
    update_freqs("freqs/var_tot_p.csv", "all_freq_p")

    update_freqs("freqs/var_af_h.csv", "all_freq_h_AF")
    update_freqs("freqs/var_af_p.csv", "all_freq_p_AF")

    update_freqs("freqs/var_am_h.csv", "all_freq_h_AM")
    update_freqs("freqs/var_am_p.csv", "all_freq_p_AM")

    update_freqs("freqs/var_as_h.csv", "all_freq_h_AS")
    update_freqs("freqs/var_as_p.csv", "all_freq_p_AS")

    update_freqs("freqs/var_eu_h.csv", "all_freq_h_EU")
    update_freqs("freqs/var_eu_p.csv", "all_freq_p_EU")

    update_freqs("freqs/var_oc_h.csv", "all_freq_h_OC")

    haplofreq_df.reset_index(inplace=True)
    haplofreq_df.to_csv("HaploFreqs_new.csv", index=False, float_format="%.10f", na_rep="<null>")

