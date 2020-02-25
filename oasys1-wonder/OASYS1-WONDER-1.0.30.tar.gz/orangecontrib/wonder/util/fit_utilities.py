#!/usr/bin/env python
# -*- coding: utf-8 -*-
# #########################################################################
# Copyright (c) 2020, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2020. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################

import operator
import itertools
import numpy

class Symmetry:
    FCC = "fcc"
    BCC = "bcc"
    SIMPLE_CUBIC = "sc"

    @classmethod
    def tuple(cls):
        return [cls.SIMPLE_CUBIC, cls.BCC, cls.FCC]

class Utilities:
    @classmethod
    def s_hkl(cls, a, h, k, l):
        return numpy.sqrt(h**2 + k**2 + l**2) / a

    @classmethod
    def theta(cls, s, wavelength):
        return numpy.arcsin (s * wavelength / 2)

    @classmethod
    def s(cls, theta, wavelength):
        return 2*numpy.sin(theta)/wavelength

    @classmethod
    def theta_hkl (cls, a, h, k, l , wavelength):
        return cls.theta(cls.s_hkl(a, h, k, l), wavelength)

def is_even(a):
    return a % 2 == 0

def is_odd(a):
    return a % 2 == 1

def is_fcc(h, k, l):
    if (is_even(h) and is_even(k) and is_even(l)):
        return True
    elif (is_odd(h) and is_odd(k) and is_odd(l)):
        return True
    else:
        return False

def is_bcc(h, k, l):
    if is_even(h+k+l):
        return True
    else:
        return False

def list_of_s_bragg(lattice_param, symmetry=Symmetry.FCC, n_peaks=numpy.inf, s_max=numpy.inf):

    s_list = []
    s_hkl_max = 0.0
    possible_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for h, k, l in itertools.combinations_with_replacement(possible_indexes, 3):
        if (symmetry == Symmetry.FCC and is_fcc(h, k, l)) or \
           (symmetry == Symmetry.BCC and is_bcc(h, k, l)) or \
            symmetry == Symmetry.SIMPLE_CUBIC:
            s_hkl = Utilities.s_hkl(lattice_param, h, k, l)

            s_hkl_max = s_hkl if s_hkl > s_hkl_max else s_hkl_max

            s_list.append([[h, k, l], s_hkl])

    s_list = sorted(s_list, key=operator.itemgetter(1))

    if not len(s_list) <= n_peaks:
        s_list = s_list[:n_peaks+1]

    if not s_max > s_hkl_max:
        last_index = 0
        for item in s_list:
            if item[1] > s_max: break
            last_index +=1

        if last_index == 0:
            s_list = []
        else:
            s_list = s_list[:(last_index)]

    if not s_list == []:
        for temp_list in s_list:
            temp_list[0] = sorted(temp_list[0], reverse=True)

        s_list.pop(0)

    return s_list

if __name__=="__main__":
    list = list_of_s_bragg(0.2873, Symmetry.FCC)

    for item in list:
        print(item)
