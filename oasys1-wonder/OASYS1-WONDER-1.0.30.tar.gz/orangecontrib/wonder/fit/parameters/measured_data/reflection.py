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

import numpy

from orangecontrib.wonder.fit.parameters.fit_parameter import PARAM_HWMAX, PARAM_HWMIN

class Reflection():

    h = 0
    k = 0
    l = 0

    d_spacing = 0.0

    intensity = None

    def __init__(self, h, k, l, intensity):
        self.h = h
        self.k = k
        self.l = l

        self.intensity = intensity

    @classmethod
    def get_parameters_prefix(cls):
        return "reflection_"

    def to_text(self):
        return str(self.h) + ", " + str(self.k) + ", " + str(self.l) + ", "  + str(self.intensity)

    def to_row(self):
        text = str(self.h) + ", " + str(self.k) + ", " + str(self.l) + ", " + self.intensity.parameter_name + " "

        if self.intensity.function:
            text += ":= " + str(self.intensity.function_value)
        else:
            text += str(self.intensity.value)

            if self.intensity.fixed:
                text += "fixed"
            elif not self.intensity.boundary is None:
                if not self.intensity.boundary.min_value == PARAM_HWMIN:
                    text += ", min " + str(self.intensity.boundary.min_value)

                if not self.intensity.boundary.max_value == PARAM_HWMAX:
                    text += ", max " + str(self.intensity.boundary.max_value)

        return text

    def get_theta_hkl(self, wavelength):
        return numpy.degrees(numpy.asin(2*self.d_spacing/wavelength))

    def get_q_hkl(self, wavelength):
        return 8*numpy.pi*self.d_spacing/(wavelength**2)

    def get_s_hkl(self, wavelength):
        return self.get_q_hkl(wavelength)/(2*numpy.pi)
