import gzip

from collections import namedtuple
from typing import Iterable, Union
from lhc.binf.genomic_coordinate import GenomicInterval


class FastaFragmentIterator:

    __slots__ = ('_iterator', '_header', '_position')

    def __init__(self, iterator):
        self._iterator = iterator
        self._header = next(iterator).rstrip('\r\n')[1:]
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self._iterator)
        while line.startswith('>'):
            self._header = line.rstrip('\r\n')[1:]
            self._position = 0
            line = next(self._iterator)
        sequence = line.rstrip('\r\n')
        position = self._position
        self._position += len(sequence)
        return GenomicInterval(position, self._position, chromosome=self._header, data=sequence)

    def __getstate__(self):
        return self._iterator, self._header, self._position

    def __setstate__(self, state):
        self._iterator, self._header, self._position = state


class FastaEntry(namedtuple('FastaEntry', ('hdr', 'seq'))):
    def __str__(self):
        return '>{}\n{}\n'.format(self.hdr, self.seq)


def iter_fasta(input: Union[str, Iterable], comment='#') -> Iterable[FastaEntry]:
    iterator = input
    if isinstance(input, str):
        iterator = gzip.open(input, 'rt') if input.endswith('.gz') else open(input)

    line = next(iterator)
    while line.startswith(comment):
        line = next(iterator)
    if not line.startswith('>'):
        raise ValueError('Invalid fasta file format.')

    hdr = line.strip()[1:]
    seq = []
    for line in iterator:
        if line.startswith('>'):
            yield FastaEntry(hdr, ''.join(seq))
            hdr = line.strip()[1:]
            del seq[:]
        else:
            seq.append(line.strip())
    yield FastaEntry(hdr, ''.join(seq))

    if isinstance(input, str):
        iterator.close()
