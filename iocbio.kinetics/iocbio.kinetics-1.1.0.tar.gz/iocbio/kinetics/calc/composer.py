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

"""Composer for analyzers"""

from .generic import AnalyzerGeneric
from .generic import Stats

from collections import OrderedDict
from PyQt5.QtCore import pyqtSignal, QObject


class AnalyzerComposeSignals(QObject):
    sigUpdate = pyqtSignal()


class AnalyzerCompose(AnalyzerGeneric):
    """Generic analyzer consisting of sub-analyzers

    In some cases, such as primary analyzer, only a single analyzer is
    expected by the routines. Use AnalyzerCompose if you need to
    combine several analyzers in this case. This analyzer can be used
    as a base class for a primary analyzer that consists of several
    sub-analyzers.

    Attributes
    ----------
    analyzers : collections.OrderedDict
      Dictionary with the analyzers. Key is used in GUI to show corresponding plots
    """

    def __init__(self):
        AnalyzerGeneric.__init__(self, None, None)
        self.analyzers = OrderedDict()
        self.signals = AnalyzerComposeSignals()

    def add_analyzer(self, key, analyzer):
        """Add new analyzer to the composed one

        As a key, use a name that will be associated by the user with the
        corresponding analyzer when examining the fits.

        The analyzer objects added to this analyzer should already be
        constructed with the connection to the database and follow
        specific data ROI. As a result, AnalyzerCompose doesn't need
        to know anything about the database nor the data, just to
        forward the analysis-related tasks to sub-analyzers.

        Parameters
        ----------
        key : str
          Key identifying the analyzer
        analyzer : derived from AnalyzerGeneric
          Analyzer object

        """        
        self.analyzers[key] = analyzer
        self.analyzers[key].signals.sigUpdate.connect(self._update_stats)
        self.analyzers[key].signals.sigUpdate.connect(self.signals.sigUpdate)
        self._update_stats()

    def list_analyzers(self):
        """List with the keys of the analyzers"""
        return list(self.analyzers.keys())

    def fit(self):
        """Perform the fit by all analyzers"""
        for key, a in self.analyzers.items():
            a.fit()

    def remove(self):
        """Remove current ROI data"""
        for key, a in self.analyzers.items():
            a.remove()

    def update(self):
        """Update data if used as a secondary analyzers"""
        for key, a in self.analyzers.items():
            a.update()

    def update_data(self, data):
        """Update current ROI data if used as a primary analyzer"""
        for key, a in self.analyzers.items():
            a.update_data(data)

    def update_event(self, event_name):
        """Update current ROI event"""
        for key, a in self.analyzers.items():
            a.update_event(event_name)

    def _update_stats(self):
        self.stats = {}
        for key, a in self.analyzers.items():
            for sk, sv in a.stats.items():
                self.stats[key + ": " + sk] = Stats(key + ": " + sv.human, sv.unit, sv.value)
