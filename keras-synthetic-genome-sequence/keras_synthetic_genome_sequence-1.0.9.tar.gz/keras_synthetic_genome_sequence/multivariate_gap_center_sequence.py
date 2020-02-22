"""Keras Sequence that returns tuples of nucleotide sequences, one with multivariate synthetic gaps and the other without as ground truth."""
from typing import Union, Dict, Tuple
import pandas as pd
import numpy as np
from .multivariate_gap_sequence import MultivariateGapSequence
from .utils import generate_synthetic_gaps


class MultivariateGapCenterSequence(MultivariateGapSequence):
    """
    Keras Sequence that returns tuples of nucleotide sequences,
    one with multivariate synthetic gaps and the other with the
    values of the chromosome in the middle.
    """

    def __getitem__(self, idx: int) -> Tuple[np.ndarray, np.ndarray]:
        """Return batch corresponding to given index.

        Parameters
        ---------------
        idx: int,
            Index corresponding to batch to be rendered.

        Returns
        ---------------
        Return Tuple containing X and Y numpy arrays corresponding to given batch index.
        """
        # Retrieves the sequence from the bed generator
        x = super().__getitem__(idx)
        # Save the original chromosomes
        y = x[:, self.window_length//2].copy()
        # Retrieve the indices corresponding to the gaps for the current batchsize
        indices = self._gaps_index[idx]
        # Extract the gaps curresponding to given indices
        masks = self._gaps_coordinates[
            np.in1d(self._gaps_coordinates[:, 0], indices)
        ]
        # For every j-th index curresponding to the i-th row of current batch
        for i, index in enumerate(indices):
            # We extract the mask curresponding to the gaps
            # for the i-th row of current batch
            gap_indices = masks[masks[:, 0] == index][:, 1]
            # And we set the one-hot encoded nucleotides as
            # a uniform distribution.
            x[i, gap_indices, :] = 0.25
        # We return the tuple of the batch, containing
        # the input with added artificial gaps represented
        # as a uniform distribution and
        # the output containing the original one-hot encoded
        # sequence of nucleotides.
        return x, y
