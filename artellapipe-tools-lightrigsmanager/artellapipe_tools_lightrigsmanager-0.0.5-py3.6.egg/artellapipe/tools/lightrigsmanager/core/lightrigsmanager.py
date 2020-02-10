#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to manage Light Rigs
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import logging.config

from Qt.QtWidgets import *
from Qt.QtCore import *

from tpPyUtils import folder as folder_utils, path as path_utils

from tpQtLib.core import base, qtutils
from tpQtLib.widgets import splitters, stack

import artellapipe
from artellapipe.utils import resource

from artellapipe.tools.lightrigsmanager.core import api

LOGGER = logging.getLogger()


class LightRig(base.BaseWidget, object):
    def __init__(self, project, name, path, file_type, config, parent=None):

        self._project = project
        self._name = name
        self._path = path
        self._file_type = file_type
        self._config = config

        super(LightRig, self).__init__(parent=parent)

    def get_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignCenter)

        return main_layout

    def ui(self):
        super(LightRig, self).ui()

        self.setMaximumSize(QSize(120, 140))
        self.setMinimumSize(QSize(120, 140))

        self._light_btn = QPushButton()
        self._light_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        light_rig_icon = resource.ResourceManager().icon(self._name.lower(), theme='lightrigs')
        if not light_rig_icon:
            light_rig_icon = resource.ResourceManager().icon('default', theme='lightrigs')
        self._light_btn.setIcon(light_rig_icon)
        self._light_btn.setIconSize(QSize(120, 140))
        self._title_lbl = QLabel(self._name)
        self._title_lbl.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self._light_btn)
        self.main_layout.addWidget(self._title_lbl)

        self._light_menu = QMenu(self)
        open_action = QAction(resource.ResourceManager().icon('open'), 'Open Light Rig', self._light_menu)
        import_action = QAction(resource.ResourceManager().icon('import'), 'Import Light Rig', self._light_menu)
        reference_action = QAction(
            resource.ResourceManager().icon('reference'), 'Reference Light Rig', self._light_menu)
        self._light_menu.addAction(open_action)
        self._light_menu.addAction(import_action)
        self._light_menu.addAction(reference_action)

        self._light_btn.clicked.connect(self._on_reference_light_rig)
        open_action.triggered.connect(self._on_open_light_rig)
        import_action.triggered.connect(self._on_import_light_rig)
        reference_action.triggered.connect(self._on_reference_light_rig)

    def contextMenuEvent(self, event):
        self._light_menu.exec_(event.globalPos())

    @property
    def name(self):
        """
        Returns the name of the light rig
        :return: str
        """

        return self._name

    def _get_light_rig_name(self):
        """
        Returns name of the light rig
        :return: str
        """

        return self._name.title().replace(' ', '_')

    def _on_open_light_rig(self):
        """
        Internal callback function that is called when the user wants to open a light rig
        """

        if not self._path:
            LOGGER.warning('Project {} has no Light Rigs!'.format(self._project.name.title()))
            return

        light_rig_name = self._get_light_rig_name()

        return api.open_light_rig(
            light_rig_name=light_rig_name, light_rig_folder=self._name, project=self._project,
            config=self._config, light_rigs_path=self._path)

    def _on_import_light_rig(self):
        """
        Internal callback function that is called when the user wants to import a light rig
        """

        if not self._path:
            LOGGER.warning('Project {} has no Light Rigs!'.format(self._project.name.title()))
            return

        light_rig_name = self._get_light_rig_name()

        return api.import_light_rig(
            light_rig_name=light_rig_name, light_rig_folder=self._name, project=self._project,
            config=self._config, light_rigs_path=self._path)

    def _on_reference_light_rig(self):
        """
        Internal callback function that is called when the user wants to reference a light rig
        """

        if not self._path:
            LOGGER.warning('Project {} has no Light Rigs!'.format(self._project.name.title()))
            return

        light_rig_name = self._get_light_rig_name()

        return api.reference_light_rig(
            light_rig_name=light_rig_name, light_rig_folder=self._name, project=self._project,
            config=self._config, light_rigs_path=self._path)


class ArtellaLightRigManager(artellapipe.Tool, object):

    LIGHT_RIG_CLASS = LightRig

    def __init__(self, project, config):
        super(ArtellaLightRigManager, self).__init__(project=project, config=config)

    def get_light_rigs_path(self):
        """
        Returns path where Light Rigs are located
        :return: str
        """

        light_rigs_path = api.get_light_rigs_path(project=self._project, config=self._config)
        if not light_rigs_path:
            msg = 'No Light Rigs Template name defined in configuration file: "{}"'.format(self.config.get_path())
            self.show_warning_message(msg)
            return None

        return light_rigs_path

    def ui(self):
        super(ArtellaLightRigManager, self).ui()

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(0)
        self.main_layout.addLayout(buttons_layout)

        self._open_btn = QToolButton()
        self._open_btn.setIcon(resource.ResourceManager().icon('open'))
        self._sync_btn = QToolButton()
        self._sync_btn.setIcon(resource.ResourceManager().icon('sync'))
        buttons_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Fixed))
        buttons_layout.addWidget(self._open_btn)
        buttons_layout.addWidget(splitters.get_horizontal_separator_widget())
        buttons_layout.addWidget(self._sync_btn)
        buttons_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Fixed))

        self.main_layout.addLayout(splitters.SplitterLayout())

        self._stack = stack.SlidingStackedWidget()
        self.main_layout.addWidget(self._stack)

        no_lights_pixmap = resource.ResourceManager().pixmap('no_light_rigs')
        no_lights_lbl = QLabel()
        no_lights_lbl.setPixmap(no_lights_pixmap)
        no_lights_widget = QWidget()
        no_lights_layout = QHBoxLayout()
        no_lights_widget.setLayout(no_lights_layout)
        no_lights_layout.setContentsMargins(2, 2, 2, 2)
        no_lights_layout.setSpacing(2)
        no_lights_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))
        no_lights_layout.addWidget(no_lights_lbl)
        no_lights_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))
        self._stack.addWidget(no_lights_widget)

        light_rigs_widget = QWidget()
        self._light_rigs_layout = QHBoxLayout()
        light_rigs_widget.setLayout(self._light_rigs_layout)
        self._light_rigs_layout.setContentsMargins(5, 5, 5, 5)
        self._light_rigs_layout.setSpacing(5)
        self._light_rigs_layout.setAlignment(Qt.AlignCenter)
        self._stack.addWidget(light_rigs_widget)

        self._update_ui()

    def setup_signals(self):
        self._open_btn.clicked.connect(self._on_open_light_rigs_folder)
        self._sync_btn.clicked.connect(self._on_sync_light_rigs)

    def synchronize_light_rigs(self):
        """
        Synchronizes current light rigs into user computer
        """

        light_rigs_path = self.get_light_rigs_path()
        if not light_rigs_path:
            msg = 'Impossible to synchronize light rigs because its path is not defined!'
            self.show_warning_message(msg)
            LOGGER.warning(msg)
            return

        artellapipe.FilesMgr().sync_paths([light_rigs_path], recursive=True)
        self._update_ui(allow_sync=False)

    def _update_ui(self, allow_sync=True):
        light_rigs_path = self.get_light_rigs_path()
        if not light_rigs_path:
            return
        if not os.path.exists(light_rigs_path) and allow_sync:
            result = qtutils.show_question(
                None, 'Light Rigs Folder is not available!',
                'Do you want to synchronize Light Rigs Folder from Artella to your computer? \n\n{}'.format(
                    light_rigs_path))
            if result == QMessageBox.Yes:
                self.synchronize_light_rigs()
                if not os.path.exists(light_rigs_path):
                    msg = 'Was not possible to synchronize Light Rigs folder from Artella: "{}"'.format(
                        light_rigs_path)
                    self.show_warning_message(msg)
                    LOGGER.warning(msg)
                    return
            else:
                self._stack.slide_in_index(0)
                return

        qtutils.clear_layout(self._light_rigs_layout)
        light_rig_file_type = self.config.get('lightrig_file_type', default='lightrig')
        for f in os.listdir(light_rigs_path):
            light_rig = self.LIGHT_RIG_CLASS(
                project=self._project, name=f, path=light_rigs_path, file_type=light_rig_file_type, config=self._config)
            self._light_rigs_layout.addWidget(light_rig)
        self._stack.slide_in_index(1)

    def _on_open_light_rigs_folder(self):
        """
        Internal callback function that is called when the user presses the folder button
        """

        light_rigs_path = self.get_light_rigs_path()
        if light_rigs_path and os.path.exists(light_rigs_path):
            folder_utils.open_folder(light_rigs_path)
            return True
        else:
            msg = 'Light Rigs Folder "{}" does not exists!'.format(light_rigs_path)
            self.show_warning_message(msg)
            LOGGER.warning(msg)
            return False

    def _on_sync_light_rigs(self):
        """
        Internal callback function that is called when the user press Sync Lights button
        """

        self.synchronize_light_rigs()
