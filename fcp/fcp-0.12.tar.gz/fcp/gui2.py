# from PySide2.QtWidgets import *
# from PySide2.QtGui import QKeySequence
# from PySide2.QtCore import Qt
#
# from .gui_lib.mainwindow import Ui_MainWindow
# from .gui_lib.devicewidget import Ui_DeviceWidget
# from .gui_lib.devicedetails import Ui_DeviceDetails
# from .gui_lib.messagewidget import Ui_MessageWidget
# from .gui_lib.messagedetails import Ui_MessageDetails
# from .gui_lib.signalwidget import Ui_SignalWidget
# from .gui_lib.signaldetails import Ui_SignalDetails
# from .gui_lib.logwidget import Ui_LogWidget
# from .gui_lib.logdetails import Ui_LogDetails
# from .gui_lib.cfgwidget import Ui_CfgWidget
# from .gui_lib.cfgdetails import Ui_CfgDetails
# from .gui_lib.cmdwidget import Ui_CmdWidget
# from .gui_lib.cmddetails import Ui_CmdDetails
# from .gui_lib.cmdarg import Ui_CmdArg
#
# def DetailsWidget(QWidget):
#    def __init__(self, gui, obj, parent):
#        QWidget.__init__(self)
#
#        self.atts = []
#
#    def save(self):
#        for att, get_f, set_f in self.atts:
#            set_f(att.text())
#
#        self.gui.reload()
#
#    def reload(self):
#        for att, get_f, set_f in self.atts:
#            att.setText(str(get_f()))
#
#    def delete(self):
#        r = self.gui.spec.rm_signal(self.signal)
#        self.setVisible(False)
#        self.dev_widget.setVisible(False)
#        return
