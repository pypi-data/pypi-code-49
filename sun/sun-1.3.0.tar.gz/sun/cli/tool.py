#!/usr/bin/python3
# -*- coding: utf-8 -*-

# sun is a part of sun.

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

import sys
import getpass
import subprocess
from sun.utils import fetch, os_info
from sun.__metadata__ import __version__, bin_path


def su():
    '''Display message when sun execute as root'''
    if getpass.getuser() == 'root':
        print('sun: Error: It should not be run as root')
        raise SystemExit()


def usage():
    '''SUN arguments'''
    args = [
        f'SUN (Slackware Update Notifier) - Version: {__version__}\n',
        'Usage: sun [OPTION]\n',
        'Optional arguments:',
        '  help     display this help and exit',
        '  start    start sun daemon',
        '  stop     stop sun daemon',
        '  restart  restart sun daemon',
        '  check    check for software updates',
        '  status   sun daemon status',
        '  info     Os information'
    ]
    for opt in args:
        print(opt)


def check_updates():
    '''Check and display upgraded packages'''
    packages = fetch()
    count = len(packages)
    message = 'No news is good news !'
    if count > 0:
        message = f'{count} software updates are available\n'
    return message, packages


def daemon_status():
    '''Display sun daemon status'''
    out = subprocess.getoutput('ps -a')
    message = 'SUN not running'
    if 'sun_daemon' in out:
        message = 'SUN is running...'
    return message


def _init_check_upodates():
    '''Sub function for init'''
    message, packages = check_updates()
    count = len(packages)
    if count > 0:
        print(message)
        for pkg in packages:
            print(pkg)
    else:
        print(message)


def init():
    '''Initialization , all begin from here'''
    su()
    args = sys.argv
    args.pop(0)
    cmd = f'{bin_path}sun_daemon'
    if len(args) == 1:
        if args[0] == 'start':
            print(f'Starting SUN daemon:  {cmd} &')
            subprocess.call(f'{cmd} &', shell=True)
        elif args[0] == 'stop':
            print(f'Stopping SUN daemon:  {cmd}')
            subprocess.call('killall sun_daemon', shell=True)
        elif args[0] == 'restart':
            print(f'Stopping SUN daemon:  {cmd}')
            subprocess.call('killall sun_daemon', shell=True)
            print(f'Starting SUN daemon:  {cmd} &')
            subprocess.call(f'{cmd} &', shell=True)
        elif args[0] == 'check':
            _init_check_upodates()
        elif args[0] == 'status':
            print(daemon_status())
        elif args[0] == 'help':
            usage()
        elif args[0] == 'info':
            print(os_info())
        else:
            print("try: 'sun help'")
    elif len(args) == 2 and args[0] == 'start' and args[1] == '--gtk':
        subprocess.call('sun_gtk &', shell=True)
    else:
        print("try: 'sun help'")