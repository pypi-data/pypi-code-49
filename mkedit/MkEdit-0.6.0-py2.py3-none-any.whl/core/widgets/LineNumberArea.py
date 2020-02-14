#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QWidget,QStyle


class LineNumberArea(QWidget):

    def __init__(self, scriptEditor):
        super(LineNumberArea, self).__init__(scriptEditor)

        self.scriptEditor = scriptEditor
        self.setStyleSheet("text-align: center;")

    def paintEvent(self, event):
        self.scriptEditor.lineNumberAreaPaintEvent(event)
        return
