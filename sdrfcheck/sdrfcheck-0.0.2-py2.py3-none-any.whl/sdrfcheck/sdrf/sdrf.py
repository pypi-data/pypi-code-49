import pandas as pd

from sdrfcheck.sdrf.exceptions import LogicError
from sdrfcheck.sdrf.sdrf_schema import minimum_schema
from ebi.ols.api.client import OlsClient


class SdrfDataFrame(pd.DataFrame):

    @property
    def _constructor(self):
        """
        This method is makes it so our methods return an instance
        :return:
        """
        return SdrfDataFrame

    def get_sdrf_columns(self):
        """
        This method return the name of the columns of the SDRF.
        :return:
        """
        return self.columns

    @staticmethod
    def parse(sdrf_file: str):
        """
        Read an SDRF into a dataframe
        :param sdrf_file:
        :return:
        """

        df = pd.read_csv(sdrf_file, sep='\t')
        # Convert all columns and values in the dataframe to lowercase
        df = df.astype(str).apply(lambda x: x.str.lower())
        df.columns = map(str.lower, df.columns)

        return SdrfDataFrame(df)

    def validate(self):
        """
        Validate a corresponding SDRF
        :return:
        """
        errors = minimum_schema.validate(self)
        for error in errors:
            print(error)
