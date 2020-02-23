#!/usr/bin/env python3

# Libraries
import argparse
import colored
import os
import sys

# Constants
NAME = 'gitlabci-local'

# Components
from .dumper import dumper
from .menu import selector
from .parser import reader
from .puller import puller
from .runner import launcher

# Main
def main():

    # Variables
    interactive = (sys.stdin.isatty() and sys.stdout.isatty())
    result = False

    # Arguments creation
    parser = argparse.ArgumentParser(
        prog=NAME, description='%s: Launch .gitlab-ci.yml jobs locally' % (NAME),
        add_help=False, formatter_class=argparse.RawTextHelpFormatter)

    # Arguments default definitions
    tagsDefault = ['deploy', 'local', 'publish']

    # Arguments enumerations definitions
    networksEnum = ['bridge', 'host', 'none']

    # Arguments optional definitions
    parser.add_argument('-h', dest='help', action='store_true',
                        help='Show this help message')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true',
                        help='Hide jobs execution context')
    parser.add_argument('-c', dest='configuration', default='.gitlab-ci.yml',
                        help='Path to the .gitlab-ci.yml configuration')
    parser.add_argument('-B', '--no-before', dest='before', action='store_false',
                        help='Disable before_script executions')
    parser.add_argument('-A', '--no-after', dest='after', action='store_false',
                        help='Disable after_script executions')
    parser.add_argument('-m', '--manual', dest='manual', action='store_true',
                        help='Allow manual jobs to be used')
    parser.add_argument(
        '-n', dest='network',
        help='Configure the network mode used\nChoices: %s. Default: %s' %
        (', '.join(networksEnum), networksEnum[0]))
    parser.add_argument('-p', '--pipeline', dest='pipeline', action='store_true',
                        help='Run complete stages rather than jobs')
    parser.add_argument('-e', dest='env', action='append',
                        help='Define VARIABLE=value, pass VARIABLE or ENV file')
    parser.add_argument(
        '-t', dest='tags', action='append',
        help='Handle listed tags as manual jobs\nDefault list: [\'%s\']' %
        ('\', \''.join(tagsDefault)))
    parser.add_argument('--tags-default', dest='tags_default', action='store_true',
                        help=argparse.SUPPRESS)
    parser.add_argument('-v', dest='volume', action='append',
                        help='Mount VOLUME or HOST:TARGET in Docker containers')
    parser.add_argument('-w', dest='workdir',
                        help='Override the container\'s working path')
    parser.add_argument('--all', dest='all', action='store_true',
                        help='Enable all jobs by default in selections')
    parser.add_argument('--defaults', dest='defaults', action='store_true',
                        help='Use default variables for .local:configurations')
    parser.add_argument('--image', dest='image', help=argparse.SUPPRESS)

    # Arguments exclusive definitions
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--dump', dest='dump', action='store_true',
                       help='Dump parsed .gitlab-ci.yml configuration')
    group.add_argument('-s', '--select', dest='select', action='store_true',
                       help='Force jobs selection from enumerated names')
    group.add_argument('-l', '--list', dest='list', action='store_true',
                       help='Select one job to run (implies --manual)')
    group.add_argument('--pull', dest='pull', action='store_true',
                       help='Pull Docker images from all jobs')

    # Arguments positional definitions
    parser.add_argument('names', nargs='*',
                        help='Names of specific jobs (or stages with --pipeline)')

    # Arguments parser
    options = parser.parse_args()
    if options.help:
        print(' ')
        parser.print_help()
        print(' ', flush=True)
        sys.exit(0)

    # Prepare paths
    options.path = os.path.dirname(os.path.abspath(options.configuration))

    # Prepare tags
    if not options.tags:
        options.tags = tagsDefault
        options.tags_default = True

    # Read configuration
    jobs = reader(options)
    if not jobs:
        sys.exit(1)

    # Header
    print(' ', flush=True)

    # Dump configuration
    if options.dump:
        result = dumper(options, jobs)

    # Pull jobs images
    elif options.pull:
        result = puller(options, jobs)

    # Select job
    elif options.list and interactive:
        options.manual = True
        result = selector(options, jobs)

    # Select jobs
    elif options.select and interactive:
        result = selector(options, jobs)

    # Launch pipeline
    elif options.pipeline:
        result = launcher(options, jobs)

    # Launch jobs
    elif options.names:
        result = launcher(options, jobs)

    # Select jobs
    elif interactive:
        result = selector(options, jobs)

    # Launch all jobs
    elif options.all:
        options.pipeline = True
        result = launcher(options, jobs)

    # Unsupported case
    else:
        print(' %s%s: %sERROR: %sUnsupported non-interactive context...%s' %
              (colored.fg('green') + colored.attr('bold'), NAME,
               colored.fg('red') + colored.attr('bold'),
               colored.attr('reset') + colored.attr('bold'), colored.attr('reset')))
        print(' ', flush=True)

    # Result
    if result:
        sys.exit(0)
    else:
        sys.exit(1)

# Entrypoint
if __name__ == '__main__':
    main()
