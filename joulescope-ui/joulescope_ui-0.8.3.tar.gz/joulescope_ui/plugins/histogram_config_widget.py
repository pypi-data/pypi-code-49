# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'histogram_config_widget.ui'
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
        Dialog.resize(368, 173)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.num_bins = QSpinBox(Dialog)
        self.num_bins.setObjectName(u"num_bins")
        self.num_bins.setMaximum(1000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.num_bins)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.signal = QComboBox(Dialog)
        self.signal.setObjectName(u"signal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.signal)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.normalization = QComboBox(Dialog)
        self.normalization.setObjectName(u"normalization")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.normalization)


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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Histogram configuration", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Number of bins (0 for auto)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Signal", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Histogram Type", None))
    # retranslateUi

