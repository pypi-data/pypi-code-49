from tensorflow.keras.callbacks import Callback
import os
import random
from typing import List
from environments_utils import is_notebook
from .utils import InvisibleAudio
import simpleaudio

__all__ = ["Ding"]


class Ding(Callback):

    available_samples = ("bojack", "pink_guy", "rick", "ding", "whale")

    def __init__(self, sample: str = "ding", path: str = None):
        r"""Create a new Ding callback.

        Ding simply plays the sound at given path when the training is complete.

        Parameters
        ------------------------------------------
        
        sample:str,
            Name of one of the available samples.
            Currently available are 'bojack', 'pink_guy', 'rick', 'whale' and 'ding'.
            Use 'random' for choosing a random sample.
        path:str,
            the path to the file to play.
            If None, as by default, the value specified under sample will be used.

        Raises
        ----------------------
        ValueError
            If the given sample does not exist.
        ValueError
            If the given path does not correspond to a playable object.

        Returns
        ----------------------
        Return a new Ding object.
        """
        super(Ding, self).__init__()
        if path is None:
            if sample == "random":
                sample = random.choice(Ding.available_samples)
            if sample not in Ding.available_samples:
                raise ValueError("Given sample '{}' does not exists.".format(sample))
            path = os.sep.join([
                os.path.dirname(os.path.abspath(__file__)),
                "samples",
                "{}.wav".format(sample)
            ])
        if not os.path.exists(path):
            raise ValueError("Given path '{}' does not exists.".format(path))

        if not any([path.endswith(ext) for ext in ["mp3", "wav"]]):
            raise ValueError("Given path is not an mp3 or wav file.")

        self._path = path

    def on_train_end(self, *args: List):
        """Plays the sound at the end of training."""
        if is_notebook():
            InvisibleAudio(path=self._path).play()
        else:
            simpleaudio.WaveObject.from_wave_file(self._path).play()
