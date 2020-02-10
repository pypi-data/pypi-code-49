#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import click

from atlantiscli import VERSION


@click.group()
@click.pass_context
@click.version_option(version=VERSION)
def main(ctx):
    ATLANTIS_URL = os.environ.get('ATLANTIS_URL')

    ctx.obj['config'] = {
        'ATLANTIS_URL': ATLANTIS_URL,
    }


@main.command(name='create')
@click.option('--user/--client', required=True, default=True)
@click.argument('yaml_filepath', required=True, type=click.File('r'))
@click.pass_context
def create(ctx, user, yaml_filepath):
    """
    Create a user/client task from a YAML file
    """
    definition_str = yaml_filepath.read()
    if user and definition_str:
        click.secho("   Creating user...", fg='green')
        output = ctx.obj.client.create_user(definition_str)

    elif not user and definition_str:
        click.secho("   Creating client...", fg='green')
        output = ctx.obj.client.create_client(definition_str)

    click.secho(json.dumps(output, indent=2, sort_keys=True), fg='yellow')