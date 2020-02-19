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
from iocbio.kinetics.calc.bump import AnalyzerBumpDatabase
from iocbio.kinetics.calc.generic import XYData
from .reader import ExperimentConfocalCaTransient

### Module flag
IocbioKineticsModule = ['analyzer']

#####################################################################################
## Calcium fluorescence analyzer
class AnalyzerCa(AnalyzerBumpDatabase):

    def __init__(self, database, data):
        self.database_table = "confocal_catransient_bump"
        self.signal = 'fluorescence'
        AnalyzerBumpDatabase.__init__(self, database, self.database_table,
                                      data, data.x(self.signal), data.y(self.signal).data,
                                      valunit="AU")
        self.axisnames = XYData("Time", "Fluorescence")
        self.axisunits = XYData("s", "AU")
        self.t_reference = 0
        self.fit()

    def fit(self):
        AnalyzerBumpDatabase.fit(self, n=3, points_per_node=5, max_nodes=15)
        
    def update_data(self, data):
        AnalyzerBumpDatabase.update_data(self, data.x(self.signal), data.y(self.signal).data)
        self.fit()

    def update_event(self, event_name):
        raise NotImplemented("You cannot update event names")

    @staticmethod
    def slice(data, x0, x1):
        sdata = data.slice(x0, x1)
        return sdata

    @staticmethod
    def auto_slicer(data):
        return []

#####################
#### ModuleAPI ######

def analyzer(database, data):
    Analyzer = {}
    p = {}
    s = []

    if data.type == ExperimentConfocalCaTransient.datatype_specific:
        Analyzer = { 'default': AnalyzerCa }

    return Analyzer, p, s

