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


from ..data import DataSource
from ..data import DataSink


class MockDataSource(DataSource):
    def __init__(self, data, indexes):
        self.data = list(data)
        self.indexes = list(indexes)
        self.current = 0

    def next(self):
        result = (
            self.data[self.current],
            self.indexes[self.current][0],
            self.indexes[self.current][1],
        )
        self.current += 1
        return result

    def hasMoreData(self):
        return self.current < sum(1 for i in self.data)


# ----------------------------------------------------------


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
        if not (self.can_write):
            raise IOError
        self.written.append(
            MockDataSink.WrittenData(data, start_data_index, end_data_index)
        )

    def isConnected(self):
        return True


# ----------------------------------------------------------


class MockDataSource_Crash(DataSource):
    def next(self):
        a = b  # noqa

    def hasMoreData(self):
        a = b  # noqa
        return False
