import argparse
import logging
import os
import sys

from typing import *

import cbee
from .build import Build


def clean(source_dir: Optional[str] = None, build_dir: Optional[str] = None) -> None:
    Build.load(source_dir, build_dir).clean()


def analyze(source_dir: Optional[str] = None, build_dir: Optional[str] = None) -> None:
    print(Build.load(source_dir, build_dir).analyze())


def build(source_dir: Optional[str] = None, build_dir: Optional[str] = None) -> None:
    Build.load(source_dir, build_dir).build()


def run(source_file_path: str, args: Optional[List[str]] = None, build_dir: Optional[str] = None) -> None:
    if not os.path.isfile(source_file_path):
        raise ValueError('must specify a source file path with a main function')
    source_dir, source_file = os.path.split(source_file_path)
    Build.load(source_dir, build_dir).run(source_file, args)


def version() -> None:
    print(f"cbee {cbee.version}")


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--verbose', '-v',
        action='store_true')
    actions = parser.add_subparsers()

    def add_source_dir(p: argparse.ArgumentParser) -> None:
        p.add_argument(
            'source_dir',
            nargs='?',
            help='Path to the project source code')
    def add_build_dir(p: argparse.ArgumentParser) -> None:
        p.add_argument(
            '--build-dir',
            help='Path to compile and build the source code')

    # clean
    parser_clean = actions.add_parser(
        'clean', help='Clean up and delete all the build files')
    add_source_dir(parser_clean)
    add_build_dir(parser_clean)
    parser_clean.set_defaults(func=clean)

    # analyze
    parser_analyze = actions.add_parser(
        'analyze', help='Analyze source code')
    add_source_dir(parser_analyze)
    add_build_dir(parser_analyze)
    parser_analyze.set_defaults(func=analyze)

    # build
    parser_build = actions.add_parser(
        'build', help='Build an application or library')
    add_source_dir(parser_build)
    add_build_dir(parser_build)
    parser_build.set_defaults(func=build)

    # run
    parser_run = actions.add_parser('run', help='Build and run an application')
    add_build_dir(parser_run)
    parser_run.add_argument(
        'source_file_path',
        help='Path to a source code file containing a main function')
    parser_run.add_argument(
        'args',
        nargs=argparse.REMAINDER,
        help='Arguments to pass to application')
    parser_run.set_defaults(func=run)

    # package

    # install

    # uninstall

    # publish

    # search

    # version
    parser_version = actions.add_parser('version', help='Prints cbee version')
    parser_version.set_defaults(func=version)

    args = parser.parse_args(argv)
    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    logging.info(f"  sys.argv {sys.argv}")
    logging.info(f"  argv     {argv}")

    args_dict = vars(args)
    func = args_dict.pop('func', lambda: parser.print_help())
    args_dict.pop('verbose')
    func(**args_dict)


if __name__ == '__main__':
    main()
