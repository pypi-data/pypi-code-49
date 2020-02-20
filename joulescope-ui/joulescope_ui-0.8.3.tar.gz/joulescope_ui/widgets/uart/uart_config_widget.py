# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uart_config_widget.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 201)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.portLabel = QLabel(Form)
        self.portLabel.setObjectName(u"portLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.portLabel)

        self.portComboBox = QComboBox(Form)
        self.portComboBox.setObjectName(u"portComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.portComboBox)

        self.baudRateComboBox = QComboBox(Form)
        self.baudRateComboBox.setObjectName(u"baudRateComboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.baudRateComboBox)

        self.parityComboBox = QComboBox(Form)
        self.parityComboBox.setObjectName(u"parityComboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.parityComboBox)

        self.stopBitsComboBox = QComboBox(Form)
        self.stopBitsComboBox.setObjectName(u"stopBitsComboBox")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.stopBitsComboBox)

        self.baudRateLabel = QLabel(Form)
        self.baudRateLabel.setObjectName(u"baudRateLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.baudRateLabel)

        self.parityLabel = QLabel(Form)
        self.parityLabel.setObjectName(u"parityLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.parityLabel)

        self.stopBitsLabel = QLabel(Form)
        self.stopBitsLabel.setObjectName(u"stopBitsLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.stopBitsLabel)

        self.statusLabel = QLabel(Form)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setStyleSheet(u"QLabel {color: red; }")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.statusLabel)

        self.controlWidget = QWidget(Form)
        self.controlWidget.setObjectName(u"controlWidget")
        self.horizontalLayout = QHBoxLayout(self.controlWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(self.controlWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.okButton = QPushButton(self.controlWidget)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)


        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.controlWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.portLabel.setText(QCoreApplication.translate("Form", u"Port", None))
        self.baudRateLabel.setText(QCoreApplication.translate("Form", u"Baud rate", None))
        self.parityLabel.setText(QCoreApplication.translate("Form", u"Parity", None))
        self.stopBitsLabel.setText(QCoreApplication.translate("Form", u"Stop bits", None))
        self.statusLabel.setText("")
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.okButton.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

