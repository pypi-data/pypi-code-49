# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signalwidget.ui',
# licensing of 'signalwidget.ui' applies.
#
# Created: Sun Nov  3 00:30:06 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_SignalWidget(object):
    def setupUi(self, SignalWidget):
        SignalWidget.setObjectName("SignalWidget")
        SignalWidget.resize(270, 52)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SignalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(SignalWidget)
        self.name.setText("")
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.start = QtWidgets.QLabel(SignalWidget)
        self.start.setText("")
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.length = QtWidgets.QLabel(SignalWidget)
        self.length.setText("")
        self.length.setObjectName("length")
        self.horizontalLayout.addWidget(self.length)
        self.signalDetailsButton = QtWidgets.QPushButton(SignalWidget)
        self.signalDetailsButton.setCheckable(True)
        self.signalDetailsButton.setObjectName("signalDetailsButton")
        self.horizontalLayout.addWidget(self.signalDetailsButton)

        self.retranslateUi(SignalWidget)
        QtCore.QMetaObject.connectSlotsByName(SignalWidget)

    def retranslateUi(self, SignalWidget):
        SignalWidget.setWindowTitle(
            QtWidgets.QApplication.translate("SignalWidget", "SignalWidget", None, -1)
        )
        self.signalDetailsButton.setText(
            QtWidgets.QApplication.translate("SignalWidget", "Details", None, -1)
        )
