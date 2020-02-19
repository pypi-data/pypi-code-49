#!/usr/bin/env python37
# -*- coding: utf-8 -*
""""
create setup file.
"""

import os
import subprocess

from glob import glob
from distutils.cmd import Command
from setuptools import setup
from src.pycreate._version import __version__

package_name = 'fzpycreate'


def versions():
    return __version__


def get_git_revision_hash():
    git_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    return git_hash.strip()


def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])


def increase_version():
    file_path = os.path.dirname(__file__)
    with open(os.path.join(file_path, 'src', package_name, '_version.py'),
              'w') as f:
        version_context = """#!/usr/bin python37
# -*- coding: utf-8 -*
__version__ = '{}'
"""
        new_version = versions()
        new_versions = new_version.split('.')
        new_versions[-1] = str(int(new_versions[-1]) + 1)
        new_version = '.'.join(new_versions)
        version_context = version_context.replace('{}', new_version)
        f.write(version_context)


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


class IncreaseVersionsCommand(Command):
    """Custom build command."""
    user_options = [
        # The format is (long option, short option, description).
        ('test=', None, 'just test'),
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.test = ''

    def finalize_options(self):
        pass

    def run(self):
        increase_version()


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
      version=versions(),
      python_requires='>=3',
      install_requires=parse_requirements(),
      entry_points={
          'console_scripts': [
              'pycreate = pycreate.pycreate:main',]
                    },
      # package source directory
      tests_require=['flake8==3.6.0', 'nose==1.3.7', 'pylint==2.2.2',
                     'coverage==4.5.2'],
      test_suite='nose.collector',
      cmdclass={
          'idist': IncreaseVersionsCommand,
          }
      )
