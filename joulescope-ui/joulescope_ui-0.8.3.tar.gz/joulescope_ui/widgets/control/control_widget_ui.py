# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_widget_ui.ui'
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

class Ui_ControlWidget(object):
    def setupUi(self, ControlWidget):
        if ControlWidget.objectName():
            ControlWidget.setObjectName(u"ControlWidget")
        ControlWidget.resize(754, 480)
        self.horizontalLayout = QHBoxLayout(ControlWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.playButton = QPushButton(ControlWidget)
        self.playButton.setObjectName(u"playButton")
        icon = QIcon()
        icon.addFile(u":/joulescope/resources/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setCheckable(True)
        self.playButton.setFlat(True)

        self.horizontalLayout.addWidget(self.playButton)

        self.recordButton = QPushButton(ControlWidget)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u":/joulescope/resources/record.png", QSize(), QIcon.Normal, QIcon.Off)
        self.recordButton.setIcon(icon1)
        self.recordButton.setCheckable(True)
        self.recordButton.setFlat(True)

        self.horizontalLayout.addWidget(self.recordButton)

        self.iRangeLabel = QLabel(ControlWidget)
        self.iRangeLabel.setObjectName(u"iRangeLabel")

        self.horizontalLayout.addWidget(self.iRangeLabel)

        self.iRangeComboBox = QComboBox(ControlWidget)
        self.iRangeComboBox.setObjectName(u"iRangeComboBox")

        self.horizontalLayout.addWidget(self.iRangeComboBox)

        self.vRangeLabel = QLabel(ControlWidget)
        self.vRangeLabel.setObjectName(u"vRangeLabel")

        self.horizontalLayout.addWidget(self.vRangeLabel)

        self.vRangeComboBox = QComboBox(ControlWidget)
        self.vRangeComboBox.setObjectName(u"vRangeComboBox")

        self.horizontalLayout.addWidget(self.vRangeComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.energyNameLabel = QLabel(ControlWidget)
        self.energyNameLabel.setObjectName(u"energyNameLabel")

        self.horizontalLayout.addWidget(self.energyNameLabel)

        self.energyValueLabel = QLabel(ControlWidget)
        self.energyValueLabel.setObjectName(u"energyValueLabel")
        font = QFont()
        font.setPointSize(12)
        self.energyValueLabel.setFont(font)

        self.horizontalLayout.addWidget(self.energyValueLabel)


        self.retranslateUi(ControlWidget)

        QMetaObject.connectSlotsByName(ControlWidget)
    # setupUi

    def retranslateUi(self, ControlWidget):
#if QT_CONFIG(tooltip)
        self.playButton.setToolTip(QCoreApplication.translate("ControlWidget", u"Enable to capture data from the selected Joulescope.  Disable to stop/pause capture.", None))
#endif // QT_CONFIG(tooltip)
        self.playButton.setText("")
#if QT_CONFIG(tooltip)
        self.recordButton.setToolTip(QCoreApplication.translate("ControlWidget", u"Click once to start recording capture Joulescope data to a file.  Click again to stop the capture.  Only new data is recorded.", None))
#endif // QT_CONFIG(tooltip)
        self.recordButton.setText("")
        self.iRangeLabel.setText(QCoreApplication.translate("ControlWidget", u"Current Range", None))
#if QT_CONFIG(tooltip)
        self.iRangeComboBox.setToolTip(QCoreApplication.translate("ControlWidget", u"Select the Joulescope current range.  \"Auto\" allows Joulescope to dynamical adjust the current range.", None))
#endif // QT_CONFIG(tooltip)
        self.vRangeLabel.setText(QCoreApplication.translate("ControlWidget", u"Voltage Range", None))
#if QT_CONFIG(tooltip)
        self.vRangeComboBox.setToolTip(QCoreApplication.translate("ControlWidget", u"The voltage range.  No autoranging option exists.", None))
#endif // QT_CONFIG(tooltip)
        self.energyNameLabel.setText(QCoreApplication.translate("ControlWidget", u"Energy", None))
        self.energyValueLabel.setText(QCoreApplication.translate("ControlWidget", u"0 J", None))
    # retranslateUi

