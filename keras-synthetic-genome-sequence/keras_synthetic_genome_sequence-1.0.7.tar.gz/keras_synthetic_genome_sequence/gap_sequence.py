"""Keras Sequence that returns tuples of nucleotide sequences, one with synthetic gaps and the other without as ground truth."""
from typing import Union, Dict, Tuple
import pandas as pd
import numpy as np
from keras_bed_sequence import BedSequence
from keras_mixed_sequence.utils import NumpySequence
from .utils import generate_synthetic_gaps


class GapSequence(BedSequence):
    """
    Keras Sequence that returns tuples of nucleotide sequences,
    one with synthetic gaps and the other without as ground truth.

    Usage examples
    -------------------------
    To use GapSequence to train your keras model you
    will need to obtain statistical metrics for the
    biological gaps you intend to mimic in your synthetic gaps.

    To achieve this, this package offers an utility called
    get_gaps_statistics, which allows you to obtain the
    mean and covariance of gaps in a given genomic assembly.

    The genomic assembly is automatically downloaded from UCSC
    using `ucsc_genomes_downloader <https://github.com/LucaCappelletti94/ucsc_genomes_downloader>`__,
    then the gaps contained within are extracted and their windows
    is expanded to the given one, after filtering for the given
    max_gap_size, as you might want to limit the gaps size to
    a relatively small one (gaps can get in the tens of thousands
    of nucleotides, for instance in the telomeres).

    Let's start by listing all the important parameters:

    .. code:: python

        assembly = "hg19"
        window_size = 200
        batch_size = 128

    Now we can start by retrieving the gaps statistics:

    .. code:: python

        from keras_synthetic_genome_sequence.utils import get_gaps_statistics

        number, mean, covariance = get_gaps_statistics(
            assembly=assembly,
            max_gap_size=100,
            window_size=window_size
        )

        print("I have identified {number} gaps!".format(number=number))

    Now you must choose the ground truth on which to apply the
    synthetic gaps, for instance the regions without gaps in
    the genomic assembly hg19, chromosome chr1.
    These regions will have to be tasselized into smaller
    chunks that are compatible with the shape you have chosen for
    the gap statistics window_size.
    We can retrieve these regions as follows:

    .. code:: python

        from ucsc_genomes_downloader import Genome
        from ucsc_genomes_downloader.utils import tessellate_bed

        hg19 = Genome(assembly, chromosomes=["chr1"])
        ground_truth = tessellate_bed(genome.filled(), window_size=window_size)

    The obtained pandas DataFrame will have a bed-like format
    and look as follows:

    +----+---------+--------------+------------+
    |    | chrom   |   chromStart |   chromEnd |
    +====+=========+==============+============+
    |  0 | chr1    |        10000 |      10200 |
    +----+---------+--------------+------------+
    |  1 | chr1    |        10200 |      10400 |
    +----+---------+--------------+------------+
    |  2 | chr1    |        10400 |      10600 |
    +----+---------+--------------+------------+
    |  3 | chr1    |        10600 |      10800 |
    +----+---------+--------------+------------+
    |  4 | chr1    |        10800 |      11000 |
    +----+---------+--------------+------------+

    Now we are ready to actually create the GapSequence:

    .. code:: python

        from keras_synthetic_genome_sequence import GapSequence

        gap_sequence = GapSequence(
            assembly=assembly,
            ground_truth,
            gaps_mean=mean,
            gaps_covariance=covariance,
            batch_size=batch_size
        )

    Now, having a model that receives as
    input and output shape (batch_size, window_size, 4),
    we can train it as follows:

    .. code:: python

        model = build_my_denoiser()
        model.fit_generator(
            gap_sequence,
            steps_per_epoch=gap_sequence.steps_per_epoch,
            epochs=2,
            shuffle=True
        )

    Happy denoising!

    """

    def __init__(
        self,
        assembly: str,
        bed: Union[pd.DataFrame, str],
        gaps_mean: np.ndarray,
        gaps_covariance: np.ndarray,
        gaps_threshold: float = 0.4,
        batch_size: int = 32,
        verbose: bool = True,
        seed: int = 42,
        elapsed_epochs: int = 0,
        genome_kwargs: Dict = None
    ):
        """Return new GapSequence object.

        Parameters
        ----------------------------
        assembly: str,
            Genomic assembly from ucsc from which to extract sequences.
            For instance, "hg19", "hg38" or "mm10".
        bed: Union[pd.DataFrame, str],
            Either path to file or Pandas DataFrame containing minimal bed columns,
            like "chrom", "chromStart" and "chromEnd".
        gaps_mean: np.ndarray,
            Mean of the multivariate Gaussian distribution to use for generating
            the gaps in the sequences. Length of the sequences must match with
            length of the mean vector.
        gaps_covariance: np.ndarray,
            Covariance matrix of the multivariate Gaussian distribution to use
            for generating the gaps in the sequences.
            Length of the sequences must match with length of the mean vector.
        gaps_threshold: float,
            Threshold for casting the multivariate Gaussian distribution to
            a binomial multivariate distribution.
        batch_size: int = 32,
            Batch size to be returned for each request.
            By default is 32.
        verbose: bool = True,
            Whetever to show a loading bar.
        seed: int = 42,
            Starting seed to use if shuffling the dataset.
        elapsed_epochs: int = 0,
            Number of elapsed epochs to init state of generator.
        genome_kwargs: Dict = None,
            Parameters to pass to the Genome object.

        Returns
        --------------------
        Return new GapSequence object.
        """
        super().__init__(
            assembly=assembly,
            bed=bed,
            batch_size=batch_size,
            verbose=verbose,
            seed=seed,
            elapsed_epochs=elapsed_epochs,
            genome_kwargs=genome_kwargs,
        )
        if len(gaps_mean) != self.window_length:
            raise ValueError(
                "Mean len({mean_len}) does not match bed file window len({window_len}).".format(
                    mean_len=len(gaps_mean),
                    window_len=self.window_length,
                )
            )
        if len(gaps_covariance) != self.window_length:
            raise ValueError(
                "Covariance len({covariance_len}) does not match bed file window len({window_len}).".format(
                    covariance_len=len(gaps_covariance),
                    window_len=self.window_length,
                )
            )
        # Rendering the gaps coordinates
        self._gaps_coordinates = generate_synthetic_gaps(
            gaps_mean,
            gaps_covariance,
            self.samples_number,
            chunk_size=50000,
            threshold=gaps_threshold,
            seed=seed
        )
        # Rendering the starting gaps index, which
        # will be shuffled alongside the bed file.
        self._gaps_index = NumpySequence(
            np.arange(self.samples_number),
            batch_size=batch_size,
            seed=seed,
            elapsed_epochs=elapsed_epochs
        )

    def on_epoch_end(self):
        """Shuffle private bed object on every epoch end."""
        super().on_epoch_end()
        self._gaps_index.on_epoch_end()

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
        y = super().__getitem__(idx)
        # Retrieve the indices corresponding to the gaps for the current batchsize
        indices = self._gaps_index[idx]
        # Extract the gaps curresponding to given indices
        masks = self._gaps_coordinates[
            np.in1d(self._gaps_coordinates[:, 0], indices)
        ]
        # Making a deep copy of y, since we are going to edit the copy.
        x = np.copy(y)
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
