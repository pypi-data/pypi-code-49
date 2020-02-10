import pysam

from lhc.io.bed.iterator import BedLineIterator


class IndexedBedFile(object):
    def __init__(self, filename):
        self.tabix_file = pysam.TabixFile(filename)
        self.is_ucsc = self.tabix_file.contigs[0].startswith('chr')

    def __getitem__(self, item):
        """
        lhc-python aware getter. Will convert chromosome to a string and detect if a genomic position or interval is
        passed as key.
        :param item:
        :return:
        """
        if hasattr(item, 'start'):
            return self.fetch(str(item.chromosome), item.start.position, item.stop.position)
        return self.fetch(str(item.chromosome), item.position, item.position + 1)

    def fetch(self, chromosome, start, stop):
        if self.is_ucsc and not chromosome.startswith('chr'):
            chromosome = 'chr' + chromosome
        elif not self.is_ucsc and chromosome.startswith('chr'):
            chromosome = chromosome[3:]
        return [BedLineIterator.parse_line(line) for line in self.tabix_file.fetch(chromosome, start, stop)]
