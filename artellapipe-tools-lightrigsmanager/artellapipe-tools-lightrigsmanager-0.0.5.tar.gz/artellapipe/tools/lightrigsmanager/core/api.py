#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API module to work with light rigs
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import logging

from tpPyUtils import path as path_utils

import artellapipe

LOGGER = logging.getLogger()


def get_config():
    """
    Returns artellapipe-tools-lightrigsmanager configuration file
    :return: ArtellaConfiguration
    """

    tool_data = artellapipe.ToolsMgr().tools.get('artellapipe-tools-lightrigsmanager')
    config = tool_data['config']

    return config


def get_light_rigs_path(project=None, config=None):
    """
    Returns path where Light Rigs are located
    :param project:
    :param config:
    :return: str
    """

    if not project:
        project = artellapipe.project

    if not config:
        config = get_config()

    light_rigs_template_name = config.get('lightrigs_template', None)
    if not light_rigs_template_name:
        msg = 'No Light Rigs Template name defined in configuration file: "{}"'.format(config.get_path())
        LOGGER.warning(msg)
        return None
    template = artellapipe.FilesMgr().get_template(light_rigs_template_name)
    if not template:
        LOGGER.warning(
            '"{}" template is not defined in project files configuration file!'.format(light_rigs_template_name))
        return None

    template_dict = {
        'project_id': project.id,
        'project_id_number': project.id_number,
    }
    light_rigs_path = template.format(template_dict)

    project_drive = project.get_drive()
    if not light_rigs_path.startswith(project_drive):
        light_rigs_path = path_utils.clean_path(os.path.join(project_drive, light_rigs_path))

    return path_utils.clean_path(light_rigs_path)


def get_light_rig_file_type(config=None):
    """
    Returns file type used by light rigs in current project
    :param project:
    :param config:
    :return:
    """

    if not config:
        if not config:
            config = get_config()

    light_rig_file_type = config.get('lightrig_file_type', default='lightrig')

    return light_rig_file_type


def get_light_rig_file_type_instance(
        light_rig_name, light_rig_folder=None, project=None, config=None, light_rigs_path=None):

    if not light_rigs_path:
        light_rigs_path = get_light_rigs_path(project=project, config=config)
    if not light_rigs_path or not os.path.isdir(light_rigs_path):
        LOGGER.warning('Project {} has no Light Rigs!'.format(project.name.title()))
        return

    light_rig_file_type = get_light_rig_file_type(config=config)
    if not light_rig_file_type:
        LOGGER.warning('Project {} does not define a proper light rig file type!'.format(project.name.title()))
        return

    light_rig_file_class = artellapipe.FilesMgr().get_file_class(light_rig_file_type)
    if not light_rig_file_class:
        LOGGER.warning('Impossible to reference Light Rig: {} | {} | {}'.format(
            light_rig_name, light_rigs_path, light_rig_file_type))
        return None

    if not light_rig_folder:
        light_rig_folder = light_rig_name
        light_rig_name = light_rig_name.title().replace(' ', '_')

    light_rig_path = os.path.join(light_rigs_path, light_rig_folder)
    if not os.path.isdir(light_rig_path):
        LOGGER.warning('Impossible to reference Light Rig: {} | {} | {}'.format(
            light_rig_name, light_rig_path, light_rig_file_type))
        return None

    light_rig_file = light_rig_file_class(project, light_rig_name, file_path=light_rig_path)

    return light_rig_file


def open_light_rig(light_rig_name, light_rig_folder=None, project=None, config=None, light_rigs_path=None):
    """
    Opens light rig in current DCC scene
    :param light_rig_name: str
    :param light_rig_folder: str
    :param project: ArtellaProject
    :param config: ArtellaConfig
    :param light_rigs_path: str
    :return: bool
    """

    light_rig_file_inst = get_light_rig_file_type_instance(
        light_rig_name, light_rig_folder=light_rig_folder, project=project, config=config,
        light_rigs_path=light_rigs_path)
    if not light_rig_file_inst:
        return False

    return light_rig_file_inst.open_file()


def import_light_rig(light_rig_name, light_rig_folder=None, project=None, config=None, light_rigs_path=None):
    """
    Imports light rig in current DCC scene
    :param light_rig_name: str
    :param light_rig_folder: str
    :param project: ArtellaProject
    :param config: ArtellaConfig
    :param light_rigs_path: str
    :return: bool
    """

    light_rig_file_inst = get_light_rig_file_type_instance(
        light_rig_name, light_rig_folder=light_rig_folder, project=project, config=config,
        light_rigs_path=light_rigs_path)
    if not light_rig_file_inst:
        return False

    return light_rig_file_inst.import_file()


def reference_light_rig(light_rig_name, light_rig_folder=None, project=None, config=None, light_rigs_path=None):
    """
    References light rig in current DCC scene
    :param light_rig_name: str
    :param light_rig_folder: str
    :param project: ArtellaProject
    :param config: ArtellaConfig
    :param light_rigs_path: str
    :return: bool
    """

    light_rig_file_inst = get_light_rig_file_type_instance(
        light_rig_name, light_rig_folder=light_rig_folder, project=project, config=config,
        light_rigs_path=light_rigs_path)
    if not light_rig_file_inst:
        return False

    return light_rig_file_inst.import_file(reference=True)
