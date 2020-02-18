# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor ehe national."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_ehe_national_blob_info import UsLaborEHENationalBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborEHENational(UsLaborBase):
    """US labor ehe national class."""

    _blobInfo = UsLaborEHENationalBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
