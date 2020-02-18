# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor ppi industry."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_ppi_industry_blob_info import UsLaborPPIIndustryBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborPPIIndustry(UsLaborBase):
    """US labor ppi industry class."""

    _blobInfo = UsLaborPPIIndustryBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
