import numpy as np
import re
from importlib.resources import open_binary
from crisprbact.utils import rev_comp
from crisprbact.off_target import (
    compute_off_target_df,
    extract_records,
    extract_features,
)

with open_binary("crisprbact", "reg_coef.pkl") as handle:
    coef = np.load(handle, allow_pickle=True)

bases = ["A", "T", "G", "C"]


def encode(seq):
    """One-hot encoding of a sequence (only non-ambiguous bases (ATGC) accepted)"""

    return np.array([[int(b == p) for b in seq] for p in bases])


# Quartiles: q1 > 0.4 > q2 > -0.08 > q3 > -0.59 > q4
def predict(X):
    return [np.sum(x * coef) for x in X]


def find_targets(seq):
    repam = "[ATGC]GG"
    L = len(seq)
    seq_revcomp = rev_comp(seq)
    matching_target = re.finditer("(?=([ATGC]{6}" + repam + "[ATGC]{16}))", seq_revcomp)
    for target in matching_target:
        yield dict(
            [
                ("target", target.group(1)),
                ("guide", target.group(1)[:20]),
                ("start", L - target.start() - 20),
                ("stop", L - target.start()),
                ("pam", L - target.start() - 22),
                ("ori", "-"),
            ]
        )


def get_strand_value(value):
    strand_dict = {"+": 1, "1": 1, "-": -1, "-1": -1}
    return strand_dict[str(value)]


def on_target_predict(seq, genome=None, seed_sizes=[8, 9, 10, 11, 12]):

    seq = seq.upper()  # make uppercase
    seq = re.sub(r"\s", "", seq)  # removes white space
    records = None
    genome_features = None
    if genome:
        records = extract_records(genome)
        genome_features = extract_features(records)

    alltargets = list(find_targets(seq))
    if alltargets:
        X = np.array(
            [
                encode(target["target"][:7] + target["target"][9:])
                for target in alltargets
            ]  # encode and remove GG of PAM
        )
        X = X.reshape(X.shape[0], -1)
        preds = predict(X)

        for i, target in enumerate(alltargets):
            target_id = i + 1
            target.update({"target_id": target_id})
            target.update({"pred": preds[i]})
            if genome:
                off_targets_per_seed = []
                for seed_size in seed_sizes:
                    # off-target found for a guide
                    off_target_df = compute_off_target_df(
                        target["guide"], seed_size, records, genome_features
                    )
                    off_targets_list = []
                    if not off_target_df.empty:
                        off_targets = off_target_df.loc[
                            0:,
                            ["start", "end", "pampos", "strand", "recid", "features"],
                        ]
                        for j, off_t in enumerate(off_targets.values.tolist()):
                            off_target_dict = {
                                "off_target_id": str(target_id)
                                + "-"
                                + str(seed_size)
                                + "-"
                                + str(j),
                                "off_target_start": off_t[0],
                                "off_target_end": off_t[1],
                                "off_target_pampos": off_t[2],
                                "off_target_strand": off_t[3],
                                "off_target_recid": off_t[4],
                            }
                            # Filter the off targets if the strand
                            # is not the opposite of the feature
                            off_t[5] = list(
                                filter(
                                    lambda feat: get_strand_value(
                                        off_target_dict["off_target_strand"]
                                    )
                                    != get_strand_value(feat.location.strand),
                                    off_t[5],
                                )
                            )
                            # Loop through features associated to an off-target position
                            if len(off_t[5]) > 0:
                                # Loop for each feature
                                for feat in off_t[5]:
                                    feature_dict = {
                                        "off_target_feat_strand": feat.location.strand,
                                        "off_target_feat_start": feat.location.start,
                                        "off_target_feat_end": feat.location.end,
                                        "off_target_feat_type": feat.type,
                                    }
                                    for k, feat in feat.qualifiers.items():
                                        if k != "translation":
                                            feature_dict["off_target_" + k] = "::".join(
                                                feat
                                            )
                                    off_targets_list.append(
                                        {**feature_dict, **off_target_dict}
                                    )
                            else:
                                off_targets_list.append(off_target_dict)
                        off_targets_per_seed.append(
                            {
                                "id": str(i) + "-" + str(seed_size),
                                "seed_size": seed_size,
                                "off_targets": off_targets_list,
                            }
                        )
                    else:
                        off_targets_per_seed.append(
                            {
                                "id": str(i) + "-" + str(seed_size),
                                "seed_size": seed_size,
                                "off_targets": [],
                            }
                        )
                        # target.update({"off_targets": off_targets_list})
                target.update({"off_targets_per_seed": off_targets_per_seed})
            else:
                target.update({"off_targets_per_seed": []})
        return alltargets
    else:
        return []
