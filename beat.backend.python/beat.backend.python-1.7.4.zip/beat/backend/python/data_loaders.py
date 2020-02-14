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
============
data_loaders
============

This module implements all the data communication related classes
"""

import logging
import six

from .data import mixDataIndices

logger = logging.getLogger(__name__)

# ----------------------------------------------------------


class DataView(object):
    """Provides access to a subset of data from a group of inputs synchronized
    together

    Data views are created from a data loader (see :py:class:`DataLoader`),
    which are provided to the algorithms of types 'sequential' and 'autonomous'
    (see :py:class:`DataLoaderList`).

    Example:

      .. code-block:: python

         view = data_loader.view('input1', 0)

         for i in range(view.count())
             (data, start_index, end_index) = view[i]


    Parameters:

      data_loader (:py:class:`DataLoader`): Name of the data channel of the
        group of inputs

      data_indices (:py:class:`list`): Data indices to consider as a list of
        tuples


    Attributes:

      data_index_start (int): Lower data index across all inputs
        (see the section *Inputs synchronization* of the User's Guide)

      data_index_end (int): Bigger data index across all inputs
        (see the section *Inputs synchronization* of the User's Guide)

    """

    def __init__(self, data_loader, data_indices):
        self.infos             = {}
        self.data_indices      = data_indices
        self.nb_data_units     = len(data_indices)
        self.data_index_start  = data_indices[0][0]
        self.data_index_end    = data_indices[-1][1]

        for input_name, infos in data_loader.infos.items():
            input_data_indices = []
            current_start = self.data_index_start

            for i in range(self.data_index_start, self.data_index_end + 1):
                for indices in infos['data_indices']:
                    if indices[1] == i:
                        input_data_indices.append( (current_start, i) )
                        current_start = i + 1
                        break

            if (len(input_data_indices) == 0) or (input_data_indices[-1][1] != self.data_index_end):
                input_data_indices.append( (current_start, self.data_index_end) )

            self.infos[input_name] = dict(
                data_source = infos['data_source'],
                data_indices = input_data_indices,
                data = None,
                start_index = -1,
                end_index = -1,
            )


    def count(self, input_name=None):
        """Returns the number of available data indexes for the given input
        name. If none given the number of available data units.

        Parameters:

            input_name (str): Name of the input for which the count is
                requested

        Returns:
            (int): Number of data indexes for the input given or the number of
                data units.
        """
        if input_name is not None:
            try:
                return len(self.infos[input_name]['data_indices'])
            except:
                return None
        else:
            return self.nb_data_units


    def __getitem__(self, index):
        if index < 0:
            return (None, None, None)

        try:
            indices = self.data_indices[index]
        except:
            return (None, None, None)

        result = {}

        for input_name, infos in self.infos.items():
            if (indices[0] < infos['start_index']) or (infos['end_index'] < indices[0]):
                (infos['data'], infos['start_index'], infos['end_index']) = \
                        infos['data_source'].getAtDataIndex(indices[0])

            result[input_name] = infos['data']

        return (result, indices[0], indices[1])


# ----------------------------------------------------------


class DataLoader(object):
    """Provides access to data from a group of inputs synchronized together

    Data loaders are provided to the algorithms of types 'sequential' and
    'autonomous' (see :py:class:`DataLoaderList`).

    Example:

      .. code-block:: python

         # Iterate through all the data
         for i in range(data_loader.count())
             (data, start_index, end_index) = data_loader[i]
             print(data['input1'].data)

         # Restrict to a subset of the data
         view = data_loader.view('input1', 0)
         for i in range(view.count())
             (data, start_index, end_index) = view[i]


    Parameters:

      channel (str): Name of the data channel of the group of inputs


    Attributes:

      data_index_start (int): Lower data index across all inputs
        (see the section *Inputs synchronization* of the User's Guide)

      data_index_end (int): Bigger data index across all inputs
        (see the section *Inputs synchronization* of the User's Guide)

      channel (str): Name of the data channel of the group

    """

    def __init__(self, channel):
        self.channel            = str(channel)
        self.infos              = {}
        self.mixed_data_indices = None
        self.nb_data_units      = 0
        self.data_index_start   = -1  # Lower index across all inputs
        self.data_index_end     = -1  # Bigger index across all inputs


    def add(self, input_name, data_source):
        self.infos[input_name] = dict(
            data_source = data_source,
            data_indices = data_source.data_indices(),
            data = None,
            start_index = -1,
            end_index = -1,
        )

        self.mixed_data_indices = mixDataIndices([ x['data_indices'] for x in self.infos.values() ])
        self.nb_data_units = len(self.mixed_data_indices)
        self.data_index_start = self.mixed_data_indices[0][0]
        self.data_index_end = self.mixed_data_indices[-1][1]


    def input_names(self):
        """Returns the name of all inputs associated to this data loader"""

        return self.infos.keys()


    def count(self, input_name=None):
        """Returns the number of available data indexes for the given input
        name. If none given the number of available data units.

        Parameters:

            input_name (str): Name of the input for which the count is
                requested

        Returns:
            (int): Number of data indexes for the input given or the number of
                data units.
        """

        if input_name is not None:
            try:
                return len(self.infos[input_name]['data_indices'])
            except:
                return 0
        else:
            return self.nb_data_units


    def view(self, input_name, index):
        """ Returns the view associated with this data loader

        Parameters:
            input_name (str): Name of the input to get data from

            index (int): Position of the data indexes to retrieve

        Returns:
            (:py:class:`DataView`) either a DataView matching the query or None
        """

        if index < 0:
            return None

        try:
            indices = self.infos[input_name]['data_indices'][index]
        except:
            return None

        limited_data_indices = [ x for x in self.mixed_data_indices
                                 if (indices[0] <= x[0]) and (x[1] <= indices[1]) ]

        return DataView(self, limited_data_indices)


    def __getitem__(self, index):
        if index < 0:
            return (None, None, None)

        try:
            indices = self.mixed_data_indices[index]
        except:
            return (None, None, None)

        result = {}

        for input_name, infos in self.infos.items():
            if (indices[0] < infos['start_index']) or (infos['end_index'] < indices[0]):
                (infos['data'], infos['start_index'], infos['end_index']) = \
                        infos['data_source'].getAtDataIndex(indices[0])

            result[input_name] = infos['data']

        return (result, indices[0], indices[1])


# ----------------------------------------------------------


class DataLoaderList(object):
    """Represents a list of data loaders

    Inputs are organized by groups. The inputs inside a group are all
    synchronized together (see the section *Inputs synchronization* of the User's
    Guide). A data loader provides access to data from a group of inputs.

    A list implementing this interface is provided to the algorithms of types
    'sequential' and 'autonomous'.

    One group of inputs is always considered as the **main** one, and is used to
    drive the algorithm. The usage of the other groups is left to the algorithm.

    See :py:class:`DataLoader`


    Example:

      .. code-block:: python

         data_loaders = DataLoaderList()
         ...

         # Retrieve a data loader by name
         data_loader = data_loaders['labels']

         # Retrieve a data loader by index
         for index in range(0, len(data_loaders)):
             data_loader = data_loaders[index]

         # Iteration over all data loaders
         for data_loader in data_loaders:
             ...

         # Retrieve the data loader an input belongs to, by input name
         data_loader = data_loaders.loaderOf('label')


    Attributes:

      main_loader (DataLoader): Main data loader

    """

    def __init__(self):
        self._loaders = []
        self.main_loader = None


    def add(self, data_loader):
        """Add a data loader to the list

        :param DataLoader data_loader: The data
            loader to add
        """
        if self.main_loader is None:
            self.main_loader = data_loader

        self._loaders.append(data_loader)


    def __getitem__(self, name_or_index):
        try:
            if isinstance(name_or_index, six.string_types):
                return [x for x in self._loaders if x.channel == name_or_index][0]

            elif isinstance(name_or_index, int):
                return self._loaders[name_or_index]
        except:
            pass

        return None


    def __iter__(self):
        for i in range(len(self._loaders)):
            yield self._loaders[i]


    def __len__(self):
        return len(self._loaders)


    def loaderOf(self, input_name):
        """Returns the data loader matching the input name"""

        try:
            return [ k for k in self._loaders if input_name in k.input_names() ][0]
        except:
            return None


    def secondaries(self):
        """Returns a list of all data loaders except the main one"""

        secondaries_list = DataLoaderList()
        for data_loader in self._loaders:
            if data_loader is not self.main_loader:
                secondaries_list.add(data_loader)

        secondaries_list.main_loader = None

        return secondaries_list
