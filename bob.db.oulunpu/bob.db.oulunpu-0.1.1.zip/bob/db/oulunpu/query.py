from pkg_resources import resource_filename
from bob.pad.base.database import FileListPadDatabase
from bob.pad.face.database import VideoPadFile
from bob.bio.video import FrameSelector
from bob.extension import rc
from bob.io.video import reader
from bob.db.base.annotations import read_annotation_file
from . import OULUNPU_FRAME_SHAPE


class File(VideoPadFile):
    """The file objects of the OULU-NPU dataset."""

    @property
    def frames(self):
        """Yields the frames of the biofile one by one.

        Yields
        ------
        :any:`numpy.array`
            A frame of the video. The size is (3, 1920, 1080).
        """
        vfilename = self.make_path(directory=self.original_directory, extension=".avi")
        return iter(reader(vfilename))

    @property
    def number_of_frames(self):
        """Returns the number of frames in a video file.

        Returns
        -------
        int
            The number of frames.
        """
        vfilename = self.make_path(directory=self.original_directory, extension=".avi")
        return reader(vfilename).number_of_frames

    @property
    def frame_shape(self):
        """Returns the size of each frame in this database.

        Returns
        -------
        (int, int, int)
            The (#Channels, Height, Width) which is :any:`OULUNPU_FRAME_SHAPE`.
        """
        return OULUNPU_FRAME_SHAPE

    @property
    def annotations(self):
        """Reads the annotations.

        If the file object has an attribute of annotation_directory, it will read
        annotations from there instead of loading annotations that are shipped with the
        database.

        Returns
        -------
        dict
            The annotations as a dictionary, e.g.:
            ``{'0': {'reye':(re_y,re_x), 'leye':(le_y,le_x)}, ...}``
        """
        if (
            hasattr(self, "annotation_directory")
            and self.annotation_directory is not None
        ):
            path = self.make_path(self.annotation_directory, extension=".json")
            return read_annotation_file(path, annotation_type="json")

        path = self.make_path(directory=self.original_directory, extension=".txt")
        annotations = {}
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                num_frame, x_eye_right, y_eye_right, x_eye_left, y_eye_left = line.split(
                    ","
                )
                annotations[num_frame] = {
                    "reye": (int(y_eye_right), int(x_eye_right)),
                    "leye": (int(y_eye_left), int(x_eye_left)),
                }
        return annotations

    def load(
        self,
        directory=None,
        extension=".avi",
        frame_selector=FrameSelector(selection_style="all"),
    ):
        """Loads the video file and returns in a
        :any:`bob.bio.video.FrameContainer`.

        Parameters
        ----------
        directory : :obj:`str`, optional
            The directory to load the data from.
        extension : :obj:`str`, optional
            The extension of the file to load.
        frame_selector : :any:`bob.bio.video.FrameSelector`, optional
            Which frames to select.

        Returns
        -------
        :any:`bob.bio.video.FrameContainer`
            The loaded frames inside a frame container.
        """
        directory = directory or self.original_directory
        extension = extension or self.original_extension
        return frame_selector(self.make_path(directory, extension))


class Database(FileListPadDatabase):
    """The database interface for the OULU-NPU dataset."""

    def __init__(
        self,
        original_directory=rc["bob.db.oulunpu.directory"],
        name="oulunpu",
        pad_file_class=None,
        original_extension=".avi",
        annotation_directory=None,
        **kwargs
    ):
        """Summary

        Parameters
        ----------
        original_directory : TYPE, optional
            Description
        name : str, optional
            Description
        pad_file_class : None, optional
            Description
        original_extension : str, optional
            Description
        annotation_directory : str
            If provided, the annotations will be read from this directory
            instead of the default annotations that are provided.
        **kwargs
            Description
        """
        if pad_file_class is None:
            pad_file_class = File
        filelists_directory = resource_filename(__name__, "lists")
        super(Database, self).__init__(
            filelists_directory=filelists_directory,
            name=name,
            original_directory=original_directory,
            pad_file_class=pad_file_class,
            original_extension=original_extension,
            annotation_directory=annotation_directory,
            training_depends_on_protocol=True,
            **kwargs
        )

    def objects(
        self,
        groups=None,
        protocol=None,
        purposes=None,
        model_ids=None,
        classes=None,
        **kwargs
    ):
        """Returns the requested samples."""
        files = super(Database, self).objects(
            groups=groups,
            protocol=protocol,
            purposes=purposes,
            model_ids=model_ids,
            classes=classes,
            **kwargs
        )
        for f in files:
            f.original_directory = self.original_directory
            f.original_extension = self.original_extension
            f.annotation_directory = self.annotation_directory

        return files

    def frames(self, padfile):
        return padfile.frames

    def number_of_frames(self, padfile):
        return padfile.number_of_frames

    @property
    def frame_shape(self):
        return OULUNPU_FRAME_SHAPE

    def annotations(self, padfile):
        return padfile.annotations
