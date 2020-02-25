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

from orangecontrib.wonder.fit.parameters.fit_parameter import ParametersList

class Caglioti(ParametersList):
    U = None
    V = None
    W = None
    a = None
    b = None
    c = None

    @classmethod
    def get_parameters_prefix(cls):
        return "caglioti_"

    def __init__(self, U, V, W, a, b, c):
        super(Caglioti, self).__init__()

        self.U = U
        self.V = V
        self.W = W
        self.a = a
        self.b = b
        self.c = c

class Lab6TanCorrection(ParametersList):
    ax = None
    bx = None
    cx = None
    dx = None
    ex = None

    @classmethod
    def get_parameters_prefix(cls):
        return "lab6_tancorrection_"

    def __init__(self, ax, bx, cx, dx, ex):
        super(Lab6TanCorrection, self).__init__()

        self.ax = ax
        self.bx = bx
        self.cx = cx
        self.dx = dx
        self.ex = ex

class ZeroError(ParametersList):
    shift = None

    @classmethod
    def get_parameters_prefix(cls):
        return "zero_error_"

    def __init__(self, shift):
        super(ZeroError, self).__init__()

        self.shift = shift

class SpecimenDisplacement(ParametersList):
    goniometer_radius = 1.0
    displacement = None

    @classmethod
    def get_parameters_prefix(cls):
        return "sd_"

    def __init__(self, goniometer_radius=1.0, displacement=None):
        super(SpecimenDisplacement, self).__init__()

        self.goniometer_radius = goniometer_radius
        self.displacement = displacement
