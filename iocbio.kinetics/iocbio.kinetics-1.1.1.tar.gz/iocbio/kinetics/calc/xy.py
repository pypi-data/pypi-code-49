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
# Generic analyzer used to show summarizing XY plots

from PyQt5.QtCore import pyqtSignal, QObject
from .generic import Stats, XYData, AnalyzerGeneric


class AnalyzerXYSignals(QObject):
    """Internal class for signaling updates"""
    sigUpdate = pyqtSignal()


class AnalyzerXY(AnalyzerGeneric):
    """Class for filling experimental data from the database

    This class can be used for fetching the data from the database and
    filling it as experiment property for further fitting by the
    derived analyzer. It is commonly used in the secondary analysis
    where the results of the primary analysis are fit.

    For fetching the data, it all has to come from the same table or
    view. The table (view) should have a column `experiment_id` that
    will be used to restrict fetched data to the analyzed
    experiment. While value can be represented by any column, the
    argument (x-axis) is fetched from column `event_value`. This
    allows AnalyzerXY to contruct SQL SELECT statement to fetch it.

    Parameters
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access
    table_name : str
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
    value_name : str
      Name of the column containing experimental values
    experiment_id : str
      Experiment ID
    axisnames : iocbio.kinetics.calc.generic.XYData
      Names of the axes
    axisunits : iocbio.kinetics.calc.generic.XYData
      Units of the axes

    """

    def __init__(self, database, table_name, value_name, data, axisnames, axisunits):
        AnalyzerGeneric.__init__(self, [], []) # start with empty data

        self.signals = AnalyzerXYSignals()
        self.database = database
        self.table_name = table_name
        self.value_name = value_name
        self.experiment_id = data.experiment_id
        self.axisnames = axisnames
        self.axisunits = axisunits

        self.get_data()

    def get_data(self):
        """Fetch the data from the database"""
        c = self.database
        v0 = 0
        x = []
        y = []
        for row in c.query("SELECT " + self.value_name + " AS value, event_value FROM " +
                           self.database.table(self.table_name) +
                           " WHERE experiment_id=:experiment_id AND event_value IS NOT NULL ORDER BY event_value ASC",
                           experiment_id = self.experiment_id):
            x.append(row.event_value)
            y.append(row.value)
        self.experiment = XYData(x, y)
        self.signals.sigUpdate.emit()

    def update(self):
        """Update the data

        In the derived classes, call these method when update is requested
        """
        self.get_data()
