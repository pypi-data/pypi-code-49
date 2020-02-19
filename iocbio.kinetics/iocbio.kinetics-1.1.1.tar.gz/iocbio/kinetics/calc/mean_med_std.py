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

"""Analyzers calculating mean, median, and std"""

import numpy as np
from .generic import AnalyzerGeneric, AnalyzerGenericSignals, XYData, Stats
from ..constants import database_table_roi


class AnalyzerMeanMedStd(AnalyzerGeneric):
    """Analyzer calculating mean, median, and std

    Records results in `self.stat` under keys `mean`, `median`, and `std`.

    See parameters and attributes from the base class: :class:`.generic.AnalyzerGeneric`
    
    """

    def __init__(self, x, y):
        AnalyzerGeneric.__init__(self, x, y)

    def fit(self):
        """Fit the data and update statistics"""
        self.stats['mean'] = Stats("mean", "", np.mean(self.experiment.y))
        self.stats['median'] = Stats("median", "", np.median(self.experiment.y))
        self.stats['std'] = Stats("std", "", np.std(self.experiment.y))
        self.calc = XYData(self.experiment.x,
                           self.experiment.x*0 + self.stats['mean'].value)


class AnalyzerMeanMedStdDB(AnalyzerMeanMedStd):
    """Analyzer calculating mean, median, and std and storing results in the database

    The results of the fit (provided by :class:`.AnalyzerMeanMedStd`)
    are stored in the table specified by the user on construction with
    the following columns: `data_id`, `mean`, `median`, `std`. Here,
    `data_id` is a reference to ROI from the table database_table_roi
    (usually named `roi`).

    All calculated parameters will be stored into the database, in the
    table given by name in the constructor. If the table is missing,
    it will be created either by the constructor or can be created
    using `database_schema` statical method. Later approach is needed
    if you use the results of this analyzer by some other analyzers.

    See parameters and attributes from the base class: :class:`.AnalyzerMeanMedStd`
    
    Parameters
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access
    tablename : str
      Name of the table to store analysis results to
    data : iocbio.kinetics.io.data.Data
      Data descriptor
    channel : str
      Name of the channel to use when accessing the data as in
      self.data.x(channel)

    """
    
    @staticmethod
    def database_schema(db, tablename):
        """Create database table and view

        Checks whether the table to store the data is
        present and create it if it's not available.

        Parameters
        ----------
        db : iocbio.kinetics.io.db.DatabaseInterface
          Database access
        tablename : str
          Name of the table to store analysis results to
        """
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(tablename) +
                 "(data_id text not null PRIMARY KEY, " +
                 "mean double precision not null, median double precision, std double precision, " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE)")

    def __init__(self, database, data, tablename, channel):
        AnalyzerMeanMedStdDB.database_schema(database, tablename)
        AnalyzerMeanMedStd.__init__(self, data.x(channel), data.y(channel).data)

        self.signals = AnalyzerGenericSignals()
        self.database = database
        self._database_table = tablename
        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.channel = channel

    def fit(self):
        """Fit the experimental data and store the results in the database"""
        AnalyzerMeanMedStd.fit(self)
        c = self.database
        if self.database.has_record(self._database_table, data_id=self.data_id):
            c.query("UPDATE " + self.database.table(self._database_table) +
                    " SET mean=:mean, median=:median, std=:std WHERE data_id=:data_id",
                    mean=self.stats['mean'].value,
                    median=self.stats['median'].value,
                    std=self.stats['std'].value,
                    data_id=self.data_id)
        else:
            c.query("INSERT INTO " + self.database.table(self._database_table) +
                    "(data_id, mean, median, std) VALUES(:data_id,:mean,:median,:std)",
                    mean=self.stats['mean'].value,
                    median=self.stats['median'].value,
                    std=self.stats['std'].value,
                    data_id=self.data_id)
        self.signals.sigUpdate.emit()

    def remove(self):
        """Remove data from current ROI from the database"""
        c = self.database
        c.query("DELETE FROM " + self.database.table(self._database_table) +
                " WHERE data_id=:data_id",
                data_id=self.data.data_id)
        self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()

    def update_data(self, data):
        """Updata data from current ROI"""
        AnalyzerMeanMedStd.update_data(self, data.x(self.channel), data.y(self.channel).data)
        self.fit()

    def update_event(self, event_name):
        pass
