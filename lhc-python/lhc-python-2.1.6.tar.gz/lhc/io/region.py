from typing import Iterable, Iterator
from lhc.binf.genomic_coordinate import GenomicInterval


def iter_region(lines: Iterable[str]) -> Iterator[GenomicInterval]:
    for line in lines:
        chromosome, interval = line.split(':', 1)
        start, stop = interval.split('-')
        yield GenomicInterval(int(start) - 1, int(stop), chromosome=chromosome)


def format_region(interval: GenomicInterval) -> str:
    return '{chr}:{start}-{stop}'.format(
        chr=interval.chromosome,
        start=interval.start.position + 1,
        stop=interval.stop.position)
