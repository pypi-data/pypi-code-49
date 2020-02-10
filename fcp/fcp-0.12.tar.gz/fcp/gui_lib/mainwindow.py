# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QUrl,
    Qt,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(390, 317)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionValidate = QAction(MainWindow)
        self.actionValidate.setObjectName(u"actionValidate")
        self.actionLogs = QAction(MainWindow)
        self.actionLogs.setObjectName(u"actionLogs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(400, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget()
        self.scrollAreaContents.setObjectName(u"scrollAreaContents")
        self.scrollAreaContents.setGeometry(QRect(0, 0, 336, 195))
        self.verticalLayout = QVBoxLayout(self.scrollAreaContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_2.addWidget(self.addButton)

        self.logsButton = QPushButton(self.centralwidget)
        self.logsButton.setObjectName(u"logsButton")
        self.logsButton.setMaximumSize(QSize(400, 16777215))
        self.logsButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.logsButton)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.logDetailsLayout = QVBoxLayout()
        self.logDetailsLayout.setObjectName(u"logDetailsLayout")

        self.horizontalLayout.addLayout(self.logDetailsLayout)

        self.deviceDetailsLayout = QVBoxLayout()
        self.deviceDetailsLayout.setObjectName(u"deviceDetailsLayout")

        self.horizontalLayout.addLayout(self.deviceDetailsLayout)

        self.messageDetailsLayout = QVBoxLayout()
        self.messageDetailsLayout.setObjectName(u"messageDetailsLayout")

        self.horizontalLayout.addLayout(self.messageDetailsLayout)

        self.signalDetailsLayout = QVBoxLayout()
        self.signalDetailsLayout.setObjectName(u"signalDetailsLayout")

        self.horizontalLayout.addLayout(self.signalDetailsLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 390, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionValidate)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionValidate.setText(
            QCoreApplication.translate("MainWindow", u"Validate", None)
        )
        self.actionLogs.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.logsButton.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))

    # retranslateUi
