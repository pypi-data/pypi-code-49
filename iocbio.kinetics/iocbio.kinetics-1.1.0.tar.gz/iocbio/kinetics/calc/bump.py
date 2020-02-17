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

"""Analyzers fitting the data with a bump functions"""

import numpy as np
from scipy.interpolate import interp1d, PchipInterpolator
from scipy.optimize import leastsq, brentq
from PyQt5.QtCore import pyqtSignal, QObject

from .generic import AnalyzerGeneric, XYData, Stats
from iocbio.kinetics.constants import database_table_roi


class BumpSpline:
    
    def __init__(self, x, y, xmax, nodes_before=6, nodes_after=6, enforce_monotonic=True):
        """
        """
        self.x = x
        self.y = y
        self.xmax = xmax
        self.nodes_before = nodes_before
        self.nodes_after = nodes_after
        self.enforce_monotonic = enforce_monotonic
        self.spline_ready = False

        self.calcspline()

    def calcspline(self):
        print("Fitting bump: %d + %d nodes; x: %f %f" % (self.nodes_before, self.nodes_after, self.x[0], self.x[-1]))
        try:
            dx0 = (self.xmax-self.x[0]) / self.nodes_before
            dx1 = (self.x[-1]-self.xmax) / self.nodes_after

            self.xx = np.append(np.linspace(self.x[0]-dx0/10, self.xmax, self.nodes_before),
                                np.linspace(self.xmax, self.x[-1]+dx1/10, self.nodes_after)[1:])
            yy = np.ones(self.xx.shape)
            r = leastsq(self.spline_error, yy)
            self.make_spline(r[0])
            self.spline_ready = True
        except:
            print("Spline fitting failed. Exception occured during spline fitting")

    def make_spline(self, yy):
        if self.enforce_monotonic:
            val = yy[0]
            zz = [val]
            for i in range(1,self.nodes_before):
                val += yy[i]**2
                zz.append(val)
            for i in range(self.nodes_before, len(yy)):
                val -= yy[i]**2
                zz.append(val)
            self.spline = PchipInterpolator(self.xx, zz)
        else:
            #self.spline = interp1d(self.xx, yy, kind="cubic")
            self.spline = PchipInterpolator(self.xx, yy)

    def spline_error(self, pars):
        self.make_spline(pars)
        return self.curr_error()

    def curr_error(self):
        return self.y - self.spline(self.x)
        #return self.y[1:-1] - self.spline(self.x[1:-1])
        #return self.y[1:self.xmax] - self.spline(self.x[1:self.xmax])

    def __call__(self, x):
        if self.spline_ready:
            return self.spline(x)
        return None

    def min(self):
        if not self.spline_ready: return None
        return min(self.spline(self.x[0]), self.spline(self.x[-1]))

    def max(self):
        if not self.spline_ready: return None
        return self.spline(self.xmax)

    def _intersect_error(self, x):
        return self.spline(x) - self.intersect_value

    def intersect(self, value):
        """
        Assuming that value is between minima and maxima, finds two argument values
        closest to the maxima at which spline is equal to value
        """
        if not self.spline_ready:
            return None, None

        self.intersect_value = value
        data = self.spline(self.x) - self.intersect_value

        i_raise, i_fall = None, None

        idx_max = (np.abs(self.x-self.xmax)).argmin()

        # raise
        i = idx_max-1
        while i >= 0:
            if data[i+1] > 0 and data[i] <= 0:
                i_raise = self.x[i] + (self.x[i+1]-self.x[i]) / (data[i+1] - data[i]) * (-data[i])
                break
            i -= 1

        # fall
        i = idx_max
        imax = len(data) - 1
        while i < imax:
            if data[i+1] < 0 and data[i] >= 0:
                i_fall = self.x[i] + (self.x[i+1]-self.x[i]) / (data[i] - data[i+1]) * (data[i])
                break
            i += 1

        return i_raise, i_fall

        # self.intersect_value = value
        # try:
        #     a ,b = brentq(self._intersect_error, self.x[0], self.xmax), brentq(self._intersect_error, self.xmax, self.x[-1])
        # except:
        #     print("Exception occured during zero finding")
        #     return None, None
        # return a, b


class AnalyzerBump(AnalyzerGeneric):
    """Analyzer for fitting experimental data with a bump approximation

    This analyzer can be used to fit the data with splines. In
    particular, it is written to fit the data which can be represented
    by a bump function (https://en.wikipedia.org/wiki/Bump_function),
    as for example intracellular calcium concentration transient
    during a heart beat. Note that this analyzer is used by
    :class:AnalyzerBumpDatabase, which is expected to be the main API
    used for that type of data.

    The used spline is PchipInterpolator
    (https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.PchipInterpolator.html),
    with an option to enforce monotonic changes before and after the
    peak. When monotonic fit is performed, the fit is much slower than
    without this requirement.

    See parameters and attributes from the base class: :class:`.generic.AnalyzerGeneric`

    Additional attributes are listed below.

    Attributes
    ----------
    spline : BumpSpline
      Used for calculations during a fit

    """

    def __init__(self, x, y):
        AnalyzerGeneric.__init__(self, x, y)

    def fit(self, n, nodes_before=6, nodes_after=6, points_per_node=None, max_nodes=100):
        """Fit the experimental data

        First, the data are convolved with the Blackman kernel. The
        convolved signal is used to find the maximum and corresponding
        argument value. Next, the number of nodes used in the spline
        is found if `points_per_node` is given (not None) as a minimum
        of `max_nodes` and number of experimental points divided by
        `points_per_node` (at least one node is minimal). Data are fit
        then with :class:`.BumpSpline` and the best fit parameters are
        used to calculate approximation and store it in `self.calc`.
        
        Parameters
        ----------
        n : int
          Number of points used to calculate `numpy.blackman` convolution kernel
        nodes_before, nodes_after : int
          Number of spline nodes before and after the peak
        points_per_node : int
          If specified, nodes_before and nodes_after are ignored and number of nodes before
          and after the peak are calculated by dividing number of experimental
          points in the corresponding parts by this factor
        max_nodes : int
          Maximal number of nodes used by the spline. Used to limit number of nodes
          if points_per_node is specified
        """
        self.stats = {}

        k = np.blackman(n)
        c = np.convolve(k, self.experiment.y, mode='same')
        if len(c) != len(self.experiment.x) or len(self.experiment.x) < 3:
            print("Seems that some data are missing, skipping analysis")
            return

        xloc = np.argmax(c)
        self.stats['arg to peak'] = Stats('arg to peak', '', self.experiment.x[ xloc ])

        if points_per_node is not None:
            nodes_before = min(max_nodes, max(1, int(xloc/points_per_node)))+1
            nodes_after = min(max_nodes, max(1, int((self.experiment.x.shape[0]-xloc)/points_per_node)))

        self.spline = BumpSpline(self.experiment.x, self.experiment.y,
                                 self.experiment.x[ np.argmax(c) ],
                                 nodes_before=nodes_before, nodes_after=nodes_after)

        if self.spline.spline_ready:
            self.calc = XYData(self.experiment.x, self.spline(self.experiment.x))
        else:
            self.calc = XYData(None, None)


class AnalyzerBumpDatabaseSignals(QObject):
    sigUpdate = pyqtSignal()


class AnalyzerBumpDatabase(AnalyzerBump):
    """Analyzer for fitting experimental data with a bump approximation

    This analyzer can be used to fit the data with splines. In
    particular, it is written to fit the data which can be represented
    by a bump function (https://en.wikipedia.org/wiki/Bump_function),
    as for example intracellular calcium concentration transient
    during a heart beat. This analyzer can be used either for temporal
    increase (bump) or decrease (hole) approximation.

    The analyzer will fit the data and calculate some parameters
    describing the fit. All calculated parameters will be stored into
    the database, in the table given by name in the constructor. If
    the table is missing, it will be created either by the constructor
    or can be created using `database_schema` statical method. Later
    approach is needed if you use the results of this analyzer by some
    other analyzers.

    The parameters describing the fit are (assuming that argument is
    "time", replaced by the actual argument in the table): time to
    peak, time between peak and the time moment at which the function
    was at X% of its amplitude (before and after the peak). The values
    of X are 5, 10, 25, 37, 50, and 75\%. In addition, maximal,
    minimal, value at start and the end of ROI are recorded, as
    predicted by the fit.

    The used spline is PchipInterpolator
    (https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.PchipInterpolator.html),
    with an option to enforce monotonic changes before and after the
    peak. When monotonic fit is performed, the fit is much slower than
    without this requirement.

    The data is stored in a table with the columns:
    
    - `data_id` reference to `database_table_roi.data_id` (ROI id)
    - `type` (text) with statistics type
    - `value` (float) value of statistics

    In addition, a view is formed with the amplitude of each ROI with the following columns:

    - `experiment_id`
    - `data_id`
    - `event_name`
    - `event_value`
    - `amplitude`

    See attributes from the base class: :class:`.AnalyzerBump`

    Additional attributes are listed below together with the
    parameters.

    Parameters
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access
    tablename : str
      Name of the table to store analysis results to
    data : iocbio.kinetics.io.data.Data
      Data descriptor
    x, y : numpy.array
      Experimental data used to fill `self.experiment`
    peak : bool
      True if increase in values is expected, False if decline is expected
    argname : str
      Name of x-axis
    valunit : str
      Unit of the values

    Attributes
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access
    tablename : str
      Name of the table to store analysis results to
    data : iocbio.kinetics.io.data.Data
      Data descriptor
    data_id : str
      ROI reference
    peak : bool
      True if increase in values is expected, False if decline is expected
    argname : str
      Name of x-axis
    valunit : str
      Unit of the values

    """

    @staticmethod
    def database_schema(db, tablename, peak):
        """Create database table and view

        Checks whether the table and/or view to store the data is
        present and create it if it's not available. The view will
        hold the amplitudes of the fitted signal, with the view name
        formed from `tablename` by adding `_amplitude` to the end of
        the name.

        Parameters
        ----------
        database : iocbio.kinetics.io.db.DatabaseInterface
          Database access
        tablename : str
          Name of the table to store analysis results to
        peak : bool
          True if increase in values is expected, False if decline is expected

        """
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(tablename) +
                 "(data_id text not null, " +
                 "type text not null, value double precision, PRIMARY KEY(data_id, type), " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")

        viewname = tablename + "_amplitude"
        if not db.has_view(viewname):
            if peak:
                db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                        "r.experiment_id, r.data_id, r.event_name, r.event_value, vmax.value-vend.value AS amplitude " +
                        "FROM " + db.table(tablename) + " vmax " +
                        "INNER JOIN " + db.table(tablename) + " vend ON vmax.data_id=vend.data_id " +
                        "INNER JOIN " + db.table("roi") + " r ON vmax.data_id=r.data_id " +
                        "WHERE vmax.type='value max' AND vend.type='value end'")
            else:
                db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                        "r.experiment_id, r.data_id, r.event_name, r.event_value, vend.value-vmin.value AS amplitude " +
                        "FROM " + db.table(tablename) + " vmin " +
                        "INNER JOIN " + db.table(tablename) + " vend ON vmin.data_id=vend.data_id " +
                        "INNER JOIN " + db.table("roi") + " r ON vmin.data_id=r.data_id " +
                        "WHERE vmin.type='value min' AND vend.type='value end'")


    def __init__(self, database, tablename, data, x, y,
                 peak=True, argname="time", valunit="AU"):
        AnalyzerBumpDatabase.database_schema(database, tablename, peak)
        AnalyzerBump.__init__(self, x, y)

        self.signals = AnalyzerBumpDatabaseSignals()
        self.database = database
        self._database_table = tablename
        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.t_reference = None # has to be found in deriving class
        self.peak = peak
        self.argname = argname
        self.valunit = valunit

    def fit(self, n, nodes_before=6, nodes_after=6, points_per_node=None, max_nodes=100):
        """Fit experimental data

        See AnalyzerBump.fit for description of the algorithm and
        parameters. If data are expected to represent "hole" (`peak`
        was False in the constructor), the data are transformed
        temporally to be able to use with the fitting methods.

        After fitting, if it is successful, the results are stored
        into the database table specified during construction of the
        object.

        """
        if len(self.experiment.x) < 1:
            return # nothing to analyze

        if not self.peak:
            self.experiment = XYData(self.experiment.x, -self.experiment.y)

        AnalyzerBump.fit(self, n=n, nodes_before=nodes_before, nodes_after=nodes_after,
                         points_per_node=points_per_node, max_nodes=max_nodes)

        if not bool(self.stats):
            # flip the sign back if needed
            if not self.peak:
                self.experiment = XYData(self.experiment.x, -self.experiment.y)
            return # nothing calculated

        tp = self.stats['arg to peak'].value
        self.stats[self.argname + ' to peak'] = Stats(self.argname + ' to peak', 's',
                                           self.stats['arg to peak'].value - self.t_reference)
        del self.stats['arg to peak']

        if self.calc.y is not None:
            # find time constants
            mx = self.calc.y.max()
            mn = max( self.calc.y[0], self.calc.y[-1] )
            for v in [5, 10, 25, 37, 50, 75]:
                i_raise, i_fall = self.spline.intersect(mn + (mx-mn)*v/100.0)
                if i_raise is not None:
                    self.stats['before %02d' % v] = Stats(self.argname + ' before %02d%%' % v, 's', tp - i_raise)
                if i_fall is not None:
                    self.stats['after %02d' % v] = Stats(self.argname + ' after %02d%%' % v, 's', i_fall - tp)

        # flip the sign back if needed
        if not self.peak:
            self.experiment = XYData(self.experiment.x, -self.experiment.y)
            if self.calc.y is not None:
                self.calc = XYData(self.calc.x,-self.calc.y)

        if self.calc.y is not None:
            # find signal range
            self.stats['value max'] = Stats('Maximal value', self.valunit,
                                            self.calc.y.max())
            self.stats['value min'] = Stats('Minimal value', self.valunit,
                                            self.calc.y.min())
            self.stats['value start'] = Stats('Value at the start', self.valunit, self.calc.y[0])
            self.stats['value end'] = Stats('Value at the end', self.valunit, self.calc.y[-1])
        else:
            # find signal range
            self.stats['value max'] = Stats('Maximal value', self.valunit,
                                            self.experiment.y.max())
            self.stats['value min'] = Stats('Minimal value', self.valunit,
                                            self.experiment.y.min())

        if self.database is not None:
            c = self.database
            for k, v in self.stats.items():
                if self.database.has_record(self._database_table, data_id=self.data_id, type=k):
                    c.query("UPDATE " + self.database.table(self._database_table) +
                              " SET value=:value WHERE data_id=:data_id AND type=:type",
                              value=v.value, data_id=self.data_id, type=k)
                else:
                    c.query("INSERT INTO " + self.database.table(self._database_table) +
                              "(data_id, type, value) VALUES(:data_id,:type,:value)",
                              data_id=self.data_id, type=k, value=v.value)
        self.signals.sigUpdate.emit()

    def remove(self):
        """Remove a record if requested"""
        
        c = self.database
        c.query("DELETE FROM " + self.database.table(self._database_table) +
                " WHERE data_id=:data_id",
                data_id=self.data_id)
        self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()
