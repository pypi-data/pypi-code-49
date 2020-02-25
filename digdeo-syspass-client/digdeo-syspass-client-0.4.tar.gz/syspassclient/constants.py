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


# Inspired by: http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991


class Constants(object):
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value

    def __getattr__(self, name):
        if name not in self.__dict__:
            raise self.ConstError("No attribute %s exist" % name)
        return self.__dict__[name]


#############################
# Variables
#############################
dd = Constants()

#############################
# Internal
#############################

#########################
# ctype-style character #
#########################

# whitespace -- a string containing all ASCII whitespace
whitespace = ' \t\n\r\v\f'

# ascii_lowercase -- a string containing all ASCII lowercase letters
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

# ascii_uppercase -- a string containing all ASCII uppercase letters
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ascii_letters -- a string containing all ASCII letters
ascii_letters = ascii_lowercase + ascii_uppercase

# digits -- a string containing all ASCII decimal digits
digits = '0123456789'

# hexdigits -- a string containing all ASCII hexadecimal digits
hexdigits = digits + 'abcdef' + 'ABCDEF'

# octdigits -- a string containing all ASCII octal digits
octdigits = '01234567'

# punctuation -- a string containing all ASCII punctuation characters
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
allowed_punctuation = "-_|./?=+()[]~*{}#"

# accent
accent = "éèàùô"

dd.whitespace = whitespace
dd.ascii_lowercase = ascii_lowercase
dd.ascii_uppercase = ascii_uppercase
dd.ascii_letters = ascii_letters
dd.digits = digits
dd.hexdigits = hexdigits
dd.octdigits = octdigits
dd.punctuation = punctuation
dd.allowed_punctuation = allowed_punctuation
dd.accent = accent
dd.ascii_all = digits + ascii_letters + punctuation + whitespace + accent

dd.syspass = {
    'api': {
        'version': '3.1',
        '3.0': {
            'methods': [
                'account/search',
                'account/view',
                'account/viewPass',
                'account/editPass',
                'account/create',
                'account/edit',
                'account/delete',
                'category/search',
                'category/view',
                'category/create',
                'category/edit',
                'category/delete',
                'client/search',
                'client/view',
                'client/create',
                'client/edit',
                'client/delete',
                'tag/search',
                'tag/view',
                'tag/create',
                'tag/edit',
                'tag/delete',
                'usergroup/search',
                'usergroup/view',
                'usergroup/create',
                'usergroup/edit',
                'usergroup/delete',
                'config/backup',
                'config/export'
            ]
        },
        '3.1': {
            'methods': [
                'account/search',
                'account/view',
                'account/viewPass',
                'account/editPass',
                'account/create',
                'account/edit',
                'account/delete',
                'category/search',
                'category/view',
                'category/create',
                'category/edit',
                'category/delete',
                'client/search',
                'client/view',
                'client/create',
                'client/edit',
                'client/delete',
                'tag/search',
                'tag/view',
                'tag/create',
                'tag/edit',
                'tag/delete',
                'userGroup/search',
                'userGroup/view',
                'userGroup/create',
                'userGroup/edit',
                'userGroup/delete',
                'config/backup',
                'config/export'
            ]
        }
    }
}
