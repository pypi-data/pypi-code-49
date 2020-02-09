import six

from targets import pipes
from targets.base_target import logger
from targets.data_target import DataTarget
from targets.errors import TargetError
from targets.fs import get_file_system, get_file_system_name
from targets.pipes import Nop, Text
from targets.target_config import FileCompressions, TargetConfig


class FileTarget(DataTarget):
    """
    Base class for FileSystem Targets like  :class:`~databand.contrib.hdfs.HdfsTarget`.

    A FileTarget has an associated :py:class:`FileSystem` to which certain operations can be
    delegated. By default, :py:meth:`exists` and :py:meth:`remove` are delegated to the
    :py:class:`FileSystem`, which is determined by the :py:attr:`fs` property.

    Methods of FileTarget raise :py:class:`FileSystemException` if there is a problem
    completing the operation.

    """

    def __init__(
        self, path, fs, config=None, io_pipe=None, properties=None, source=None
    ):
        """
        Initializes a FileTarget instance.

        :param str path: the path associated with this FileTarget.
        """
        super(FileTarget, self).__init__(properties=properties, source=source)

        self.path = path
        self._fs = fs
        self.fs_name = self._fs.name if self._fs else get_file_system_name(path)
        self.io_pipe = io_pipe
        self.config = config  # type: TargetConfig
        if not path:
            raise TargetError("path must be set")

    @property
    def fs(self):
        if self._fs is None:
            return get_file_system(self.fs_name)
        return self._fs

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.path == other.path

    def _get_pipe(self, mode):
        if self.io_pipe:
            return self.io_pipe

        if six.PY2:
            pipe = Nop
        # python3 has differences between binary and non binary stream, so we need to have a proper handling for that
        elif "b" not in mode:
            pipe = Text
        else:
            pipe = Nop
        if not self.config:
            return pipe

        if self.config.compression == FileCompressions.gzip:
            pipe = pipe >> pipes.Gzip
        elif self.config.compression == FileCompressions.bzip:
            pipe = pipe >> pipes.Bzip2
        return pipe

    def open(self, mode="r"):
        """
        Open the FileSystem target.

        This method returns a file-like object which can either be read from or written to depending
        on the specified mode.

        :param str mode: the mode `r` opens the FileTarget in read-only mode, whereas `w` will
                         open the FileTarget in write mode. Subclasses can implement
                         additional options.
        """

        io_pipe = self._get_pipe(mode)
        if "r" in mode:
            return io_pipe.pipe_reader(self.fs.open_read(self.path, mode=mode))
        elif "w" in mode:
            return io_pipe.pipe_writer(self.fs.open_write(self.path, mode=mode))
        else:
            raise ValueError("Unsupported open mode '{}'".format(mode))

    def exists(self):
        """
        Returns ``True`` if the path for this FileTarget exists; ``False`` otherwise.

        This method is implemented by using :py:attr:`fs`.
        """
        path = self.path
        if "*" in path or "?" in path or "[" in path or "{" in path:
            logger.warning(
                "Using wildcards in path %s might lead to processing of an incomplete dataset; "
                "override exists() to suppress the warning.",
                path,
            )

        return self.fs.exists(path)

    def exist_after_write_consistent(self):
        return self.fs.exist_after_write_consistent()

    def remove(self):
        """
        Remove the resource at the path specified by this FileTarget.

        This method is implemented by using :py:attr:`fs`.
        """
        self.fs.remove(self.path)

    def __repr__(self):
        return repr(self.path)

    def __str__(self):
        return str(self.path)

    # basic file ops
    def mkdir_parent(self):
        self.fs.mkdir_parent(self.path)

    def move(self, new_path, raise_if_exists=False):
        self.fs.move(self.path, str(new_path), raise_if_exists=raise_if_exists)

    def move_from(self, from_path, raise_if_exists=False):
        self.fs.move(from_path, self.path, raise_if_exists=raise_if_exists)
        self.mark_success()

    def copy_from_local(self, local_path):
        self.fs.copy_from_local(local_path, self.path)

    def copy(self, new_path, raise_if_exists=False):
        self.fs.copy(self.path, str(new_path), raise_if_exists)

    def __fspath__(self):
        """
        https://www.python.org/dev/peps/pep-0519/
        make pandas be able to get targets
        :return:
        """
        return self.path

    def mark_success(self):
        if not self.exists():
            logger.info("Target is not exists, it can not be marked as success")

    def __hash__(self):
        return hash(self.path)


FileSystemTarget = FileTarget
