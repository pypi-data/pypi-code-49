# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
from iocbio.kinetics.calc.composer import AnalyzerCompose
from iocbio.kinetics.calc.mean_med_std import AnalyzerMeanMedStdDB
import numpy as np

### Module flag
IocbioKineticsModule = ['analyzer']

#####################################################################################
# Low calcium
class AnalyzerMechUFreqCaSL_Low(AnalyzerCompose):
    """Low calcium"""
    def __init__(self, database, data):
        AnalyzerCompose.__init__(self)

        AnalyzerCompose.add_analyzer(self, "SL",
                                     AnalyzerMeanMedStdDB(database, data,
                                                          "mechanics_ufreqcasl_sl_calow",
                                                          'sarcomere length'))

        AnalyzerCompose.add_analyzer(self, "Ca Bound",
                                     AnalyzerMeanMedStdDB(database, data,
                                                          "mechanics_ufreqcasl_ca_bound_calow",
                                                          'fluorescence side'))
        if 'fluorescence bottom' in data.keys(): 
            AnalyzerCompose.add_analyzer(self, "Ca Free",
                                         AnalyzerMeanMedStdDB(database, data,
                                                              "mechanics_ufreqcasl_ca_free_calow",
                                                              'fluorescence bottom'))

        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.composer = True
        self.fit()

    @staticmethod
    def slice(data, x0, x1):
        sdata = data.slice(x0, x1)
        sdata.event_name = 'Low'
        sdata.event_value = None
        return sdata

    @staticmethod
    def auto_slicer(data):
        return []


#####################################################################################
# High calcium
class AnalyzerMechUFreqCaSL_High(AnalyzerCompose):
    """High calcium"""
    def __init__(self, database, data):
        AnalyzerCompose.__init__(self)

        AnalyzerCompose.add_analyzer(self, "Ca Bound",
                                     AnalyzerMeanMedStdDB(database, data,
                                                          "mechanics_ufreqcasl_ca_bound_cahigh",
                                                          'fluorescence side'))
        if 'fluorescence bottom' in data.keys(): 
            AnalyzerCompose.add_analyzer(self, "Ca Free",
                                         AnalyzerMeanMedStdDB(database, data,
                                                              "mechanics_ufreqcasl_ca_free_cahigh",
                                                              'fluorescence bottom'))

        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.composer = True
        self.fit()

    @staticmethod
    def slice(data, x0, x1):
        sdata = data.slice(x0, x1)
        sdata.event_name = 'High'
        sdata.event_value = None
        return sdata

    @staticmethod
    def auto_slicer(data):
        return []

#####################
#### ModuleAPI ######

def analyzer(database, data):
    """ModuleAPI"""
    Analyzer = {}
    if data.type == "SBMicroscope Mechanics Unloaded cardiomyocyte Ca and SL stimulation frequency response" or \
       data.type == "SBMicroscope Mechanics Loaded cardiomyocyte Ca and SL stimulation frequency response":
        Analyzer['low'] = AnalyzerMechUFreqCaSL_Low
        Analyzer['high'] = AnalyzerMechUFreqCaSL_High

    return Analyzer, None, None
