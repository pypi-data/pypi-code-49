# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devicedetails.ui',
# licensing of 'devicedetails.ui' applies.
#
# Created: Sun Nov  3 00:30:05 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_DeviceDetails(object):
    def setupUi(self, DeviceDetails):
        DeviceDetails.setObjectName("DeviceDetails")
        DeviceDetails.resize(398, 382)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DeviceDetails)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(DeviceDetails)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
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
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.messageContents = QtWidgets.QWidget()
        self.messageContents.setGeometry(QtCore.QRect(0, 0, 334, 192))
        self.messageContents.setObjectName("messageContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.messageContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.messageContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cmdsButton = QtWidgets.QPushButton(self.groupBox)
        self.cmdsButton.setCheckable(True)
        self.cmdsButton.setObjectName("cmdsButton")
        self.horizontalLayout_5.addWidget(self.cmdsButton)
        self.cfgsButton = QtWidgets.QPushButton(self.groupBox)
        self.cfgsButton.setCheckable(True)
        self.cfgsButton.setObjectName("cfgsButton")
        self.horizontalLayout_5.addWidget(self.cfgsButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addButton = QtWidgets.QPushButton(self.groupBox)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_4.addWidget(self.addButton)
        self.deleteDeviceButton = QtWidgets.QPushButton(self.groupBox)
        self.deleteDeviceButton.setObjectName("deleteDeviceButton")
        self.horizontalLayout_4.addWidget(self.deleteDeviceButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.cfgDetails = QtWidgets.QVBoxLayout()
        self.cfgDetails.setObjectName("cfgDetails")
        self.horizontalLayout_3.addLayout(self.cfgDetails)
        self.cmdDetails = QtWidgets.QVBoxLayout()
        self.cmdDetails.setObjectName("cmdDetails")
        self.horizontalLayout_3.addLayout(self.cmdDetails)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(DeviceDetails)
        QtCore.QMetaObject.connectSlotsByName(DeviceDetails)

    def retranslateUi(self, DeviceDetails):
        DeviceDetails.setWindowTitle(
            QtWidgets.QApplication.translate("DeviceDetails", "DeviceDetails", None, -1)
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("DeviceDetails", "Device", None, -1)
        )
        self.nameLabel.setText(
            QtWidgets.QApplication.translate("DeviceDetails", "name", None, -1)
        )
        self.idLabel.setText(
            QtWidgets.QApplication.translate("DeviceDetails", "id", None, -1)
        )
        self.cmdsButton.setText(
            QtWidgets.QApplication.translate("DeviceDetails", "Cmds", None, -1)
        )
        self.cfgsButton.setText(
            QtWidgets.QApplication.translate("DeviceDetails", "Cfgs", None, -1)
        )
        self.addButton.setText(
            QtWidgets.QApplication.translate("DeviceDetails", "Add", None, -1)
        )
        self.deleteDeviceButton.setText(
            QtWidgets.QApplication.translate("DeviceDetails", "Delete", None, -1)
        )
