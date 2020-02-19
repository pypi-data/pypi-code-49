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
protocoltemplate
================

Validation of protocoltemplate

Forward importing from :py:mod:`beat.backend.python.protocoltemplate`:
:py:class:`beat.backend.python.protocoltemplate.Storage`
"""

import six

from . import schema
from . import prototypes

from beat.backend.python.protocoltemplate import Storage
from beat.backend.python.protocoltemplate import (
    ProtocolTemplate as BackendProtocolTemplate,
)


class ProtocolTemplate(BackendProtocolTemplate):
    """Protocol template define the design of the database.


    Parameters:

      prefix (str): Establishes the prefix of your installation.

      data (dict, str): The piece of data representing the protocol templates.
        It must validate against the schema defined for protocol templates. If a
        string is passed, it is supposed to be a valid path to protocol template
        in the designated prefix area.

      dataformat_cache (:py:class:`dict`, Optional): A dictionary mapping
        dataformat names to loaded dataformats. This parameter is optional and,
        if passed, may greatly speed-up protocol template loading times as
        dataformats that are already loaded may be re-used. If you use this
        parameter, you must guarantee that the cache is refreshed as appropriate
        in case the underlying dataformats change.


    Attributes:

      name (str): The full, valid name of this protocol template

      description (str): The short description string, loaded from the JSON
        file if one was set.

      documentation (str): The full-length docstring for this object.

      storage (object): A simple object that provides information about file
        paths for this protocol template

      errors (list): A list containing errors found while loading this
        protocol template.

      data (dict): The original data for this protocol template, as loaded by
        our JSON decoder.

    """

    def __init__(self, prefix, data, dataformat_cache=None):
        super(ProtocolTemplate, self).__init__(prefix, data, dataformat_cache)

    def _load(self, data, dataformat_cache):
        """Loads the database"""

        self._name = None
        self.storage = None
        self.dataformats = {}  # preloaded dataformats

        if data is None:  # loads prototype and validates it
            self.data, self.errors = prototypes.load("protocoltemplate")
            assert not self.errors, "\n  * %s" % "\n  *".join(self.errors)  # nosec
        else:
            if isinstance(data, six.string_types):  # user has passed a file pointer

                self._name = data
                self.storage = Storage(self.prefix, self._name)
                data = self.storage.json.path
                if not self.storage.json.exists():
                    self.errors.append(
                        "Protocol template declaration file not found: %s" % data
                    )
                    return

            # this runs basic validation, including JSON loading if required
            self.data, self.errors = schema.validate("protocoltemplate", data)
            if self.errors:
                return  # don't proceed with the rest of validation
