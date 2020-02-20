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
data
====

Forward importing from :py:mod:`beat.backend.python.data`:
:py:func:`beat.backend.python.data.mixDataIndices`
:py:func:`beat.backend.python.data.getAllFilenames`
:py:class:`beat.backend.python.data.DataSource`
:py:class:`beat.backend.python.data.CachedDataSource`
:py:class:`beat.backend.python.data.DatabaseOutputDataSource`
:py:class:`beat.backend.python.data.RemoteDataSource`
:py:class:`beat.backend.python.data.DataSink`
:py:class:`beat.backend.python.data.CachedDataSink`
:py:class:`beat.backend.python.data.StdoutDataSink`
:py:func:`beat.backend.python.data.load_data_index`
:py:func:`beat.backend.python.data.load_data_index_db`
:py:func:`beat.backend.python.data.foundSplitRanges`
"""

from beat.backend.python.data import mixDataIndices  # noqa
from beat.backend.python.data import getAllFilenames  # noqa
from beat.backend.python.data import DataSource  # noqa
from beat.backend.python.data import CachedDataSource  # noqa
from beat.backend.python.data import DatabaseOutputDataSource  # noqa
from beat.backend.python.data import RemoteDataSource  # noqa
from beat.backend.python.data import DataSink  # noqa
from beat.backend.python.data import CachedDataSink  # noqa
from beat.backend.python.data import StdoutDataSink  # noqa
from beat.backend.python.data import load_data_index  # noqa
from beat.backend.python.data import load_data_index_db  # noqa
from beat.backend.python.data import foundSplitRanges  # noqa
