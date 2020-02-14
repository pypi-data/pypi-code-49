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
====
hash
====

Various functions for hashing platform contributions and others
"""

import hashlib
import simplejson
import collections
import copy
import six
import os


# ----------------------------------------------------------


def _sha256(s):
    """A python2/3 shortcut for :py:func:`haslib.sha256.hexdigest` to will
    ensure that the given string is unicode before going further.
    """
    if isinstance(s, six.string_types):
        try:
            s = six.u(s).encode('utf-8')
        except Exception:
            s = s.encode('utf-8')
    return hashlib.sha256(s).hexdigest()


# ----------------------------------------------------------


def _stringify(dictionary):
    names = sorted(dictionary.keys())

    converted_dictionary = '{'
    for name in names:
        converted_dictionary += '"%s":%s,' % (name, str(dictionary[name]))

    if len(converted_dictionary) > 1:
        converted_dictionary = converted_dictionary[:-1]

    converted_dictionary += '}'

    return converted_dictionary


# ----------------------------------------------------------


def _compact(text):
    return text.replace(' ', '').replace('\n', '')


# ----------------------------------------------------------


def toPath(hash, suffix='.data'):
    """ Returns the path on disk which corresponds to the hash given.

    Parameters:
        hash (str): Hash from which the path is generated

        suffix (str): Suffix of the file for which the path is generated

    Returns:
        str: Path to file based on hash
    """
    return os.path.join(hash[0:2], hash[2:4], hash[4:6], hash[6:] + suffix)


# ----------------------------------------------------------


def toUserPath(username):
    """Returns the path to the user specific folder

    Parameters:
        username (str): User name to get the path from

    Return:
        str: Path on file system for the user
    """

    hash = _sha256(username)
    return os.path.join(hash[0:2], hash[2:4], username)


# ----------------------------------------------------------


def hash(dictionary_or_string):
    """Generates a hash for the given parameter

    Parameters:
        dictionary_or_string (str or dict): Input to hash

    Returns:
        str: Hash from input
    """

    if isinstance(dictionary_or_string, dict):
        return _sha256(_stringify(dictionary_or_string))
    else:
        return _sha256(dictionary_or_string)


# ----------------------------------------------------------


def hashJSON(contents, description):
    """Hashes the pre-loaded JSON object using :py:meth:`hashlib.hash.hexdigest`

    Excludes description changes

    Returns:
        str: hash
    """

    if description in contents:
        contents = copy.deepcopy(contents)  # temporary copy
        del contents[description]
    contents = simplejson.dumps(contents, sort_keys=True)
    return hashlib.sha256(contents.encode('utf-8')).hexdigest()


# ----------------------------------------------------------


def hashJSONFile(path, description):
    """Hashes the JSON file contents using :py:meth:`hashlib.hash.hexdigest`

    Excludes description changes

    Returns:
        str: hash
    """

    try:
        with open(path, 'rb') as f:
            # preserve order
            return hashJSON(simplejson.loads(f.read().decode('utf-8'),
                            object_pairs_hook=collections.OrderedDict),
                            description)
    except simplejson.JSONDecodeError:
        # falls back to normal file content hashing
        return hashFileContents(path)


# ----------------------------------------------------------


def hashFileContents(path):
    """Hashes the file contents using :py:meth:`hashlib.hash.hexdigest`.

    Returns:
        str: hash
    """

    with open(path, 'rb') as f:
        sha256 = hashlib.sha256()
        for chunk in iter(lambda: f.read(sha256.block_size * 1000), b''):
            sha256.update(chunk)

        return sha256.hexdigest()


# ----------------------------------------------------------


def hashDataset(database_name, protocol_name, set_name):
    """Hashes a Dataset

    Parameters:
        database_name (str): Database name
        protocol_name (str): Database protocol name
        set_name (str): Name of the set in the database

    Returns:
        str: hash
    """

    s = _compact("""{
        "database": "%s",
        "protocol": "%s",
        "set": "%s"
}""") % (database_name, protocol_name, set_name)
    return hash(s)
