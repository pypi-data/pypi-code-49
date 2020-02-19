import argparse
import pysam

from textwrap import TextWrapper
from typing import Iterable
from lhc.binf.genomic_coordinate import GenomicInterval
from lhc.binf.loci.loci_file import open_loci_file
from lhc.binf.sequence.reverse_complement import reverse_complement
from lhc.io.file import open_file


def extract(regions: Iterable[GenomicInterval], sequences):
    for region in regions:
        sequence = sequences.fetch(str(region.chromosome), region.start.position, region.stop.position)
        yield reverse_complement(sequence) if region.strand == '-' else sequence


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser():
    return define_parser(argparse.ArgumentParser())


def define_parser(parser):
    add_arg = parser.add_argument
    parser.add_argument('input', nargs='?',
                        help='regions to extract (default: stdin).')
    parser.add_argument('output', nargs='?',
                        help='sequence file to extract sequences to (default: stdout).')
    add_arg('-s', '--sequence', required=True,
            help='sequence file to extract regions from')
    parser.set_defaults(func=init_extract)
    return parser


def init_extract(args):
    wrapper = TextWrapper()
    with open_loci_file(args.input) as regions, open_file(args.output, 'w') as output:
        sequences = pysam.FastaFile(args.sequence)
        for region, sequence in zip(regions, extract(regions, sequences)):
            output.write('>{}\n{}\n'.format(region.data['gene_id'], '\n'.join(wrapper.wrap(sequence))))


if __name__ == '__main__':
    import sys
    sys.exit(main())
