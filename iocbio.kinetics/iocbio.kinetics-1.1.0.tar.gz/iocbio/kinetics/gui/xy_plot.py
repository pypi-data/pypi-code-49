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
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabBar
import pyqtgraph as pg
import numpy as np


class XYPlot(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.data = None
        self.analyser_key = None
        self.plot_switch_tabs = None
        self.plot_switch_tabs_list = []

        self.pw = pg.PlotWidget()

        self.calc_plot = pg.PlotCurveItem(pen={'color': '#ff0000', 'width': 2})
        # try ScatterPlotItem PlotDataItem
        self.experiment_plot = pg.PlotDataItem(pen=None,
                                               symbolBrush=(100,100,100),
                                               symbolPen='k', symbolSize=8,
                                               downsampleMethod='subsample',
                                               downsample=25,
                                               autoDownsample=True,
                                               clipToView=True)

        self.pw.setTitle(' ')
        self.pw.addItem(self.experiment_plot)
        self.pw.addItem(self.calc_plot)

        # { Creating layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pw)
        self.setLayout(self.layout)
        # }

    def plot_tab_changed(self, index):
        self.analyser_key = self.plot_switch_tabs_list[index]
        self.update_plot()

    def set_data(self, data):
        if self.data is not None:
            self.data.signals.sigUpdate.disconnect(self.update_plot)

        self.data = data
        if data is None: return

        self.data.signals.sigUpdate.connect(self.update_plot)
        self.update_plot()

    def update_plot(self):
        if self.data.composer:
            if self.data.list_analyzers() != self.plot_switch_tabs_list:
                self.manage_tabs()
            self.plot_switch_tabs.show()
            if self.analyser_key is None:
                self.analyser_key == self.plot_switch_tabs.currentIndex()
            d = self.data.analyzers[self.analyser_key]
        else:
            if self.plot_switch_tabs is not None:
                self.plot_switch_tabs.hide()
            d = self.data

        x_axisnames = d.axisnames.x
        x_axisunits = d.axisunits.x
        y_axisnames = d.axisnames.y
        y_axisunits = d.axisunits.y
        x_experiment = d.experiment.x
        y_experiment = d.experiment.y
        x_calc = d.calc.x
        y_calc = d.calc.y

        self.experiment_plot.setData(x_experiment, y_experiment)
        self.calc_plot.setData(x_calc, y_calc)
        self.pw.setLabel('bottom', x_axisnames, x_axisunits)
        self.pw.setLabel('left', y_axisnames, y_axisunits)

    def manage_tabs(self):
        if self.plot_switch_tabs is not None:
            self.plot_switch_tabs.currentChanged.disconnect()
            self.plot_switch_tabs.deleteLater()

        self.plot_switch_tabs = QTabBar()
        self.plot_switch_tabs.setShape(QTabBar.RoundedSouth)
        self.plot_switch_tabs.setUsesScrollButtons(True)
        self.plot_switch_tabs_list = []
        self.layout.addWidget(self.plot_switch_tabs)

        self.plot_switch_tabs_list = self.data.list_analyzers()

        for tab in self.plot_switch_tabs_list:
            self.plot_switch_tabs.addTab(tab)

        self.analyser_key = self.plot_switch_tabs_list[0]
        self.plot_switch_tabs.currentChanged.connect(self.plot_tab_changed)


class XYPlotWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.data = None

        self.pw = pg.PlotWidget()

        self.calc_plot = pg.PlotCurveItem(pen={'color': '#ff0000', 'width': 2})
        # try ScatterPlotItem PlotDataItem
        self.experiment_plot = pg.PlotDataItem(pen=None,
                                               symbolBrush=(100,100,100),
                                               symbolPen='k', symbolSize=8,
                                               downsampleMethod='subsample',
                                               downsample=25,
                                               autoDownsample=True,
                                               clipToView=True)

        self.pw.setTitle(' ')
        self.pw.addItem(self.experiment_plot)
        self.pw.addItem(self.calc_plot)

        # { Creating layout
        layout = QVBoxLayout()
        layout.addWidget(self.pw)
        self.setLayout(layout)
        # }

    def set_data(self, data):
        if self.data is not None:
            self.data.signals.sigUpdate.disconnect(self.update_plot)

        self.data = data
        if data is None: return

        self.data.signals.sigUpdate.connect(self.update_plot)
        self.update_plot()

    def update_plot(self):
        d = self.data
        if 0:
            self.experiment_plot.setData(d.experiment.x, d.experiment.y)
            self.calc_plot.setData(d.calc.x, d.calc.y)
            self.pw.setLabel('bottom', d.axisnames.x, d.axisunits.x)
            self.pw.setLabel('left', d.axisnames.y, d.axisunits.y)
