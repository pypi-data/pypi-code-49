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


class Algorithm:

    def setup(self, parameters):
        self.int8_value      = parameters['int8_value']
        self.int8_range      = parameters['int8_range']
        self.int8_choices    = parameters['int8_choices']
        self.int16_value     = parameters['int16_value']
        self.int16_range     = parameters['int16_range']
        self.int16_choices   = parameters['int16_choices']
        self.int32_value     = parameters['int32_value']
        self.int32_range     = parameters['int32_range']
        self.int32_choices   = parameters['int32_choices']
        self.int64_value     = parameters['int64_value']
        self.int64_range     = parameters['int64_range']
        self.int64_choices   = parameters['int64_choices']
        self.uint8_value     = parameters['uint8_value']
        self.uint8_range     = parameters['uint8_range']
        self.uint8_choices   = parameters['uint8_choices']
        self.uint16_value    = parameters['uint16_value']
        self.uint16_range    = parameters['uint16_range']
        self.uint16_choices  = parameters['uint16_choices']
        self.uint32_value    = parameters['uint32_value']
        self.uint32_range    = parameters['uint32_range']
        self.uint32_choices  = parameters['uint32_choices']
        self.uint64_value    = parameters['uint64_value']
        self.uint64_range    = parameters['uint64_range']
        self.uint64_choices  = parameters['uint64_choices']
        self.float32_value   = parameters['float32_value']
        self.float32_range   = parameters['float32_range']
        self.float32_choices = parameters['float32_choices']
        self.float64_value   = parameters['float64_value']
        self.float64_range   = parameters['float64_range']
        self.float64_choices = parameters['float64_choices']
        self.bool_value      = parameters['bool_value']
        self.string_value    = parameters['string_value']
        return True

    def process(self, data_loaders, outputs):
        return True
