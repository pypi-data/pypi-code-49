"""Configures and stores the .heartrc configuration file with the details
for the HEART CRM Salesforce OAUTH app."""
import os
import stat
import yaml


FILENAME = '.heartrc'
CURRENT_DIR = os.getcwd()
HOME_DIR = os.path.expanduser('~')
FILE_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = os.path.join(FILE_DIR, '..')


def configure(**kwargs):
    """Configures the .heartrc file to allow the user to connect without
    having to enter the information for the OAUTH app every time.

    Parameters
    ----------
    directory : str
        the directory to write the configuration file to.
    """
    keys = ['redirect_uri', 'client_id', 'client_secret', 'sandbox']
    config = dict()
    for key in keys:
        value = kwargs.get(key, None)
        if value:
            config[key] = value
        else:
            value = input('{}: '.format(key))
            value = value.lower() == 'y' if key == 'sandbox' else value
            config[key] = value

    filename = os.path.join(PROJECT_DIR, FILENAME)
    with open(filename, 'w') as f:
        yaml.dump(config, f)
    # Only give the owner permissions on the file
    os.chmod(filename, stat.S_IRWXU)


def read_heartrc():
    """Finds the .heartrc configuration file. The order of precedence is:
    1. The current working directory
    2. The root directory for heartrc
    3. The home directory for the user
    """
    config = None
    for directory in [CURRENT_DIR, PROJECT_DIR, HOME_DIR]:
        files = os.listdir(directory)
        if FILENAME in files:
            with open(os.path.join(directory, FILENAME)) as f:
                config = yaml.safe_load(f)
            break
    return config
