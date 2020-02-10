# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messagewidget.ui',
# licensing of 'messagewidget.ui' applies.
#
# Created: Sun Nov  3 00:30:06 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MessageWidget(object):
    def setupUi(self, MessageWidget):
        MessageWidget.setObjectName("MessageWidget")
        MessageWidget.resize(268, 41)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MessageWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(MessageWidget)
        self.name.setText("")
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.id = QtWidgets.QLabel(MessageWidget)
        self.id.setText("")
        self.id.setObjectName("id")
        self.horizontalLayout.addWidget(self.id)
        self.dlc = QtWidgets.QLabel(MessageWidget)
        self.dlc.setText("")
        self.dlc.setObjectName("dlc")
        self.horizontalLayout.addWidget(self.dlc)
        self.frequency = QtWidgets.QLabel(MessageWidget)
        self.frequency.setText("")
        self.frequency.setObjectName("frequency")
        self.horizontalLayout.addWidget(self.frequency)
        self.messageDetailsButton = QtWidgets.QPushButton(MessageWidget)
        self.messageDetailsButton.setCheckable(True)
        self.messageDetailsButton.setObjectName("messageDetailsButton")
        self.horizontalLayout.addWidget(self.messageDetailsButton)

        self.retranslateUi(MessageWidget)
        QtCore.QMetaObject.connectSlotsByName(MessageWidget)

    def retranslateUi(self, MessageWidget):
        MessageWidget.setWindowTitle(
            QtWidgets.QApplication.translate("MessageWidget", "MessageWidget", None, -1)
        )
        self.messageDetailsButton.setText(
            QtWidgets.QApplication.translate("MessageWidget", "Details", None, -1)
        )
