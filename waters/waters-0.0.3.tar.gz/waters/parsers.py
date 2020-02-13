import xml.etree.cElementTree as ET
from collections import Counter
import pandas as pd


class XMLparser(object):
    """General xml parsing capabilities."""
    def __init__(self, data_path):
        self.tree = ET.parse(data_path)
        self.root = self.tree.getroot()

    def get_tag_counts(self):
        """Count the top level tags.

        Returns:
            Counter: count of each first-level tag.
        """
        return Counter(c.tag for c in self.root)



class iaDBsXMLparser(XMLparser):
    """Parser of iaDBs xml files."""
    def prot_ids(self):
        """Get the number each protein id occured in the XML file.

        Returns:
            Counter: counts of id's.
        """
        return Counter(p.attrib['ID'] for p in self.root.findall('HIT/PROTEIN'))

    def proteins(self):
        """Get all protein information from the XML file.
    
        Returns:
            pd.DataFrame: Protein information.
        """
        return pd.DataFrame(p.attrib for p in self.root.findall('HIT/PROTEIN'))

    def products(self):
        """Get all products information from the XML file.

        Returns:
            pd.DataFrame: Products information.
        """
        return pd.DataFrame(p.attrib for p in self.root.findall('PRODUCT'))

    def parameters(self):
        """Get iaDBs parameters.

        Returns:
            dict: Parameter-value.
        """
        return dict(p.attrib.values() for p in self.root.findall('PARAMS/PARAM'))

    def query_masses(self):
        """Get all query mass information from the XML file.

        Returns:
            pd.DataFrame: Products information.
        """
        return pd.DataFrame(p.attrib for p in self.root.findall('QUERY_MASS'))

    def count_proteins_per_hit(self):
        """Count how many times a given number of proteins were assigned to one hit.

        Returns:
            Counter: Distribution of proteins number per hit.
        """
        return Counter(len(h) for h in self.root.iter('HIT'))

    def info(self):
        """Return core information about the seach outcomes."""
        out = {}
        tag_counts = self.get_tag_counts()
        params = self.parameters()
        out['raw_file'] = params['RawFile']
        out['acquired_name'] = params['AcquiredName']
        out['sample_description'] = params['SampleDescription']
        out['queries_cnt'] = tag_counts['QUERY_MASS']
        out['hits_cnt'] = tag_counts['HIT']
        out['peptides_cnt'] = tag_counts['PEPTIDE']
        out['proteins_cnt'] = len(self.prot_ids())
        return out
