# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""NOAA GFS weather."""

from datetime import datetime
from dateutil import parser
from pyspark.sql.functions import col, udf
from typing import List, Optional

from ._opendataset_factory import TabularOpenDatasetFactory
from .accessories.location_time_public_data import LocationTimePublicData
from .dataaccess._noaa_gfs_weather_blob_info import NoaaGfsWeatherBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor
from .dataaccess.dataset_partition_prep import prep_partition_year_month_day
from .dataaccess.pandas_data_load_limit import PandasDataLoadLimitToDay
from .environ import SparkEnv, PandasEnv

from multimethods import multimethod


class NoaaGfsWeather(LocationTimePublicData, TabularOpenDatasetFactory):
    """NOAA GFS forecast weather class."""

    default_start_date = parser.parse('2018-01-01')
    default_end_date = datetime.today()

    """const instance of blobInfo."""
    _blobInfo = NoaaGfsWeatherBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)

    time_column_name = 'currentDatetime'
    latitude_column_name = 'latitude'
    longitude_column_name = 'longitude'
    id = 'ID'

    mandatory_columns = [
        time_column_name,
        latitude_column_name,
        longitude_column_name]

    partition_prep_func = prep_partition_year_month_day
    fine_grain_timestamp = time_column_name

    def __init__(
            self,
            start_date: datetime = default_start_date,
            end_date: datetime = default_end_date,
            cols: Optional[List[str]] = None,
            limit: Optional[int] = -1,
            enable_telemetry: bool = True):
        """
        Initialize filtering fields.

        :param start_date: start date you'd like to query inclusively.
        :type start_date: datetime
        :param end_date: end date you'd like to query inclusively.
        :type end_date: datetime
        :param cols: a list of column names you'd like to retrieve. None will get all columns.
        :type cols: List[str]
        :param limit: to_pandas_dataframe() will load only "limit" days of data. -1 means no limit.
        :type limit: int
        :param enable_telemetry: whether to send telemetry
        :type enable_telemetry: bool
        """
        self._registry_id = self._blobInfo.registry_id
        self.path = self._blobInfo.get_data_wasbs_path()
        self.start_date = start_date\
            if (self.default_start_date < start_date)\
            else self.default_start_date
        self.end_date = end_date\
            if (end_date is None or self.default_end_date > end_date)\
            else self.default_end_date
        super(NoaaGfsWeather, self).__init__(cols, enable_telemetry=enable_telemetry)
        self.limit = limit
        if enable_telemetry:
            self.log_properties['StartDate'] = self.start_date.strftime("%Y-%m-%dT%H:%M:%S")\
                if self.start_date is not None else ''
            self.log_properties['EndDate'] = self.end_date.strftime("%Y-%m-%dT%H:%M:%S")\
                if self.end_date is not None else ''
            self.log_properties['Path'] = self.path

    @multimethod(SparkEnv, datetime, datetime)
    def filter(self, env, min_date, max_date):
        """Filter time.

        :param min_date: min date
        :param max_date: max date

        :return: filtered data frame.
        """
        self.data = self.data.na.drop(how='all', subset=self.cols).na.drop(
            how='any', subset=[self.longitude_column_name, self.latitude_column_name])

        # create unique id for weather stations, hardcoded due to id issue in weather dataset
        unique_id_udf = udf(lambda x, y: '-'.join([x, y]))
        self.data = self.data.withColumn(
            self.id, unique_id_udf(col(self.latitude_column_name), col(self.longitude_column_name)))

        ds = super(NoaaGfsWeather, self).filter(env, min_date, max_date)
        return ds.select(self.selected_columns + [self.id])

    @multimethod(PandasEnv, datetime, datetime)
    def filter(self, env, min_date, max_date):
        """Filter time.

        :param min_date: min date
        :param max_date: max date

        :return: filtered data frame.
        """
        ds = super(NoaaGfsWeather, self).filter(env, min_date, max_date)
        ds = ds.dropna(how='all', axis=0, subset=self.cols).dropna(
            how='any', axis=0, subset=[self.longitude_column_name, self.latitude_column_name])

        # create unique id for weather stations, hardcoded due to id issue in weather dataset
        ds[self.id] = ds[self.latitude_column_name] + '-' + ds[self.longitude_column_name]

        return ds[self.selected_columns + [self.id]]

    def get_pandas_limit(self):
        """Get instance of pandas data load limit class."""
        return PandasDataLoadLimitToDay(self.start_date, self.end_date, limit=self.limit)

    def _to_spark_dataframe(self, activity_logger):
        """To spark dataframe.

        :param activity_logger: activity logger

        :return: SPARK dataframe
        """
        descriptor = BlobParquetDescriptor(self._blobInfo)
        return descriptor.get_spark_dataframe(self)

    def _to_pandas_dataframe(self, activity_logger):
        """
        Get pandas dataframe.

        :param activity_logger: activity logger

        :return: Pandas dataframe based on its own filters.
        :rtype: pandas.DataFrame
        """
        descriptor = BlobParquetDescriptor(self._blobInfo)
        return descriptor.get_pandas_dataframe(self)
