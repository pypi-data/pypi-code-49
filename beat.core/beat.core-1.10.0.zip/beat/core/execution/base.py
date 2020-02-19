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
base
====

Execution utilities
"""


import os
import glob
import collections
import logging
import simplejson as json

from .. import schema
from .. import database
from .. import algorithm
from .. import stats

from beat.backend.python.helpers import convert_experiment_configuration_to_container


logger = logging.getLogger(__name__)


class BaseExecutor(object):
    """Executors runs the code given an execution block information


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
        cache=None,
        dataformat_cache=None,
        database_cache=None,
        algorithm_cache=None,
        library_cache=None,
        custom_root_folders=None,
    ):

        # Initialisations
        self.prefix = prefix
        self.cache = cache or os.path.join(self.prefix, "cache")
        self.algorithm = None
        self.loop_algorithm = None
        self.databases = {}
        self.input_list = None
        self.data_loaders = None
        self.output_list = None
        self.data_sinks = []
        self.errors = []
        self.data = data
        self.debug = False

        # Check that the cache path exists
        if not os.path.exists(self.cache):
            raise IOError("Cache path `%s' does not exist" % self.cache)

        # Check the custom root folders
        if custom_root_folders is not None:
            if not isinstance(custom_root_folders, collections.Mapping):
                raise TypeError("The custom root folders must be in dictionary format")
        else:
            custom_root_folders = {}

        # Temporary caches, if the user has not set them, for performance
        database_cache = database_cache if database_cache is not None else {}
        dataformat_cache = dataformat_cache if dataformat_cache is not None else {}
        algorithm_cache = algorithm_cache if algorithm_cache is not None else {}
        library_cache = library_cache if library_cache is not None else {}

        # Basic validation of the data declaration, including JSON loading if required
        if not isinstance(data, dict):
            if not os.path.exists(data):
                self.errors.append("File not found: %s" % data)
                return

        self.data, self.errors = schema.validate("execution", data)
        if self.errors:
            return

        # Load the algorithm (using the algorithm cache if possible)
        if self.data["algorithm"] in algorithm_cache:
            self.algorithm = algorithm_cache[self.data["algorithm"]]
        else:
            self.algorithm = algorithm.Algorithm(
                self.prefix, self.data["algorithm"], dataformat_cache, library_cache
            )
            algorithm_cache[self.algorithm.name] = self.algorithm

        if not self.algorithm.valid:
            self.errors += self.algorithm.errors
            return

        if "loop" in self.data:
            loop = self.data["loop"]
            if loop["algorithm"] in algorithm_cache:
                self.loop_algorithm = algorithm_cache[loop["algorithm"]]
            else:
                self.loop_algorithm = algorithm.Algorithm(
                    self.prefix, loop["algorithm"], dataformat_cache, library_cache
                )
                algorithm_cache[self.loop_algorithm.name] = self.loop_algorithm

                if len(loop["inputs"]) != len(self.loop_algorithm.input_map):
                    self.errors.append(
                        "The number of inputs of the loop algorithm doesn't correspond"
                    )

                for name in self.data["inputs"].keys():
                    if name not in self.algorithm.input_map.keys():
                        self.errors.append(
                            "The input '%s' doesn't exist in the loop algorithm" % name
                        )

                if len(loop["outputs"]) != len(self.loop_algorithm.output_map):
                    self.errors.append(
                        "The number of outputs of the loop algorithm doesn't correspond"
                    )

                for name in self.data["outputs"].keys():
                    if name not in self.algorithm.output_map.keys():
                        self.errors.append(
                            "The output '%s' doesn't exist in the loop algorithm" % name
                        )

        # Check that the mapping in coherent
        if len(self.data["inputs"]) != len(self.algorithm.input_map):
            self.errors.append(
                "The number of inputs of the algorithm doesn't correspond"
            )

        if "outputs" in self.data and (
            len(self.data["outputs"]) != len(self.algorithm.output_map)
        ):
            self.errors.append(
                "The number of outputs of the algorithm doesn't correspond"
            )

        for name in self.data["inputs"].keys():
            if name not in self.algorithm.input_map.keys():
                self.errors.append(
                    "The input '%s' doesn't exist in the algorithm" % name
                )

        if "outputs" in self.data:
            for name in self.data["outputs"].keys():
                if name not in self.algorithm.output_map.keys():
                    self.errors.append(
                        "The output '%s' doesn't exist in the algorithm" % name
                    )

        if "loop" in self.data:
            for name in ["request", "answer"]:
                if name not in self.algorithm.loop_map.keys():
                    self.errors.append(
                        "The loop '%s' doesn't exist in the algorithm" % name
                    )

        if self.errors:
            return

        # Load the databases (if any is required)
        self._update_db_cache(
            self.data["inputs"], custom_root_folders, database_cache, dataformat_cache
        )

        if "loop" in self.data:
            self._update_db_cache(
                self.data["loop"]["inputs"],
                custom_root_folders,
                database_cache,
                dataformat_cache,
            )

    def __enter__(self):
        """Prepares inputs and outputs for the processing task

        Raises:

          IOError: in case something cannot be properly setup

        """

        logger.info("Start the execution of '%s'", self.algorithm.name)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Closes all sinks and disconnects inputs and outputs
        """

        for sink in self.data_sinks:
            # we save the output only if no valid error has been thrown
            # n.b.: a system exit will raise SystemExit which is not an Exception
            if not isinstance(exc_type, Exception):
                sink.close()

        self.input_list = None
        self.data_loaders = []
        self.output_list = None
        self.data_sinks = []

    def _update_db_cache(
        self, inputs, custom_root_folders, database_cache, dataformat_cache
    ):
        """ Update the database cache based on the input list given"""

        for name, details in inputs.items():
            if "database" in details:

                if details["database"] not in self.databases:

                    if details["database"] in database_cache:
                        db = database_cache[details["database"]]
                    else:
                        db = database.Database(
                            self.prefix, details["database"], dataformat_cache
                        )

                        name = "database/%s" % db.name
                        if name in custom_root_folders:
                            db.data["root_folder"] = custom_root_folders[name]

                        database_cache[db.name] = db

                    self.databases[db.name] = db

                    if not db.valid:
                        self.errors += db.errors

    def _prepare_inputs(self):
        """Prepares all input required by the execution."""

        raise NotImplementedError()

    def _prepare_outputs(self):
        """Prepares all output required by the execution."""

        raise NotImplementedError()

    def process(
        self, virtual_memory_in_megabytes=0, max_cpu_percent=0, timeout_in_minutes=0
    ):
        """Executes the user algorithm code

        Parameters:

          virtual_memory_in_megabytes (:py:class:`int`, Optional): The amount
            of virtual memory (in Megabytes) available for the job. If set to
            zero, no limit will be applied.

          max_cpu_percent (:py:class:`int`, Optional): The maximum amount of
            CPU usage allowed in a system. This number must be an integer
            number between 0 and ``100*number_of_cores`` in your system. For
            instance, if your system has 2 cores, this number can go between 0
            and 200. If it is <= 0, then we don't track CPU usage.

          timeout_in_minutes (int): The number of minutes to wait for the user
            process to execute. After this amount of time, the user process is
            killed with ``signal.SIGKILL``. If set to zero, no timeout will be
            applied.

        Returns:

          dict: A dictionary which is JSON formattable containing the summary of
            this block execution.

        """

        raise NotImplementedError()

    @property
    def valid(self):
        """A boolean that indicates if this executor is valid or not"""

        return not bool(self.errors)

    @property
    def analysis(self):
        """A boolean that indicates if the current block is an analysis block"""
        return "result" in self.data

    @property
    def outputs_exist(self):
        """Returns ``True`` if outputs this block is supposed to produce exists."""

        if self.analysis:
            path = os.path.join(self.cache, self.data["result"]["path"]) + "*"
            if not glob.glob(path):
                return False

        else:
            for name, details in self.data["outputs"].items():
                path = os.path.join(self.cache, details["path"]) + "*"
                if not glob.glob(path):
                    return False

        # if you get to this point all outputs already exist
        return True

    @property
    def io_statistics(self):
        """Summarize current I/O statistics looking at data sources and sinks, inputs and outputs

        Returns:

          dict: A dictionary summarizing current I/O statistics
        """

        return stats.io_statistics(self.data, self.input_list, self.output_list)

    def __str__(self):
        return json.dumps(self.data, indent=4)

    def write(self, path):
        """Writes contents to precise filesystem location"""

        with open(path, "wt") as f:
            f.write(str(self))

    def dump_runner_configuration(self, directory):
        """Exports contents useful for a backend runner to run the algorithm"""

        data = convert_experiment_configuration_to_container(self.data)

        with open(os.path.join(directory, "configuration.json"), "wb") as f:
            json_data = json.dumps(data, indent=2)
            f.write(json_data.encode("utf-8"))

        tmp_prefix = os.path.join(directory, "prefix")
        if not os.path.exists(tmp_prefix):
            os.makedirs(tmp_prefix)

        self.algorithm.export(tmp_prefix)

        if self.loop_algorithm:
            self.loop_algorithm.export(tmp_prefix)

    def dump_databases_provider_configuration(self, directory):
        """Exports contents useful for a backend runner to run the algorithm"""

        with open(os.path.join(directory, "configuration.json"), "wb") as f:
            json_data = json.dumps(self.data, indent=2)
            f.write(json_data.encode("utf-8"))

        tmp_prefix = os.path.join(directory, "prefix")
        if not os.path.exists(tmp_prefix):
            os.makedirs(tmp_prefix)

        for db in self.databases.values():
            db.export(tmp_prefix)
