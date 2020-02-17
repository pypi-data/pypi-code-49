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
# Analyzers that get data already in the form concentration/VO2
# and fit it with MM relationship

from iocbio.kinetics.calc.mm import AnalyzerMM
from iocbio.kinetics.calc.generic import AnalyzerGeneric, XYData, Stats
from iocbio.kinetics.constants import database_table_experiment
from .analyzer_primary import AnalyzerRespiration

import numpy as np
from PyQt5.QtCore import pyqtSignal, QObject

### Module flag
IocbioKineticsModule = ['analyzer', 'database_schema']

# General signaling class
class AnalyzerRespirationSignals(QObject):
    sigUpdate = pyqtSignal()

##############################################################
# respiration analysis using Michaelis-Menten relationship
class AnalyzerRespirationMM(AnalyzerMM):

    database_table = "VO2_titration_mm_raw"
    
    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerRespirationMM.database_table) +
                 "(experiment_id text PRIMARY KEY, " +
                 "vmax double precision, km double precision, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")


    def __init__(self, database, data):
        self.database_schema(database)
        AnalyzerMM.__init__(self, [], []) # start with empty data

        self.signals = AnalyzerRespirationSignals()
        self.database = database
        self.table_name = AnalyzerRespirationMM.database_table
        self.table_source = AnalyzerRespiration.database_conc_view
        self.experiment_id = data.experiment_id

        self.get_data()
        self.fit()

    def get_data(self):
        c = self.database
        v0 = 0
        v = []
        conc = []
        for row in c.query("SELECT rate, event_name, event_value FROM " +
                           self.database.table(self.table_source) +
                           " WHERE experiment_id=:experiment_id",
                           experiment_id = self.experiment_id):
            r = row.rate
            n = row.event_name
            c = row.event_value
            if n == "V0":
                v0 = r
            elif c is not None:
                v.append(r)
                conc.append(c)
        v = np.array(v)
        conc = np.array(conc)
        v = v - v0
        self.experiment = XYData(conc, v)

    def fit(self):
        AnalyzerMM.fit(self)
        c = self.database
        if self.database.has_record(self.table_name, experiment_id=self.experiment_id):
            c.query("UPDATE " + self.database.table(self.table_name) +
                    " SET vmax=:vmax, km=:km WHERE experiment_id=:experiment_id",
                    vmax=self.vmax, km=self.km, experiment_id=self.experiment_id)
        else:
            c.query("INSERT INTO " + self.database.table(self.table_name) +
                    "(experiment_id, vmax, km) VALUES(:experiment_id,:vmax,:km)",
                    experiment_id=self.experiment_id, vmax=self.vmax, km=self.km)
        self.stats['VO2 max'] = Stats("Vmax", "umol/l/min", self.vmax)
        self.stats['VO2 Km'] = Stats("Km", "mM or other unit", self.km)
        self.signals.sigUpdate.emit()

    def update(self):
        self.get_data()
        self.fit()


##############################################################
# general characteristics for respiration
class AnalyzerRespirationExtremes(AnalyzerGeneric):

    database_table = "VO2_extremes_raw"
    
    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerRespirationExtremes.database_table) +
                 "(experiment_id text PRIMARY KEY, " +
                 "v0 double precision, vmax double precision, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")
        viewname = AnalyzerRespirationExtremes.database_table + "_extended"
        if not db.has_view(viewname):
            db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                     "experiment_id, v0, vmax, v0/vmax AS flux_control, (vmax-v0)/v0 AS acr FROM " +
                     db.table(AnalyzerRespirationExtremes.database_table))


    def __init__(self, database, data):
        self.database_schema(database)
        AnalyzerGeneric.__init__(self, None, None)

        self.signals = AnalyzerRespirationSignals()
        self.database = database
        self.table_name = AnalyzerRespirationExtremes.database_table
        self.table_source = AnalyzerRespiration.database_conc_view
        self.experiment_id = data.experiment_id

        self.analyze()

    def analyze(self):
        c = self.database
        vbg = None
        for row in c.query("SELECT rate FROM " + self.database.table(self.table_source) +
                           " WHERE experiment_id=:experiment_id AND event_name=:event",
                           experiment_id=self.experiment_id, event="VBG"):
            vbg = row.rate

        v0 = None
        for row in c.query("SELECT rate FROM " + self.database.table(self.table_source) +
                             " WHERE experiment_id=:experiment_id AND event_name=:event",
                             experiment_id=self.experiment_id, event="V0"):
            v0 = row.rate

        vmax = None
        for row in c.query("SELECT MAX(rate) AS rate FROM " + self.database.table(self.table_source) +
                             " WHERE experiment_id=:experiment_id",
                             experiment_id=self.experiment_id):
            vmax = row.rate

        if vbg is None or v0 is None or vmax is None:
            return # something is missing

        v0 -= vbg
        vmax -= vbg

        if self.database.has_record(self.table_name, experiment_id=self.experiment_id):
            c.query("UPDATE " + self.database.table(self.table_name) +
                      " SET v0=:v0, vmax=:vmax WHERE experiment_id=:experiment_id",
                      v0=v0, vmax=vmax, experiment_id=self.experiment_id)
        else:
            c.query("INSERT INTO "+ self.database.table(self.table_name) +
                      "(experiment_id, v0, vmax) VALUES(:experiment_id,:v0,:vmax)",
                      experiment_id=self.experiment_id, v0=v0, vmax=vmax)

        self.stats["VBG"] = Stats("Vbg (background rate)", "umol/l/min", vbg)
        self.stats["V0"] = Stats("V0 (after subtracting Vbg)", "umol/l/min", v0)
        self.stats["Vmax"] = Stats("V maximal recorded (after subtracting Vbg)", "umol/l/min", vmax)
        self.stats["ACR"] = Stats("ACR: (Vmax-V0)/V0", "", (vmax-v0)/v0)
        self.stats["FCR"] = Stats("Flux control ratio: V0/Vmax", "", v0/vmax)

        self.signals.sigUpdate.emit()

    def update(self):
        self.analyze()

##############################################################
# PK ratios
class AnalyzerRespirationRatiosPK(AnalyzerGeneric):

    database_table = "VO2_MerviPK_ratios_raw"
    
    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerRespirationRatiosPK.database_table) +
                  "(experiment_id text PRIMARY KEY, " +
                  "v0 double precision, vatp double precision, vpep double precision, vpk double precision, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                  ")")
        viewname = AnalyzerRespirationRatiosPK.database_table + "_extended"
        if not db.has_view(viewname):
            db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                  "experiment_id, v0, vatp, (vpep-v0)/(vatp-v0) AS vpep_remaining, " +
                  "(vpk-v0)/(vatp-v0) AS vpk_remaining FROM " +
                  db.table(AnalyzerRespirationRatiosPK.database_table))


    def __init__(self, database, data):
        self.database_schema(database)
        AnalyzerGeneric.__init__(self, None, None)

        self.signals = AnalyzerRespirationSignals()
        self.database = database
        self.table_name = AnalyzerRespirationRatiosPK.database_table
        self.table_source = AnalyzerRespiration.database_conc_view
        self.experiment_id = data.experiment_id

        self.analyze()

    def getvalue(self, event):
        v = None
        c = self.database
        for row in c.query("SELECT rate FROM " + self.database.table(self.table_source) +
                             " WHERE experiment_id=:experiment_id AND event_name=:event",
                             experiment_id=self.experiment_id,event=event):
            v = row.rate
        return v

    def analyze(self):
        vbg = self.getvalue("VBG")
        v0 = self.getvalue("V0")
        vatp = self.getvalue("2mM ATP")
        vpep = self.getvalue("5mM PEP")
        vpk = self.getvalue("20U PK")

        if None in [vbg, v0, vatp, vpep, vpk]:
            return # something is missing

        v0 -= vbg
        vatp -= vbg
        vpep -= vbg
        vpk -= vbg

        c = self.database
        if self.database.has_record(self.table_name, experiment_id=self.experiment_id):
            c.query("UPDATE " + self.database.table(self.table_name) +
                      " SET v0=:v0, vatp=:vatp, vpep=:vpep, vpk=:vpk WHERE experiment_id=:experiment_id",
                      v0=v0, vatp=vatp, vpep=vpep, vpk=vpk, experiment_id=self.experiment_id)
        else:
            c.query("INSERT INTO "+ self.database.table(self.table_name) +
                      "(experiment_id, v0, vatp, vpep, vpk) VALUES(:experiment_id,:v0,:vatp,:vpep,:vpk)",
                      experiment_id=self.experiment_id, v0=v0, vatp=vatp, vpep=vpep, vpk=vpk)

        self.stats["VPEP"] = Stats("(VPEP-V0)/(VATP-V0)", "%", (vpep-v0)/(vatp-v0)*100)
        self.stats["VPK"] = Stats("(VPK-V0)/(VATP-V0)", "%", (vpk-v0)/(vatp-v0)*100)

        self.signals.sigUpdate.emit()

    def update(self):
        self.analyze()


#############################################################################################
class AnalyzerRespirationMMADP(AnalyzerRespirationMM):
    def __init__(self, database, data):
        AnalyzerRespirationMM.__init__(self, database,
                                       data)
        self.axisnames = XYData("ADP", "VO2")
        self.axisunits = XYData("mM or possibly other", "umol/l/min")

class AnalyzerRespirationMMATP(AnalyzerRespirationMM):
    def __init__(self, database, data):
        AnalyzerRespirationMM.__init__(self, database,
                                       data)
        self.axisnames = XYData("ATP", "VO2")
        self.axisunits = XYData("mM or possibly other", "umol/l/min")

#####################
#### ModuleAPI ######

def analyzer(database, data):    
    if data.type.find("Strathkelvin ADP titration") == 0:
        p = AnalyzerRespirationMMADP(database, data)
        return None, \
            { 'sysbio respiration': p }, \
            [ AnalyzerRespirationExtremes(database, data), p ]
    elif data.type == "Strathkelvin ATP titration":
        p = AnalyzerRespirationMMATP(database, data)
        return None, \
            { 'sysbio respiration': p }, \
            [ AnalyzerRespirationExtremes(database, data), p ]
    elif data.type == "Strathkelvin merviPK":
        return None, None, [ AnalyzerRespirationExtremes(database, data),
                             AnalyzerRespirationRatiosPK(database, data) ]
    return None, None, None

def database_schema(db):
    AnalyzerRespirationMM.database_schema(db)
    AnalyzerRespirationExtremes.database_schema(db)
    AnalyzerRespirationRatiosPK.database_schema(db)
