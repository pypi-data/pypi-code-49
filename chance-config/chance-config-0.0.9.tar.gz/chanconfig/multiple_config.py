#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: chanconfig/multiple_config.py
# Author: Jimin Huang <huangjimin@whu.edu.cn>
# Date: 18.05.2018
from __future__ import absolute_import
import logging
import pkg_resources
import yaml

from yaml.parser import ParserError

from chanconfig import utils
from .config import ReadConfigurationError


class MultipleConfig(object):
    """Class for configurations from stdin, config files and env.
    """

    def __init__(
        self, path, package=None, arguments={}, argument_settings={}
    ):
        """Initialize class with given path and optional package name.

        Args:
            path: a str
            package: a str, default None
            arguments: (dict) command arguments
            argument_settings: (dict) as {
                key: (env_name, process_method, default)
            }
        """
        self.logger = logging.getLogger(__name__)

        if package:
            try:
                path = pkg_resources.resource_filename(package, path)
            except ImportError as error:
                self.logger.exception(error)
                raise ReadConfigurationError(path, str(error))

        try:
            with open(path) as ymlfile:
                self.dict = yaml.load(ymlfile)
        except (IOError, ParserError) as error:
            self.logger.exception(error)
            raise ReadConfigurationError(path, str(error))

        self.update(self.process_arguments(arguments))
        self.update(self.process_arguments(argument_settings))

        self.logger.info(
            'Successfully read configurations from {0}'.format(path)
        )

    def __getattr__(self, name):
        return getattr(self.dict, name)

    def __eq__(self, other):
        return self.dict == other

    def __repr__(self):
        return str(self.dict)

    def update(self, update_dict):
        """Update values from another dict

        Args:
            update_dict: a ``dict``
        """
        self.dict = utils.deep_update(self.dict, update_dict)

    def process_arguments(self, arguments):
        """Process argument settings and arguments to a dict

        Args:
            arguments: (dict) settings of specified keys

        Return:
            (dict) as {key: val}
        """
        new_val_dict = {}
        update_value = None
        for key, val in arguments.items():
            key = key.lstrip('--')
            keys = key.split('.')

            try:
                existing_value = utils.deep_find(self.dict, keys)
            except KeyError:
                existing_value = None

            try:
                update_value = utils.generate_update_value(val, existing_value)
            except AssertionError:
                update_value = val
            except Exception as e:
                self.logger.exception(e)
                self.logger.info('Set default value of {}'.format(key))
                update_value = val[2]

            new_val_dict = utils.update_dict_by_path(
                new_val_dict, keys, update_value
            )
        return new_val_dict
