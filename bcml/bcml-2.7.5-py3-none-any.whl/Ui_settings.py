# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\macad\Documents\Git\BCML-2\.vscode\settings.ui',
# licensing of 'c:\Users\macad\Documents\Git\BCML-2\.vscode\settings.ui' applies.
#
# Created: Tue Oct  1 11:32:50 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(333, 248)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SettingsDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtCemu = QtWidgets.QLineEdit(SettingsDialog)
        self.txtCemu.setObjectName("txtCemu")
        self.horizontalLayout.addWidget(self.txtCemu)
        self.btnBrowseCemu = QtWidgets.QPushButton(SettingsDialog)
        self.btnBrowseCemu.setStyleSheet("padding: 4px 8px;")
        self.btnBrowseCemu.setObjectName("btnBrowseCemu")
        self.horizontalLayout.addWidget(self.btnBrowseCemu)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(SettingsDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtGameDump = QtWidgets.QLineEdit(SettingsDialog)
        self.txtGameDump.setObjectName("txtGameDump")
        self.horizontalLayout_2.addWidget(self.txtGameDump)
        self.btnBrowseGame = QtWidgets.QPushButton(SettingsDialog)
        self.btnBrowseGame.setStyleSheet("padding: 4px 8px;")
        self.btnBrowseGame.setObjectName("btnBrowseGame")
        self.horizontalLayout_2.addWidget(self.btnBrowseGame)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(SettingsDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtMlc = QtWidgets.QLineEdit(SettingsDialog)
        self.txtMlc.setObjectName("txtMlc")
        self.horizontalLayout_3.addWidget(self.txtMlc)
        self.btnBrowseMlc = QtWidgets.QPushButton(SettingsDialog)
        self.btnBrowseMlc.setStyleSheet("padding: 4px 8px;")
        self.btnBrowseMlc.setObjectName("btnBrowseMlc")
        self.horizontalLayout_3.addWidget(self.btnBrowseMlc)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(SettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.drpLang = QtWidgets.QComboBox(SettingsDialog)
        self.drpLang.setObjectName("drpLang")
        self.horizontalLayout_4.addWidget(self.drpLang)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.chkDark = QtWidgets.QCheckBox(SettingsDialog)
        self.chkDark.setObjectName("chkDark")
        self.verticalLayout.addWidget(self.chkDark)
        self.chkGuessMerge = QtWidgets.QCheckBox(SettingsDialog)
        self.chkGuessMerge.setObjectName("chkGuessMerge")
        self.verticalLayout.addWidget(self.chkGuessMerge)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtWidgets.QApplication.translate("SettingsDialog", "Settings", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SettingsDialog", "Cemu Directory", None, -1))
        self.btnBrowseCemu.setText(QtWidgets.QApplication.translate("SettingsDialog", "Browse...", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("SettingsDialog", "Game Dump Directory", None, -1))
        self.btnBrowseGame.setText(QtWidgets.QApplication.translate("SettingsDialog", "Browse...", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("SettingsDialog", "MLC Directory", None, -1))
        self.btnBrowseMlc.setText(QtWidgets.QApplication.translate("SettingsDialog", "Browse...", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("SettingsDialog", "Game Language", None, -1))
        self.chkDark.setText(QtWidgets.QApplication.translate("SettingsDialog", "Use dark theme", None, -1))
        self.chkGuessMerge.setText(QtWidgets.QApplication.translate("SettingsDialog", "Estimate RSTB values for merged files", None, -1))

