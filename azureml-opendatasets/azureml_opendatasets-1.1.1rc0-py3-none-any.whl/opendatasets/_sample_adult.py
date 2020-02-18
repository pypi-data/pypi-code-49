# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Sample Adult data."""

from azureml.core import Dataset
from azureml.data import TabularDataset
from azureml.data._dataset import _DatasetTelemetryInfo
from azureml.telemetry.activity import ActivityType

from ._utils.telemetry_utils import get_run_common_properties
from .accessories.public_data_telemetry import _PublicDataTelemetry
from .dataaccess._sample_adult_blob_info import SampleAdultBlobInfo


class SampleAdult:
    """Sample Adult data class."""
    _blobInfo = SampleAdultBlobInfo()

    @staticmethod
    def get_tabular_dataset(enable_telemetry: bool = True) -> TabularDataset:
        blobInfo = SampleAdult._blobInfo
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
