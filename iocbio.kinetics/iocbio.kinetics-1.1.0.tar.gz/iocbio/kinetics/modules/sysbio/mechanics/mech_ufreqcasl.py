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
from iocbio.kinetics.calc.bump import AnalyzerBumpDatabase
from iocbio.kinetics.calc.generic import XYData

import numpy as np

### Module flag
IocbioKineticsModule = ['analyzer']

#####################################################################################
## Sarcomere length, fiber deformation analyzer, included in the main analyzer below
class AnalyzerMechFreqmech(AnalyzerBumpDatabase):
    """Sarcomere length, fiber deformation analyzer, included in the main analyzer"""
    
    def __init__(self, database, data, database_table, signal, peak):
        self.database_table = database_table
        self.signal = signal
        AnalyzerBumpDatabase.__init__(self, database, self.database_table,
                                      data, data.x(self.signal), data.y(self.signal).data,
                                      peak=peak, valunit="um")
        self.axisnames = XYData("Time", signal)
        self.axisunits = XYData("s", "um")
        self.t_reference = data.reference_time
        self.fit()

    def fit(self):
        AnalyzerBumpDatabase.fit(self, n=3, points_per_node=4, max_nodes=25)
        
    def update_data(self, data):
        self.t_reference = data.reference_time
        AnalyzerBumpDatabase.update_data(self, data.x(self.signal), data.y(self.signal).data)
        self.fit()

    def update_event(self, event_name):
        raise NotImplemented("You cannot update event names")
    
#####################################################################################
## Calcium fluorescence analyzer, included in the main analyzer below    
class AnalyzerMechFreqCa(AnalyzerBumpDatabase):
    """Calcium fluorescence analyzer, included in the main analyzer"""
    def __init__(self, database, data, database_table, signal, peak):
        self.database_table = database_table
        self.signal = signal
        AnalyzerBumpDatabase.__init__(self, database, self.database_table,
                                      data, data.x(self.signal), data.y(self.signal).data,
                                      peak=peak, valunit="AU")
        self.axisnames = XYData("Time", "Fluorescence")
        self.axisunits = XYData("s", "AU")
        self.t_reference = data.reference_time
        self.fit()

    def fit(self):
        AnalyzerBumpDatabase.fit(self, n=3, points_per_node=2, max_nodes=15)
        
    def update_data(self, data):
        self.t_reference = data.reference_time
        AnalyzerBumpDatabase.update_data(self, data.x(self.signal), data.y(self.signal).data)
        self.fit()

    def update_event(self, event_name):
        raise NotImplemented("You cannot update event names")
       
#####################################################################################
## Main analyzers
class AnalyzerMechFreqCaSL(AnalyzerCompose):
    """Main analyzers"""
    def __init__(self, database, data):

        AnalyzerCompose.__init__(self)
        data.reference_time = self.reftime(data)
        AnalyzerCompose.add_analyzer(self, "SL", AnalyzerMechFreqmech(database, data, "mechanics_ufreqcasl_sl", "sarcomere length", False ))
        AnalyzerCompose.add_analyzer(self, "Ca Bound", AnalyzerMechFreqCa(database, data, "mechanics_ufreqcasl_ca_bound", 'fluorescence side', True  ))
        if 'fluorescence bottom' in data.keys(): 
            AnalyzerCompose.add_analyzer(self, "Ca Free", AnalyzerMechFreqCa(database, data, "mechanics_ufreqcasl_ca_free",  'fluorescence bottom', False ))
        if data.type =='SBMicroscope Mechanics Loaded cardiomyocyte Ca and SL stimulation frequency response': 
            AnalyzerCompose.add_analyzer(self, "Left fiber", AnalyzerMechFreqmech(database, data, "mechanics_ufreqcasl_left_def", 'deformation left fiber', False ))
            AnalyzerCompose.add_analyzer(self, "Right fiber", AnalyzerMechFreqmech(database, data,"mechanics_ufreqcasl_right_def", 'deformation right fiber', True ))
        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.composer = True

    @staticmethod
    def reftime(data):
        x0, x1 = data.xlim()
        return data.get_reference_time((x0+x1)/2)

    def update_data(self, data):
        data.reference_time = self.reftime(data)
        AnalyzerCompose.update_data(self, data)

    @staticmethod
    def slice(data, x0, x1):
        sdata = data.slice(x0, x1)
        events = data.config['events']
        etime = list(events.keys())
        etime.sort()
        ename = None

        for i in range(len(etime)-1):
            if etime[i] <= x0 and etime[i+1]>x0:
                ename = events[ etime[i] ]
        if ename is None and len(etime) > 0 and etime[-1] <= x0:
            ename = events[ etime[-1] ]

        try:
            evalue = float(ename)
        except:
            evalue = None

        sdata.event_name = ename+' -> %i' % data.get_pulse_no(0.5*(x1+x0))
        sdata.event_value = evalue
        return sdata

    @staticmethod
    def auto_slicer(data):
        events = data.config['events']
        etime = sorted(list(events.keys()))

        if len(etime) == 0:
            return []

        #offset = 0.1
        offset = 0.15
        return [AnalyzerMechFreqCaSL.slice(data, t0-offset, t1) for t0, t1 in data.get_auto_slice_ranges()]


#####################
#### ModuleAPI ######

def analyzer(database, data):
    Analyzer = {}
    if data.type == "SBMicroscope Mechanics Unloaded cardiomyocyte Ca and SL stimulation frequency response" or \
       data.type == "SBMicroscope Mechanics Loaded cardiomyocyte Ca and SL stimulation frequency response":
        Analyzer['default'] = AnalyzerMechFreqCaSL

    return Analyzer, None, None
