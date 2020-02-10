import gzip
import sys
import argparse

from contextlib import contextmanager
from typing import IO, Iterable, Optional
from lhc.binf.genomic_coordinate import GenomicInterval, get_converter
from lhc.io.bed import BedConverter
from lhc.io.gff import GffConverter
from lhc.io.gtf import GtfConverter


def filter(intervals: Iterable[GenomicInterval], expression=None) -> Iterable[GenomicInterval]:
    for interval in intervals:
        local_variables = {
            'chromosome': interval.chromosome,
            'start': interval.start,
            'stop': interval.stop,
            'strand': interval.strand
        }
        local_variables.update(interval.data)
        if eval(expression, local_variables):
            yield interval


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser():
    return define_parser(argparse.ArgumentParser())


def define_parser(parser):
    parser.add_argument('input', nargs='?',
                        help='name of the intervals file to be filtered (default: stdin).')
    parser.add_argument('output', nargs='?',
                        help='name of the filtered intervals file (default: stdout).')
    parser.add_argument('-f', '--filter', required=True,
                        help='filter to apply (default: none).')
    parser.add_argument('-i', '--input-format',
                        help='file format of input file (useful for reading from stdin).')
    parser.add_argument('-o', '--output-format',
                        help='file format of output file (useful for writing to stdout).')
    parser.add_argument('-v', '--inverse', action='store_true',
                        help='invert filter.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--region',
                       help='apply filter in region (default: none).')
    group.add_argument('-x', '--exclude',
                       help='do not apply filter in region (default: none).')
    parser.set_defaults(func=init_filter)
    return parser


def init_filter(args):
    with open_file(args.input) as input, open_file(args.output, 'w') as output:
        input_converter = get_converter(args.input,
                                        args.input_format,
                                        [BedConverter, GffConverter, GtfConverter])(input)
        output_converter = get_converter(args.output,
                                         args.output_format,
                                         [BedConverter, GffConverter, GtfConverter])(None)
        for interval in filter(input_converter, args.filter):
            output.write(output_converter.format(interval))


@contextmanager
def open_file(filename: Optional[str], mode='r', encoding='utf-8') -> IO:
    fileobj = sys.stdout if filename is None else \
        gzip.open(filename, '{}t'.format(mode), encoding=encoding) if filename.endswith('.gz') else \
        open(filename, mode, encoding=encoding)
    yield fileobj
    fileobj.close()


if __name__ == '__main__':
    sys.exit(main())
