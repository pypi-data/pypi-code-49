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
