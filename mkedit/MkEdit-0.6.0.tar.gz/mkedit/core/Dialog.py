#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QInputDialog

class Dialog:
    def inputDirNameDialog(self):
        (text, ok) = QInputDialog.getText(None, "输入框", "请输入创建文件夹名称")
        if ok and text:
            return text
        else:
            return None

    def inputFileNameDialog(self):
        (text, ok) = QInputDialog.getText(None, "输入框", "请输入创建文件名称")
        if ok and text:
            return text
        else:
            return None



