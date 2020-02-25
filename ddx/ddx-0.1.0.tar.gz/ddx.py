#!/usr/bin/python

"""
ddx
"""
import os
import pwd
import random
#import argparse
import subprocess

import click


@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
@click.option('--template', type=click.Choice(['base', 'djapi'], case_sensitive=False))
def new(name, template='base'):
    """ Create project directory """
    BASE_DIR = os.path.join(os.getcwd(), name)
    link = "https://github.com/ChanMo/django_boilerplate.git"

    if template == 'djapi':
        link = "https://github.com/ChanMo/djapi.git"

    subprocess.run(["git", "clone", link, name])
    os.chdir(BASE_DIR)

    user = pwd.getpwuid(os.getuid()).pw_name

    subprocess.run(["docker", "build", "--tag=django", "."])
    subprocess.run(["docker", "run", "--rm", "--mount", "type=bind,src={},target=/app".format(BASE_DIR), "django", "django-admin", "startproject", "api"])
    subprocess.run(["sudo", "chown", "{0}:{0}".format(user), ".", "-R"]) # need impro
    subprocess.run(["docker", "image", "rm", "django"])
    subprocess.run(["mv", "local.py", "api/api/local.py"])

    if template == 'djapi':
        subprocess.run(["mv", "urls.py", "api/api/urls.py"])
        subprocess.run(["mv", "accounts", "api/"])

    subprocess.run(["mv", "api-dockerfile", "api/Dockerfile"])
    subprocess.run(["mv", "requirements.txt", "api/requirements.txt"])
    #subprocess.run(["rm", "Dockerfile"])

cli.add_command(new)

if __name__ == '__main__':
    cli()
