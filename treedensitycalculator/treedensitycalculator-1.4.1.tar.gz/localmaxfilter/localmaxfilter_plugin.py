# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------
| Date                : November 2018
| Copyright           : (C) 2018 by Tinne Cahy (Geo Solutions) and Ann Crabbé (KU Leuven)
| Email               : tinne.cahy@geosolutions.be, ann.crabbe@kuleuven.be
| Acknowledgements    : Translated from Local Maximum Filter [C++ software]
|                       Ghent University, Laboratory of Forest Management and Spatial Information Techniques
|                       Lieven P.C. Verbeke
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
| License as published by the Free Software Foundation; either version 3 of the License, or any later version.
| ----------------------------------------------------------------------------------------------------------------
"""
from os import path
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QWidget, QMenu
from functools import partial

from qgis.core import QgsApplication
from localmaxfilter.localmaxfilter_provider import LocalMaxFilterProvider
from localmaxfilter.gui.local_max_filter_gui import LocalMaxFilterWidget
from localmaxfilter.resources import qInitResources
# noinspection PyUnresolvedReferences
from processing.gui.menus import addAlgorithmEntry, removeAlgorithmEntry
qInitResources()
DEPENDENCIES = ['numpy', 'osgeo']


class LocalMaxFilterPlugin:
    """ QGIS Plugin Implementation """

    def __init__(self, iface):
        """
        :param QgsInterface iface: the interface instance which provides the hook to manipulate the QGIS GUI at run time
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = path.dirname(__file__)

        # List of actions added by this plugin
        self.actions = []

        # Add an empty menu to the Raster Menu
        self.main_menu = QMenu(title='Tree Density', parent=self.iface.rasterMenu())
        self.main_menu.setIcon(QIcon(':/lumos'))
        self.iface.rasterMenu().addMenu(self.main_menu)
        self.provider = None

    def add_action(self, icon_path: str, text: str, callback: callable, enabled_flag: bool = True,
                   status_tip: str = None, whats_this: str = None, parent: QWidget = None)->QAction:
        """ Add a toolbar item to the toolbar.

        :param icon_path: can be a resource path (e.g. ':/plugins/foo/bar.png') or a normal file system path
        :param text: text to be displayed on the menu item
        :param callback: function to be called when the action is triggered
        :param enabled_flag: flag indicating if the action should be enabled by default
        :param status_tip: optional text to show in a popup when mouse pointer hovers over the action
        :param whats_this: optional text to show in the status bar when the mouse pointer hovers over the action
        :param parent: parent widget for the new action
        :returns: The action that was created. Note that the action is also added to self.actions list
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        self.main_menu.addAction(action)
        self.actions.append(action)

        return action

    def initGui(self):
        """ Create the menu entries and toolbar icons inside the QGIS GUI """

        self.add_action(icon_path=':/lumos',
                        text='Tree Density Calculator',
                        callback=partial(self.run, 'lmf'),
                        status_tip='Tree Density Calculator based on Brightness Image',
                        parent=self.iface.mainWindow())

        self.initProcessing()

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.rasterMenu().removeAction(self.main_menu.menuAction())

        for action in self.actions:
            self.iface.removeToolBarIcon(action)

        QgsApplication.processingRegistry().removeProvider(self.provider)

    @staticmethod
    def run(name: str):
        """Run method that performs all the real work"""
        if name == 'lmf':
            widget = LocalMaxFilterWidget()
        else:
            return
        widget.show()
        widget.exec_()

    def initProcessing(self):
        self.provider = LocalMaxFilterProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)
