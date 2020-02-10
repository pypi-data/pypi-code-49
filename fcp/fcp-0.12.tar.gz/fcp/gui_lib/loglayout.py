# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loglayout.ui',
# licensing of 'loglayout.ui' applies.
#
# Created: Sun Nov  3 00:30:05 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_LogLayout(object):
    def setupUi(self, LogLayout):
        LogLayout.setObjectName("LogLayout")
        LogLayout.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(LogLayout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(LogLayout)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.logContents = QtWidgets.QWidget()
        self.logContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.logContents.setObjectName("logContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.logContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.logContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(LogLayout)
        QtCore.QMetaObject.connectSlotsByName(LogLayout)

    def retranslateUi(self, LogLayout):
        LogLayout.setWindowTitle(
            QtWidgets.QApplication.translate("LogLayout", "LogLayout", None, -1)
        )
