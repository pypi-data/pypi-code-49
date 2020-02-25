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

class IncidentRadiation(ParametersList):

    @classmethod
    def get_parameters_prefix(cls):
        return "incident_radiation_"

    wavelength = None
    is_single_wavelength = True
    xray_tube_key = None
    secondary_wavelengths = []
    secondary_wavelengths_weights = []
    principal_wavelength_weight = None

    def __init__(self, wavelength = None):
        self.wavelength = wavelength
        self.is_single_wavelength = True

    def set_multiple_wavelengths(self, xray_tube_key=None, secondary_wavelengths = [], secondary_wavelengths_weights = [], recalculate=True):
        self.is_single_wavelength = False
        self.xray_tube_key=xray_tube_key
        self.secondary_wavelengths = secondary_wavelengths
        self.secondary_wavelengths_weights = secondary_wavelengths_weights
        self.principal_wavelength_weight = self.get_principal_wavelenght_weight(recalculate=recalculate)

    def set_single_wavelength(self, wavelength=None, recalculate=True):
        self.is_single_wavelength = True
        self.wavelength = wavelength
        self.xray_tube_key=None
        self.secondary_wavelengths = []
        self.secondary_wavelengths_weights = []
        self.principal_wavelength_weight = self.get_principal_wavelenght_weight(recalculate=recalculate)

    def get_principal_wavelenght_weight(self, recalculate=False): # recalculate is to improve efficiency
        if not recalculate:
            return self.principal_wavelength_weight
        else:
            if not self.is_single_wavelength:
                total_weight = 0.0

                for weight in self.secondary_wavelengths_weights:
                    total_weight += weight.value

                if total_weight >= 1.0: raise ValueError("Weight of principal wavelength is <= 0")

                return 1.0 - total_weight

            else: return 1.0
