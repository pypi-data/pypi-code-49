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

"""Specific analyzers used to analyze currents through cell membrane"""

import numpy as np
from scipy.integrate import trapz
from scipy.optimize import leastsq
from scipy.special import lambertw

from .generic import AnalyzerGeneric, XYData, Stats
from .xy import AnalyzerXY
from ..constants import database_table_experiment


class AnalyzerCurrent(AnalyzerGeneric):
    """Current analyzer"""

    def __init__(self, x, y, baseline_subtraction=True):
        AnalyzerGeneric.__init__(self, x, y)
        self.baseline_subtraction = baseline_subtraction

    def fit(self, n=7):
        if self.experiment.y.size < n:
            return
        if n > 2:
            x = self.experiment.x
            y = self.experiment.y
            k = np.blackman(n)
            k /= k.sum()
            #c = self.experiment.y#
            c = np.convolve(k, self.experiment.y, mode='same')
        else:
            c = self.experiment.y.copy()

        if self.baseline_subtraction:
            current_baseline = self.experiment.y[-20:].mean()
        else:
            current_baseline = 0.0
        current_peak = c.min() - current_baseline
        ind_to_peak = np.argmin(c)
        arg_to_peak = self.experiment.x[ind_to_peak]

        y_int = y - current_baseline
        #charge_carried = trapz(pulse[a:b] - pulse[b-20:b].mean(), dx=self.Dt)
        charge_carried = trapz(y_int[y_int<0], x[y_int<0])
        charge_carried = trapz(y_int, x)

        self.stats['current baseline'] = Stats('current baseline', 'pA', current_baseline)
        self.stats['current peak'] = Stats('current peak', 'pA', current_peak)
        self.stats['arg to peak'] = Stats('arg to peak', 's', arg_to_peak)
        self.stats['charge carried'] = Stats('charge carried', 'pC', charge_carried)

        #self.calc = XYData([arg_to_peak, arg_to_peak], [0.95*current_peak, 1.05*current_peak])
        # self.calc = XYData(self.experiment.x[ind_to_peak-20:ind_to_peak+20],
        #                    c[ind_to_peak-20:ind_to_peak+20])

        #self.calc = XYData(x[y_int<0], y_int[y_int<0])
        self.calc = XYData(x, y_int)


class AnalyzerCurrentIV(AnalyzerXY):
    """I-V curve analyzer"""

    database_table = "electrophysiology_current_iv_fit"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerCurrentIV.database_table) +
                 "(experiment_id text PRIMARY KEY, " +
                 "gmax double precision, " +
                 "vrev double precision, " +
                 "vhalfi double precision, " +
                 "kg double precision, " +
                 "v_current_max double precision, " +
                 "max_current double precision, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")

    @staticmethod
    def iv_func(V, Gmax, Vrev, Vhalf, kG):
        # The cardiac L-type calcium channel distal carboxy terminus autoinhibition is regulated by calcium
        # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3774502/
        # http://jgp.rupress.org/content/128/1/15?ijkey=cf7d206e01efdf758ad1e8be2afbd9e20048376f&keytype2=tf_ipsecsha
        # https://academic.oup.com/cardiovascres/article/38/2/424/299912
        # http://circres.ahajournals.org/content/90/9/933 -- read this
        return Gmax*(V-Vrev)/(1+np.exp((Vhalf-V)/kG))

    @staticmethod
    def iv_error_func(x0, y, y_std, V):
        Gmax, Vrev, Vhalf, kG = x0
        return (y - AnalyzerCurrentIV.iv_func(V, Gmax, Vrev, Vhalf, kG)) / y_std

    def __init__(self, database, table_name, value_name, data, axisnames, axisunits):
        AnalyzerXY.__init__(self, database, table_name, value_name, data, axisnames, axisunits)
        AnalyzerCurrentIV.database_schema(database)
        self.analyze()

    def update(self):
        self.get_data()
        self.analyze()

    def analyze(self):
        x, y = self.experiment.x, self.experiment.y
        if len(x) < 4 or len(y) < 4:
            self.stats['fail'] = Stats('Cannot fit! At least 4 points are needed', '', 0)
            return

        # x0_I = Gmax, Vrev, Vhalf, kG
        x0_I = [5.0, 50., -15., 5.0]
        (gmax, vrev, vhalfi, kg), msg = leastsq(self.iv_error_func, x0_I, args=(y, 1., x))
        v_current_max = -kg * lambertw(np.exp(vrev/kg-vhalfi/kg-1)) + vrev - kg
        v_current_max = v_current_max.real
        max_current = self.iv_func(v_current_max, gmax, vrev, vhalfi, kg)
        # print('Gmax, Vrev, VhalfI, kG, VImax, msg', Gmax, Vrev, VhalfI, kG, V_current_max, msg)

        self.stats['gmax'] = Stats('Maximal conductance', 'pA/mV', gmax)
        self.stats['vrev'] = Stats('Reversal potential', 'mV', vrev)
        self.stats['vhalfi'] = Stats('Activation midpoint potential', 'mV', vhalfi)
        self.stats['kg'] = Stats('Slope factor', '', kg)
        self.stats['v_current_max'] = Stats('Potential at maximal current ', 'mV', v_current_max)
        self.stats['max_current'] = Stats('Maximal current', 'pA', max_current)

        # experiment_id is inherited from AnalyzerXY
        c = self.database
        if self.database.has_record(self.database_table, experiment_id=self.experiment_id):
            c.query("UPDATE " + c.table(self.database_table) +
                    " SET gmax=:gmax, vrev=:vrev, vhalfi=:vhalfi, kg=:kg, v_current_max=:v_current_max, max_current=:max_current" +
                    " WHERE experiment_id=:experiment_id",
                    gmax=gmax, vrev=vrev, vhalfi=vhalfi, kg=kg, v_current_max=v_current_max, max_current=max_current,
                    experiment_id=self.experiment_id)
        else:
            c.query("INSERT INTO " + c.table(self.database_table) +
                    " (experiment_id, gmax, vrev, vhalfi, kg, v_current_max, max_current)" +
                    " VALUES(:experiment_id, :gmax, :vrev, :vhalfi, :kg, :v_current_max, :max_current)",
                    experiment_id=self.experiment_id,
                    gmax=gmax, vrev=vrev, vhalfi=vhalfi, kg=kg, v_current_max=v_current_max, max_current=max_current)

        dt = 1.0
        v = np.arange(x[0], x[-1]+dt, dt)
        self.calc = XYData(v, self.iv_func(v, gmax, vrev, vhalfi, kg))
        self.signals.sigUpdate.emit()


# class 
