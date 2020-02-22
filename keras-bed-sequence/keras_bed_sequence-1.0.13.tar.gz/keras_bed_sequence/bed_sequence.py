"""Keras Sequence to lazily one-hot encode sequences from a given bed file."""
from typing import Dict, Tuple, Union
from tensorflow.keras.utils import Sequence, to_categorical
import pandas as pd
import numpy as np
from ucsc_genomes_downloader import Genome
from keras_mixed_sequence.utils import sequence_length, batch_slice
from .utils import nucleotides_to_numbers


class BedSequence(Sequence):
    """Keras Sequence to lazily one-hot encode sequences from a given bed file.

    Usage examples
    ------------------------
    The following examples are tested within the package test suite.

    Classification task example
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Let's start by building an extremely simple classification task model:

    .. code:: python

        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense, Flatten
        from keras_mixed_sequence import MixedSequence

        model = Sequential([
            Flatten(),
            Dense(1)
        ])
        model.compile(
            optimizer="nadam",
            loss="MSE"
        )

    We then proceed to load the training data into Keras Sequences,
    using in particular a MixedSequence object:

    .. code:: python

        import numpy as np
        from keras_mixed_sequence import MixedSequence
        from keras_bed_sequence import BedSequence

        batch_size = 32
        bed_sequence = BedSequence(
            "hg19",
            "path/to/bed/files.bed",
            batch_size
        )
        y = the_output_values
        mixed_sequence = MixedSequence(
            x=bed_sequence,
            y=y,
            batch_size=batch_size
        )

    Finally we can proceed to use the obtained MixedSequence
    to train our model:

    .. code:: python

        model.fit_generator(
            mixed_sequence,
            steps_per_epoch=mixed_sequence.steps_per_epoch,
            epochs=2,
            verbose=0,
            shuffle=True
        )

    Auto-encoding task example
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Let's start by building an extremely simple auto-encoding task model:

    .. code:: python

        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Conv2D, Reshape, Conv2DTranspose

        model = Sequential([
            Reshape((200, 4, 1)),
            Conv2D(16, kernel_size=3, activation="relu"),
            Conv2DTranspose(1, kernel_size=3, activation="relu"),
            Reshape((-1, 200, 4))
        ])
        model.compile(
            optimizer="nadam",
            loss="MSE"
        )

    We then proceed to load the training data into Keras Sequences,
    using in particular a MixedSequence object:

    .. code:: python

        import numpy as np
        from keras_mixed_sequence import MixedSequence
        from keras_bed_sequence import BedSequence

        batch_size = 32
        bed_sequence = BedSequence(
            "hg19",
            "path/to/bed/files.bed",
            batch_size
        )
        mixed_sequence = MixedSequence(
            x=bed_sequence,
            y=bed_sequence,
            batch_size=batch_size
        )

    Finally we can proceed to use the obtained MixedSequence
    to train our model:

    .. code:: python

        model.fit_generator(
            mixed_sequence,
            steps_per_epoch=mixed_sequence.steps_per_epoch,
            epochs=2,
            verbose=0,
            shuffle=True
        )

    Multi-task example (classification + auto-encoding)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Let's start by building an extremely simple multi-tasks model:

    .. code:: python

        from tensorflow.keras.models import Model
        from tensorflow.keras.layers import Dense, Conv2D, Reshape, Flatten, Conv2DTranspose, Input

        inputs = Input(shape=(200, 4))

        flattened = Flatten()(inputs)

        output1 = Dense(
            units=1,
            activation="relu",
            name="output1"
        )(flattened)

        hidden = Reshape((200, 4, 1))(inputs)
        hidden = Conv2D(16, kernel_size=3, activation="relu")(hidden)
        hidden = Conv2DTranspose(1, kernel_size=3, activation="relu")(hidden)
        output2 = Reshape((200, 4), name="output2")(hidden)

        model = Model(
            inputs=inputs,
            outputs=[output1, output2],
            name="my_model"
        )

        model.compile(
            optimizer="nadam",
            loss="MSE"
        )

    We then proceed to load the training data into Keras Sequences,
    using in particular a MixedSequence object:

    .. code:: python

        import numpy as np
        from keras_mixed_sequence import MixedSequence
        from keras_bed_sequence import BedSequence

        batch_size = 32
        bed_sequence = BedSequence(
            "hg19",
            "{cwd}/test.bed".format(
                cwd=os.path.dirname(os.path.abspath(__file__))
            ),
            batch_size
        )
        y = np.random.randint(
            2,
            size=(bed_sequence.samples_number, 1)
        )
        mixed_sequence = MixedSequence(
            bed_sequence,
            {
                "output1": y,
                "output2": bed_sequence
            },
            batch_size
        )

    Finally we can proceed to use the obtained MixedSequence
    to train our model:

    .. code:: python

        model.fit_generator(
            mixed_sequence,
            steps_per_epoch=mixed_sequence.steps_per_epoch,
            epochs=2,
            verbose=0,
            shuffle=True
        )

    """

    def __init__(
        self,
        assembly: Union[str, Genome],
        bed: Union[pd.DataFrame, str],
        batch_size: int = 32,
        verbose: bool = True,
        nucleotides: str = "actg",
        seed: int = 42,
        elapsed_epochs: int = 0,
        genome_kwargs: Dict = None
    ):
        """Return new BedSequence object.

        Parameters
        --------------------
        assembly: Union[str, Genome],
            Genomic assembly from ucsc from which to extract sequences.
            For instance, "hg19", "hg38" or "mm10".
        bed: Union[pd.DataFrame, str],
            Either path to file or Pandas DataFrame containing minimal bed columns,
            like "chrom", "chromStart" and "chromEnd".
        batch_size: int = 32,
            Batch size to be returned for each request.
            By default is 32.
        verbose: bool = True,
            Whetever to show a loading bar.
        nucleotides: str = "actg",
            Nucleotides to consider when one-hot encoding.
        seed: int = 42,
            Starting seed to use if shuffling the dataset.
        elapsed_epochs: int = 0,
            Number of elapsed epochs to init state of generator.
        genome_kwargs: Dict = None,
            Parameters to pass to the Genome object.

        Raises
        --------------------
        ValueError:
            If the bed file regions does not have the same length.

        Returns
        --------------------
        Return new BedSequence object.
        """
        # If the given bed file is provided
        # we load the file using pandas.
        if isinstance(bed, str):
            bed = pd.read_csv(bed, sep="\t")

        # Every window in the bed file must be
        # of the same length.
        if len(set((bed.chromEnd - bed.chromStart).values)) != 1:
            raise ValueError(
                "The bed file regions must have the same length!"
            )

        self._window_length = (bed.chromEnd - bed.chromStart).values[0]

        # We retrieve the required chromosomes
        # from the required assembly.
        if isinstance(assembly, Genome):
            self._genome = assembly
        else:
            self._genome = Genome(
                assembly=assembly,
                chromosomes=bed.chrom.unique(),
                verbose=verbose,
                **({} if genome_kwargs is None else genome_kwargs)
            )

        self._batch_size = batch_size
        self._seed, self._elapsed_epochs = seed, elapsed_epochs

        # We extract the sequences of the bed file from
        # the given genome.
        sequences = self._genome.bed_to_sequence(bed).sequence

        # We encode the nucleotide sequences
        # as small integers
        self._x = nucleotides_to_numbers(
            nucleotides,
            sequences,
            verbose=verbose
        )

        self._nucleotides_number = len(nucleotides)

    def on_epoch_end(self):
        """Shuffle private bed object on every epoch end."""
        state = np.random.RandomState(seed=self._seed + self._elapsed_epochs)
        self._elapsed_epochs += 1
        state.shuffle(self._x)

    def __len__(self) -> int:
        """Return length of bed generator."""
        return sequence_length(self._x, self._batch_size)

    @property
    def steps_per_epoch(self) -> int:
        """Return length of bed generator."""
        return len(self)

    @property
    def window_length(self) -> int:
        """Return number of nucleotides in a window."""
        return self._window_length

    @property
    def nucleotides_number(self) -> int:
        """Return number of nucleotides considered."""
        return self._nucleotides_number

    @property
    def batch_size(self) -> int:
        """Return batch size to be rendered."""
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size: int):
        """Set batch size to given value."""
        self._batch_size = batch_size

    @property
    def samples_number(self) -> int:
        """Return number of available samples."""
        return len(self._x)

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
        return to_categorical(
            self._x[batch_slice(idx, self.batch_size)],
            num_classes=self.nucleotides_number
        )
