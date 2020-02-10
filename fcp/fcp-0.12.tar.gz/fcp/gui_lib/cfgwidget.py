# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cfgwidget.ui',
# licensing of 'cfgwidget.ui' applies.
#
# Created: Sat Dec  7 20:50:27 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_CfgWidget(object):
    def setupUi(self, CfgWidget):
        CfgWidget.setObjectName("CfgWidget")
        CfgWidget.resize(400, 300)
        CfgWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(CfgWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(CfgWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self._CfgScrollContents = QtWidgets.QWidget()
        self._CfgScrollContents.setGeometry(QtCore.QRect(0, 0, 356, 209))
        self._CfgScrollContents.setObjectName("_CfgScrollContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._CfgScrollContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CfgScrollContents = QtWidgets.QVBoxLayout()
        self.CfgScrollContents.setObjectName("CfgScrollContents")
        self.verticalLayout_2.addLayout(self.CfgScrollContents)
        self.scrollArea.setWidget(self._CfgScrollContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.addCfgButton = QtWidgets.QPushButton(self.groupBox)
        self.addCfgButton.setObjectName("addCfgButton")
        self.verticalLayout_3.addWidget(self.addCfgButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(CfgWidget)
        QtCore.QMetaObject.connectSlotsByName(CfgWidget)

    def retranslateUi(self, CfgWidget):
        CfgWidget.setWindowTitle(
            QtWidgets.QApplication.translate("CfgWidget", "CfgWidget", None, -1)
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("CfgWidget", "Configs", None, -1)
        )
        self.addCfgButton.setText(
            QtWidgets.QApplication.translate("CfgWidget", "Add Cfg", None, -1)
        )
