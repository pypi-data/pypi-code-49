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
from orangecontrib.wonder.fit.parameters.measured_data.line_profile import LineProfile

class MeasuredDataset(ParametersList):

    diffraction_patterns = None

    incident_radiations = None
    phases = None
    line_profiles = None

    initialized = False

    def __init__(self,
                 diffraction_patterns = None,
                 incident_radiations = None,
                 phases = None,
                 line_profiles = None):
        self.phases = phases
        self.diffraction_patterns = diffraction_patterns
        self.incident_radiations = incident_radiations
        self.line_profiles = line_profiles
        self.initialized = False

    @classmethod
    def initialize_with_diffraction_patterns(cls, diffraction_patterns=[]):
        if diffraction_patterns is None: raise ValueError("Diffraction Patterns is None")
        if not isinstance(diffraction_patterns, list): raise ValueError("Diffraction Patterns is not a list")
        if len(diffraction_patterns) < 1: raise ValueError("Diffraction Patterns list is empty")

        dataset = MeasuredDataset(diffraction_patterns=diffraction_patterns)

        diffraction_patterns_number = dataset.get_diffraction_patterns_number()

        dataset.line_profiles = [None] * diffraction_patterns_number
        dataset.initialized = True

        return dataset

    def set_phases(self, phases=None):
        if not self.initialized: raise ValueError("MeasuredDataset not intialized")
        if phases is None: raise ValueError("Phases is None")
        if not isinstance(phases, list): raise ValueError("Phases is not a list")
        if len(phases) < 1: raise ValueError("Phases list is empty")

        self.phases=phases

        diffraction_patterns_number = self.get_diffraction_patterns_number()

        if self.initialized and diffraction_patterns_number > 0:
            for diffraction_pattern_index in range(diffraction_patterns_number):
                if self.line_profiles[diffraction_pattern_index] is None:
                    self.line_profiles[diffraction_pattern_index] = LineProfile(self.phases)
                else:
                    self.line_profiles[diffraction_pattern_index].set_phases(self.phases)

    def get_diffraction_patterns_number(self):
        try:
            return len(self.diffraction_patterns)
        except:
            return 0

    def get_phases_number(self):
        try:
            return len(self.phases)
        except:
            return 0

    def get_diffraction_pattern(self, diffraction_pattern_index):
        try:
            return self.diffraction_patterns[diffraction_pattern_index]
        except:
            return None

    def get_phase(self, phase_index):
        try:
            return self.phases[phase_index]
        except:
            return None

    def get_line_profile(self, diffraction_pattern_index):
        try:
            return self.line_profiles[diffraction_pattern_index]
        except:
            return None

    def get_incident_radiations_item(self, diffraction_pattern_index):
        try:
            return self.incident_radiations[0 if len(self.incident_radiations) == 1 else diffraction_pattern_index]
        except:
            return None

    @classmethod
    def __duplicate_attributes_list(cls, attributes_list):
        if attributes_list is None: attributes_list_copy = None
        else:
            dimension = len(attributes_list)
            attributes_list_copy = [None]*dimension
            for index in range(dimension):
                attributes_list_copy[index] = attributes_list[index].duplicate()

        return attributes_list_copy

    def duplicate_diffraction_patterns(self):
        return MeasuredDataset.__duplicate_attributes_list(self.diffraction_patterns)

    def duplicate(self):
        diffraction_patterns = MeasuredDataset.__duplicate_attributes_list(self.diffraction_patterns)
        incident_radiations  = MeasuredDataset.__duplicate_attributes_list(self.incident_radiations)
        phases               = MeasuredDataset.__duplicate_attributes_list(self.phases)
        line_profiles        = MeasuredDataset.__duplicate_attributes_list(self.line_profiles)

        dataset = MeasuredDataset(diffraction_patterns=diffraction_patterns,
                                  incident_radiations=incident_radiations,
                                  phases=phases,
                                  line_profiles=line_profiles)

        dataset.initialized = self.initialized

        return dataset

