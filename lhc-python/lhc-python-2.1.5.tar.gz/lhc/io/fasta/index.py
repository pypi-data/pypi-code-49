import pysam


class IndexedFastaSet(object):
    def __init__(self, filename):
        self.tabix_index = pysam.FastaFile(filename)
        self.is_ucsc = self.tabix_index.references[0].startswith('chr')

    def __getitem__(self, item):
        if hasattr(item, 'start'):
            return self.fetch(str(item.chromosome), item.start.position, item.stop.position)
        return self.fetch(str(item.chromosome), item.position, item.position + 1)

    def fetch(self, chromosome, start, stop):
        if self.is_ucsc and not chromosome.startswith('chr'):
            chromosome = 'chr' + chromosome
        elif not self.is_ucsc and chromosome.startswith('chr'):
            chromosome = chromosome[3:]
        return self.tabix_index.fetch(chromosome, start, stop)
