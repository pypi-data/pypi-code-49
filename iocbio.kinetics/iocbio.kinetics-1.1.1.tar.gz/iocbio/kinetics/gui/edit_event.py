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

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QColor, QFrame, QPalette
from unicodedata import normalize
import re


class HLine(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFrameShape(QFrame.HLine)
        self.setLineWidth(5)
        self.set_color()

    def set_color(self, color=None):
        if color is not None:
            palette = QPalette(self.palette())
            color = QColor(color)
            color.setAlpha(60)
            palette.setColor(palette.Foreground, color)
            self.setPalette(palette)


class EventEdit(QWidget):

    sigEventNameChanged = pyqtSignal(str, str)

    def __init__(self):
        QWidget.__init__(self)

        self.data = None
        self.edit = QLineEdit()
        self.line = HLine()

        layout_up = QHBoxLayout()
        layout_up.addWidget(QLabel('Event name:'))
        layout_up.addWidget(self.edit)

        layout = QVBoxLayout()
        layout.addLayout(layout_up)
        layout.addWidget(self.line)
        self.setLayout(layout)

        self.edit.returnPressed.connect(self.event_name_changed)

        if self.data is None:
            self.hide()

    def set_data(self, data):
        self.data = data
        if data is None:
            self.hide()
            return

        self.update_fields()

    def update_fields(self):
        self.edit.setText(str(self.data.data.event_name))
        self.line.set_color('#%s'%self.data.data.data_id[:6])
        self.show()

    def event_name_changed(self):
        if self.data is None: return
        txt = normalize('NFKC', re.sub(' +', ' ', self.edit.text().strip()))
        self.edit.setText(txt)
        self.sigEventNameChanged.emit(self.data.data.data_id, txt)
