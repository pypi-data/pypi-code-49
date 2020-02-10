import argparse
import gzip
import sys

from contextlib import contextmanager
from typing import Iterable, IO


def shift(lines : Iterable[str], shift=0) -> Iterable[str]:
    for line in lines:
        if line.startswith('#'):
            yield line
        else:
            parts = line.split('\t')
            parts[1] = str(int(parts[1]) + shift)
            yield '\t'.join(parts)


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser():
    return define_parser(argparse.ArgumentParser())


def define_parser(parser):
    parser.add_argument('input', nargs='?',
                        help='name of the vcf_ file to be filtered (default: stdin).')
    parser.add_argument('output', nargs='?',
                        help='name of the filtered vcf_ file (default: stdout).')
    parser.add_argument('-a', '--amount', type=int, default=0,
                        help='amount to shift position by (default: none).')
    parser.set_defaults(func=init_shift)
    return parser


def init_shift(args):
    with open_input(args.input) as input, open_output(args.output) as output:
        for line in shift(input, args.amount):
            output.write(line)

@contextmanager
def open_input(filename : str) -> Iterable[str]:
    fileobj = sys.stdin if filename is None else \
        gzip.open(filename, 'rt', encoding='utf-8') if filename.endswith('.gz') else \
        open(filename, encoding='utf-8')
    yield fileobj
    fileobj.close()


@contextmanager
def open_output(filename: str) -> IO:
    fileobj = sys.stdout if filename is None else \
        gzip.open(filename, 'wt', encoding='utf-8') if filename.endswith('.gz') else \
        open(filename, 'w', encoding='utf-8')
    yield fileobj
    fileobj.close()


if __name__ == '__main__':
    sys.exit(main())
