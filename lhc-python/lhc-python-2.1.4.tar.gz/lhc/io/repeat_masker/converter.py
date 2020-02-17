from collections import Counter
from typing import Iterable, Iterator
from lhc.binf.genomic_coordinate import GenomicInterval, GenomicIntervalConverter


class RepeatMaskerConverter(GenomicIntervalConverter):

    COLUMNS = ['score', 'divergence', 'deletion', 'insertion', 'chromosome', 'start', 'end', 'query_left', 'strand',
               'subfamily', 'class/family', 'match_start', 'match_end', 'match_left', 'id']
    EXTENSIONS = ['.fa.out', '.fa.out.gz']

    def __init__(self, lines: Iterator[str]):
        self.lines = lines
        self.transcript_ids = Counter()
        self.unknown_genes = 0

    def __iter__(self) -> Iterable[GenomicInterval]:
        next(self.lines)
        next(self.lines)
        next(self.lines)
        for line in self.lines:
            yield self.parse(line)

    def parse(self, line):
        parts = line.rstrip('\r\n').split()
        class_, *family = parts[10].split('/', 1)
        try:
            gene_id = parts[14]
        except IndexError:
            self.unknown_genes += 1
            gene_id = 'unknown_{}'.format(self.unknown_genes)
        transcript_id = '{}.1'.format(gene_id)
        self.transcript_ids[transcript_id] += 1
        exon_number = self.transcript_ids[transcript_id]
        exon_id = '{}.{}'.format(transcript_id, exon_number)
        return GenomicInterval(
            int(parts[5]) - 1,
            int(parts[6]),
            chromosome=parts[4],
            strand='+' if parts[8] == '+' else '-',
            data={'score': parts[0], 'divergence': parts[1], 'deletion': parts[2], 'insertion': parts[3],
                  'subfamily_id': parts[9], 'class_id': class_, 'family_id': ''.join(family), 'gene_id': gene_id,
                  'transcript_id': transcript_id, 'source': 'RepeatMasker', 'feature': 'repeat_element', 'frame': '0',
                  'exon_id': exon_id, 'exon_number': exon_number})

    def format(self, interval: GenomicInterval):
        raise NotImplementedError('This function has not yet been implemented.')
