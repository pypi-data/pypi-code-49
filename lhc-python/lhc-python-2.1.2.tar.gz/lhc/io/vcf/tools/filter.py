import argparse
import gzip
import sys

from contextlib import contextmanager
from functools import partial
from typing import IO, Iterable
from lhc.binf.genomic_coordinate import GenomicPosition
from lhc.io.bed.index import IndexedBedFile
from lhc.io.vcf.iterator import VcfIterator
from lhc.io.vcf.index import IndexedVcfFile


def filter_(variants : VcfIterator, filters=None) -> Iterable[GenomicPosition]:
    for variant in variants:
        if all(filter(variant) for filter in filters):
            yield variant


def filter_variant(variant, filter) -> bool:
    local_variables = {'chrom': variant.chromosome, 'pos': variant.position.position}
    local_variables.update(variant.data)
    return eval(filter, local_variables)


def filter_in_region(variant, region_set) -> bool:
    regions = region_set[variant]
    return regions is not None and len(regions) > 0


def filter_out_region(variant, region_set) -> bool:
    regions = region_set[variant]
    return regions is None or len(regions) == 0


def exclude_variant(variant, variant_set) -> bool:
    variants = variant_set[variant]
    return variants is None or len(variants) == 0


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
    parser.add_argument('-f', '--filter', action='append', default=[],
                        help='filter to apply (default: none).')
    parser.add_argument('-i', '--filter-in', action='append', default=[],
                        help='filter in region (default: none).')
    parser.add_argument('-o', '--filter-out', action='append', default=[],
                        help='filter out region (default: none).')
    parser.add_argument('-x', '--exclude', action='append', default=[],
                        help='exclude matches to variant file (default: none)')
    parser.set_defaults(func=init_filter)
    return parser


def init_filter(args):
    filters = []
    for filter in args.filter:
        filters.append(partial(filter_variant, filter=filter))
    for filter_in in args.filter_in:
        filters.append(partial(filter_in_region, region_set=IndexedBedFile(filter_in)))
    for filter_out in args.filter_out:
        filters.append(partial(filter_out_region, region_set=IndexedBedFile(filter_out)))
    for exclude in args.exclude:
        filters.append(partial(exclude_variant, variant_set=IndexedVcfFile(exclude)))

    with open_input(args.input) as variants, open_output(args.output) as output:
        output.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO')
        if len(variants.samples) > 0:
            output.write('\tFORMAT\t' + '\t'.join(variants.samples))
        output.write('\n')
        for variant in filter_(variants, filters):
            output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                str(variant.chromosome),
                variant.position + 1,
                variant.data['id'],
                variant.data['ref'],
                ','.join(variant.data['alt']),
                '.' if variant.data['qual'] is None else variant.data['qual'],
                ':'.join(variant.data['filter']),
                ';'.join('{}={}'.format(key, value) for key, value in variant.data['info'].items())
            ))

            if len(variants.samples) > 0:
                output.write('\t{}\t{}'.format(
                    ':'.join(variant.data['format']),
                    '\t'.join(variant.data[sample] for sample in variants.samples)
                ))
            output.write('\n')

@contextmanager
def open_input(filename : str) -> VcfIterator:
    fileobj = sys.stdin if filename is None else \
        gzip.open(filename, 'rt', encoding='utf-8') if filename.endswith('.gz') else \
        open(filename, encoding='utf-8')
    if filename.endswith('.vcf') or filename.endswith('.vcf.gz'):
        yield VcfIterator(fileobj)
    else:
        raise ValueError('unrecognised file format: {}'.format(filename))
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
