from typing import Iterable
from lhc.binf.genomic_coordinate import GenomicInterval, GenomicIntervalConverter


class BedConverter(GenomicIntervalConverter):

    COLUMNS = ['chromosome', 'start', 'stop', 'name', 'score', 'strand', 'thickStart', 'thickEnd', 'itemRgb',
               'blockCount', 'blockSizes', 'blockStarts']
    EXTENSIONS = ['.bed', '.bed.gz']

    def __init__(self, lines: Iterable[str]):
        self.lines = lines

    def __iter__(self) -> Iterable[GenomicInterval]:
        for line in self.lines:
            yield self.parse(line)

    def parse(self, line):
        parts = line.rstrip('\r\n').split('\t')
        name = parts[3] if len(parts) > 3 else ''
        score = parts[4] if len(parts) > 4 else ''
        strand = parts[5] if len(parts) > 5 else '+'
        return GenomicInterval(int(parts[1]) - 1, int(parts[2]),
                               chromosome=parts[0],
                               strand=strand,
                               data={'name': name, 'score': score})

    def format(self, interval: GenomicInterval):
        return '{}\t{}\t{}\t{}\t{}\t{}\n'.format(interval.chromosome, interval.start.position + 1, interval.stop.position, interval.data['name'], interval.data['score'], interval.strand)
