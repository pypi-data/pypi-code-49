import logging
import pandas as pd
from ..data.rawbeepfile import RawBeepFile
from ..data.nodelocationfile import NodeLocationFile

class NodeDataset:
    """dataframe for merged beep / node location"""
    def __init__(self, beep_filename, node_filename):
        """filenames of raw beep data and node location data"""
        logging.info('loading datasets from beep file:{};  node location file:{}'.format(beep_filename, node_filename))
        self.beeps = RawBeepFile(filename=beep_filename)
        self.nodes = NodeLocationFile(filename=node_filename)

        # merged location dataframe
        df = self.beeps.df.reset_index()
        df = df.merge(right=self.nodes.df, left_on='NodeId', right_on='NodeId')
        df = df.set_index('Time')
        delta = self.beeps.beep_count() - df.shape[0]
        if delta > 0:
            logging.warning('dropped {:,} records after merging node locations'.format(delta))
        self.df = df

    def save(self, filename, channel=None, tag_id=None):
        """merged beep / node location dataset to file; optionally save specific tag dataset"""
        df = self.merged_df
        if channel is not None:
            df = df[df.RadioId==channel]
        if tag_id is not None:
            df = df[df.TagId==tag_id]
        df.to_csv(filename)

    def channels(self):
        """return list of unique radio channels"""
        return sorted(self.df.RadioId.unique())