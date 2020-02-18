# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Boston city safety."""

from .dataaccess._boston_safety_blob_info import BostonSafetyBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor
from ._city_safety import CitySafety
from datetime import datetime
from dateutil import parser


class BostonSafety(CitySafety):
    """Boston city safety class."""

    default_start_date = parser.parse('2001-01-01')
    default_end_date = datetime.today()

    """const instance of blobInfo."""
    _blobInfo = BostonSafetyBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
