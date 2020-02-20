# The API for diagnostics and debug output.
import click

_Verbose = False
_Debug = False


def configure_logging(verbose, debug):
    global _Verbose
    _Verbose = verbose
    global _Debug
    _Debug = debug


def debug(msg):
    if _Debug:
        click.secho(msg, fg='blue', err=True)


def info(msg, force = False):
    if _Verbose:
        click.secho(msg, fg='yellow', err=True)


def error(msg):
    click.secho(msg, fg='red', err=True)


def fatal(msg):
    raise RuntimeError(msg)
