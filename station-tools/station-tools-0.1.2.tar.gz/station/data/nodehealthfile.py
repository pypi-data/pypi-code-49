import pandas as pd
from . import datafile

class NodeHealthFile(datafile.DataFile):
    """Node Health File"""
    def __init__(self, filename):
        super(NodeHealthFile, self).__init__(filename)

    def _clean(self):
        pass