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
from PyQt5.QtCore import QSettings, QByteArray
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QScrollArea, QPushButton, QFileDialog
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout

class OpenExperiment(QDialog):

    settingGeometry = "Open Experiment/geometry"

    def __init__(self, modules):
        QDialog.__init__(self)
        self.setWindowTitle('IOCBIO Kinetics: Open new experiment')

        QBtn = QDialogButtonBox.Open | QDialogButtonBox.Cancel

        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        # file open
        lopen = QHBoxLayout()
        lopen.addWidget(QLabel('File:'), stretch=0)
        self.filename = None
        self.filelabel = QLabel()
        lopen.addWidget(self.filelabel, stretch=0)
        lopen.addStretch(1)
        obutton = QPushButton('Select')
        obutton.clicked.connect(self.onFile)
        lopen.addWidget(obutton, stretch=0)

        # options
        self.parser, optgui = modules.gui()
        scroll = QScrollArea()
        scroll.setWidget(optgui)
        scroll.setWidgetResizable(True)

        # main layout
        layout = QVBoxLayout()
        layout.addLayout(lopen, stretch=0)
        layout.addWidget(scroll, stretch=1)
        layout.addWidget(buttonBox, stretch=0)
        self.setLayout(layout)

        settings = QSettings()
        self.restoreGeometry(settings.value(OpenExperiment.settingGeometry, QByteArray()))

    def closeEvent(self, event):
        settings = QSettings()
        settings.setValue(OpenExperiment.settingGeometry, self.saveGeometry())

    def onFile(self):
        fname, ftype = QFileDialog.getOpenFileName(self, caption='Open file')
        if fname != '':
            self.filename = fname
            self.filelabel.setText(fname)

    def getResponse(self):
        response = self.parser.get_options_gui()
        response['file_name'] = self.filename
        return response
