import pysam

from functools import lru_cache
from lhc.binf.genomic_coordinate.nested_genomic_interval import NestedGenomicInterval
from lhc.binf.genomic_coordinate.nested_genomic_interval_factory import NestedGenomicIntervalFactory
from lhc.io.gff import GffConverter


class IndexedGffFile(object):
    def __init__(self, filename, max_buffer=16):
        self.tabix_file = pysam.TabixFile(filename)
        self.buffer = {}
        self.max_buffer = max_buffer
        self.factory = NestedGenomicIntervalFactory()
        self.is_ucsc = self.tabix_file.contigs[0].startswith('chr')

    def __getitem__(self, key):
        if hasattr(key, 'start'):
            return self.fetch(str(key.chromosome), key.start.position, key.stop.position)
        return self.fetch(str(key.chromosome), key.position, key.position + 1)

    def fetch(self, chromosome, start, stop, type=None):
        if self.is_ucsc and not chromosome.startswith('chr'):
            chromosome = 'chr' + chromosome
        elif not self.is_ucsc and chromosome.startswith('chr'):
            chromosome = chromosome[3:]

        if type is None:
            features = []
            for line in self.tabix_file.fetch(chromosome, start, stop):
                parts = line.rstrip('\r\n').split('\t')
                features.append(NestedGenomicInterval(int(parts[3]) - 1, int(parts[4]), chromosome=parts[0], data={
                    'name': parts[2]
                }))
            return features

        genes = []
        for line in self.tabix_file.fetch(chromosome, start, stop):
            parts = line.rstrip('\r\n').split('\t')
            if parts[2] == type:
                genes.append((parts[0], int(parts[3]) - 1, int(parts[4])))

        features = []
        for chromosome, start, stop in genes:
            self.factory.reset()
            feature = self._get_feature(chromosome, start, stop)
            if feature is not None:
                features.append(feature)
        return features

    @lru_cache(128)
    def _get_feature(self, chromosome, start, stop):
        converter = GffConverter()
        for line in self.tabix_file.fetch(chromosome, start, stop):
            entry = converter.parse(line)
            self.factory.add_interval(entry, parents=_get_parent(line))
            if self.factory.has_complete_interval():
                feature = self.factory.get_complete_interval()
                if feature.start.position == start and feature.stop.position == stop:
                    return feature
        while len(self.factory.tops) > 0:
            feature = self.factory.get_complete_interval()
            if feature.start.position == start and feature.stop.position == stop:
                return feature
        return None
