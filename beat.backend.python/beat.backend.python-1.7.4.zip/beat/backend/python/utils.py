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
utils
=====

This module implements helper classes and functions.
"""

import os
import shutil
import collections
import numpy
import simplejson
import six

from . import hash


# ----------------------------------------------------------


def hashed_or_simple(prefix, what, path, suffix=".json"):
    """Returns a hashed path or simple path depending on where the resource is
    """

    username, right_bit = path.split("/", 1)
    hashed_prefix = hash.toUserPath(username)
    candidate = os.path.join(prefix, what, hashed_prefix, right_bit) + suffix

    if os.path.exists(candidate):
        return candidate

    return os.path.join(prefix, what, path + suffix)


# ----------------------------------------------------------


def safe_rmfile(f):
    """Safely removes a file from the disk"""

    if os.path.exists(f):
        os.unlink(f)


# ----------------------------------------------------------


def safe_rmdir(f):
    """Safely removes the directory containg a given file from the disk"""

    d = os.path.dirname(f)

    if not os.path.exists(d):
        return

    if not os.listdir(d):
        os.rmdir(d)


# ----------------------------------------------------------


def extension_for_language(language):
    """Returns the preferred extension for a given programming language

    The set of languages supported must match those declared in our
    ``common.json`` schema.

    Parameters:

      language (str) The language for which you'd like to get the extension for.


    Returns:

      str: The extension for the given language, including a leading ``.`` (dot)


    Raises:

      KeyError: If the language is not defined in our internal dictionary.

    """

    return dict(unknown="", cxx=".so", matlab=".m", python=".py", r=".r")[language]


# ----------------------------------------------------------


class Prefix(object):
    def __init__(self, paths=None):
        if isinstance(paths, list):
            self.paths = paths
        elif paths is not None:
            self.paths = [paths]
        else:
            self.paths = []

    def add(self, path):
        self.paths.append(path)

    def path(self, filename):
        for p in self.paths:
            fullpath = os.path.join(p, filename)
            if os.path.exists(fullpath):
                return fullpath

        return os.path.join(self.paths[0], filename)


# ----------------------------------------------------------


class File(object):
    """User helper to read and write file objects"""

    def __init__(self, path, binary=False):

        self.path = path
        self.binary = binary

    def exists(self):

        return os.path.exists(self.path)

    def load(self):

        mode = "rb" if self.binary else "rt"
        with open(self.path, mode) as f:
            return f.read()

    def try_load(self):

        if os.path.exists(self.path):
            return self.load()
        return None

    def backup(self):

        if not os.path.exists(self.path):
            return  # no point in backing-up

        backup = self.path + "~"
        if os.path.exists(backup):
            os.remove(backup)

        shutil.copy(self.path, backup)

    def save(self, contents):

        d = os.path.dirname(self.path)
        if not os.path.exists(d):
            os.makedirs(d)

        if os.path.exists(self.path):
            self.backup()

        mode = "wb" if self.binary else "wt"
        if self.binary:
            mode = "wb"
            if isinstance(contents, six.string_types):
                contents = contents.encode("utf-8")
        else:
            mode = "wt"
            if not isinstance(contents, six.string_types):
                contents = contents.decode("utf-8")

        with open(self.path, mode) as f:
            f.write(contents)

    def remove(self):

        safe_rmfile(self.path)
        safe_rmfile(self.path + "~")  # backup
        safe_rmdir(self.path)  # remove containing directory


# ----------------------------------------------------------


class AbstractStorage(object):

    asset_type = None
    asset_folder = None

    def __init__(self, path):

        if not all(
            [type(attr) == str for attr in [self.asset_type, self.asset_folder]]
        ):
            raise TypeError(
                "asset_type and asset_folder must be configured properly\n"
                "asset_type: {}\n"
                "asset_folder: {}".format(self.asset_type, self.asset_folder)
            )

        self.path = path
        self.json = File(self.path + ".json")
        self.doc = File(self.path + ".rst")

    def exists(self):
        """If the database declaration file exists"""

        return self.json.exists()

    def remove(self):
        """Removes the object from the disk"""

        self.json.remove()
        self.doc.remove()

    def hash(self):
        """The 64-character hash of the database declaration JSON"""

        raise NotImplementedError

    def load(self):
        """Loads the JSON declaration as a file"""

        raise NotImplementedError

    def save(self):
        """Saves the JSON declaration as files"""

        raise NotImplementedError


class Storage(AbstractStorage):
    """Resolves paths for objects that provide only a description"""

    def __init__(self, path):
        super(Storage, self).__init__(path)

    def hash(self, description="description"):
        """Re-imp"""

        return hash.hashJSONFile(self.json.path, description)

    def load(self):
        """Re-imp"""

        tp = collections.namedtuple("Storage", ["declaration", "description"])
        return tp(self.json.load(), self.doc.try_load())

    def save(self, declaration, description=None):
        """Re-imp"""

        if description:
            self.doc.save(description.encode("utf8"))
        if not isinstance(declaration, six.string_types):
            declaration = simplejson.dumps(declaration, indent=4)
        self.json.save(declaration)


# ----------------------------------------------------------


class CodeStorage(AbstractStorage):
    """Resolves paths for objects that provide a description and code

    Parameters:

      language (str): One of the valdid programming languages

    """

    def __init__(self, path, language=None):
        super(CodeStorage, self).__init__(path)

        self._language = language or self.__auto_discover_language()
        self.code = File(
            self.path + extension_for_language(self._language), binary=True
        )

    def __auto_discover_language(self, json=None):
        """Discovers and sets the language from its own JSON descriptor"""
        try:
            text = json or self.json.load()
            json = simplejson.loads(text)
            return json["language"]
        except (IOError, KeyError, simplejson.JSONDecodeError):
            return "unknown"

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
        self.code = File(
            self.path + extension_for_language(self._language), binary=True
        )

    def hash(self):
        """Re-imp"""

        declaration_hash = hash.hashJSONFile(self.json.path, "description")

        if self.code.exists():
            code_hash = hash.hashFileContents(self.code.path)
            return hash.hash(dict(declaration=declaration_hash, code=code_hash))
        else:
            return declaration_hash

    def exists(self):
        """Re-imp"""

        return super(CodeStorage, self).exists() and self.code.exists()

    def load(self):
        """Re-imp"""

        tp = collections.namedtuple(
            "CodeStorage", ["declaration", "code", "description"]
        )
        return tp(self.json.load(), self.code.try_load(), self.doc.try_load())

    def save(self, declaration, code=None, description=None):
        """Re-imp"""

        if description:
            self.doc.save(description.encode("utf8"))

        if not isinstance(declaration, six.string_types):
            declaration = simplejson.dumps(declaration, indent=4)
        self.json.save(declaration)

        if code:
            if self._language == "unknown":
                self.language = self.__auto_discover_language(declaration)
            self.code.save(code)

    def remove(self):
        """Re-imp"""

        super(CodeStorage, self).remove()
        self.code.remove()


# ----------------------------------------------------------


class NumpyJSONEncoder(simplejson.JSONEncoder):
    """Encodes numpy arrays and scalars

    See Also:

      :py:class:`simplejson.JSONEncoder`

    """

    def default(self, obj):
        if isinstance(obj, numpy.ndarray) or isinstance(obj, numpy.generic):
            return obj.tolist()
        elif isinstance(obj, numpy.dtype):
            if obj.name == "str":
                return "string"
            return obj.name
        return simplejson.JSONEncoder.default(self, obj)


# ----------------------------------------------------------


def error_on_duplicate_key_hook(pairs):
    """JSON loader hook that will error out if several same keys are found

    Returns an OrderedDict if everything goes well
    """

    dct = collections.OrderedDict()
    for key, value in pairs:
        if key in dct:
            raise RuntimeError(
                "Invalid file content\n{} found several times".format(key)
            )
        dct[key] = value

    return dct


# ----------------------------------------------------------


def has_argument(method, argument):
    try:
        from inspect import signature

        sig = signature(method)
        params = sig.parameters
    except ImportError:
        from inspect import getargspec

        params = getargspec(method).args

    return argument in params
