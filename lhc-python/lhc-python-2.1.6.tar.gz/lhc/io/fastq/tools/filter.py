import argparse
import fileinput
import gzip
import os

from multiprocessing import Process
from lhc.io.fastq import iter_partial_fastq
from lhc.misc.bitap import bitap_fuzzy


class FilterJob(Process):
    def __init__(
        self,
        input_streams,
        output_streams,
        filters,
        mode,
        group=None,
        target=None,
        name=None,
        args=(),
        kwargs={}
    ):
        super().__init__(group, target, name, args, kwargs)

        self.input_streams = input_streams
        self.output_streams = output_streams
        self.filters = filters
        self.mode = mode

    def run(self):
        for reads in filter(self.input_streams, self.filters, self.mode):
            for read, output_stream in zip(reads, self.output_streams):
                output_stream.write(str(read))


def filter(input_streams, filters, mode='all'):
    fn = all if mode == 'all' else\
        any if mode == 'any' else\
        None

    for i, reads in enumerate(zip(*input_streams)):
        if i % 10000 == 0:
            print(i)
        if fn(bitap_fuzzy(query, reads[index].seq, mismatches) is not None for query, mismatches, index in filters):
            yield reads


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser() -> argparse.ArgumentParser:
    return define_parser(argparse.ArgumentParser(
        'Filters synchronised (eg. single-/paired-end) fastq files for the presence of any or all of the filter'
        ' sequences. Consider using "agrep" instead.'))


def define_parser(parser) -> argparse.ArgumentParser:
    parser.add_argument('read_files', nargs='+')
    parser.add_argument('-f', '--filter', dest='filters', nargs=3, action='append',
                        metavar=('SEQUENCE', 'MISMATCHES', 'INDEX'), required=True)
    parser.add_argument('-j', '--jobs', default=1, type=int)
    parser.add_argument('-m', '--mode', choices=['all', 'any'], default='all')
    parser.add_argument('-o', '--output-dir')
    parser.set_defaults(func=init_filter)
    return parser


def init_filter(args):
    filters = [(sequence, int(mismatches), int(index)) for sequence, mismatches, index in args.filters]

    output_names = [read_file.rsplit('.', 2)[0] if read_file.endswith('.gz') else
                    read_file.rsplit('.', 1)[0] for read_file in args.read_files]
    if args.output_dir is not None:
        output_names = [os.path.join(args.output_dir, os.path.basename(output_name))
                        for output_name in output_names]

    jobs = []
    for i in range(args.jobs):
        input_streams = [iter_partial_fastq(read_file, i / args.jobs, (i + 1) / args.jobs)
                         for read_file in args.read_files]
        output_streams = [open('{}.{}.filtered.fastq'.format(output_name, i), 'w')
                          for output_name in output_names]
        jobs.append(FilterJob(input_streams, output_streams, filters, args.mode))
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    for output_name in output_names:
        output_stream = gzip.open('{}.filtered.fastq.gz'.format(output_name), 'w')
        for line in fileinput.input(['{}.{}.filtered.fastq'.format(output_name, i) for i in range(args.jobs)]):
            output_stream.write(line.encode('utf-8'))
        for i in range(args.jobs):
            os.remove('{}.{}.filtered.fastq'.format(output_name, i))


if __name__ == '__main__':
    import sys
    sys.exit(main())
