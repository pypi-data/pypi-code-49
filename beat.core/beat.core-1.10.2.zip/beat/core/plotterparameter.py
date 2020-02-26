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
================
plotterparameter
================

Validation for plotterparameters
"""

import simplejson as json

from . import schema
from . import prototypes
from . import utils
from . import plotter


class Storage(utils.Storage):
    """Resolves paths for plotterparameters

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      name (str): The name of the plotterparameter object in the format
        ``<user>/<plotterparameter-name>/<version>``
    """

    asset_type = "plotterparameter"
    asset_folder = "plotterparameters"

    def __init__(self, prefix, name):

        if name.count("/") != 2:
            raise RuntimeError(f"invalid plotterparameter name: {name}")

        self.username, self.name, self.version = name.split("/")
        self.fullname = name
        self.prefix = prefix

        path = utils.hashed_or_simple(
            self.prefix, self.asset_folder, name, suffix=".json"
        )
        path = path[:-5]

        super(Storage, self).__init__(path)


# ----------------------------------------------------------


class Plotterparameter(object):
    """Each plotterparameter is a specific configuration for the specified
    plotter. Plotterparameters configure all the parameters of the plotter,
    much like an experiment contains configurations for the
    algorithms'/databases' parameters.

    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (:py:class:`object`, Optional): The piece of data representing the
        plotterparameter. It must validate against the schema defined for
        plotterparameters. If a string is passed, it is supposed to be a valid
        path to a plotterparameter in the designated prefix area.

      plotter_cache (:py:class:`dict`, Optional): A dictionary mapping
        plotter names to loaded plotters. This parameter is optional and,
        if passed, may greatly speed-up algorithm loading times as plotters
        that are already loaded may be re-used.

    Attributes:

      name (str): The plotterparameter name

      description (str): The short description string, loaded from the JSON
        file if one was set.

      documentation (str): The full-length docstring for this object.

      storage (object): A simple object that provides information about file
        paths for this plotterparameter

      plotter (object): An object of type :py:class:`.plotter.Plotter`
        that represents the plotter to which this plotterparameter is applicable.

      errors (list): A list strings containing errors found while loading this
        plotterparameter.

      data (dict): The original data for this plotterparameter, as loaded by our
        JSON decoder.
    """

    def __init__(self, prefix, data, plotter_cache=None):
        self._name = None
        self.storage = None
        self.errors = []
        self.data = None
        self.plotter = None
        self.prefix = prefix

        plotter_cache = plotter_cache if plotter_cache is not None else {}
        self._load(data, plotter_cache)

    def _load(self, data, plotter_cache):
        """Loads the plotterparameter"""

        self._load_data(data)

        if self.errors:
            return  # don't proceed with the rest of validation

        self._load_plotter(plotter_cache)

        if self.errors:
            return  # don't proceed with the rest of validation

        self._validate_data()

    def _load_data(self, data):
        """Loads given plotterparameter data
        and the plotterparameter's name

        Parameters:

          data (str): a string (the name of the param),
            an object (the param data),
            or a tuple/list (the param data & the plotter data)
        """
        # first load the raw plotterparameter data, if data isnt None
        if isinstance(data, (tuple, list)):  # the user has passed a tuple
            data, self.plotter = data
        elif isinstance(data, str):  # user has passed the name
            self._name = data
            self.storage = Storage(self.prefix, self._name)
            if not self.storage.json.exists():
                self.errors.append(
                    f"Plotterparameter declaration file not found: {data}"
                )
                return
            data = self.storage.json.path  # loads data from JSON declaration

        # At this point, `data' can be a dictionary or ``None``
        # Either way, assign something valid to `self.data'
        if data is None:  # use the dummy plotterparameter
            self.data, self.errors = prototypes.load("plotterparameter")
            assert not self.errors, "\n  * %s" % "\n  *".join(self.errors)  # nosec
        else:
            # this runs basic validation, including JSON loading if required
            self.data, self.errors = schema.validate("plotterparameter", data)

    def _load_plotter(self, plotter_cache):
        """Loads the plotter for the plotterparameter.
        Assumes that `self.data' has been calculated.

        Parameters:

          plotter_cache (:py:class:`dict`): a dict mapping plotter names
          to already-loaded plotter objects
        """
        # find the plotter if it wasnt given
        if self.plotter is None:
            plotter_name = self.data["plotter"]

            pl = None
            if plotter_name in plotter_cache:
                pl = plotter_cache[plotter_name]
            else:
                pl = plotter.Plotter(self.prefix, plotter_name)

            if pl.errors:
                self.errors.extend(pl.errors)
                return

            plotter_cache[plotter_name] = pl
            self.plotter = pl

    def _validate_data(self):
        """Validates that the properties in the plotterparameter's
        data properly configure the plotter's fields
        """
        for key, val in self.data["data"].items():
            try:
                self.plotter.clean_parameter(key, val)
            except KeyError:
                self.errors.append(
                    f"'{key}' isn't a parameter for plotter {self.plotter.name}"
                )
                return
            except ValueError:
                self.errors.append(
                    f"'{val}' is invalid for parameter {key} of plotter {self.plotter.name}"
                )
                return

    @property
    def valid(self):
        """A boolean that indicates if this plotterparameter is valid or not"""
        return not bool(self.errors)

    @property
    def name(self):
        """Returns the name of this object"""
        return self._name or "__unnamed_plotterparameter__"

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
            raise RuntimeError("plotterparameter has no name")

        if self.storage.doc.exists():
            return self.storage.doc.load()
        return None

    @documentation.setter
    def documentation(self, value):
        """Sets the full-length description for this object"""

        if not self._name:
            raise RuntimeError("plotterparameter has no name")

        if callable(getattr(value, "read", None)):
            self.storage.doc.save(value.read())
        else:
            self.storage.doc.save(value)

    def hash(self):
        """Returns the hexadecimal hash for the current plotterparameter"""

        if not self._name:
            raise RuntimeError("plotterparameter has no name")

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
                raise RuntimeError("plotterparameter has no name")
            storage = self.storage  # overwrite

        storage.save(str(self), self.description)
