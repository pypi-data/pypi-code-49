# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gpio_widget_ui.ui'
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


class Ui_GpioWidget(object):
    def setupUi(self, GpioWidget):
        if GpioWidget.objectName():
            GpioWidget.setObjectName(u"GpioWidget")
        GpioWidget.resize(666, 34)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GpioWidget.sizePolicy().hasHeightForWidth())
        GpioWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(GpioWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input1CheckBox = QCheckBox(GpioWidget)
        self.input1CheckBox.setObjectName(u"input1CheckBox")

        self.horizontalLayout.addWidget(self.input1CheckBox)

        self.input1Label = QLabel(GpioWidget)
        self.input1Label.setObjectName(u"input1Label")

        self.horizontalLayout.addWidget(self.input1Label)

        self.label = QLabel(GpioWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(10, 0))

        self.horizontalLayout.addWidget(self.label)

        self.input0CheckBox = QCheckBox(GpioWidget)
        self.input0CheckBox.setObjectName(u"input0CheckBox")

        self.horizontalLayout.addWidget(self.input0CheckBox)

        self.input0Label = QLabel(GpioWidget)
        self.input0Label.setObjectName(u"input0Label")

        self.horizontalLayout.addWidget(self.input0Label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.output1Button = QPushButton(GpioWidget)
        self.output1Button.setObjectName(u"output1Button")
        self.output1Button.setStyleSheet(u"QPushButton {padding-left: 10px; padding-right: 10px;}")
        self.output1Button.setCheckable(True)

        self.horizontalLayout.addWidget(self.output1Button)

        self.output0Button = QPushButton(GpioWidget)
        self.output0Button.setObjectName(u"output0Button")
        self.output0Button.setStyleSheet(u"QPushButton {padding-left: 10px; padding-right: 10px;}")
        self.output0Button.setCheckable(True)

        self.horizontalLayout.addWidget(self.output0Button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.voltageLabel = QLabel(GpioWidget)
        self.voltageLabel.setObjectName(u"voltageLabel")

        self.horizontalLayout.addWidget(self.voltageLabel)

        self.voltageComboBox = QComboBox(GpioWidget)
        self.voltageComboBox.setObjectName(u"voltageComboBox")

        self.horizontalLayout.addWidget(self.voltageComboBox)


        self.retranslateUi(GpioWidget)

        QMetaObject.connectSlotsByName(GpioWidget)
    # setupUi

    def retranslateUi(self, GpioWidget):
        GpioWidget.setWindowTitle(QCoreApplication.translate("GpioWidget", u"Form", None))
#if QT_CONFIG(tooltip)
        self.input1CheckBox.setToolTip(QCoreApplication.translate("GpioWidget", u"<html><head/><body><p>Check to enable general purpose input 1 (IN1).</p><p>When IN1 is enabled, the data overwrites the voltage least-significant bit, which reduces the resolution from 14 bits to 13 bits.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.input1CheckBox.setText(QCoreApplication.translate("GpioWidget", u"IN1", None))
#if QT_CONFIG(tooltip)
        self.input1Label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.input1Label.setText(QCoreApplication.translate("GpioWidget", u"_", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("GpioWidget", u"The IN1 signal value.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.input0CheckBox.setToolTip(QCoreApplication.translate("GpioWidget", u"<html><head/><body><p>Check to enable general purpose input 0 (IN1).</p><p>When IN0 is enabled, the data overwrites the current least-significant bit, which reduces the resolution from 14 bits to 13 bits.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.input0CheckBox.setText(QCoreApplication.translate("GpioWidget", u"IN0", None))
#if QT_CONFIG(tooltip)
        self.input0Label.setToolTip(QCoreApplication.translate("GpioWidget", u"The IN0 signal value.", None))
#endif // QT_CONFIG(tooltip)
        self.input0Label.setText(QCoreApplication.translate("GpioWidget", u"_", None))
#if QT_CONFIG(tooltip)
        self.output1Button.setToolTip(QCoreApplication.translate("GpioWidget", u"<html><head/><body><p>Toggle the output 1 (OUT1) value.</p><p>When inactive the output will be 0 V (digital low).  When pressed, the output will be the configured voltage, (digital high).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.output1Button.setText(QCoreApplication.translate("GpioWidget", u"OUT1", None))
#if QT_CONFIG(tooltip)
        self.output0Button.setToolTip(QCoreApplication.translate("GpioWidget", u"<html><head/><body><p>Toggle the output 0 (OUT0) value.</p><p>When inactive the output will be 0 V (digital low).  When pressed, the output will be the configured voltage, (digital high).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.output0Button.setText(QCoreApplication.translate("GpioWidget", u"OUT0", None))
#if QT_CONFIG(tooltip)
        self.voltageLabel.setToolTip(QCoreApplication.translate("GpioWidget", u"<html><head/><body><p>Select the general purpose input/output reference voltage.</p><p>The reference voltage determines the output signal voltage,  the logic level thresholds for the inputs, and the maximum voltage the inputs can tolerate.  </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.voltageLabel.setText(QCoreApplication.translate("GpioWidget", u"Voltage", None))
#if QT_CONFIG(tooltip)
        self.voltageComboBox.setToolTip(QCoreApplication.translate("GpioWidget", u"<html><head/><body><p>Select the general purpose input/output reference voltage.</p><p>The reference voltage determines the output signal voltage,  the logic level thresholds for the inputs, and the maximum voltage the inputs can tolerate.  </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

