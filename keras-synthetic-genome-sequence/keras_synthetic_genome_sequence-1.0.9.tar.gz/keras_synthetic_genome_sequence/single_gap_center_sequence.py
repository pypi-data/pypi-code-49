"""Keras Sequence that returns tuples of nucleotide sequences, one with a synthetic gap in the middle and the other containing the corresponding value."""
from typing import Union, Dict, Tuple
import pandas as pd
import numpy as np
from keras_bed_sequence import BedSequence
from keras_mixed_sequence.utils import NumpySequence
from .utils import generate_synthetic_gaps


class SingleGapCenterSequence(BedSequence):
    """
    Keras Sequence that returns tuples of nucleotide sequences,
    one with a single nucleotide gap in the middle
    and the other containing the corresponding value.
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
        y = x[:, self.window_length//2].copy()
        x[:, self.window_length//2, :] = 0.25
        return x, y
