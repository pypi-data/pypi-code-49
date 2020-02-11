import os
import sys
import click
import traceback
import logging
import threading
import time
from pprint import pformat, pprint
from tabulate import tabulate

from . import logs, storage
from .auth import AuthModule
from .compat import format_exception
from .errors import SpintopException
from .models import Query
from .spintop import Spintop


class CLIParseException(SpintopException):
    pass

logger = logs._logger('cli')

_spintop = None 
spintop_kwargs = {}
def spintop():
    global _spintop, spintop_kwargs
    if _spintop is None:
        _spintop = Spintop(**spintop_kwargs)
    return _spintop

@click.group()
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.option('--url', default='https://api.spinhub.ca')
@click.option('--org-id', default=None)
def _cli(verbose, url, org_id):
    global spintop_kwargs
    logs.VERBOSE = verbose
    spintop_kwargs = dict(verbose=verbose, org_id=org_id, spinhub_url=url)

@_cli.command('site-data-dir')
def site_data_dir():
    click.echo(storage.SITE_DATA_DIR)
    
@_cli.command('login')
@click.option('--username', default=None)
@click.option('--password', default=None)
def login_command(username, password):
    if username is None and password is not None:
        raise CLIParseException('You cannot specify the password as option but not the username')
    
    spintop().assert_no_login() # Check first before prompting
    
    if username is None:
        username = click.prompt('Username')
        
    if password is None:
        password = click.prompt('Password', hide_input=True)
    
    spintop().login(username, password)

@_cli.command('register')
@click.argument('name')
@click.option('--token', default=None)
@click.option('--org-id', default=None)
def register(name, token, org_id=None):
    spintop().register_machine(name, token, org_id=org_id)

@_cli.command('logout')
def logout_command():
    stored_username = spintop().stored_logged_username()
    if stored_username:
        if click.confirm('Logging out %s. Continue ?' % stored_username):
            spintop().logout()
    else:
        click.echo('No credentials stored.')
    
@_cli.command('show-token')
def get_org_token():
    print(spintop().spinhub.get_token())

@_cli.command('ls-orgs')
def get_orgs():
    orgs = spintop().get_user_orgs()
    spintop().spinhub.retrieve_tests(test_selector=Query().testbench_name_is('demo-testbench'))
    data = [[org['uuid'], org['key']] for org in orgs]
    click.echo(tabulate(data, headers=['UUID', 'Org Key']))

@_cli.command('ls-peers')
def get_orgs():
    this_machine = spintop().get_machine()
    peers = spintop().get_peers()
    data = [[
            peer_machine['uuid'], 
            peer_machine['nickname'] + (' (self)' if peer_machine['uuid'] == this_machine['uuid'] else ''),
            'Machine' if peer_machine['is_machine'] else 'User'
        ] for peer_machine in peers]
    click.echo(tabulate(data, headers=['UUID', 'Nickname', 'Type']))
    
@_cli.group('config')
def config():
    pass
    
@config.command('show')
def show_config():
    config = spintop().config.get_stored()
    click.echo(pformat(config))
    
@config.command('update')
@click.argument('key_values', nargs=-1)
def update_profile(key_values):
    profile = spintop().config.get_selected_profile()
    updates = {}
    for key_value in key_values:
        key, value = key_value.split('=')
        updates[key] = value
        
    click.echo('Will update profile named %s with:' % profile['name'])
    click.echo(pformat(updates))
    if click.confirm('Proceed ?'):
        spintop().config.update_profile(**updates)
        spintop().config.save()
    
@config.command('clear')
def clear_config():
    if click.confirm('This will delete all local credentials and profiles. Proceed ?'):
        spintop().delete_config()
    
@_cli.command('test-api-private')
def test_private_command():
    print(spintop().spinhub.test_private_endpoint().content)
    
@_cli.command('force-corrupt-access-token')
def force_corrupt_access_token():
    spintop().spinhub.auth.credentials.access_token = spinhub.auth.credentials.access_token[0:-4]
    spintop().spinhub.auth.save_credentials()


def cli(args=None, internal=True):
    try:
        return _cli(args, prog_name='spintop')
    except Exception as e:
        if logs.VERBOSE:
            click.echo(traceback.format_exc())
        else:
            click.echo(format_exception(e))
    except SystemExit:
        if not internal:
            raise
            
if __name__ == '__main__':
    cli(internal=False)