import logging
import sys
from argparse import ArgumentParser, Namespace

from atl_cache_warmer.ConfluenceSite import ConfluenceSite
from atl_cache_warmer.JiraSite import JiraSite


def create_arg_parser() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('-u',
                        dest="username",
                        type=str,
                        help="username to use",
                        required=True)
    parser.add_argument('-p',
                        dest="password",
                        type=str,
                        help="password to use",
                        required=True)
    parser.add_argument('-j',
                        dest='jira_url',
                        type=str,
                        help="url for jira",
                        default=None)
    parser.add_argument('-t',
                        dest="jira_target",
                        type=str,
                        help="path in jira to make request to",
                        default=None
                        )
    parser.add_argument('-c',
                        dest='confluence_url',
                        help="url for confluence",
                        type=str,
                        default=None)
    parser.add_argument('-s',
                        dest="space",
                        help="confluence space to make request to",
                        type=str,
                        default=None)
    parser.add_argument('-i',
                        dest="iterate",
                        help="when used in combination with -s, will attempt to iterate through and request all pages "
                             "in the target space.  Jira support coming soon(TM)",
                        action="store_true")
    parser.add_argument('-v',
                        dest="verbosity",
                        help="Increase verbosity level, can used up to 2 times",
                        action="count",
                        default=0)

    return parser


def main():
    arg_parser = create_arg_parser()
    parsed_args: Namespace = arg_parser.parse_args(sys.argv[1:])
    log_level = logging.ERROR
    if parsed_args.verbosity == 0:
        log_level = logging.WARNING
    elif parsed_args.verbosity == 1:
        log_level = logging.INFO
    elif parsed_args.verbosity == 2:
        log_level = logging.DEBUG
    logging.basicConfig(
        level=log_level
    )
    if parsed_args.confluence_url is not None:
        try:
            try:
                c = ConfluenceSite(confluence_url=parsed_args.confluence_url,
                                   confluence_username=parsed_args.username,
                                   confluence_password=parsed_args.password,
                                   confluence_target_space=parsed_args.space,
                                   iterate=parsed_args.iterate
                                   )
            except Exception as ex:
                logging.exception(ex)
                sys.exit(1)

            c.run()
        except Exception as ex:
            logging.error(ex)
            pass

    if parsed_args.jira_url is not None:

        try:
            j = JiraSite(jira_url=parsed_args.jira_url,
                         jira_username=parsed_args.username,
                         jira_password=parsed_args.password,
                         jira_destination=parsed_args.jira_target,
                         iterate=parsed_args.iterate)
            j.run()
        except Exception as ex:
            logging.error(ex)
            pass
