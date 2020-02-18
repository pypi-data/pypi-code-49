# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor ehe state."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_ehe_state_blob_info import UsLaborEHEStateBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborEHEState(UsLaborBase):
    """US labor ehe state class."""

    _blobInfo = UsLaborEHEStateBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
