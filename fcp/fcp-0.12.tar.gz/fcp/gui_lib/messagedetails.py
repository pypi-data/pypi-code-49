# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messagedetails.ui',
# licensing of 'messagedetails.ui' applies.
#
# Created: Sun Nov  3 00:30:06 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MessageDetails(object):
    def setupUi(self, MessageDetails):
        MessageDetails.setObjectName("MessageDetails")
        MessageDetails.resize(419, 283)
        self.verticalLayout = QtWidgets.QVBoxLayout(MessageDetails)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(MessageDetails)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.idLabel = QtWidgets.QLabel(self.groupBox)
        self.idLabel.setObjectName("idLabel")
        self.horizontalLayout_2.addWidget(self.idLabel)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idEdit.setObjectName("idEdit")
        self.horizontalLayout_2.addWidget(self.idEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dlcLabel = QtWidgets.QLabel(self.groupBox)
        self.dlcLabel.setObjectName("dlcLabel")
        self.horizontalLayout_3.addWidget(self.dlcLabel)
        self.dlcEdit = QtWidgets.QLineEdit(self.groupBox)
        self.dlcEdit.setObjectName("dlcEdit")
        self.horizontalLayout_3.addWidget(self.dlcEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frequencyLabel = QtWidgets.QLabel(self.groupBox)
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.horizontalLayout_4.addWidget(self.frequencyLabel)
        self.frequencyEdit = QtWidgets.QLineEdit(self.groupBox)
        self.frequencyEdit.setObjectName("frequencyEdit")
        self.horizontalLayout_4.addWidget(self.frequencyEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.signalContents = QtWidgets.QWidget()
        self.signalContents.setGeometry(QtCore.QRect(0, 0, 375, 66))
        self.signalContents.setObjectName("signalContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.signalContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.signalContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addButton = QtWidgets.QPushButton(self.groupBox)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_5.addWidget(self.addButton)
        self.deleteMessageButton = QtWidgets.QPushButton(self.groupBox)
        self.deleteMessageButton.setObjectName("deleteMessageButton")
        self.horizontalLayout_5.addWidget(self.deleteMessageButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(MessageDetails)
        QtCore.QMetaObject.connectSlotsByName(MessageDetails)

    def retranslateUi(self, MessageDetails):
        MessageDetails.setWindowTitle(
            QtWidgets.QApplication.translate(
                "MessageDetails", "MessageDetails", None, -1
            )
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("MessageDetails", "Message", None, -1)
        )
        self.nameLabel.setText(
            QtWidgets.QApplication.translate("MessageDetails", "name", None, -1)
        )
        self.idLabel.setText(
            QtWidgets.QApplication.translate("MessageDetails", "id", None, -1)
        )
        self.dlcLabel.setText(
            QtWidgets.QApplication.translate("MessageDetails", "dlc", None, -1)
        )
        self.frequencyLabel.setText(
            QtWidgets.QApplication.translate("MessageDetails", "frequency", None, -1)
        )
        self.addButton.setText(
            QtWidgets.QApplication.translate("MessageDetails", "Add", None, -1)
        )
        self.deleteMessageButton.setText(
            QtWidgets.QApplication.translate("MessageDetails", "Delete", None, -1)
        )
