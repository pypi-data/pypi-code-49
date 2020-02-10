# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logdetails.ui',
# licensing of 'logdetails.ui' applies.
#
# Created: Sat Dec  7 20:52:43 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_LogDetails(object):
    def setupUi(self, LogDetails):
        LogDetails.setObjectName("LogDetails")
        LogDetails.resize(400, 300)
        LogDetails.setMinimumSize(QtCore.QSize(200, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(LogDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(LogDetails)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_2.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_2.addWidget(self.nameEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.idLabel = QtWidgets.QLabel(self.groupBox)
        self.idLabel.setObjectName("idLabel")
        self.horizontalLayout_3.addWidget(self.idLabel)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idEdit.setObjectName("idEdit")
        self.horizontalLayout_3.addWidget(self.idEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.n_argsLabel = QtWidgets.QLabel(self.groupBox)
        self.n_argsLabel.setObjectName("n_argsLabel")
        self.horizontalLayout_4.addWidget(self.n_argsLabel)
        self.n_argsEdit = QtWidgets.QLineEdit(self.groupBox)
        self.n_argsEdit.setObjectName("n_argsEdit")
        self.horizontalLayout_4.addWidget(self.n_argsEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.commentLabel = QtWidgets.QLabel(self.groupBox)
        self.commentLabel.setObjectName("commentLabel")
        self.horizontalLayout_5.addWidget(self.commentLabel)
        self.commentEdit = QtWidgets.QLineEdit(self.groupBox)
        self.commentEdit.setObjectName("commentEdit")
        self.horizontalLayout_5.addWidget(self.commentEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stringLabel = QtWidgets.QLabel(self.groupBox)
        self.stringLabel.setObjectName("stringLabel")
        self.horizontalLayout.addWidget(self.stringLabel)
        self.stringEdit = QtWidgets.QLineEdit(self.groupBox)
        self.stringEdit.setObjectName("stringEdit")
        self.horizontalLayout.addWidget(self.stringEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.logDeleteButton = QtWidgets.QPushButton(self.groupBox)
        self.logDeleteButton.setObjectName("logDeleteButton")
        self.verticalLayout_2.addWidget(self.logDeleteButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(LogDetails)
        QtCore.QMetaObject.connectSlotsByName(LogDetails)

    def retranslateUi(self, LogDetails):
        LogDetails.setWindowTitle(
            QtWidgets.QApplication.translate("LogDetails", "LogDetails", None, -1)
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("LogDetails", "Log", None, -1)
        )
        self.nameLabel.setText(
            QtWidgets.QApplication.translate("LogDetails", "name", None, -1)
        )
        self.idLabel.setText(
            QtWidgets.QApplication.translate("LogDetails", "id", None, -1)
        )
        self.n_argsLabel.setText(
            QtWidgets.QApplication.translate("LogDetails", "n_args", None, -1)
        )
        self.commentLabel.setText(
            QtWidgets.QApplication.translate("LogDetails", "comment", None, -1)
        )
        self.stringLabel.setText(
            QtWidgets.QApplication.translate("LogDetails", "string", None, -1)
        )
        self.logDeleteButton.setText(
            QtWidgets.QApplication.translate("LogDetails", "Delete", None, -1)
        )
