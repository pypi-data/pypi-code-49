#!/usr/bin/python3
# -*- coding: utf-8 -*-

# utils.py is a part of sun.

# Copyright 2015-2020 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# sun is a tray notification applet for informing about
# package updates in Slackware.

# https://gitlab.com/dslackw/sun

# sun is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import re
import getpass
import urllib3
from sun.__metadata__ import (
    arch,
    kernel,
    pkg_path,
    conf_path,
    etc_slackpkg,
    changelog_txt,
    var_lib_slackpkg
)


def url_open(link):
    '''Return urllib urlopen'''
    try:
        http = urllib3.PoolManager()
        con = http.request('GET', link)
        r = con.data
    except urllib3.exceptions.NewConnectionError as e:
        print(e)
    except AttributeError as e:
        print(e)
    except ValueError as e:
        return e
    except KeyboardInterrupt as e:
        print(e)
        raise SystemExit()
    return r


def read_file(registry):
    '''Return reading file'''
    with open(registry, 'r', encoding='utf-8', errors='ignore') as file_txt:
        read_file = file_txt.read()
        return read_file


def slack_ver():
    '''Open a file and read the Slackware version'''
    dist = read_file('/etc/slackware-version')
    sv = re.findall(r'\d+', dist)
    if len(sv) > 2:
        version = ('.'.join(sv[:2]))
    else:
        version = ('.'.join(sv))
    return dist.split()[0], version


def installed_packages():
    '''Count installed Slackware packages'''
    for pkg in os.listdir(pkg_path):
        if not pkg.startswith('.'):
            yield pkg


def read_config(config):
    '''Read the config file and return an uncomment line'''
    for line in config.splitlines():
        line = line.lstrip()
        if line and not line.startswith('#'):
            return line
    return ''


def mirror():
    '''Get mirror from slackpkg mirrors file'''
    slack_mirror = read_config(read_file(f'{etc_slackpkg}mirrors'))
    if slack_mirror:
        return f'{slack_mirror}{changelog_txt}'
    else:
        print('\nYou do not have any mirror selected in /etc/slackpkg/mirrors'
              '\nPlease edit that file and uncomment ONE mirror.\n')
        return ''


def fetch():
    '''Get the ChangeLog.txt file size and counts the upgraded packages'''
    mir, r, slackpkg_last_date = mirror(), '', ''
    upgraded = []
    if mir:
        r = url_open(mir)
    if os.path.isfile(var_lib_slackpkg + changelog_txt):
        slackpkg_last_date = read_file('{0}{1}'.format(
            var_lib_slackpkg, changelog_txt)).split('\n', 1)[0].strip()
    else:
        return upgraded
    for line in r.splitlines():
        line = line.decode('utf-8')
        if slackpkg_last_date == line.strip():
            break
        # This condition checks the packages
        if (line.endswith('z:  Upgraded.') or line.endswith('z:  Rebuilt.') or
                line.endswith('z:  Added.') or line.endswith('z:  Removed.')):
            upgraded.append(line.split('/')[-1])
        # This condition checks the kernel
        if line.endswith('*:  Upgraded.') or line.endswith('*:  Rebuilt.'):
            upgraded.append(line)
    return upgraded


def config():
    '''Return sun configuration values'''
    conf_args = {
        'INTERVAL': 60,
        'STANDBY': 3
    }
    config_file = read_file(f'{conf_path}sun.conf')
    for line in config_file.splitlines():
        line = line.lstrip()
        if line and not line.startswith('#'):
            conf_args[line.split('=')[0]] = line.split('=')[1]
    return conf_args


def os_info():
    '''Get the OS info'''
    stype = 'Stable'
    mir = mirror()
    if mir and 'current' in mir:
        stype = 'Current'
    info = (
        f'User: {getpass.getuser()}\n'
        f'OS: {slack_ver()[0]}\n'
        f'Version: {slack_ver()[1]}\n'
        f'Type: {stype}\n'
        f'Arch: {arch}\n'
        f'Kernel: {kernel}\n'
        f'Packages: {len(list(installed_packages()))}'
        )
    return info