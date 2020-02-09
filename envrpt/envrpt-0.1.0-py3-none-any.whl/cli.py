
import argparse
import sys

from pip._vendor.pkg_resources import get_distribution

from .core import analyze_environment
from .report import REPORT_TYPES, make_report


def create_parser():
    parser = argparse.ArgumentParser(
        description='Analyzes the packages installed in a Python environment',
    )

    version = get_distribution('envrpt').version
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s ' + str(version),
    )

    parser.add_argument(
        '--skip-outdated-check',
        action='store_true',
        help='skips querying the package server for new versions of packages',
    )
    parser.add_argument(
        '--skip-vulnerability-check',
        action='store_true',
        help='skips checking installed packages for known vulnerabilities',
    )

    parser.add_argument(
        '-f',
        '--format',
        choices=sorted(REPORT_TYPES),
        default='console',
        help='the format to output the environment report in; if not specified'
        ', defaults to console',
    )
    parser.add_argument(
        '-o',
        '--output',
        action='store',
        metavar='FILENAME',
        help='the filename to write the output to; if not specified, defaults'
        ' to stdout',
    )

    parser.add_argument(
        '-s',
        '--summary-only',
        action='store_true',
        help='only show a summary of the environment',
    )
    parser.add_argument(
        '-p',
        '--problems-only',
        action='store_true',
        help='only show packages with problems',
    )

    return parser


def main():
    args = create_parser().parse_args()

    if args.output:
        try:
            output = open(args.output, 'w')
        except IOError as exc:
            print(
                'Could not open %s for writing: %s' % (
                    args.output,
                    exc,
                ),
                file=sys.stderr,
            )
            return 73
    else:
        output = sys.stdout

    environment = analyze_environment(
        outdated_packages=not args.skip_outdated_check,
        vulnerable_packages=not args.skip_vulnerability_check,
    )

    report = make_report(
        environment,
        args.format,
        {
            'tty': output.isatty(),
            'summary_only': args.summary_only,
            'problems_only': args.problems_only,
        },
    )

    output.write(report)
    output.write('\n')

    return 0

