from pathlib import Path
import click
import os
import configparser
import time
import hashlib


def get_config_path():
    home = str(Path.home())
    return f'{home}/.treebeard'


config_path = get_config_path()


def get_notebook_name():
    if not os.path.isfile(f"{os.getcwd()}/main.ipynb"):
        return None
    return Path(os.getcwd()).name


def get_treebeard_env():
    """Reads variables from a local file, credentials.cfg"""
    config = configparser.RawConfigParser()
    treebeard_project_id = None
    run_id = None
    email = None
    api_key = None

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
        pass  # Default values indicate error occurred
    treebeard_env = {
        'notebook_id': get_notebook_name(),
        'project_id': treebeard_project_id,
        'run_id': run_id,
        'email': email,
        'api_key': api_key
    }
    return treebeard_env


def set_credentials(email, key):
    """Create user credentials"""
    # key = secrets.token_urlsafe(16)
    config = configparser.RawConfigParser()
    config.add_section('credentials')
    config.set('credentials', 'TREEBEARD_EMAIL', email)
    # Project id is last 10 numbers of hash of email
    m = hashlib.sha256()
    m.update(email.encode())
    project_id = m.hexdigest()[:10]
    config.set('credentials', 'TREEBEARD_PROJECT_ID', project_id)
    config.set('credentials', 'TREEBEARD_API_KEY', key)
    with open(config_path, 'w') as configfile:
        config.write(configfile)
    click.echo(
        f'User credentials saved in {config_path}\nEmail: {email}\nProject ID: {project_id}\nAPI key: {key}')
    return


def fetch_credentials():
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
    treebeard_env = get_treebeard_env()
    print(f"Treebeard env is {treebeard_env}")
    return f"{treebeard_env['project_id']}/{treebeard_env['notebook_id']}/{treebeard_env['run_id']}"
