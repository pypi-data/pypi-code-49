# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logwidget.ui',
# licensing of 'logwidget.ui' applies.
#
# Created: Sat Dec  7 20:52:35 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_LogWidget(object):
    def setupUi(self, LogWidget):
        LogWidget.setObjectName("LogWidget")
        LogWidget.resize(400, 300)
        LogWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(LogWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(LogWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.LogScrollContents = QtWidgets.QWidget()
        self.LogScrollContents.setGeometry(QtCore.QRect(0, 0, 356, 209))
        self.LogScrollContents.setObjectName("LogScrollContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LogScrollContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logContents = QtWidgets.QVBoxLayout()
        self.logContents.setObjectName("logContents")
        self.verticalLayout_2.addLayout(self.logContents)
        self.scrollArea.setWidget(self.LogScrollContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.addLogButton = QtWidgets.QPushButton(self.groupBox)
        self.addLogButton.setObjectName("addLogButton")
        self.verticalLayout_3.addWidget(self.addLogButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(LogWidget)
        QtCore.QMetaObject.connectSlotsByName(LogWidget)

    def retranslateUi(self, LogWidget):
        LogWidget.setWindowTitle(
            QtWidgets.QApplication.translate("LogWidget", "LogWidget", None, -1)
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("LogWidget", "Logs", None, -1)
        )
        self.addLogButton.setText(
            QtWidgets.QApplication.translate("LogWidget", "Add Log", None, -1)
        )
