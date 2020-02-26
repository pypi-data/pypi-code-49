import re
import pandas as pd

from crisprbact.utils import rev_comp


def get_pos_features(position, f_df):
    if len(f_df) > 0:
        feature_at_pos = f_df[(f_df.start < position) & (f_df.end > position)]
        return feature_at_pos.feature.values
    else:
        return []


def get_off_target_pos(guide, recs, records):
    for rec in recs:
        # + ori
        offs_plus = re.finditer(guide[-records:] + "[ATGC]GG", str(rec.seq))
        offs = [match.span() + (match.end(), "+", rec.id) for match in offs_plus]
        # - ori
        offs_minus = re.finditer("CC[ATGC]" + rev_comp(guide[-records:]), str(rec.seq))
        offs += [match.span() + (match.start(), "-", rec.id) for match in offs_minus]
        offs_dict = dict(zip(["start", "end", "pampos", "strand", "recid"], zip(*offs)))
        return pd.DataFrame(offs_dict)


def extract_records(genome):
    records = list(genome)
    if records and len(records) > 0:
        return records
    else:
        return None


def extract_features(recs):
    f_list = []
    for rec in recs:
        for f in rec.features:
            if f.type in ["CDS", "ncRNA", "rRNA", "tRNA"]:
                f_list.append(
                    (
                        f.location.start.position,
                        f.location.end.position,
                        f.location.strand,
                        f.type,
                        f,
                        rec.id,
                    )
                )
    f_dict = dict(
        zip(["start", "end", "strand", "type", "feature", "recid"], zip(*f_list[1:]),)
    )  # starts at 1 to get rid of the first feature which is the whole chromosome
    return pd.DataFrame(f_dict)


def compute_off_target_df(guide, seed_size, records, feature_df):
    """ Returns a pandas DataFrame with data about the identified off-targets.
    The features column contains a list of biopython SeqFeature objects that overlap
    with the off-target"""
    offs_df = get_off_target_pos(guide, records, seed_size)
    offs_df["features"] = [
        get_pos_features(off.pampos, feature_df) for i, off in offs_df.iterrows()
    ]
    return offs_df
