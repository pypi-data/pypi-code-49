# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US labor cpi data."""

from ._us_labor_base_blob_info import UsLaborBaseBlobInfo


class UsLaborCPIBlobInfo(UsLaborBaseBlobInfo):
    """Blob info of US labor cpi Data."""

    def __init__(self):
        """Initialize Blob Info."""
        super(UsLaborCPIBlobInfo, self).__init__()
        self.registry_id = 'us-consumer-price-index'
        self.blob_relative_path = "cpi/"
