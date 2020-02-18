# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US population by county."""

from ._opendataset_factory import TabularOpenDatasetFactory
from .accessories.public_data import PublicData
from .dataaccess._us_population_county_blob_info import UsPopulationCountyBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor
from .dataaccess.pandas_data_load_limit import PandasDataLoadLimitNone


class UsPopulationCounty(PublicData, TabularOpenDatasetFactory):
    """US population by county class."""

    _blobInfo = UsPopulationCountyBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)

    def __init__(
            self,
            enable_telemetry: bool = True):
        """
        Initialize.

        :param enable_telemetry: whether to send telemetry
        :type enable_telemetry: bool
        """
        self._registry_id = self._blobInfo.registry_id
        self.path = self._blobInfo.get_data_wasbs_path()

        super(UsPopulationCounty, self).__init__(cols=None, enable_telemetry=enable_telemetry)
        if enable_telemetry:
            self.log_properties['Path'] = self.path

    def get_pandas_limit(self):
        """Get instance of pandas data load limit class."""
        return PandasDataLoadLimitNone()

    def _to_spark_dataframe(self, activity_logger):
        """To spark dataframe.

        :param activity_logger: activity logger

        :return: SPARK dataframe
        """
        descriptor = BlobParquetDescriptor(self._blobInfo)
        ds = descriptor.get_spark_dataframe(self)
        return ds

    def _to_pandas_dataframe(self, activity_logger):
        """
        Get pandas dataframe.

        :param activity_logger: activity logger

        :return: Pandas dataframe based on its own filters.
        :rtype: pandas.DataFrame
        """
        descriptor = BlobParquetDescriptor(self._blobInfo)
        ds = descriptor.get_pandas_dataframe(self)
        return ds
