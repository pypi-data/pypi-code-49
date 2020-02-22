from typing import Tuple
import numpy as np
from ucsc_genomes_downloader import Genome
from ucsc_genomes_downloader.utils import expand_bed_regions


def get_gaps_statistics(genome: Genome, max_gap_size: int, window_size: int) -> Tuple[int, np.ndarray, np.ndarray]:
    """Return number, mean and covariance of gaps.

    Parameters
    --------------------------
    genome:Genome,
        The genome to use.
    max_gap_size:int,
        The maximum gap size to take in consideration.
    window_size:int
        The target window size

    Returns
    --------------------------
    Returns Tuple containing number of gaps, mean and covariance.
    """
    # Obtaining gaps
    gaps = genome.gaps()
    # Getting gaps whose size is below given threshold
    gaps = gaps[gaps.chromEnd - gaps.chromStart < max_gap_size]
    # Expanding gaps to given window size
    gaps = expand_bed_regions(gaps, window_size, alignment="center")
    # Retrieving the sequences corresponding to given gaps
    sequences = genome.bed_to_sequence(gaps).sequence.str.lower()
    # Obtaining a mask of gaps
    gaps_mask = np.array([
        list(sequence)
        for sequence in sequences
    ]) == "n"
    number = len(gaps_mask)
    mean = gaps_mask.mean(axis=0)
    covariance = np.cov(gaps_mask.T)
    return number, mean, covariance
