from typing import Iterable, Iterator
from lhc.binf.genomic_coordinate import GenomicInterval


def iter_gtf(lines: Iterable[str]) -> Iterator[GenomicInterval]:
    for line in lines:
        parts = line.rstrip('\r\n').split('\t')
        attributes = parse_attributes(parts[8])
        attributes['source'] = parts[1]
        attributes['feature'] = parts[2]
        attributes['score'] = parts[5]
        attributes['frame'] = parts[7]
        yield GenomicInterval(int(parts[3]) - 1, int(parts[4]),
                              chromosome=parts[0],
                              strand=parts[6],
                              data=attributes)


def format_gtf(interval: GenomicInterval) -> str:
    attrs = {key: value for key, value in interval.data.items() if key not in {'source', 'feature', 'score', 'frame'}}
    return '{chr}\t{data[source]}\t{data[feature]}\t{start}\t{stop}\t{data[score]}\t{strand}\t{data[frame]}\t{attrs}'.format(
        chr=interval.chromosome,
        start=interval.start.position + 1,
        stop=interval.stop.position,
        strand=interval.strand,
        data=interval.data,
        attrs='; '.join('{} "{}"'.format(key, value) if isinstance(value, str) else '{} {}'.format(key, value) for key, value in attrs.items()))


def parse_attributes(line):
    parts = (part.strip() for part in line.split(';'))
    parts = [part.split(' ', 1) for part in parts if part != '']
    for part in parts:
        part[1] = part[1][1:-1] if part[1].startswith('"') else int(part[1])
    return dict(parts)
