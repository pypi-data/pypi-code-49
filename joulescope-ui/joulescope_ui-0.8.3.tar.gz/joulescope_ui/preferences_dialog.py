# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")
        PreferencesDialog.resize(660, 388)
        PreferencesDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.profileWidget = QWidget(PreferencesDialog)
        self.profileWidget.setObjectName(u"profileWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.profileWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.profileLabel = QLabel(self.profileWidget)
        self.profileLabel.setObjectName(u"profileLabel")

        self.horizontalLayout_3.addWidget(self.profileLabel)

        self.profileComboBox = QComboBox(self.profileWidget)
        self.profileComboBox.setObjectName(u"profileComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileComboBox.sizePolicy().hasHeightForWidth())
        self.profileComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.profileComboBox)

        self.profileActivateButton = QPushButton(self.profileWidget)
        self.profileActivateButton.setObjectName(u"profileActivateButton")

        self.horizontalLayout_3.addWidget(self.profileActivateButton)

        self.profileResetButton = QPushButton(self.profileWidget)
        self.profileResetButton.setObjectName(u"profileResetButton")

        self.horizontalLayout_3.addWidget(self.profileResetButton)

        self.profileNewButton = QPushButton(self.profileWidget)
        self.profileNewButton.setObjectName(u"profileNewButton")

        self.horizontalLayout_3.addWidget(self.profileNewButton)

        self.profileHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.profileHorizontalSpacer)

        self.helpButton = QPushButton(self.profileWidget)
        self.helpButton.setObjectName(u"helpButton")

        self.horizontalLayout_3.addWidget(self.helpButton)


        self.verticalLayout.addWidget(self.profileWidget)

        self.widget = QWidget(PreferencesDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeView = QTreeView(self.widget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setAnimated(True)
        self.treeView.header().setVisible(False)

        self.horizontalLayout.addWidget(self.treeView)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.targetWidget = QWidget()
        self.targetWidget.setObjectName(u"targetWidget")
        self.targetWidget.setGeometry(QRect(0, 0, 311, 278))
        self.formLayout_2 = QFormLayout(self.targetWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.scrollArea.setWidget(self.targetWidget)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget)

        self.buttonFrame = QFrame(PreferencesDialog)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttonFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.resetButton = QPushButton(self.buttonFrame)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout_2.addWidget(self.resetButton)

        self.cancelButton = QPushButton(self.buttonFrame)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)

        self.okButton = QPushButton(self.buttonFrame)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout_2.addWidget(self.okButton)


        self.verticalLayout.addWidget(self.buttonFrame)


        self.retranslateUi(PreferencesDialog)

        QMetaObject.connectSlotsByName(PreferencesDialog)
    # setupUi

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QCoreApplication.translate("PreferencesDialog", u"Preferences", None))
        self.profileLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Profile", None))
        self.profileActivateButton.setText(QCoreApplication.translate("PreferencesDialog", u"Activate", None))
        self.profileResetButton.setText(QCoreApplication.translate("PreferencesDialog", u"Reset", None))
        self.profileNewButton.setText(QCoreApplication.translate("PreferencesDialog", u"New", None))
        self.helpButton.setText(QCoreApplication.translate("PreferencesDialog", u"Help", None))
        self.resetButton.setText(QCoreApplication.translate("PreferencesDialog", u"Reset to Defaults", None))
        self.cancelButton.setText(QCoreApplication.translate("PreferencesDialog", u"Cancel", None))
        self.okButton.setText(QCoreApplication.translate("PreferencesDialog", u"OK", None))
    # retranslateUi

