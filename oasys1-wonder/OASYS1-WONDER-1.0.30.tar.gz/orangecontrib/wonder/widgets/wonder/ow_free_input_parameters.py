#!/usr/bin/env python
# -*- coding: utf-8 -*-
# #########################################################################
# Copyright (c) 2020, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2020. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################

import sys

from PyQt5.QtWidgets import QMessageBox, QScrollArea, QApplication
from PyQt5.QtCore import Qt

from orangewidget.settings import Setting
from orangewidget.widget import OWAction
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_widget import OWGenericWidget
from orangecontrib.wonder.util.gui_utility import gui

from orangecontrib.wonder.fit.parameters.fit_global_parameters import FitGlobalParameters


class OWFreeInputParameters(OWGenericWidget):
    name = "Free Input Parameters"
    description = "Free Input Parameters"
    icon = "icons/free_input_parameters.png"
    priority = 50

    want_main_area = False

    free_input_parameters = Setting("")

    inputs = [("Fit Global Parameters", FitGlobalParameters, 'set_data')]
    outputs = [("Fit Global Parameters", FitGlobalParameters)]

    def __init__(self):
        super().__init__(show_automatic_box=True)

        main_box = gui.widgetBox(self.controlArea,
                                 "", orientation="vertical",
                                 width=self.CONTROL_AREA_WIDTH - 10, height=500)


        button_box = gui.widgetBox(main_box,
                                   "", orientation="horizontal",
                                   width=self.CONTROL_AREA_WIDTH - 25)


        gui.button(button_box,  self, "Send Free Input Parameters", height=40, callback=self.send_free_input_parameters)

        tabs = gui.tabWidget(main_box)
        tab_free_in = gui.createTabPage(tabs, "Free Input Parameters")

        self.scrollarea_free_in = QScrollArea(tab_free_in)
        self.scrollarea_free_in.setMinimumWidth(self.CONTROL_AREA_WIDTH-45)
        self.scrollarea_free_in.setMinimumHeight(160)

        self.text_area_free_in = gui.textArea(height=400, width=self.CONTROL_AREA_WIDTH-65, readOnly=False)
        self.text_area_free_in.setText(self.free_input_parameters)

        self.scrollarea_free_in.setWidget(self.text_area_free_in)
        self.scrollarea_free_in.setWidgetResizable(1)

        tab_free_in.layout().addWidget(self.scrollarea_free_in, alignment=Qt.AlignHCenter)

        runaction = OWAction("Send Free Input Parameters", self)
        runaction.triggered.connect(self.send_free_input_parameters)
        self.addAction(runaction)

        orangegui.rubber(self.controlArea)

    def get_max_height(self):
        return 600

    def send_free_input_parameters(self):
        try:
            if not self.fit_global_parameters is None:
                self.free_input_parameters = self.text_area_free_in.toPlainText()

                self.fit_global_parameters.free_input_parameters.parse_values(self.free_input_parameters)
                self.fit_global_parameters.regenerate_parameters()

                self.send("Fit Global Parameters", self.fit_global_parameters)

        except Exception as e:
            QMessageBox.critical(self, "Error",
                                 str(e),
                                 QMessageBox.Ok)

            if self.IS_DEVELOP: raise e

        self.setStatusMessage("")
        self.progressBarFinished()


    def set_data(self, data):
        if not data is None:
            self.fit_global_parameters = data.duplicate()

            self.fit_global_parameters.free_input_parameters.parse_values(self.text_area_free_in.toPlainText()) # existing parameters

            self.text_area_free_in.setText(self.fit_global_parameters.free_input_parameters.to_python_code())
            self.free_input_parameters = self.text_area_free_in.toPlainText()

            if self.is_automatic_run:
                self.send_free_input_parameters()


if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWFreeInputParameters()
    ow.show()
    a.exec_()
    ow.saveSettings()
