#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QDialog, QVBoxLayout, QShortcut, QApplication
from mkedit.core.widgets import PreView
from PySide2.QtGui import QKeySequence
from PySide2.QtCore import QSize, Qt


class PrewViewDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.mainLayout = QVBoxLayout(self)
        self.preView = PreView(self)
        self.mainLayout.addWidget(self.preView)
        self.setLayout(self.mainLayout)
        desktop = QApplication.desktop()
        size = QSize()
        size.setHeight(int(desktop.height() * 0.95))
        size.setWidth(int(desktop.height() * 0.95))
        self.setFixedSize(size)
        shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_P), self)
        shortcut.activated.connect(self.closePreView)

    def closePreView(self):
        self.close()

    def setPreHtml(self, html):
        self.preView.setPreContent(html)
        self.show()
