import os, sys, numpy, copy

from PyQt5.QtWidgets import QMessageBox, QScrollArea, QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QColor, QFont

from silx.gui.plot.PlotWindow import PlotWindow

from orangewidget.settings import Setting
from orangewidget import gui as orangegui
from orangewidget.widget import OWAction

from orangecontrib.wonder.widgets.gui.ow_generic_widget import OWGenericWidget
from orangecontrib.wonder.util.gui_utility import gui, ConfirmDialog
from oasys.widgets import congruence

from orangecontrib.wonder.fit.parameters.fit_global_parameters import FitGlobalParameters
from orangecontrib.wonder.fit.parameters.measured_data.measured_dataset import MeasuredDataset
from orangecontrib.wonder.fit.parameters.measured_data.diffraction_pattern import DiffractionPattern, DiffractionPatternFactory, DiffractionPatternLimits
from orangecontrib.wonder.fit.parameters.initialization.fit_initialization import FitInitialization

class OWDiffractionPattern(OWGenericWidget):

    name = "Load Diffraction Pattern"
    description = "Loads diffraction pattern " \
                  "points from most common file formats"
    icon = "icons/diffraction_pattern.png"
    priority = 1

    want_main_area = True

    filename = Setting(["<input file>"])

    twotheta_min = Setting([0.0])
    twotheta_has_min = Setting([0])
    twotheta_max = Setting([0.0])
    twotheta_has_max = Setting([0])

    diffraction_pattern_name = Setting([""])

    horizontal_headers = ["2Theta [deg]", "s [nm^-1]", "Intensity", "Error"]

    inputs = []

    diffraction_patterns = None

    def __init__(self):
        super().__init__(show_automatic_box=False)

        main_box = gui.widgetBox(self.controlArea,
                                 "Load Diffraction Pattern", orientation="vertical",
                                 width=self.CONTROL_AREA_WIDTH - 5, height=600)


        button_box = gui.widgetBox(main_box,
                                   "", orientation="horizontal",
                                   width=self.CONTROL_AREA_WIDTH-25)

        gui.button(button_box, self, "Load Data", height=50, callback=self.load_diffraction_patterns)

        tabs_button_box = gui.widgetBox(main_box, "", addSpace=False, orientation="horizontal")

        btns = [gui.button(tabs_button_box, self, "Insert Before", callback=self.insert_before),
                gui.button(tabs_button_box, self, "Insert After", callback=self.insert_after),
                gui.button(tabs_button_box, self, "Remove", callback=self.remove),
                gui.button(tabs_button_box, self, "Remove All", callback=self.remove_all)]

        for btn in btns:
            btn.setFixedHeight(40)

        btns[3].setStyleSheet("color: red")
        font = QFont(btns[3].font())
        font.setItalic(True)
        btns[3].setFont(font)

        self.diffraction_pattern_tabs = gui.tabWidget(main_box)
        self.diffraction_pattern_box_array = []

        for index in range(len(self.filename)):
            diffraction_pattern_tab = gui.createTabPage(self.diffraction_pattern_tabs, DiffractionPattern.get_default_name(index))

            diffraction_pattern_box = DiffractionPatternBox(widget=self,
                                                            parent=diffraction_pattern_tab,
                                                            index = index,
                                                            filename                    = self.filename[index],
                                                            twotheta_min                = self.twotheta_min[index],
                                                            twotheta_has_min            = self.twotheta_has_min[index],
                                                            twotheta_max                = self.twotheta_max[index],
                                                            twotheta_has_max            = self.twotheta_has_max[index],
                                                            diffraction_pattern_name    = self.diffraction_pattern_name[index])

            self.diffraction_pattern_box_array.append(diffraction_pattern_box)

        self.tabs = gui.tabWidget(self.mainArea)
        self.tab_diff = []
        self.tabs_data_plot = []
        self.tab_data = []
        self.tab_plot = []
        self.plot = []
        self.table_data = []

        for index in range(len(self.filename)):
            self.tab_diff.append(gui.createTabPage(self.tabs, DiffractionPattern.get_default_name(index)))
            self.tabs_data_plot.append(gui.tabWidget(self.tab_diff[index]))
            self.tab_data.append(gui.createTabPage(self.tabs_data_plot[index], "Data"))
            self.tab_plot.append(gui.createTabPage(self.tabs_data_plot[index], "Plot"))

            self.plot.append(PlotWindow())
            self.plot[index].setDefaultPlotLines(True)
            self.plot[index].setActiveCurveColor(color="#00008B")
            self.plot[index].setGraphXLabel(r"2$\theta$")
            self.plot[index].setGraphYLabel("Intensity")

            self.tab_plot[index].layout().addWidget(self.plot[index])

            table_widget = self.create_table_widget()

            self.table_data.append(table_widget)

            self.tab_data[index].layout().addWidget(table_widget, alignment=Qt.AlignHCenter)

        runaction = OWAction("Load Diffraction Patterns", self)
        runaction.triggered.connect(self.load_diffraction_patterns)
        self.addAction(runaction)
        
    def insert_before(self):
        current_index = self.diffraction_pattern_tabs.currentIndex()

        if ConfirmDialog.confirmed(parent=self, message="Confirm Insertion of a new element before " + self.diffraction_pattern_tabs.tabText(current_index) + "?"):
            diffraction_pattern_tab = gui.widgetBox(self.diffraction_pattern_tabs, addToLayout=0, margin=4)
            diffraction_pattern_box = DiffractionPatternBox(widget=self, parent=diffraction_pattern_tab, index=current_index)
            diffraction_pattern_box.after_change_workspace_units()

            self.diffraction_pattern_tabs.insertTab(current_index, diffraction_pattern_tab, "TEMP")
            self.diffraction_pattern_box_array.insert(current_index, diffraction_pattern_box)

            diffraction_pattern_pd_tab = gui.widgetBox(self.tabs, addToLayout=0, margin=4)
            self.tabs.insertTab(current_index, diffraction_pattern_pd_tab, "TEMP")
            self.tab_diff.insert(current_index, diffraction_pattern_pd_tab)

            self.tabs_data_plot.insert(current_index, gui.tabWidget(self.tab_diff[current_index]))
            self.tab_data.insert(current_index, gui.createTabPage(self.tabs_data_plot[current_index], "Data"))
            self.tab_plot.insert(current_index, gui.createTabPage(self.tabs_data_plot[current_index], "Plot"))

            self.plot.insert(current_index, PlotWindow())
            self.plot[current_index].setDefaultPlotLines(True)
            self.plot[current_index].setActiveCurveColor(color="#00008B")
            self.plot[current_index].setGraphXLabel(r"2$\theta$")
            self.plot[current_index].setGraphYLabel("Intensity")

            self.tab_plot[current_index].layout().addWidget(self.plot[current_index])

            scrollarea = QScrollArea(self.tab_data[current_index])
            scrollarea.setMinimumWidth(805)
            scrollarea.setMinimumHeight(605)

            self.table_data.insert(current_index, self.create_table_widget())

            scrollarea.setWidget(self.table_data[current_index])
            scrollarea.setWidgetResizable(1)

            self.tab_data[current_index].layout().addWidget(scrollarea, alignment=Qt.AlignHCenter)

            for index in range(current_index, self.diffraction_pattern_tabs.count()):
                self.diffraction_pattern_tabs.setTabText(index, DiffractionPattern.get_default_name(index))
                self.diffraction_pattern_box_array[index].index = index
                self.tabs.setTabText(index, DiffractionPattern.get_default_name(index))

            self.dumpSettings()
            self.diffraction_pattern_tabs.setCurrentIndex(current_index)
            self.tabs.setCurrentIndex(current_index)

    def insert_after(self):
        current_index = self.diffraction_pattern_tabs.currentIndex()

        if ConfirmDialog.confirmed(parent=self, message="Confirm Insertion of a new element after " + self.diffraction_pattern_tabs.tabText(current_index) + "?"):
            diffraction_pattern_tab = gui.widgetBox(self.diffraction_pattern_tabs, addToLayout=0, margin=4)
            diffraction_pattern_box = DiffractionPatternBox(widget=self, parent=diffraction_pattern_tab, index=current_index+1)
            diffraction_pattern_box.after_change_workspace_units()

            diffraction_pattern_pd_tab = gui.widgetBox(self.tabs, addToLayout=0, margin=4)

            if current_index == self.diffraction_pattern_tabs.count() - 1:  # LAST
                self.diffraction_pattern_tabs.addTab(diffraction_pattern_tab, "TEMP")
                self.diffraction_pattern_box_array.append(diffraction_pattern_box)
                
                self.tabs.addTab(diffraction_pattern_pd_tab, "TEMP")
                self.tab_diff.append(diffraction_pattern_pd_tab)
    
                self.tabs_data_plot.append(gui.tabWidget(self.tab_diff[current_index + 1]))
                self.tab_data.append(gui.createTabPage(self.tabs_data_plot[current_index + 1], "Data"))
                self.tab_plot.append(gui.createTabPage(self.tabs_data_plot[current_index + 1], "Plot"))
    
                self.plot.append(PlotWindow())
                self.plot[current_index + 1].setDefaultPlotLines(True)
                self.plot[current_index + 1].setActiveCurveColor(color="#00008B")
                self.plot[current_index + 1].setGraphXLabel(r"2$\theta$")
                self.plot[current_index + 1].setGraphYLabel("Intensity")
    
                self.tab_plot[current_index + 1].layout().addWidget(self.plot[current_index + 1])
    
                scrollarea = QScrollArea(self.tab_data[current_index])
                scrollarea.setMinimumWidth(805)
                scrollarea.setMinimumHeight(605)
    
                self.table_data.append(self.create_table_widget())
    
                scrollarea.setWidget(self.table_data[current_index + 1])
                scrollarea.setWidgetResizable(1)
    
                self.tab_data[current_index + 1].layout().addWidget(scrollarea, alignment=Qt.AlignHCenter)
            else:
                self.diffraction_pattern_tabs.insertTab(current_index + 1, diffraction_pattern_tab, "TEMP")
                self.diffraction_pattern_box_array.insert(current_index + 1, diffraction_pattern_box)
                
                self.tabs.insertTab(current_index + 1, diffraction_pattern_pd_tab, "TEMP")
                self.tab_diff.insert(current_index + 1, diffraction_pattern_pd_tab)
    
                self.tabs_data_plot.insert(current_index + 1, gui.tabWidget(self.tab_diff[current_index + 1]))
                self.tab_data.insert(current_index + 1, gui.createTabPage(self.tabs_data_plot[current_index + 1], "Data"))
                self.tab_plot.insert(current_index + 1, gui.createTabPage(self.tabs_data_plot[current_index + 1], "Plot"))
    
                self.plot.insert(current_index + 1, PlotWindow())
                self.plot[current_index + 1].setDefaultPlotLines(True)
                self.plot[current_index + 1].setActiveCurveColor(color="#00008B")
                self.plot[current_index + 1].setGraphXLabel(r"2$\theta$")
                self.plot[current_index + 1].setGraphYLabel("Intensity")
    
                self.tab_plot[current_index + 1].layout().addWidget(self.plot[current_index + 1])
    
                scrollarea = QScrollArea(self.tab_data[current_index + 1])
                scrollarea.setMinimumWidth(805)
                scrollarea.setMinimumHeight(605)
    
                self.table_data.insert(current_index + 1, self.create_table_widget())
    
                scrollarea.setWidget(self.table_data[current_index + 1])
                scrollarea.setWidgetResizable(1)
    
                self.tab_data[current_index + 1].layout().addWidget(scrollarea, alignment=Qt.AlignHCenter)

            for index in range(current_index, self.diffraction_pattern_tabs.count()):
                self.diffraction_pattern_tabs.setTabText(index, DiffractionPattern.get_default_name(index))
                self.diffraction_pattern_box_array[index].index = index
                self.tabs.setTabText(index, DiffractionPattern.get_default_name(index))

            self.dumpSettings()
            self.diffraction_pattern_tabs.setCurrentIndex(current_index + 1)
            self.tabs.setCurrentIndex(current_index + 1)

    def remove(self):
        if self.diffraction_pattern_tabs.count() <= 1:
            QMessageBox.critical(self, "Error",
                                       "Remove not possible, Fit process needs at least 1 element",
                                       QMessageBox.Ok)
        else:
            current_index = self.diffraction_pattern_tabs.currentIndex()

            if ConfirmDialog.confirmed(parent=self, message="Confirm Removal of " + self.diffraction_pattern_tabs.tabText(current_index) + "?"):
                self.diffraction_pattern_tabs.removeTab(current_index)
                self.diffraction_pattern_box_array.pop(current_index)

                self.tabs.removeTab(current_index)
                self.tab_diff.pop(current_index)
                self.tabs_data_plot.pop(current_index)
                self.tab_data.pop(current_index)
                self.tab_plot.pop(current_index)
                self.plot.pop(current_index)
                self.table_data.pop(current_index)

                for index in range(current_index, self.diffraction_pattern_tabs.count()):
                    self.diffraction_pattern_tabs.setTabText(index, DiffractionPattern.get_default_name(index))
                    self.diffraction_pattern_box_array[index].index = index
                    self.tabs.setTabText(index, DiffractionPattern.get_default_name(index))

                self.dumpSettings()
                self.diffraction_pattern_tabs.setCurrentIndex(current_index)
                self.tabs.setCurrentIndex(current_index)

    def remove_all(self):
        if ConfirmDialog.confirmed(parent=self, message="Confirm Removal of ALL diffraction Pattern?"):
            self.diffraction_pattern_tabs.clear()
            self.diffraction_pattern_box_array = []

            diffraction_pattern_box = DiffractionPatternBox(widget=self,
                                                            parent=gui.createTabPage(self.diffraction_pattern_tabs, DiffractionPattern.get_default_name(0)),
                                                            index = 0)

            self.diffraction_pattern_box_array.append(diffraction_pattern_box)

            self.tabs.clear()
            self.tab_diff = []
            self.tabs_data_plot = []
            self.tab_data = []
            self.tab_plot = []
            self.plot = []
            self.table_data = []

            self.tab_diff.append(gui.createTabPage(self.tabs, DiffractionPattern.get_default_name(0)))
            self.tabs_data_plot.append(gui.tabWidget(self.tab_diff[0]))
            self.tab_data.append(gui.createTabPage(self.tabs_data_plot[0], "Data"))
            self.tab_plot.append(gui.createTabPage(self.tabs_data_plot[0], "Plot"))

            self.plot.append(PlotWindow())
            self.plot[0].setDefaultPlotLines(True)
            self.plot[0].setActiveCurveColor(color="#00008B")
            self.plot[0].setGraphXLabel(r"2$\theta$")
            self.plot[0].setGraphYLabel("Intensity")

            self.tab_plot[0].layout().addWidget(self.plot[0])

            table_widget = self.create_table_widget()

            self.table_data.append(table_widget)

            self.tab_data[0].layout().addWidget(table_widget, alignment=Qt.AlignHCenter)

            self.dumpSettings()


    def load_diffraction_patterns(self):
        try:
            self.dumpSettings()

            self.diffraction_patterns = []
            for index in range(len(self.filename)):
                self.diffraction_pattern_box_array[index].load_diffraction_pattern()
                self.diffraction_patterns.append(self.diffraction_pattern_box_array[index].diffraction_pattern)

                self.show_data(index)

            self.tabs.setCurrentIndex(self.diffraction_pattern_tabs.currentIndex())
            self.tabs_data_plot[self.diffraction_pattern_tabs.currentIndex()].setCurrentIndex(1)

            fit_global_parameters = FitGlobalParameters(masured_dataset=MeasuredDataset.initialize_with_diffraction_patterns(diffraction_patterns=self.diffraction_patterns),
                                                        fit_initialization=FitInitialization())
            fit_global_parameters.regenerate_parameters()

            self.send("Fit Global Parameters", fit_global_parameters)

        except Exception as e:
            QMessageBox.critical(self, "Error during load",
                                 str(e),
                                 QMessageBox.Ok)

            if self.IS_DEVELOP: raise e

    def show_data(self, diffraction_pattern_index=0):
        diffraction_pattern = self.diffraction_patterns[diffraction_pattern_index]

        x = []
        y = []

        for index in range(0, diffraction_pattern.diffraction_points_count()):
            x.append(diffraction_pattern.get_diffraction_point(index).twotheta)
            y.append(diffraction_pattern.get_diffraction_point(index).intensity)

        self.plot[diffraction_pattern_index].addCurve(x, y, linewidth=2, color="#0B0B61")

        self.populate_table(self.table_data[diffraction_pattern_index], diffraction_pattern)


    def create_table_widget(self):
        table = QTableWidget(1, 4)
        table.setMinimumWidth(750)
        table.setAlternatingRowColors(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        table.verticalHeader().setVisible(False)
        table.setHorizontalHeaderLabels(self.horizontal_headers)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        return table

    def populate_table(self, table_widget, diffraction_pattern):
        table_widget.clear()

        row_count = table_widget.rowCount()
        for n in range(0, row_count):
            table_widget.removeRow(0)

        for index in range(0, diffraction_pattern.diffraction_points_count()):
            table_widget.insertRow(0)

        for index in range(0, diffraction_pattern.diffraction_points_count()):
            diffraction_point = diffraction_pattern.get_diffraction_point(index)
            twotheta = diffraction_point.twotheta
            intensity = diffraction_point.intensity
            error = diffraction_point.error
            s = diffraction_point.s

            table_item = QTableWidgetItem("" if twotheta is None else str(round(twotheta, 6)))
            table_item.setTextAlignment(Qt.AlignRight)
            table_widget.setItem(index, 0, table_item)

            table_item = QTableWidgetItem("" if s is None else str(round(s, 6)))
            table_item.setTextAlignment(Qt.AlignRight)
            table_widget.setItem(index, 1, table_item)

            table_item = QTableWidgetItem(str(round(intensity, 6)))
            table_item.setTextAlignment(Qt.AlignRight)
            table_widget.setItem(index, 2, table_item)

            table_item = QTableWidgetItem("" if error is None else str(round(error, 6)))
            table_item.setTextAlignment(Qt.AlignRight)
            table_widget.setItem(index, 3, table_item)

        table_widget.setHorizontalHeaderLabels(self.horizontal_headers)
        table_widget.resizeRowsToContents()
        table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def get_parameter_box_array(self):
        return self.diffraction_pattern_box_array

    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def dumpSettings(self):
        self.dump_filename()
        self.dump_twotheta_has_min()
        self.dump_twotheta_min()
        self.dump_twotheta_has_max()
        self.dump_twotheta_max()
        self.dump_diffraction_pattern_name()

    def dump_filename(self): self.dump_variable("filename")
    def dump_twotheta_min(self): self.dump_variable("twotheta_min")
    def dump_twotheta_has_min(self): self.dump_variable("twotheta_has_min")
    def dump_twotheta_max(self): self.dump_variable("twotheta_max")
    def dump_twotheta_has_max(self): self.dump_variable("twotheta_has_max")
    def dump_diffraction_pattern_name(self): self.dump_variable("diffraction_pattern_name")


from PyQt5.QtWidgets import QVBoxLayout
from orangecontrib.wonder.util.gui_utility import InnerBox

class DiffractionPatternBox(InnerBox):

    filename = "<input file>"
    twotheta_min = 0.0
    twotheta_has_min = 0
    twotheta_max = 0.0
    twotheta_has_max = 0
    diffraction_pattern_name = ""

    widget = None
    is_on_init = True

    parameter_functions = {}

    diffraction_pattern = None

    index = 0

    def __init__(self,
                 widget=None,
                 parent=None,
                 index = 0,
                 filename = "<input file>",
                 twotheta_min = 0.0,
                 twotheta_has_min = 0,
                 twotheta_max = 0.0,
                 twotheta_has_max = 0,
                 diffraction_pattern_name = ""):
        super(DiffractionPatternBox, self).__init__()


        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.setFixedWidth(widget.CONTROL_AREA_WIDTH-35)
        self.setFixedHeight(500)

        self.widget = widget
        self.index = index
        
        self.filename                    = filename
        self.twotheta_min                = twotheta_min
        self.twotheta_has_min            = twotheta_has_min
        self.twotheta_max                = twotheta_max
        self.twotheta_has_max            = twotheta_has_max
        self.diffraction_pattern_name    = diffraction_pattern_name

        self.CONTROL_AREA_WIDTH = widget.CONTROL_AREA_WIDTH-45

        parent.layout().addWidget(self)
        container = self

        gui.lineEdit(container, self, "diffraction_pattern_name", "Sample Name\n(will appear in tabs and plots)", labelWidth=180, valueType=str, callback=widget.dump_diffraction_pattern_name)

        file_box = gui.widgetBox(container, "", orientation="horizontal", width=self.CONTROL_AREA_WIDTH)

        self.le_filename = gui.lineEdit(file_box, self, value="filename", valueType=str, label="File", labelWidth=50, callback=widget.dump_filename, orientation="horizontal")

        orangegui.button(file_box, self, "...", callback=self.open_folders)

        box = gui.widgetBox(container, "", orientation="horizontal", width=self.CONTROL_AREA_WIDTH)

        orangegui.checkBox(box, self, "twotheta_has_min", "2\u03b8 min [deg]", labelWidth=350, callback=widget.dump_twotheta_has_min)
        gui.lineEdit(box, self, "twotheta_min", " ", labelWidth=5, valueType=float, validator=QDoubleValidator(), callback=self.set_twotheta_min, orientation="horizontal")

        box = gui.widgetBox(container, "", orientation="horizontal", width=self.CONTROL_AREA_WIDTH)

        orangegui.checkBox(box, self, "twotheta_has_max", "2\u03b8 max [deg]", labelWidth=350, callback=widget.dump_twotheta_has_max)
        gui.lineEdit(box, self, "twotheta_max", " ", labelWidth=5, valueType=float, validator=QDoubleValidator(), callback=self.set_twotheta_max, orientation="horizontal")

        self.is_on_init = False

    def set_twotheta_min(self):
        self.twotheta_has_min = 1
        if not self.is_on_init:
            self.widget.dump_twotheta_min()
            self.widget.dump_twotheta_has_min()

    def set_twotheta_max(self):
        self.twotheta_has_max = 1
        if not self.is_on_init:
            self.widget.dump_twotheta_max()
            self.widget.dump_twotheta_has_max()

    def open_folders(self):
        self.filename=gui.selectFileFromDialog(self,
                                               self.filename,
                                               start_directory=os.curdir)

        self.le_filename.setText(self.filename)

    def after_change_workspace_units(self):
        pass

    def set_index(self, index):
        self.index = index

    def load_diffraction_pattern(self):
        congruence.checkFile(self.filename)

        if self.twotheta_has_min == 1 or self.twotheta_has_max == 1:
            limits = DiffractionPatternLimits(twotheta_min=self.twotheta_min if self.twotheta_has_min==1 else -numpy.inf,
                                              twotheta_max=self.twotheta_max if self.twotheta_has_max==1 else numpy.inf)
        else:
            limits=None

        self.diffraction_pattern = DiffractionPatternFactory.create_diffraction_pattern_from_file(self.filename, limits, self.diffraction_pattern_name)
if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWDiffractionPattern()
    ow.show()
    a.exec_()
    ow.saveSettings()
