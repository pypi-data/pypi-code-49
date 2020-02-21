# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\IanFu\Documents\github\fseutil\fseutil\gui\layout\ui\dialog_0101_adb_datasheet_1.ui',
# licensing of 'C:\Users\IanFu\Documents\github\fseutil\fseutil\gui\layout\ui\dialog_0101_adb_datasheet_1.ui' applies.
#
# Created: Mon Feb 10 17:57:50 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1613, 1153)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(5, 5, 1601, 1141))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1599, 1134))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(5, 5, 1587, 1122))
        self.label.setMinimumSize(QtCore.QSize(1587, 1122))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/adb2_datasheet_1_1587_1122.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "ADB Vol. 2 2019 Data Sheet No. 1", None, -1))

