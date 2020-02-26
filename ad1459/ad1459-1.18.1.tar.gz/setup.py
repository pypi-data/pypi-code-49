#!/usr/bin/env python3

""" AD1459, an IRC Client

  Copyright ©2019-2020 by Gaven Royer

  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted, provided that the above
  copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
  TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
  FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
  ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
  SOFTWARE.

  This is the Python package.
"""

from setuptools import setup, find_packages, Command
import subprocess

prefix = '/usr/share'
rdnn_base = 'in.donotspellitgav'
rdnn = f'{rdnn_base}.Ad1459'

version = {}
with open('ad1459/__version__.py') as fp:
    exec(fp.read(), version)

with open('README.md') as readme:
    long_description = readme.read()

class Release(Command):
    """ Generate a release and push it to git."""
    description = "Generate a release and push it to git."

    user_options = [
        ('dry-run', None, 'Skip the actual release and do a dry run instead.'),
        ('prerelease=', None, 'Release this version as a "alpha", "beta" or "rc".'),
        ('force-version=', None, 'Force a specific MAJOR, MINOR, or PATCH increment.')
    ]

    def initialize_options(self):
        self.dry_run = False
        self.prerelease = None
        self.force_version = None
    
    def finalize_options(self):
        if self.force_version:
            if not self.force_version.upper() in ['MAJOR', 'MINOR', 'PATCH']:
                raise Exception(
                    f'Invalid component {self.force_version}\n'
                    'Please specify a version component to increment. Can be '
                    'MAJOR MINOR or PATCH.'
                )
        
        if self.prerelease:
            if not self.prerelease.lower() in ['alpha', 'beta', 'rc']:
                raise Exception(
                    f'Invalid prerelease {self.prerelease}\n'
                    'Please specify a prerelease type. Can be alpha beta or rc.'
                )

    def run(self):
        command = ['cz', 'bump']
        if self.dry_run:
            command.append('--dry-run')
        if self.prerelease:
            command += ['--prerelease', self.prerelease.lower()]
        if self.force_version:
            command += ['--increment', self.force_version.upper()]
        print(command)
        subprocess.run(command)
        if not self.dry_run:
            subprocess.run(
                ['git', 'push', '--follow-tags']
            )

class PyPI(Command):
    """ Generate a release to PyPI."""
    description = 'Generate a release to PyPI'
    user_options = [
        ('no-clean', None, 'Don\'t clean up the build after pushing.'),
        ('no-push', None, 'Don\'t push the release to PyPI.')
    ]

    def initialize_options(self):
        self.no_clean = False
        self.no_push = False
    
    def finalize_options(self):
        pass
    
    def run(self):
        build_command = ['python3', 'setup.py', 'sdist', 'bdist_wheel']
        subprocess.run(build_command)
        
        if not self.no_push:
            release_command = ['python3', '-m', 'twine', 'upload', 'dist/*']
            subprocess.run(release_command)
        
        if not self.no_clean:
            clean_command = ['rm', '-r', 'dist/', 'build/', 'ad1459.egg-info']
            subprocess.run(clean_command)

class GResource(Command):
    """ Generate the GResource file."""
    description = 'Generate the GResource file.'
    user_options = []

    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass

    def run(self):
        build_command = [
            'glib-compile-resources',
            '--sourcedir=data',
            '--target=ad1459/resources/in.donotspellitgav.ad1459.gresource',
            'data/in.donotspellitgav.ad1459.gresource.xml'
        ]
        subprocess.run(build_command)

setup(
    name='ad1459',
    version=version['__version__'],
    packages=find_packages(),
    scripts=['ad1459/ad1459'],

    # Dependencies
    install_requires=[
      'pydle',
      'pure-sasl',
      'keyring'
    ],

    data_files=[
      (f'{prefix}/applications', [f'data/meta/{rdnn_base}.ad1459.desktop']),
      (f'{prefix}/icons/hicolor/scalable/apps', [
          f'data/icons/{rdnn}.svg',
          f'data/icons/{rdnn}.Devel.svg'
      ]),
      (f'{prefix}/icons/hicolor/symbolic/apps', [f'data/icons/{rdnn}-symbolic.svg']),
    ],
    package_data={'ad1459': [f'resources/*.gresource']},

    # Commands
    cmdclass={
        'release': Release,
        'pypi': PyPI,
        'gresource': GResource
    },

    # Project Metadata
    author='Gaven Royer',
    author_email='gavroyer@gmail.com',
    description='An IRC Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='ad1459 irc client chat gui gtk',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications :: Gnome",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        'License :: OSI Approved :: ISC License (ISCL)',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Topic :: Communications :: Chat :: Internet Relay Chat"
    ]
)