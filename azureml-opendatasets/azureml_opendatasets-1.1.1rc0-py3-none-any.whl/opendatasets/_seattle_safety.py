# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Seattle safety."""

from datetime import datetime
from dateutil import parser

from .dataaccess._seattle_safety_blob_info import SeattleSafetyBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor
from ._city_safety import CitySafety


class SeattleSafety(CitySafety):
    """Seattle city safety class."""

    default_start_date = parser.parse('2000-01-01')
    default_end_date = datetime.today()

    """const instance of blobInfo."""
    _blobInfo = SeattleSafetyBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
