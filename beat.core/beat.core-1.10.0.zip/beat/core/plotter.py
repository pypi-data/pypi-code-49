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
plotter
=======

Validation for plotters
"""

import os
import six
import sys

from . import dataformat
from . import algorithm
from . import schema
from . import prototypes
from . import utils
from . import loader


# ----------------------------------------------------------


class Storage(utils.CodeStorage):
    """Resolves paths for plotter

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The name of the algorithm object in the format
        ``<user>/<name>/<version>``.

    """

    asset_type = "plotter"
    asset_folder = "plotters"

    def __init__(self, prefix, name, language=None):

        if name.count("/") != 2:
            raise RuntimeError("invalid plotter name: `%s'" % name)

        self.username, self.name, self.version = name.split("/")
        self.fullname = name
        self.prefix = prefix

        path = utils.hashed_or_simple(
            self.prefix, self.asset_folder, name, suffix=".json"
        )
        path = path[:-5]

        super(Storage, self).__init__(path, language)


# ----------------------------------------------------------


class Runner(algorithm.Runner):
    """A special loader class for plotters, with specialized methods"""

    def process(self, inputs=None):
        """Runs through data"""

        exc = self.exc or RuntimeError

        def _check_argument(argument, name):
            if argument is None:
                raise exc("Missing argument: %s" % name)

        # setup() must have run
        if not self.ready:
            raise exc("Plottr '%s' is not yet setup" % self.name)

        _check_argument(inputs, "inputs")
        return loader.run(self.obj, "process", self.exc, inputs)


# ----------------------------------------------------------


class Plotter(object):
    """Plotter represent runnable components within the platform that generate
    images from data points.

    This class can only parse the meta-parameters of the plotter (i.e.,
    parameters and applicable dataformat). The actual plotter is not directly
    treated by this class - it can, however, provide you with a loader for
    actually running the plotting code (see :py:meth:`Plotter.runner`).


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (:py:class:`object`, Optional): The piece of data representing the
        plotter. It must validate against the schema defined for plotters. If a
        string is passed, it is supposed to be a valid path to a plotter in the
        designated prefix area. If a tuple is passed (or a list), then we
        consider that the first element represents the plotter declaration,
        while the second, the code for the plotter (either in its source format
        or as a binary blob). If ``None`` is passed, loads our default
        prototype for plotters (source code will be in Python).

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

      description (str): The short description string, loaded from the JSON
        file if one was set.

      documentation (str): The full-length docstring for this object.

      storage (object): A simple object that provides information about file
        paths for this algorithm

      dataformat (object): An object of type :py:class:`.dataformat.DataFormat`
        that represents the dataformat to which this plotter is applicable.

      libraries (dict): A mapping object defining other libraries this plotter
        needs to load so it can work properly.

      uses (dict): A mapping object defining the required library import name
        (keys) and the full-names (values).

      parameters (dict): A dictionary containing all pre-defined parameters
        that this algorithm accepts.

      errors (list): A list containing errors found while loading this
        algorithm.

      data (dict): The original data for this algorithm, as loaded by our JSON
        decoder.

      code (str): The code that is associated with this algorithm, loaded as a
        text (or binary) file.

    """

    def __init__(self, prefix, data, dataformat_cache=None, library_cache=None):

        self._name = None
        self.storage = None
        self.prefix = prefix
        self.dataformat = None
        self.libraries = {}

        dataformat_cache = dataformat_cache if dataformat_cache is not None else {}
        library_cache = library_cache if library_cache is not None else {}

        self._load(data, dataformat_cache, library_cache)

    def _load(self, data, dataformat_cache, library_cache):
        """Loads the algorithm"""

        self.errors = []
        self.data = None
        self.code = None

        self._name = None
        self.storage = None
        self.dataformats = None
        self.libraries = {}

        code = None

        if data is None:  # loads prototype and validates it

            data = None
            code = None

        elif isinstance(data, (tuple, list)):  # user has passed individual info

            data, code = data  # break down into two components

        if isinstance(data, six.string_types):  # user has passed a file pointer

            self._name = data
            self.storage = Storage(self.prefix, self._name)
            if not self.storage.json.exists():
                self.errors.append("Plotter declaration file not found: %s" % data)
                return

            data = self.storage.json.path  # loads data from JSON declaration

        # At this point, `data' can be a dictionary or ``None``
        if data is None:  # loads the default declaration for an algorithm
            self.data, self.errors = prototypes.load("plotter")
            assert not self.errors, "\n  * %s" % "\n  *".join(self.errors)  # nosec
        else:  # just assign it
            # this runs basic validation, including JSON loading if required
            self.data, self.errors = schema.validate("plotter", data)

        if self.errors:
            return  # don't proceed with the rest of validation

        if self.storage is not None:  # loading from the disk, check code
            if not self.storage.code.exists():
                self.errors.append(
                    "Plotter code not found: %s" % self.storage.code.path
                )
                return
            else:
                code = self.storage.code.load()

        # At this point, `code' can be a string (or a binary blob) or ``None``
        if code is None:  # loads the default code for an algorithm
            self.code = prototypes.binary_load("plotter.py")
            self.data["language"] = "python"

        else:  # just assign it - notice that in this case, no language is set
            self.code = code

        if self.errors:
            return  # don't proceed with the rest of validation

        # if no errors so far, make sense out of the declaration data
        self.parameters = self.data.setdefault("parameters", {})
        self.dataformat = None

        self._validate_dataformat(dataformat_cache)
        self._convert_parameter_types()

        # finally, the libraries
        self._validate_required_libraries(library_cache)
        self._check_language_consistence()

    # Methods re-bound from the Algorithm class
    if six.PY2:
        _convert_parameter_types = algorithm.Algorithm._convert_parameter_types.im_func

        _validate_required_libraries = (
            algorithm.Algorithm._validate_required_libraries.im_func
        )

        _check_language_consistence = (
            algorithm.Algorithm._check_language_consistence.im_func
        )
    else:
        _convert_parameter_types = algorithm.Algorithm._convert_parameter_types

        _validate_required_libraries = algorithm.Algorithm._validate_required_libraries

        _check_language_consistence = algorithm.Algorithm._check_language_consistence

    def _validate_dataformat(self, dataformat_cache):
        """Makes sure we can load the requested format
        """

        name = self.data["dataformat"]

        if dataformat_cache and name in dataformat_cache:  # reuse
            self.dataformat = dataformat_cache[name]
        else:  # load it
            self.dataformat = dataformat.DataFormat(
                self.prefix, name, dataformat_cache=dataformat_cache
            )
            dataformat_cache[name] = self.dataformat

        if self.dataformat.errors:
            self.errors.append(
                "found error validating base data format `%s' "
                "for plotter `%s': %s"
                % (name, self.name, "\n".join(self.dataformat.errors))
            )

    @property
    def schema_version(self):
        """Returns the schema version"""
        return self.data.get("schema_version", 1)

    @property
    def name(self):
        """Returns the name of this object
        """
        return self._name or "__unnamed_plotter__"

    @name.setter
    def name(self, value):
        if self.data["language"] == "unknown":
            raise RuntimeError("plotter has no programming language set")

        self._name = value
        self.storage = Storage(self.prefix, value, self.data["language"])

    language = algorithm.Algorithm.language
    if six.PY2:
        clean_parameter = algorithm.Algorithm.clean_parameter.im_func
    else:
        clean_parameter = algorithm.Algorithm.clean_parameter
    valid = algorithm.Algorithm.valid

    @property
    def api_version(self):
        """Returns the API version"""
        return self.data.get("api_version", 1)

    def uses_dict(self):
        """Returns the usage dictionary for all dependent modules"""

        if self.data["language"] == "unknown":
            raise RuntimeError("plotter has no programming language set")

        if not self._name:
            raise RuntimeError("plotter has no name")

        retval = {}

        if self.uses is not None:
            for name, value in self.uses.items():
                retval[name] = dict(
                    path=self.libraries[value].storage.code.path,
                    uses=self.libraries[value].uses_dict(),
                )

        return retval

    def runner(self, klass="Plotter", exc=None):
        """Returns a runnable plotter object.

        Parameters:

          klass (str): The name of the class to load the runnable algorithm
            from

          exc (:std:term:`class`): If passed, must be a valid exception class
            that will be used to report errors in the read-out of this
            plotter's code.

        Returns:

          :py:class:`beat.backend.python.algorithm.Runner`: An instance of the
            algorithm, which will be constructed, but not setup.  You **must**
            set it up before using the ``process`` method.

        """

        if not self._name:
            exc = exc or RuntimeError
            raise exc("plotter has no name")

        if self.data["language"] == "unknown":
            exc = exc or RuntimeError
            raise exc("plotter has no programming language set")

        if not self.valid:
            message = "cannot load code for invalid plotter (%s)" % (self.name,)
            exc = exc or RuntimeError
            raise exc(message)

        # loads the module only once through the lifetime of the plotter object
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

    description = algorithm.Algorithm.description

    @property
    def documentation(self):
        """The full-length description for this object"""

        if not self._name:
            raise RuntimeError("plotter has no name")

        if self.storage.doc.exists():
            return self.storage.doc.load()
        return None

    @documentation.setter
    def documentation(self, value):
        """Sets the full-length description for this object"""

        if not self._name:
            raise RuntimeError("plotter has no name")

        if hasattr(value, "read"):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)

    uses = algorithm.Algorithm.uses
    parameters = algorithm.Algorithm.parameters

    def hash(self):
        """Returns the hexadecimal hash for the current plotter"""

        if not self._name:
            raise RuntimeError("plotter has no name")

        return self.storage.hash()

    def write(self, storage=None):
        """Writes contents to prefix location

        Parameters:

          storage (:py:class:`.Storage`, Optional): If you pass a new storage,
            then this object will be written to that storage point rather than
            its default.

        """

        if self.data["language"] == "unknown":
            raise RuntimeError("plotter has no programming language set")

        if storage is None:
            if not self._name:
                raise RuntimeError("plotter has no name")
            storage = self.storage  # overwrite

        storage.save(str(self), self.code, self.description)


if six.PY2:
    Plotter.json_dumps = algorithm.Algorithm.json_dumps.im_func
    Plotter.__str__ = algorithm.Algorithm.__str__.im_func
else:
    Plotter.json_dumps = algorithm.Algorithm.json_dumps
    Plotter.__str__ = algorithm.Algorithm.__str__
