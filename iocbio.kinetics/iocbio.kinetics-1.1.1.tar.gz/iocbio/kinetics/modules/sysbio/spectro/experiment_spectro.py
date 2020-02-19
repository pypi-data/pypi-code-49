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

### Module flag
IocbioKineticsModule = ['database_schema', 'database_info']

### Implementation

class ExperimentSpectro(ExperimentGeneric):
    """General description of experiment performed on Spectrophotomer Thermo Evolution 600"""

    database_table = "spectro"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentSpectro.database_table) +
                 "(experiment_id text PRIMARY KEY, rawdata text, filename text, title text, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")

    @staticmethod
    def store(database, data):
        ExperimentGeneric.database_schema(database)
        ExperimentSpectro.database_schema(database)

        experiment_id = data.experiment_id

        ExperimentGeneric.store(database, experiment_id, time=data.time,
                                type_generic=data.type_generic,
                                type_specific=data.type, hardware="spectro")

        c = database
        print(data.config)
        if not database.has_record(ExperimentSpectro.database_table,
                                   experiment_id = experiment_id):
           c.query("INSERT INTO " + database.table(ExperimentSpectro.database_table) +
                   "(experiment_id, rawdata, filename, title) " +
                   "VALUES(:experiment_id,:ftxt,:fname,:exptitle)",
                   experiment_id=experiment_id,
                   ftxt=data.fulltext,
                   exptitle=data.config["experiment title"],
                   fname=data.config["this file"])

    @staticmethod
    def get_fulltxt(database, experiment_id):
        hw = ExperimentGeneric.hardware(database, experiment_id)
        if hw != "spectro": return None
        
        print('Loading raw data for experiment:', experiment_id)
        return database.query("SELECT rawdata FROM " + database.table(ExperimentSpectro.database_table) +
                              " WHERE experiment_id=:experiment_id",
                              experiment_id=experiment_id).first().rawdata

    def __init__(self, database, data):
        ExperimentGeneric.__init__(self,database)
        ExperimentSpectro.database_schema(database)

        experiment_id = data.experiment_id
        self.name = data.config["this file"]


#####################
#### ModuleAPI ######

def database_info(database):
    return "SELECT filename from %s s where s.experiment_id=e.experiment_id" % database.table("spectro")

def database_schema(db):
    ExperimentSpectro.database_schema(db)
