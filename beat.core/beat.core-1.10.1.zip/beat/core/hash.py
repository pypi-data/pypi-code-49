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

Also forward importing from :py:mod:`beat.backend.python.hash`
"""

import collections

import simplejson as json

from beat.backend.python.hash import *  # noqa
from beat.backend.python.hash import _sha256  # noqa
from beat.backend.python.hash import _stringify
from beat.backend.python.hash import _compact


# ----------------------------------------------------------


def hashBlockOutput(
    block_name,
    algorithm_name,
    algorithm_hash,
    parameters,
    environment,
    input_hashes,
    output_name,
):
    """Generate a hash for a given block output

    Parameters:
        :param str block_name: Name of the block (unused)

        :param str algorithm_name: Name of the algorithm used by the block
        (parameter unused)

        :param str algorithm_hash: Hash of the algorithm used by the block

        :param dict parameters: Configured parameters

        :param dict environment: Environment parameters

        :param dict input_hashes: Dictionary containing the input's hashes

        :param str output_name: Name of the output
    """

    # Note: 'block_name' and 'algorithm_name' aren't used to compute the hash,
    # but are useful when an application wants to implement its own hash
    # function
    s = (
        _compact(
            """{
        "algorithm": "%s",
        "parameters": %s,
        "environment": %s,
        "inputs": %s,
        "output": "%s"
}"""
        )
        % (
            algorithm_hash,
            _stringify(parameters),
            _stringify(environment),
            _stringify(input_hashes),
            output_name,
        )
    )
    return hash(s)


# ----------------------------------------------------------


def hashAnalyzer(
    analyzer_name, algorithm_name, algorithm_hash, parameters, environment, input_hashes
):
    """Generate a hash for a given analyzer

    Parameters:
        :param str analyzer_name: Name of the analyzer (unused)

        :param str algorithm_name: Name of the algorithm used by the analyzer

        :param str algorithm_hash: Hash of the algorithm used by the analyzer

        :param dict parameters: Configured parameters

        :param dict environment: Environment parameters

        :param dict input_hashes: Dictionary containing the inputs's hashes
    """

    # Note: 'analyzer_name' isn't used to compute the hash, but is useful when
    # an applications want to implement its own hash function
    s = (
        _compact(
            """{
        "algorithm_name": "%s",
        "algorithm": "%s",
        "parameters": %s,
        "environment": %s,
        "inputs": %s
}"""
        )
        % (
            algorithm_name,
            algorithm_hash,
            _stringify(parameters),
            _stringify(environment),
            _stringify(input_hashes),
        )
    )
    return hash(s)


# ----------------------------------------------------------


def hashJSONStr(contents, description):
    """Hashes the JSON string contents using ``hashlib.sha256``

    Excludes description changes
    """

    try:
        return hashJSON(  # noqa
            json.loads(contents, object_pairs_hook=collections.OrderedDict), description
        )  # preserve order
    except json.JSONDecodeError:
        # falls back to normal file content hashing
        return hash(contents)
