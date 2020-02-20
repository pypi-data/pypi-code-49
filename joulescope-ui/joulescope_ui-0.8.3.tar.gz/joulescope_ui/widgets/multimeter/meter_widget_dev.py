# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meter_widget_dev.ui'
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

from joulescope_ui import joulescope_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(478, 681)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; font-size: 48pt; }")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; font-size: 48pt; }")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; font-size: 48pt; }")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; font-size: 48pt; }")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.updateRateLabel = QLabel(self.frame)
        self.updateRateLabel.setObjectName(u"updateRateLabel")

        self.horizontalLayout.addWidget(self.updateRateLabel)

        self.updateRateSpinBox = QSpinBox(self.frame)
        self.updateRateSpinBox.setObjectName(u"updateRateSpinBox")

        self.horizontalLayout.addWidget(self.updateRateSpinBox)

        self.hzLabel = QLabel(self.frame)
        self.hzLabel.setObjectName(u"hzLabel")

        self.horizontalLayout.addWidget(self.hzLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u" TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.updateRateLabel.setText(QCoreApplication.translate("Form", u"Update Rate", None))
        self.hzLabel.setText(QCoreApplication.translate("Form", u"Hz", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Switch to Oscillosope", None))
    # retranslateUi

