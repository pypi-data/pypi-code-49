# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'max_window_config_widget.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(368, 123)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.signal = QComboBox(Dialog)
        self.signal.setObjectName(u"signal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.signal)

        self.time_len = QDoubleSpinBox(Dialog)
        self.time_len.setObjectName(u"time_len")
        self.time_len.setDecimals(5)
        self.time_len.setMinimum(0.000010000000000)
        self.time_len.setMaximum(1000.000000000000000)
        self.time_len.setSingleStep(0.100000000000000)
        self.time_len.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.time_len)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Max Window configuration", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Width of window (in seconds)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Signal", None))
    # retranslateUi

