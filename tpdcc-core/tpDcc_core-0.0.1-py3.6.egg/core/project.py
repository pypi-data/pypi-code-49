#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains generic functionality when dealing with projects
"""

from __future__ import print_function, division, absolute_import

import os
import logging

from tpDcc.libs import qt
from tpDcc.libs.python import path, folder, settings
from tpDcc.core import consts

LOGGER = logging.getLogger()


class ProjectData(object):
    def __init__(self, name, project_path, settings, options):
        self._name = name
        self._project_path = project_path
        self._settings = settings
        self._options = options

    def get_name(self):
        return self._name

    def get_path(self):
        return self._project_path

    def get_full_path(self):
        return path.join_path(self._project_path, self._name)

    def get_settings(self):
        return self._settings

    def get_options(self):
        return self._options

    name = property(get_name)
    project_path = property(get_path)
    full_path = property(get_full_path)
    settings = property(get_settings)
    options = property(get_options)

    def get_project_file(self):
        """
        Returns path where project file is located
        :return: str
        """

        return path.join_path(self.full_path, consts.PROJECTS_NAME)

    def get_options_file(self):
        """
        Returns path where project options file is located
        :return:
        """

        self._setup_options()

        return self.options.get_file()

    def has_options(self):
        """
        Returns whether the project has options or not
        :return: bool
        """

        self._setup_options()

        return self.options.has_settings()

    def has_option(self, name, group=None):
        """
        Returns whether the project has given option or not
        :param name: str, name of the option
        :param group: variant, str || None, group of the option (optional)
        :return: bool
        """

        self._setup_options()

        if group:
            name = '{}.{}'.format(group, name)
        else:
            name = str(name)

        return self.options.has_setting(name)

    def add_option(self, name, value, group=None, option_type=None):
        """
        Adds a new option to the project options file
        :param name: str, name of the option
        :param value: variant, value of the option
        :param group: variant, str || None, group of the option (optional)
        :param option_type: variant, str || None, option type (optional)
        """

        self._setup_options()

        if group:
            name = '{}.{}'.format(group, name)
        else:
            name = str(name)

        if option_type == 'script':
            value = [value, 'script']

        self.options.set(name, value)

    def set_option(self, name, value, group=None):
        """
        Set an option of the option settings file. If the option does not exist, it will be created
        :param name: str, name of the option we want to set
        :param value: variant, value of the option
        :param group: variant, str || None, group of the option (optional)
        """

        if group:
            name = '{}.{}'.format(group, name)
        else:
            name = str(name)

        self.options.set(name, value)

    def get_unformatted_option(self, name, group=None):
        """
        Returns option without format (string format)
        :param name: str, name of the option we want to retrieve
        :param group: variant, str || None, group of the option (optional)
        :return: str
        """

        self._setup_options()

        if group:
            name = '{}.{}'.format(group, name)
        else:
            name = str(name)

        value = self.options.get(name)

        return value

    def get_option(self, name, group=None):
        """
        Returns option value with proper format (to force string use get_unformatted_option function)
        :param name: str, name of the option we want to retrieve
        :param group: variant, str || None, group of the option (optional)
        :return: variante
        """

        self._setup_options()

        value = self.get_unformatted_option(name, group)
        new_value = None

        try:
            new_value = eval(value)
        except Exception:
            pass

        if value is None:
            LOGGER.warning('Impossible to access option with proper format from {}'.format(self.options.directory))
            if group:
                LOGGER.warning('Could not find option: "{}" in group: "{}"'.format(name, group))
            else:
                LOGGER.warning('Could not find option: {}'.format(name))

        if type(new_value) == list or type(new_value) == tuple or type(new_value) == dict:
            value = new_value
        if type(value) == str or type(value) == unicode:
            if value.find(',') > -1:
                value = value.split(',')

        LOGGER.debug('Accessed Project Option - Option: "{}" | Group: "{}" | Value: "{}"'.format(name, group, value))

        return value

    def get_option_match(self, name, return_first=True):
        self._setup_options()
        options_dict = self.options.settings_dict
        found = dict()
        for key in options_dict:
            if key.endswith(name):
                if return_first:
                    LOGGER.debug('Accessed - Option: {}, value: {}'.format(name, options_dict[key]))
                found[name] = options_dict[key]

        return found

    def get_options(self):
        """
        Returns all optiosn contained in the settings file
        :return: str
        """

        self._setup_options()
        options = list()
        if self.options:
            options = self.options.get_settings()

        return options

    def clear_options(self):
        """
        Clears all the options of the task
        """

        if self.options:
            self.options.clear()

    def get_project_image(self):
        """
        Returns the image used by the project
        :return: QPixmap
        """

        from tpDcc.libs.qt.core import image

        if not self._settings:
            self._load_project()

        project_file = self.get_project_file()
        if not self._settings.has_settings():
            LOGGER.warning('No valid project data found on Project Data File: {}'.format(project_file))

        encoded_image = self._settings.get('image')
        if not encoded_image:
            return

        encoded_image = encoded_image.encode('utf-8')
        return QPixmap.fromImage(image.base64_to_image(encoded_image))

    def update_project(self):

        if not self._settings:
            self._load_project()

        project_file = self.get_project_file()
        if not self._settings.has_settings():
            LOGGER.warning('No valid project data found on Project Data File: {}'.format(project_file))

        self._name = self._settings.get('name')
        self._project_path = path.get_dirname(path.get_dirname(project_file))

    def set_project_image(self, image_path):
        """
        Updates project image icon
        :param image_path: str, path that points to the image of the new project icon
        """

        from tpDcc.libs.qt.core import image

        if not os.path.isfile(image_path):
            LOGGER.warning('Given image path "{}" is not valid!'.format(image_path))
            return False

        if not self._settings:
            self._load_project()

        project_file = self.get_project_file()
        if not self._settings.has_settings():
            LOGGER.warning('No valid project data found on Project Data File: {}'.format(project_file))

        self._settings.set('image', image.image_to_base64(image_path))

        return True

    def create_project(self):
        project_full_path = self.full_path
        if path.is_dir(project_full_path):
            LOGGER.warning('Project Path {} already exists! Choose another one ...'.format(project_full_path))
            return

        folder.create_folder(name=self.name, directory=self.project_path)
        self._set_default_settings()

        return self

    def create_folder(self, name, relative_path=None):
        if relative_path is None:
            folder.create_folder(name=name, directory=self.full_path)
        else:
            folder.create_folder(name=name, directory=path.join_path(self.full_path, relative_path))
    # endregion

    # region Private Functions
    def _load_project(self):
        self._set_default_settings()
        self._setup_options()

    def _set_settings_path(self, folder_path):
        if not self._settings:
            self._load_project()

        project_file_path = self.get_project_file()
        project_file = path.get_basename(project_file_path)
        self._settings.set_directory(folder_path, project_file)

    def _set_options_path(self, folder_path):
        if not self._options:
            self._load_project()

        self._options.set_directory(folder_path, 'options.json')

    def _set_default_settings(self):

        from tpDcc.libs.qt.core import image

        project_file_path = self.get_project_file()
        project_path = path.get_dirname(project_file_path)
        self._settings = settings.JSONSettings()
        self._set_settings_path(project_path)
        self._settings.set('version', '0.0.0')
        self._settings.set('name', self.name)
        self._settings.set('path', self.project_path)
        self._settings.set('full_path', self.full_path)
        self._settings.set('image', image.image_to_base64(qt.resource.get('icons', 'rignode_icon') + '.png'))

    def _setup_options(self):

        if not self._options:
            self._options = settings.JSONSettings()

        self._options.set_directory(os.path.dirname(self.get_project_file()), 'options.json')
