from typing import Iterable
from lhc.binf.genomic_coordinate import GenomicInterval, GenomicIntervalConverter


class GffConverter(GenomicIntervalConverter):

    COLUMNS = ['chromosome', 'source', 'feature', 'start', 'stop', 'score', 'strand', 'frame', 'attribute']
    EXTENSIONS = ['.gff', '.gff.gz']

    def __init__(self, lines: Iterable[str]):
        self.lines = lines

    def __iter__(self) -> Iterable[GenomicInterval]:
        for line in self.lines:
            yield self.parse(line)

    def parse(self, line) -> GenomicInterval:
        parts = line.rstrip('\r\n').split('\t')
        return GenomicInterval(int(parts[3]) - 1, int(parts[4]),
                               chromosome=parts[0],
                               strand=parts[6],
                               data={
                                   'source': parts[1],
                                   'type': parts[2],
                                   'score': parts[5],
                                   'phase': parts[7],
                                   'attr': GffConverter.parse_attributes(parts[8])
                               })

    @staticmethod
    def parse_attributes(line):
        attributes = {}
        for part in line.split(';'):
            if part:
                key, value = part.split('=', 1) if '=' in part else part
                attributes[key] = value.split(',')
        return attributes

    def format(self, interval: GenomicInterval):
        return '{}\t.\t.\t{}\t{}\n'.format(interval.chromosome, interval.start.position + 1, interval.stop.position)
