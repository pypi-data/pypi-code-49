# The Click application that is the front-end to the acronyms filter.

import sys
import os
import click
from acronyms.acronym_filter import Filter
from acronyms.logging import configure_logging, error, debug as logdebug, info


@click.command()
@click.option('-a', '--acronyms', envvar='PANDOC_ACRONYMS_ACRONYMS', default="", help='A file with acronym definitions in JSON format.', multiple=True)
@click.option('-v', '--verbose/--no-verbose', envvar='PANDOC_ACRONYMS_VERBOSE', default=False, help='Enable verbose output.')
@click.option('-s', '--suggest/--no-suggest', envvar='PANDOC_ACRONYMS_SUGGEST', default=False, help='Suggest marking acronyms detected in the text.')
@click.option('-v', '--debug/--no-debug', envvar='PANDOC_ACRONYMS_DEBUG', default=False, help='Enable debug output.')
@click.version_option()
@click.argument('format', nargs=-1)
def filter(acronyms, verbose, suggest, debug, format):
    """The pandoc-acronyms filter."""
    filter = Filter()
    filter.suggest = suggest
    configure_logging(verbose, debug)
    logdebug("command line: {}".format(" ".join(sys.argv)))
    logdebug("verbose: {}, debug: {}, suggest: {}".format(verbose, debug, suggest))
    try:
        filter.run(acronyms)
    except Exception as e:
        error(str(e))
        if verbose:
            raise e


if __name__ == '__main__':
    filter()  # pylint: disable=no-value-for-parameter
