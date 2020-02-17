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
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QSettings, QByteArray
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QSplitter, QLabel, QApplication
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QPushButton, QApplication, QCheckBox, QMenu, QDialog
from PyQt5.QtGui import QPalette, QColor
import pyqtgraph as pg
import numpy as np

from .experiment_plot import ExperimentViewPlot
from .xy_plot import XYPlot
from .stats_widget import StatsView
from .edit_event import EventEdit

from ..handler.roi import ROIHandler
from ..handler.experiment_generic import ExperimentGeneric

from .roi_list import RoiListView

class MainWidget(QWidget):

    settingLowerSplitter = "Main Widget/lower splitter"
    settingMainSplitter = "Main Widget/main splitter"

    def __init__(self, database, data, modules):
        QWidget.__init__(self)

        Analyzer, self.analyzer_overall_plot, analyzer_overall_stats = modules.analyzers(database, data)
        self.rois = ROIHandler(database, data, Analyzer)

        for rtype, analyzer in self.analyzer_overall_plot.items():
            self.rois.sigUpdate.connect(analyzer.update)

        for i in analyzer_overall_stats:
            found = False
            for z,v in self.analyzer_overall_plot.items():
                if i == v:
                    found = True
                    break
            if not found:
                self.rois.sigUpdate.connect(i.update)

        experiment_overview = ExperimentViewPlot(data, list(Analyzer.keys()))
        roi_plot = XYPlot()
        roi_stats = StatsView()
        self.analyzer_overall_xyplot = XYPlot()
        analyzer_overall_stats_view = StatsView()
        analyzer_overall_stats_view.set_data(analyzer_overall_stats)

        copy_exp_id_btn = QPushButton('ID')
        copy_exp_id_btn.clicked.connect(self.copy_exp_id)

        rois_list_widget = RoiListView()
        rois_list_widget.layout().addWidget(copy_exp_id_btn)
        rois_list_widget.set_list(self.rois.sorted_roi_list)

        edit_roi_event = EventEdit()

        roi_edit_stats_layout = QVBoxLayout()
        roi_edit_stats_layout.addWidget(edit_roi_event, 0)
        roi_edit_stats_layout.addWidget(roi_stats, 1)
        roi_edit_stats_widget = QWidget()
        roi_edit_stats_widget.setLayout(roi_edit_stats_layout)

        self.lower_splitter = QSplitter(Qt.Horizontal)
        self.lower_splitter.addWidget(rois_list_widget)
        self.lower_splitter.addWidget(roi_plot)
        self.lower_splitter.addWidget(roi_edit_stats_widget)
        self.lower_splitter.addWidget(self.analyzer_overall_xyplot)
        self.lower_splitter.addWidget(analyzer_overall_stats_view)

        main_layout = QVBoxLayout()

        self.main_splitter = QSplitter(Qt.Vertical)
        self.main_splitter.addWidget(experiment_overview)
        self.main_splitter.addWidget(self.lower_splitter)
        main_layout.addWidget(self.main_splitter)

        # set widget layout
        self.setLayout(main_layout)

        # { Connecting events
        self.rois.sigRois.connect(experiment_overview.update_rois)
        self.rois.sigActiveRoiAnalyser.connect(roi_plot.set_data)
        self.rois.sigActiveRoiAnalyser.connect(roi_stats.set_data)
        self.rois.sigActiveRoiAnalyser.connect(edit_roi_event.set_data)
        self.rois.sigActiveRoiType.connect(self.onActiveRoiType)
        self.rois.sigActiveRoi.connect(rois_list_widget.set_active)
        self.rois.sigRois.connect(lambda rid, rlist: rois_list_widget.set_list(rlist))

        rois_list_widget.sigActiveRoi.connect(self.rois.set_active)
        rois_list_widget.sigActiveRoi.connect(lambda rid: experiment_overview.xview_change_request(self.rois.get_roi_data(rid)))
        rois_list_widget.sigRoiRemove.connect(self.rois.remove)

        experiment_overview.sigAdd.connect(lambda t,x: self.rois.add(roi_type=t, rng=x))
        experiment_overview.sigRemove.connect(self.rois.remove)
        experiment_overview.sigActive.connect(self.rois.set_active)
        experiment_overview.sigRoiRangeChanged.connect(self.rois.update_range)

        edit_roi_event.sigEventNameChanged.connect(self.rois.update_event)
        # }

        # load settings
        settings = QSettings()
        self.lower_splitter.restoreState(settings.value(MainWidget.settingLowerSplitter, QByteArray()))
        self.main_splitter.restoreState(settings.value(MainWidget.settingMainSplitter, QByteArray()))

        if bool(self.analyzer_overall_plot):
            k = list(self.analyzer_overall_plot.keys())[0]
            self.onActiveRoiType(k)
        self.rois.trigger_updates()

    def copy_exp_id(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.rois.experiment_id, mode=cb.Clipboard)

    def save_settings(self):
        settings = QSettings()
        settings.setValue(MainWidget.settingLowerSplitter, self.lower_splitter.saveState())
        settings.setValue(MainWidget.settingMainSplitter, self.main_splitter.saveState())

    def onActiveRoiType(self, roi_type):
        if roi_type in self.analyzer_overall_plot:
            self.analyzer_overall_xyplot.set_data(self.analyzer_overall_plot[roi_type])


class MainGUI(QMainWindow):

    settingGeometry = "Main GUI/geometry"
    settingSplitter = "Main GUI/splitter"
    settingSelector = "Main GUI/selector"

    def __init__(self, database, data, modules, splash = None):
        QMainWindow.__init__(self)

        app = QApplication.instance()
        self.database = database
        self.modules = modules
        self.reopen_database_connection = False
        self.open_file = False

        selectedItem = None
        if data is not None:
            experiment_id = data.experiment_id
        else:
            experiment_id = None

        self.setWindowTitle('IOCBIO Kinetics')

        # { Setting graphics general properites
        pg.setConfigOption('antialias', False)
        pg.setConfigOption('background', self.palette().color(QPalette.Window))
        pg.setConfigOption('foreground', '000000')
        # }

        sql = """
            SELECT experiment_id, date, time, type_generic AS type,
            %s AS info,
            hardware FROM %s e""" % (modules.database_info(database),
                                     database.table("experiment"))

        # get database header
        rows = database.query(sql + " limit 1")
        if rows.first() is not None:
            headers = rows.first().keys()
            headers.remove('experiment_id')
        else:
            headers = ['no data']

        # set the selector widget
        self.selector = QTreeWidget()
        self.selector.setHeaderLabels(headers)

        items = []

        # group by type
        prevtype = None
        p = None
        for e in database.query(sql +
                                " order by type, date,time,info"):
            t = e.type
            if prevtype != t:
                if splash and prevtype is not None:
                    splash.showMessage("Loaded " + prevtype)
                    app.processEvents()
                if p is not None:
                    items.append( p )
                prevtype = t
                p = QTreeWidgetItem([t])
                p.experiment_id = None
            content = []
            for k in headers:
                content.append(e[k])
            item = QTreeWidgetItem(p, content)
            item.experiment_id = e.experiment_id
            p.addChild(item)
        if p is not None:
            items.append( p )

        # group by date
        prevdate = None
        p = None
        for e in database.query(sql +
                                " order by date,type_generic,time,info"):
            d = e.date
            if prevdate != d:
                if splash and prevdate is not None:
                    splash.showMessage("Loaded " + prevdate)
                    app.processEvents()
                if p is not None:
                    items.append( p )
                prevdate = d
                p = QTreeWidgetItem([d])
                p.experiment_id = None
            content = []
            for k in headers:
                content.append(e[k])
            item = QTreeWidgetItem(p, content)
            item.experiment_id = e.experiment_id
            if experiment_id == e.experiment_id:
                selectedItem = item
            p.addChild(item)
        if p is not None: items.append( p )

        self.selector.insertTopLevelItems(0, items)
        for i in items:
            self.selector.setFirstItemColumnSpanned(i, True)

        self.read_only_checkbox = QCheckBox('Read only mode. Note: When read-only, no changes will be saved')
        bg_color = self.palette().color(QPalette.Window).name()
        self.read_only_checkbox.setStyleSheet('QCheckBox:unchecked {color: #f44542; background-color: %s;}' % bg_color)
        self.set_database_read_only(self.database.read_only)

        # db options
        open_layout = QHBoxLayout()
        open_buttons_layout = QVBoxLayout()
        # fill database connection properties
        dbs = ''
        for name, value in database.connection_parameters.items():
            dbs += '%s: %s\n' % (name, value)
        dblabel = QLabel(dbs[:-1])
        dblabel.setWordWrap(True)
        dblabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        open_layout.addWidget(dblabel, stretch=1)
        open_file = QPushButton(' Open new experiment ')
        settings_menu = QMenu(self)
        settings_button = QPushButton('Settings ...')
        settings_menu.addAction('Change database', self.onOpenDbConnection)
        settings_menu.addAction('Select modules', self.onOpenModulesSelector)
        settings_button.setMenu(settings_menu)
        open_buttons_layout.addWidget(open_file)
        open_buttons_layout.addStretch(1)
        open_buttons_layout.addWidget(settings_button)
        open_layout.addLayout(open_buttons_layout)
        
        left_layout = QVBoxLayout()
        left_layout.addLayout(open_layout, stretch=0)        
        left_layout.addWidget(self.selector, stretch=1)
        left_layout.addWidget(self.read_only_checkbox, stretch=0)
        lw = QWidget()
        lw.setLayout(left_layout)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(lw)#self.selector)

        # placeholder for the right
        self.right_layout = QHBoxLayout()
        self.prev_right_widget = None
        self.set_right_widget()

        rw = QWidget()
        rw.setLayout(self.right_layout)
        self.splitter.addWidget(rw)
        self.main_content_widget = None

        self.setCentralWidget(self.splitter)

        # connect signals
        self.selector.currentItemChanged.connect(self.onCurrentItemChanged)
        self.read_only_checkbox.stateChanged.connect(lambda: self.set_database_read_only(self.read_only_checkbox.isChecked()))
        open_file.clicked.connect(self.onOpenFile)

        settings = QSettings()
        self.restoreGeometry(settings.value(MainGUI.settingGeometry, QByteArray()))
        self.splitter.restoreState(settings.value(MainGUI.settingSplitter, QByteArray()))
        self.selector.restoreGeometry(settings.value(MainGUI.settingSelector, QByteArray()))

        self.show()

        if selectedItem is not None: self.selector.setCurrentItem(selectedItem)

    def set_database_read_only(self, state):
        if self.database.disable_read_only:
            state = False
            self.read_only_checkbox.setCheckState(Qt.Unchecked)
        else:
            if state:
                self.read_only_checkbox.setCheckState(Qt.Checked)
            else:
                self.read_only_checkbox.setCheckState(Qt.Unchecked)
            self.database.set_read_only(state)

    def closeEvent(self, event):
        settings = QSettings()
        settings.setValue(MainGUI.settingGeometry, self.saveGeometry())
        settings.setValue(MainGUI.settingSplitter, self.splitter.saveState())
        settings.setValue(MainGUI.settingSelector, self.selector.saveGeometry())
        if self.main_content_widget is not None:
            self.main_content_widget.save_settings()

        self.close()
        event.accept()

    def onCurrentItemChanged(self, itemNew, itemOld):
        if self.main_content_widget is not None:
            self.main_content_widget.save_settings()
            self.main_content_widget.deleteLater()
            self.main_content_widget = None

        if itemOld is not None:
            self.set_database_read_only(True)

        data = None
        if itemNew is not None and itemNew.experiment_id is not None:
            experiment_id = itemNew.experiment_id
            data = self.modules.create_data(self.database, experiment_id=experiment_id)
            if data is None:
                raise NotImplementedError("Not implemented hardware: " + ExperimentGeneric.hardware(self.database, experiment_id) +
                                          "\nExperiment ID: " + experiment_id)

            self.main_content_widget = MainWidget(self.database, data, self.modules)
            self.set_right_widget(self.main_content_widget)

        else:
            self.set_right_widget()

        if data is None:
            self.setWindowTitle('IOCBIO Kinetics, no data loaded')
        else:
            self.setWindowTitle('IOCBIO Kinetics: %s / %s' % (data.type, data.name))

    def onOpenDbConnection(self):
        self.reopen_database_connection = True
        self.close()

    def onOpenFile(self):
        self.open_file = True
        self.close()
        
    def onOpenModulesSelector(self):
        self.modules.select_modules_gui()

    def set_right_widget(self, widget=None):
        if widget is None:
            widget = QLabel("Please select experiment")

        if self.prev_right_widget is not None:
            self.right_layout.replaceWidget(self.prev_right_widget, widget)
            self.prev_right_widget.deleteLater()
            del self.prev_right_widget
        else:
            self.right_layout.addWidget(widget)
        self.prev_right_widget = widget
