# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""San Francisco crime."""

from datetime import datetime
from dateutil import parser

from .dataaccess._sanfrancisco_reported_crime_blob_info import SanFranciscoReportedCrimeBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor
from ._city_reported_crime import CityReportedCrime


class SanFranciscoReportedCrime(CityReportedCrime):
    """San Francisco city crime class."""

    default_start_date = parser.parse('2000-01-01')
    default_end_date = datetime.today()

    """const instance of blobInfo."""
    _blobInfo = SanFranciscoReportedCrimeBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
