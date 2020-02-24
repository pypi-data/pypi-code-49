#!/usr/bin/env python37
# -*- coding: utf-8 -*
""""
create setup file.
"""

import os
import subprocess

from setuptools import setup

package_name = 'fzpycreate'


def get_git_revision_hash():
    git_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    return git_hash.strip()


def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])


def no_cythonize(extensions, **_ignore):
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in ('.pyx', '.py'):
                if extension.language == 'c++':
                    ext = '.cpp'
                else:
                    ext = '.c'
                sfile = path + ext
            sources.append(sfile)
        extension.sources[:] = sources
    return extensions


def parse_requirements():
    """ load requirements from a pip requirements file """
    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)
    requirements_txt_file = os.path.join(path, "requirements.txt")
    requirements_ini_file = os.path.join(path, "requirements.ini")
    if os.path.isfile(requirements_txt_file):
        lineiter = (line.strip() for line in open(requirements_txt_file))
        return [line for line in lineiter if
                line and not (line.startswith("#") or
                              line.startswith('-'))]
    elif os.path.isfile(requirements_ini_file):
        lineiter = (line.strip() for line in open(requirements_ini_file))
        return [line for line in lineiter if line
                and not (line.startswith("#") or
                         line.startswith('-'))]
    else:
        return []


extensions = []

setup(ext_modules=extensions,
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      entry_points={
          'console_scripts': [
              'pycreate = pycreate.pycreate:main',]
                    },
      )
