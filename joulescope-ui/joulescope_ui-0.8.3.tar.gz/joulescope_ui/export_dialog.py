# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_dialog.ui'
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
        Form.resize(644, 313)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.filenameLabel = QLabel(self.frame)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.filenameLabel)

        self.filenameWidget = QWidget(self.frame)
        self.filenameWidget.setObjectName(u"filenameWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.filenameWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.filenameLineEdit = QLineEdit(self.filenameWidget)
        self.filenameLineEdit.setObjectName(u"filenameLineEdit")

        self.horizontalLayout_2.addWidget(self.filenameLineEdit)

        self.filenameSelectButton = QPushButton(self.filenameWidget)
        self.filenameSelectButton.setObjectName(u"filenameSelectButton")

        self.horizontalLayout_2.addWidget(self.filenameSelectButton)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.filenameWidget)

        self.contentsWidget = QWidget(self.frame)
        self.contentsWidget.setObjectName(u"contentsWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.contentsWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.contentsWidget)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.closeWidget = QWidget(Form)
        self.closeWidget.setObjectName(u"closeWidget")
        self.horizontalLayout = QHBoxLayout(self.closeWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closeSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.closeSpacer)

        self.cancelButton = QPushButton(self.closeWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(self.closeWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.saveButton)


        self.verticalLayout.addWidget(self.closeWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.filenameLabel.setText(QCoreApplication.translate("Form", u"Filename", None))
        self.filenameSelectButton.setText(QCoreApplication.translate("Form", u"Choose", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

