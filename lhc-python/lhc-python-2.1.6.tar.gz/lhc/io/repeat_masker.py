from collections import Counter
from typing import Iterable, Iterator
from lhc.binf.genomic_coordinate import GenomicInterval


def iter_repeat_masker(lines: Iterable[str]) -> Iterator[GenomicInterval]:
    transcript_ids = Counter()
    unknown_genes = 0

    lines = iter(lines)
    next(lines)
    next(lines)
    next(lines)
    for line in lines:
        parts = line.rstrip('\r\n').split()
        class_, *family = parts[10].split('/', 1)
        try:
            gene_id = parts[14]
        except IndexError:
            unknown_genes += 1
            gene_id = 'unknown_{}'.format(unknown_genes)
        transcript_id = '{}.1'.format(gene_id)
        transcript_ids[transcript_id] += 1
        exon_number = transcript_ids[transcript_id]
        exon_id = '{}.{}'.format(transcript_id, exon_number)
        yield GenomicInterval(
            int(parts[5]) - 1,
            int(parts[6]),
            chromosome=parts[4],
            strand='+' if parts[8] == '+' else '-',
            data={'score': parts[0], 'divergence': parts[1], 'deletion': parts[2], 'insertion': parts[3],
                  'subfamily_id': parts[9], 'class_id': class_, 'family_id': ''.join(family), 'gene_id': gene_id,
                  'transcript_id': transcript_id, 'source': 'RepeatMasker', 'feature': 'repeat_element', 'frame': '0',
                  'exon_id': exon_id, 'exon_number': exon_number})
