# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cfgdetails.ui',
# licensing of 'cfgdetails.ui' applies.
#
# Created: Sat Dec  7 20:49:30 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_CfgDetails(object):
    def setupUi(self, CfgDetails):
        CfgDetails.setObjectName("CfgDetails")
        CfgDetails.resize(400, 300)
        CfgDetails.setMinimumSize(QtCore.QSize(200, 0))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CfgDetails)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(CfgDetails)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_3.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_3.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.idLabel_2 = QtWidgets.QLabel(self.groupBox)
        self.idLabel_2.setObjectName("idLabel_2")
        self.horizontalLayout_2.addWidget(self.idLabel_2)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idEdit.setObjectName("idEdit")
        self.horizontalLayout_2.addWidget(self.idEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commentLabel = QtWidgets.QLabel(self.groupBox)
        self.commentLabel.setObjectName("commentLabel")
        self.horizontalLayout.addWidget(self.commentLabel)
        self.commentEdit = QtWidgets.QLineEdit(self.groupBox)
        self.commentEdit.setObjectName("commentEdit")
        self.horizontalLayout.addWidget(self.commentEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.deleteCfgButton = QtWidgets.QPushButton(self.groupBox)
        self.deleteCfgButton.setObjectName("deleteCfgButton")
        self.verticalLayout.addWidget(self.deleteCfgButton)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(CfgDetails)
        QtCore.QMetaObject.connectSlotsByName(CfgDetails)

    def retranslateUi(self, CfgDetails):
        CfgDetails.setWindowTitle(
            QtWidgets.QApplication.translate("CfgDetails", "CfgDetails", None, -1)
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("CfgDetails", "Config", None, -1)
        )
        self.nameLabel.setText(
            QtWidgets.QApplication.translate("CfgDetails", "name", None, -1)
        )
        self.idLabel_2.setText(
            QtWidgets.QApplication.translate("CfgDetails", "id", None, -1)
        )
        self.commentLabel.setText(
            QtWidgets.QApplication.translate("CfgDetails", "comment", None, -1)
        )
        self.deleteCfgButton.setText(
            QtWidgets.QApplication.translate("CfgDetails", "Delete", None, -1)
        )
