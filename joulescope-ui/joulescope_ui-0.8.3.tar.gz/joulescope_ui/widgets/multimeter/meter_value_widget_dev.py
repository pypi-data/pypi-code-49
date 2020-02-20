# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meter_value_widget_dev.ui'
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
        Form.resize(806, 127)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.valueLabel = QLabel(Form)
        self.valueLabel.setObjectName(u"valueLabel")
        self.valueLabel.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; font-size: 48pt; }")
        self.valueLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.valueLabel)

        self.unitLabel = QLabel(Form)
        self.unitLabel.setObjectName(u"unitLabel")
        self.unitLabel.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; font-size: 48pt; }")

        self.horizontalLayout.addWidget(self.unitLabel)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stdLabel = QLabel(self.frame)
        self.stdLabel.setObjectName(u"stdLabel")
        self.stdLabel.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; }")
        self.stdLabel.setLineWidth(0)

        self.gridLayout.addWidget(self.stdLabel, 0, 0, 1, 1)

        self.stdName = QLabel(self.frame)
        self.stdName.setObjectName(u"stdName")
        self.stdName.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; }")
        self.stdName.setLineWidth(0)

        self.gridLayout.addWidget(self.stdName, 0, 1, 1, 1)

        self.minLabel = QLabel(self.frame)
        self.minLabel.setObjectName(u"minLabel")
        self.minLabel.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; }")
        self.minLabel.setLineWidth(0)

        self.gridLayout.addWidget(self.minLabel, 1, 0, 1, 1)

        self.minName = QLabel(self.frame)
        self.minName.setObjectName(u"minName")
        self.minName.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; }")
        self.minName.setLineWidth(0)

        self.gridLayout.addWidget(self.minName, 1, 1, 1, 1)

        self.maxLabel = QLabel(self.frame)
        self.maxLabel.setObjectName(u"maxLabel")
        self.maxLabel.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; }")
        self.maxLabel.setLineWidth(0)

        self.gridLayout.addWidget(self.maxLabel, 2, 0, 1, 1)

        self.maxName = QLabel(self.frame)
        self.maxName.setObjectName(u"maxName")
        self.maxName.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; }")
        self.maxName.setLineWidth(0)

        self.gridLayout.addWidget(self.maxName, 2, 1, 1, 1)

        self.p2pLabel = QLabel(self.frame)
        self.p2pLabel.setObjectName(u"p2pLabel")
        self.p2pLabel.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; }")
        self.p2pLabel.setLineWidth(0)

        self.gridLayout.addWidget(self.p2pLabel, 3, 0, 1, 1)

        self.p2pName = QLabel(self.frame)
        self.p2pName.setObjectName(u"p2pName")
        self.p2pName.setStyleSheet(u"QLabel { background-color : black; color : green; font-weight: bold; }")
        self.p2pName.setLineWidth(0)

        self.gridLayout.addWidget(self.p2pName, 3, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.valueLabel.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.unitLabel.setText(QCoreApplication.translate("Form", u" mA ", None))
        self.stdLabel.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.stdName.setText(QCoreApplication.translate("Form", u" \u00b5 ", None))
        self.minLabel.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.minName.setText(QCoreApplication.translate("Form", u" min ", None))
        self.maxLabel.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.maxName.setText(QCoreApplication.translate("Form", u" max ", None))
        self.p2pLabel.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.p2pName.setText(QCoreApplication.translate("Form", u" p2p ", None))
    # retranslateUi

