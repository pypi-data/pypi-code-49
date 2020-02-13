import pandas as pd
import utm
from . import datafile

class NodeLocationFile(datafile.DataFile):
    """Node Location File Encapsulation
    expected fields: NodeId, lat, lng"""
    def __init__(self, filename):
        super(NodeLocationFile, self).__init__(filename)

    def _clean(self):
        """rename lat,lng to node_lat, node_lng; append utm"""
        self.df = self.df.rename(columns={'lat': 'node_lat', 'lng': 'node_lng'})
        self.df = self.append_utm(self.df)
        return self.df

    def append_utm(self, df):
        """append utm x,y,zone,letter to dataframe"""
        xs = []
        ys = []
        zones = []
        letters = []
        for i, record in df.iterrows():
            (x,y,zone,letter) = utm.from_latlon(record.node_lat, record.node_lng)
            xs.append(x)
            ys.append(y)
            zones.append(zone)
            letters.append(letter)
        df['node_x'] = xs
        df['node_y'] = ys
        df['zone'] = zones
        df['letter'] = letters
        return df

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    data = NodeLocationFile(filename)
    print(data.df)