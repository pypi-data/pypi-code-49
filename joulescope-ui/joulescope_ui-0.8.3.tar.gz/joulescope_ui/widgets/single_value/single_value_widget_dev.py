# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'single_value_widget_dev.ui'
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
        Form.resize(387, 76)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.fieldLabel = QLabel(self.widget)
        self.fieldLabel.setObjectName(u"fieldLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fieldLabel)

        self.fieldComboBox = QComboBox(self.widget)
        self.fieldComboBox.addItem("")
        self.fieldComboBox.addItem("")
        self.fieldComboBox.addItem("")
        self.fieldComboBox.addItem("")
        self.fieldComboBox.setObjectName(u"fieldComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fieldComboBox)

        self.statisticLabel = QLabel(self.widget)
        self.statisticLabel.setObjectName(u"statisticLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.statisticLabel)

        self.statisticComboBox = QComboBox(self.widget)
        self.statisticComboBox.addItem("")
        self.statisticComboBox.addItem("")
        self.statisticComboBox.addItem("")
        self.statisticComboBox.addItem("")
        self.statisticComboBox.addItem("")
        self.statisticComboBox.setObjectName(u"statisticComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.statisticComboBox)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(44, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget { background-color : black; }\n"
"QLabel { color : green; font-weight: bold; font-size: 32pt; }")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.valueLabel = QLabel(self.widget_2)
        self.valueLabel.setObjectName(u"valueLabel")
        self.valueLabel.setLineWidth(0)
        self.valueLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.valueLabel)

        self.unitLabel = QLabel(self.widget_2)
        self.unitLabel.setObjectName(u"unitLabel")
        self.unitLabel.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.unitLabel)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.fieldLabel.setText(QCoreApplication.translate("Form", u"Field", None))
        self.fieldComboBox.setItemText(0, QCoreApplication.translate("Form", u"Current", None))
        self.fieldComboBox.setItemText(1, QCoreApplication.translate("Form", u"Voltage", None))
        self.fieldComboBox.setItemText(2, QCoreApplication.translate("Form", u"Power", None))
        self.fieldComboBox.setItemText(3, QCoreApplication.translate("Form", u"Energy", None))

        self.statisticLabel.setText(QCoreApplication.translate("Form", u"Statistic", None))
        self.statisticComboBox.setItemText(0, QCoreApplication.translate("Form", u"mean", None))
        self.statisticComboBox.setItemText(1, QCoreApplication.translate("Form", u"standard deviation", None))
        self.statisticComboBox.setItemText(2, QCoreApplication.translate("Form", u"minimum", None))
        self.statisticComboBox.setItemText(3, QCoreApplication.translate("Form", u"maximum", None))
        self.statisticComboBox.setItemText(4, QCoreApplication.translate("Form", u"peak-to-peak", None))

        self.valueLabel.setText(QCoreApplication.translate("Form", u"0.000", None))
        self.unitLabel.setText(QCoreApplication.translate("Form", u" mA ", None))
    # retranslateUi

