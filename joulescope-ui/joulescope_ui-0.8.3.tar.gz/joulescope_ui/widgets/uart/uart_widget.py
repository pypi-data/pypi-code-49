# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uart_widget.ui'
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
        Form.resize(652, 515)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(False)

        self.verticalLayout.addWidget(self.textBrowser)

        self.textEntryWidget = QWidget(Form)
        self.textEntryWidget.setObjectName(u"textEntryWidget")
        self.horizontalLayout = QHBoxLayout(self.textEntryWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.textEntryWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.configButton = QPushButton(self.textEntryWidget)
        self.configButton.setObjectName(u"configButton")

        self.horizontalLayout.addWidget(self.configButton)


        self.verticalLayout.addWidget(self.textEntryWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.configButton.setText(QCoreApplication.translate("Form", u"Configure", None))
    # retranslateUi

