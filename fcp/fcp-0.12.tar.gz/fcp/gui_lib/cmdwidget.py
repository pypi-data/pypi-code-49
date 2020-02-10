# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmdwidget.ui',
# licensing of 'cmdwidget.ui' applies.
#
# Created: Sun Nov  3 00:30:05 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_CmdWidget(object):
    def setupUi(self, CmdWidget):
        CmdWidget.setObjectName("CmdWidget")
        CmdWidget.resize(400, 300)
        CmdWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(CmdWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(CmdWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self._CmdScrollContents = QtWidgets.QWidget()
        self._CmdScrollContents.setGeometry(QtCore.QRect(0, 0, 356, 209))
        self._CmdScrollContents.setMinimumSize(QtCore.QSize(300, 0))
        self._CmdScrollContents.setObjectName("_CmdScrollContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._CmdScrollContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CmdScrollContents = QtWidgets.QVBoxLayout()
        self.CmdScrollContents.setObjectName("CmdScrollContents")
        self.verticalLayout_2.addLayout(self.CmdScrollContents)
        self.scrollArea.setWidget(self._CmdScrollContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.addCmdButton = QtWidgets.QPushButton(self.groupBox)
        self.addCmdButton.setObjectName("addCmdButton")
        self.verticalLayout_4.addWidget(self.addCmdButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(CmdWidget)
        QtCore.QMetaObject.connectSlotsByName(CmdWidget)

    def retranslateUi(self, CmdWidget):
        CmdWidget.setWindowTitle(
            QtWidgets.QApplication.translate("CmdWidget", "CmdWidget", None, -1)
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("CmdWidget", "Commands", None, -1)
        )
        self.addCmdButton.setText(
            QtWidgets.QApplication.translate("CmdWidget", "Add Cmd", None, -1)
        )
