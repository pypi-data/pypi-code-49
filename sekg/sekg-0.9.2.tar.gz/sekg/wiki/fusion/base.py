from abc import abstractmethod

"""
fuse each concept with concept in Wikidata.
"""


class GenericKGFusion:
    @abstractmethod
    def fuse(self):
        """
        fuse the given term with the concept in wikidata. e.g. link 'JSON' to "(JavaScript Object Notation) https://www.wikidata.org/wiki/Q2063"
        """
        pass
