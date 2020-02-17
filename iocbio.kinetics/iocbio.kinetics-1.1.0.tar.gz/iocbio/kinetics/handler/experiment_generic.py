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
from ..constants import database_table_experiment


class ExperimentGeneric(object):
    """Handler for experiment records

    This handler provides a collection of methods used by all
    experiments. This class is responsible for creating general
    experiments database table and provides facilities to query it as
    well as make new experiment record.

    Database table name is defined by
    :class:`..constants.database_table_experiment` and has the
    following columns:

    - experiment_id: text, primary key
    - date: text
    - time: text
    - type_generic: text
    - type_specific: text
    - hardware: text

    Parameters
    ----------
    db : iocbio.kinetics.io.db.DatabaseInterface
      Database access

    Attributes
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access

    """

    database_table = database_table_experiment

    @staticmethod
    def database_schema(db):
        """Create experiments database table if it is missing"""
        
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentGeneric.database_table) +
                 "(experiment_id text not null, date text not null, time text, type_generic text not null, type_specific text not null, hardware text not null " +
                 ", primary key(experiment_id))")

    @staticmethod
    def has_record(database, experiment_id):
        """Check if experiment has a record

        Checks whether experiment with experiment_id has been recorded in the
        database already
        """
        try:
            res = database.has_record(ExperimentGeneric.database_table, experiment_id=experiment_id)
        except:
            res = False
        return res

    @staticmethod
    def hardware(database, experiment_id):
        """Hardware used for the experiment

        Returns hardware column value for experiment with the
        experiment_id. It is assumed that the experiment is recorded
        in the database.

        """
        return database.query("select hardware from " + database.table("experiment") +
                              " where experiment_id=:experiment_id",
                              experiment_id=experiment_id).first().hardware

    @staticmethod
    def store(database, experiment_id, time, type_generic, type_specific, hardware):
        """Store new experimental record

        Stores a new experiment record if it does not exist in the
        database. If there is a record already in the database with
        the same experiment_id, this method will return without
        altering the database.

        Parameters
        ----------
        database : iocbio.kinetics.io.db.DatabaseInterface
          Database access
        experiment_id : str
          Experiment ID
        time : datetime
          Date and time of the experiment
        type_generic : str
          Generic type of the experiment
        type_specific : str
          Specific type of the experiment
        hardware : str
          String defining the hardware
        """
        
        if ExperimentGeneric.has_record(database, experiment_id):
            return

        date = time.split()[0]
        t = time.split()[1]
        database.query("INSERT INTO " + database.table(ExperimentGeneric.database_table) +
                            "(experiment_id, date, time, type_generic, type_specific, hardware) " +
                            "VALUES(:experiment_id, :date, :time, :typeg, :types, :hardware)",
                            experiment_id=experiment_id, date=date, time=t,
                            typeg=type_generic, types=type_specific, hardware=hardware)


    def __init__(self, db):
        self.database = db
