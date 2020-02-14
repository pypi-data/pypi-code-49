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
=======
outputs
=======

This module implements output related classes
"""

import six

import logging
import zmq

logger = logging.getLogger(__name__)


class SynchronizationListener:
    """A callback mechanism to keep Inputs and Outputs in groups and lists
    synchronized together."""

    def __init__(self):
        self.data_index_start = -1
        self.data_index_end = -1

    def onIntervalChanged(self, data_index_start, data_index_end):
        """Callback updating the start and end index to use.

        Parameters:
            data_index_start (int): New start index for the data

            data_index_end (int): New end index for the data
        """

        self.data_index_start = data_index_start
        self.data_index_end = data_index_end


# ----------------------------------------------------------


class Output(object):
    """Represents one output of a processing block

    A list of outputs implementing this interface is provided to the algorithms
    (see :py:class:`OutputList`).


    Parameters:

      name (str): Name of the output

      data_sink (data.DataSink): Sink of data to be used by the output,
        pre-configured with the correct data format.


    Attributes:

      name (str): Name of the output (algorithm-specific)

      data_sink (data.DataSink): Sink of data used by the output

      last_written_data_index (int): Index of the last block of data written by
        the output

      nb_data_blocks_written (int): Number of data blocks written so far


    """

    def __init__(
        self, name, data_sink, synchronization_listener=None, force_start_index=0
    ):

        self.name = str(name)
        self.last_written_data_index = force_start_index - 1
        self.nb_data_blocks_written = 0
        self.data_sink = data_sink
        self._synchronization_listener = synchronization_listener

    def _createData(self):
        """Retrieves an uninitialized block of data corresponding to the data
        format of the output

        This method must be called to correctly create a new block of data
        """

        if hasattr(self.data_sink, "dataformat"):
            return self.data_sink.dataformat.type()
        else:
            raise RuntimeError(
                "The currently used data sink is not bound to "
                "a dataformat - you cannot create uninitialized data under "
                "these circumstances"
            )

    def write(self, data, end_data_index=None):
        """Write a block of data on the output

        Parameters:

          data (baseformat.baseformat): The block of data to write, or
            None (if the algorithm doesn't want to write any data)

          end_data_index (int): Last index of the written data (see the section
            *Inputs synchronization* of the User's Guide). If not specified,
            the *current end data index* of the Inputs List is used

        """

        end_data_index = self._compute_end_data_index(end_data_index)

        # if the user passes a dictionary, converts to the proper baseformat type
        if isinstance(data, dict):
            d = self.data_sink.dataformat.type()
            d.from_dict(data, casting="safe", add_defaults=False)
            data = d

        self.data_sink.write(data, self.last_written_data_index + 1, end_data_index)

        self.last_written_data_index = end_data_index
        self.nb_data_blocks_written += 1

    def isDataMissing(self):
        """Returns whether data are missing"""

        return (self._synchronization_listener is not None) and (
            self._synchronization_listener.data_index_end
            != self.last_written_data_index
        )

    def isConnected(self):
        """Returns whether the associated data sink is connected"""

        return self.data_sink.isConnected()

    def _compute_end_data_index(self, end_data_index):
        if end_data_index is not None:
            if (end_data_index < self.last_written_data_index + 1) or (
                (self._synchronization_listener is not None)
                and (end_data_index > self._synchronization_listener.data_index_end)
            ):
                raise KeyError(
                    "Algorithm logic error on write(): `end_data_index' "
                    "is not consistent with last written index"
                )

        elif self._synchronization_listener is not None:
            end_data_index = self._synchronization_listener.data_index_end

        else:
            end_data_index = self.last_written_data_index + 1

        return end_data_index

    def close(self):
        """Closes the associated data sink"""

        self.data_sink.close()


# ----------------------------------------------------------


class RemotelySyncedOutput(Output):
    def __init__(
        self,
        name,
        data_sink,
        socket,
        synchronization_listener=None,
        force_start_index=0,
    ):
        super(RemotelySyncedOutput, self).__init__(
            name, data_sink, synchronization_listener, force_start_index
        )
        self.socket = socket

    def write(self, data, end_data_index=None):
        super(RemotelySyncedOutput, self).write(data, end_data_index)

        self.socket.send_string("wrt", zmq.SNDMORE)
        self.socket.send_string(self.name, zmq.SNDMORE)
        self.socket.send_string("{}".format(end_data_index))
        self.socket.recv()


# ----------------------------------------------------------


class OutputList:
    """Represents the list of outputs of a processing block

    A list implementing this interface is provided to the algorithms

    See :py:class:`Output`.

    Example:

      .. code-block:: python

         outputs = OutputList()
         ...

         print(outputs['result'].data_format)

         for index in six.moves.range(0, len(outputs)):
             outputs[index].write(...)

         for output in outputs:
             output.write(...)

         for output in outputs[0:2]:
             output.write(...)

    """

    def __init__(self):
        self._outputs = []

    def __getitem__(self, index):

        if isinstance(index, six.string_types):
            try:
                return [x for x in self._outputs if x.name == index][0]
            except IndexError:
                pass
        elif isinstance(index, int):
            if index < len(self._outputs):
                return self._outputs[index]
        return None

    def __iter__(self):
        for k in self._outputs:
            yield k

    def __len__(self):
        return len(self._outputs)

    def add(self, output):
        """Adds an output to the list


        Parameters:

          input (Output): The output to add

        """

        self._outputs.append(output)
