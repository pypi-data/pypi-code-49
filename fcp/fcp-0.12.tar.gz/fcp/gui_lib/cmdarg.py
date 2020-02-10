# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmdarg.ui',
# licensing of 'cmdarg.ui' applies.
#
# Created: Sun Nov  3 00:30:04 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_CmdArg(object):
    def setupUi(self, CmdArg):
        CmdArg.setObjectName("CmdArg")
        CmdArg.resize(400, 300)
        CmdArg.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CmdArg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(CmdArg)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.idLabel = QtWidgets.QLabel(self.groupBox)
        self.idLabel.setObjectName("idLabel")
        self.horizontalLayout_2.addWidget(self.idLabel)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idEdit.setObjectName("idEdit")
        self.horizontalLayout_2.addWidget(self.idEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.commentLabel = QtWidgets.QLabel(self.groupBox)
        self.commentLabel.setObjectName("commentLabel")
        self.horizontalLayout_3.addWidget(self.commentLabel)
        self.commentEdit = QtWidgets.QLineEdit(self.groupBox)
        self.commentEdit.setObjectName("commentEdit")
        self.horizontalLayout_3.addWidget(self.commentEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.deleteArgButton = QtWidgets.QPushButton(self.groupBox)
        self.deleteArgButton.setObjectName("deleteArgButton")
        self.verticalLayout_3.addWidget(self.deleteArgButton)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(CmdArg)
        QtCore.QMetaObject.connectSlotsByName(CmdArg)

    def retranslateUi(self, CmdArg):
        CmdArg.setWindowTitle(
            QtWidgets.QApplication.translate("CmdArg", "CmdArg", None, -1)
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("CmdArg", "Argument", None, -1)
        )
        self.idLabel.setText(QtWidgets.QApplication.translate("CmdArg", "id", None, -1))
        self.nameLabel.setText(
            QtWidgets.QApplication.translate("CmdArg", "name", None, -1)
        )
        self.commentLabel.setText(
            QtWidgets.QApplication.translate("CmdArg", "comment", None, -1)
        )
        self.deleteArgButton.setText(
            QtWidgets.QApplication.translate("CmdArg", "Delete", None, -1)
        )
