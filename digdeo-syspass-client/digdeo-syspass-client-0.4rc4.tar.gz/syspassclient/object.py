#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of SysPass Client
#
# Copyright (C) 2020  DigDeo SAS
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


import logging


class Object(object):

    def __init__(self):
        self.__verbose = True
        self.__verbose_level = 0
        self.__debug = False
        self.__debug_level = 0

        self.verbose = True
        self.verbose_level = 0
        self.debug = False
        self.debug_level = 0

        self.logger = logging.getLogger('SyspassClient')
        self.logger.setLevel('INFO')
        f_handler = logging.FileHandler('/tmp/syspassclient.log')
        f_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        # while self.logger.handlers:
        #     self.logger.handlers.pop()
        self.logger.addHandler(f_handler)

    @property
    def verbose(self):
        """
        Get if the verbose information's is display to the screen.

        :return: True if verbose mode is enable, False for disable it.
        :rtype: bool
        """
        return bool(self.__verbose)

    @verbose.setter
    def verbose(self, verbose):
        """
        Set if the verbose information's display on the screen.

        Generally it highly stress the console and is here for future maintenance of that Application.

        Enjoy future dev it found it function ;)

        :param verbose: True is verbose mode is enable, False for disable it.
        :type verbose: bool
        :raise TypeError: when "verbose" argument is not a :py:data:`bool`
        """
        # Exit as soon of possible
        if type(verbose) != bool:
            raise TypeError("'verbose' must be a bool type")

        # make the job in case
        if self.verbose != bool(verbose):
            self.__verbose = bool(verbose)

    @property
    def verbose_level(self):
        """
        Get the verbose information's level to display on the screen.

        Range: 0 to 3

        See: Object.set_verbose_level() for more information's about effect of ``debug_level``

        :return: The debug level as set with MorseDecoder.set_debug_level()
        :rtype: int
        """
        return self.__verbose_level

    @verbose_level.setter
    def verbose_level(self, verbose_level):
        """
        Set the verbose level of information'ss display on the screen.

        Generally it highly stress the console and is here for future maintenance of that Application.

        Enjoy future dev it found it function ;)

        :param verbose_level: The Debug level to set
        :type verbose_level: int
        :raise TypeError: when "verbose_level" argument is not a :py:data:`int`
        """
        # Exit as soon of possible
        if type(verbose_level) != int:
            raise TypeError("'verbose_level' must be a int type")

        # make the job in case
        if self.verbose_level != verbose_level:
            self.__verbose_level = verbose_level

    @property
    def debug(self):
        """
        Get the debugging information's level to display on the screen.

        :return: True if debugging mode is enable, False for disable it.
        :rtype: bool
        """
        return bool(self.__debug)

    @debug.setter
    def debug(self, debug):
        """
        Set the debugging level of information'ss display on the screen.

        Generally it highly stress the console and is here for future maintenance of that Application.

        Enjoy future dev it found it function ;)

        :param debug: True is debugging mode is enable, False for disable it.
        :type debug: bool
        :raise TypeError: when "debug" argument is not a :py:data:`bool`
        """
        # Exit as soon of possible
        if type(debug) != bool:
            raise TypeError("'debug' must be a bool type")

        # make the job in case
        if self.debug != bool(debug):
            self.__debug = bool(debug)

    @property
    def debug_level(self):
        """
        Get the debugging information's level to display on the screen.

        Range: 0 to 3

        See: MorseDecoder.set_debug_level() for more information's about effect of ``debug_level``

        :return: The debug level as set with MorseDecoder.set_debug_level()
        :rtype: int
        """
        return self.__debug_level

    @debug_level.setter
    def debug_level(self, debug_level):
        """
        Set the debugging level of information'ss display on the screen.

        Generally it highly stress the console and is here for future maintenance of that Application.

        Enjoy future dev it found it function ;)

        :param debug_level: The Debug level to set
        :type debug_level: int
        :raise TypeError: when "debug_level" argument is not a :py:data:`int`
        """
        # Exit as soon of possible
        if type(debug_level) != int:
            raise TypeError("'debug_level' must be a int type")

        # make the job in case
        if self.debug_level != debug_level:
            self.__debug_level = debug_level
