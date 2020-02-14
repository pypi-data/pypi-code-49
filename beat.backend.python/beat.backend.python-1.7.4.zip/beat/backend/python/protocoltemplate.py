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
protocoltemplates
========

Validation of database protocol templates
"""

import simplejson as json

from .dataformat import DataFormat

from . import utils


# ----------------------------------------------------------


class Storage(utils.Storage):
    """Resolves paths for protocol templates

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The name of the protocol template object in the format
        ``<name>/<version>``.

    """

    asset_type = "protocoltemplate"
    asset_folder = "protocoltemplates"

    def __init__(self, prefix, name):

        if name.count("/") != 1:
            raise RuntimeError("invalid protocol template name: `%s'" % name)

        self.name, self.version = name.split("/")
        self.fullname = name
        self.prefix = prefix

        path = utils.hashed_or_simple(
            self.prefix, self.asset_folder, name, suffix=".json"
        )
        path = path[:-5]
        super(Storage, self).__init__(path)


# ----------------------------------------------------------


class ProtocolTemplate(object):
    """Protocol template define the design of the database.


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The fully qualified protocol template name (e.g. ``db/1``)

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

    def _load(self, data, dataformat_cache):
        """Loads the protocol template"""

        self._name = data

        self.storage = Storage(self.prefix, self._name)
        json_path = self.storage.json.path
        if not self.storage.json.exists():
            self.errors.append(
                "Protocol template declaration file not found: %s" % json_path
            )
            return

        with open(json_path, "rt") as f:
            try:
                self.data = json.loads(
                    f.read(), object_pairs_hook=utils.error_on_duplicate_key_hook
                )
            except RuntimeError as error:
                self.errors.append(
                    "Protocol template declaration file invalid: %s" % error
                )
                return

            for set_ in self.data["sets"]:

                for key, value in set_["outputs"].items():

                    if value in self.dataformats:
                        continue

                    if value in dataformat_cache:
                        dataformat = dataformat_cache[value]
                    else:
                        dataformat = DataFormat(self.prefix, value)
                        dataformat_cache[value] = dataformat

                    self.dataformats[value] = dataformat

    @property
    def name(self):
        """Returns the name of this object
        """
        return self._name or "__unnamed_protocoltemplate__"

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
            raise RuntimeError("protocol template has no name")

        if hasattr(value, "read"):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)

    def hash(self):
        """Returns the hexadecimal hash for its declaration"""

        if not self._name:
            raise RuntimeError("protocol template has no name")

        return self.storage.hash()

    @property
    def schema_version(self):
        """Returns the schema version"""
        return self.data.get("schema_version", 1)

    @property
    def valid(self):
        """A boolean that indicates if this database is valid or not"""

        return not bool(self.errors)

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
                raise RuntimeError("protocol template has no name")
            storage = self.storage  # overwrite

        storage.save(str(self), self.description)

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
            raise RuntimeError("protocol template has no name")

        if not self.valid:
            raise RuntimeError("protocol template is not valid")

        if prefix == self.prefix:
            raise RuntimeError(
                "Cannot export protocol template to the same prefix (" "%s)" % prefix
            )

        for k in self.dataformats.values():
            k.export(prefix)

        self.write(Storage(prefix, self.name))

    def sets(self):
        """Returns all the sets available in this protocol template"""

        return self.data["sets"]

    def set(self, name):
        """Returns the set requested

        Parameters:
          name (str): name of the set to retrieve
        """

        set_ = None
        for item in self.data["sets"]:
            if item["name"] == name:
                set_ = item
                break
        return set_
