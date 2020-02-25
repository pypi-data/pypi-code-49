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

from orangecontrib.wonder.util.fit_utilities import Symmetry
from orangecontrib.wonder.fit.parameters.fit_parameter import FitParameter

from orangecontrib.wonder.fit.parameters.measured_data.phase import Phase

class GSASIIPhase(Phase):

    cif_file = None

    def __init__(self, a, b, c, alpha, beta, gamma, symmetry=Symmetry.SIMPLE_CUBIC, cif_file=None, formula=None, intensity_scale_factor=None, name=""):
        super(GSASIIPhase, self).__init__(a, b, c, alpha, beta, gamma, symmetry=symmetry, use_structure=True, formula=formula, intensity_scale_factor=intensity_scale_factor, name=name)

        self.cif_file = cif_file
        self.gsasii_reflections_list = None

    @classmethod
    def init_cube(cls, a0, symmetry=Symmetry.FCC, cif_file=None, formula=None, intensity_scale_factor=None, name="", progressive=""):
        if not cls.is_cube(symmetry): raise ValueError("Symmetry doesn't belong to a cubic crystal cell")

        if a0.fixed:
            a = FitParameter(parameter_name=Phase.get_parameters_prefix() + progressive + "a", value=a0.value, fixed=a0.fixed, boundary=a0.boundary)
            b = FitParameter(parameter_name=Phase.get_parameters_prefix() + progressive + "b", value=a0.value, fixed=a0.fixed, boundary=a0.boundary)
            c = FitParameter(parameter_name=Phase.get_parameters_prefix() + progressive + "c", value=a0.value, fixed=a0.fixed, boundary=a0.boundary)
        else:
            a = a0
            b = FitParameter(parameter_name=Phase.get_parameters_prefix() + progressive + "b", function=True, function_value=Phase.get_parameters_prefix() + progressive + "a")
            c = FitParameter(parameter_name=Phase.get_parameters_prefix() + progressive + "c", function=True, function_value=Phase.get_parameters_prefix() + progressive + "a" )

        alpha = FitParameter(parameter_name=Phase.get_parameters_prefix() + progressive + "alpha", value=90, fixed=True)
        beta  = FitParameter(parameter_name=Phase.get_parameters_prefix() + progressive + "beta",  value=90, fixed=True)
        gamma = FitParameter(parameter_name=Phase.get_parameters_prefix() + progressive + "gamma", value=90, fixed=True)

        return GSASIIPhase(a,
                           b,
                           c,
                           alpha,
                           beta,
                           gamma,
                           symmetry=symmetry,
                           cif_file=cif_file,
                           formula=formula,
                           intensity_scale_factor=intensity_scale_factor,
                           name=name)
