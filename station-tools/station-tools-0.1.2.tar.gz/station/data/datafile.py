import pandas as pd
class DataFile:
    """generic csv data file abstraction"""
    def __init__(self, filename):
        """load filename into a pandas dataframe df"""
        self.filename = filename
        df = pd.read_csv(filename, dtype={'NodeId': str, 'TagId':str})
        self.df = self._clean_node_id(df)
        self.df = self._clean()

    def _clean(self):
        """logic for preparing the data frame for a given file type"""
        return self.df

    def _clean_node_id(self, df):
        """strip leading 0 from NodeId"""
        if 'NodeId' in df.columns:
            df.NodeId = df.NodeId.apply(lambda record: str(record).lstrip("0").upper())
        return df