from PyQt5.QtWidgets import QMessageBox

from oasys.menus.menu import OMenu
from orangecanvas.scheme.link import SchemeLink

from orangecontrib.wonder.widgets.wonder.ow_fitter import OWFitter

class WonderMenu(OMenu):

    def __init__(self):
        super().__init__(name="Wonder")

        self.openContainer()
        self.addContainer("Fitter")
        self.addSubMenu("Enable Automatic Fit in all the Fitter widgets")
        self.addSubMenu("Disable Automatic Fit in all the Fitter widgets")
        self.addSeparator()
        self.addSubMenu("Enable Plotting in all the Fitter widgets")
        self.addSubMenu("Disable Plotting in all the Fitter widgets")
        self.closeContainer()
        self.addSeparator()
        self.addSubMenu("Go to Wonder Use Cases Page")

    def executeAction_1(self, action):
        try:
            for node in self.canvas_main_window.current_document().scheme().nodes:
                widget = self.canvas_main_window.current_document().scheme().widget_for_node(node)

                if isinstance(widget, OWFitter):
                    if hasattr(widget, "is_automatic_run"):
                        widget.is_automatic_run = True
        except Exception as exception:
            QMessageBox.critical(None, "Error", exception.args[0], QMessageBox.Ok)

    def executeAction_2(self, action):
        try:
            for node in self.canvas_main_window.current_document().scheme().nodes:
                widget = self.canvas_main_window.current_document().scheme().widget_for_node(node)

                if isinstance(widget, OWFitter):
                    if hasattr(widget, "is_automatic_run"):
                        widget.is_automatic_run = False
        except Exception as exception:
            QMessageBox.critical(None, "Error", exception.args[0], QMessageBox.Ok)

    def executeAction_3(self, action):
        try:
            for node in self.canvas_main_window.current_document().scheme().nodes:
                widget = self.canvas_main_window.current_document().scheme().widget_for_node(node)

                if isinstance(widget, OWFitter):
                    if hasattr(widget, "is_automatic_run"):
                        widget.is_interactive = 1
                        widget.set_interactive()
        except Exception as exception:
            QMessageBox.critical(None, "Error", exception.args[0], QMessageBox.Ok)

    def executeAction_4(self, action):
        try:
            for node in self.canvas_main_window.current_document().scheme().nodes:
                widget = self.canvas_main_window.current_document().scheme().widget_for_node(node)

                if isinstance(widget, OWFitter):
                    if hasattr(widget, "is_interactive"):
                        widget.is_interactive = 0
                        widget.set_interactive()
        except Exception as exception:
            QMessageBox.critical(None, "Error", exception.args[0], QMessageBox.Ok)

    def executeAction_5(self, action):
        try:
            import webbrowser
            webbrowser.open("https://github.com/WONDER-project/WONDER_Use-Cases")
        except Exception as exception:
            QMessageBox.critical(None, "Error", exception.args[0], QMessageBox.Ok)

