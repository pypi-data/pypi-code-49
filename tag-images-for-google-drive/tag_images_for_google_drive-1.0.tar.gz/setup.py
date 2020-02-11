#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import subprocess
from typing import List

from setuptools import setup, find_packages

PYTHON_VERSION = "3.7"

# Package for run
requirements: List[str] = [
    'click', 'click-pathlib',
]

setup_requirements: List[str] = ["pytest-runner", "setuptools_scm"]

# Package for tests
test_requirements: List[str] = [
    'pytest>=2.8.0',
    'pytest-openfiles',  # For tests
    'pytest-xdist',
    'pytest-mock',
    'unittest2',
]

# Package for builds
dev_requirements: List[str] = [
    'pip',
    'twine',  # To publish package in Pypi
    'sphinx', 'sphinx-execute-code', 'sphinx_rtd_theme', 'recommonmark', 'nbsphinx',  # To generate doc
    'flake8', 'pylint',  # For lint
    'PyInstaller',
    'daff',
    'mypy',
]


# Return git remote url
def _git_url() -> str:
    try:
        with open(os.devnull, "wb") as devnull:
            out = subprocess.check_output(
                ["git", "remote", "get-url", "origin"],
                cwd=".",
                universal_newlines=True,
                stderr=devnull,
            )
        return out.strip()
    except subprocess.CalledProcessError:
        # git returned error, we are not in a git repo
        return ""
    except OSError:
        # git command not found, probably
        return ""


# Return Git remote in HTTP form
def _git_http_url() -> str:
    return re.sub(r".*@(.*):(.*).git", r"http://\1/\2", _git_url())

# ------------------------
def find_dirs(dir_name):
    for dir, dirs, files in os.walk('.'):
        if dir_name in dirs:
            yield os.path.relpath(os.path.join(dir, dir_name))

# Find all of the man pages
# TODO: publish man ?
def get_man_files():
    data_files = []
    man_sections = {}
    for dir in find_dirs('man'):
        for file in os.listdir(dir):
            section = file.split('.')[-1]
            man_sections[section] = man_sections.get(section, []) + [os.path.join(dir, file)]
    for section in man_sections:
        data_files.append(('share/man/man'+section, man_sections[section]))
    return data_files

setup(
    name='tag_images_for_google_drive',
    author="Philippe PRADOS",
    author_email="github@prados.fr",
    description="Manage tags and description to be indexed by Google Drive",
    long_description=open('README.md', mode='r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url=_git_http_url(),

    license='Apache License',
    keywords="image index google drive",
    classifiers=[  # See https://pypi.org/classifiers/
        # 'Development Status :: 2 - PRE-ALPHA',
        # Before release
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved',
        'Natural Language :: English',
        'Programming Language :: Python :: ' + PYTHON_VERSION,
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='~=' + PYTHON_VERSION,
    test_suite="tests",
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    extras_require={
        'dev': dev_requirements,
        'test': test_requirements,
    },
    packages=find_packages(),
    package_data={
        "tag_images_for_google_drive": ["py.typed"],
    },
    # TODO data_files=get_man_files(),
    zip_safe=True,
    use_scm_version=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            'tag_images_for_google_drive = tag_images_for_google_drive.tag_images_for_google_drive:main'
        ]
    },
)
