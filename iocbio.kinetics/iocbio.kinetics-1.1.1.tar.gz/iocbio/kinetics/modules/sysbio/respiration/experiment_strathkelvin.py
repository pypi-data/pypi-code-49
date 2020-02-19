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
from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric
from iocbio.kinetics.constants import database_table_experiment
from .analyzer_primary import AnalyzerRespiration, AnalyzerRespirationTMPD, AnalyzerRespirationTMPDCorrected

### Module flag
IocbioKineticsModule = ['analyzer', 'database_schema', 'database_info']

### Implementation

class ExperimentStrathkelvin(ExperimentGeneric):
    """General description of experiment performed on Strathkelvin"""

    database_table = "strathkelvin"
    database_config_table = "VO2_config"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentStrathkelvin.database_table) +
                 "(experiment_id text PRIMARY KEY, rawdata text, filename text, title text, channel integer, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentStrathkelvin.database_config_table) +
                 "(experiment_id text not null, cells_in_mkL double precision, chamber_volume_in_ml double precision, " +
                 "temperature double precision"
                 ", primary key(experiment_id), " +
                "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")

    @staticmethod
    def getvalue(data, key, protocol=True):
        k = key
        if k not in data.config:
            if protocol:
                k = data.config["protocol"] + "." + key
                if k not in data.config:
                    for s in data.config:
                        if s.startswith(data.config["protocol"]) and s.endswith(" " + key):
                            k = s

                if k not in data.config:
                    return None

        v = data.config[k]
        try:
            vf = float(v)
            return vf
        except:
            pass
        return v

    @staticmethod
    def getcells(data):
        cells = ExperimentStrathkelvin.getvalue(data, "cells")
        if cells is None: return cells
        if cells[-3:] != "mkL":
            print("Unexpected unit for cells: %s" % cells)
            this_is_an_ugly_crash
        cells = float(cells[:-3])
        return cells

    @staticmethod
    def store(database, data):
        ExperimentGeneric.database_schema(database)
        ExperimentStrathkelvin.database_schema(database)

        experiment_id = data.experiment_id

        ExperimentGeneric.store(database, experiment_id, time=data.time,
                                type_generic=data.type_generic,
                                type_specific=data.type, hardware="strathkelvin")

        c = database
        if not database.has_record(ExperimentStrathkelvin.database_table,
                                   experiment_id = experiment_id):
           c.query("INSERT INTO " + database.table(ExperimentStrathkelvin.database_table) +
                   "(experiment_id, rawdata, filename, title, channel) " +
                   "VALUES(:experiment_id,:ftxt,:fname,:exptitle,:channel)",
                   experiment_id=experiment_id,
                   ftxt=data.fulltext,
                   fname=data.config["this file"],
                   exptitle=data.config["experiment title"],
                   channel=int(data.config["channel index"]))


    @staticmethod
    def get_fulltxt(database, experiment_id):
        if ExperimentGeneric.hardware(database, experiment_id) != 'strathkelvin':
            return None
        print('Loading raw data for experiment:', experiment_id)
        for q in database.query("SELECT rawdata FROM " + database.table(ExperimentStrathkelvin.database_table) +
                                " WHERE experiment_id=:experiment_id",
                                experiment_id=experiment_id):
            return q.rawdata
        return None

    def __init__(self, database, data):
        ExperimentGeneric.__init__(self,database)
        ExperimentStrathkelvin.database_schema(database)

        experiment_id = data.experiment_id
        self.name = data.config["this file"]

        cells = ExperimentStrathkelvin.getcells(data)
        volume_ml = ExperimentStrathkelvin.getvalue(data, "volume_ml")
        temperature = ExperimentStrathkelvin.getvalue(data, "temperature")

        if not database.has_record(ExperimentStrathkelvin.database_config_table, experiment_id=experiment_id):
            database.query("INSERT INTO " + database.table(ExperimentStrathkelvin.database_config_table) +
                    "(experiment_id, cells_in_mkL, chamber_volume_in_ml, temperature) " +
                    "VALUES (:experiment_id,:cells,:volume,:temperature)",
                    experiment_id=experiment_id, cells=cells,
                    volume=volume_ml, temperature=temperature)
        else:
            database.query("UPDATE " + database.table(ExperimentStrathkelvin.database_config_table) +
                    " SET cells_in_mkL=:cells, chamber_volume_in_ml=:volume, temperature=:temperature WHERE experiment_id=:experiment_id",
                    experiment_id=experiment_id, cells=cells,
                    volume=volume_ml, temperature=temperature)


#############################################################################################
# allocation of experiment handler and analyzers for strathkelvin experiments

def generate_titration_types():
    titration_types = {'Strathkelvin merviPK': 'MerviPK'}
    for i in ['GMPS', 'SGMP', 'ATP_glucose_PEP_PK', 'ATP_AMP_PEP_PK', 'creatine_ATP_PEP_PK',
              'ATP_glucose_ADP', 'ATP_AMP_ADP', 'creatine_ATP_ADP']:
        titration_types['Strathkelvin ' + i] = i
    return titration_types

def allocate_handler_analyzer(database, data):
    titration_types = generate_titration_types()

    # if something is changed here, check whether database_schema are generated below as well
    if data.type in titration_types:
        Analyzer = { 'default': AnalyzerRespiration }
        experiment_handler = ExperimentStrathkelvin(database, data)
    elif data.type.find("Strathkelvin ADP titration") == 0:
        Analyzer = { 'default': AnalyzerRespiration }
        experiment_handler = ExperimentStrathkelvin(database, data)
    elif data.type.find("Strathkelvin Respiratory complexes") == 0:
        Analyzer = {
            'default': AnalyzerRespiration,
            'TMPD oxydation': AnalyzerRespirationTMPD,
            'TMPD corrected': AnalyzerRespirationTMPDCorrected,
        }
        experiment_handler = ExperimentStrathkelvin(database, data)
    elif data.type == "Strathkelvin ATP titration":
        Analyzer = { 'default': AnalyzerRespiration }
        experiment_handler = ExperimentStrathkelvin(database, data)
    else:
        return None, None
    return Analyzer, experiment_handler


#####################
#### ModuleAPI ######

def database_info(database):
    return "SELECT 'channel-' || CAST(channel AS TEXT) from %s s where s.experiment_id=e.experiment_id" % database.table("strathkelvin")

def database_schema(db):
    ExperimentStrathkelvin.database_schema(db)

def analyzer(database, data):
    A, _ = allocate_handler_analyzer(database, data)
    return A, None, None
