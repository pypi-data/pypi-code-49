import logging
import pandas as pd
from ..data.rawbeepfile import RawBeepFile
from ..data.nodelocationfile import NodeLocationFile

logging.basicConfig(level=logging.INFO)
class BeepLocationDataset:
    """dataframe for merged beep / node location"""
    def __init__(self, beep_filename, node_filename):
        """filenames of raw beep data and node location data"""
        logging.info('loading datasets from beep file:{};  node location file:{}'.format(beep_filename, node_filename))
        self.beeps = RawBeepFile(filename=beep_filename)
        self.nodes = NodeLocationFile(filename=node_filename)
        # merged location dataframe
        self.df = None
        self._merge()

    def _merge(self):
        """merge beep dataset with node location dataset"""
        df = self.beeps.df.reset_index()
        print(self.nodes.df)
        print(df.NodeId.unique())
        df = df.merge(right=self.nodes.df, left_on='NodeId', right_on='NodeId')
        df = df.set_index('Time')
        delta = self.beeps.beep_count() - df.shape[0]
        if delta > 0:
            logging.error('dropped {:,} of {:,} records after merging node locations'.format(delta, self.beeps.beep_count()))
        self.df = df