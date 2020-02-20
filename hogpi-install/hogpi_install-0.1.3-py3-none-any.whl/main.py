import click
from PyInquirer import prompt
from subprocess import run
from pprint import pprint

from installers import ffmpeg


def get_action():
    q_get_action = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': ['Install', 'Update', 'Exit']
        }
    ]
    return prompt(q_get_action)['action']


def get_installers():
    q_get_installers = [
        {
            'type': 'checkbox',
            'name': 'installers',
            'message': 'What do you want to install?',
            'choices': [
                {
                    'name': 'ffmpeg'
                }
            ]
        }
    ]
    return prompt(q_get_installers)['installers']


def handle_installers(installers):
    for installer in installers:
        print(f'Installing {installer}')
        eval(installer).install()

@click.group()
def cli():
    pass


@click.command()
def install():
    action = get_action()
    if action == 'Install':
        installers = get_installers()
        handle_installers(installers)
    elif action == 'Update':
        run(['sudo', 'apt', 'update'])
        run(['sudo', 'apt', 'upgrade', '-y'])
    elif action == 'Exit':
        return


cli.add_command(install)

if __name__ == '__main__':
    cli()
