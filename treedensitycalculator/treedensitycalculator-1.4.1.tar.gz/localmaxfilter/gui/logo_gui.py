# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : September 2018
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
| Acknowledgements    : Translated from VIPER Tools 2.0 (UC Santa Barbara, VIPER Lab).
|                       Dar Roberts, Kerry Halligan, Philip Dennison, Kenneth Dudley, Ben Somers, Ann Crabbé
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
from qgis.PyQt.QtGui import QPixmap
from qgis.PyQt.QtWidgets import QWidget, QLabel, QHBoxLayout
from qgis.PyQt.QtCore import Qt
from localmaxfilter.resources import qInitResources
qInitResources()


class LogoWidget(QWidget):
    """ QWidget with the project's logo. To be placed above each widget/dialog. """

    def __init__(self, parent=None):
        super(LogoWidget, self).__init__(parent=parent)

        self.setContentsMargins(0, 0, 0, 0)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignHCenter)

        lumos = QLabel(self)
        lumos.setContentsMargins(0, 0, 0, 0)
        lumos.setPixmap(QPixmap(':/lumos_full'))
        layout.addWidget(lumos)

        # gent = QLabel(self)
        # gent.setContentsMargins(0, 0, 0, 0)
        # gent.setPixmap(QPixmap(':/logo_gent'))
        # layout.addWidget(gent)


def _run():
    from qgis.core import QgsApplication
    app = QgsApplication([], True)
    app.initQgis()

    z = LogoWidget()
    z.show()
    app.exec_()


if __name__ == '__main__':
    _run()
