import sys
import argparse

from typing import Iterable
from lhc.binf.genomic_coordinate import GenomicInterval, get_converter
from lhc.io import open_file
from lhc.io.bed import BedConverter
from lhc.io.gff import GffConverter
from lhc.io.gtf import GtfConverter


def extend(intervals: Iterable[GenomicInterval], *, five_prime=0, three_prime=0) -> Iterable[GenomicInterval]:
    for interval in intervals:
        if interval.strand == '+':
            interval.start -= five_prime
            interval.stop += three_prime
        else:
            interval.start -= three_prime
            interval.stop += five_prime
        yield interval


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser():
    return define_parser(argparse.ArgumentParser())


def define_parser(parser):
    parser.add_argument('input', nargs='?',
                        help='name of the intervals file to be extended (default: stdin).')
    parser.add_argument('output', nargs='?',
                        help='name of the extended intervals file (default: stdout).')
    parser.add_argument('-i', '--input-format',
                        help='file format of input file (useful for reading from stdin).')
    parser.add_argument('-o', '--output-format',
                        help='file format of output file (useful for writing to stdout).')
    parser.add_argument('-5', '--five-prime', type=int, default=0,
                        help='extend in the 5\' direction.')
    parser.add_argument('-3', '--three-prime', type=int, default=0,
                        help='extend in the 3\' direction.')
    parser.set_defaults(func=init_extend)
    return parser


def init_extend(args):
    if not (args.five_prime or args.three_prime):
        raise ValueError('At least one of --five-prime or --three-prime must be specified.')
    with open_file(args.input) as input, open_file(args.output, 'w') as output:
        input_converter = get_converter(args.input,
                                        args.input_format,
                                        [BedConverter, GffConverter, GtfConverter])(input)
        output_converter = get_converter(args.output,
                                         args.output_format,
                                         [BedConverter, GffConverter, GtfConverter])(None)
        for interval in extend(input_converter, five_prime=args.five_prime, three_prime=args.three_prime):
            output.write(output_converter.format(interval))


if __name__ == '__main__':
    sys.exit(main())
