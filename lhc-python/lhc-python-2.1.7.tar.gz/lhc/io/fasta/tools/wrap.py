import argparse
import sys

from typing import Generator, IO, Iterator
from lhc.io import open_file


def wrap(input: IO, *, width: int, chunk_size=2 ** 16) -> Iterator[str]:
    chunk = ''
    for next_chunk in iter_chunks(input, chunk_size):
        chunk += next_chunk
        it = split_chunk(chunk, width)
        while True:
            try:
                yield next(it)
            except StopIteration as e:
                chunk = e.value
                break
    yield chunk


def iter_chunks(input: IO, chunk_size: int) -> Iterator[str]:
    chunk = input.read(chunk_size)
    while chunk != '':
        yield chunk
        chunk = input.read(chunk_size)


def split_chunk(chunk: str, width: int) -> Generator[str, None, str]:
    line = ''
    for part in chunk.splitlines(keepends=True):
        if part.startswith('>'):
            if line:
                yield line
            if part.endswith('\n'):
                yield part.strip()
                line = ''
            else:
                line = part
        else:
            line += part.strip()
            for i in range(len(line) // width):
                yield line[i * width:(i + 1) * width]
            line = line[len(line) - (len(line) % width):]
    return line


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser():
    return define_parser(argparse.ArgumentParser())


def define_parser(parser):
    add_arg = parser.add_argument
    add_arg('input', nargs='?')
    add_arg('output', nargs='?')
    add_arg('-c', '--chunk-size', default=2 ** 16, type=int,
            help='The number of bytes to read at a time.')
    add_arg('-w', '--width', default=80, type=int,
            help='The maximum length of a sequence line (default: 80).')
    parser.set_defaults(func=init_wrap)
    return parser


def init_wrap(args):
    with open_file(args.input) as input, open_file(args.output, 'w') as output:
        for line in wrap(input, width=args.width, chunk_size=args.chunk_size):
            output.write(line)
            output.write('\n')


if __name__ == '__main__':
    sys.exit(main())
