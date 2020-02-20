# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/joulescope/resources/icon_64x64.ico", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.actionExit = QAction(mainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDeveloper = QAction(mainWindow)
        self.actionDeveloper.setObjectName(u"actionDeveloper")
        self.actionDeveloper.setCheckable(True)
        self.actionDisable = QAction(mainWindow)
        self.actionDisable.setObjectName(u"actionDisable")
        self.actionPlay = QAction(mainWindow)
        self.actionPlay.setObjectName(u"actionPlay")
        self.actionStop = QAction(mainWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.actionRecord = QAction(mainWindow)
        self.actionRecord.setObjectName(u"actionRecord")
        self.actionOpen = QAction(mainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(mainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionPreferences = QAction(mainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionAbout = QAction(mainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionUsbInrush = QAction(mainWindow)
        self.actionUsbInrush.setObjectName(u"actionUsbInrush")
        self.actionSave = QAction(mainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionClearEnergy = QAction(mainWindow)
        self.actionClearEnergy.setObjectName(u"actionClearEnergy")
        self.actionCredits = QAction(mainWindow)
        self.actionCredits.setObjectName(u"actionCredits")
        self.actionGettingStarted = QAction(mainWindow)
        self.actionGettingStarted.setObjectName(u"actionGettingStarted")
        self.actionUsersGuide = QAction(mainWindow)
        self.actionUsersGuide.setObjectName(u"actionUsersGuide")
        self.actionViewLogs = QAction(mainWindow)
        self.actionViewLogs.setObjectName(u"actionViewLogs")
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuDevice = QMenu(self.menubar)
        self.menuDevice.setObjectName(u"menuDevice")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDevice.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionGettingStarted)
        self.menuHelp.addAction(self.actionUsersGuide)
        self.menuHelp.addAction(self.actionViewLogs)
        self.menuHelp.addAction(self.actionCredits)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionClearEnergy)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Joulescope", None))
        self.actionExit.setText(QCoreApplication.translate("mainWindow", u"E&xit", None))
        self.actionExit.setIconText(QCoreApplication.translate("mainWindow", u"Exit", None))
        self.actionDeveloper.setText(QCoreApplication.translate("mainWindow", u"Developer", None))
        self.actionDisable.setText(QCoreApplication.translate("mainWindow", u"Disable", None))
        self.actionPlay.setText(QCoreApplication.translate("mainWindow", u"Play", None))
        self.actionStop.setText(QCoreApplication.translate("mainWindow", u"Stop", None))
        self.actionRecord.setText(QCoreApplication.translate("mainWindow", u"Record", None))
        self.actionOpen.setText(QCoreApplication.translate("mainWindow", u"&Open", None))
        self.actionClose.setText(QCoreApplication.translate("mainWindow", u"&Close", None))
        self.actionPreferences.setText(QCoreApplication.translate("mainWindow", u"Preferences", None))
        self.actionAbout.setText(QCoreApplication.translate("mainWindow", u"&About", None))
        self.actionUsbInrush.setText(QCoreApplication.translate("mainWindow", u"USB Inrush", None))
        self.actionSave.setText(QCoreApplication.translate("mainWindow", u"&Save", None))
        self.actionClearEnergy.setText(QCoreApplication.translate("mainWindow", u"Clear &Energy", None))
        self.actionCredits.setText(QCoreApplication.translate("mainWindow", u"Credits", None))
        self.actionGettingStarted.setText(QCoreApplication.translate("mainWindow", u"Getting Started", None))
        self.actionUsersGuide.setText(QCoreApplication.translate("mainWindow", u"User's Guide", None))
        self.actionViewLogs.setText(QCoreApplication.translate("mainWindow", u"View logs...", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"&File", None))
        self.menuView.setTitle(QCoreApplication.translate("mainWindow", u"&View", None))
        self.menuDevice.setTitle(QCoreApplication.translate("mainWindow", u"&Device", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mainWindow", u"&Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("mainWindow", u"&Tools", None))
    # retranslateUi

