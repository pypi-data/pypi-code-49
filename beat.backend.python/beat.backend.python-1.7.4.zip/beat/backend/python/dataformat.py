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
dataformat
==========

Validation and parsing for dataformats
"""

import re
import copy

import six
import numpy
import simplejson as json

from . import utils
from .baseformat import baseformat


# ----------------------------------------------------------


class Storage(utils.Storage):
    """Resolves paths for dataformats

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The name of the dataformat object in the format
        ``<user>/<name>/<version>``.

    """

    asset_type = "dataformat"
    asset_folder = "dataformats"

    def __init__(self, prefix, name):

        if name.count("/") != 2:
            raise RuntimeError("invalid dataformat name: `%s'" % name)

        self.username, self.name, self.version = name.split("/")
        self.fullname = name
        self.prefix = prefix

        path = utils.hashed_or_simple(
            self.prefix, self.asset_folder, name, suffix=".json"
        )
        path = path[:-5]
        super(Storage, self).__init__(path)

    def hash(self):
        """The 64-character hash of the database declaration JSON"""
        return super(Storage, self).hash("#description")


# ----------------------------------------------------------


class DataFormat(object):
    """Data formats define the chunks of data that circulate between blocks.

    Parameters:

      prefix (str): Establishes the prefix of
        your installation.

      data (str, dict): The fully qualified algorithm name (e.g. ``user/algo/1``)
        or a dictionary representing the data format (for analyzer results).

      parent (:py:class:`tuple`, Optional): The parent DataFormat for this
        format. If set to ``None``, this means this dataformat is the first one
        on the hierarchy tree. If set to a tuple, the contents are
        ``(format-instance, field-name)``, which indicates the originating
        object that is this object's parent and the name of the field on that
        object that points to this one.

      dataformat_cache (:py:class:`dict`, Optional): A dictionary mapping
        dataformat names to loaded dataformats. This parameter is optional and,
        if passed, may greatly speed-up data format loading times as
        dataformats that are already loaded may be re-used. If you use this
        parameter, you must guarantee that the cache is refreshed as
        appropriate in case the underlying dataformats change.

    Attributes:

      name (str): The full, valid name of this dataformat

      description (str): The short description string, loaded from the JSON
        file if one was set.

      documentation (str): The full-length docstring for this object.

      storage (object): A simple object that provides information about file
        paths for this dataformat

      errors (list): A list strings containing errors found while loading this
        dataformat.

      data (dict): The original data for this dataformat, as loaded by our JSON
        decoder.

      resolved (dict): A dictionary similar to :py:attr:`data`, but with
        references fully resolved.

      referenced (dict): A dictionary pointing to all loaded dataformats.

      parent (dataformat.DataFormat): The pointer to the
        dataformat to which the current format is part of. It is useful for
        internal error reporting.

    """

    def __init__(self, prefix, data, parent=None, dataformat_cache=None):

        self._name = None
        self.storage = None
        self.resolved = None
        self.prefix = prefix
        self.errors = []
        self.data = None
        self.resolved = None
        self.referenced = {}
        self.parent = parent

        # if the user has not provided a cache, still use one for performance
        dataformat_cache = dataformat_cache if dataformat_cache is not None else {}

        try:
            self._load(data, dataformat_cache)
        finally:
            if self._name is not None:  # registers it into the cache, even if failed
                dataformat_cache[self._name] = self

    def _load(self, data, dataformat_cache):
        """Loads the dataformat"""

        if isinstance(data, dict):
            self._name = "analysis:result"
            self.data = data
        else:
            self._name = data
            self.storage = Storage(self.prefix, data)
            json_path = self.storage.json.path
            if not self.storage.exists():
                self.errors.append(
                    "Dataformat declaration file not found: %s" % json_path
                )
                return

            with open(json_path, "rb") as f:
                try:
                    self.data = json.loads(
                        f.read().decode("utf-8"),
                        object_pairs_hook=utils.error_on_duplicate_key_hook,
                    )
                except RuntimeError as error:
                    self.errors.append(
                        "Dataformat declaration file invalid: %s" % error
                    )
                    return

        dataformat_cache[self._name] = self  # registers itself into the cache

        self.resolved = copy.deepcopy(self.data)

        # remove reserved fields
        def is_reserved(x):
            """Returns if the field name is a reserved name"""
            return (x.startswith("__") and x.endswith("__")) or x in (
                "#description",
                "#schema_version",
            )

        for key in list(self.resolved):
            if is_reserved(key):
                del self.resolved[key]

        def maybe_load_format(name, obj, dataformat_cache):
            """Tries to load a given dataformat from its relative path"""

            if isinstance(obj, six.string_types) and obj.find("/") != -1:  # load it

                if obj in dataformat_cache:  # reuse

                    if dataformat_cache[obj] is None:  # recursion detected
                        return self

                    self.referenced[obj] = dataformat_cache[obj]

                else:  # load it
                    self.referenced[obj] = DataFormat(
                        self.prefix, obj, (self, name), dataformat_cache
                    )

                return self.referenced[obj]

            elif isinstance(obj, dict):  # can cache it, must load from scratch
                return DataFormat(self.prefix, obj, (self, name), dataformat_cache)

            elif isinstance(obj, list):
                retval = copy.deepcopy(obj)
                retval[-1] = maybe_load_format(field, obj[-1], dataformat_cache)
                return retval

            return obj

        # now checks that every referred dataformat is loaded, resolves it
        for field, value in self.data.items():
            if field in ("#description", "#schema_version"):
                continue  # skip the description and schema version meta attributes
            self.resolved[field] = maybe_load_format(field, value, dataformat_cache)

        # at this point, there should be no more external references in
        # ``self.resolved``. We treat the "#extends" property, which requires a
        # special handling, given its nature.
        if "#extends" in self.resolved:

            ext = self.data["#extends"]
            self.referenced[ext] = maybe_load_format(self._name, ext, dataformat_cache)
            basetype = self.resolved["#extends"]
            tmp = self.resolved
            self.resolved = basetype.resolved
            self.resolved.update(tmp)
            del self.resolved["#extends"]  # avoids infinite recursion

    @property
    def name(self):
        """Returns the name of this object, either from the filename or composed
        from the hierarchy it belongs.
        """
        if self.parent and self._name is None:
            return self.parent[0].name + "." + self.parent[1] + "_type"
        else:
            return self._name or "__unnamed_dataformat__"

    @name.setter
    def name(self, value):
        self._name = value
        self.storage = Storage(self.prefix, value)

    @property
    def schema_version(self):
        """Returns the schema version"""
        return self.data.get("#schema_version", 1)

    @property
    def extends(self):
        """If this dataformat extends another one, this is it, otherwise ``None``
        """
        return self.data.get("#extends")

    @property
    def type(self):
        """Returns a new type that can create instances of this dataformat.

        The new returned type provides a basis to construct new objects which
        represent the dataformat. It provides a simple JSON serializer and a
        for-screen representation.

        Example:

          To create an object respecting the data format from a JSON
          descriptor, use the following technique:

          .. code-block:: python

            ftype = dataformat(...).type
            json = simplejson.loads(...)
            newobj = ftype(**json) # instantiates the new object, checks format

          To dump the object into JSON, use the following technique:

          .. code-block:: python

             simplejson.dumps(newobj.as_dict(), indent=4)

          A string representation of the object uses the technique above to
          pretty-print the object contents to the screen.
        """

        if self.resolved is None:
            raise RuntimeError(
                "Cannot prototype while not properly initialized\n{}".format(
                    self.errors
                )
            )

        classname = re.sub(r"[-/]", "_", self.name)
        if not isinstance(classname, str):
            classname = str(classname)

        def init(self, **kwargs):
            baseformat.__init__(self, **kwargs)

        attributes = dict(__init__=init, _name=self.name, _format=self.resolved)

        # create the converters for the class we're about to return
        for k, v in self.resolved.items():

            if isinstance(v, list):  # it is an array
                attributes[k] = copy.deepcopy(v)
                if isinstance(v[-1], DataFormat):
                    attributes[k][-1] = v[-1].type
                else:
                    if v[-1] in ("string", "str"):
                        attributes[k][-1] = str
                    else:
                        attributes[k][-1] = numpy.dtype(v[-1])

            elif isinstance(v, DataFormat):  # it is another dataformat
                attributes[k] = v.type

            else:  # it is a simple type
                if v in ("string", "str"):
                    attributes[k] = str
                else:
                    attributes[k] = numpy.dtype(v)

        return type(classname, (baseformat,), attributes)

    @property
    def valid(self):
        """A boolean that indicates if this dataformat is valid or not"""
        return not bool(self.errors)

    @property
    def description(self):
        """The short description for this object"""
        return self.data.get("#description", None)

    @description.setter
    def description(self, value):
        """Sets the short description for this object"""
        self.data["#description"] = value

    @property
    def documentation(self):
        """The full-length description for this object"""

        if not self._name:
            raise RuntimeError("dataformat has no name")

        if self.storage.doc.exists():
            return self.storage.doc.load()
        return None

    @documentation.setter
    def documentation(self, value):
        """Sets the full-length description for this object"""

        if not self._name:
            raise RuntimeError("dataformat has no name")

        if hasattr(value, "read"):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)

    def hash(self):
        """Returns the hexadecimal hash for its declaration"""

        if not self._name:
            raise RuntimeError("dataformat has no name")

        return self.storage.hash()

    def validate(self, data):
        """Validates a piece of data provided by the user

        In order to validate, the data object must be complete and
        safe-castable to this dataformat. For any other validation operation
        that would require special settings, use instead the :py:meth:`type`
        method to generate a valid type and use either ``from_dict``,
        ``unpack`` or ``unpack_from`` depending on your use-case.

        Parameters:

          data (dict, str, :std:term:`file object`): This parameter represents
            the data to be validated.  It may be a dictionary with the JSON
            representation of a data blob or, else, a binary blob (represented
            by either a string or a file descriptor object) from which the data
            will be read. If problems occur, an exception is raised.

        Returns:

          ``None``: Raises if an error occurs.
        """

        obj = self.type()
        if isinstance(data, dict):
            obj.from_dict(data, casting="safe", add_defaults=False)
        elif isinstance(data, six.string_types):
            obj.unpack(data)
        else:
            obj.unpack_from(data)

    def isparent(self, other):
        """Tells if the other object extends self (directly or indirectly).

        Parameters:

          other (DataFormat): another object to check


        Returns:

          bool: ``True``, if ``other`` is a parent of ``self``. ``False``
            otherwise.

        """

        if other.extends:
            if self.name == other.extends:
                return True
            else:
                return self.isparent(other.referenced[other.extends])

        return False

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
                raise RuntimeError("dataformat has no name")
            storage = self.storage  # overwrite

        storage.save(str(self), self.description)

    def export(self, prefix):
        """Recursively exports itself into another prefix

        Other required dataformats are also copied.


        Parameters:

          prefix (str): Establishes the prefix of your installation.


        Returns:

          None


        Raises:

          RuntimeError: If prefix and self.prefix point to the same directory.

        """

        if not self._name:
            raise RuntimeError("dataformat has no name")

        if not self.valid:
            raise RuntimeError("dataformat is not valid:\n{}".format(self.errors))

        if prefix == self.prefix:
            raise RuntimeError(
                "Cannot export dataformat to the same prefix (" "%s)" % prefix
            )

        for k in self.referenced.values():
            k.export(prefix)

        self.write(Storage(prefix, self.name))
