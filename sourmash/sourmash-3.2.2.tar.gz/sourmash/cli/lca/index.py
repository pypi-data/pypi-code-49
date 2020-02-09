"""create LCA database"""

from sourmash.cli.utils import add_ksize_arg


def subparser(subparsers):
    subparser = subparsers.add_parser('index')
    subparser.add_argument('csv', help='taxonomy spreadsheet')
    subparser.add_argument('lca_db_out', help='output database name')
    subparser.add_argument(
        'signatures', nargs='+',
        help='one or more sourmash signatures'
    )
    subparser.add_argument(
        '--scaled', metavar='S', default=10000, type=float
    )
    add_ksize_arg(subparser, 31)
    subparser.add_argument(
        '-q', '--quiet', action='store_true',
        help='suppress non-error output'
    )
    subparser.add_argument(
        '-d', '--debug', action='store_true',
        help='output debugging output'
    )
    subparser.add_argument(
        '-C', '--start-column', metavar='C', default=2, type=int,
        help='column at which taxonomic assignments start; default=2'
    )
    subparser.add_argument(
        '--tabs', action='store_true',
        help='input spreadsheet is tab-delimited; default is commas'
    )
    subparser.add_argument(
        '--no-headers', action='store_true',
        help='no headers present in taxonomy spreadsheet'
    )
    subparser.add_argument(
        '--split-identifiers', action='store_true',
        help='split names in signatures on whitspace and period'
    )
    subparser.add_argument('-f', '--force', action='store_true')
    subparser.add_argument(
        '--traverse-directory', action='store_true',
        help='load all signatures underneath directories'
    )
    subparser.add_argument(
        '--report', help='output a report on anomalies, if any'
    )
    subparser.add_argument(
        '--require-taxonomy', action='store_true',
        help='ignore signatures with no taxonomy entry'
    )


def main(args):
    import sourmash
    return sourmash.lca.command_index.index(args)
