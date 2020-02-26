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
toolchain
=========

Validation for toolchains
"""

import collections

import simplejson as json

from . import schema
from . import prototypes
from . import utils


class Storage(utils.Storage):
    """Resolves paths for toolchains

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The name of the toolchain object in the format
        ``<user>/<name>/<version>``.
    """

    asset_type = "toolchain"
    asset_folder = "toolchains"

    def __init__(self, prefix, name):

        if name.count("/") != 2:
            raise RuntimeError("invalid toolchain name: `%s'" % name)

        self.username, self.name, self.version = name.split("/")
        self.fullname = name
        self.prefix = prefix

        path = utils.hashed_or_simple(
            self.prefix, self.asset_folder, name, suffix=".json"
        )
        path = path[:-5]

        super(Storage, self).__init__(path)


class Toolchain(object):
    """Toolchains define the dataflow in an experiment.

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (:py:class:`object`, Optional): The piece of data representing the
        toolchain.  It must validate against the schema defined for toolchains.
        If a string is passed, it is supposed to be a valid path to an
        toolchain in the designated prefix area. If ``None`` is passed, loads
        our default prototype for toolchains.


    Attributes:

      name (str): The toolchain name

      description (str): The short description string, loaded from the JSON
        file if one was set.

      documentation (str): The full-length docstring for this object.

      storage (object): A simple object that provides information about file
        paths for this toolchain

      errors (list): A list containing errors found while loading this
        toolchain.

      data (dict): The original data for this toolchain, as loaded by our JSON
        decoder.
    """

    def __init__(self, prefix, data):

        self._name = None
        self.storage = None
        self.prefix = prefix
        self.errors = []
        self.data = data
        self._load(data)

    def _load(self, data):

        self._name = None
        self.storage = None

        if data is None:  # loads prototype and validates it

            self.data, self.errors = prototypes.load("toolchain")
            assert not self.errors, "\n  * %s" % "\n  *".join(self.errors)  # nosec

        else:

            if not isinstance(data, dict):  # user has a file pointer
                self._name = data
                self.storage = Storage(self.prefix, self._name)
                if not self.storage.exists():
                    self.errors.append(
                        "Toolchain declaration file not found: %s" % data
                    )
                    return

                data = self.storage.json.path

            # this runs basic validation, including JSON loading if required
            self.data, self.errors = schema.validate("toolchain", data)

        if self.errors:
            return  # don't proceed with the rest of validation

        # these will be filled by the following methods
        channels = []
        inputs = []
        outputs = []
        names = {}
        connections = []
        loop_connections = []

        self._check_datasets(channels, outputs, names)

        self._check_blocks(channels, inputs, outputs, names)
        self._check_loops(channels, inputs, outputs, names)
        self._check_analyzers(channels, inputs, names)

        self._check_connections(channels, inputs, outputs, connections)

        self._check_representation(channels, names, connections, loop_connections)

    def _check_datasets(self, channels, outputs, names):
        """Checks all datasets"""

        for i, dataset in enumerate(self.data["datasets"]):

            if dataset["name"] in names:
                self.errors.append(
                    "/datasets/[#%d]/name: duplicated name, first "
                    "occurance of '%s' happened at '%s'"
                    % (i, dataset["name"], names[dataset["name"]])
                )
            else:
                names[dataset["name"]] = "/datasets/%s[#%d]" % (dataset["name"], i)
                channels.append(dataset["name"])

            outputs += ["%s.%s" % (dataset["name"], k) for k in dataset["outputs"]]

        return channels, outputs, names

    def _check_blocks(self, channels, inputs, outputs, names):
        """Checks all blocks"""

        for i, block in enumerate(self.data["blocks"]):

            if block["name"] in names:
                self.errors.append(
                    "/blocks/[#%d]/name: duplicated name, first "
                    "occurance of '%s' happened at '%s'"
                    % (i, block["name"], names[block["name"]])
                )
            else:
                names[block["name"]] = "/blocks/%s[#%d]" % (block["name"], i)

            inputs += ["%s.%s" % (block["name"], k) for k in block["inputs"]]
            outputs += ["%s.%s" % (block["name"], k) for k in block["outputs"]]

            if block["synchronized_channel"] not in channels:
                self.errors.append(
                    "/blocks/%s[#%d]/synchronized_channel: invalid "
                    "synchronization channel '%s'"
                    % (block["name"], i, block["synchronized_channel"])
                )

        return channels, inputs, outputs, names

    def _check_loops(self, channels, inputs, outputs, names):
        """ Check all loops"""

        if "loops" in self.data:
            for i, loop in enumerate(self.data["loops"]):
                loop_name = loop["name"]

                if loop_name in names:
                    self.errors.append(
                        "/loops/[#%d]/name: duplicated name, first "
                        "occurance of '%s' happened at '%s'"
                        % (i, loop_name, names[loop_name])
                    )
                else:
                    names[loop_name] = "/loops/%s[#%d]" % (loop_name, i)

                for prefix in ["processor_", "evaluator_"]:
                    inputs += [
                        "%s.%s" % (loop_name, k) for k in loop[prefix + "inputs"]
                    ]
                    outputs += [
                        "%s.%s" % (loop["name"], k) for k in loop[prefix + "outputs"]
                    ]

                if loop["synchronized_channel"] not in channels:
                    self.errors.append(
                        "/loops/%s[#%d]/synchronized_channel: "
                        "invalid synchronization channel '%s'"
                        % (loop_name, i, loop["synchronized_channel"])
                    )

        return channels, inputs, outputs, names

    def _check_analyzers(self, channels, inputs, names):
        """Checks all analyzers"""

        for i, analyzer in enumerate(self.data["analyzers"]):

            if analyzer["name"] in names:
                self.errors.append(
                    "/analyzers/[#%d]/name: duplicated name, first "
                    "occurance of '%s' happened at '%s'"
                    % (i, analyzer["name"], names[analyzer["name"]])
                )
            else:
                names[analyzer["name"]] = "/analyzers/%s[#%d]" % (analyzer["name"], i)

            inputs += ["%s.%s" % (analyzer["name"], k) for k in analyzer["inputs"]]

            if analyzer["synchronized_channel"] not in channels:
                self.errors.append(
                    "/analyzers/%s[#%d]/synchronized_channel: "
                    "invalid synchronization channel '%s'"
                    % (analyzer["name"], i, analyzer["synchronized_channel"])
                )

    def _check_connections(self, channels, inputs, outputs, connections):
        """Checks connection consistency"""

        input_endpoints = dict()
        unconnected_inputs = set(inputs)

        for i, connection in enumerate(self.data["connections"]):

            # checks no 2 connections arrive at the same input
            if connection["to"] in input_endpoints:
                connected = input_endpoints[connection["to"]]
                self.errors.append(
                    "/connection/%s->%s[#%d]/: ending on the same "
                    "input as /connection/%s->%s[#%d] is unsupported"
                    % (
                        connection["from"],
                        connection["to"],
                        i,
                        connected["from"],
                        connection["to"],
                        connected["position"],
                    )
                )
            else:
                input_endpoints[connection["to"]] = {
                    "from": connection["from"],
                    "position": i,
                }

            if connection["from"] not in outputs:
                self.errors.append(
                    "/connections/%s->%s[#%d]/: invalid output endpoint '%s'"
                    % (connection["from"], connection["to"], i, connection["from"])
                )

            if connection["to"] not in inputs:
                self.errors.append(
                    "/connections/%s->%s[#%d]/: invalid input "
                    "endpoint '%s'"
                    % (connection["from"], connection["to"], i, connection["to"])
                )
            else:
                # we now know this input is connected at least once
                if connection["to"] in unconnected_inputs:
                    unconnected_inputs.remove(connection["to"])

            if connection["channel"] not in channels:
                self.errors.append(
                    "/connections/%s->%s[#d]/channel: invalid "
                    "synchronization channel '%s'"
                    % (connection["from"], connection["to"], connection["channel"])
                )

            connections.append("%s/%s" % (connection["from"], connection["to"]))

        if len(unconnected_inputs) != 0:
            self.errors.append(
                "input(s) `%s' remain unconnected" % (", ".join(unconnected_inputs),)
            )

    def _check_representation(self, channels, names, connections, loop_connections):
        """Checks the representation for this toolchain"""

        # all connections must exist
        for connection in self.data["representation"]["connections"]:
            if connection not in connections:
                self.errors.append(
                    "/representation/connections/%s: not listed "
                    "on /connections" % connection
                )

        # all blocks must exist
        for block in self.data["representation"]["blocks"]:
            if block not in names:
                self.errors.append(
                    "/representation/blocks/%s: not listed on "
                    "/datasets, /blocks or /analyzers" % block
                )

        # all channel colors must be a valid dataset name
        for channel in self.data["representation"]["channel_colors"]:
            if channel not in channels:
                self.errors.append(
                    "/representation/channel_colors/%s: not a "
                    "dataset listed on /datasets" % channel
                )

    @property
    def schema_version(self):
        """Returns the schema version"""
        return self.data.get("schema_version", 1)

    @property
    def name(self):
        """Returns the name of this object"""

        return self._name or "__unnamed_toolchain__"

    @name.setter
    def name(self, value):
        self._name = value
        self.storage = Storage(self.prefix, value)

    @property
    def datasets(self):
        """All declared datasets"""

        data = self.data["datasets"]
        return dict(zip([k["name"] for k in data], data))

    @property
    def blocks(self):
        """All declared blocks"""

        data = self.data["blocks"]
        return dict(zip([k["name"] for k in data], data))

    @property
    def loops(self):
        """All declared loops"""

        data = self.data.get("loops", {})
        return dict(zip([k["name"] for k in data], data))

    @property
    def analyzers(self):
        """All declared analyzers"""

        data = self.data["analyzers"]
        return dict(zip([k["name"] for k in data], data))

    def algorithm_item(self, name):
        """ Returns a block, loop or analyzer matching the name given"""

        item = None

        for algo_items in [self.blocks, self.loops, self.analyzers]:

            if name in algo_items:
                item = algo_items.get(name)
                break
        return item

    @property
    def connections(self):
        """All declared connections"""

        return self.data["connections"]

    def dependencies(self, name):
        """Returns the block dependencies for a given block/analyzer in a set

        The calculation uses all declared connections for that block/analyzer.
        Dataset connections are ignored.
        """

        dependencies = set()
        datasets = self.datasets  # property - does some work nevertheless
        for conn in self.data["connections"]:
            from_ = conn["from"].split(".", 1)[0]
            to_ = conn["to"].split(".", 1)[0]
            if to_ == name and from_ not in datasets:
                dependencies.add(from_)
        return dependencies

    def execution_order(self):
        """Returns the execution order in an ordered dictionary with block
        deps.
        """

        items = [
            k["name"]
            for k in self.data["blocks"]
            + self.data.get("loops", [])
            + self.data["analyzers"]
        ]
        deps = dict(zip(items, [self.dependencies(k) for k in items]))
        queue = collections.OrderedDict()

        while len(items) != len(queue):  # while there are blocks/analyzers to treat
            insert = collections.OrderedDict()
            for k in items:
                # if block has no executed deps
                if k not in queue and deps[k].issubset(queue.keys()):
                    insert[k] = deps[k]  # insert into queue
                queue.update(insert)

        return queue

    def dot_diagram(
        self,
        title=None,
        label_callback=None,
        edge_callback=None,
        result_callback=None,
        is_layout=False,
    ):
        """Returns a dot diagram representation of the toolchain

        Parameters:

          title (str): A title for the generated drawing. If ``None`` is given,
            then prints out the toolchain name.

          label_callback (:std:term:`function`): A python function that is
            called back each time a label needs to be inserted into a block.
            The prototype of this function is ``label_callback(type, name)``.
            ``type`` may be one of ``dataset``, ``block`` or ``analyzer``. This
            callback is used by the experiment class to complement diagram
            information before plotting.

          edge_callback (:std:term:`function`): A python function that is
            called back each time an edge needs to be inserted into the graph.
            The prototype of this function is ``edge_callback(start)``.
            ``start`` is the name of the starting point for the connection, it
            should determine the dataformat for the connection.

          result_callback (:std:term:`function`): A function to draw ports on
            analyzer blocks.  The prototype of this function is
            ``result_callback(name, color)``.


        Returns

          graphviz.Digraph: With the graph ready for show-time.

        """

        # the representation for channel colors must be complete
        all_colors = set(self.data["representation"]["channel_colors"].keys())
        channels = set([k["name"] for k in self.data["datasets"]])
        missing = channels - all_colors
        if missing:
            raise KeyError(
                "/representation/channel_colors/%s: is missing "
                "from object descriptor - fix it before drawing" % ",".join(missing)
            )

        label_callback = None
        if is_layout:
            label_callback = label_callback or (lambda x, y: "%s" % y)
        else:
            label_callback = label_callback or (lambda x, y: "<b><u>%s</u></b>" % y)

        edge_callback = edge_callback or (lambda x: "")
        result_callback = result_callback or (lambda x: [])
        title = title or "Toolchain: %s" % self.name
        channel_colors = self.data["representation"]["channel_colors"]

        from .drawing import make_label as make_drawing_label, make_layout_label
        from graphviz import Digraph

        fontname = "Helvetica"
        fontsize = "12"

        make_label = make_layout_label if is_layout else make_drawing_label
        root = Digraph(self.name)
        splineType = "line" if is_layout else "polyline"
        # default is 0.25, but it seems 0.5 is needed to keep everything separated
        # when the layout is parsed by beat.editor
        nodesep = "0.5" if is_layout else "0.25"
        root.attr(
            "graph",
            rankdir="LR",
            compound="true",
            splines=splineType,
            labelloc="t",
            label=title,
            fontname=fontname,
            fontsize=str(3 * int(fontsize)),
            nodesep=nodesep,
        )

        datasets = Digraph("dataset_cluster")
        datasets.attr("graph", rank="same", label="datasets")

        for d, info in self.datasets.items():
            datasets.node(
                d,
                label=make_label(
                    [], label_callback("dataset", d), info["outputs"], channel_colors[d]
                ),
                shape="none",
                fontsize=fontsize,
                fontname=fontname,
            )

        root.subgraph(datasets)

        def _draw_block(graph, n, info):
            color = channel_colors[info["synchronized_channel"]]

            if "outputs" in info:
                label = make_label(
                    info["inputs"], label_callback("block", n), info["outputs"], color
                )
            else:
                label = make_label(
                    info["inputs"],
                    label_callback("analyzer", n),
                    result_callback(n),
                    color,
                )

            root.node(
                n, label=label, shape="none", fontsize=fontsize, fontname=fontname
            )

            for c in [k for k in self.connections if k["to"].startswith(n + ".")]:
                edge_color = channel_colors[c["channel"]]
                if is_layout:
                    label = edge_callback(c["from"])
                    root.body.append(
                        '\t%s:e -> %s:w [color="%s"]'
                        % (
                            c["from"].replace(".", ":output_"),
                            c["to"].replace(".", ":input_"),
                            edge_color,
                        )
                    )
                else:
                    root.edge(
                        c["from"].replace(".", ":output_"),
                        c["to"].replace(".", ":input_"),
                        color=edge_color,
                        label=edge_callback(c["from"]),
                        fontcolor=color,
                        fontsize=fontsize,
                        fontname=fontname,
                    )

        for name, info in self.blocks.items():
            _draw_block(root, name, info)

        analyzers = Digraph("analyzer_cluster")
        analyzers.attr("graph", rank="same", label="analyzers")

        for name, info in self.analyzers.items():
            _draw_block(analyzers, name, info)

        root.subgraph(analyzers)

        return root

    @property
    def valid(self):
        """A boolean that indicates if this toolchain is valid or not"""

        return not bool(self.errors)

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
            raise RuntimeError("toolchain has no name")

        if self.storage.doc.exists():
            return self.storage.doc.load()
        return None

    @documentation.setter
    def documentation(self, value):
        """Sets the full-length description for this object"""

        if not self._name:
            raise RuntimeError("toolchain has no name")

        if hasattr(value, "read"):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)

    def hash(self):
        """Returns the hexadecimal hash for its declaration"""

        if not self._name:
            raise RuntimeError("toolchain has no name")

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
            if not self._name:
                raise RuntimeError("toolchain has no name")
            storage = self.storage  # overwrite

        storage.save(str(self), self.description)
