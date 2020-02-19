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
# Analyzers that process primary streams coming from Spectrophotometer and fitting the
# local absorbance changes by linear relations

from iocbio.kinetics.calc.linreg import AnalyzerLinRegress, AnalyzerLinRegressDB
from iocbio.kinetics.calc.explin_fit import AnalyzerExpLinFit
from iocbio.kinetics.calc.generic import Stats, XYData
from iocbio.kinetics.calc.mm import AnalyzerMMDatabase
from iocbio.kinetics.constants import database_table_roi, database_table_experiment

from PyQt5.QtCore import pyqtSignal, QObject

### Module flag
IocbioKineticsModule = ['analyzer', 'database_schema']

### Implementation

class AnalyzerSpectroSignals(QObject):
    sigUpdate = pyqtSignal()


class AnalyzerSpectro(AnalyzerLinRegress):

    table_name = "spectro_dabsdt_raw"
    view_name = "spectro_dabsdt_raw_conc"
    
    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerSpectro.table_name) +
                 "(data_id text PRIMARY KEY, " +
                 "rate double precision, " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")
        viewname=AnalyzerSpectro.view_name
        if not db.has_view(viewname):
            db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT "
                    "r.experiment_id, rate, event_value, event_name FROM " + db.table("roi") + " r join " +
                    db.table(AnalyzerSpectro.table_name) + " v on r.data_id = v.data_id")


    def __init__(self, database, data):
        self.database_schema(database)
        AnalyzerLinRegress.__init__(self, data.x('abs'), data.y('abs').data)

        self.signals = AnalyzerSpectroSignals()
        self.database = database
        self.data = data
        self.axisnames = XYData("Time", "Absorbance")
        self.axisunits = XYData("min", "")

        self.fit()

    def fit(self):
        AnalyzerLinRegress.fit(self)
        if self.slope is None or self.intercept is None:
            self.remove()
            return
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
        self.stats['Rate'] = Stats("Absorbance change rate", "Abs/min", -self.slope)
        self.signals.sigUpdate.emit()

    def remove(self):
        c = self.database
        c.query("DELETE FROM " + self.database.table(self.table_name) +
                " WHERE data_id=:data_id",
                data_id=self.data.data_id)
        self.signals.sigUpdate.emit()

    def update_data(self, data):
        AnalyzerLinRegress.update_data(self, data.x('abs'), data.y('abs').data)
        self.fit()

    def update_event(self, event_name):
        ename = AnalyzerSpectro.namecheck(event_name)
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
        xref = (x0+x1)/2.0
        ename = None
        for _,e in data.config['events_slice'].items():
            if e['time'][0] <= xref and e['time'][1]>xref:
                ename = e['name']
                break

        try:
            evalue = float(ename)
        except:
            evalue = None

        sdata.event_name = ename
        sdata.event_value = evalue
        return sdata

    @staticmethod
    def auto_slicer(data):
        events = data.config['events_slice']

        sliced_data = []
        def times(t0, t1):
            dt = (t1-t0)/4.0
            tm = (t0+t1)/2.0
            return tm-dt, tm+dt

        for _, i in events.items():
            sliced_data.append(AnalyzerSpectro.slice(data, *times(i['time'][0],i['time'][1])))

        return sliced_data


class AnalyzerSpectroCytOx(AnalyzerExpLinFit):

    table_name = 'spectro_cytox'

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerSpectroCytOx.table_name) +
                 "(data_id text PRIMARY KEY, " +
                 "exponential_amplitude double precision, rate_constant double precision, " +
                 "linear_offset double precision, linear_slope double precision, " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")

    def __init__(self, database, data):
        self.database_schema(database)
        AnalyzerExpLinFit.__init__(self, data.x('abs'), data.y('abs').data)

        self.signals = AnalyzerSpectroSignals()
        self.database = database
        self.data = data

        self.axisnames = XYData("Time", "Absorbance")
        self.axisunits = XYData("min", "")

        self.fit()

    def fit(self):
        AnalyzerExpLinFit.fit(self)
        if self.database is not None:
            c = self.database
            if self.database.has_record(self.table_name, data_id=self.data.data_id):
                c.query("UPDATE " + self.database.table(self.table_name) +
                        " SET exponential_amplitude=:exponential_amplitude, rate_constant=:rate_constant, " +
                        "linear_offset=:linear_offset, linear_slope=:linear_slope WHERE data_id=:data_id",
                        exponential_amplitude=self.exponential_amplitude,
                        rate_constant=self.rate_constant,
                        linear_offset=self.linear_offset,
                        linear_slope=self.linear_slope,
                        data_id=self.data.data_id)
            else:
                c.query("INSERT INTO " + self.database.table(self.table_name) +
                        " (data_id, exponential_amplitude, rate_constant, linear_offset, linear_slope) " +
                        " VALUES(:data_id, :exponential_amplitude, :rate_constant, :linear_offset, :linear_slope)",
                        exponential_amplitude=self.exponential_amplitude,
                        rate_constant=self.rate_constant,
                        linear_offset=self.linear_offset,
                        linear_slope=self.linear_slope,
                        data_id=self.data.data_id)

        self.signals.sigUpdate.emit()

    def remove(self):
        c = self.database
        c.query("DELETE FROM " + self.database.table(self.table_name) +
                " WHERE data_id=:data_id",
                data_id=self.data.data_id)
        self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()

    def update_data(self, data):
        AnalyzerExpLinFit.update_data(self, data.x('abs'), data.y('abs').data)
        self.fit()

    def update_event(self, event_name):
        self.data.event_name = event_name
        self.data.event_value = 0

    @staticmethod
    def slice(data, x0, x1):
        sdata = data.slice(x0, x1)
        return sdata

    @staticmethod
    def auto_slicer(data):
        return []
        # x = data.x('abs')
        # l = len(x)
        # x0, x1 = data.x('abs')[int(0.2*l)], data.x('abs')[int(0.8*l)]
        # sliced_data = [AnalyzerSpectroCytOx.slice(data, x0, x1)]
        # return sliced_data


#############################################################################

class AnalyzerSpectroTrace(AnalyzerLinRegressDB):

    def __init__(self, database, data):
        AnalyzerLinRegressDB.__init__(self, database=database, data=data, channel='abs')
        self.axisnames = XYData("Time", "Absorbance")
        self.axisunits = XYData("min", "")
        self.fit()

    def fit(self):
        AnalyzerLinRegressDB.fit(self)
        self.stats['Rate'] = Stats("Absorbance change rate", "Abs/min", -self.slope)
        self.signals.sigUpdate.emit()

############################################################################

class AnalyzerSpectroMM_ATParg(AnalyzerMMDatabase):
    def __init__(self, database, data):
        AnalyzerMMDatabase.__init__(self, database,
                                    "spectro_dabsdt_mm_raw",
                                    AnalyzerSpectro.view_name,
                                    data.experiment_id)
        self.axisnames = XYData("ATP", "dAbs/dt")
        self.axisunits = XYData("mM or possibly other", "1/min")


#####################
#### ModuleAPI ######

def analyzer(database, data):
    titration_types = {
        'Thermo Evo 600 AK activity F': 'ak_activity_forward',
        'Thermo Evo 600 AK activity R': 'ak_activity_reverse',
        'Thermo Evo 600 ATPase activity': 'atpase_activity',
        'Thermo Evo 600 CK activity': 'ck_activity',
        'Thermo Evo 600 PK activity': 'pk_activity',
        'Thermo Evo 600 HK activity': 'hk_activity',
        }

    Analyzer = None
    overall = None
    if data.type in titration_types:
        Analyzer = { 'default': AnalyzerSpectro }
    elif data.type == "Thermo Evo 600 Spectro CytOx":
        Analyzer = { 'default': AnalyzerSpectroCytOx }
    elif data.type == "Thermo Evo 600 Spectro Trace":
        Analyzer = { 'default': AnalyzerSpectroTrace }
    else:
        return None, None, None

    if data.type in ['Thermo Evo 600 ATPase activity', 'Thermo Evo 600 PK activity']:
        overall = dict(default = AnalyzerSpectroMM_ATParg(database, data))
    
    return Analyzer, overall, None


def database_schema(db):
    AnalyzerSpectro.database_schema(db)
    AnalyzerSpectroCytOx.database_schema(db)
