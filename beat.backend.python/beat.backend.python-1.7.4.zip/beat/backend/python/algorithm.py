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
=========
algorithm
=========

Validation for algorithms
"""

import os
import sys
import logging

import six
import numpy
import simplejson as json

from . import dataformat
from . import library
from . import loader
from . import utils


logger = logging.getLogger(__name__)


# ----------------------------------------------------------


class Storage(utils.CodeStorage):
    """Resolves paths for algorithms

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The name of the algorithm object in the format
        ``<user>/<name>/<version>``.

    """

    asset_type = "algorithm"
    asset_folder = "algorithms"

    def __init__(self, prefix, name, language=None):

        if name.count("/") != 2:
            raise RuntimeError("invalid algorithm name: `%s'" % name)

        self.username, self.name, self.version = name.split("/")
        self.fullname = name
        self.prefix = prefix

        path = utils.hashed_or_simple(
            self.prefix, self.asset_folder, name, suffix=".json"
        )
        path = path[:-5]
        super(Storage, self).__init__(path, language)


# ----------------------------------------------------------


class Runner(object):
    """A special loader class for algorithms, with specialized methods

    Parameters:

      module (:std:term:`module`): The preloaded module containing the
        algorithm as returned by :py:func:`.loader.load_module`.

      obj_name (str): The name of the object within the module you're
        interested on

      algorithm (object): The algorithm instance that is used for parameter
        checking.

      exc (:std:term:`class`): The class to use as base exception when
        translating the exception from the user code. Read the documentation of
        :py:func:`.loader.run` for more details.

    """

    def __init__(self, module, obj_name, algorithm, exc=None):

        try:
            class_ = getattr(module, obj_name)
        except Exception:
            if exc is not None:
                type, value, traceback = sys.exc_info()
                six.reraise(exc, exc(value), traceback)
            else:
                raise  # Just re-raise the user exception

        self.obj = loader.run(class_, "__new__", exc)
        self.name = module.__name__
        self.algorithm = algorithm
        self.exc = exc

        self.ready = not hasattr(self.obj, "setup")

        has_api_v1 = self.algorithm.api_version == 1
        has_prepare = hasattr(self.obj, "prepare")

        self.prepared = has_api_v1 or not has_prepare

        if has_api_v1 and has_prepare:
            logger.warning("Prepare is a reserved function name starting with API V2")

    def _check_parameters(self, parameters):
        """Checks input parameters from the user and fill defaults"""

        user_keys = set(parameters.keys())
        algo_parameters = self.algorithm.parameters or {}
        valid_keys = set(algo_parameters.keys())

        # Checks the user is not trying to set an undeclared parameter
        if not user_keys.issubset(valid_keys):
            err_keys = user_keys - valid_keys
            message = (
                "parameters `%s' are not declared for algorithm `%s' - "
                "valid parameters are `%s'"
                % (",".join(err_keys), self.name, ",".join(valid_keys))
            )
            exc = self.exc or KeyError
            raise exc(message)

        retval = dict()

        for key, definition in algo_parameters.items():

            if key in parameters:
                try:
                    value = self.algorithm.clean_parameter(key, parameters[key])
                except Exception as e:
                    message = (
                        "parameter `%s' cannot be safely cast to the declared "
                        "type on algorithm `%s': %s" % (key, self.name, e)
                    )
                    exc = self.exc or ValueError
                    raise exc(message)

            else:  # User has not set a value, use the default
                value = algo_parameters[key]["default"]

            # In the end, set the value on the dictionary to be returned
            retval[key] = value

        return retval

    def setup(self, parameters):
        """Sets up the algorithm, only effective on the first call"""

        # Only effective on the first call
        if self.ready:
            return self.ready

        completed_parameters = self._check_parameters(parameters)

        self.ready = loader.run(self.obj, "setup", self.exc, completed_parameters)
        return self.ready

    def prepare(self, data_loaders):
        """Let the algorithm process the data on the non-principal channels"""

        # Only effective on the first call
        if self.prepared:
            return self.prepared

        # setup() must have run
        if not self.ready:
            exc = self.exc or RuntimeError
            raise exc("Algorithm '%s' is not yet setup" % self.name)

        # Not available in API version 1
        if self.algorithm.api_version == 1:
            self.prepared = True
            return True

        # The method is optional
        if hasattr(self.obj, "prepare"):
            if self.algorithm.type in [
                Algorithm.AUTONOMOUS,
                Algorithm.AUTONOMOUS_LOOP_PROCESSOR,
            ]:
                self.prepared = loader.run(
                    self.obj, "prepare", self.exc, data_loaders.secondaries()
                )
            else:
                self.prepared = loader.run(self.obj, "prepare", self.exc, data_loaders)
        else:
            self.prepared = True

        return self.prepared

    def process(
        self,
        inputs=None,
        data_loaders=None,
        outputs=None,
        output=None,
        loop_channel=None,
    ):
        """Runs through data"""

        exc = self.exc or RuntimeError

        def _check_argument(argument, name):
            if argument is None:
                raise exc("Missing argument: %s" % name)

        # setup() must have run
        if not self.ready:
            raise exc("Algorithm '%s' is not yet setup" % self.name)

        # prepare() must have run
        if not self.prepared:
            raise exc("Algorithm '%s' is not yet prepared" % self.name)

        # Call the correct version of process()
        if self.algorithm.isAnalyzer:
            _check_argument(output, "output")
            outputs_to_use = output
        else:
            _check_argument(outputs, "outputs")
            outputs_to_use = outputs

        if self.algorithm.type == Algorithm.LEGACY:
            _check_argument(inputs, "inputs")
            return loader.run(self.obj, "process", self.exc, inputs, outputs_to_use)

        else:
            _check_argument(data_loaders, "data_loaders")

            if self.algorithm.is_sequential:
                _check_argument(inputs, "inputs")

                run_args = [
                    self.obj,
                    "process",
                    self.exc,
                    inputs,
                    data_loaders,
                    outputs_to_use,
                ]

            elif self.algorithm.is_autonomous:
                run_args = [self.obj, "process", self.exc, data_loaders, outputs_to_use]

            else:
                raise exc("Unknown algorithm type: %s" % self.algorithm.type)

            has_loop_arg = utils.has_argument(self.obj.process, "loop_channel")
            if loop_channel is not None:
                if has_loop_arg:
                    run_args.append(loop_channel)
                else:
                    raise exc(
                        "Algorithm '%s' is not a valid loop enabled algorithm"
                        % self.name
                    )
            elif has_loop_arg:
                raise exc(
                    "Algorithm '%s' is a loop enabled algorithm but no loop_channel given"
                    % self.name
                )

            return loader.run(*run_args)

    def validate(self, result):
        """Validates the given results"""

        exc = self.exc or RuntimeError

        if not self.algorithm.is_loop:
            raise exc("Wrong algorithm type: %s" % self.algorithm.type)

        # setup() must have run
        if not self.ready:
            raise exc("Algorithm '%s' is not yet setup" % self.name)

        # prepare() must have run
        if not self.prepared:
            raise exc("Algorithm '%s' is not yet prepared" % self.name)

        answer = loader.run(self.obj, "validate", self.exc, result)

        if not isinstance(answer, tuple):
            raise exc("Improper implementation: validate must return a tuple")

        return answer

    def write(self, outputs, processor_output_name, end_data_index):
        """Write to the outputs"""

        exc = self.exc or RuntimeError

        if not self.algorithm.is_loop:
            raise exc("Wrong algorithm type: %s" % self.algorithm.type)

        # setup() must have run
        if not self.ready:
            raise exc("Algorithm '%s' is not yet setup" % self.name)

        # prepare() must have run
        if not self.prepared:
            raise exc("Algorithm '%s' is not yet prepared" % self.name)

        return loader.run(
            self.obj, "write", self.exc, outputs, processor_output_name, end_data_index
        )

    def read(self, inputs):
        """Triggers a read of the inputs

        This is used by the loop when used in conjunction with a sequential
        loop user.
        """

        exc = self.exc or RuntimeError

        if not self.algorithm.is_loop:
            raise exc("Wrong algorithm type: %s" % self.algorithm.type)

        # setup() must have run
        if not self.ready:
            raise exc("Algorithm '%s' is not yet setup" % self.name)

        # prepare() must have run
        if not self.prepared:
            raise exc("Algorithm '%s' is not yet prepared" % self.name)

        return loader.run(self.obj, "read", self.exc, inputs)

    def __getattr__(self, key):
        """Returns an attribute of the algorithm - only called at last resort
        """
        return getattr(self.obj, key)


# ----------------------------------------------------------


class Algorithm(object):
    """Algorithms represent runnable components within the platform.

    This class can only parse the meta-parameters of the algorithm (i.e., input
    and output declaration, grouping, synchronization details, parameters and
    splittability). The actual algorithm is not directly treated by this class.
    It can, however, provide you with a loader for actually running the
    algorithmic code (see :py:meth:`Algorithm.runner`).


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The fully qualified algorithm name (e.g. ``user/algo/1``)

      dataformat_cache (:py:class:`dict`, Optional): A dictionary mapping
        dataformat names to loaded dataformats. This parameter is optional and,
        if passed, may greatly speed-up algorithm loading times as dataformats
        that are already loaded may be re-used.

      library_cache (:py:class:`dict`, Optional): A dictionary mapping library
        names to loaded libraries. This parameter is optional and, if passed,
        may greatly speed-up library loading times as libraries that are
        already loaded may be re-used.


    Attributes:

      name (str): The algorithm name

      dataformats (dict): A dictionary containing all pre-loaded dataformats
        used by this algorithm. Data format objects will be of type
        :py:class:`.dataformat.DataFormat`.

      libraries (dict): A mapping object defining other libraries this
        algorithm needs to load so it can work properly.

      uses (dict): A mapping object defining the required library import name
        (keys) and the full-names (values).

      parameters (dict): A dictionary containing all pre-defined parameters
        that this algorithm accepts.

      splittable (bool): A boolean value that indicates if this algorithm is
        automatically parallelizeable by our backend.

      input_map (dict): A dictionary where the key is the input name and the
        value, its type. All input names (potentially from different groups)
        are comprised in this dictionary.

      output_map (dict): A dictionary where the key is the output name and the
        value, its type. All output names (potentially from different groups)
        are comprised in this dictionary.

      results (dict): If this algorithm is actually an analyzer (i.e., there
        are no formal outputs, but results that must be saved by the platform),
        then this dictionary contains the names and data types of those
        elements.

      groups (dict): A list containing dictionaries with inputs and outputs
        belonging to the same synchronization group.

      errors (list): A list containing errors found while loading this
        algorithm.

      data (dict): The original data for this algorithm, as loaded by our JSON
        decoder.

      code (str): The code that is associated with this algorithm, loaded as a
        text (or binary) file.

    """

    LEGACY = "legacy"
    SEQUENTIAL = "sequential"
    AUTONOMOUS = "autonomous"
    SEQUENTIAL_LOOP_EVALUATOR = "sequential_loop_evaluator"
    AUTONOMOUS_LOOP_EVALUATOR = "autonomous_loop_evaluator"
    SEQUENTIAL_LOOP_PROCESSOR = "sequential_loop_processor"
    AUTONOMOUS_LOOP_PROCESSOR = "autonomous_loop_processor"

    dataformat_klass = dataformat.DataFormat

    def __init__(self, prefix, name, dataformat_cache=None, library_cache=None):

        self._name = None
        self.storage = None
        self.prefix = prefix
        self.dataformats = {}
        self.libraries = {}
        self.groups = []
        self.errors = []

        dataformat_cache = dataformat_cache if dataformat_cache is not None else {}
        library_cache = library_cache if library_cache is not None else {}

        self._load(name, dataformat_cache, library_cache)

    def _load(self, data, dataformat_cache, library_cache):
        """Loads the algorithm"""

        self._name = data

        self.storage = Storage(self.prefix, data)
        json_path = self.storage.json.path
        if not self.storage.exists():
            self.errors.append("Algorithm declaration file not found: %s" % json_path)
            return

        with open(json_path, "rb") as f:
            try:
                self.data = json.loads(
                    f.read().decode("utf-8"),
                    object_pairs_hook=utils.error_on_duplicate_key_hook,
                )
            except RuntimeError as error:
                self.errors.append("Algorithm declaration file invalid: %s" % error)
                return

        self.code_path = self.storage.code.path
        self.code = self.storage.code.load()

        self.groups = self.data["groups"]

        # create maps for easy access to data
        self.input_map = dict(
            [(k, v["type"]) for g in self.groups for k, v in g["inputs"].items()]
        )
        self.output_map = dict(
            [
                (k, v["type"])
                for g in self.groups
                for k, v in g.get("outputs", {}).items()
            ]
        )
        self.loop_map = dict(
            [(k, v["type"]) for g in self.groups for k, v in g.get("loop", {}).items()]
        )

        self._load_dataformats(dataformat_cache)
        self._convert_parameter_types()
        self._load_libraries(library_cache)

    def _update_dataformat_cache(self, type_name, dataformat_cache):
        """Update the data format cache based on the type name"""

        if type_name not in self.dataformats:
            if dataformat_cache and type_name in dataformat_cache:  # reuse
                thisformat = dataformat_cache[type_name]
            else:  # load it
                thisformat = self.dataformat_klass(self.prefix, type_name)
                if dataformat_cache is not None:  # update it
                    dataformat_cache[type_name] = thisformat

            self.dataformats[type_name] = thisformat
        return self.dataformats[type_name]

    def _update_dataformat_cache_for_group(self, group, dataformat_cache):
        for _, entry in group.items():
            self._update_dataformat_cache(entry["type"], dataformat_cache)

    def _load_dataformats(self, dataformat_cache):
        """Makes sure we can load all requested formats
        """

        for group in self.groups:
            self._update_dataformat_cache_for_group(group["inputs"], dataformat_cache)

            if "outputs" in group:
                self._update_dataformat_cache_for_group(
                    group["outputs"], dataformat_cache
                )

            if "loop" in group:
                self._update_dataformat_cache_for_group(group["loop"], dataformat_cache)

        if self.results:

            for name, result in self.results.items():
                result_type = result["type"]
                # results can only contain base types and plots therefore, only
                # process plots
                if result_type.find("/") != -1:
                    self._update_dataformat_cache(result_type, dataformat_cache)

    def _convert_parameter_types(self):
        """Converts types to numpy equivalents, checks defaults, ranges and choices
        """

        def _try_convert(name, tp, value, desc):
            try:
                return tp.type(value)
            except Exception as e:
                self.errors.append(
                    "%s for parameter `%s' cannot be cast to type "
                    "`%s': %s" % (desc, name, tp.name, e)
                )

        if self.parameters is None:
            return

        for name, parameter in self.parameters.items():
            if parameter["type"] == "string":
                parameter["type"] = numpy.dtype("str")
            else:
                parameter["type"] = numpy.dtype(parameter["type"])

            if "range" in parameter:
                parameter["range"][0] = _try_convert(
                    name, parameter["type"], parameter["range"][0], "start of range"
                )
                parameter["range"][1] = _try_convert(
                    name, parameter["type"], parameter["range"][1], "end of range"
                )
                if parameter["range"][0] >= parameter["range"][1]:
                    self.errors.append(
                        "range for parameter `%s' has a start greater "
                        "then the end value (%r >= %r)"
                        % (name, parameter["range"][0], parameter["range"][1])
                    )

            if "choice" in parameter:
                for i, choice in enumerate(parameter["choice"]):
                    parameter["choice"][i] = _try_convert(
                        name,
                        parameter["type"],
                        parameter["choice"][i],
                        "choice[%d]" % i,
                    )

            if "default" in parameter:
                parameter["default"] = _try_convert(
                    name, parameter["type"], parameter["default"], "default"
                )

                if "range" in parameter:  # check range
                    if (
                        parameter["default"] < parameter["range"][0]
                        or parameter["default"] > parameter["range"][1]
                    ):
                        self.errors.append(
                            "default for parameter `%s' (%r) is not "
                            "within parameter range [%r, %r]"
                            % (
                                name,
                                parameter["default"],
                                parameter["range"][0],
                                parameter["range"][1],
                            )
                        )

                if "choice" in parameter:  # check choices
                    if parameter["default"] not in parameter["choice"]:
                        self.errors.append(
                            "default for parameter `%s' (%r) is not "
                            "a valid choice `[%s]'"
                            % (
                                name,
                                parameter["default"],
                                ", ".join(["%r" % k for k in parameter["choice"]]),
                            )
                        )

    def _load_libraries(self, library_cache):

        # all used libraries must be loadable; cannot use self as a library

        if self.uses:

            for name, value in self.uses.items():

                self.libraries[value] = library_cache.setdefault(
                    value, library.Library(self.prefix, value, library_cache)
                )

    @property
    def name(self):
        """Returns the name of this object
        """
        return self._name or "__unnamed_algorithm__"

    @name.setter
    def name(self, value):
        """Sets the name of this object

        Parameters:
            name (str): Name of this object
        """

        if self.data["language"] == "unknown":
            raise RuntimeError("algorithm has no programming language set")

        self._name = value
        self.storage = Storage(self.prefix, value, self.data["language"])

    @property
    def schema_version(self):
        """Returns the schema version"""
        return self.data.get("schema_version", 1)

    @property
    def language(self):
        """Returns the current language set for the executable code"""
        return self.data["language"]

    @property
    def api_version(self):
        """Returns the API version"""
        return self.data.get("api_version", 1)

    @property
    def type(self):
        """Returns the type of algorithm"""
        if self.api_version == 1:
            return Algorithm.LEGACY

        return self.data.get("type", Algorithm.SEQUENTIAL)

    @property
    def is_autonomous(self):
        """ Returns whether the algorithm is in the autonomous category"""
        return self.type in [
            Algorithm.AUTONOMOUS,
            Algorithm.AUTONOMOUS_LOOP_EVALUATOR,
            Algorithm.AUTONOMOUS_LOOP_PROCESSOR,
        ]

    @property
    def is_sequential(self):
        """ Returns whether the algorithm is in the sequential category"""
        return self.type in [
            Algorithm.SEQUENTIAL,
            Algorithm.SEQUENTIAL_LOOP_EVALUATOR,
            Algorithm.SEQUENTIAL_LOOP_PROCESSOR,
        ]

    @property
    def is_loop(self):
        return self.type in [
            Algorithm.SEQUENTIAL_LOOP_EVALUATOR,
            Algorithm.AUTONOMOUS_LOOP_EVALUATOR,
        ]

    @language.setter
    def language(self, value):
        """Sets the current executable code programming language"""
        if self.storage:
            self.storage.language = value
        self.data["language"] = value

    def clean_parameter(self, parameter, value):
        """Checks if a given value against a declared parameter

        This method checks if the provided user value can be safe-cast to the
        parameter type as defined on its specification and that it conforms to
        any parameter-imposed restrictions.


        Parameters:

          parameter (str): The name of the parameter to check the value against

          value (object): An object that will be safe cast into the defined
            parameter type.


        Returns:

          The converted value, with an appropriate numpy type.


        Raises:

          KeyError: If the parameter cannot be found on this algorithm's
            declaration.

          ValueError: If the parameter cannot be safe cast into the algorithm's
            type. Alternatively, a ``ValueError`` may also be raised if a range
            or choice was specified and the value does not obey those settings
            stipulated for the parameter
        """

        if (self.parameters is None) or (parameter not in self.parameters):
            raise KeyError(parameter)

        retval = self.parameters[parameter]["type"].type(value)

        if (
            "choice" in self.parameters[parameter]
            and retval not in self.parameters[parameter]["choice"]
        ):
            raise ValueError(
                "value for `%s' (%r) must be one of `[%s]'"
                % (
                    parameter,
                    value,
                    ", ".join(["%r" % k for k in self.parameters[parameter]["choice"]]),
                )
            )

        if "range" in self.parameters[parameter] and (
            retval < self.parameters[parameter]["range"][0]
            or retval > self.parameters[parameter]["range"][1]
        ):
            raise ValueError(
                "value for `%s' (%r) must be picked within "
                "interval `[%r, %r]'"
                % (
                    parameter,
                    value,
                    self.parameters[parameter]["range"][0],
                    self.parameters[parameter]["range"][1],
                )
            )

        return retval

    @property
    def valid(self):
        """A boolean that indicates if this algorithm is valid or not"""

        return not bool(self.errors)

    @property
    def uses(self):
        return self.data.get("uses")

    @uses.setter
    def uses(self, value):
        if not isinstance(value, dict):
            raise RuntimeError("Invalid uses entry, must be a dict")
        self.data["uses"] = value
        return value

    @property
    def isAnalyzer(self):
        """Returns whether this algorithms is an analyzer"""

        return self.results is not None

    @property
    def results(self):
        """The results of this algorithm"""

        return self.data.get("results")

    @results.setter
    def results(self, value):
        self.data["results"] = value
        return value

    @property
    def parameters(self):
        """The parameters of this algorithm"""

        return self.data.get("parameters")

    @parameters.setter
    def parameters(self, value):
        self.data["parameters"] = value
        return value

    @property
    def splittable(self):
        """Whether this algorithm can be split between several processes"""
        return self.data.get("splittable", False)

    @splittable.setter
    def splittable(self, value):
        self.data["splittable"] = value
        return value

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

        if not self._name:
            raise RuntimeError("algorithm has no name")

        if self.storage.doc.exists():
            return self.storage.doc.load()
        return None

    @documentation.setter
    def documentation(self, value):
        """Sets the full-length description for this object"""

        if not self._name:
            raise RuntimeError("algorithm has no name")

        if hasattr(value, "read"):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)

    def hash(self):
        """Returns the hexadecimal hash for the current algorithm"""

        if not self._name:
            raise RuntimeError("algorithm has no name")

        return self.storage.hash()

    def result_dataformat(self):
        """Generates, on-the-fly, the dataformat for the result readout"""

        if not self.results:
            raise TypeError(
                "algorithm `%s' is a block algorithm, not an analyzer" % (self.name)
            )

        format = dataformat.DataFormat(
            self.prefix, dict([(k, v["type"]) for k, v in self.results.items()])
        )

        format.name = "analysis:" + self.name

        return format

    def uses_dict(self):
        """Returns the usage dictionary for all dependent modules"""

        if self.data["language"] == "unknown":
            raise RuntimeError("algorithm has no programming language set")

        if not self._name:
            raise RuntimeError("algorithm has no name")

        retval = {}

        if self.uses is not None:
            for name, value in self.uses.items():
                retval[name] = dict(
                    path=self.libraries[value].storage.code.path,
                    uses=self.libraries[value].uses_dict(),
                )

        return retval

    def runner(self, klass="Algorithm", exc=None):
        """Returns a runnable algorithm object.

        Parameters:

          klass (str): The name of the class to load the runnable algorithm from

          exc (:std:term:`class`): If passed, must be a valid exception class
            that will be used to report errors in the read-out of this algorithm's code.

        Returns:

          :py:class:`Runner`: An instance of the algorithm,
            which will be constructed, but not setup.  You **must** set it up
            before using the ``process`` method.
        """

        if not self._name:
            exc = exc or RuntimeError
            raise exc("algorithm has no name")

        if self.data["language"] == "unknown":
            exc = exc or RuntimeError
            raise exc("algorithm has no programming language set")

        if not self.valid:
            message = "cannot load code for invalid algorithm (%s)" % (self.name,)
            exc = exc or RuntimeError
            raise exc(message)

        # loads the module only once through the lifetime of the algorithm object
        try:
            self.__module = getattr(
                self,
                "module",
                loader.load_module(
                    self.name.replace(os.sep, "_"),
                    self.storage.code.path,
                    self.uses_dict(),
                ),
            )
        except Exception:
            if exc is not None:
                type, value, traceback = sys.exc_info()
                six.reraise(exc, exc(value), traceback)
            else:
                raise  # just re-raise the user exception

        return Runner(self.__module, klass, self, exc)

    def json_dumps(self, indent=4):
        """Dumps the JSON declaration of this object in a string


        Parameters:

          indent (int): The number of indentation spaces at every indentation level


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

        if self.data["language"] == "unknown":
            raise RuntimeError("algorithm has no programming language set")

        if storage is None:
            if not self._name:
                raise RuntimeError("algorithm has no name")
            storage = self.storage  # overwrite

        storage.save(str(self), self.code, self.description)

    def export(self, prefix):
        """Recursively exports itself into another prefix

        Dataformats and associated libraries are also copied.


        Parameters:

          prefix (str): A path to a prefix that must different then my own.


        Returns:

          None


        Raises:

          RuntimeError: If prefix and self.prefix point to the same directory.

        """

        if not self._name:
            raise RuntimeError("algorithm has no name")

        if not self.valid:
            raise RuntimeError("algorithm is not valid:\n%s" % "\n".join(self.errors))

        if prefix == self.prefix:
            raise RuntimeError(
                "Cannot export algorithm to the same prefix (" "%s)" % prefix
            )

        for k in self.libraries.values():
            k.export(prefix)

        for k in self.dataformats.values():
            k.export(prefix)

        self.write(Storage(prefix, self.name, self.language))
