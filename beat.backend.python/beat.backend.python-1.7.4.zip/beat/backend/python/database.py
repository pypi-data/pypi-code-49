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
========
database
========

Validation of databases
"""

import os
import sys

import six
import simplejson as json
import itertools
import numpy as np
from collections import namedtuple

from . import loader
from . import utils

from .protocoltemplate import ProtocolTemplate
from .dataformat import DataFormat
from .outputs import OutputList
from .exceptions import OutputError


# ----------------------------------------------------------


class Storage(utils.CodeStorage):
    """Resolves paths for databases

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The name of the database object in the format
        ``<name>/<version>``.

    """

    asset_type = "database"
    asset_folder = "databases"

    def __init__(self, prefix, name):

        if name.count("/") != 1:
            raise RuntimeError("invalid database name: `%s'" % name)

        self.name, self.version = name.split("/")
        self.fullname = name
        self.prefix = prefix

        path = os.path.join(self.prefix, self.asset_folder, name + ".json")
        path = path[:-5]
        # views are coded in Python
        super(Storage, self).__init__(path, "python")


# ----------------------------------------------------------


class Runner(object):
    """A special loader class for database views, with specialized methods

    Parameters:

      db_name (str): The full name of the database object for this view

      module (:std:term:`module`): The preloaded module containing the database
        views as returned by :py:func:`.loader.load_module`.

      prefix (str): Establishes the prefix of your installation.

      root_folder (str): The path pointing to the root folder of this database

      exc (:std:term:`class`): The class to use as base exception when
        translating the exception from the user code. Read the documention of
        :py:func:`.loader.run` for more details.

      *args: Constructor parameters for the database view. Normally, none.

      **kwargs: Constructor parameters for the database view. Normally, none.

    """

    def __init__(self, module, definition, prefix, root_folder, exc=None):

        try:
            class_ = getattr(module, definition["view"])
        except Exception:
            if exc is not None:
                type, value, traceback = sys.exc_info()
                six.reraise(exc, exc(value), traceback)
            else:
                raise  # just re-raise the user exception

        self.obj = loader.run(class_, "__new__", exc)
        self.ready = False
        self.prefix = prefix
        self.root_folder = root_folder
        self.definition = definition
        self.exc = exc or RuntimeError
        self.data_sources = None

    def index(self, filename):
        """Index the content of the view"""

        parameters = self.definition.get("parameters", {})

        objs = loader.run(self.obj, "index", self.exc, self.root_folder, parameters)

        if not isinstance(objs, list):
            raise self.exc("index() didn't return a list")

        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        with open(filename, "wb") as f:
            data = json.dumps(objs, cls=utils.NumpyJSONEncoder)
            f.write(data.encode("utf-8"))

    def setup(self, filename, start_index=None, end_index=None, pack=True):
        """Sets up the view"""

        if self.ready:
            return

        with open(filename, "rb") as f:
            objs = json.loads(
                f.read().decode("utf-8"),
                object_pairs_hook=utils.error_on_duplicate_key_hook,
            )

        Entry = namedtuple("Entry", sorted(objs[0].keys()))
        objs = [Entry(**x) for x in objs]

        parameters = self.definition.get("parameters", {})

        loader.run(
            self.obj,
            "setup",
            self.exc,
            self.root_folder,
            parameters,
            objs,
            start_index=start_index,
            end_index=end_index,
        )

        # Create data sources for the outputs
        from .data import DatabaseOutputDataSource

        self.data_sources = {}
        for output_name, output_format in self.definition.get("outputs", {}).items():
            data_source = DatabaseOutputDataSource()
            data_source.setup(
                self,
                output_name,
                output_format,
                self.prefix,
                start_index=start_index,
                end_index=end_index,
                pack=pack,
            )
            self.data_sources[output_name] = data_source

        self.ready = True

    def get(self, output, index):
        """Returns the data of the provided output at the provided index"""

        if not self.ready:
            raise self.exc("Database view not yet setup")

        return loader.run(self.obj, "get", self.exc, output, index)

    def get_output_mapping(self, output):
        return loader.run(self.obj, "get_output_mapping", self.exc, output)

    def objects(self):
        return self.obj.objs


# ----------------------------------------------------------


class Database(object):
    """Databases define the start point of the dataflow in an experiment.


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The fully qualified database name (e.g. ``db/1``)

      dataformat_cache (:py:class:`dict`, Optional): A dictionary mapping
        dataformat names to loaded dataformats. This parameter is optional and,
        if passed, may greatly speed-up database loading times as dataformats
        that are already loaded may be re-used. If you use this parameter, you
        must guarantee that the cache is refreshed as appropriate in case the
        underlying dataformats change.


    Attributes:

      name (str): The full, valid name of this database

      data (dict): The original data for this database, as loaded by our JSON
        decoder.

    """

    def __init__(self, prefix, name, dataformat_cache=None):

        self._name = None
        self.prefix = prefix
        self.dataformats = {}  # preloaded dataformats
        self.storage = None

        self.errors = []
        self.data = None

        # if the user has not provided a cache, still use one for performance
        dataformat_cache = dataformat_cache if dataformat_cache is not None else {}

        self._load(name, dataformat_cache)

    def _update_dataformat_cache(self, outputs, dataformat_cache):
        for key, value in outputs.items():

            if value in self.dataformats:
                continue

            if value in dataformat_cache:
                dataformat = dataformat_cache[value]
            else:
                dataformat = DataFormat(self.prefix, value)
                dataformat_cache[value] = dataformat

            self.dataformats[value] = dataformat

    def _load_v1(self, dataformat_cache):
        """Loads a v1 database and fills the dataformat cache"""

        for protocol in self.data["protocols"]:
            for set_ in protocol["sets"]:
                self._update_dataformat_cache(set_["outputs"], dataformat_cache)

    def _load_v2(self, dataformat_cache):
        """Loads a v2 database and fills the dataformat cache"""

        for protocol in self.data["protocols"]:
            protocol_template = ProtocolTemplate(
                self.prefix, protocol["template"], dataformat_cache
            )
            for set_ in protocol_template.sets():
                self._update_dataformat_cache(set_["outputs"], dataformat_cache)

    def _load(self, data, dataformat_cache):
        """Loads the database"""

        self._name = data

        self.storage = Storage(self.prefix, self._name)
        json_path = self.storage.json.path
        if not self.storage.json.exists():
            self.errors.append("Database declaration file not found: %s" % json_path)
            return

        with open(json_path, "rb") as f:
            try:
                self.data = json.loads(
                    f.read().decode("utf-8"),
                    object_pairs_hook=utils.error_on_duplicate_key_hook,
                )
            except RuntimeError as error:
                self.errors.append("Database declaration file invalid: %s" % error)
                return

        self.code_path = self.storage.code.path
        self.code = self.storage.code.load()

        if self.schema_version == 1:
            self._load_v1(dataformat_cache)
        elif self.schema_version == 2:
            self._load_v2(dataformat_cache)
        else:
            raise RuntimeError(
                "Invalid schema version {schema_version}".format(
                    schema_version=self.schema_version
                )
            )

    @property
    def name(self):
        """Returns the name of this object
        """
        return self._name or "__unnamed_database__"

    @name.setter
    def name(self, value):
        self._name = value
        self.storage = Storage(self.prefix, value)

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
            raise RuntimeError("database has no name")

        if self.storage.doc.exists():
            return self.storage.doc.load()
        return None

    @documentation.setter
    def documentation(self, value):
        """Sets the full-length description for this object"""

        if not self._name:
            raise RuntimeError("database has no name")

        if hasattr(value, "read"):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)

    def hash(self):
        """Returns the hexadecimal hash for its declaration"""

        if not self._name:
            raise RuntimeError("database has no name")

        return self.storage.hash()

    @property
    def schema_version(self):
        """Returns the schema version"""
        return self.data.get("schema_version", 1)

    @property
    def valid(self):
        """A boolean that indicates if this database is valid or not"""

        return not bool(self.errors)

    @property
    def protocols(self):
        """The declaration of all the protocols of the database"""

        data = self.data["protocols"]
        return dict(zip([k["name"] for k in data], data))

    def protocol(self, name):
        """The declaration of a specific protocol in the database"""

        return self.protocols[name]

    @property
    def protocol_names(self):
        """Names of protocols declared for this database"""

        data = self.data["protocols"]
        return [k["name"] for k in data]

    def sets(self, protocol):
        """The declaration of a specific set in the database protocol"""

        if self.schema_version == 1:
            data = self.protocol(protocol)["sets"]
        else:
            protocol = self.protocol(protocol)
            protocol_template = ProtocolTemplate(self.prefix, protocol["template"])
            if not protocol_template.valid:
                raise RuntimeError(
                    "\n  * {}".format("\n  * ".join(protocol_template.errors))
                )
            data = protocol_template.sets()

        return dict(zip([k["name"] for k in data], data))

    def set(self, protocol, name):
        """The declaration of all the protocols of the database"""

        return self.sets(protocol)[name]

    def set_names(self, protocol):
        """The names of sets in a given protocol for this database"""

        if self.schema_version == 1:
            data = self.protocol(protocol)["sets"]
        else:
            protocol = self.protocol(protocol)
            protocol_template = ProtocolTemplate(self.prefix, protocol["template"])
            if not protocol_template.valid:
                raise RuntimeError(
                    "\n  * {}".format("\n  * ".join(protocol_template.errors))
                )
            data = protocol_template.sets()

        return [k["name"] for k in data]

    def view_definition(self, protocol_name, set_name):
        """Returns the definition of a view

        Parameters:
          protocol_name (str): The name of the protocol where to retrieve the view
            from

          set_name (str): The name of the set in the protocol where to retrieve the
            view from

        """

        if self.schema_version == 1:
            view_definition = self.set(protocol_name, set_name)
        else:
            protocol = self.protocol(protocol_name)
            template_name = protocol["template"]
            protocol_template = ProtocolTemplate(self.prefix, template_name)
            view_definition = protocol_template.set(set_name)
            view_definition["view"] = protocol["views"][set_name]["view"]
            parameters = protocol["views"][set_name].get("parameters")
            if parameters is not None:
                view_definition["parameters"] = parameters

        return view_definition

    def view(self, protocol, name, exc=None, root_folder=None):
        """Returns the database view, given the protocol and the set name

        Parameters:

          protocol (str): The name of the protocol where to retrieve the view
            from

          name (str): The name of the set in the protocol where to retrieve the
            view from

          exc (:std:term:`class`): If passed, must be a valid exception class
            that will be used to report errors in the read-out of this
            database's view.

        Returns:

          The database view, which will be constructed, but not setup. You
          **must** set it up before using methods ``done`` or ``next``.

        """

        if not self._name:
            exc = exc or RuntimeError
            raise exc("database has no name")

        if not self.valid:
            message = (
                "cannot load view for set `%s' of protocol `%s' "
                "from invalid database (%s)\n%s"
                % (protocol, name, self.name, "   \n".join(self.errors))
            )
            if exc:
                raise exc(message)

            raise RuntimeError(message)

        # loads the module only once through the lifetime of the database
        # object
        try:
            if not hasattr(self, "_module"):
                self._module = loader.load_module(
                    self.name.replace(os.sep, "_"), self.storage.code.path, {}
                )
        except Exception:
            if exc is not None:
                type, value, traceback = sys.exc_info()
                six.reraise(exc, exc(value), traceback)
            else:
                raise  # just re-raise the user exception

        if root_folder is None:
            root_folder = self.data["root_folder"]

        return Runner(
            self._module,
            self.view_definition(protocol, name),
            self.prefix,
            root_folder,
            exc,
        )

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
            if not self._name:
                raise RuntimeError("database has no name")
            storage = self.storage  # overwrite

        storage.save(str(self), self.code, self.description)

    def export(self, prefix):
        """Recursively exports itself into another prefix

        Dataformats associated are also exported recursively


        Parameters:

          prefix (str): A path to a prefix that must different then my own.


        Returns:

          None


        Raises:

          RuntimeError: If prefix and self.prefix point to the same directory.

        """

        if not self._name:
            raise RuntimeError("database has no name")

        if not self.valid:
            raise RuntimeError("database is not valid")

        if prefix == self.prefix:
            raise RuntimeError(
                "Cannot export database to the same prefix (" "%s)" % prefix
            )

        for k in self.dataformats.values():
            k.export(prefix)

        if self.schema_version != 1:
            for protocol in self.protocols.values():
                protocol_template = ProtocolTemplate(self.prefix, protocol["template"])
                protocol_template.export(prefix)

        self.write(Storage(prefix, self.name))


# ----------------------------------------------------------


class View(object):
    def __init__(self):
        #  Current databases definitions uses named tuple to store information.
        #  This has one limitation, python keywords like `class` cannot be used.
        #  output_member_map allows to use that kind of keyword as output name
        #  while using something different for the named tuple (for example cls,
        #  klass, etc.)
        self.output_member_map = {}

    def index(self, root_folder, parameters):
        """Returns a list of (named) tuples describing the data provided by the view.

        The ordering of values inside the tuples is free, but it is expected
        that the list is ordered in a consistent manner (ie. all train images
        of person A, then all train images of person B, ...).

        For instance, assuming a view providing that kind of data:

        .. code-block:: text

           ----------- ----------- ----------- ----------- ----------- -----------
           |  image  | |  image  | |  image  | |  image  | |  image  | |  image  |
           ----------- ----------- ----------- ----------- ----------- -----------
           ----------- ----------- ----------- ----------- ----------- -----------
           | file_id | | file_id | | file_id | | file_id | | file_id | | file_id |
           ----------- ----------- ----------- ----------- ----------- -----------
           ----------------------------------- -----------------------------------
           |             client_id           | |             client_id           |
           ----------------------------------- -----------------------------------

        a list like the following should be generated:

        .. code-block:: python

           [
               (client_id=1, file_id=1, image=filename1),
               (client_id=1, file_id=2, image=filename2),
               (client_id=1, file_id=3, image=filename3),
               (client_id=2, file_id=4, image=filename4),
               (client_id=2, file_id=5, image=filename5),
               (client_id=2, file_id=6, image=filename6),
               ...
           ]

        .. warning::

           DO NOT store images, sound files or data loadable from a file in the
           list!  Store the path of the file to load instead.

        """

        raise NotImplementedError

    def setup(self, root_folder, parameters, objs, start_index=None, end_index=None):

        # Initialisation
        self.root_folder = root_folder
        self.parameters = parameters
        self.objs = objs

        # Determine the range of indices that must be provided
        self.start_index = start_index if start_index is not None else 0
        self.end_index = end_index if end_index is not None else len(self.objs) - 1

        self.objs = self.objs[self.start_index : self.end_index + 1]  # noqa

    def get(self, output, index):
        """Returns the data of the provided output at the provided index in the
        list of (named) tuples describing the data provided by the view
        (accessible at self.objs)
        """

        raise NotImplementedError

    def get_output_mapping(self, output):
        """Returns the object member to use for given output if any otherwise
        the member name is the output name.
        """
        return self.output_member_map.get(output, output)


# ----------------------------------------------------------


class DatabaseTester:
    """Used while developing a new database view, to test its behavior

    This class tests that, for each combination of connected/not connected
    outputs:

      - Data indices seems consistent
      - All the connected outputs produce data
      - All the not connected outputs don't produce data

    It also report some stats, and can generate a text file detailing the
    data generated by each output.

    By default, outputs are assumed to produce data at constant intervals.
    Those that don't follow this pattern, must be declared as 'irregular'.

    Note that no particular check is done about the database declaration or
    the correctness of the generated data with their data formats. This class
    is mainly used to check that the outputs are correctly synchronized.
    """

    # Mock output class
    class MockOutput:
        def __init__(self, name, connected):
            self.name = name
            self.connected = connected
            self.last_written_data_index = -1
            self.written_data = []

        def write(self, data, end_data_index):
            self.written_data.append(
                (self.last_written_data_index + 1, end_data_index, data)
            )
            self.last_written_data_index = end_data_index

        def isConnected(self):
            return self.connected

    class SynchronizedUnit:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.data = {}
            self.children = []

        def addData(self, output, start, end, data):
            if (start == self.start) and (end == self.end):
                self.data[output] = self._dataToString(data)
            elif (len(self.children) == 0) or (self.children[-1].end < start):
                unit = DatabaseTester.SynchronizedUnit(start, end)
                unit.addData(output, start, end, data)
                self.children.append(unit)
            else:
                for index, unit in enumerate(self.children):
                    if (unit.start <= start) and (unit.end >= end):
                        unit.addData(output, start, end, data)
                        break
                    elif (unit.start == start) and (unit.end < end):
                        new_unit = DatabaseTester.SynchronizedUnit(start, end)
                        new_unit.addData(output, start, end, data)
                        new_unit.children.append(unit)

                        for i in range(index + 1, len(self.children)):
                            unit = self.children[i]
                            if unit.end <= end:
                                new_unit.children.append(unit)
                            else:
                                break

                        self.children = (
                            self.children[:index] + [new_unit] + self.children[i:]
                        )
                        break

        def toString(self):
            texts = {}

            for child in self.children:
                child_texts = child.toString()
                for output, text in child_texts.items():
                    if output in texts:
                        texts[output] += " " + text
                    else:
                        texts[output] = text

            if len(self.data) > 0:
                length = max([len(x) + 6 for x in self.data.values()])

                if len(texts) > 0:
                    children_length = len(texts.values()[0])
                    if children_length >= length:
                        length = children_length
                    else:
                        diff = length - children_length
                        if diff % 2 == 0:
                            diff1 = diff / 2
                            diff2 = diff1
                        else:
                            diff1 = diff // 2
                            diff2 = diff - diff1

                        for k, v in texts.items():
                            texts[k] = "|%s%s%s|" % ("-" * diff1, v[1:-1], "-" * diff2)

                for output, value in self.data.items():
                    output_length = len(value) + 6
                    diff = length - output_length
                    if diff % 2 == 0:
                        diff1 = diff / 2
                        diff2 = diff1
                    else:
                        diff1 = diff // 2
                        diff2 = diff - diff1
                    texts[output] = "|-%s %s %s-|" % ("-" * diff1, value, "-" * diff2)

            length = max(len(x) for x in texts.values())
            for k, v in texts.items():
                if len(v) < length:
                    texts[k] += " " * (length - len(v))

            return texts

        def _dataToString(self, data):
            if (len(data) > 1) or (len(data) == 0):
                return "X"

            value = data[data.keys()[0]]

            if isinstance(value, np.ndarray) or isinstance(value, dict):
                return "X"

            return str(value)

    def __init__(
        self,
        name,
        view_class,
        outputs_declaration,
        parameters,
        irregular_outputs=[],
        all_combinations=True,
    ):
        self.name = name
        self.view_class = view_class
        self.outputs_declaration = {}
        self.parameters = parameters
        self.irregular_outputs = irregular_outputs

        self.determine_regular_intervals(outputs_declaration)

        if all_combinations:
            for L in range(0, len(self.outputs_declaration) + 1):
                for subset in itertools.combinations(
                    self.outputs_declaration.keys(), L
                ):
                    self.run(subset)
        else:
            self.run(self.outputs_declaration.keys())

    def determine_regular_intervals(self, outputs_declaration):
        outputs = OutputList()
        for name in outputs_declaration:
            outputs.add(DatabaseTester.MockOutput(name, True))

        view = self.view_class()
        view.setup("", outputs, self.parameters)

        view.next()

        for output in outputs:
            if output.name not in self.irregular_outputs:
                self.outputs_declaration[output.name] = (
                    output.last_written_data_index + 1
                )
            else:
                self.outputs_declaration[output.name] = None

    def run(self, connected_outputs):
        if len(connected_outputs) == 0:
            return

        print(
            "Testing '%s', with %d output(s): %s"
            % (self.name, len(connected_outputs), ", ".join(connected_outputs))
        )

        # Create the mock outputs
        connected_outputs = dict(
            [x for x in self.outputs_declaration.items() if x[0] in connected_outputs]
        )

        not_connected_outputs = dict(
            [
                x
                for x in self.outputs_declaration.items()
                if x[0] not in connected_outputs
            ]
        )

        outputs = OutputList()
        for name in self.outputs_declaration.keys():
            outputs.add(DatabaseTester.MockOutput(name, name in connected_outputs))

        # Create the view
        view = self.view_class()
        view.setup("", outputs, self.parameters)

        # Initialisations
        next_expected_indices = {}
        for name, interval in connected_outputs.items():
            next_expected_indices[name] = 0

        next_index = 0

        def _done():
            for output in outputs:
                if output.isConnected() and not view.done(
                    output.last_written_data_index
                ):
                    return False
            return True

        # Ask for all the data
        while not (_done()):
            view.next()

            # Check the indices for the connected outputs
            for name in connected_outputs.keys():
                if name not in self.irregular_outputs:
                    if not (
                        outputs[name].written_data[-1][0] == next_expected_indices[name]
                    ):
                        raise OutputError("Wrong current index")
                    if not (
                        outputs[name].written_data[-1][1]
                        == next_expected_indices[name] + connected_outputs[name] - 1
                    ):
                        raise OutputError("Wrong next index")
                else:
                    if not (
                        outputs[name].written_data[-1][0] == next_expected_indices[name]
                    ):
                        raise OutputError("Wrong current index")
                    if not (
                        outputs[name].written_data[-1][1] >= next_expected_indices[name]
                    ):
                        raise OutputError("Wrong next index")

            # Check that the not connected outputs didn't produce data
            for name in not_connected_outputs.keys():
                if len(outputs[name].written_data) != 0:
                    raise OutputError("Data written on unconnected output")

            # Compute the next data index that should be produced
            next_index = 1 + min(
                [x.written_data[-1][1] for x in outputs if x.isConnected()]
            )

            # Compute the next data index that should be produced by each
            # connected output
            for name in connected_outputs.keys():
                if name not in self.irregular_outputs:
                    if (
                        next_index
                        == next_expected_indices[name] + connected_outputs[name]
                    ):
                        next_expected_indices[name] += connected_outputs[name]
                else:
                    if next_index > outputs[name].written_data[-1][1]:
                        next_expected_indices[name] = (
                            outputs[name].written_data[-1][1] + 1
                        )

        # Check the number of data produced on the regular outputs
        for name in connected_outputs.keys():
            print("  - %s: %d data" % (name, len(outputs[name].written_data)))
            if name not in self.irregular_outputs:
                if not (
                    len(outputs[name].written_data)
                    == next_index / connected_outputs[name]
                ):
                    raise OutputError("Invalid number of data produced")

        # Check that all outputs ends on the same index
        for name in connected_outputs.keys():
            if not outputs[name].written_data[-1][1] == next_index - 1:
                raise OutputError("Outputs not on same index")

        # Generate a text file with lots of details (only if all outputs are
        # connected)
        if len(connected_outputs) == len(self.outputs_declaration):
            sorted_outputs = sorted(outputs, key=lambda x: len(x.written_data))

            unit = DatabaseTester.SynchronizedUnit(
                0, sorted_outputs[0].written_data[-1][1]
            )

            for output in sorted_outputs:
                for data in output.written_data:
                    unit.addData(output.name, data[0], data[1], data[2])

            texts = unit.toString()

            outputs_max_length = max([len(x) for x in self.outputs_declaration.keys()])

            with open(self.name.replace(" ", "_") + ".txt", "w") as f:
                for i in range(1, len(sorted_outputs) + 1):
                    output_name = sorted_outputs[-i].name
                    f.write(output_name + ": ")

                    if len(output_name) < outputs_max_length:
                        f.write(" " * (outputs_max_length - len(output_name)))

                    f.write(texts[output_name] + "\n")
