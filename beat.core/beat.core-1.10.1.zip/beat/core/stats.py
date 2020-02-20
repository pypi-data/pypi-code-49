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
=====
stats
=====

A class that can read, validate and update statistical information

Forward impored from :py:mod:`beat.backend.python.stats`:
:py:func:`beat.backend.python.stats.io_statistics`
:py:func:`beat.backend.python.stats.update`
"""


import os
import copy

import simplejson as json

from . import schema
from . import prototypes

from beat.backend.python.stats import io_statistics  # noqa
from beat.backend.python.stats import update  # noqa


class Statistics(object):
    """Statistics define resource usage for algorithmic code runs


    Parameters:

      data (:py:class:`object`, Optional): The piece of data representing the
        statistics the be read, it must validate against our pre-defined
        execution schema. If the input is ``None`` or empty, then start a new
        statistics from scratch.


    Attributes:

      errors (list): A list strings containing errors found while loading this
        statistics information.

      data (dict): The original data for these statistics

    """

    def __init__(self, data=None):

        self.errors = []

        if data:
            self._load(data)  # also runs validation
        else:
            self._data, self.errors = prototypes.load("statistics")  # also validates

    def _load(self, data):
        """Loads the statistics

        Parameters:

          data (object, str, file): The piece of data to load. The input can be
            a valid python object that represents a JSON structure, a file,
            from which the JSON contents will be read out or a string. See
            :py:func:`schema.validate` for more details.
        """

        # reset
        self._data = None
        self.errors = []

        if not isinstance(data, dict):  # user has passed a file pointer
            if not os.path.exists(data):
                self.errors.append("File not found: %s" % data)
                return

        # this runs basic validation, including JSON loading if required
        self._data, self.errors = schema.validate("statistics", data)
        if self.errors:
            return  # don't proceed with the rest of validation

    @property
    def schema_version(self):
        """Returns the schema version"""

        return self.data.get("schema_version", 1)

    @property
    def cpu(self):
        """Returns only CPU information"""

        return self._data["cpu"]

    @cpu.setter
    def cpu(self, data):
        """Sets the CPU information"""

        for key in ("user", "system", "total"):
            self._data["cpu"][key] = data[key]

        for key in ("voluntary", "involuntary"):
            self._data["cpu"]["context_switches"][key] = data["context_switches"][key]

    @property
    def memory(self):
        """Returns only memory information"""

        return self._data["memory"]

    @memory.setter
    def memory(self, data):
        """Sets only the memory information"""

        for key in ("rss",):
            self._data["memory"][key] = data[key]

    @property
    def data(self):
        """Returns only I/O information"""

        return self._data["data"]

    @data.setter
    def data(self, data):
        """Sets only the I/O information"""

        for key in ("volume", "blocks", "time"):
            self._data["data"][key]["read"] = data[key]["read"]
            self._data["data"][key]["write"] = data[key]["write"]

        self._data["data"]["files"] = list(data["files"])
        self._data["network"] = data["network"]

    @property
    def valid(self):
        """A boolean that indicates if this executor is valid or not"""

        return not bool(self.errors)

    def __add__(self, other):
        """Adds two statistics data blocks"""

        retval = Statistics(copy.deepcopy(self._data))
        retval += other
        return retval

    def __iadd__(self, other):
        """Self-add statistics from another block"""

        if not isinstance(other, Statistics):
            return NotImplemented

        for key in ("user", "system", "total"):
            self._data["cpu"][key] += other._data["cpu"][key]

        for key in ("voluntary", "involuntary"):
            self._data["cpu"]["context_switches"][key] += other._data["cpu"][
                "context_switches"
            ][key]

        for key in ("rss",):  # gets the maximum between the two
            self._data["memory"][key] = max(
                other._data["memory"][key], self._data["memory"][key]
            )

        for key in ("volume", "blocks", "time"):
            self._data["data"][key]["read"] += other._data["data"][key]["read"]
            self._data["data"][key]["write"] += other._data["data"][key]["write"]

        self._data["data"]["files"] += other._data["data"]["files"]

        self._data["data"]["network"]["wait_time"] += other._data["data"]["network"][
            "wait_time"
        ]

        return self

    def __str__(self):

        return self.as_json(2)

    def as_json(self, indent=None):
        """Returns self as as JSON

        Parameters:
            :param indent int: Indentation to use for the JSON generation

        Returns:
            dict: JSON representation
        """

        return json.dumps(self._data, indent=indent)

    def as_dict(self):
        """Returns self as a dictionary"""

        return self._data

    def write(self, f):
        """Writes contents to a file-like object"""

        if hasattr(f, "write"):
            f.write(str(self))
        else:
            with open(f, "wt") as fobj:
                fobj.write(str(self))


# ----------------------------------------------------------


def cpu_statistics(start, end):
    """Summarizes current CPU usage

    This method should be used when the currently set algorithm is the only one
    executed through the whole process. It is done for collecting resource
    statistics on separate processing environments. It follows the recipe in:
    http://stackoverflow.com/questions/30271942/get-docker-container-cpu-usage-as-percentage

    Returns:

      dict: A dictionary summarizing current CPU usage

    """

    if "system_cpu_usage" not in end:
        return {
            "user": 0.0,
            "system": 0.0,
            "total": 0.0,
            "percent": 0.0,
            "processors": 1,
        }

    if start is not None:
        user_cpu = end["cpu_usage"]["total_usage"] - start["cpu_usage"]["total_usage"]
        total_cpu = end["system_cpu_usage"] - start["system_cpu_usage"]

    else:
        user_cpu = end["cpu_usage"]["total_usage"]
        total_cpu = end["system_cpu_usage"]

    user_cpu /= 1000000000.0  # in seconds
    total_cpu /= 1000000000.0  # in seconds
    processors = (
        len(end["cpu_usage"]["percpu_usage"])
        if end["cpu_usage"]["percpu_usage"] is not None
        else 1
    )

    return {
        "user": user_cpu,
        "system": 0.0,
        "total": total_cpu,
        "percent": 100.0 * processors * user_cpu / total_cpu if total_cpu else 0.0,
        "processors": processors,
    }


# ----------------------------------------------------------


def memory_statistics(data):
    """Summarizes current memory usage

    This method should be used when the currently set algorithm is the only one
    executed through the whole process. It is done for collecting resource
    statistics on separate processing environments.

    Returns:

      dict: A dictionary summarizing current memory usage

    """

    limit = float(data["limit"])
    memory = float(data["max_usage"])

    return {
        "rss": memory,
        "limit": limit,
        "percent": 100.0 * memory / limit if limit else 0.0,
    }
