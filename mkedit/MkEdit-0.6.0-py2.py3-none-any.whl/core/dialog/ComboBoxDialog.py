#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton


class ComboBoxDialog(QDialog):
    def __init__(self, prent=None):
        QDialog.__init__(self, prent)
        self.init()
        self.initUI()
        self.initEvent()

    def init(self):
        self.mainLayout = QVBoxLayout()
        self.comboBox = QComboBox(self)
        self.bottomLayout = QHBoxLayout()

        self.cancel = QPushButton("cancel")
        self.ok = QPushButton('ok')
        self.result = ""

    def initUI(self):
        self.mainLayout.addWidget(self.comboBox)
        self.bottomLayout.addWidget(self.ok)
        self.bottomLayout.addWidget(self.cancel)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)

    def initEvent(self):
        self.cancel.clicked.connect(self.cancelCall)
        self.ok.clicked.connect(self.okCall)

    def initData(self, selectList: list = None):
        for item in selectList:
            self.comboBox.addItem(item)

    def cancelCall(self):
        self.reject()

    def okCall(self):
        self.result = self.comboBox.currentText()
        self.accept()
