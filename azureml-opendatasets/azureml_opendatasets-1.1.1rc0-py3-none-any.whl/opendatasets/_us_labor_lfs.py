# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor lfs."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_lfs_blob_info import UsLaborLFSBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborLFS(UsLaborBase):
    """US labor lfs class."""

    _blobInfo = UsLaborLFSBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
