import stat
import sys
import errno
import re
from PyInquirer import prompt

import sys
import glob
import tempfile
import os
from shutil import copytree, ignore_patterns, copy

import subprocess

TEMPLATE_PATH = os.path.join(
    tempfile.gettempdir(), 'framework-templates', 'python')
TEMPLATE_REPO_URL = 'https://bitbucket.org/We-Kan-Code/python-backend-framework.git'
TEMPLATE_REPO_BRANCH = 'master'

COMMANDS = ['', 'echo "..."', 'python -m venv venv', 'echo "..."', 'venv/bin/pip3 install wheel',
            'venv/bin/pip3 install -r requirements.txt']


def git(*args):
    return subprocess.check_call(['git'] + list(args))


def get_repo():
    if os.path.isdir(TEMPLATE_PATH):
        git('-C', TEMPLATE_PATH, 'pull')
    else:
        git('clone', TEMPLATE_REPO_URL, TEMPLATE_PATH, '-b', TEMPLATE_REPO_BRANCH)


def dir_copy(source_path, destination_path):
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    copy(source_path, destination_path)


def create_project(answers):
    PROJECT_NAME = answers['project_name']
    PROJECT_DESTINATION = os.path.abspath(answers['project_destination'])

    destination = os.path.join(PROJECT_DESTINATION, PROJECT_NAME)

    if os.path.exists(destination):
        print('ERROR: Destination already contains a folder with the name ' + PROJECT_NAME)
        print('Exiting ...')
        sys.exit(1)

    get_repo()

    copytree(TEMPLATE_PATH, destination,
             ignore=ignore_patterns('.git', 'templates'))
    os.mkdir(os.path.join(destination, 'storage', 'logs'))

    COMMANDS[0] = 'cd ' + destination
    if os.name == 'nt':
        COMMANDS[3] = '.\\venv\\scripts\\activate.bat'
        COMMANDS[4] = 'pip install wheel'
        COMMANDS[5] = 'pip install -r requirements.txt'
    os.system(" && ".join(COMMANDS))


def create_file(module_path, model_name, file_type):
    template_file = os.path.join(
        TEMPLATE_PATH, 'templates', file_type + '.pyt')
    template_write_file = os.path.join(
        TEMPLATE_PATH, 'templates', file_type + 'w.pyt')

    dir_name = file_type
    if file_type != 'schema':
        dir_name += 's'

    model_name_lower = model_name.lower()

    destination = os.path.join(module_path, model_name_lower,
                               dir_name, model_name_lower + '.py')

    if os.path.exists(destination):
        print('ERROR: Destination already contains a module')
        print('Exiting ...')
        sys.exit(1)

    with open(template_file) as file:
        s = file.read()
        s = s.replace('%model_upper%', model_name.capitalize())
        s = s.replace('%model_lower%', model_name.lower())
        s = s.replace('%model_caps%', model_name.upper())
    with open(template_write_file, "w") as file:
        file.write(s)

    dir_copy(template_write_file, destination)


def create_module(answers):
    model_name = answers['model_name']
    project_root = os.path.abspath(answers['project_root'])

    if os.path.exists(os.path.join(project_root, model_name, 'src')):
        print(project_root + ' not found')
        sys.exit(1)

    get_repo()

    create_file(os.path.join(project_root, 'src', 'app'), model_name, 'model')
    create_file(os.path.join(project_root, 'src', 'app'),
                model_name, 'controller')
    create_file(os.path.join(project_root, 'src', 'app'),
                model_name, 'service')
    create_file(os.path.join(project_root, 'src', 'app'), model_name, 'schema')


def create_module_without_model(answers):
    """"""
    name = answers['name']
    project_root = os.path.abspath(answers['project_root'])

    if os.path.exists(os.path.join(project_root, name, 'src')):
        print(project_root + ' not found')
        sys.exit(1)

    get_repo()

    create_file(os.path.join(project_root, 'src', 'app'),
                name, 'controller')
    create_file(os.path.join(project_root, 'src', 'app'),
                name, 'service')


def main():
    try:
        questions = [
            {
                'type': 'list',
                'name': 'generator_choice',
                'message': 'Select one of the options below to start',
                'choices': [
                    'New project',
                    'New module (Model + Schema + Controller + Service)',
                    'New module (Controller + Service)'
                ],
            }
        ]

        answers = prompt(questions)

        if answers['generator_choice'] == 'New project':
            project_generator_questions = [
                {
                    'type': 'input',
                    'name': 'project_name',
                    'message': 'Project name:',
                    'validate': lambda input: True if input and re.match(
                        '^[A-Za-z0-9_-]*$',
                        input
                    )
                    else 'Project name may only include letters, numbers, underscores and hashes.'
                },
                {
                    'type': 'input',
                    'name': 'project_destination',
                    'message': 'Project destination:',
                }
            ]
            answers = prompt(project_generator_questions)
            create_project(answers)
        elif answers['generator_choice'] == 'New module (Model + Schema + Controller + Service)':
            model_generator_questions = [
                {
                    'type': 'input',
                    'name': 'model_name',
                    'message': 'Model name:',
                    'validate': lambda input: True if input and re.match(
                        '^[A-Za-z0-9_-]*$',
                        input
                    )
                    else 'Model name may only include letters, numbers, underscores and hashes.'
                },
                {
                    'type': 'input',
                    'name': 'project_root',
                    'message': 'Project root:',
                }
            ]
            answers = prompt(model_generator_questions)
            create_module(answers)
        else:
            generator_questions = [
                {
                    'type': 'input',
                    'name': 'name',
                    'message': 'Controller name:',
                    'validate': lambda input: True if input and re.match(
                        '^[A-Za-z0-9_-]*$',
                        input
                    )
                    else 'Controller name may only include letters, numbers, underscores and hashes.'
                },
                {
                    'type': 'input',
                    'name': 'project_root',
                    'message': 'Project root:',
                }
            ]
            answers = prompt(generator_questions)
            create_module_without_model(answers)
    except KeyError:
        sys.exit(1)


if __name__ == '__main__':
    main()
