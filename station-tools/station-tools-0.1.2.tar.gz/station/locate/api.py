import logging
import utm
import pandas as pd

from . import nodedataset

class LocationApi:
    """utility for localizing tags in merged beep/node dataset"""
    def __init__(self, beep_filename, node_filename):
        """filenames of raw beep data and node location data"""
        self.nodedata = nodedataset.NodeDataset(beep_filename, node_filename) 
        # ez reference
        self.merged_df = self.nodedata.df

        # assume utm zone, letter from first record
        self.zone = self.merged_df.iloc[0].zone
        self.letter = self.merged_df.iloc[0].letter

    def weighted_average(self, freq, tag_id, channel):
        """generate weighted average location dataset for given channel, tag_id and frequency
        return a dataframe
        """
        filtered_df = self.merged_df[self.merged_df.TagId==tag_id]
        filtered_df = filtered_df[filtered_df.RadioId==channel]

        # resample to given frequency
        rs = filtered_df.resample(freq)
        mean_df = rs.mean()
        nunique_df = rs.nunique()
        count_df = rs.count()

        lats = []
        lngs = []
        for i, record in mean_df.iterrows():
            try:
                lat,lng = utm.to_latlon(record.node_x, record.node_y, self.zone, self.letter)
                lats.append(lat)
                lngs.append(lng)
            except:
                lats.append(None)
                lngs.append(None)

        out_df = pd.DataFrame({
            'lat': lats,
            'lng': lngs,
            'easting': mean_df.node_x,
            'northing': mean_df.node_y,
            'count': count_df.TagRSSI,
            'unique_nodex': nunique_df.NodeId,
        }, index=mean_df.index)

        # mean x,y from weighted node_x, node_y dataframe
        return out_df
