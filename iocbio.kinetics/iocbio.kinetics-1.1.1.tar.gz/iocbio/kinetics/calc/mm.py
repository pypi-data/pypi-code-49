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
import scipy.optimize
import numpy as np
from PyQt5.QtCore import pyqtSignal, QObject

from .generic import AnalyzerGeneric, XYData, Stats
from iocbio.kinetics.constants import database_table_roi, database_table_experiment


class AnalyzerMM:
    """Analyzer for fitting experimental data with Michaelis-Menten equation

    This analyzer provides `fit` method that fits the experimental
    data in `self.experiment` by Michaelis-Menten equation. Results
    are stored in attributes `km` and `vmax` as well as best fit
    calculation in `calc`.

    Parameters
    ----------
    x : numpy.array
      experimental data, x-axis
    y : numpy.array
      experimental data, y-axis (values)

    Attributes
    ----------
    vmax : float
      Vmax
    km : float
      Km
    calc : iocbio.kinetics.calc.generic.XYData
      calculated best fit solution
    """

    @staticmethod
    def mm(x, km, vmax):
        """Static method for calculation of Michaelis-Menten function at given x"""
        return vmax*x/(km + x)

    def __init__(self, x, y):
        AnalyzerGeneric.__init__(self, x, y)
        self.vmax, self.km = None, None

    def fit(self):
        """Fit the data

        Fits the data stored in `self.experiment` and fills the object
        attributes vmax, km, and calc. Call this data on
        initialization of the derived analyzer and when the data are
        updated.

        """
        if self.experiment.x.size < 2:
            self.vmax, self.km = None, None
            self.calc = XYData(None, None)
            return # not enough data

        x = [1,1]
        r = scipy.optimize.leastsq( self.error, x )
        self.vmax, self.km = r[0][0], abs(r[0][1])
        xmx = self.experiment.x.max()
        stps = 100
        xx = np.arange(0, xmx + 2*xmx/stps, xmx/stps)
        self.calc = XYData(xx, AnalyzerMM.mm(xx, self.km, self.vmax))

    def error(self, x):
        """Residual of the fit"""
        vmax = x[0]
        km = abs(x[1])
        y = self.experiment.y - AnalyzerMM.mm(self.experiment.x, km, vmax)
        return y


##############################################################
# kinetics analysis using Michaelis-Menten relationship
# and taking into account offset induced by V0
class AnalyzerMMDatabaseSignals(QObject):
    sigUpdate = pyqtSignal()

class AnalyzerMMDatabase(AnalyzerMM):
    """Analyzer for fitting experimental data with Michaelis-Menten equation and storing the results in the database

    This analyzer combines fetching the experimental data from the
    database, fitting of the experimental data, and storing the
    results into the database. The derived class has to provide names
    for the axes and the units. On construction, the tables for
    fetching and storing the data have to be given.

    For fetching the data, it all has to come from the same table or
    view. The table (view) should have a column `experiment_id` that
    will be used to restrict fetched data to the analyzed
    experiment. Value column is expected to have name `rate`. The
    argument (x-axis) is fetched from column `event_value` and V0 is
    expected to be marked by "V0" in `event_name` column of the
    table. V0 will be subtracted from all the rates before the fit. If
    there is no V0 found in the data, it is assumed to be zero.

    In practice, if the data fetching requirements are met, this class
    can be used by just deriving it and making a short constructor.

    See also attributes from :class:AnalyzerMM .

    Parameters
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access
    table_name : str
      Name of the table to store the fit results in
    table_source : str
      Name of the table to get the data from
    value_name : str
      Name of the column containing experimental values
    data : iocbio.kinetics.io.data.Data
      Data descriptor, used to obtain `experiment_id`
    axisnames : iocbio.kinetics.calc.generic.XYData
      Names of the axes
    axisunits : iocbio.kinetics.calc.generic.XYData
      Units of the axes

    Attributes
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access
    table_name : str
      Name of the table to get the data from
    table_source : str
      Name of the table containing experimental values in `rate` column
    experiment_id : str
      Experiment ID
    experiment : iocbio.kinetics.calc.generic.XYData
      Experimental data used to fit
    """

    @staticmethod
    def database_schema(db, tablename):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(tablename) +
                 "(experiment_id text PRIMARY KEY, " +
                 "vmax double precision, km double precision, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")


    def __init__(self, database, table_name, table_source, experiment_id):
        AnalyzerMMDatabase.database_schema(database, table_name)
        AnalyzerMM.__init__(self, [], []) # start with empty data

        self.signals = AnalyzerMMDatabaseSignals()
        self.database = database
        self.table_name = table_name
        self.table_source = table_source
        self.experiment_id = experiment_id

        self.get_data()
        self.fit()

    def get_data(self):
        """Fetch the data from the database"""
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
        """Fit and store results in the database"""
        
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
        self.stats['Max'] = Stats("Max", "unit/min", self.vmax)
        self.stats['Km'] = Stats("Km", "mM or other unit", self.km)
        self.signals.sigUpdate.emit()

    def update(self):
        """Update and fit the data"""
        self.get_data()
        self.fit()

