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
======
inputs
======

This module implements input related classes
"""

import logging

from functools import reduce

import six


logger = logging.getLogger(__name__)

# ----------------------------------------------------------


class Input(object):
    """Represents an input of a processing block that receive data from a
    (legacy) data source

    A list of those inputs must be provided to the algorithms (see
    :py:class:`InputList`)


    Parameters:

      name (str): Name of the input

      data_format (str): Data format accepted by the input


    Attributes:

      group (InputGroup): Group containing this input

      name (str): Name of the input (algorithm-specific)

      data (baseformat.baseformat): The last block of data received on
        the input

      data_index (int): Index of the last block of data received on the input
        (see the section *Inputs synchronization* of the User's Guide)

      data_index_end (int): End index of the last block of data received on the
        input (see the section *Inputs synchronization* of the User's Guide)

      data_format (str): Data format accepted by the input

      data_same_as_previous (bool): Indicates if the last block of data
        received was changed (see the section *Inputs synchronization* of the
        User's Guide)

      nb_data_blocks_read (int): Number of data blocks read so far

    """

    def __init__(self, name, data_format, data_source):

        self.group                 = None
        self.name                  = str(name)
        self.data                  = None
        self.data_index            = -1
        self.data_index_end        = -1
        self.next_data_index       = 0
        self.data_same_as_previous = True
        self.data_format           = data_format
        self.nb_data_blocks_read   = 0
        self.data_source           = data_source


    def isDataUnitDone(self):
        """Indicates if the current data unit will change at the next iteration
        """

        if (self.data_index_end >= 0) and (self.group.last_data_index == -1):
            return True

        return (self.data_index_end == self.group.last_data_index)


    def hasMoreData(self):
        """Indicates if there is more data to process on the input"""

        return (self.next_data_index < len(self.data_source))


    def hasDataChanged(self):
        """Indicates if the current data unit is different than the one at the
        previous iteration
        """

        return not self.data_same_as_previous


    def next(self):
        """Retrieves the next block of data"""

        if self.group.restricted_access:
            raise RuntimeError('Not authorized')

        if self.next_data_index >= len(self.data_source):
            message = "User algorithm asked for more data for channel " \
                      "`%s' on input `%s', but it is over (no more data). This " \
                      "normally indicates a programming error on the user " \
                      "side." % (self.group.channel, self.name)
            raise RuntimeError(message)

        (self.data, self.data_index, self.data_index_end) = self.data_source[self.next_data_index]

        self.data_same_as_previous = False
        self.next_data_index += 1
        self.nb_data_blocks_read += 1


# ----------------------------------------------------------


class InputGroup:
    """Represents a group of inputs synchronized together

    A group implementing this interface is provided to the algorithms (see
    :py:class:`InputList`).

    See :py:class:`Input`

    Example:

      .. code-block:: python

         inputs = InputList()

         print(inputs['labels'].data_format)

         for index in range(0, len(inputs)):
             print(inputs[index].data_format)

         for input in inputs:
             print(input.data_format)

         for input in inputs[0:2]:
             print(input.data_format)


    Parameters:

      channel (str): Name of the data channel of the group

      synchronization_listener (outputs.SynchronizationListener):
        Synchronization listener to use

      restricted_access (bool): Indicates if the algorithm can freely use the
        inputs


    Attributes:

      data_index (int): Index of the last block of data received on the inputs
        (see the section *Inputs synchronization* of the User's Guide)

      data_index_end (int): End index of the last block of data received on the
        inputs (see the section *Inputs synchronization* of the User's Guide)

      channel (str): Name of the data channel of the group

      synchronization_listener (outputs.SynchronizationListener):
        Synchronization listener used

    """

    def __init__(self, channel, synchronization_listener=None,
                 restricted_access=True):

        self._inputs                  = []
        self.data_index               = -1  # Lower index across all inputs
        self.data_index_end           = -1  # Bigger index across all inputs
        self.first_data_index         = -1  # Start index of the current data units
        self.last_data_index          = -1  # End index of the current data units
        self.channel                  = str(channel)
        self.synchronization_listener = synchronization_listener
        self.restricted_access        = restricted_access


    def __getitem__(self, index):

        if isinstance(index, six.string_types):
            try:
                return [x for x in self._inputs if x.name == index][0]
            except:
                pass
        elif isinstance(index, int):
            if index < len(self._inputs):
                return self._inputs[index]
        return None


    def __iter__(self):
        for k in self._inputs: yield k


    def __len__(self):
        return len(self._inputs)


    def add(self, input):
        """Add an input to the group

        Parameters:

          input (Input): The input to add

        """

        input.group = self
        self._inputs.append(input)


    def hasMoreData(self):
        """Indicates if there is more data to process in the group"""

        return bool([x for x in self._inputs if x.hasMoreData()])



    def next(self):
        """Retrieve the next block of data on all the inputs"""

        # Only for groups not managed by the platform
        if self.restricted_access:
            raise RuntimeError('Not authorized')

        # Only retrieve new data on the inputs where the current data expire
        # first
        lower_end_index = reduce(lambda x, y: min(x, y.data_index_end),
                self._inputs[1:], self._inputs[0].data_index_end)
        inputs_to_update = [x for x in self._inputs \
                if x.data_index_end == lower_end_index]
        inputs_up_to_date = [x for x in self._inputs if x not in inputs_to_update]

        for input in inputs_to_update:
            input.next()

        for input in inputs_up_to_date:
            input.data_same_as_previous = True

        # Compute the group's start and end indices
        self.data_index = reduce(lambda x, y: min(x, y.data_index),
                self._inputs[1:], self._inputs[0].data_index)
        self.data_index_end = reduce(lambda x, y: max(x, y.data_index_end),
                self._inputs[1:], self._inputs[0].data_index_end)

        self.first_data_index = reduce(lambda x, y: max(x, y.data_index),
                self._inputs[1:], self._inputs[0].data_index)
        self.last_data_index = reduce(lambda x, y: min(x, y.data_index_end),
                self._inputs[1:], self._inputs[0].data_index_end)

        # Inform the synchronisation listener
        if self.synchronization_listener is not None:
            self.synchronization_listener.onIntervalChanged(self.first_data_index,
                                                            self.last_data_index)


# ----------------------------------------------------------


class InputList:
    """Represents the list of inputs of a processing block

    Inputs are organized by groups. The inputs inside a group are all
    synchronized together (see the section *Inputs synchronization* of the
    User's Guide).

    A list implementing this interface is provided to the algorithms

    One group of inputs is always considered as the **main** one, and is used
    to drive the algorithm. The usage of the other groups is left to the
    algorithm.

    See :py:class:`Input`
    See :py:class:`InputGroup`


    Example:

      .. code-block:: python

         inputs = InputList()
         ...

         # Retrieve an input by name
         input = inputs['labels']

         # Retrieve an input by index
         for index in range(0, len(inputs)):
             input = inputs[index]

         # Iteration over all inputs
         for input in inputs:
             ...

         # Iteration over some inputs
         for input in inputs[0:2]:
             ...

         # Retrieve the group an input belongs to, by input name
         group = inputs.groupOf('label')

         # Retrieve the group an input belongs to
         input = inputs['labels']
         group = input.group


    Attributes:

      main_group (InputGroup): Main group (for data-driven
        algorithms)

    """

    def __init__(self):
        self._groups = []
        self.main_group = None


    def add(self, group):
        """Add a group to the list

        :param InputGroup group: The group to add
        """
        if group.restricted_access and (self.main_group is None):
            self.main_group = group

        self._groups.append(group)


    def __getitem__(self, index):
        if isinstance(index, six.string_types):
            try:
                return [k for k in map(lambda x: x[index], self._groups) \
                        if k is not None][0]
            except:
                pass

        elif isinstance(index, int):
            for group in self._groups:
                if index < len(group): return group[index]
                index -= len(group)

        return None


    def __iter__(self):
        for i in range(len(self)): yield self[i]


    def __len__(self):
        return reduce(lambda x, y: x + len(y), self._groups, 0)


    def nbGroups(self):
        """Returns the number of groups this list belongs to"""
        return len(self._groups)


    def groupOf(self, input_name):
        """Returns the group which this input_name belongs to

        Parameters:
            :param str input_name: Name of the input for which the group should
                be search for.
        """
        try:
            return [k for k in self._groups if k[input_name] is not None][0]
        except:
            return None


    def hasMoreData(self):
        """Indicates if there is more data to process in any group"""
        return bool([x for x in self._groups if x.hasMoreData()])


    def group(self, name_or_index):
        """Returns the group matching the name or index passed as parameter"""

        if isinstance(name_or_index, six.string_types):
            try:
                return [x for x in self._groups if x.channel == name_or_index][0]
            except:
                return None
        elif isinstance(name_or_index, int):
            return self._groups[name_or_index]
        else:
            return None
