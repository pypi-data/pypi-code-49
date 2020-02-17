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
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

import numpy as np


def float_to_nice_string(f):
    if f is None:
        return "none"
    if np.isneginf(f):
        return '- inf'
    if np.isposinf(f):
        return '+ inf'
    if np.isnan(f):
        return 'nan'
    if np.abs(f) < 1.e-12:
        return str('< 10^-12')
    digits = 5
    # { TODO following is for testing period
    try:
        power = int(np.ceil(np.log10(np.abs(f))))
    except:
        print(type(f), f)
    # }
    round_rule = digits-power
    if round_rule < 1:
        round_rule = 1
    return str(round(f, round_rule))


class StatsView(QWidget):

    def __init__(self):
        QTableWidget.__init__(self)

        self.data = []#None

        # {Creating ui
        self.stats_table = QTableWidget()
        self.stats_table.setSortingEnabled(True)
        layout = QVBoxLayout()
        # layout.addWidget(QLabel('Statistics:'), 0)
        layout.addWidget(self.stats_table)#, 1)
        self.setLayout(layout)
        # }

    def set_data(self, data):
        if not isinstance(data, list):
            if data is not None:
                data = [data]
            else:
                data = []

        if not self.data:
            for d in self.data:
                d.signals.sigUpdate.disconnect(self.update_stats)

        self.data = data
        if not self.data:
            self.stats_table.clear()
            self.stats_table.setRowCount(0)
            self.stats_table.horizontalHeader().setVisible(False)
            return

        for d in self.data:
            d.signals.sigUpdate.connect(self.update_stats)

        self.update_stats()

    def update_stats(self):
        self.stats_table.clear()
        self.stats_table.setColumnCount(3)
        self.stats_table.setRowCount(0)
        self.stats_table.verticalHeader().setVisible(False)
        self.stats_table.horizontalHeader().setVisible(True)
        self.stats_table.setHorizontalHeaderLabels(['parameter', 'value', 'unit'])

        for data_obj in self.data:
            data = data_obj.stats
            
            if data == {}:
                return

            keys = sorted(data.keys())

            for key in keys:
                d = data[key]
                desc, value, unit = d.human, d.value, d.unit

                i = self.stats_table.rowCount()
                self.stats_table.insertRow(i)

                self.stats_table.setItem(i, 0, QTableWidgetItem(desc))
                item = QTableWidgetItem(float_to_nice_string(value))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.stats_table.setItem(i, 1, item)
                self.stats_table.setItem(i, 2, QTableWidgetItem(unit))

            self.stats_table.resizeColumnsToContents()
            self.stats_table.resizeRowsToContents()
