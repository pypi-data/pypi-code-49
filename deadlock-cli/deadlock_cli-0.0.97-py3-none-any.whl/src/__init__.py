#! python3
import os
import subprocess
from string import Template

import click
import inquirer

@click.command()
@click.option('--n', default=1)
def dots(n):
    click.echo('.' * n)
