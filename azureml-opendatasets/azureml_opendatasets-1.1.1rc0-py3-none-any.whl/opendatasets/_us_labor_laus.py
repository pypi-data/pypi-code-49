# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor laus."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_laus_blob_info import UsLaborLAUSBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborLAUS(UsLaborBase):
    """US labor laus class."""

    _blobInfo = UsLaborLAUSBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
