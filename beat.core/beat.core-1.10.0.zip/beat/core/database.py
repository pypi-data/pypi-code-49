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

Forward importing from :py:mod:`beat.backend.python.database`:
:py:class:`beat.backend.python.database.Storage`
"""

import os

import six

from . import schema

from .dataformat import DataFormat
from .protocoltemplate import ProtocolTemplate

from . import prototypes

from beat.backend.python.database import Storage
from beat.backend.python.database import Database as BackendDatabase
from beat.backend.python.protocoltemplate import Storage as PTStorage


def get_first_procotol_template(prefix):
    pt_root_folder = os.path.join(prefix, PTStorage.asset_folder)
    pts_available = sorted(os.listdir(pt_root_folder))

    if not pts_available:
        raise RuntimeError("Invalid prefix content, no protocol template available")

    selected_protocol_template = None
    for procotol_template_folder in pts_available:
        protocol_template_versions = sorted(
            os.listdir(os.path.join(pt_root_folder, procotol_template_folder))
        )
        version = protocol_template_versions[-1].split(".")[0]
        protocol_template_name = "{}/{}".format(procotol_template_folder, version)
        protocol_template = ProtocolTemplate(prefix, protocol_template_name)
        if protocol_template.valid:
            selected_protocol_template = protocol_template_name
            break

    if selected_protocol_template is None:
        raise RuntimeError("No valid protocol template found")

    return selected_protocol_template


class Database(BackendDatabase):
    """Databases define the start point of the dataflow in an experiment.


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (dict, str): The piece of data representing the database. It must
        validate against the schema defined for databases. If a string is
        passed, it is supposed to be a valid path to an database in the
        designated prefix area.

      dataformat_cache (:py:class:`dict`, Optional): A dictionary mapping
        dataformat names to loaded dataformats. This parameter is optional and,
        if passed, may greatly speed-up database loading times as dataformats
        that are already loaded may be re-used. If you use this parameter, you
        must guarantee that the cache is refreshed as appropriate in case the
        underlying dataformats change.


    Attributes:

      name (str): The full, valid name of this database

      description (str): The short description string, loaded from the JSON
        file if one was set.

      documentation (str): The full-length docstring for this object.

      storage (object): A simple object that provides information about file
        paths for this database

      errors (list): A list containing errors found while loading this
        database.

      data (dict): The original data for this database, as loaded by our JSON
        decoder.

    """

    def __init__(self, prefix, data, dataformat_cache=None):
        super(Database, self).__init__(prefix, data, dataformat_cache)

    def _validate_view(self, view_name):
        if view_name.find(".") != -1 or view_name.find(os.sep) != -1:
            self.errors.append(
                "dataset views are required to sit inside the "
                "database root folder, but `%s' is either in a "
                "subdirectory or points to a python module, what is "
                "unsupported by this version" % (view_name)
            )

    def _load(self, data, dataformat_cache):
        """Loads the database"""

        self._name = None
        self.storage = None
        self.dataformats = {}  # preloaded dataformats
        code = None

        if isinstance(data, (tuple, list)):  # user has passed individual info

            data, code = data  # break down into two components

        if isinstance(data, six.string_types):  # user has passed a file pointer

            self._name = data
            self.storage = Storage(self.prefix, self._name)
            data = self.storage.json.path
            if not self.storage.json.exists():
                self.errors.append("Database declaration file not found: %s" % data)
                return

        # At this point, `data' can be a dictionary or ``None``
        if data is None:  # loads the default declaration for a database
            self.data, self.errors = prototypes.load("database")
            self.data["protocols"][0]["template"] = get_first_procotol_template(
                self.prefix
            )
            assert not self.errors, "\n  * %s" % "\n  *".join(self.errors)  # nosec
        else:
            # this runs basic validation, including JSON loading if required
            self.data, self.errors = schema.validate("database", data)

        if self.errors:
            return  # don't proceed with the rest of validation

        if self.storage is not None:  # loading from the disk, check code
            if not self.storage.code.exists():
                self.errors.append(
                    "Database view code not found: %s" % self.storage.code.path
                )
                return
            else:
                code = self.storage.code.load()

        # At this point, `code' can be a string (or a binary blob) or ``None``
        if code is None:  # loads the default code for an algorithm
            self.code = prototypes.binary_load("database.py")

        else:  # just assign it - notice that in this case, no language is set
            self.code = code

        if self.errors:
            return  # don't proceed with the rest of validation

        self._validate_semantics(dataformat_cache)

    def _validate_semantics(self, dataformat_cache):
        """Validates all semantical aspects of the database"""

        # all protocol names must be unique
        protocol_names = [k["name"] for k in self.data["protocols"]]
        if len(protocol_names) != len(set(protocol_names)):
            self.errors.append(
                "found different protocols with the same name: %s" % (protocol_names,)
            )

        # all set names within a protocol must be unique
        for protocol in self.data["protocols"]:
            set_names = self.set_names(protocol["name"])
            if len(set_names) != len(set(set_names)):
                self.errors.append(
                    "found different sets with the same name at protocol "
                    "`%s': %s" % (protocol["name"], set_names)
                )

            # all outputs must have valid data types
            for _, set_ in self.sets(protocol["name"]).items():

                for key, value in set_["outputs"].items():

                    if value in self.dataformats:
                        continue

                    if value in dataformat_cache:  # re-use
                        dataformat = dataformat_cache[value]
                    else:
                        dataformat = DataFormat(self.prefix, value)
                        dataformat_cache[value] = dataformat

                    self.dataformats[value] = dataformat

                    if dataformat.errors:
                        self.errors.append(
                            "found error validating data format `%s' "
                            "for output `%s' on set `%s' of protocol `%s': %s"
                            % (
                                value,
                                key,
                                set_["name"],
                                protocol["name"],
                                "\n".join(dataformat.errors),
                            )
                        )

                # all view names must be relative to the database root path
                if self.schema_version == 1:
                    self._validate_view(set_["view"])

            if self.schema_version != 1:
                for view in protocol["views"].keys():
                    self._validate_view(view)
