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

IocbioKineticsModule = ['database_schema', 'database_info']

class ExperimentElectrophysiology(ExperimentGeneric):
    """General description of experiment performed on SBMicroscope Electrophysiology"""

    database_table = "electrophysiology"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentElectrophysiology.database_table) +
                 "(experiment_id text not null, filename text, mode text, title text, cell integer NOT NULL, tag text, " +
                 "PRIMARY KEY (experiment_id), " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE, " +
                 "FOREIGN KEY (cell) REFERENCES prep_electrophysiology_cardiomyocyte(id))")

    @staticmethod
    def store(database, data):
        ExperimentGeneric.database_schema(database)
        ExperimentElectrophysiology.database_schema(database)

        experiment_id = data.experiment_id

        ExperimentGeneric.store(database, experiment_id, time=data.time,
                                type_generic=data.type_generic,
                                type_specific=data.type, hardware="electrophysiology")

        c = database
        if not database.has_record(ExperimentElectrophysiology.database_table,
                                   experiment_id = experiment_id):
           c.query("INSERT INTO " + database.table(ExperimentElectrophysiology.database_table) +
                   "(experiment_id, filename, mode, title, cell, tag) " +
                   "VALUES(:experiment_id,:fname,:mode,:exptitle,:cell,:tag)",
                   experiment_id=experiment_id,
                   fname=data.config['filename'],
                   mode=data.config['mode'],
                   exptitle=data.name,
                   cell=data.config['cell_id'],
                   tag=data.config['condition'])

    @staticmethod
    def get_fname_mode(database, experiment_id):
        hw = ExperimentGeneric.hardware(database, experiment_id)
        if hw != 'electrophysiology':
            return None, None, None
        for r in database.query("SELECT filename, mode, tag FROM " + database.table(ExperimentElectrophysiology.database_table) +
                                " WHERE experiment_id=:experiment_id",
                                experiment_id=experiment_id):
            return r.filename, r.mode, r.tag
        return None, None, None

    def __init__(self, database, data):
        ExperimentGeneric.__init__(self, database)
        ExperimentElectrophysiology.database_schema(database)
        experiment_id = data.experiment_id
        self.name = data.name

    
def database_info(database):
    return "SELECT title from %s s where s.experiment_id=e.experiment_id" % database.table("electrophysiology")

def database_schema(db):
    ExperimentElectrophysiology.database_schema(db)

