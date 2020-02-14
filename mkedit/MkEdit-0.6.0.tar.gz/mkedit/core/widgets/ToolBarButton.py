#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QPushButton
import qtawesome as qta


class ToolBarButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)

    def setAwesomeIcon(self, iconName):
        icon = qta.icon(iconName,
                        active=iconName,
                        color='gray',
                        color_active='blue')
        self.setIcon(icon)


class ToolBarMenuInfo:
    def __init__(self, id: str = None, icon: str = None, shortcut: str = None, separator: bool = False, callBack=None):
        self.id = id
        self.icon = icon
        self.shortcut = shortcut
        self.separator = separator
        self.callBack = callBack
