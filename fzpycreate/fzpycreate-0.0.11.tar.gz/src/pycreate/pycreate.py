#!/usr/bin/env python36
# -*- coding: utf-8 -*

"""
Summary
-------
Create empty python projects.


TODO: 1. git init commit (Done!!!)
      2. dependency configuration
"""

__author__ = ['fzhao']

import argparse
import os
import subprocess


file_path = os.path.dirname(__file__)
current_path = os.getcwd()


def write_readme(path, project_name):
    """
    write README.md file.

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    f = open(os.path.join(path, project_name, "README.md"), 'w')
    f.write("#{}".format(project_name))
    f.close()


def write_setup(path, project_name):
    """
    write setup.py file
    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    f = open(os.path.join(path, project_name, "setup.py"), 'w')
    with open(os.path.join(file_path, "setup.txt")) as read_setup:
        setup = read_setup.read()
        setup = setup.replace('{name}', project_name)
        f.write(setup)
    f.close()

    f1 = open(os.path.join(path, project_name, "setup.cfg"), 'w')
    with open(os.path.join(file_path, "setup_conf.txt")) as read_setup:
        setup = read_setup.read()
        setup = setup.replace('{1}', project_name)
        f1.write(setup)
    f1.close()


def write_manifest(path, project_name):
    """
    write MANIFEST.in file.

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name

    Notes
    -----
    A MANIFEST.in is needed in certain cases where you need to package
    additional files
    """
    f = open(os.path.join(path, project_name, "MANIFEST.in"), 'w')
    manifest = """
include README.md
include CHANGELOG
include LICENCE.md.txt
include requirement.ini

recursive-include bin *.txt *.py
recursive-include src/{} *.txt *.py
graft tests
    """
    manifest = manifest.replace('{}', project_name)
    f.write(manifest)
    f.close()


def write_licence(path, project_name):
    """
    write MANIFEST.in file

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    license_txt = """{} license
==================
Belonging to Fan Zhao only

    """
    license_txt = license_txt.replace('{}', project_name)
    with open(os.path.join(path, project_name, "LICENCE.md.txt"), 'w') as f:
        f.write(license_txt)


def write_project(path, project_name):
    """
    write projects file

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    src_dir = os.path.join(path, project_name, 'src')
    if not os.path.exists(src_dir):
        os.mkdir(src_dir)
    project_dir = os.path.join(path, project_name, 'src', project_name)
    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
        with open(os.path.join(project_dir, "__init__.py"), 'w') as f:
            init = """#!/usr/bin/env python37
# -*- coding: utf-8 -*
from ._version import __version__

            """
            f.write(init)
        with open(os.path.join(project_dir, "_version.py"), 'w') as f:
            version = """
__version__= '0.0.0'

            """
            f.write(version)
        test_dir = os.path.join(path, project_name, 'tests')
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)
        with open(os.path.join(test_dir, "__init__.py"),
                  'w') as f:
            init = """"""
            f.write(init)


def write_git_ignore(path, project_name):
    """
    write projects file

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    with open(os.path.join(path, project_name, ".gitignore"), 'w') as f:
        git_ignore = """*.py[cod]

#------------------
# C extensions
#------------------
*.so

#------------------
# Packages
#------------------
*.egg
*.egg-info
dist
build
eggs
parts
var
sdist
develop-eggs
.installed.cfg
lib
lib64
__pycache__

#------------------
# Installer logs
#------------------
pip-log.txt

#------------------
# Unit test / coverage reports
#------------------
.coverage
.tox
nosetests.xml

#------------------
# Translations
#------------------
*.mo
#------------------
# Mr Developer
#------------------
.mr.developer.cfg
.project
.pydevproject

#------------------
# Temp files
#------------------
*~
#------------------
# Pipy codes
#------------------
.pypirc

#------------------
# Vim files
#------------------
.swp
.swo

#------------------
# pycharm
#------------------
.idea/*

#------------------
# virtualenv
#------------------
env/*

#------------------
# notebook
#------------------
notebook/*
notes/*
notebooks/*

#------------------
# requirements
#------------------
requirement.txt

"""
        f.write(git_ignore)


def write_tox(path, project_name):
    """
    write projects file

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    with open(os.path.join(path, project_name, "tox.ini"), 'w') as f:
        tox = """[flake8]
ignore = E402, W503, W504

[tox]
envlist = py37

[testenv]
deps = flake8
       nose
       pylint
       coverage
commands=
    nosetests src/ tests/
    flake8 src/ tests/
"""
        f.write(tox)


def write_bin(path, project_name):
    """
    create bin folder

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    os.mkdir(os.path.join(path, project_name, 'bin'))
    with open(os.path.join(path, project_name, 'bin', "__init__.py"), 'w')\
            as f:
        init = """#!/usr/bin/env python36
# -*- coding: utf-8 -*
from ._version import __version__

"""
        f.write(init)


def write_requirement(path, project_name):
    """
    write requirement.ini file

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    with open(os.path.join(path, project_name, "requirement.ini"), 'w') as f:
        requirement = """
"""
        f.write(requirement)


def write_changelog(path, project_name):
    """
    write requirement.ini file

    Parameters
    ----------
    path : str
        project path

    project_name : str
        project name
    """
    with open(os.path.join(path, project_name, "CHANGELOG"), 'w') as f:
        changelog = """0.0.1 (30/09/2019)
------------------

    """
        f.write(changelog)


def main():
    parser = argparse.ArgumentParser(
        description='Handle python create projects.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--create', dest='name', action='store',
                        default=None,
                        help='create new virtual env with the NAME')

    parser.add_argument('-g', '--git', dest='enable_git', action='store_true',
                        help='Initialize git')

    parser.add_argument('--compile', dest='compile_name', action='store',
                        default=None, help='compile dependency.')

    parser.add_argument('-e', '--venv', dest='env', action='store',
                        default=None, help="create virtual environment.")

    results = parser.parse_args()

    if results.name is not None:
        projects_path = os.path.join(current_path, results.name)
        if not os.path.exists(projects_path):
            os.mkdir(projects_path)
            write_readme(current_path, results.name)
            write_setup(current_path, results.name)
            write_manifest(current_path, results.name)
            write_licence(current_path, results.name)
            write_project(current_path, results.name)
            write_bin(current_path, results.name)
            write_requirement(current_path, results.name)
            write_tox(current_path, results.name)
            write_changelog(current_path, results.name)
            print("""Create new projects.""".format(results.name))
        else:
            print("Path exists. Cannot create new projects.")
    if results.enable_git and results.name is not None:
        projects_path = os.path.join(current_path, results.name)
        if os.path.exists(projects_path):
            write_git_ignore(current_path, results.name)
            os.chdir(projects_path)
            subprocess.check_output(['git', 'init'])
            subprocess.check_output(['git', 'add', './'])
            subprocess.check_output(['git', 'commit', '-m', '\"init commit\"'])
            print("init git.")

    if results.compile_name is not None:
        subprocess.check_output(['pip-compile', results.compile_name])

    if results.env is not None:
        subprocess.check_output(['sh', os.path.join(file_path, "pip.sh"),
                                 results.env])

    return None


if __name__ == '__main__':
    main()
