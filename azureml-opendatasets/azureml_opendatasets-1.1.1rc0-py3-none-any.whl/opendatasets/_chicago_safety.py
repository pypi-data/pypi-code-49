# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Chicago safety."""

from .dataaccess._chicago_safety_blob_info import ChicagoSafetyBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor
from ._city_safety import CitySafety
from datetime import datetime
from dateutil import parser


class ChicagoSafety(CitySafety):
    """Chicago city safety class."""

    default_start_date = parser.parse('2000-01-01')
    default_end_date = datetime.today()

    """const instance of blobInfo."""
    _blobInfo = ChicagoSafetyBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
