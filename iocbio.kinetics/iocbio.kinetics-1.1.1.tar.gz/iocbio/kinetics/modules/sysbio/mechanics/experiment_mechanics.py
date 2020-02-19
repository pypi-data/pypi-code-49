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

class ExperimentMechanics(ExperimentGeneric):
    """General description of experiment performed on SBMicroscope Mechanics"""

    database_table = "mechanics"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentMechanics.database_table) +
                 "(experiment_id text PRIMARY KEY, filename text, mode text, title text, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")

    @staticmethod
    def store(database, data):
        ExperimentGeneric.database_schema(database)
        ExperimentMechanics.database_schema(database)

        experiment_id = data.experiment_id

        ExperimentGeneric.store(database, experiment_id, time=data.time,
                                type_generic=data.type_generic,
                                type_specific=data.type, hardware="mechanics")

        c = database
        if not database.has_record(ExperimentMechanics.database_table,
                                   experiment_id = experiment_id):
            
           c.query("INSERT INTO " + database.table(ExperimentMechanics.database_table) +
                   "(experiment_id, filename, mode, title) " +
                   "VALUES(:experiment_id,:fname,:mode,:exptitle)",
                   experiment_id=experiment_id,
                   fname=data.config['filename'],
                   mode=data.config['mode'],
                   exptitle=data.name)

    @staticmethod
    def get_fname_mode(database, experiment_id):
        hw = ExperimentGeneric.hardware(database, experiment_id)
        if hw != 'mechanics':
            return None, None
        r = database.query("SELECT filename, mode FROM " + database.table(ExperimentMechanics.database_table) +
                           " WHERE experiment_id=:experiment_id",
                           experiment_id=experiment_id).first()
        return r.filename, r.mode

    def __init__(self, database, data):
        ExperimentMechanics.database_schema(database)
        ExperimentGeneric.__init__(self, database)
        experiment_id = data.experiment_id
        self.name = data.name


def database_info(database):
    return "SELECT title from %s s where s.experiment_id=e.experiment_id" % database.table("mechanics")

def database_schema(db):
    ExperimentMechanics.database_schema(db)

