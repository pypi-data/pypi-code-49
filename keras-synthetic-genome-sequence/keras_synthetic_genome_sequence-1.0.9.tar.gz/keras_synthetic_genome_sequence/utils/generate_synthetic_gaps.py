from multiprocessing import Pool, cpu_count
from typing import Dict
import math
from tqdm.auto import tqdm
import numpy as np


def _generate_synthetic_gaps(
    mean: np.ndarray,
    covariance: np.ndarray,
    size: int,
    offset: int,
    threshold: int,
    seed: int
) -> np.ndarray:
    """Return numpy array with the coordinates of gaps in matrix mask.

    Parameters
    ------------------
    mean: np.ndarray,
        Mean of biological gaps in considered windows.
    covariance: np.ndarray,
        Covariance of biological gaps in considered windows.
    size: int,
        Total number of rows to generate.
    chunk_size: int,
        Size of the chunk to process per sub-process step.
    threshold: int,
        Threshold used to convert the multivariate gaussian
        distribution to a multivariate binomial.
    seed: int,
        The seed to use to render the gaps.

    Returns
    ------------------
    Return numpy array with shape (size, 2) containing
    the coordinates of the gaps in the generated matrix mask.
    """
    state = np.random.RandomState(seed=seed)
    rows, columns = np.where(state.multivariate_normal(
        mean=mean,
        cov=covariance,
        size=size
    ) > threshold)
    rows += offset
    return np.array((rows, columns)).T


def _generate_synthetic_gaps_wrapper(task: Dict):
    return _generate_synthetic_gaps(**task)


def generate_synthetic_gaps(
    mean: np.ndarray,
    covariance: np.ndarray,
    size: int,
    chunk_size: int,
    threshold: int,
    seed: int
) -> np.ndarray:
    """Return numpy array with the coordinates of gaps in matrix mask.

    Parameters
    ------------------
    mean: np.ndarray,
        Mean of biological gaps in considered windows.
    covariance: np.ndarray,
        Covariance of biological gaps in considered windows.
    size: int,
        Total number of rows to generate.
    chunk_size: int,
        Size of the chunk to process per sub-process step.
    threshold: int,
        Threshold used to convert the multivariate gaussian
        distribution to a multivariate binomial.
    seed: int,
        The initial seed to use to render the gaps.

    Returns
    ------------------
    Return numpy array with shape(size, 2) containing
    the coordinates of the gaps in the generated matrix mask.
    """
    tasks = [
        {
            "mean": mean,
            "covariance": covariance,
            "size": min(chunk_size, size-chunk_size*i),
            "offset": chunk_size*i,
            "threshold": threshold,
            "seed": i+seed
        }
        for i in range(math.ceil(size/chunk_size))
    ]
    with Pool(cpu_count()) as p:
        indices = np.vstack(list(tqdm(
            p.imap(_generate_synthetic_gaps_wrapper, tasks),
            total=len(tasks),
            desc="Generating synthetic gaps",
            leave=False,
            dynamic_ncols=True
        )))
        p.close()
        p.join()
    return indices
