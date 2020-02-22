from typing import Dict
import math
from multiprocessing import Pool, cpu_count
from tqdm.auto import tqdm
import pandas as pd
import numpy as np


def _nucleotides_to_numbers(nucleotides: str, sequences: pd.Series) -> np.ndarray:
    """Return sequences encoded as small integers.

    Parameters
    --------------------------
    nucleotides: str,
        Nucleotides to take in consideration when encoding,
        for instance "acgt".
    sequences: pd.Series,
        Pandas series with the nucleotide sequences.

    Returns
    --------------------------
    Returns numpy ndarray containing the encoded nucleotides.
    """
    return np.array([
        [
            nucleotides.find(nucleotide)
            for nucleotide in sequence.lower()
        ] for sequence in sequences
    ], dtype=np.int8)


def _nucleotides_to_numbers_wrapper(task: Dict) -> np.ndarray:
    return _nucleotides_to_numbers(**task)


def nucleotides_to_numbers(nucleotides: str, sequences: pd.Series, verbose: bool) -> np.ndarray:
    """Return sequences encoded as small integers.

    Parameters
    --------------------------
    nucleotides: str,
        Nucleotides to take in consideration when encoding,
        for instance "acgt".
    sequences: pd.Series,
        Pandas series with the nucleotide sequences.
    verbose: bool,
        Whetever to show the loading bar while processing.

    Returns
    --------------------------
    Returns numpy ndarray containing the encoded nucleotides.
    """
    total = math.ceil(len(sequences)/10000)
    tasks = (
        {
            "nucleotides": nucleotides,
            "sequences": sequences[10000*i:10000*(i+1)]
        }
        for i in range(total)
    )
    with Pool(min(cpu_count(), total)) as p:
        encoded = np.vstack(list(tqdm(
            p.imap(
                _nucleotides_to_numbers_wrapper,
                tasks
            ),
            desc="Converting nucleotides to numeric classes",
            disable=not verbose,
            dynamic_ncols=True,
            leave=False,
            total=total
        )))
        p.close()
        p.join()
    return encoded
