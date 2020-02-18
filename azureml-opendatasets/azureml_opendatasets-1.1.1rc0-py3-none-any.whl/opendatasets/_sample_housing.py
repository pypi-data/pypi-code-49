# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Sample Boston housing data."""

from azureml.core import Dataset
from azureml.data import TabularDataset
from azureml.data._dataset import _DatasetTelemetryInfo
from azureml.telemetry.activity import ActivityType

from ._utils.telemetry_utils import get_run_common_properties
from .accessories.public_data_telemetry import _PublicDataTelemetry
from .dataaccess._sample_housing_blob_info import SampleBostonHousingBlobInfo


class SampleHousing:
    """Sample Boston hoursing data class."""
    _blobInfo = SampleBostonHousingBlobInfo()

    @staticmethod
    def get_tabular_dataset(enable_telemetry: bool = True) -> TabularDataset:
        blobInfo = SampleHousing._blobInfo
        url_path = blobInfo.get_url()
        if enable_telemetry:
            log_properties = get_run_common_properties()
            log_properties['RegistryId'] = blobInfo.registry_id
            log_properties['Path'] = url_path
            log_properties['ActivityType'] = ActivityType.PUBLICAPI
            ds = Dataset.Tabular.from_delimited_files(path=url_path)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            _PublicDataTelemetry.log_event('get_tabular_dataset', **log_properties)
            return ds
        else:
            ds = Dataset.Tabular.from_delimited_files(path=url_path)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            return ds
