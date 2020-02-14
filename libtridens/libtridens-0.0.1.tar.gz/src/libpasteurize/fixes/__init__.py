import sys
from lib2to3 import refactor
import importlib
import inspect
import os
import shutil
import pkgutil

def get_fixers(module, exclude=[]):
    fix_names = []
    for m_info in pkgutil.walk_packages(module.__path__, prefix=module.__package__+'.'):
        if ('fix_' in m_info.name) and (m_info.name not in exclude):
            fix_names.append(m_info.name)
    return set(fix_names)

def install_fixer(path):
    """
    Attempts to add a fixer to the fixes tree.
    """
    where = os.path.dirname(os.path.abspath(__file__))
    shutil.copy(path, where)

def uninstall_fixer(submodule):
    where = os.path.dirname(os.path.abspath(__file__))
    os.remove(os.path.join(where, submodule + '.py'))
