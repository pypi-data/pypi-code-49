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


import logging

from collections import namedtuple

from ..data import DataSource
from ..data import DataSink


class MockDataSource(DataSource):

    def __init__(self, data_and_indices):
        super(MockDataSource, self).__init__()
        self.infos = [ (x[1], x[2]) for x in data_and_indices ]
        self.data = [ x[0] for x in data_and_indices ]

    def __getitem__(self, index):
        return (self.data[index], self.infos[index][0], self.infos[index][1])


#----------------------------------------------------------


class CrashingDataSource(DataSource):

    def __init__(self):
        super(CrashingDataSource, self).__init__()

        Infos = namedtuple('Infos', ['start_index', 'end_index'])
        self.infos = [Infos(0, 0)]

    def __getitem__(self, index):
        a = b
        return (None, None, None)


#----------------------------------------------------------


class MockDataSink(DataSink):

    class WrittenData:
        def __init__(self, data, start, end):
            self.data = data
            self.start = start
            self.end = end

    def __init__(self, dataformat):
        self.written = []
        self.can_write = True
        self.dataformat = dataformat

    def write(self, data, start_data_index, end_data_index):
        if not(self.can_write): raise IOError
        self.written.append(
            MockDataSink.WrittenData(data, start_data_index, end_data_index)
        )

    def isConnected(self):
        return True

# Based on https://stackoverflow.com/a/20553331/5843716
class MockLoggingHandler(logging.Handler):
    """Mock logging handler to check for expected logs.

    Messages are available from an instance's ``messages`` dict, in order,
    indexed by a lowercase log level string (e.g., 'debug', 'info', etc.).
    """

    def __init__(self, *args, **kwargs):
        self.messages = {
            'debug': [], 'info': [],
            'warning': [], 'error': [],
            'critical': [], 'extra': []
        }
        super(MockLoggingHandler, self).__init__(*args, **kwargs)

    def emit(self, record):
        "Store a message from ``record`` in the instance's ``messages`` dict."
        try:
            self.messages[record.levelname.lower()].append(record.getMessage())
        except Exception:
            self.handleError(record)

    def reset(self):
        self.acquire()
        try:
            for message_list in self.messages.values():
                message_list.clear()
        finally:
            self.release()
