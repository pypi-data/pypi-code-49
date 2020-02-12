#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import click

from atlantiscli.config import ATLANTIS_URL
from atlantiscli import VERSION


@click.group()
@click.pass_context
@click.version_option(version=VERSION)
def main(ctx):
    ctx.obj['config'] = {
        'ATLANTIS_URL': ATLANTIS_URL,
    }


@main.group()
def user():
    pass


@user.command(name='create')
@click.argument('name', required=True)
@click.argument('email', required=True)
@click.argument('password', required=True)
@click.pass_context
def create_user(ctx, name, email, password):
    click.secho("   Creating user...", fg='green')
    user = ctx.obj.client.create_user(name, email, password)
    click.secho(json.dumps(user, indent=2, sort_keys=True), fg='yellow')


user.add_command(create_user)


@main.group()
def client():
    pass


@client.command(name='create')
@click.argument('name', required=True)
@click.argument('redirect_uri', required=True)
@click.argument('scope', required=True)
@click.pass_context
def create_client(ctx, name, redirect_uri, scope) :
    click.secho("   Creating client...", fg='green')
    client = ctx.obj.client.create_client(name, redirect_uri, scope)
    click.secho(json.dumps(client, indent=2, sort_keys=True), fg='yellow')


client.add_command(create_client)