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
# Analyzers that process primary streams coming from respirometer and fitting the
# local oxygen changes by either linear relations or making some other analysis
# on the basis of raw oxygen trace

# This module is used through the other modules

import numpy as np

from iocbio.kinetics.calc.linreg import AnalyzerLinRegress
from iocbio.kinetics.calc.generic import Stats, XYData, AnalyzerGeneric
from iocbio.kinetics.calc.composer import AnalyzerCompose
from iocbio.kinetics.constants import database_table_roi, database_table_experiment

from PyQt5.QtCore import pyqtSignal, QObject

### Module flag
IocbioKineticsModule = ['database_schema']


class AnalyzerRespirationSignals(QObject):
    sigUpdate = pyqtSignal()


#######################################################################################
# Calculation of respiration rate from oxygen trace
class AnalyzerRespiration(AnalyzerLinRegress):

    database_table = "VO2_raw"
    database_conc_view = "VO2_raw_conc"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerRespiration.database_table) +
                 "(data_id text PRIMARY KEY, " +
                 "rate double precision, " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")
        if not db.has_view(AnalyzerRespiration.database_conc_view):
            db.query("CREATE VIEW " + db.table(AnalyzerRespiration.database_conc_view) + " AS SELECT "
                    "r.experiment_id, rate, event_value, event_name FROM " + db.table("roi") + " r join " +
                    db.table(AnalyzerRespiration.database_table) + " v on r.data_id = v.data_id")


    def __init__(self, database, data):
        self.database_schema(database)
        AnalyzerLinRegress.__init__(self, data.x('o2'), data.y('o2').data)

        self.signals = AnalyzerRespirationSignals()
        self.database = database
        self.table_name = AnalyzerRespiration.database_table
        self.data = data
        self.axisnames = XYData("Time", "O2")
        self.axisunits = XYData("min", "umol/l")

        self.fit()

    def fit(self):
        AnalyzerLinRegress.fit(self)
        if self.database is not None:
            c = self.database
            if self.database.has_record(self.table_name, data_id=self.data.data_id):
                c.query("UPDATE " + self.database.table(self.table_name) +
                          " SET rate=:rate WHERE data_id=:data_id",
                          rate=-self.slope, data_id=self.data.data_id)
            else:
                c.query("INSERT INTO " + self.database.table(self.table_name) +
                          "(data_id, rate) VALUES(:data_id,:rate)",
                          data_id=self.data.data_id, rate=-self.slope)
        self.stats['VO2'] = Stats("Respiration rate", "umol/l/min", -self.slope)
        self.signals.sigUpdate.emit()

    def remove(self):
        c = self.database
        c.query("DELETE FROM " + self.database.table(self.table_name) +
                " WHERE data_id=:data_id",
                data_id=self.data.data_id)
        self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()

    def update_data(self, data):
        AnalyzerLinRegress.update_data(self, data.x('o2'), data.y('o2').data)
        self.fit()

    def update_event(self, event_name):
        ename = AnalyzerRespiration.namecheck(event_name)
        try:
            evalue = float(ename)
        except:
            evalue = None
        self.data.event_name = ename
        self.data.event_value = evalue

    @staticmethod
    def namecheck(name):
        if name in ["CM"]:
            return "V0"
        return name

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
        if ename is None and etime[-1] <= x0:
            ename = events[ etime[-1] ]

        ename = AnalyzerRespiration.namecheck(ename)
        try:
            evalue = float(ename)
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
        def times(t0, t1):
            dt = (t1-t0)/4.0
            tm = (t0+t1)/2.0
            return tm-dt, tm+dt

        # v background
        sdata = AnalyzerRespiration.slice(data, *times(data.x('o2')[0],etime[0]))
        sdata.event_name = "VBG"
        sliced_data.append(sdata)

        for i in range(len(etime)-1):
            sliced_data.append(AnalyzerRespiration.slice(data, *times(etime[i],etime[i+1])))
        sliced_data.append(AnalyzerRespiration.slice(data,
                                                      *times(etime[-1], data.x('o2')[-1])))

        return sliced_data


#############################################################################################
# TMPD (auto)oxydation analyzer and its helper classes

class AnalyzerRespirationTMPD_VO2time(AnalyzerGeneric):
    def __init__(self, parent, data):
        AnalyzerGeneric.__init__(self, data.x('vo2'), data.y('vo2').data)
        self.parent = parent
        self.axisnames = XYData("Time", "VO2")
        self.axisunits = XYData("min", "umol/l/min")
        self.data = data
        self.fit()

    def fit(self):
        if not hasattr(self.parent, 'slope') or not hasattr(self.parent, 'intercept'): return
        time = self.data.x('o2_vo2')
        o2 = self.data.y('o2_vo2').data
        vo2 = [ self.parent.slope*o2[i] + self.parent.intercept for i in range(len(o2)) ]
        self.calc = XYData(time, vo2)

    def update_data(self, data):
        AnalyzerGeneric.update_data(self, data.x('vo2'), data.y('vo2').data)
        self.data = data
        self.fit()


class AnalyzerRespirationTMPD(AnalyzerLinRegress):

    database_table = 'VO2_TMPD_oxydation'
    signals = AnalyzerRespirationSignals()
    
    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerRespirationTMPD.database_table) +
                 "(data_id text PRIMARY KEY, " +
                 "slope double precision, " +
                 "intercept double precision, " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")

    def __init__(self, database, data):
        self.database_schema(database)
        AnalyzerLinRegress.__init__(self, data.y('o2_vo2').data, data.y('vo2').data)

        self.database = database
        self.data = data
        self.axisnames = XYData("O2", "VO2")
        self.axisunits = XYData("umol/l", "umol/l/min")

        self.fit()

        self.composer = True
        self.plot_vo2time = AnalyzerRespirationTMPD_VO2time(self, data)
        self.analyzers = {
            'VO2(O2)': self,
            'VO2(time)': self.plot_vo2time,
        }

    def fit(self):
        AnalyzerLinRegress.fit(self)
        if self.database is not None:
            c = self.database
            if self.database.has_record(self.database_table, data_id=self.data.data_id):
                c.query("UPDATE " + self.database.table(self.database_table) +
                          " SET slope=:slope, intercept=:intercept WHERE data_id=:data_id",
                          slope=self.slope, intercept=self.intercept, data_id=self.data.data_id)
            else:
                c.query("INSERT INTO " + self.database.table(self.database_table) +
                          "(data_id, slope, intercept) VALUES(:data_id,:slope,:intercept)",
                          data_id=self.data.data_id, slope=self.slope, intercept=self.intercept)
        self.stats['Slope'] = Stats("Slope", "1/min", self.slope)
        self.stats['Intercept'] = Stats("Intercept", "umol/l/min", self.intercept)
        self.signals.sigUpdate.emit()

    def list_analyzers(self):
        return list(self.analyzers.keys())

    def remove(self):
        c = self.database
        c.query("DELETE FROM " + self.database.table(self.database_table) +
                " WHERE data_id=:data_id",
                data_id=self.data.data_id)
        self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()

    def update_data(self, data):
        AnalyzerLinRegress.update_data(self, data.y('o2_vo2').data, data.y('vo2').data)
        self.fit()
        self.plot_vo2time.update_data(data)
        self.signals.sigUpdate.emit()

    def update_event(self, event_name):
        ename = AnalyzerRespiration.namecheck(event_name)
        try:
            evalue = float(ename)
        except:
            evalue = None
        self.data.event_name = ename
        self.data.event_value = evalue

    @staticmethod
    def slice(data, x0, x1):
        return AnalyzerRespiration.slice(data, x0, x1)

    @staticmethod
    def auto_slicer(data):
        return []

#############################################################################################
# Analyzer correcting for TMPD (auto)oxydation and its helper classes

class AnalyzerRespirationTMPDCorrected(AnalyzerGeneric):

    @staticmethod
    def der_function(o2, t, rate, eslope, eint):
        return [-rate - eslope*o2[0] - eint]

    @staticmethod
    def fit_function(o2_0, rate, eslope, eint, t):
        from scipy.integrate import odeint
        y = odeint(AnalyzerRespirationTMPDCorrected.der_function,
                   [o2_0], t, (rate, eslope, eint))
        return y.flatten()

    @staticmethod
    def error_function(v, t, y, slope, intercept):
        return y-AnalyzerRespirationTMPDCorrected.fit_function(*v, slope, intercept, t)

    def __init__(self, database, data):
        AnalyzerGeneric.__init__(self, data.x('o2'), data.y('o2').data)
        self.signals = AnalyzerRespirationSignals()
        self.database = database
        self.data = data # used by event name reader
        self.experiment_id = data.experiment_id
        self.axisnames = XYData("Time", "O2")
        self.axisunits = XYData("min", "umol/l")

        self.fit()
        AnalyzerRespirationTMPD.signals.sigUpdate.connect(self.update)

    def fit(self):
        from scipy.optimize import least_squares
        from iocbio.kinetics.constants import database_table_roi
        
        # get TMPD oxydation data
        c = self.database
        slope, intercept = None, None
        for row in c.query("SELECT AVG(slope) AS slope, AVG(intercept) AS intercept FROM " +
                           self.database.table(AnalyzerRespirationTMPD.database_table) + " v "
                           " JOIN " + self.database.table(database_table_roi) + " r ON r.data_id = v.data_id " +
                           " WHERE experiment_id=:experiment_id",
                             experiment_id=self.experiment_id):
            slope, intercept = row.slope, row.intercept

        if slope is not None and intercept is not None:

            t = np.array(self.experiment.x)
            t0 = t[0]
            y = np.array(self.experiment.y)
        
            r = least_squares(self.error_function, [200.0,1], args=(t, y, slope, intercept), 
                              loss='soft_l1', f_scale=1, tr_solver='exact',
                              ftol=1.e-10, xtol=1.e-10, max_nfev=100000)
            sol = r.x
            msg = r.message
            s = r.success
            self.o2_0, self.rate = sol

            self.calc = XYData(t, self.fit_function(*sol, slope, intercept, t))
            self.stats['VO2'] = Stats("Corrected respiration rate", "umol/l/min", self.rate)
            self.stats['O2_0'] = Stats("O2 at the start", "umol/l", self.o2_0)
            self.stats['Slope'] = Stats("TMPD slope", "1/min", slope)
            self.stats['Intercept'] = Stats("TMPD intercept", "umol/l/min", intercept)
            
            print(msg)
            print(sol)

        else:
            print('Cannot fit TMPD oxydation corrected data')

        self.signals.sigUpdate.emit()
        
    def remove(self):
        # c = self.database
        # c.query("DELETE FROM " + self.database.table(self.table_name) +
        #         " WHERE data_id=:data_id",
        #         data_id=self.data.data_id)
        # self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()

    def update(self):
        self.fit()

    def update_data(self, data):
        AnalyzerGeneric.update_data(self, data.x('o2'), data.y('o2').data)
        self.fit()

    def update_event(self, event_name):
        # ename = AnalyzerRespiration.namecheck(event_name)
        # try:
        #     evalue = float(ename)
        # except:
        #     evalue = None
        self.data.event_name = ename
        self.data.event_value = evalue

    @staticmethod
    def slice(data, x0, x1):
        return AnalyzerRespiration.slice(data, x0, x1)

    @staticmethod
    def auto_slicer(data):
        return []


#####################
#### ModuleAPI ######

def database_schema(db):
    AnalyzerRespiration.database_schema(db)
    AnalyzerRespirationTMPD.database_schema(db)
