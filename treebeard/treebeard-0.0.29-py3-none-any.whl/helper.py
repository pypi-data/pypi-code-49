from pathlib import Path
import click
import os
import configparser
import time

# config_path = os.path.join(os.path.expanduser('~'), '.treebeard')
config_path = '.treebeard'


def get_notebook_name():
    if not os.path.isfile(f"{os.getcwd()}/main.ipynb"):
        raise Exception(
            "The current directory must contain a file named main.ipynb")
    return Path(os.getcwd()).name


def get_treebeard_env(config_path):
    """Reads variables from a local file, credentials.cfg"""
    config = configparser.RawConfigParser()
    treebeard_project_id = ''
    run_id = ''
    email = ''
    api_key = ''

    try:
        config.read(config_path)
        email = config.get('credentials', 'TREEBEARD_EMAIL')
        treebeard_project_id = config.get(
            'credentials', 'TREEBEARD_PROJECT_ID')
        api_key = config.get('credentials', 'TREEBEARD_API_KEY')
        # run_id = config.get('credentials', 'TREEBEARD_RUN_ID')

        run_id = os.getenv('TREEBEARD_RUN_ID')
        if run_id is None:
            run_id = f"local-{int(time.time())}"
        # treebeard_project_id = os.getenv('TREEBEARD_PROJECT_ID')
        # email = os.getenv('TREEBEARD_EMAIL')
        # api_key = os.getenv('TREEBEARD_API_KEY')
    except:
        click.echo(click.style(
            'This library will not function without credentials.\nPlease email alex@treebeard.io to obtain an API key then run `treebeard configure`', fg='red'))

    treebeard_env = {
        'notebook_id': get_notebook_name(),
        'project_id': treebeard_project_id,
        'run_id': run_id,
        'email': email,
        'api_key': api_key
    }
    return treebeard_env


def set_credentials(email, key, config_path):
    """Create user credentials"""
    # key = secrets.token_urlsafe(16)
    config = configparser.RawConfigParser()
    config.add_section('credentials')
    config.set('credentials', 'TREEBEARD_EMAIL', email)
    # Project id is last 10 numbers of hash of email
    project_id = str(hash(email))[-10:]
    config.set('credentials', 'TREEBEARD_PROJECT_ID', project_id)
    config.set('credentials', 'TREEBEARD_API_KEY', key)
    with open(config_path, 'w') as configfile:
        config.write(configfile)
    click.echo(
        f'User credentials saved in {config_path}\nEmail: {email}\nProject ID: {project_id}\nAPI key: {key}')
    return


def fetch_credentials(config_path):
    """
    Checks for user credentials and returns user email and API key
    """
    # Does credentials.cfg exist and if it does, can we read the API key
    config = configparser.RawConfigParser()
    try:
        os.path.isfile(config_path)
        config.read(config_path)
        key = config.get('credentials', 'TREEBEARD_API_KEY')
        email = config.get('credentials', 'TREEBEARD_EMAIL')
        click.echo('Connecting to your account.')
    except:
        click.echo(f"No credentials found - please run: treebeard configure")
    return key, email


def get_run_path():
    treebeard_env = get_treebeard_env(config_path)
    print(f"Treebeard env is {treebeard_env}")
    return f"{treebeard_env['project_id']}/{treebeard_env['notebook_id']}/{treebeard_env['run_id']}"
