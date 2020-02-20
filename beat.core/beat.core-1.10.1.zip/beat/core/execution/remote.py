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
==========
remote
==========

Execution utilities
"""

import logging


from .base import BaseExecutor

from beat.backend.python.helpers import create_inputs_from_configuration
from beat.backend.python.helpers import create_outputs_from_configuration


logger = logging.getLogger(__name__)


class RemoteExecutor(BaseExecutor):
    """Base class for Executors that communicate with a message handler


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (dict, str): The piece of data representing the block to be executed.
        It must validate against the schema defined for execution blocks. If a
        string is passed, it is supposed to be a fully qualified absolute path to
        a JSON file containing the block execution information.

      cache (:py:class:`str`, Optional): If your cache is not located under
        ``<prefix>/cache``, then specify a full path here. It will be used
        instead.

      dataformat_cache (:py:class:`dict`, Optional): A dictionary mapping
        dataformat names to loaded dataformats. This parameter is optional and,
        if passed, may greatly speed-up database loading times as dataformats
        that are already loaded may be re-used. If you use this parameter, you
        must guarantee that the cache is refreshed as appropriate in case the
        underlying dataformats change.

      database_cache (:py:class:`dict`, Optional): A dictionary mapping
        database names to loaded databases. This parameter is optional and, if
        passed, may greatly speed-up database loading times as databases that
        are already loaded may be re-used. If you use this parameter, you must
        guarantee that the cache is refreshed as appropriate in case the
        underlying databases change.

      algorithm_cache (:py:class:`dict`, Optional): A dictionary mapping
        algorithm names to loaded algorithms. This parameter is optional and,
        if passed, may greatly speed-up database loading times as algorithms
        that are already loaded may be re-used. If you use this parameter, you
        must guarantee that the cache is refreshed as appropriate in case the
        underlying algorithms change.

      library_cache (:py:class:`dict`, Optional): A dictionary mapping library
        names to loaded libraries. This parameter is optional and, if passed,
        may greatly speed-up library loading times as libraries that are
        already loaded may be re-used. If you use this parameter, you must
        guarantee that the cache is refreshed as appropriate in case the
        underlying libraries change.


    Attributes:

      cache (str): The path to the cache currently being used

      errors (list): A list containing errors found while loading this execution
        block.

      data (dict): The original data for this executor, as loaded by our JSON
        decoder.

      algorithm (beat.core.algorithm.Algorithm): An object representing the
        algorithm to be run.

      databases (dict): A dictionary in which keys are strings with database
        names and values are :py:class:`.database.Database`, representing the
        databases required for running this block. The dictionary may be empty
        in case all inputs are taken from the file cache.

      views (dict): A dictionary in which the keys are tuples pointing to the
        ``(<database-name>, <protocol>, <set>)`` and the value is a setup view
        for that particular combination of details. The dictionary may be empty
        in case all inputs are taken from the file cache.

      input_list (beat.backend.python.inputs.InputList): A list of inputs that
        will be served to the algorithm.

      output_list (beat.backend.python.outputs.OutputList): A list of outputs
        that the algorithm will produce.

      data_sources (list): A list with all data-sources created by our execution
        loader.

      data_sinks (list): A list with all data-sinks created by our execution
        loader. These are useful for clean-up actions in case of problems.

    """

    def __init__(
        self,
        prefix,
        data,
        ip_address,
        cache=None,
        dataformat_cache=None,
        database_cache=None,
        algorithm_cache=None,
        library_cache=None,
        custom_root_folders=None,
    ):

        super(RemoteExecutor, self).__init__(
            prefix,
            data,
            cache=cache,
            dataformat_cache=dataformat_cache,
            database_cache=database_cache,
            algorithm_cache=algorithm_cache,
            library_cache=library_cache,
            custom_root_folders=custom_root_folders,
        )

        # Initialisations
        self.ip_address = ip_address
        self.message_handler = None

    def _prepare_inputs(self):
        """Prepares all input required by the execution."""

        (self.input_list, self.data_loaders) = create_inputs_from_configuration(
            self.data, self.algorithm, self.prefix, self.cache
        )

    def _prepare_outputs(self):
        """Prepares all output required by the execution."""

        (self.output_list, self.data_sinks) = create_outputs_from_configuration(
            self.data,
            self.algorithm,
            self.prefix,
            self.cache,
            input_list=self.input_list,
            data_loaders=self.data_loaders,
        )

    def kill(self):
        """Stops the user process by force - to be called from signal handlers"""

        if self.message_handler is not None:
            self.message_handler.kill()
            return True

        return False
