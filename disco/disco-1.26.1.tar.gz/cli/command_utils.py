import os
from requests import HTTPError, ConnectionError as RequestsConnectionError
from tabulate import tabulate
import click

from disco.core.exceptions import DiscoException, GraphQLRequestException, InvalidCredentials
from disco.gql import Authentication


class ExpandedPath(click.Path):
    """
    Allows click.Path() validator to convert user's home path
    i.e `~/some_file.py` => `/Users/SOME_USER/some_file.py`

    see:
        https://github.com/pallets/click/issues/287
    """
    def convert(self, value, param, ctx):
        value = os.path.expanduser(value)
        return super(ExpandedPath, self).convert(value, param, ctx)


def verify_logged_in():
    """
    Verifies that the user is logged in and print error message if not
    Returns: True if user is logged in

    """
    if not Authentication.is_logged_in():
        error_message("You must be logged in to perform this operation")
        return False
    return True


def success_message_func(message):
    """
    A helper function for creating success message functions

    Args:
        message (str): The message to show

    Returns: a function that outputs a success message

    """

    return lambda response=None: click.echo(click.style(message, fg='green'))


def error_message_func(message):
    """
    A helper function for creating error message functions

    Args:
        message (str): The message to show

    Returns: a function that outputs an error message

    """

    return lambda response=None: click.echo(click.style(message, fg='red'))


def exception_message(exception):
    """
        A helper function for creating error messages
        The function determines the message to show by the exception given

        Args:
            message (str): The message to show

        Returns: a function that outputs an error message

        """
    click.echo(click.style(f"{get_error_message(exception)}", fg='red'))


def get_error_message(exception):
    """
    Get a message for the given exception
    Args:
        exception (:obj:`Exception`): An exception

    Returns:
        A message for the user according to the exception
    """
    if isinstance(exception, DiscoException):
        if isinstance(exception, GraphQLRequestException):
            messages = list(map(lambda error: error['message'], exception.errors))
            if any(msg.find('Cast to ObjectId failed') >= 0 for msg in messages):
                return "Bad format for Id"
        if isinstance(exception, InvalidCredentials):
            return "Wrong username or password - run 'disco login' and try again"

    if isinstance(exception, RequestsConnectionError):
        return "No internet connection"

    if isinstance(exception, HTTPError):
        if exception.response.status_code == 400:
            return "Not logged in or bad request"

    return 'Unknown'


def error_message(message):
    """
    Outputs an error message
    Args:
        message (str): Message to show

    Returns:
        None
    """
    error_message_func(message)()


def success_message(message):
    """
    Outputs a success message
    Args:
        message (str): Message to show

    Returns:
        None
    """
    success_message_func(message)()


def info_message(message):
    """
    Outputs an informational message
    Args:
        message (str): Message to show

    Returns:
        None
    """
    click.echo(click.style(message, fg='yellow'))


def list_to_table(obj_list, headers=""):
    """
    Converts a list to a displayable table
    The list must be a list of lists with the same length
    Args:
        obj_list (:obj:`list` of :obj:`list` of :obj:`str`): List of objects to display
        headers: (:obj:`list` of :obj:`str): Table headers

    Returns:
        A string that contains a table
    """
    return tabulate(obj_list, headers, tablefmt='grid')
