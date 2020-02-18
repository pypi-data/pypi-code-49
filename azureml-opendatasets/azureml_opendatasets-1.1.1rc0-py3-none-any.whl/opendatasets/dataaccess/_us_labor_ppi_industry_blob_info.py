# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US labor ppi industry data."""

from ._us_labor_base_blob_info import UsLaborBaseBlobInfo


class UsLaborPPIIndustryBlobInfo(UsLaborBaseBlobInfo):
    """Blob info of US labor ppi industry Data."""

    def __init__(self):
        """Initialize Blob Info."""
        super(UsLaborPPIIndustryBlobInfo, self).__init__()
        self.registry_id = 'us-producer-price-index-industry'
        self.blob_relative_path = "ppi_industry/"
