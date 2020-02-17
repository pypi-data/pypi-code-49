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
# Analyzers that process primary streams coming from Electrophysiology and fitting the
# local fluorescence changes by bump spline

from iocbio.kinetics.calc.bump import AnalyzerBumpDatabase
from iocbio.kinetics.calc.generic import Stats, XYData, AnalyzerGenericSignals
from iocbio.kinetics.calc.mean_med_std import AnalyzerMeanMedStdDB
from iocbio.kinetics.calc.xy import AnalyzerXY
from iocbio.kinetics.calc.generic import XYData
from iocbio.kinetics.calc.composer import AnalyzerCompose
from iocbio.kinetics.constants import database_table_experiment

import iocbio.kinetics.global_vars as g

import numpy as np
from scipy.optimize import leastsq

### Module flag
IocbioKineticsModule = ['analyzer']


class AnalyzerElecFluoMax(AnalyzerMeanMedStdDB):

    database_table = "electrophysiology_fluorescence_maximum"

    def __init__(self, database, data):
        AnalyzerMeanMedStdDB.__init__(self, database, data, self.database_table, 'fluorescence')
        self.axisnames = XYData("Time", "Fluorescence")
        self.axisunits = XYData("s", "AU")
        self.fit()

    @staticmethod
    def slice(data, x0, x1):
        sdata = data.slice(x0, x1)
        sdata.event_name = 'High'
        sdata.event_value = None
        return sdata

    @staticmethod
    def auto_slicer(data):
        ch = 'fluorescence'
        x = data.x(ch)
        y = data.y(ch).data

        offset = 150
        mx = np.argmax(y)
        i0 = max(mx-offset, 0)
        i1 = min(mx+offset, x.size-1)

        print(x[mx], y[mx], i0, i1)

        return [AnalyzerElecFluoMax.slice(data, x[i0], x[i1])]


class AnalyzerElecFluo(AnalyzerBumpDatabase):

    database_table = "electrophysiology_fluorescence_bump"

    def __init__(self, database, data):
        AnalyzerBumpDatabase.__init__(self, database, AnalyzerElecFluo.database_table,
                                      data, data.x('fluorescence'), data.y('fluorescence').data)
        self.axisnames = XYData("Time", "Fluorescence")
        self.axisunits = XYData("s", "AU")

        self.set_reference_time()
        self.fit()

    def set_reference_time(self):
        # find corresponding event time
        events = g.data.config['events']
        etime = list(events.keys())
        etime.sort()
        t = None
        if len(self.experiment.x) > 0:
            x0 = self.experiment.x[0]
            for i in range(len(etime)-1):
                if etime[i] <= x0 and etime[i+1]>x0:
                    t = etime[i]
            if t is None and len(etime) > 0 and etime[-1] <= x0:
                t = etime[-1]
            if t is None and len(etime) == 1:
                t = etime[-1]

        self.t_reference = t
        print("Reference time:", t)

    def fit(self):
        AnalyzerBumpDatabase.fit(self,11)

    def update_data(self, data):
        AnalyzerBumpDatabase.update_data(self, data.x('fluorescence'), data.y('fluorescence').data)
        self.set_reference_time()
        self.fit()

    def update_event(self, event_name):
        raise NotImplemented("You cannot update event names")

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

        #ename = AnalyzerStrathkelvin.namecheck(ename)
        if ename.startswith('pulse_'):
            ename_tmp = ename[6:]
        else:
            ename_tmp = ename

        try:
            evalue = float(ename_tmp)
        except:
            evalue = None

        sdata.event_name = ename
        sdata.event_value = evalue
        return sdata

    @staticmethod
    def auto_slicer(data):
        events = data.config['events']
        etime = list(events.keys())
        etime.sort()
        if len(etime) == 0: return []

        sliced_data = []
        offset = 0.03#data.config['dt'] * 40
        for t in etime:
            sliced_data.append(AnalyzerElecFluo.slice(data, t+offset, t+1-offset))

        return sliced_data


class AnalyzerElecFluoRecoveryKinetics(AnalyzerXY):

    database_table = "electrophysiology_fluorescence_srrecovery_fit"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerElecFluoRecoveryKinetics.database_table) +
                 "(experiment_id text PRIMARY KEY, " +
                 "amplitude double precision, " +
                 "hill_coefficient double precision, " +
                 "ka double precision, " +
                 "baseline double precision, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) +
                 "(experiment_id) ON DELETE CASCADE)")

    @staticmethod
    def recovery_func(x, amplitude, ka, baseline, n):
        xn = x**n
        return amplitude*xn/(xn + ka**n) + baseline

    @staticmethod
    def recovery_error_func(v, y, x):
        amplitude, ka, baseline, n = v
        return y - AnalyzerElecFluoRecoveryKinetics.recovery_func(x, amplitude, ka, baseline, n)

    def __init__(self, database, table_name, value_name, data, axisnames, axisunits):
        AnalyzerXY.__init__(self, database, table_name, value_name, data, axisnames, axisunits)
        self.database_schema(database)
        self.analyze()

    def update(self):
        self.get_data()
        self.analyze()

    def update_database(self):
        c = self.database
        s = self.stats
        if self.database.has_record(self.database_table, experiment_id=self.experiment_id):
            c.query("UPDATE " + c.table(self.database_table) +
                    " SET amplitude=:amplitude, hill_coefficient=:hill_coefficient, ka=:ka, baseline=:baseline" +
                    " WHERE experiment_id=:experiment_id",
                    amplitude=s['amplitude'].value, hill_coefficient=s['hill_coefficient'].value,
                    ka=s['ka'].value, baseline=s['baseline'].value,
                    experiment_id=self.experiment_id)
        else:
            c.query("INSERT INTO " + c.table(self.database_table) +
                    " (experiment_id, amplitude, hill_coefficient, ka, baseline)" +
                    " VALUES(:experiment_id, :amplitude, :hill_coefficient, :ka, :baseline)",
                    experiment_id=self.experiment_id,
                    amplitude=s['amplitude'].value, hill_coefficient=s['hill_coefficient'].value,
                    ka=s['ka'].value, baseline=s['baseline'].value)

    def analyze(self):
        x, y = self.experiment.x, self.experiment.y
        if len(x) < 4 or len(y) < 4:
            self.stats['fail'] = Stats('Cannot fit! At least 4 points are needed', '', 0)
            return

        mn, mx = np.min(y), np.max(y)
        v0 = [mx-mn, 6, mn, 4]
        (amplitude, ka, baseline, n), msg = leastsq(self.recovery_error_func, v0, args=(y, x))

        self.stats['amplitude'] = Stats('Amplitude', 'AU', amplitude)
        self.stats['hill_coefficient'] = Stats('Hill coefficient', '', n)
        self.stats['ka'] = Stats('Half saturation', 'pulses', ka)
        self.stats['baseline'] = Stats('Baseline', 'AU', baseline)
        self.update_database()

        dx = 0.1
        xx = np.arange(x[0], x[-1]+dx, dx)
        self.calc = XYData(xx, self.recovery_func(xx, amplitude, ka, baseline, n))
        self.signals.sigUpdate.emit()


#####################
#### ModuleAPI ######

def analyzer(database, data):
    Analyzer = {}
    p = {}
    s = []
    if data.type == "SBMicroscope Electrophysiology LTCC":
        Analyzer['fluorescence'] = AnalyzerElecFluo
        p['fluorescence'] = \
            AnalyzerXY(database,
                       "electrophysiology_fluorescence_bump_amplitude",
                       "amplitude", data, XYData("Voltage", "Fluorescence amplitude"),
                       XYData("mV", "AU"))

    if data.type == "SBMicroscope Electrophysiology SR content by NCX":
        Analyzer['fluorescence'] = AnalyzerElecFluo

    if data.type == "SBMicroscope Electrophysiology SR recovery by LTCC":
        Analyzer['fluorescence'] = AnalyzerElecFluo
        p['fluorescence'] = \
            AnalyzerElecFluoRecoveryKinetics(database,
                                             "electrophysiology_fluorescence_bump_amplitude",
                                             "amplitude", data, XYData("Pulse number", "Fluorescence amplitude"),
                                             XYData("", "AU"))
        ac = AnalyzerCompose()
        ac.composer = True
        ac.add_analyzer('Current',
                        AnalyzerXY(database,
                                   "electrophysiology_current_srrecovery_i_max_fluorescenc",
                                   "value", data, XYData("Pulse number", "Current at max fluorescence"),
                                   XYData("", "pA")))
        ac.add_analyzer('Charge',
                        AnalyzerXY(database,
                                   "electrophysiology_current_srrecovery_charge",
                                   "value", data, XYData("Pulse number", "Charge"),
                                   XYData("", "pC")))

        p['sr recovery current'] = ac
        s.append(p['fluorescence'])
        
    if data.type == "SBMicroscope Electrophysiology Fluorescence maximum":
        Analyzer['fluorescence maximum'] = AnalyzerElecFluoMax
        
    return Analyzer, p, s
