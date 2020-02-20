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
experiment
==========

Validation for experiments
"""

import os
import collections
import itertools
import simplejson as json

from . import utils
from . import algorithm

from . import schema
from . import database
from . import toolchain
from . import hash

EVALUATOR_PREFIX = "evaluator_"
PROCESSOR_PREFIX = "processor_"


class Storage(utils.Storage):
    """Resolves paths for experiments

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The name of the experiment object in the format
        ``<user>/<toolchain-user>/<toolchain-name>/<version>/<name>`` or
        ``<user>/<toolchain-name>/<version>/<name>``, in case ``<user>`` and
        ``<toolchain-user>`` are the same.
    """

    asset_type = "experiment"
    asset_folder = "experiments"

    def __init__(self, prefix, name):

        if name.count(os.sep) not in (3, 4):
            raise RuntimeError("invalid experiment label: `%s'" % name)

        s = name.split(os.sep)
        if len(s) == 4:
            name = os.path.join(s[0], name)

        self.username, self.toolchain_username, self.toolchain, self.version, self.name = name.split(
            os.sep
        )

        self.label = name
        self.toolchain = os.path.join(
            self.toolchain_username, self.toolchain, self.version
        )
        self.prefix = prefix

        path = utils.hashed_or_simple(
            self.prefix, self.asset_folder, name, suffix=".json"
        )
        path = path[:-5]

        super(Storage, self).__init__(path)


class Experiment(object):
    """Experiments define the complete workflow for user test on the platform.

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (:py:class:`object`, Optional): The piece of data representing the
        experiment. It must validate against the schema defined for toolchains.
        If a string is passed, it is supposed to be a valid path to an
        experiment in the designated prefix area. If ``None`` is passed, loads
        our default prototype for toolchains. If a tuple is passed (or a list),
        then we consider that the first element represents the experiment,
        while the second, the toolchain definition. The toolchain bit can be
        defined as a dictionary or as a string (pointing to a valid path in the
        designated prefix area).

      dataformat_cache (:py:class:`dict`, Optional): A dictionary mapping
        dataformat names to loaded dataformats. This parameter is optional and,
        if passed, may greatly speed-up experiment loading times as dataformats
        that are already loaded may be re-used. If you use this parameter, you
        must guarantee that the cache is refreshed as appropriate in case the
        underlying dataformats change.

      database_cache (:py:class:`dict`, Optional): A dictionary mapping
        database names to loaded databases. This parameter is optional and, if
        passed, may greatly speed-up experiment loading times as databases that
        are already loaded may be re-used. If you use this parameter, you must
        guarantee that the cache is refreshed as appropriate in case the
        underlying databases change.

      algorithm_cache (:py:class:`dict`, Optional): A dictionary mapping
        algorithm names to loaded algorithms. This parameter is optional and,
        if passed, may greatly speed-up experiment loading times as algorithms
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

      label (str): The full, valid label of this experiment

      description (str): The short description string, loaded from the JSON
        file if one was set.

      documentation (str): The full-length docstring for this object.

      storage (object): A simple object that provides information about file
        paths for this toolchain

      toolchain (beat.core.toolchain.Toolchain): The toolchain in which this
        experiment is based.

      databases (dict): A dictionary containing the names and
        :py:class:`beat.core.database.Database` pointers for all referenced
        databases.

      algorithms (dict): A dictionary containing the names and
        :py:class:`beat.core.algorithm.Algorithm` pointers for all referenced
        algorithms.

      datasets (dict): A dictionary containing the names and
        :py:class:`beat.core.database.Database` pointers for all datasets in
        this experiment.

      blocks (dict): A dictionary containing the names and
        :py:class:`beat.core.algorithm.Algorithm` pointers for all blocks in
        this experiment.

      analyzers (dict): A dictionary containing the names and
        :py:class:`beat.core.algorithm.Algorithm` pointers for all analyzers in
        this experiment.

      errors (list): A list strings containing errors found while loading this
        experiment.

      data (dict): The original data for this experiment, as loaded by our JSON
        decoder.
    """

    def __init__(
        self,
        prefix,
        data,
        dataformat_cache=None,
        database_cache=None,
        algorithm_cache=None,
        library_cache=None,
    ):

        self.prefix = prefix

        # initializes the internal object cache
        self.toolchain = None

        self._label = None
        self.data = None
        self.errors = []
        self.storage = None
        self.datasets = {}
        self.blocks = {}
        self.loops = {}
        self.analyzers = {}

        self.databases = {}
        self.algorithms = {}

        # temporary caches, if the user has not set them, for performance
        database_cache = database_cache if database_cache is not None else {}
        dataformat_cache = dataformat_cache if dataformat_cache is not None else {}
        algorithm_cache = algorithm_cache if algorithm_cache is not None else {}
        library_cache = library_cache if library_cache is not None else {}

        self._load(
            data, database_cache, dataformat_cache, algorithm_cache, library_cache
        )

    def _load(
        self, data, database_cache, dataformat_cache, algorithm_cache, library_cache
    ):
        """Loads the experiment"""

        self._label = None
        self.data = None
        self.errors = []

        if data is None:  # Invalid case
            # There can't be a prototype for experiments they must be
            # filled based on the toolchain and the content of the prefix
            raise RuntimeError("Experiments can't have default implementation")

        elif isinstance(data, (tuple, list)):  # the user has passed a tuple

            experiment_data, toolchain_data = data

        else:  # the user has passed a path-like object

            self.storage = Storage(self.prefix, data)
            self._label = self.storage.label
            experiment_data = self.storage.json.path
            toolchain_data = self.storage.toolchain
            if not self.storage.exists():
                self.errors.append("Experiment declaration file not found: %s" % data)
                return

        # this runs basic validation, including JSON loading if required
        self.data, self.errors = schema.validate("experiment", experiment_data)
        if self.errors:
            return  # don't proceed with the rest of validation

        # checks all internal aspects of the experiment
        self._check_datasets(database_cache, dataformat_cache)
        self._check_blocks(algorithm_cache, dataformat_cache, library_cache)
        self._check_loops(algorithm_cache, dataformat_cache, library_cache)
        self._check_analyzers(algorithm_cache, dataformat_cache, library_cache)
        self._check_global_parameters()
        self._load_toolchain(toolchain_data)
        if self.errors:
            return  # stop, if up to here there were problems

        # cross-checks all aspects of the experiment against related toolchain
        self._crosscheck_toolchain_datasets()
        if self.errors:
            return

        self._crosscheck_toolchain_blocks()
        if self.errors:
            return

        self._crosscheck_toolchain_loops()
        if self.errors:
            return

        self._crosscheck_toolchain_analyzers()
        if self.errors:
            return

        self._crosscheck_connection_dataformats(dataformat_cache)
        if self.errors:
            return

        self._crosscheck_block_algorithm_pertinence()
        if self.errors:
            return

        self._crosscheck_loop_algorithm_pertinence()

    def _check_datasets(self, database_cache, dataformat_cache):
        """checks all datasets are valid"""

        for dataset, properties in self.data["datasets"].items():

            # loads the database
            dbname = properties["database"]
            if dbname not in self.databases:

                # load database
                if dbname in database_cache:
                    db = database_cache[dbname]
                else:
                    db = database.Database(self.prefix, dbname, dataformat_cache)
                    database_cache[dbname] = db

                self.databases[dbname] = db
                if db.errors:
                    self.errors.append(
                        "/datasets/%s: database `%s' is invalid" % (dataset, dbname)
                    )
                    continue
            else:
                db = self.databases[dbname]  # take a loaded value
                if db.errors:
                    continue  # already done

            # checks that the referred protocol is there
            protoname = properties["protocol"]
            if protoname not in db.protocols:
                self.errors.append(
                    "/datasets/%s: cannot find protocol `%s' on "
                    "database `%s' - valid protocols are %s"
                    % (dataset, protoname, dbname, ", ".join(db.protocols.keys()))
                )
                continue

            # finally, check if the referred set is inside the protocol
            setname = properties["set"]
            if setname not in db.sets(protoname):
                self.errors.append(
                    "/datasets/%s: cannot find set `%s' on "
                    "protocol `%s' from database `%s' - valid set names "
                    "are %s"
                    % (
                        dataset,
                        setname,
                        protoname,
                        dbname,
                        ", ".join(db.sets(protoname).keys()),
                    )
                )
                continue

            # if you get to this point, then adds the set to our cache
            self.datasets[dataset] = dict(database=db, protocol=protoname, set=setname)

    def _check_blocks(self, algorithm_cache, dataformat_cache, library_cache):
        """checks all blocks are valid"""

        for blockname, block in self.data["blocks"].items():

            algoname = block["algorithm"]
            if algoname not in self.algorithms:

                # loads the algorithm
                if algoname in algorithm_cache:
                    thisalgo = algorithm_cache[algoname]
                else:
                    thisalgo = algorithm.Algorithm(
                        self.prefix, algoname, dataformat_cache, library_cache
                    )
                    algorithm_cache[algoname] = thisalgo

                self.algorithms[algoname] = thisalgo
                if thisalgo.errors:
                    self.errors.append(
                        "/blocks/%s: algorithm `%s' is invalid: %s"
                        % (blockname, algoname, "\n".join(thisalgo.errors))
                    )
            else:
                thisalgo = self.algorithms[algoname]
                if thisalgo.errors:
                    continue  # already done

            # checks all inputs correspond
            for algoin, blockin in block["inputs"].items():
                if hasattr(thisalgo, "input_map") and algoin not in thisalgo.input_map:
                    self.errors.append(
                        "/blocks/%s/inputs/%s: algorithm `%s' does not "
                        "have an input named `%s' - valid algorithm inputs are %s"
                        % (
                            blockname,
                            blockin,
                            algoname,
                            algoin,
                            ", ".join(thisalgo.input_map.keys()),
                        )
                    )

            # checks all outputs correspond
            for algout, blockout in block["outputs"].items():
                if (
                    hasattr(thisalgo, "output_map")
                    and algout not in thisalgo.output_map
                ):
                    self.errors.append(
                        "/blocks/%s/outputs/%s: algorithm `%s' does not "
                        "have an output named `%s' - valid algorithm outputs are "
                        "%s"
                        % (
                            blockname,
                            blockout,
                            algoname,
                            algout,
                            ", ".join(thisalgo.output_map.keys()),
                        )
                    )

            # checks if parallelization make sense
            if block.get("nb_slots", 1) > 1 and not thisalgo.splittable:
                self.errors.append(
                    "/blocks/%s/nb_slots: you have set the number of "
                    "slots for algorithm `%s' to %d, but it is not splittable"
                    % (blockname, thisalgo.name, block["nb_slots"])
                )

            # check parameter consistence
            for parameter, value in block.get("parameters", {}).items():
                try:
                    thisalgo.clean_parameter(parameter, value)
                except Exception as e:
                    self.errors.append(
                        "/blocks/%s/parameters/%s: cannot convert "
                        "value `%s' to required type: %s"
                        % (blockname, parameter, value, e)
                    )

            self.blocks[blockname] = block

    def _check_loops(self, algorithm_cache, dataformat_cache, library_cache):
        """checks all loops are valid"""
        loops = self.data.get("loops", {})

        for loopname, loop in loops.items():
            for key in [PROCESSOR_PREFIX, EVALUATOR_PREFIX]:
                algoname = loop[key + "algorithm"]
                if algoname not in self.algorithms:

                    # loads the algorithm
                    if algoname in algorithm_cache:
                        thisalgo = algorithm_cache[algoname]
                    else:
                        thisalgo = algorithm.Algorithm(
                            self.prefix, algoname, dataformat_cache, library_cache
                        )
                        algorithm_cache[algoname] = thisalgo

                    self.algorithms[algoname] = thisalgo
                    if thisalgo.errors:
                        self.errors.append(
                            "/loops/%s: algorithm `%s' is invalid:\n%s"
                            % (loopname, algoname, "\n".join(thisalgo.errors))
                        )
                        continue

                else:
                    thisalgo = self.algorithms[algoname]
                    if thisalgo.errors:
                        continue  # already done

                # checks all inputs correspond
                for algoin, loop_input in loop[key + "inputs"].items():
                    if algoin not in thisalgo.input_map:
                        self.errors.append(
                            "/loop/%s/inputs/%s: algorithm `%s' does "
                            "not have an input named `%s' - valid algorithm inputs "
                            "are %s"
                            % (
                                loopname,
                                loop_input,
                                algoname,
                                algoin,
                                ", ".join(thisalgo.input_map.keys()),
                            )
                        )

                # checks all outputs correspond
                for algout, loop_output in loop[key + "outputs"].items():
                    if (
                        hasattr(thisalgo, "output_map")
                        and algout not in thisalgo.output_map
                    ):
                        self.errors.append(
                            "/loops/%s/outputs/%s: algorithm `%s' does not "
                            "have an output named `%s' - valid algorithm outputs are "
                            "%s"
                            % (
                                loopname,
                                loop_output,
                                algoname,
                                algout,
                                ", ".join(thisalgo.output_map.keys()),
                            )
                        )

            # checks if parallelization makes sense
            if loop.get("nb_slots", 1) > 1 and not thisalgo.splittable:
                self.errors.append(
                    "/loop/%s/nb_slots: you have set the number "
                    "of slots for algorithm `%s' to %d, but it is not "
                    "splittable" % (algoname, thisalgo.name, loop["nb_slots"])
                )

            # check parameter consistence
            for parameter, value in loop.get("parameters", {}).items():
                try:
                    thisalgo.clean_parameter(parameter, value)
                except Exception as e:
                    self.errors.append(
                        "/loop/%s/parameters/%s: cannot convert "
                        "value `%s' to required type: %s"
                        % (loopname, parameter, value, e)
                    )

            self.loops[loopname] = loop

    def _check_analyzers(self, algorithm_cache, dataformat_cache, library_cache):
        """checks all analyzers are valid"""

        for analyzername, analyzer in self.data["analyzers"].items():

            algoname = analyzer["algorithm"]
            if algoname not in self.algorithms:

                # loads the algorithm
                if algoname in algorithm_cache:
                    thisalgo = algorithm_cache[algoname]
                else:
                    thisalgo = algorithm.Algorithm(
                        self.prefix, algoname, dataformat_cache, library_cache
                    )
                    algorithm_cache[algoname] = thisalgo

                self.algorithms[algoname] = thisalgo
                if thisalgo.errors:
                    self.errors.append(
                        "/analyzers/%s: algorithm `%s' is invalid:\n%s"
                        % (analyzername, algoname, "\n".join(thisalgo.errors))
                    )
                    continue

            else:
                thisalgo = self.algorithms[algoname]
                if thisalgo.errors:
                    continue  # already done

            # checks all inputs correspond
            for algoin, analyzerin in analyzer["inputs"].items():
                if algoin not in thisalgo.input_map:
                    self.errors.append(
                        "/analyzers/%s/inputs/%s: algorithm `%s' does "
                        "not have an input named `%s' - valid algorithm inputs "
                        "are %s"
                        % (
                            analyzername,
                            analyzerin,
                            algoname,
                            algoin,
                            ", ".join(thisalgo.input_map.keys()),
                        )
                    )

            # checks if parallelization makes sense
            if analyzer.get("nb_slots", 1) > 1 and not thisalgo.splittable:
                self.errors.append(
                    "/analyzer/%s/nb_slots: you have set the number "
                    "of slots for algorithm `%s' to %d, but it is not "
                    "splittable" % (analyzername, thisalgo.name, analyzer["nb_slots"])
                )

            # check parameter consistence
            for parameter, value in analyzer.get("parameters", {}).items():
                try:
                    thisalgo.clean_parameter(parameter, value)
                except Exception as e:
                    self.errors.append(
                        "/analyzer/%s/parameters/%s: cannot convert "
                        "value `%s' to required type: %s"
                        % (analyzername, parameter, value, e)
                    )

            self.analyzers[analyzername] = analyzer

    def _check_global_parameters(self):
        """checks global parameters"""

        for algoname, parameters in self.data["globals"].items():
            if algoname in ["queue", "environment"]:
                continue  # skip that

            # else, algorithms must be loaded in memory already
            if algoname not in self.algorithms:
                self.errors.append(
                    "/globals/%s: found parameter section for "
                    "algorithm `%s' which is not used anywhere in the "
                    "experiment" % (algoname, algoname)
                )
                continue

            # ...and each parameter must validate
            thisalgo = self.algorithms[algoname]
            if not thisalgo.valid:
                continue  # doesn't even check
            for parameter, value in parameters.items():
                try:
                    thisalgo.clean_parameter(parameter, value)
                except Exception as e:
                    self.errors.append(
                        "/globals/%s/%s: cannot convert "
                        "value `%s' to required type: %s"
                        % (algoname, parameter, value, e)
                    )

    def _load_toolchain(self, data):
        """Loads the related toolchain"""

        # finally, we load the toolchain and cross-validate it
        self.toolchain = toolchain.Toolchain(self.prefix, data)

        if self.toolchain.errors:
            if self.storage is not None:
                self.errors.append(
                    "toolchain `%s' is not valid, because:\n  * %s"
                    % (self.storage.toolchain, "\n  * ".join(self.toolchain.errors))
                )
            else:
                self.errors.append(
                    "toolchain data is not valid, because:\n  * %s"
                    % "\n  * ".join(self.toolchain.errors)
                )
            return

    def _crosscheck_toolchain_datasets(self):
        """There must exist a 1-to-1 relation to existing datasets"""

        toolchain_datasets = self.toolchain.datasets

        if sorted(toolchain_datasets.keys()) != sorted(self.datasets.keys()):

            self.errors.append(
                "mismatch between the toolchain dataset names (%s)"
                " and the experiment's (%s)"
                % (
                    ", ".join(sorted(toolchain_datasets.keys())),
                    ", ".join(sorted(self.datasets.keys())),
                )
            )

        # toolchain must use a subset of the dataset endpoints
        for dataset_name, dataset in self.datasets.items():

            db_endpts = set(
                dataset["database"]
                .set(dataset["protocol"], dataset["set"])["outputs"]
                .keys()
            )
            tc_endpts = set(toolchain_datasets[dataset_name]["outputs"])

            if not tc_endpts.issubset(db_endpts):

                self.errors.append(
                    "/datasets/%s: toolchain endpoints (%s) must "
                    "be a subset of what is available on database `%s', "
                    "protocol `%s', "
                    "set `%s' outputs (%s)"
                    % (
                        dataset_name,
                        ", ".join(tc_endpts),
                        dataset["database"].name,
                        dataset["protocol"],
                        dataset["set"],
                        ", ".join(db_endpts),
                    )
                )

    def _crosscheck_toolchain_blocks(self):
        """There must exist a 1-to-1 relation to existing blocks"""

        toolchain_blocks = self.toolchain.blocks

        if sorted(toolchain_blocks.keys()) != sorted(self.blocks.keys()):

            self.errors.append(
                "mismatch between the toolchain block names (%s)"
                " and the experiment's (%s)"
                % (
                    ", ".join(sorted(toolchain_blocks.keys())),
                    ", ".join(sorted(self.blocks.keys())),
                )
            )

        # the number of block endpoints and the toolchain's must match
        for block_name, block in self.blocks.items():

            if len(block["inputs"]) != len(toolchain_blocks[block_name]["inputs"]):

                self.errors.append(
                    "/blocks/%s: toolchain blocks has %d inputs "
                    "while the experiment has %d inputs"
                    % (
                        block_name,
                        len(toolchain_blocks[block_name]["inputs"]),
                        len(block["inputs"]),
                    )
                )

    def _crosscheck_toolchain_loops(self):
        """There must exist a 1-to-1 relation to existing loops"""

        toolchain_loops = self.toolchain.loops

        if sorted(toolchain_loops.keys()) != sorted(self.loops.keys()):

            self.errors.append(
                "mismatch between the toolchain loop names (%s)"
                " and the experiment's (%s)"
                % (
                    ", ".join(sorted(toolchain_loops.keys())),
                    ", ".join(sorted(self.loops.keys())),
                )
            )

        # the number of block endpoints and the toolchain's must match
        for block_name, block in self.loops.items():
            for prefix in [PROCESSOR_PREFIX, EVALUATOR_PREFIX]:
                block_input_count = len(block[prefix + "inputs"])
                toolchain_input_block = len(
                    toolchain_loops[block_name][prefix + "inputs"]
                )
                if block_input_count != toolchain_input_block:

                    self.errors.append(
                        "/loops/{}: toolchain loops has {} {}inputs "
                        "while the experiment has {} inputs".format(
                            block_name, toolchain_input_block, prefix, block_input_count
                        )
                    )

    def _crosscheck_toolchain_analyzers(self):
        """There must exist a 1-to-1 relation to existing analyzers"""

        toolchain_analyzers = self.toolchain.analyzers

        if sorted(toolchain_analyzers.keys()) != sorted(self.analyzers.keys()):

            self.errors.append(
                "mismatch between the toolchain analyzer names "
                "(%s) and the experiment's (%s)"
                % (
                    ", ".join(sorted(toolchain_analyzers.keys())),
                    ", ".join(sorted(self.analyzers.keys())),
                )
            )

        # the number of analyzer endpoints and the toolchain's must match
        for analyzer_name, analyzer in self.analyzers.items():

            if len(analyzer["inputs"]) != len(
                toolchain_analyzers[analyzer_name]["inputs"]
            ):

                self.errors.append(
                    "/analyzers/%s: toolchain analyzers has %d "
                    "inputs while the experiment has %d inputs"
                    % (
                        analyzer_name,
                        len(toolchain_analyzers[analyzer_name]["inputs"]),
                        len(analyzer["inputs"]),
                    )
                )

    def _crosscheck_connection_dataformats(self, dataformat_cache):
        """Connected endpoints must use the same dataformat as defined by the
        generator and receptor algorithms
        """

        for connection in self.toolchain.connections:

            from_endpt = connection["from"].split(".", 1)

            if from_endpt[0] in self.datasets:
                dataset = self.datasets[from_endpt[0]]
                from_dtype = dataset["database"].set(
                    dataset["protocol"], dataset["set"]
                )["outputs"][from_endpt[1]]
                from_name = "dataset"

            elif from_endpt[0] in self.blocks:  # it is a block
                block = self.blocks[from_endpt[0]]
                mapping = block["outputs"]
                imapping = dict(zip(mapping.values(), mapping.keys()))
                algout = imapping[from_endpt[1]]  # name of output on algorithm
                from_dtype = self.algorithms[block["algorithm"]].output_map[algout]
                from_name = "block"

            elif from_endpt[0] in self.loops:
                loop = self.loops[from_endpt[0]]
                for prefix in [PROCESSOR_PREFIX, EVALUATOR_PREFIX]:
                    mapping = loop[prefix + "outputs"]
                    imapping = dict(zip(mapping.values(), mapping.keys()))
                    if from_endpt[1] in imapping:
                        algout = imapping[from_endpt[1]]  # name of output on algorithm
                        from_dtype = self.algorithms[
                            loop[prefix + "algorithm"]
                        ].output_map[algout]
                        break
                from_name = "loop"

            else:
                self.errors.append("Unknown endpoint %s" % from_endpt[0])
                continue

            to_endpt = connection["to"].split(".", 1)

            if to_endpt[0] in self.blocks:
                block = self.blocks[to_endpt[0]]
                mapping = block["inputs"]
                imapping = dict(zip(mapping.values(), mapping.keys()))
                algoin = imapping[to_endpt[1]]  # name of input on algorithm
                to_dtype = self.algorithms[block["algorithm"]].input_map[algoin]
                to_name = "block"

            elif to_endpt[0] in self.loops:
                loop = self.loops[to_endpt[0]]
                for prefix in [PROCESSOR_PREFIX, EVALUATOR_PREFIX]:
                    mapping = loop[prefix + "inputs"]
                    imapping = dict(zip(mapping.values(), mapping.keys()))
                    if to_endpt[1] in imapping:
                        algoin = imapping[to_endpt[1]]  # name of input on algorithm
                        to_dtype = self.algorithms[
                            loop[prefix + "algorithm"]
                        ].input_map[algoin]
                        break
                to_name = "loop"

            elif to_endpt[0] in self.analyzers:  # it is an analyzer
                analyzer = self.analyzers[to_endpt[0]]
                mapping = analyzer["inputs"]
                imapping = dict(zip(mapping.values(), mapping.keys()))
                algoin = imapping[to_endpt[1]]  # name of input on algorithm
                to_dtype = self.algorithms[analyzer["algorithm"]].input_map[algoin]
                to_name = "analyzer"
            else:
                self.errors.append("Unknown endpoint %s" % to_endpt[0])
                continue

            if from_dtype == to_dtype:
                continue  # OK

            # The other acceptable condition is that the receiving end is a
            #  subset of the producing end. This can happen if the producing end
            # is a subclass of the receiving end - that is, the receiving end
            # uses a data format that is a parent of the producing end.

            from_format = dataformat_cache[from_dtype]
            to_format = dataformat_cache[to_dtype]

            if to_format.isparent(from_format):
                continue  # OK

            # If you get to this point, then an error must be issued
            self.errors.append(
                "mismatch in data type at connection (%s) %s "
                "-> (%s) %s - start point uses `%s' while end point "
                "uses `%s' (must be equal or a parent format)"
                % (
                    from_name,
                    ".".join(from_endpt),
                    to_name,
                    ".".join(to_endpt),
                    from_dtype,
                    to_dtype,
                )
            )

    def _crosscheck_block_algorithm_pertinence(self):
        """The number of groups and the input-output connectivity must respect
        the individual synchronization channels and the block's.
        """

        for name, block in self.data["blocks"].items():

            # filter connections that end on the visited block - remember, each
            # input is checked for receiving a single input connection. It is
            # illegal to connect an input multiple times. At this point, you
            # already know that is not the case.
            input_connections = [
                k["channel"]
                for k in self.toolchain.connections
                if k["to"].startswith(name + ".")
            ]

            # filter connections that start on the visited block, retain output
            # name so we can check synchronization and then group
            output_connections = set(
                [
                    (k["from"].replace(name + ".", ""), k["channel"])
                    for k in self.toolchain.connections
                    if k["from"].startswith(name + ".")
                ]
            )

            output_connections = [k[1] for k in output_connections]

            # note: dataformats have already been checked - only need to check
            # for the grouping properties between inputs and outputs

            # create channel groups
            chain_in = collections.Counter(input_connections)
            chain_out = collections.Counter(output_connections)
            chain_groups = [(v, chain_out.get(k, 0)) for k, v in chain_in.items()]

            # now check the algorithm for conformance
            algo_groups = self.algorithms[self.blocks[name]["algorithm"]].groups
            algo_groups = [
                (len(k["inputs"]), len(k.get("outputs", []))) for k in algo_groups
            ]
            if collections.Counter(chain_groups) != collections.Counter(algo_groups):
                self.errors.append(
                    "synchronization mismatch in input/output "
                    "grouping between block `%s' and algorithm `%s'"
                    % (name, self.blocks[name]["algorithm"])
                )

    def _crosscheck_loop_algorithm_pertinence(self):
        """The number of groups and the input-output connectivity must respect
        the individual synchronization channels and the block's.
        """

        loops = self.data.get("loops", {})
        for name, loop in loops.items():

            # filter connections that end on the visited block - remember, each
            # input is checked for receiving a single input connection. It is
            # illegal to connect an input multiple times. At this point, you
            # already know that is not the case.
            input_connections = [
                k["channel"]
                for k in self.toolchain.connections
                if k["to"].startswith(name + ".")
            ]

            # filter connections that start on the visited block, retain output
            # name so we can check synchronization and then group
            output_connections = set(
                [
                    (k["from"].replace(name + ".", ""), k["channel"])
                    for k in self.toolchain.connections
                    if k["from"].startswith(name + ".")
                ]
            )

            output_connections = [k[1] for k in output_connections]

            # note: dataformats have already been checked - only need to check
            # for the grouping properties between inputs and outputs

            # create channel groups
            chain_in = collections.Counter(input_connections)
            chain_out = collections.Counter(output_connections)
            chain_groups_count = [(v, chain_out.get(k, 0)) for k, v in chain_in.items()]

            # now check the algorithms for conformance
            processor_algorithm_name = loop[PROCESSOR_PREFIX + "algorithm"]
            evaluator_algorithm_name = loop[EVALUATOR_PREFIX + "algorithm"]

            processor_algo_groups_list = self.algorithms[
                processor_algorithm_name
            ].groups
            evaluator_algo_groups_list = self.algorithms[
                evaluator_algorithm_name
            ].groups

            groups_count = []
            for processor_algo_groups, evaluator_algo_groups in itertools.zip_longest(
                processor_algo_groups_list, evaluator_algo_groups_list
            ):
                inputs = 0
                outputs = 0
                if processor_algo_groups:
                    inputs = len(processor_algo_groups["inputs"])
                    outputs = len(processor_algo_groups.get("outputs", []))

                if evaluator_algo_groups:
                    inputs += len(evaluator_algo_groups["inputs"])
                    outputs += len(evaluator_algo_groups.get("outputs", []))

                groups_count.append((inputs, outputs))

            if collections.Counter(chain_groups_count) != collections.Counter(
                groups_count
            ):
                self.errors.append(
                    "synchronization mismatch in input/output "
                    "grouping between loop `{}', algorithm `{}' "
                    "and loop algorithm `{}'".format(
                        name, processor_algorithm_name, evaluator_algorithm_name
                    )
                )

            for processor_algo_groups, evaluator_algo_groups in zip(
                processor_algo_groups_list, evaluator_algo_groups_list
            ):
                processor_algo_loop = processor_algo_groups["loop"]
                evaluator_algo_loop = evaluator_algo_groups["loop"]

                for channel in ["request", "answer"]:
                    if (
                        processor_algo_loop[channel]["type"]
                        != evaluator_algo_loop[channel]["type"]
                    ):
                        self.errors.append(
                            "{} loop channel type incompatible between {} and {}".format(
                                channel,
                                processor_algorithm_name,
                                evaluator_algorithm_name,
                            )
                        )

    def _crosscheck_analyzer_algorithm_pertinence(self):
        """
        The number of groups and the input-output connectivity must respect the
        individual synchronization channels and the analyzer.
        """

        for name, analyzer in self.data["analyzers"].items():

            # filter connections that end on the visited block
            input_connections = [
                k["channel"]
                for k in self.toolchain.connections
                if k["to"].startswith(name + ".")
            ]

            # note: dataformats have already been checked - only need to check
            # for the grouping properties for the inputs

            # create channel groups
            chain_groups = collections.Counter(input_connections)

            # now check the algorithm for conformance
            algo_groups = self.algorithms[self.analyzers[name]["algorithm"]].groups
            algo_groups = [len(k["inputs"]) for k in algo_groups]
            if collections.Counter(chain_groups) != collections.Counter(algo_groups):
                self.errors.append(
                    "synchronization mismatch in input "
                    "grouping between analyzer `%s' and algorithm `%s'"
                    % (name, self.analyzers[name]["algorithm"])
                )

    @property
    def label(self):
        """Returns the label of this experiment"""

        return self._label or "__unlabelled_experiment__"

    name = label  # compatiblity

    @label.setter
    def label(self, value):
        self._label = value
        self.storage = Storage(self.prefix, value)

    @property
    def schema_version(self):
        """Returns the schema version"""

        return self.data.get("schema_version", 1)

    @property
    def valid(self):
        """A boolean that indicates if this experiment is valid or not"""

        return not bool(self.errors)

    def _inputs(self, name, input_prefix=""):
        """Calculates and returns the inputs for a given block"""

        # filter connections that end on the visited block
        _connections = [
            k for k in self.toolchain.connections if k["to"].startswith(name + ".")
        ]

        # organize the connections into a map: block input name -> from key
        connections = dict(
            [
                (
                    k["to"].replace(name + ".", ""),
                    tuple(k["from"].split(".", 1) + [k["channel"]]),
                )
                for k in _connections
            ]
        )

        # makes sure we don't have multiple incomming connections
        assert len(_connections) == len(connections), (  # nosec
            "detected multiple input "
            "connections for block `%s' on experiment `%s'" % (name, self.label)
        )

        retval = dict()

        # config_data = self.blocks.get(name, self.analyzers.get(name))
        for item in [self.blocks, self.loops, self.analyzers]:
            if name in item:
                config_data = item[name]
                break

        if config_data is None:
            raise KeyError("did not find `%s' among blocks, loops or analyzers" % name)

        # if get_loop_data:
        #     inputs = config_data[EVALUATOR_PREFIX + "inputs"]
        # else:
        #     inputs = config_data[PROCESSOR_PREFIX + "inputs"]
        inputs = config_data[input_prefix + "inputs"]

        for algo_endpt, block_endpt in inputs.items():
            block, output, channel = connections[block_endpt]

            if block in self.toolchain.datasets:

                dataset_config = self.datasets[block]
                retval[algo_endpt] = dict(
                    database=dataset_config["database"].name,
                    protocol=dataset_config["protocol"],
                    set=dataset_config["set"],
                    output=output,  # dataset output name always matches block's!
                    endpoint=block_endpt,  # the block intake name
                    channel=channel,
                    hash=hash.hashDataset(
                        dataset_config["database"].name,
                        dataset_config["protocol"],
                        dataset_config["set"],
                    ),
                )

                # the path in the cache is calculated from the hash
                retval[algo_endpt]["path"] = hash.toPath(
                    retval[algo_endpt]["hash"], suffix=".db"
                )

            else:  # a normal block

                # Here comes the trick: block hashes cannot be easily generated
                # - they require the input hashes to be adequately generated.
                # The way forward is to gather all inputs **and** outputs and
                # then go one by one generating the input **and** output hashes
                # until all is done.

                retval[algo_endpt] = {
                    "from": "%s.%s" % (block, output),
                    "channel": channel,
                    "endpoint": block_endpt,  # the block intake name
                }

        return retval

    def _block_outputs(self, name, output_prefix=""):
        """Calculates and returns the outputs for a given block"""

        for item in [self.blocks, self.loops]:
            if name in item:
                config_data = item[name]
                break

        if config_data is None:
            raise KeyError("did not find `%s' among blocks or loops" % name)

        # filter connections that end on the visited block
        connections = [
            k for k in self.toolchain.connections if k["from"].startswith(name + ".")
        ]

        # organize the connections into a map: block input name -> from key
        connections = dict(
            [
                (
                    k["from"].replace(name + ".", ""),
                    tuple(k["to"].split(".", 1) + [k["channel"]]),
                )
                for k in connections
            ]
        )

        retval = dict()

        # notice: there can be multiply connected outputs
        # if get_loop_data:
        #     outputs = config_data[EVALUATOR_PREFIX + "outputs"]
        # else:
        #     outputs = config_data[PROCESSOR_PREFIX + "outputs"]
        outputs = config_data[output_prefix + "outputs"]

        for algo_endpt, block_endpt in outputs.items():
            block, input, channel = connections[block_endpt]
            retval[algo_endpt] = dict(
                channel=channel, endpoint=block_endpt  # the block outtake name
            )

        return retval

    def _configuration(self, name):
        """Returns the execution configuration for a particular block

        This method returns the (JSON) configuration for a particular block in
        this experiment. This configuration is sent to worker nodes when the
        platform wants to command the execution of a particular algorithm.

        The variable ``blocks`` from this object contains a dictionary with all
        block names as keys.

        Parameters:

          name (str): The name of the block from which to get the configuration
            of. If the block does not exist, raises a :py:class:`KeyError`.


        Raises:

          KeyError: if the block name does not exist in this experiment.
        """

        for item in [self.blocks, self.loops, self.analyzers]:
            if name in item:
                config_data = item[name]
                break

        # resolve the execution information
        queue = config_data.get("queue", self.data["globals"]["queue"])
        nb_slots = config_data.get("nb_slots", 1)

        toolchain_data = self.toolchain.algorithm_item(name)

        if toolchain_data is None:
            raise KeyError("did not find `%s' among blocks, loops or analyzers" % name)

        if name in self.loops:

            def build_block_data(name, config_data, algorithm_prefix):
                # resolve parameters taking globals in consideration
                algorithm_name = config_data[algorithm_prefix + "algorithm"]

                parameters = self.data["globals"].get(algorithm_name)
                if parameters is None:
                    parameters = dict()
                else:
                    parameters = dict(parameters)  # copy

                parameters.update(config_data.get(algorithm_prefix + "parameters", {}))

                environment = config_data.get(
                    algorithm_prefix + "environment",
                    self.data["globals"]["environment"],
                )

                return dict(
                    inputs=self._inputs(name, algorithm_prefix),
                    outputs=self._block_outputs(name, algorithm_prefix),
                    channel=toolchain_data["synchronized_channel"],
                    algorithm=algorithm_name,
                    parameters=parameters,
                    queue=queue,
                    environment=environment,
                )

            retval = build_block_data(name, config_data, PROCESSOR_PREFIX)
            retval["nb_slots"] = nb_slots
            retval["loop"] = build_block_data(name, config_data, EVALUATOR_PREFIX)

        else:
            env = config_data.get("environment", self.data["globals"]["environment"])
            # resolve parameters taking globals in consideration

            parameters = self.data["globals"].get(config_data["algorithm"])
            if parameters is None:
                parameters = dict()
            else:
                parameters = dict(parameters)  # copy

            parameters.update(config_data.get("parameters", {}))

            retval = dict(
                inputs=self._inputs(name),
                channel=toolchain_data["synchronized_channel"],
                algorithm=config_data["algorithm"],
                parameters=parameters,
                queue=queue,
                environment=env,
                nb_slots=nb_slots,
            )

            if name in self.blocks:
                retval["outputs"] = self._block_outputs(name)
            else:
                # Analyzers have only 1 output file/cache. This is the result of an
                # optimization as most of the outputs are single numbers.
                # Furthermore, given we need to read it out on beat.web, having a
                # single file optimizes resource usage. The synchronization channel
                # for the analyzer itself is respected.
                retval["result"] = dict()  # missing the hash/path

        return retval

    def setup(self):
        """Prepares the experiment so it can be executed by a scheduling
        service.

        This method will calculate the block execution order and prepare the
        configuration for each block in the experiment so its execution can be
        carried out by an adequate scheduling service.

        Returns:

          collections.OrderedDict: An ordered dictionary with the
            block/analyzer execution order and configuration details. The keys
            of this ordered dictionary correspond to the block and analyzer
            names in the toolchain. The values correspond to a list of
            dependencies for the given block in terms of other block names and
            the block/analyzer configuration, as a dictionary.
        """

        exec_order = self.toolchain.execution_order()

        for key in exec_order:
            exec_order[key] = dict(
                dependencies=exec_order[key], configuration=self._configuration(key)
            )

        # import ipdb; ipdb.set_trace()
        for key, value in exec_order.items():
            # now compute missing hashes - because we're in execution order,
            # there should be no missing input hashes in any of the blocks.
            config = value["configuration"]
            if "outputs" in config:  # it is a block

                def process_config(config):
                    block_outputs = {}
                    for output, output_value in config["outputs"].items():
                        output_value["hash"] = hash.hashBlockOutput(
                            key,
                            config["algorithm"],
                            self.algorithms[config["algorithm"]].hash(),
                            config["parameters"],
                            config["environment"],
                            dict([(k, v["hash"]) for k, v in config["inputs"].items()]),
                            output,
                        )
                        output_value["path"] = hash.toPath(output_value["hash"], "")

                        # set the inputs for the following blocks
                        block_outputs[
                            "%s.%s" % (key, output_value["endpoint"])
                        ] = output_value

                    dependents = [
                        exec_order[k]["configuration"]
                        for k in exec_order
                        if key in exec_order[k]["dependencies"]
                    ]

                    # updates inputs which have not yet been updated
                    for dependent in dependents:

                        def process_inputs(inputs):
                            for input_name, input_value in inputs.items():
                                if input_value.get("from") in block_outputs.keys():
                                    input_value["hash"] = block_outputs[
                                        input_value.get("from")
                                    ]["hash"]
                                    input_value["path"] = block_outputs[
                                        input_value.get("from")
                                    ]["path"]
                                    del input_value[
                                        "from"
                                    ]  # no need for further update

                        inputs = dependent["inputs"]
                        process_inputs(inputs)
                        if "loop" in dependent:
                            process_inputs(dependent["loop"]["inputs"])

                process_config(config)
                if "loop" in config:
                    process_config(config["loop"])
            else:  # it is an analyzer: 1 single output
                config["result"]["hash"] = hash.hashAnalyzer(
                    key,
                    config["algorithm"],
                    self.algorithms[config["algorithm"]].hash(),
                    config["parameters"],
                    config["environment"],
                    dict([(k, v["hash"]) for k, v in config["inputs"].items()]),
                )
                config["result"]["path"] = hash.toPath(config["result"]["hash"], "")

        return exec_order

    def dot_diagram(self):
        """Returns a dot diagram representation of the experiment"""

        title = "Experiment: %s" % self.label

        def __label_callback(type, name):
            """Adds experiment information to the given block"""

            if type == "dataset":
                info = self.datasets[name]
                return "<b><u>%s</u></b><br/>%s<br/><i>%s:%s</i>" % (
                    name,
                    info["database"].name,
                    info["protocol"],
                    info["set"],
                )
            elif type == "block":
                info = self.blocks[name]
                env = info.get("environment", self.data["globals"]["environment"])
                nb_slots = info.get("nb_slots", 1)
                return "<b><u>%s</u></b><br/>%s<br/><i>@%s(%s) x %d</i>" % (
                    name,
                    info["algorithm"],
                    env["name"],
                    env["version"],
                    nb_slots,
                )
            elif type == "analyzer":
                info = self.analyzers[name]
                env = info.get("environment", self.data["globals"]["environment"])
                nb_slots = info.get("nb_slots", 1)
                return "<b><u>%s</u></b><br/>%s<br/><i>@%s(%s) x %d</i>" % (
                    name,
                    info["algorithm"],
                    env["name"],
                    env["version"],
                    nb_slots,
                )  # , ports)
            else:
                return name

        def __result_callback(name):
            """Adds result information to analyzers"""

            def __mkport(k, v):
                name = k if not v["display"] else "+" + k
                return "%s<br/>(%s)" % (name, v["type"])

            info = self.analyzers[name]
            results = self.algorithms[info["algorithm"]].results
            return [__mkport(k, v) for k, v in results.items()]

        def __edge_callback(start):
            """Adds the datatype to the given block"""

            block, endpoint = start.split(".", 1)
            if block in self.datasets:
                db = self.datasets[block]
                dbset = db["database"].set(db["protocol"], db["set"])
                return dbset["outputs"][endpoint]
            else:
                forward_mapping = self.blocks[block]["outputs"]
                reverse_mapping = dict((v, k) for k, v in forward_mapping.items())
                algo_output = reverse_mapping[endpoint]
                algo = self.algorithms[self.blocks[block]["algorithm"]]
                return algo.output_map[algo_output]

        return self.toolchain.dot_diagram(
            title, __label_callback, __edge_callback, __result_callback
        )

    @property
    def description(self):
        """The short description for this object"""

        return self.data.get("description", None)

    @description.setter
    def description(self, value):
        """Sets the short description for this object"""

        self.data["description"] = value

    @property
    def documentation(self):
        """The full-length description for this object"""

        if not self._label:
            raise RuntimeError("experiment has no label")

        if self.storage.doc.exists():
            return self.storage.doc.load()
        return None

    @documentation.setter
    def documentation(self, value):
        """Sets the full-length description for this object"""

        if not self._label:
            raise RuntimeError("experiment has no label")

        if hasattr(value, "read"):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)

    def hash(self):
        """Returns the hexadecimal hash for its declaration"""

        if not self._label:
            raise RuntimeError("experiment has no label")

        return self.storage.hash()

    def json_dumps(self, indent=4):
        """Dumps the JSON declaration of this object in a string


        Parameters:

          indent (int): The number of indentation spaces at every indentation
          level


        Returns:

          str: The JSON representation for this object
        """

        return json.dumps(self.data, indent=indent, cls=utils.NumpyJSONEncoder)

    def __str__(self):

        return self.json_dumps()

    def write(self, storage=None):
        """Writes contents to prefix location

        Parameters:

          storage (:py:class:`.Storage`, Optional): If you pass a new storage,
            then this object will be written to that storage point rather than
            its default.
        """

        if storage is None:
            if not self._label:
                raise RuntimeError("experiment has no label")
            storage = self.storage  # overwrite

        storage.save(str(self), self.description)

    def export(self, prefix):
        """Recursively exports itself into another prefix

        Databases and algorithms associated are also exported recursively


        Parameters:

          prefix (str): A path to a prefix that must different then my own.


        Returns:

          None


        Raises:

          RuntimeError: If prefix and self.prefix point to the same directory.
        """

        if not self._label:
            raise RuntimeError("experiment has no label")

        if not self.valid:
            raise RuntimeError("experiment is not valid")

        if prefix == self.prefix:
            raise RuntimeError(
                "Cannot export experiment to the same prefix (" "%s)" % (prefix)
            )

        self.toolchain.write(toolchain.Storage(prefix, self.toolchain.name))

        for k in self.algorithms.values():
            k.export(prefix)

        for k in self.databases.values():
            k.export(prefix)

        self.write(Storage(prefix, self.name))
