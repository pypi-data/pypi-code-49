# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devicewidget.ui',
# licensing of 'devicewidget.ui' applies.
#
# Created: Sun Nov  3 00:30:05 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_DeviceWidget(object):
    def setupUi(self, DeviceWidget):
        DeviceWidget.setObjectName("DeviceWidget")
        DeviceWidget.resize(264, 41)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DeviceWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name = QtWidgets.QLabel(DeviceWidget)
        self.name.setText("")
        self.name.setObjectName("name")
        self.horizontalLayout_2.addWidget(self.name)
        self.id = QtWidgets.QLabel(DeviceWidget)
        self.id.setText("")
        self.id.setObjectName("id")
        self.horizontalLayout_2.addWidget(self.id)
        self.deviceDetailsButton = QtWidgets.QPushButton(DeviceWidget)
        self.deviceDetailsButton.setCheckable(True)
        self.deviceDetailsButton.setObjectName("deviceDetailsButton")
        self.horizontalLayout_2.addWidget(self.deviceDetailsButton)

        self.retranslateUi(DeviceWidget)
        QtCore.QMetaObject.connectSlotsByName(DeviceWidget)

    def retranslateUi(self, DeviceWidget):
        DeviceWidget.setWindowTitle(
            QtWidgets.QApplication.translate("DeviceWidget", "DeviceWidget", None, -1)
        )
        self.deviceDetailsButton.setText(
            QtWidgets.QApplication.translate("DeviceWidget", "Details", None, -1)
        )
