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

"""Schema validation for BEAT JSON I/O"""


import os
import pkg_resources

import six
import simplejson as json
import jsonschema

from beat.backend.python.utils import error_on_duplicate_key_hook


def maybe_load_json(s):
    """Maybe loads the JSON from a string or filename"""

    # if it is a string
    if isinstance(s, six.string_types):
        # if it is a valid path
        if os.path.exists(s):
            with open(s, "rt") as f:
                return maybe_load_json(f)
        else:
            return json.loads(s, object_pairs_hook=error_on_duplicate_key_hook)

    # if it is a 'file-like' object
    if hasattr(s, "read"):
        return maybe_load_json(s.read())

    return s


def load_schema(schema_name, version=1):
    """Returns a JSON validator for the schema given the relative name


  Parameters:

    schema_name (str): the name of the schema to load. This value corresponds
      to the filename inside our schema directory (where this file is located)
      and should *exclude* the extension ``.json``.

    version (int): the version of the schema to use.


  Returns:

    jsonschema.Draft4Validator: An instance of a JSON schema draft-4 validator.


  Raises:

    jsonschema.SchemaError: If there is an error on the schema.

  """

    fname = pkg_resources.resource_filename(
        __name__, os.path.join(schema_name, "%d.json" % version)
    )

    with open(fname, "rb") as f:
        data = f.read().decode()
        try:
            schema = json.loads(data)
        except json.errors.JSONDecodeError:
            print("Invalid json:\n {data}".format(data))
            raise

    basedir = os.path.realpath(os.path.dirname(fname))
    resolver = jsonschema.RefResolver("file://" + basedir + "/", schema)

    # now we load it
    return jsonschema.Draft4Validator(schema, resolver=resolver)


def validate(schema_name, data):
    """Validates the input data using the schema

  This function handles schema versionning in the context of BEAT transparently
  by first peeking the schema version required by the JSON data and then
  validating the JSON data against the proper schema version for the respective
  type.


  Example:

    .. code-block:: python

       try:
           cleaned_data, error_list = validate('toolchain', '/to/my/file.json')
       except json.JSONDecodeError as e:
           print(e)


  Parameters:

    schema_name (str): The relative path to the schema to use for validation.
      For example, to validate a toolchain, use ``'toolchain'``.

    data (object, str, file): The piece of data to validate. The input can be a
      valid python object that represents a JSON structure, a file, from which
      the JSON contents will be read out or a string.

      If ``data`` is a string and represents a valid filesystem path, the
      relevant file will be opened and read as with
      :py:func:`json.load``. Otherwise, it will be considered to be
      string containing a valid JSON structure that will be loaded as with
      :py:func:`json.loads`.

      Note that if the file is opened and read internally using
      :py:func:`json.load`, exceptions may be thrown by that subsystem,
      concerning the file structure. Consult the manual page for
      :py:mod:`simplejson` for details.


  Returns:

    A tuple with two elements: the cleaned JSON data structure, after
    processing and a list of errors found by ``jsonschema``. If no errors
    occur, then returns an empty list for the second element of the tuple.

  Raises:

    jsonschema.SchemaError: If there is an error on the schema.

  """

    try:
        data = maybe_load_json(data)
    except json.JSONDecodeError as e:
        return data, ["invalid JSON code: %s" % str(e)]
    except RuntimeError as e:
        return data, ["Invalid JSON: %s" % str(e)]

    # handles the schema version
    if schema_name != "dataformat":
        version = data.get("schema_version", 1)
    else:
        version = data.get("#schema_version", 1)

    validator = load_schema(schema_name, version)

    def encode_error(error, indent=""):
        abspath = "/".join([""] + ([str(k) for k in error.absolute_path] or [""]))
        schpath = "/".join([""] + ([str(k) for k in error.schema_path] or [""]))
        retval = indent + "%s: %s (rule: %s)" % (abspath, error.message, schpath)
        for another_error in error.context:
            retval += "\n" + encode_error(another_error, indent + "  ")
        return retval

    errorlist = [
        encode_error(k)
        for k in sorted(validator.iter_errors(data), key=lambda e: e.path)
    ]

    return data, errorlist
