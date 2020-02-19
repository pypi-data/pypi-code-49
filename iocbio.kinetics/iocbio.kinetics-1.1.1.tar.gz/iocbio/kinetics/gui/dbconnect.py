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
from PyQt5.QtCore import Qt, pyqtSignal, QSettings, QByteArray
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QCheckBox, QStackedLayout
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox, QRadioButton, QGridLayout, QLineEdit
from collections import OrderedDict

from ..io.db import DatabaseInterface
from .custom_widgets import SmallLabel

class ConnectionParameters(QWidget):

    def __init__(self, parameters):
        QWidget.__init__(self)

        self.parameters = parameters
        layout = QGridLayout()
        for k, v in self.parameters.items():

            input_widget = QLineEdit(v['default'])
            input_widget.setMinimumWidth(150)
            v['field'] = input_widget

            row = layout.rowCount()
            layout.addWidget(QLabel(v['short']), row, 0)
            layout.addWidget(input_widget, row, 1)
            layout.addWidget(SmallLabel(v['description']), row+1, 0, 1, 2)
            layout.addWidget(SmallLabel(''), row+2, 0, 1, 2)

        self.setLayout(layout)

    def get_parameter_values(self):
        d = {}
        for k, v in self.parameters.items():
            d[k] = v['field'].text()
        return d


class ConnectDatabaseGUI(QWidget):
    """Class for selecting database type"""
    settingGeometry = "Connect Database GUI/geometry"

    def __init__(self):
        QWidget.__init__(self)

        DatabaseInterface.remove_login()
        settings = DatabaseInterface.settings()
        dbtype = str(settings.value(DatabaseInterface.settings_dbtype, "sqlite3"))
        self.save_settings = False
        self.sqlite3 = QRadioButton('SQLite')
        self.postgresql = QRadioButton('PostgreSQL')
        getattr(self, dbtype).setChecked(True)
        connect = QPushButton('Connect')

        self.sqlite3.toggled.connect(self.show_dbtype_options)
        connect.clicked.connect(self.connect_database)

        psql_parameters = OrderedDict([
            ['hostname', {'short': 'Hostname', 'description': 'Hostname of database server', 'default': ''}],
            ['database', {'short': 'Database name', 'description': '', 'default': ''}],
            ['schema', {'short': 'Schema', 'description': 'PostgreSQL schema. For example: public', 'default': 'public'}],
            ])

        for key, value in psql_parameters.items():
            value['default'] = str(settings.value(getattr(DatabaseInterface, 'settings_pg_'+key), ''))

        self.layout_stack = QStackedLayout()
        self.sqlite_connection_parameters = QWidget()
        self.psql_connection_parameters = ConnectionParameters(psql_parameters)
        self.layout_stack.addWidget(self.sqlite_connection_parameters)
        self.layout_stack.addWidget(self.psql_connection_parameters)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Select database type:'))
        layout.addWidget(self.sqlite3)
        layout.addWidget(self.postgresql)
        layout.addLayout(self.layout_stack)
        layout.addWidget(QLabel('Login username and password were reset.\n'))
        layout.addStretch(1)
        layout.addWidget(connect)

        self.setWindowTitle('IOCBIO Kinetics: connect to database')
        self.setLayout(layout)
        self.show_dbtype_options()

        # load settings
        self.restoreGeometry(settings.value(ConnectDatabaseGUI.settingGeometry, QByteArray()))

    def show_dbtype_options(self):
        if self.sqlite3.isChecked():
            self.layout_stack.setCurrentWidget(self.sqlite_connection_parameters)
        if self.postgresql.isChecked():
            self.layout_stack.setCurrentWidget(self.psql_connection_parameters)

    def connect_database(self):
        settings = DatabaseInterface.settings()
        settings.setValue(ConnectDatabaseGUI.settingGeometry, self.saveGeometry())
        if self.sqlite3.isChecked():
            settings.setValue(DatabaseInterface.settings_dbtype, 'sqlite3')
        if self.postgresql.isChecked():
            settings.setValue(DatabaseInterface.settings_dbtype, 'postgresql')
            for k, v in self.layout_stack.currentWidget().get_parameter_values().items():
                settings.setValue(getattr(DatabaseInterface, 'settings_pg_'+k), v)
        self.save_settings = True
        self.close()
