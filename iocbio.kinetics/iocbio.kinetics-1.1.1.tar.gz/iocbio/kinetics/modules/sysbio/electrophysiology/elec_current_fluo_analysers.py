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
# Secondary analyzers that combine electrophysiology current and fluorescence measurements

from PyQt5.QtCore import pyqtSignal, QObject
from iocbio.kinetics.calc.generic import AnalyzerGeneric, XYData

import numpy as np

#from .elec_current_analyzer import AnalyzerElecCurrent

### Module flag
IocbioKineticsModule = ['analyzer']

### Implementation

class AnalyserElecNCXcurrentFluoSignals(QObject):
    sigUpdate = pyqtSignal()


class AnalyserElecNCXcurrentFluo(AnalyzerGeneric):

    def __init__(self, database, table_name, value_name, data, axisnames, axisunits):
        #AnalyzerXY.__init__(self, database, table_name, value_name, data, axisnames, axisunits)
        AnalyzerGeneric.__init__(self, [], []) # start with empty data

        self.signals = AnalyserElecNCXcurrentFluoSignals()
        self.data = data
        self.database = database
        self.axisnames = axisnames
        self.axisunits = axisunits

    def get_data(self):
        # print('getting data')
        # print(dir(self.data))
        # print(self.data.data_id)
        # print(self.data.experiment_id)

        c = self.database
        x0, x1 = None, None
        for row in c.query("SELECT x0, x1 FROM " +
                           self.database.table('roi') +
                           " WHERE experiment_id=:experiment_id AND type='ncx current'",
                           experiment_id = self.data.experiment_id):

            x0, x1 = row.x0, row.x1

        if x0 is not None and x1 is not None:
            data = self.data.slice(x0, x1)
            cx, cy = data.x('current'), data.y('current').data
            fx, fy = data.x('fluorescence'), data.y('fluorescence').data

            new_cy = np.interp(fx, cx, cy)

            self.experiment = XYData(fy, new_cy)
            self.signals.sigUpdate.emit()


    def update(self):
        self.get_data()
        # print('update')

# class AnalyserElecNCXcurrentFluo(AnalyzerGeneric):
#
#     def __init__(self, database, data):
#         AnalyzerElecCurrent.__init__(self, database, data, baseline_subtraction=False)

#####################
#### ModuleAPI ######

def analyzer(database, data):
    if data.type == "SBMicroscope Electrophysiology SR content by NCX":
        return None, \
            { 'ncx current': AnalyserElecNCXcurrentFluo(database,
                                                        "electrophysiology_fluorescence_bump_amplitude",
                                                        "amplitude", data, XYData("Fluorescence amplitude", "Current"),
                                                        XYData("AU", "pA")) }, \
            None
    return None, None, None
