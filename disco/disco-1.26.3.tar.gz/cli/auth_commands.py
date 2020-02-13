import click
from disco.core.exceptions import InvalidCredentials, DiscoException
from disco.gql import Authentication
from .command_utils import success_message, error_message

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command('login', context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--user', help='User email to log in with.', prompt='Enter username')
@click.option('-p', '--password', help='User password to log in with.', prompt='Enter password', hide_input=True)
def login(user, password):
    """
    Login to Dis.co.

    $ disco login -u <email> -p <password>
    """
    try:
        Authentication.login(user, password)
        success_message("Signed in successfully")
    except InvalidCredentials:
        error_message("Wrong username or password")
    except DiscoException:
        error_message("Unknown error occurred")


@click.command('logout', context_settings=CONTEXT_SETTINGS)
def logout():
    """
    Logout of Dis.co.

    $ disco logout
    """
    Authentication.logout()
    success_message("Logged out successfully")
