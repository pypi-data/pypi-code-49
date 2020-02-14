"""
A module to supply the application version

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import os
import sys

def get_version():
    """Returns the application version from a VERSION file."""
    # PYINSTALLER: data files must be bundle-aware
    version_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    version_path = os.path.join(version_path, 'VERSION')
    with open(version_path, 'rt') as version_file:
        version = version_file.read().strip()
    return version


__version__ = get_version()
