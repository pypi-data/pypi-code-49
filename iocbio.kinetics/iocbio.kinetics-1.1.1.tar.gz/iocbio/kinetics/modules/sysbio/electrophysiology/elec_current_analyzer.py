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
# local current parameters, eg integral, peak

from iocbio.kinetics.calc.current import AnalyzerCurrent
from iocbio.kinetics.calc.generic import Stats, XYData
from iocbio.kinetics.calc.current import AnalyzerCurrentIV
from iocbio.kinetics.constants import database_table_roi

import iocbio.kinetics.global_vars as g

from PyQt5.QtCore import pyqtSignal, QObject
import numpy as np

### Module flag
IocbioKineticsModule = ['analyzer']

### Implementation

class AnalyzerElecCurrentSignals(QObject):
    sigUpdate = pyqtSignal()


class AnalyzerElecCurrent(AnalyzerCurrent):

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

    def __init__(self, database, data, baseline_subtraction=True):
        self.database_schema(database)
        AnalyzerCurrent.__init__(self, data.x('current'), data.y('current').data, baseline_subtraction)

        self.signals = AnalyzerElecCurrentSignals()
        self.database = database
        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.axisnames = XYData("Time", "Current")
        self.axisunits = XYData("s", "pA")

        self.set_reference_time()
        self.fit()
        self.update_database()

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
        n = 7
        if self.experiment.y.size < n:
            return
        AnalyzerCurrent.fit(self, n)

        self.stats['time to peak'] = Stats('time to peak', 's', self.stats['arg to peak'].value - self.t_reference)
        del self.stats['arg to peak']

    def update_database(self):
        if self.database is not None:
            c = self.database
            for k, v in self.stats.items():
                # print(k,v)
                if self.database.has_record(self.database_table, data_id=self.data_id, type=k):
                    c.query("UPDATE " + self.database.table(self.database_table) +
                              " SET value=:value WHERE data_id=:data_id AND type=:type",
                              value=v.value, data_id=self.data_id, type=k)
                else:
                    c.query("INSERT INTO " + self.database.table(self.database_table) +
                              "(data_id, type, value) VALUES(:data_id,:type,:value)",
                              data_id=self.data_id, type=k, value=v.value)
        self.signals.sigUpdate.emit()

    def remove(self):
        c = self.database
        c.query("DELETE FROM " + self.database.table(self.database_table) +
                " WHERE data_id=:data_id",
                data_id=self.data_id)
        self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()

    def update_data(self, data):
        AnalyzerCurrent.update_data(self, data.x('current'), data.y('current').data)
        self.set_reference_time()
        self.fit()
        self.update_database()

    def update_event(self, event_name):
        raise NotImplemented("You cannot update event names")


class AnalyzerElecCurrentTail(AnalyzerElecCurrent):

    database_table = "electrophysiology_current_tail"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerElecCurrentTail.database_table) +
                 "(data_id text not null, " +
                 "type text not null, value double precision, PRIMARY KEY(data_id, type), " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")

        for view, param in [['_qv', 'charge carried']]:#, ['_ttp', 'time to peak']]:[['_iv', 'current peak']]:#
            viewname = AnalyzerElecCurrentTail.database_table + view
            if not db.has_view(viewname):
                db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                         "r.experiment_id, r.event_name, r.event_value, param.value " +
                         "FROM " + db.table(AnalyzerElecCurrentTail.database_table) + " param " +
                         "INNER JOIN " + db.table("roi") + " r ON param.data_id=r.data_id " +
                         "WHERE param.type='%s'" % param)

    @staticmethod
    def auto_slicer(data):
        events = data.config['events']
        etime = list(events.keys())
        etime.sort()
        if len(etime) == 0: return []

        sliced_data = []
        offset = data.config['dt'] * 40
        for t in etime:
            sliced_data.append(AnalyzerElecCurrentTail.slice(data, t+offset+0.45, t+0.95))

        return sliced_data

    def __init__(self, database, data):
        AnalyzerElecCurrent.__init__(self, database, data)


class AnalyzerElecCurrentStep(AnalyzerElecCurrent):

    database_table = "electrophysiology_current_step"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerElecCurrentStep.database_table) +
                 "(data_id text not null, " +
                 "type text not null, value double precision, PRIMARY KEY(data_id, type), " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")

        for view, param in [['_iv', 'current peak']]:#, ['_qv', 'charge carried'], ['_ttp', 'time to peak']]:
            viewname = AnalyzerElecCurrentStep.database_table + view
            if not db.has_view(viewname):
                db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                         "r.experiment_id, r.event_name, r.event_value, param.value " +
                         "FROM " + db.table(AnalyzerElecCurrentStep.database_table) + " param " +
                         "INNER JOIN " + db.table("roi") + " r ON param.data_id=r.data_id " +
                         "WHERE param.type='%s'" % param)

    @staticmethod
    def auto_slicer(data):
        events = data.config['events']
        etime = list(events.keys())
        etime.sort()
        if len(etime) == 0: return []

        sliced_data = []
        offset = data.config['dt'] * 25
        for t in etime:
            sl = AnalyzerElecCurrentStep.slice(data, t+0.2, t+0.45)
            x = np.array(sl.x('current'))
            y = np.array(sl.y('current').data)

            x_larger_baseline = x[y >= y[-20:].mean()]
            x_peak = x[np.argmin(y)]
            y_max_ind = np.argmax(y)
            if x_peak < x[y_max_ind]:
                y_min_ind = np.argmin(y[y_max_ind:])
                x_peak = x[y_max_ind:][y_min_ind]

            x_rel = x_larger_baseline[x_larger_baseline < x_peak]

            if x_rel.size < 0:
                t0 = t + offset + 0.2
            else:
                t0 = max(x_rel[-1], t+offset+0.2)
                # print('event, t0', t, t0)
            del sl

            sliced_data.append(AnalyzerElecCurrentStep.slice(data, t0, t+0.45))

        return sliced_data

    def __init__(self, database, data, baseline_subtraction=True):
        AnalyzerElecCurrent.__init__(self, database, data, baseline_subtraction)


class AnalyzerElecCurrentSRRecovery(AnalyzerElecCurrent):

    database_table = "electrophysiology_current_srrecovery"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerElecCurrentSRRecovery.database_table) +
                 "(data_id text not null, " +
                 "type text not null, value double precision, PRIMARY KEY(data_id, type), " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")

        for view, param in [['_charge', 'charge carried'], ['_i_max_fluorescenc', 'current at max fluorescence']]:
            viewname = AnalyzerElecCurrentSRRecovery.database_table + view
            if not db.has_view(viewname):
                db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                         "r.experiment_id, r.event_name, r.event_value, param.value " +
                         "FROM " + db.table(AnalyzerElecCurrentSRRecovery.database_table) + " param " +
                         "INNER JOIN " + db.table("roi") + " r ON param.data_id=r.data_id " +
                         "WHERE param.type='%s'" % param)

    @staticmethod
    def auto_slicer(data):
        events = data.config['events']
        etime = list(events.keys())
        etime.sort()
        if len(etime) == 0: return []

        sliced_data = []
        offset = data.config['dt'] * 25
        for t in etime:
            # sl = AnalyzerElecCurrentSRRecovery.slice(data, t+0.1, t+0.35)
            # x = np.array(sl.x('current'))
            # y = np.array(sl.y('current').data)
            #
            # x_larger_baseline = x[y >= y[-20:].mean()]
            # x_peak = x[np.argmin(y)]
            # y_max_ind = np.argmax(y)
            # if x_peak < x[y_max_ind]:
            #     y_min_ind = np.argmin(y[y_max_ind:])
            #     x_peak = x[y_max_ind:][y_min_ind]
            #
            # x_rel = x_larger_baseline[x_larger_baseline < x_peak]
            #
            # if x_rel.size < 0:
            #     t0 = t + offset + 0.1
            # else:
            #     t0 = max(x_rel[-1], t+offset+0.1)
            # del sl

            t0 = t + offset + 0.1

            sliced_data.append(AnalyzerElecCurrentSRRecovery.slice(data, t0, t+0.35))

        return sliced_data

    def __init__(self, database, data):
        AnalyzerElecCurrent.__init__(self, database, data, baseline_subtraction=True)

    def fit(self):
        n = 7
        if self.experiment.y.size < n:
            return
        AnalyzerCurrent.fit(self, n)
        self.stats['time to peak'] = Stats('time to peak', 's', self.stats['arg to peak'].value - self.t_reference)
        del self.stats['arg to peak']

        # print(self.experiment.x[0], self.experiment.x[-1])

        nslice = self.data.slice(self.experiment.x[0], self.experiment.x[-1])
        c_x = nslice.x('current')
        c_y = nslice.y('current').data
        fl_x = nslice.x('fluorescence')
        fl_y = nslice.y('fluorescence').data

        if fl_y.size < n:
            print('Cannot fit because there is less than %i data points')
            return

        k = np.blackman(n)
        k /= k.sum()
        fl_c = np.convolve(k, fl_y, mode='same')
        c_c = np.convolve(k, c_y, mode='same')

        k = np.blackman(251)
        k /= k.sum()
        tmx = fl_x[np.argmax(fl_c)]
        c_at_max_fl = c_c[np.argmin(np.abs(c_x-tmx))]

        self.stats['current at max fluorescence'] = Stats('current at maximum fluorescence', 'pA', c_at_max_fl)
        self.update_database()


class AnalyzerElecCurrentNCX(AnalyzerElecCurrent):

    database_table = "electrophysiology_caffeine_current_ncx"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerElecCurrentNCX.database_table) +
                 "(data_id text not null, " +
                 "type text not null, value double precision, PRIMARY KEY (data_id, type), " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")

    @staticmethod
    def auto_slicer(data):
        events = data.config['events']
        etime = list(events.keys())
        etime.sort()
        if len(etime) == 0: return []

        sliced_data = []
        for t in etime:
            sliced_data.append(AnalyzerElecCurrentNCX.slice(data, t, t+10))

        return sliced_data

    def __init__(self, database, data):
        AnalyzerElecCurrent.__init__(self, database, data)


#####################
#### ModuleAPI ######

def analyzer(database, data):
    Analyzer = {}
    p = {}
    s = []
    if data.type == "SBMicroscope Electrophysiology LTCC":
        Analyzer['step current'] = AnalyzerElecCurrentStep
        p['step current'] = \
            AnalyzerCurrentIV(database,
                              "electrophysiology_current_step_iv",
                              "value", data, XYData("Voltage", "Peak current"),
                              XYData("mV", "pA"))
        s.append(p['step current'])
    if data.type == "SBMicroscope Electrophysiology SR content by NCX":
        Analyzer['ncx current'] = AnalyzerElecCurrentNCX
    if data.type == "SBMicroscope Electrophysiology SR recovery by LTCC":
        Analyzer['sr recovery current']=AnalyzerElecCurrentSRRecovery

    return Analyzer, p, s
