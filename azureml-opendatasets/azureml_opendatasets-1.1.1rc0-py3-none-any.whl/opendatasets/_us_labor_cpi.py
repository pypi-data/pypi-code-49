# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor cpi."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_cpi_blob_info import UsLaborCPIBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborCPI(UsLaborBase):
    """US labor cpi class."""

    _blobInfo = UsLaborCPIBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
