from typing import Iterable, Iterator
from lhc.binf.genomic_coordinate import GenomicInterval


def iter_bed(lines: Iterable[str]) -> Iterator[GenomicInterval]:
    for line in lines:
        if line.startswith('#'):
            continue
        parts = line.rstrip('\r\n').split('\t')
        name = parts[3] if len(parts) > 3 else ''
        score = parts[4] if len(parts) > 4 else ''
        strand = parts[5] if len(parts) > 5 else '+'
        yield GenomicInterval(int(parts[1]) - 1, int(parts[2]),
                              chromosome=parts[0],
                              strand=strand,
                              data={'gene_id': name, 'score': score})


def format_bed(interval: GenomicInterval) -> str:
    return '{chr}\t{start}\t{stop}\t{data[gene_id]}\t{data[score]}\t{strand}\n'.format(
        chr=interval.chromosome,
        start=interval.start.position + 1,
        stop=interval.stop.position,
        data=interval.data,
        strand=interval.strand)
