from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
import regex as re


def _doRow(row: pd.Series):
    X = row["predicted"]
    Y = row["input"]

    pattern = "[A-Za-z]+|[0-9]+"
    Yalpha = pd.Series(re.findall(pattern, Y))
    Ysepa = pd.Series(re.split(pattern, Y))
    Xalpha = pd.Series(re.findall(pattern, X))
    Xsepa = pd.Series(re.split(pattern, X))
    common, ixX, ixY = np.intersect1d(Xalpha, Yalpha, return_indices=True)
    ixX = pd.Series(ixX)
    ixY = pd.Series(ixY)

    YN = pd.Series(["D" if a.isdigit() else "L" for a in Yalpha])
    YN.loc[ixY] = "[" + YN.loc[ixY] + (1 + ixY.index).astype(str) + "]"
    YNN = [Ysepa[i] + YN[i] for i in range(len(YN))]

    XN = pd.Series(["D" if a.isdigit() else "L" for a in Xalpha])
    XN.loc[ixX] = "[" + XN.loc[ixX] + (1 + ixX.index).astype(str) + "]"
    XNN = [Xsepa[i] + XN[i] for i in range(len(XN))]

    PY = "".join(YNN)
    PX = "".join(XNN)
    return [PY, PX]


def _calcRules(M: pd.DataFrame):
    rule = []
    VAL_Y = M["PY"].value_counts()
    for vc in VAL_Y.index:
        Mred = M[M["PY"] == vc]
        VAL_X = Mred.PX.value_counts()
        for vx in VAL_X.index:
            Mrred = Mred[Mred.PX == vx]
            score = Mrred.score.mean()
            rule.append([vc, vx, VAL_X.loc[vx], score, Mrred.index])

    return pd.DataFrame(
        columns=["Y Pattern", "X Pattern", "num_matches", "avg_score", "match_ix"], data=rule
    ).sort_values(by="num_matches", ascending=False)


def calc_regex_rules(matches: pd.DataFrame):
    A = matches[["predicted", "input"]].apply(_doRow, axis=1, result_type="expand")
    A.columns = ["PY", "PX"]
    A["score"] = matches.score

    return _calcRules(A)


def _get_chunks_and_separators(string: str, pattern: str = "[A-Za-z]+|[0-9]+") -> Tuple[List[str], List[str]]:
    return re.findall(pattern, string), re.split(pattern, string)


def _make_chunks_into_pattern_list(chunks: List[str]) -> List[str]:
    return ["D" if a.isdigit() else "L" for a in chunks]


def _strip_encoded_pattern(string_pattern):
    return re.sub(r"[\[\]\d]", "", string_pattern)


def _get_string_pattern(string: str, pattern: str = "[A-Za-z]+|[0-9]+") -> str:
    """
    Based on the regex pattern for tokens, get the encoded string representing string pattern
    """
    chunks, separators = _get_chunks_and_separators(string, pattern)
    pattern_chunks = _make_chunks_into_pattern_list(chunks)
    return "".join(map(lambda x, y: x + y, separators, pattern_chunks))


def _get_matching_pattern_chunks(string: str, string_pattern: str, pattern: str = "[A-Za-z]+|[0-9]+") -> Optional[str]:
    """
    Based on the pattern for tokens and string_pattern, get the string
    representing tokens values from the matching part of the pattern.
    """
    if _get_string_pattern(string, pattern) != _strip_encoded_pattern(string_pattern):
        return None
    pattern_chunks = list(zip(re.findall(r"[L|D]\d*", string_pattern), re.findall(pattern, string)))
    keep_pattern_chunk = [pattern_chunk for pattern_chunk in pattern_chunks if re.match(r"[L|D]\d+", pattern_chunk[0])]
    keep_pattern_chunk.sort(key=lambda x: x[0])
    return str(keep_pattern_chunk)


def apply_rule(
    input_pattern: str, predict_pattern: str, input_list: List[str], predicted_list: List[str]
) -> pd.DataFrame:
    """
    Matches entries in `input_list` against entries in `predicted_list`. The entries in
    `input_list` and `predicted_list` are chunked according to `input_pattern` and
    `predict_pattern`, respectively, and entries with equal chunks are considered to match.

    Args:
        input_pattern (str): Pattern to which the entries in `input_list` are chunked.
        predict_pattern (str): Pattern to which the entries in `predicted_list` are chunked.
        input_list (List(str)): Entries to match from.
        predicted_list (List(str)): Entries to match to.

    Returns:
        (pandas.DataFrame): Data frame with one row per match.
    """

    df_input = pd.DataFrame(input_list)
    df_input.columns = ["input"]
    df_predicted = pd.DataFrame(predicted_list)
    df_predicted.columns = ["predicted"]

    matching_chunks_column = "matching_chunks"
    df_input[matching_chunks_column] = df_input["input"].apply(
        _get_matching_pattern_chunks, string_pattern=input_pattern
    )
    df_input = df_input.dropna()
    df_predicted[matching_chunks_column] = df_predicted["predicted"].apply(
        _get_matching_pattern_chunks, string_pattern=predict_pattern
    )
    df_predicted = df_predicted.dropna()

    df_matches = df_input.merge(df_predicted, on=matching_chunks_column)
    return df_matches[["input", "predicted", matching_chunks_column]]
