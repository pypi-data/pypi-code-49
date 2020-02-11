import sys
import logging

import pipeline
from pipeline.main import main
from pipeline import settings, init_logging
from pipeline.config import load_config_file, ConfigLoadError
from pipeline.cli_args import (
    Arg,
    parse_args,
    ValidationError
)


ARGS = [
    Arg(
        name='config_file',
        data_type='path',
        ensure_exists='file',
        required=True,
    ),
]


def eprint(*args, **kwargs):
    ''' Pretty print format for error messages. '''
    print(*args, file=sys.stderr, **kwargs)


def cli(task) -> None:
    """
    Initialize args, config, logging, settings, and runs main function.
    Use sys.exit to terminate program.
    """

    try:
        parsed_args = parse_args(ARGS)
    except ValidationError as exception:
        eprint('Argument error: {msg}'.format(msg=exception))
        sys.exit(1)

    # load config file
    try:
        config_values = load_config_file(
            config_file=parsed_args.get('config_file'),
        )

        # set settings from config_values
        for name, value in config_values.items():
            if hasattr(settings, name):
                setattr(settings, name, value)

    except ConfigLoadError as exception:
        eprint('No config file loaded: {msg}, going for default. God bless.'.format(msg=exception))

    # init logging
    init_logging()

    # get logger for this file
    log = logging.getLogger(__name__)

    # log program info
    log.info('Trell Data Pipeline commencing: version=%s', pipeline.__version__)

    # run main program
    main(task)
    # main(task, args)
    sys.exit(0)
