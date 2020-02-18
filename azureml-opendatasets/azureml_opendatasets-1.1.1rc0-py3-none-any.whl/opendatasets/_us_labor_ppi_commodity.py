# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor ppi commodity."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_ppi_commodity_blob_info import UsLaborPPICommodityBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborPPICommodity(UsLaborBase):
    """US labor ppi commodity class."""

    _blobInfo = UsLaborPPICommodityBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
