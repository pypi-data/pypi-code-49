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

from orangecontrib.wonder.fit.parameters.fit_parameter import ParametersList, FitParameter
from orangecontrib.wonder.util.fit_utilities import Utilities, Symmetry
from oasys.widgets import congruence


class Phase(ParametersList):
    a = None
    b = None
    c = None

    alpha = None
    beta = None
    gamma = None

    symmetry = Symmetry.SIMPLE_CUBIC

    use_structure = False
    formula = None
    intensity_scale_factor = None
    name = ""

    def __init__(self, a, b, c, alpha, beta, gamma, symmetry=Symmetry.SIMPLE_CUBIC, use_structure=False, formula=None, intensity_scale_factor=None, name=""):
        super(Phase, self).__init__()

        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.symmetry = symmetry
        self.use_structure = use_structure
        self.formula = None if formula is None else formula.strip()
        self.intensity_scale_factor = intensity_scale_factor
        self.name = name

    @classmethod
    def get_parameters_prefix(cls):
        return "phase_"

    @classmethod
    def get_default_name(cls, phase_index=0):
        return "Phase " + str(phase_index + 1)

    @classmethod
    def is_cube(cls, symmetry):
        return symmetry in (Symmetry.BCC, Symmetry.FCC, Symmetry.SIMPLE_CUBIC)

    @classmethod
    def init_cube(cls, a0, symmetry=Symmetry.FCC, use_structure=False, formula=None, intensity_scale_factor=None, name="", progressive=""):
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

        return Phase(a,
                     b,
                     c,
                     alpha,
                     beta,
                     gamma,
                     symmetry=symmetry,
                     use_structure=use_structure,
                     formula=formula,
                     intensity_scale_factor=intensity_scale_factor,
                     name=name)

    def get_s(self, h, k, l):
        if Phase.is_cube(self.symmetry):
            if self.a.value is None:
                return 0
            else:
                return Utilities.s_hkl(self.a.value, h, k, l)
        else:
            NotImplementedError("Only Cubic supported: TODO!!!!!!")

    def get_d_spacing(self, h, k, l):
        if Phase.is_cube(self.symmetry):
            if self.a.value is None:
                return 0
            else:
                return 1 / Utilities.s_hkl(self.a.value, h, k, l)
        else:
            NotImplementedError("Only Cubic supported: TODO!!!!!!")

    def get_name(self, phase_index=0):
        try:
            congruence.checkEmptyString(self.name, "--")

            return self.name.strip()
        except:
            return Phase.get_default_name(phase_index)


