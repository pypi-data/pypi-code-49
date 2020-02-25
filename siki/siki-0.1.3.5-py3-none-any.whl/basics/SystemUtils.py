# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 08, 2018
# Modifi: May 08, 2018

import platform
import sys

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

def distribution_info():
    return """Python version: %s
    dist: %s
    linux_distribution: %s
    system: %s
    machine: %s
    platform: %s
    uname: %s
    version: %s
    mac_ver: %s
    """ % (
    sys.version.split('\n'),
    str(platform.dist()),
    linux_distribution(),
    platform.system(),
    platform.machine(),
    platform.platform(),
    platform.uname(),
    platform.version(),
    platform.mac_ver())

def is_windows():
    return 'Windows' == platform.system()

def is_linux():
    return 'Linux' == platform.system()

def is_darwin():
    return 'Darwin' == platform.system()