# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmddetails.ui',
# licensing of 'cmddetails.ui' applies.
#
# Created: Sun Nov  3 00:30:04 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_CmdDetails(object):
    def setupUi(self, CmdDetails):
        CmdDetails.setObjectName("CmdDetails")
        CmdDetails.resize(462, 428)
        CmdDetails.setMinimumSize(QtCore.QSize(300, 0))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(CmdDetails)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(CmdDetails)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.commentLabel = QtWidgets.QLabel(self.groupBox)
        self.commentLabel.setObjectName("commentLabel")
        self.horizontalLayout_3.addWidget(self.commentLabel)
        self.commentEdit = QtWidgets.QLineEdit(self.groupBox)
        self.commentEdit.setObjectName("commentEdit")
        self.horizontalLayout_3.addWidget(self.commentEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.n_argsLabel = QtWidgets.QLabel(self.groupBox)
        self.n_argsLabel.setObjectName("n_argsLabel")
        self.horizontalLayout_2.addWidget(self.n_argsLabel)
        self.n_argsEdit = QtWidgets.QLineEdit(self.groupBox)
        self.n_argsEdit.setObjectName("n_argsEdit")
        self.horizontalLayout_2.addWidget(self.n_argsEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.idLabel = QtWidgets.QLabel(self.groupBox)
        self.idLabel.setObjectName("idLabel")
        self.horizontalLayout_4.addWidget(self.idLabel)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idEdit.setObjectName("idEdit")
        self.horizontalLayout_4.addWidget(self.idEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self._CmdArgContents = QtWidgets.QWidget()
        self._CmdArgContents.setGeometry(QtCore.QRect(0, 0, 408, 182))
        self._CmdArgContents.setObjectName("_CmdArgContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self._CmdArgContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.CmdArgContents = QtWidgets.QVBoxLayout()
        self.CmdArgContents.setObjectName("CmdArgContents")
        self.verticalLayout_3.addLayout(self.CmdArgContents)
        self.scrollArea.setWidget(self._CmdArgContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.addArgButton = QtWidgets.QPushButton(self.groupBox)
        self.addArgButton.setObjectName("addArgButton")
        self.verticalLayout.addWidget(self.addArgButton)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.deleteCmdButton = QtWidgets.QPushButton(self.groupBox)
        self.deleteCmdButton.setObjectName("deleteCmdButton")
        self.verticalLayout_4.addWidget(self.deleteCmdButton)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.argDetailsLayout = QtWidgets.QVBoxLayout()
        self.argDetailsLayout.setObjectName("argDetailsLayout")
        self.horizontalLayout_5.addLayout(self.argDetailsLayout)

        self.retranslateUi(CmdDetails)
        QtCore.QMetaObject.connectSlotsByName(CmdDetails)

    def retranslateUi(self, CmdDetails):
        CmdDetails.setWindowTitle(
            QtWidgets.QApplication.translate("CmdDetails", "CmdDetails", None, -1)
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("CmdDetails", "Command", None, -1)
        )
        self.nameLabel.setText(
            QtWidgets.QApplication.translate("CmdDetails", "name", None, -1)
        )
        self.commentLabel.setText(
            QtWidgets.QApplication.translate("CmdDetails", "comment", None, -1)
        )
        self.n_argsLabel.setText(
            QtWidgets.QApplication.translate("CmdDetails", "n_args", None, -1)
        )
        self.idLabel.setText(
            QtWidgets.QApplication.translate("CmdDetails", "id", None, -1)
        )
        self.addArgButton.setText(
            QtWidgets.QApplication.translate("CmdDetails", "Add Arg", None, -1)
        )
        self.deleteCmdButton.setText(
            QtWidgets.QApplication.translate("CmdDetails", "Delete", None, -1)
        )
