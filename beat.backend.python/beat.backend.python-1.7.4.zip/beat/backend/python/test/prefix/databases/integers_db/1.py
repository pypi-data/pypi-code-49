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


import random
import numpy
from collections import namedtuple
from beat.backend.python.database import View


class Double(View):

    def index(self, root_folder, parameters):
        Entry = namedtuple('Entry', ['a', 'b', 'sum'])

        return [
            Entry(1, 10, 11),
            Entry(2, 20, 22),
            Entry(3, 30, 33),
            Entry(4, 40, 44),
            Entry(5, 50, 55),
            Entry(6, 60, 66),
            Entry(7, 70, 77),
            Entry(8, 80, 88),
            Entry(9, 90, 99),
        ]


    def get(self, output, index):
        obj = self.objs[index]

        if output == 'a':
            return {
                'value': numpy.int32(obj.a)
            }

        elif output == 'b':
            return {
                'value': numpy.int32(obj.b)
            }

        elif output == 'sum':
            return {
                'value': numpy.int32(obj.sum)
            }
        elif output == 'class':
            return {
                'value': numpy.int32(obj.cls)
            }


#----------------------------------------------------------


class Triple(View):

    def index(self, root_folder, parameters):
        Entry = namedtuple('Entry', ['a', 'b', 'c', 'sum'])

        return [
            Entry(1, 10, 100, 111),
            Entry(2, 20, 200, 222),
            Entry(3, 30, 300, 333),
            Entry(4, 40, 400, 444),
            Entry(5, 50, 500, 555),
            Entry(6, 60, 600, 666),
            Entry(7, 70, 700, 777),
            Entry(8, 80, 800, 888),
            Entry(9, 90, 900, 999),
        ]


    def get(self, output, index):
        obj = self.objs[index]

        if output == 'a':
            return {
                'value': numpy.int32(obj.a)
            }

        elif output == 'b':
            return {
                'value': numpy.int32(obj.b)
            }

        elif output == 'c':
            return {
                'value': numpy.int32(obj.c)
            }

        elif output == 'sum':
            return {
                'value': numpy.int32(obj.sum)
            }


#----------------------------------------------------------


class Labelled(View):

    def index(self, root_folder, parameters):
        Entry = namedtuple('Entry', ['label', 'value'])

        return [
            Entry('A', 1),
            Entry('A', 2),
            Entry('A', 3),
            Entry('A', 4),
            Entry('A', 5),
            Entry('B', 10),
            Entry('B', 20),
            Entry('B', 30),
            Entry('B', 40),
            Entry('B', 50),
            Entry('C', 100),
            Entry('C', 200),
            Entry('C', 300),
            Entry('C', 400),
            Entry('C', 500),
        ]


    def get(self, output, index):
        obj = self.objs[index]

        if output == 'label':
            return {
                'value': obj.label
            }

        elif output == 'value':
            return {
                'value': numpy.int32(obj.value)
            }


#----------------------------------------------------------


class DifferentFrequencies(View):

    def index(self, root_folder, parameters):
        Entry = namedtuple('Entry', ['a', 'b'])

        return [
            Entry(1, 10),
            Entry(1, 20),
            Entry(1, 30),
            Entry(1, 40),
            Entry(2, 50),
            Entry(2, 60),
            Entry(2, 70),
            Entry(2, 80),
        ]


    def get(self, output, index):
        obj = self.objs[index]

        if output == 'a':
            return {
                'value': numpy.int32(obj.a)
            }

        elif output == 'b':
            return {
                'value': numpy.int32(obj.b)
            }
