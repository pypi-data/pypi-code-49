#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


"""
====
data
====

Data I/O classes and functions
"""

import os
import re
import glob
import simplejson as json
import time
import abc
import zmq
import logging
import six

from functools import reduce
from collections import namedtuple

from .hash import hashFileContents
from .dataformat import DataFormat
from .algorithm import Algorithm
from .exceptions import RemoteException

logger = logging.getLogger(__name__)


# ----------------------------------------------------------


def mixDataIndices(list_of_data_indices):
    """Given a collection of lists of data indices (belonging to separate
    but synchronized files/inputs), returns the most granular list of
    indices that span all the data

    For example, the mix of

      [(0, 2), (3, 4)]

    and

      [(0, 4)]

    is:

      [(0, 2), (3, 4)]


    The mix of

      [(0, 2), (3, 4)]

    and

      [(0, 1), (2, 3), (4, 4)]

    is:

      [(0, 1), (2, 2), (3, 3), (4, 4)]

    """

    start = max([x[0][0] for x in list_of_data_indices])
    end = min([x[-1][1] for x in list_of_data_indices])

    result = []
    current_start = start

    for index in range(start, end + 1):
        done = False

        for l in list_of_data_indices:
            for indices in l:
                if indices[1] == index:
                    result.append((current_start, index))
                    current_start = index + 1
                    done = True
                    break

            if done:
                break

    return result


# ----------------------------------------------------------


def getAllFilenames(filename, start_index=None, end_index=None):
    """Returns the names of all the files related to the given data file,
    taking the provided start and end indices into account.


    Parameters:

        filename (str): Name of the data file (path/to/cache/<hash>.data)

        start_index (int): The starting index (if not set or set to
            ``None``, the default, equivalent to ``0``)

        end_index (int): The end index (if not set or set to ``None``, the
            default, equivalent to ``the last existing data``)


    Returns:

        (data_filenames, indices_filenames,
         data_checksum_filenames, indices_checksum_filenames)
    """

    index_re = re.compile(r"^.*\.(\d+)\.(\d+)\.(data|index)(.checksum)?$")

    def file_start(f):
        """Returns the converted start indexes from a filename, otherwise 0"""
        r = index_re.match(f)
        if r:
            return int(r.group(1))
        return 0

    # Retrieve all the related files
    basename, ext = os.path.splitext(filename)
    filenames = sorted(glob.glob(basename + ".*"), key=file_start)

    # (If necessary) Only keep files containing the desired indices
    if (start_index is not None) or (end_index is not None):
        filtered_filenames = []
        for f in filenames:
            match = index_re.match(f)
            if match:
                start = int(match.group(1))
                end = int(match.group(2))
                if ((start_index is not None) and (end < start_index)) or (
                    (end_index is not None) and (start > end_index)
                ):
                    continue
            filtered_filenames.append(f)
        filenames = filtered_filenames

    # Separate the filenames in different lists
    data_filenames = [x for x in filenames if re.match(r"^.*\.(\d+)\.(\d+)\.data$", x)]
    indices_filenames = [
        x for x in filenames if re.match(r"^.*\.(\d+)\.(\d+)\.index$", x)
    ]
    data_checksum_filenames = [
        x for x in filenames if re.match(r"^.*\.(\d+)\.(\d+)\.data.checksum$", x)
    ]
    indices_checksum_filenames = [
        x for x in filenames if re.match(r"^.*\.(\d+)\.(\d+)\.index.checksum$", x)
    ]

    return (
        data_filenames,
        indices_filenames,
        data_checksum_filenames,
        indices_checksum_filenames,
    )


# ----------------------------------------------------------


class DataSource(object):
    """Base class to load data from some source"""

    def __init__(self):
        self.infos = []
        self.read_duration = 0
        self.nb_bytes_read = 0
        self.ready = False

    def close(self):
        self.infos = []

    def __del__(self):
        """Makes sure all resources are released when the object is deleted"""
        self.close()

    def __len__(self):
        if not self.ready:
            self._prepare()

        return len(self.infos)

    def __iter__(self):
        if not self.ready:
            self._prepare()

        for i in range(0, len(self.infos)):
            yield self[i]

    def __getitem__(self, index):
        raise NotImplementedError

    def first_data_index(self):
        if not self.ready:
            self._prepare()

        return self.infos[0].start_index

    def last_data_index(self):
        if not self.ready:
            self._prepare()

        return self.infos[-1].end_index

    def data_indices(self):
        if not self.ready:
            self._prepare()

        return [(x.start_index, x.end_index) for x in self.infos]

    def getAtDataIndex(self, data_index):
        if not self.ready:
            self._prepare()

        for index, infos in enumerate(self.infos):
            if (infos.start_index <= data_index) and (data_index <= infos.end_index):
                return self[index]

        return (None, None, None)

    def statistics(self):
        """Return the statistics about the number of bytes read"""
        return (self.nb_bytes_read, self.read_duration)

    def _prepare(self):
        self.ready = True


# ----------------------------------------------------------


class CachedDataSource(DataSource):
    """Utility class to load data from a file in the cache"""

    def __init__(self):
        super(CachedDataSource, self).__init__()

        self.filenames = None
        self.encoding = None  # Must be 'binary' or 'json'
        self.prefix = None
        self.dataformat = None
        self.current_file = None
        self.current_file_index = None
        self.unpack = True

    def _readHeader(self, file):
        """Read the header of the provided file"""

        # Read file format
        self.encoding = file.readline()[:-1]
        if not isinstance(self.encoding, str):
            self.encoding = self.encoding.decode("utf8")

        if self.encoding not in ("binary", "json"):
            raise RuntimeError(
                "valid formats for data reading are 'binary' "
                "or 'json': the format `%s' is invalid" % self.encoding
            )

        # Read data format
        dataformat_name = file.readline()[:-1]

        if self.dataformat is None:
            if not isinstance(dataformat_name, str):
                dataformat_name = dataformat_name.decode("utf8")

            if dataformat_name.startswith("analysis:"):
                algo_name = dataformat_name.split(":")[1]
                algo = Algorithm(self.prefix, algo_name)
                if not algo.valid:
                    raise RuntimeError(
                        "the dataformat `%s' is the result of an "
                        "algorithm which is not valid" % algo_name
                    )
                self.dataformat = algo.result_dataformat()
            else:
                self.dataformat = DataFormat(self.prefix, dataformat_name)

            if not self.dataformat.valid:
                raise RuntimeError(
                    "the dataformat `{}' is not valid\n{}".format(
                        dataformat_name, self.dataformat.errors
                    )
                )

        return True

    def setup(self, filename, prefix, start_index=None, end_index=None, unpack=True):
        """Configures the data source


        Parameters:

          filename (str): Name of the file to read the data from

          prefix (str): Establishes the prefix of your installation.

          start_index (int): The starting index (if not set or set to
            ``None``, the default, read data from the begin of file)

          end_index (int): The end index (if not set or set to ``None``, the
            default, reads the data until the end)

          unpack (bool): Indicates if the data must be unpacked or not


        Returns:

          ``True``, if successful, or ``False`` otherwise.

        """
        index_re = re.compile(r"^.*\.(\d+)\.(\d+)\.(data|index)(.checksum)?$")

        def check_consistency(data_filenames, checksum_filenames):
            """Perform some sanity check on the data/checksum files on disk:

              1. One-to-one mapping between data and checksum files
              2. Checksum comparison between hash(data) and checksum files
              3. Contiguous indices if they are present
            """

            # Make sure that we have a perfect match between data files and
            # checksum files
            checksum_filenames_noext = [
                os.path.splitext(f)[0] for f in checksum_filenames
            ]

            if data_filenames != checksum_filenames_noext:
                raise IOError(
                    "number of data files and checksum files for `%s' "
                    "does not match (%d != %d)"
                    % (filename, len(data_filenames), len(checksum_filenames_noext))
                )

            # list of start/end indices to check that there are contiguous
            indices = []
            for f_data, f_chck in zip(data_filenames, checksum_filenames):
                expected_chksum = open(f_chck, "rt").read().strip()
                current_chksum = hashFileContents(f_data)
                if expected_chksum != current_chksum:
                    raise IOError(
                        "data file `%s' has a checksum (%s) that differs "
                        "from expected one (%s)"
                        % (f_data, current_chksum, expected_chksum)
                    )

                r = index_re.match(f_data)
                if r:
                    indices.append((int(r.group(1)), int(r.group(2))))

            indices = sorted(indices, key=lambda v: v[0])
            ok_indices = True

            if len(indices) > 1:
                ok_indices = sum(
                    [
                        (indices[i + 1][0] - indices[i][1] == 1)
                        for i in range(len(indices) - 1)
                    ]
                )

            if not ok_indices:
                raise IOError(
                    "data file `%s|%s' has missing indices." % (f_data, f_chck)
                )

        self.prefix = prefix
        self.unpack = unpack

        # Retrieve the list of all needed files
        (
            self.filenames,
            indices_filenames,
            data_checksum_filenames,
            indices_checksum_filenames,
        ) = getAllFilenames(filename, start_index, end_index)

        if len(self.filenames) == 0:
            logger.warn("No files found for %s" % filename)
            return False

        check_consistency(self.filenames, data_checksum_filenames)

        # Load all the needed infos from all the files
        FileInfos = namedtuple(
            "FileInfos", ["file_index", "start_index", "end_index", "offset", "size"]
        )

        for file_index, current_filename in enumerate(self.filenames):
            try:
                f = open(current_filename, "rb")
            except Exception as e:
                logger.warn("Could not setup `%s': %s" % (filename, e))
                return False

            # Reads the header of the current file
            self._readHeader(f)
            offset = f.tell()

            # Process each data unit from the file
            while True:
                line = f.readline()
                if not line:
                    break

                offset += len(line)

                (start, end, data_size) = [int(x) for x in line.split()]

                if ((start_index is None) or (start >= start_index)) and (
                    (end_index is None) or (end <= end_index)
                ):
                    self.infos.append(
                        FileInfos(
                            file_index=file_index,
                            start_index=start,
                            end_index=end,
                            offset=offset,
                            size=data_size,
                        )
                    )

                f.seek(data_size, 1)
                offset += data_size

            f.close()

        return True

    def close(self):
        if self.current_file is not None:
            self.current_file.close()

        super(CachedDataSource, self).close()

    def __getitem__(self, index):
        """Retrieve a block of data

        Returns:

          A tuple (data, start_index, end_index)

        """

        if not self.ready:
            self._prepare()

        if (index < 0) or (index >= len(self.infos)):
            return (None, None, None)

        infos = self.infos[index]

        if self.current_file_index != infos.file_index:
            if self.current_file is not None:
                self.current_file.close()
                self.current_file = None

            try:
                self.current_file = open(self.filenames[infos.file_index], "rb")
                self.current_file_index = infos.file_index
            except Exception as e:
                raise IOError(
                    "Could not read `%s': %s" % (self.filenames[infos.file_index], e)
                )

        self.current_file.seek(infos.offset, 0)

        t1 = time.time()
        encoded_data = self.current_file.read(infos.size)
        t2 = time.time()

        self.read_duration += t2 - t1
        self.nb_bytes_read += infos.size

        if self.unpack:
            data = self.dataformat.type()
            data.unpack(encoded_data)
        else:
            data = encoded_data

        return (data, infos.start_index, infos.end_index)


# ----------------------------------------------------------


class DatabaseOutputDataSource(DataSource):
    """Utility class to load data from an output of a database view"""

    def __init__(self):
        super(DatabaseOutputDataSource, self).__init__()

        self.prefix = None
        self.dataformat = None
        self.view = None
        self.output_name = None
        self.pack = True

    def setup(
        self,
        view,
        output_name,
        dataformat_name,
        prefix,
        start_index=None,
        end_index=None,
        pack=False,
    ):
        """Configures the data source


        Parameters:

          prefix (str): Establishes the prefix of your installation.

          start_index (int): The starting index (if not set or set to
            ``None``, the default, read data from the begin of file)

          end_index (int): The end index (if not set or set to ``None``, the
            default, reads the data until the end)

          unpack (bool): Indicates if the data must be unpacked or not


        Returns:

          ``True``, if successful, or ``False`` otherwise.

        """

        self.prefix = prefix
        self.view = view
        self.output_name = output_name
        self.pack = pack

        self.dataformat = DataFormat(self.prefix, dataformat_name)

        if not self.dataformat.valid:
            raise RuntimeError("the dataformat `%s' is not valid" % dataformat_name)

        # Load all the needed infos from all the files
        Infos = namedtuple("Infos", ["start_index", "end_index"])

        objects = self.view.objects()

        start = None
        end = None
        previous_value = None

        attribute = self.view.get_output_mapping(output_name)

        for index, obj in enumerate(objects):
            if start is None:
                start = index
                previous_value = getattr(obj, attribute)
            elif getattr(obj, attribute) != previous_value:
                end = index - 1
                previous_value = None

                if ((start_index is None) or (start >= start_index)) and (
                    (end_index is None) or (end <= end_index)
                ):
                    self.infos.append(Infos(start_index=start, end_index=end))

                start = index
                previous_value = getattr(obj, attribute)

        end = index

        if ((start_index is None) or (start >= start_index)) and (
            (end_index is None) or (end <= end_index)
        ):
            self.infos.append(Infos(start_index=start, end_index=end))

        return True

    def __getitem__(self, index):
        """Retrieve a block of data

        Returns:

          A tuple (data, start_index, end_index)

        """

        if not self.ready:
            self._prepare()

        if (index < 0) or (index >= len(self.infos)):
            return (None, None, None)

        infos = self.infos[index]

        t1 = time.time()
        data = self.view.get(self.output_name, infos.start_index)
        t2 = time.time()

        self.read_duration += t2 - t1

        if isinstance(data, dict):
            d = self.dataformat.type()
            d.from_dict(data, casting="safe", add_defaults=False)
            data = d

        if self.pack:
            data = data.pack()
            self.nb_bytes_read += len(data)

        return (data, infos.start_index, infos.end_index)


# ----------------------------------------------------------


class RemoteDataSource(DataSource):
    """Utility class to load data from a data source accessible via a socket"""

    def __init__(self):
        super(RemoteDataSource, self).__init__()

        self.socket = None
        self.input_name = None
        self.dataformat = None
        self.unpack = True

    def setup(self, socket, input_name, dataformat_name, prefix, unpack=True):
        """Configures the data source


        Parameters:

          socket (zmq.Socket): The socket to use to access the data.

          input_name (str): Name of the input corresponding to the data source.

          dataformat_name (str): Name of the data format.

          prefix (str): Establishes the prefix of your installation.

          unpack (bool): Indicates if the data must be unpacked or not


        Returns:

          ``True``, if successful, or ``False`` otherwise.

        """

        self.socket = socket
        self.input_name = input_name
        self.unpack = unpack

        self.dataformat = DataFormat(prefix, dataformat_name)

        if not self.dataformat.valid:
            raise RuntimeError("the dataformat `%s' is not valid" % dataformat_name)

        return True

    def __getitem__(self, index):
        """Retrieve a block of data

        Returns:

          A tuple (data, start_index, end_index)

        """

        if not self.ready:
            self._prepare()

        if (index < 0) or (index >= len(self.infos)):
            return (None, None, None)

        infos = self.infos[index]

        logger.debug("send: (get) get %s %d", self.input_name, index)

        t1 = time.time()

        self.socket.send_string("get", zmq.SNDMORE)
        self.socket.send_string(self.input_name, zmq.SNDMORE)
        self.socket.send_string("%d" % index)

        answer = self.socket.recv().decode("utf-8")

        if answer == "err":
            self.read_duration += time.time() - t1
            kind = self.socket.recv()
            message = self.socket.recv()
            raise RemoteException(kind, message)

        start = int(answer)
        end = int(self.socket.recv())

        packed = self.socket.recv()

        t2 = time.time()

        logger.debug("recv: <bin> (size=%d), indexes=(%d, %d)", len(packed), start, end)

        self.nb_bytes_read += len(packed)

        if self.unpack:
            data = self.dataformat.type()
            data.unpack(packed)
        else:
            data = packed

        self.read_duration += t2 - t1

        return (data, infos.start_index, infos.end_index)

    def _prepare(self):
        # Load the needed infos from the socket
        Infos = namedtuple("Infos", ["start_index", "end_index"])

        logger.debug("send: (ifo) infos %s", self.input_name)

        self.socket.send_string("ifo", zmq.SNDMORE)
        self.socket.send_string(self.input_name)

        answer = self.socket.recv().decode("utf-8")
        logger.debug("recv: %s", answer)

        if answer == "err":
            kind = self.socket.recv()
            message = self.socket.recv()
            raise RemoteException(kind, message)

        nb = int(answer)
        for i in range(nb):
            start = int(self.socket.recv())
            end = int(self.socket.recv())
            self.infos.append(Infos(start_index=start, end_index=end))

        self.ready = True


# ----------------------------------------------------------


class DataSink(object):

    """Interface of all the Data Sinks

    Data Sinks are used by the outputs of an algorithm to write/transmit data.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self, data, start_data_index, end_data_index):
        """Writes a block of data

        Parameters:

          data (baseformat.baseformat): The block of data to write

          start_data_index (int): Start index of the written data

          end_data_index (int): End index of the written data

        """

        pass

    @abc.abstractmethod
    def isConnected(self):
        """Returns whether the data sink is connected"""

        pass

    def close(self):
        """Closes the data sink"""

        pass


# ----------------------------------------------------------


class StdoutDataSink(DataSink):

    """Data Sink that prints informations about the written data on stdout

    Note: The written data is lost! Use this class for debugging purposes
    """

    def __init__(self):
        super(StdoutDataSink, self).__init__()
        self.dataformat = None
        self.prefix = ""
        self.display_data = True

    def setup(self, dataformat, prefix=None, display_data=True):
        self.dataformat = dataformat
        self.display_data = display_data

        if prefix is not None:
            self.prefix = prefix
            if self.prefix != "":
                self.prefix += " "

    def write(self, data, start_data_index, end_data_index):
        """Write a block of data

        Parameters:

          data (baseformat.baseformat) The block of data to write

          start_data_index (int): Start index of the written data

          end_data_index (int): End index of the written data

        """

        if self.display_data:
            print(
                "%s(%d -> %d): %s"
                % (self.prefix, start_data_index, end_data_index, str(data))
            )
        else:
            print(
                "%s(%d -> %d): <data>" % (self.prefix, start_data_index, end_data_index)
            )

    def isConnected(self):
        return True


# ----------------------------------------------------------


class CachedDataSink(DataSink):

    """Data Sink that save data in the Cache

    The default behavior is to save the data in a binary format.
    """

    def __init__(self):
        self.filename = None
        self.encoding = None
        self.dataformat = None
        self.start_index = None
        self.end_index = None

        self.data_file = None
        self.index_file = None
        self.last_written_data_index = None

        self.nb_bytes_written = 0
        self.write_duration = 0

    def setup(self, filename, dataformat, start_index, end_index, encoding="binary"):
        """Configures the data sink

        Parameters:

          filename (str): Name of the file to generate

          dataformat (dataformat.DataFormat): The dataformat to be used
            inside this file. All objects stored inside this file will respect
            that format.

          encoding (str): String defining the encoding to be used for encoding
            the data. Only a few options are supported: ``binary``
            (the default) or ``json`` (debugging purposes).

        """

        # Close current file if open
        self.close()

        if encoding not in ("binary", "json"):
            raise RuntimeError(
                "valid formats for data writing are 'binary' "
                "or 'json': the format `%s' is invalid" % format
            )

        if dataformat.name == "__unnamed_dataformat__":
            raise RuntimeError("cannot record data using an unnamed data format")

        filename, data_ext = os.path.splitext(filename)

        self.filename = "%s.%d.%d%s" % (filename, start_index, end_index, data_ext)
        self.encoding = encoding
        self.dataformat = dataformat
        self.start_index = start_index
        self.end_index = end_index

        self.nb_bytes_written = 0
        self.write_duration = 0
        self.last_written_data_index = None

        try:
            self.data_file = open(self.filename, "wb")
        except Exception as e:
            logger.error("Failed to open data file {}: {}".format(self.filename, e))
            return False

        try:
            index_filename = self.filename.replace(".data", ".index")
            self.index_file = open(index_filename, "wt")
        except Exception as e:
            logger.error("Failed to open index file {}: {}".format(index_filename, e))
            return False

        # Write the dataformat
        self.data_file.write(six.b("%s\n%s\n" % (self.encoding, self.dataformat.name)))
        self.data_file.flush()

        return True

    def close(self):
        """Closes the data sink
        """

        if self.data_file is not None:
            self.data_file.close()
            self.index_file.close()

            # If file is not complete, delete it
            if (self.last_written_data_index is None) or (
                self.last_written_data_index < self.end_index
            ):
                if self.last_written_data_index is None:
                    message = "No data written"
                else:
                    message = "No enough data written: last written {} vs end {}".format(
                        self.last_data_index, self.end_index
                    )

                logger.warning("Removing cache files: {}".format(message))

                try:
                    os.remove(self.filename)
                    os.remove(self.filename.replace(".data", ".index"))
                    return True
                except Exception:
                    return False

            # Creates the checksums for all data and indexes
            chksum_data = hashFileContents(self.filename)
            with open(self.filename + ".checksum", "wt") as f:
                f.write(chksum_data)

            index_filename = self.filename.replace(".data", ".index")
            chksum_index = hashFileContents(index_filename)
            with open(index_filename + ".checksum", "wt") as f:
                f.write(chksum_index)

            self.data_file = None
            self.index_file = None
            self.last_written_data_index = None

        return True

    def __del__(self):
        """Make sure the files are closed when the object is deleted
        """
        self.close()

    def write(self, data, start_data_index, end_data_index):
        """Writes a block of data to the filesystem

        Parameters:

          data (baseformat.baseformat): The block of data to write

          start_data_index (int): Start index of the written data

          end_data_index (int): End index of the written data

        """

        # If the user passed a dictionary - convert it
        if isinstance(data, dict):
            data = self.dataformat.type(**data)
        else:
            # Checks that the input data conforms to the expected format
            if data.__class__._name != self.dataformat.name:
                raise TypeError(
                    "input data uses format `%s' while this sink "
                    "expects `%s'" % (data.__class__._name, self.dataformat)
                )

        if self.data_file is None:
            raise RuntimeError("No destination file")

        # Encoding
        if self.encoding == "binary":
            encoded_data = data.pack()
        else:
            from .utils import NumpyJSONEncoder

            encoded_data = json.dumps(data.as_dict(), indent=4, cls=NumpyJSONEncoder)

        # Adds a new line by the end of the encoded data
        encoded_data += six.b("\n")

        informations = six.b(
            "%d %d %d\n" % (start_data_index, end_data_index, len(encoded_data))
        )

        t1 = time.time()

        self.data_file.write(informations + encoded_data)
        self.data_file.flush()

        indexes = "%d %d\n" % (start_data_index, end_data_index)
        self.index_file.write(indexes)
        self.index_file.flush()

        t2 = time.time()

        self.nb_bytes_written += len(informations) + len(encoded_data) + len(indexes)
        self.write_duration += t2 - t1

        self.last_written_data_index = end_data_index

    def statistics(self):
        """Return the statistics about the number of bytes written to the cache"""
        return (self.nb_bytes_written, self.write_duration)

    def isConnected(self):
        return self.filename is not None


# ----------------------------------------------------------


def load_data_index(cache_root, hash_path):
    """Loads a cached-data index if it exists. Returns empty otherwise.

    Parameters:

      cache_root (str): The path to the root of the cache directory

      hash_path (str): The hashed path of the input you wish to load the indexes
        for, as it is returned by the utility function :py:func:`.hash.toPath`.


    Returns:

      A list, which will be empty if the index file is not present. Note that,
      given the current design, an empty list means an error condition.

    """

    name_no_extension = os.path.splitext(hash_path)[0]  # remove .data
    index_stem = os.path.join(cache_root, name_no_extension)
    index_glob = index_stem + "*.index"

    candidates = glob.glob(index_glob)

    if not candidates:
        raise RuntimeError(
            "No index file matching the pattern `%s' found." % index_glob
        )

    retval = []
    end_index = 0
    for filename in candidates:
        with open(filename, "rt") as f:
            data = [k.split() for k in f.readlines() if k.strip()]
            start = [int(k[0]) for k in data]
            end = int(data[-1][1])  # last index

        # Checks if the sum exists and is correct
        expected_chksum = open(filename + ".checksum", "rt").read().strip()

        current_chksum = hashFileContents(filename)
        if expected_chksum != current_chksum:
            raise RuntimeError(
                "index file `%s' has a "
                "checksum (%s) that differs from expected one (%s)"
                % (filename, current_chksum, expected_chksum)
            )

        retval.extend(start)
        if end > end_index:
            end_index = end

    return sorted(retval) + [end_index + 1]


# ----------------------------------------------------------


def load_data_index_db(cache_root, hash_path):
    filename = os.path.join(cache_root, hash_path)

    if not os.path.exists(filename):
        return None

    retval = []

    with open(filename, "rb") as f:
        data = json.loads(f.read())

    current = data[0]

    column_names = current.keys()

    for col in range(0, len(column_names)):
        retval.append([0])

    for row, entry in enumerate(data[1:]):
        for col, name in enumerate(column_names):
            if entry[name] != current[name]:
                retval[col].append(row + 1)
                current[name] = entry[name]

    for col in range(0, len(column_names)):
        retval[col].append(len(data))

    return retval


# ----------------------------------------------------------


def _foundCommonIndices(lst):
    """Returns the list of common indices, given a list of list of indices
    """

    if lst == []:
        return lst
    lst_set = [set(k) for k in lst]
    common_indices = sorted(list(reduce(set.intersection, lst_set)))
    return common_indices


# ----------------------------------------------------------


def foundSplitRanges(lst, n_split):
    """Splits a list of lists of indices into n splits for parallelization
    purposes. """

    if [] in lst or lst == []:
        return []
    ci_lst = _foundCommonIndices(lst)
    res = []
    average_length = (float)(ci_lst[-1]) / n_split
    c = 0
    s = 0
    for i in range(1, len(ci_lst)):
        if ci_lst[i] >= (c + 1) * average_length and c < n_split - 1:
            res.append((ci_lst[s], ci_lst[i] - 1))
            s = i
            c += 1
        elif i == len(ci_lst) - 1:
            res.append((ci_lst[s], ci_lst[i] - 1))
    return res
