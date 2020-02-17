import scipy.io.wavfile
import scipy.signal
from bob.db.base import read_annotation_file
from bob.io.base import load
from bob.io.video import reader
from bob.bio.video.utils import FrameSelector
from bob.bio.video.database import VideoBioFile
import numpy as np
import subprocess
import tempfile
from os.path import split, splitext
from . import SWAN_FRAME_SHAPE
import logging

logger = logging.getLogger(__name__)

SITE_MAPPING = {"1": "NTNU", "2": "UIO", "3": "MPH-FRA", "4": "IDIAP", "6": "MPH-IND"}

DEVICE_MAPPING = {"p": "iPhone", "t": "iPad"}

MODALITY_MAPPING = {"1": "face", "2": "voice", "3": "eye", "4": "finger"}


def read_audio(video_path, new_rate=None):
    with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        cmd = ["ffmpeg", "-v", "quiet", "-i", video_path, "-y", "-vn", f.name]
        subprocess.call(cmd)
        f.seek(0)
        rate, signal = scipy.io.wavfile.read(f.name)
    if new_rate is not None and rate != new_rate:
        logger.debug("Resampling audio from %d to %d", rate, new_rate)
        samps = round(len(signal) * new_rate / rate)  # Number of samples to resample
        signal, rate = scipy.signal.resample(signal, samps), new_rate
    return rate, signal


class Client(object):
    """A base class for SWAN clients"""

    def __init__(self, site, id_in_site, gender, **kwargs):
        super(Client, self).__init__(**kwargs)
        self.institute = site
        self.id_in_site = id_in_site
        self.gender = gender

    @property
    def id(self):
        return "{}_{}".format(self.institute, self.id_in_site)


def swan_file_metadata(path):
    """Returns the metadata associated with a SWAN file recorded during the
    biometric recognition phase.

    Parameters
    ----------
    path : str
        The path of the SWAN file.

    Returns
    -------
    client : :any:`Client`
    session : str
    nrecording : str
    device : str
    modality : str
    """
    # For example:
    # path: IDIAP/session_01/iPad/00001/4_00001_m_01_01_t_2.mp4
    _, path = split(path)
    # path: 4_00001_m_01_01_t_2.mp4
    path, extension = splitext(path)
    parts = path.split("_")
    if len(parts) == 8:
        parts = parts[1:]
    # path: 4_00001_m_01_01_t_2
    site, identity, gender, session, nrecording, device, modality = parts
    site = SITE_MAPPING[site]
    client = Client(site, identity, gender)
    device = DEVICE_MAPPING[device]
    modality = MODALITY_MAPPING[modality]
    session = int(session)
    return client, session, nrecording, device, modality


class SwanFile(object):
    """A base class for SWAN bio files which can handle the metadata."""

    def __init__(self, **kwargs):
        super(SwanFile, self).__init__(**kwargs)
        (
            self.client,
            self.session,
            self.nrecording,
            self.device,
            self.modality,
        ) = swan_file_metadata(self.path)


class SwanVideoFile(VideoBioFile, SwanFile):
    """A base class for SWAN video files"""

    def swap(self, data):
        # rotate the video or image since SWAN videos are not upright!
        return np.swapaxes(data, -2, -1)

    def load(
        self,
        directory=None,
        extension=None,
        frame_selector=FrameSelector(selection_style="all"),
    ):
        if extension is None:
            video_path = self.make_path(directory or self.original_directory, extension)
            for _ in range(100):
                try:
                    video = load(video_path)
                    break
                except RuntimeError:
                    pass
            video = self.swap(video)
            return frame_selector(video)
        else:
            return super(SwanVideoFile, self).load(directory, extension, frame_selector)

    @property
    def frames(self):
        """Yields the frames of the padfile one by one.

        Parameters
        ----------
        padfile : :any:`SwanVideoFile`
            The high-level pad file

        Yields
        ------
        :any:`numpy.array`
            A frame of the video. The size is (3, 1280, 720).
        """
        vfilename = self.make_path(directory=self.original_directory)
        video = reader(vfilename)
        for frame in video:
            yield self.swap(frame)

    @property
    def number_of_frames(self):
        """Returns the number of frames in a video file.

        Parameters
        ----------
        padfile : :any:`SwanVideoFile`
            The high-level pad file

        Returns
        -------
        int
            The number of frames.
        """
        vfilename = self.make_path(directory=self.original_directory)
        return reader(vfilename).number_of_frames

    @property
    def frame_shape(self):
        """Returns the size of each frame in this database.

        Returns
        -------
        (int, int, int)
            The (#Channels, Height, Width) which is (3, 1920, 1080).
        """
        return SWAN_FRAME_SHAPE

    @property
    def annotations(self):
        """Returns the annotations of the current file

        Returns
        -------
        dict
            The annotations as a dictionary, e.g.:
            ``{'0': {'reye':(re_y,re_x), 'leye':(le_y,le_x)}, ...}``
        """
        return read_annotation_file(
            self.make_path(self.annotation_directory, self.annotation_extension),
            self.annotation_type,
        )


class SwanAudioFile(SwanVideoFile):
    """A base class that extracts audio from SWAN video files"""

    def __init__(self, new_rate=None, **kwargs):
        super().__init__(**kwargs)
        self.new_rate = new_rate

    def load(self, directory=None, extension=None):
        if extension is None:
            video_path = self.make_path(directory, extension)
            rate, audio = read_audio(video_path, new_rate=self.new_rate)
            return rate, np.cast["float"](audio)
        else:
            return super(SwanAudioFile, self).load(directory, extension)


class SwanVideoDatabase(object):
    """SwanVideoDatabase"""

    def __init__(self, new_rate=None, **kwargs):
        super().__init__(**kwargs)
        self.new_rate = new_rate

    def frames(self, padfile):
        return padfile.frames

    def number_of_frames(self, padfile):
        return padfile.number_of_frames

    @property
    def frame_shape(self):
        return SWAN_FRAME_SHAPE

    def update_files(self, files):
        for f in files:
            f.original_directory = self.original_directory
            f.annotation_directory = self.annotation_directory
            f.annotation_extension = self.annotation_extension
            f.annotation_type = self.annotation_type
            f.new_rate = self.new_rate
        return files
