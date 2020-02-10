import argparse

from ._build_webviz import build_webviz
from ._certificate import create_ca


def main() -> None:

    parser = argparse.ArgumentParser(
        prog=("Creates a Webviz Dash app from a configuration setup")
    )

    subparsers = parser.add_subparsers(
        help="The options available. "
        'Type e.g. "webviz build --help" '
        "to get help on that particular "
        "option."
    )

    # Add "build" argument parser:

    parser_build = subparsers.add_parser("build", help="Build a Webviz " "Dash App")

    parser_build.add_argument(
        "yaml_file", type=str, help="Path to YAML configuration file"
    )
    parser_build.add_argument(
        "--portable",
        type=str,
        default=None,
        metavar="OUTPUTFOLDER",
        help="A portable webviz instance will created "
        "and saved to the given folder.",
    )
    parser_build.add_argument(
        "--theme", type=str, default="default", help="Which installed theme to use."
    )
    parser_build.add_argument(
        "--loglevel",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        type=str,
        help="Wanted level of logging output from webviz plugins. "
        "Selecting e.g. INFO will show all log events of level INFO or higher "
        "(WARNING, ERROR and CRITICAL). Default level is WARNING.",
    )

    parser_build.set_defaults(func=build_webviz)

    # Add "certificate" parser:

    parser_cert = subparsers.add_parser(
        "certificate",
        help="Create a https certificate authority for webviz "
        "(validity limited to localhost only)",
    )

    parser_cert.add_argument(
        "--force",
        action="store_true",
        help="Overwrite webviz root https certificate if it already exists",
    )

    parser_cert.add_argument(
        "--auto-install",
        action="store_true",
        help="Automatically install the webviz certificate in "
        "your personal public key infrastructure",
    )

    parser_cert.set_defaults(func=create_ca)

    # Do the argument parsing:

    args = parser.parse_args()

    args.func(args)
