# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US labor ppi commodity data."""

from ._us_labor_base_blob_info import UsLaborBaseBlobInfo


class UsLaborPPICommodityBlobInfo(UsLaborBaseBlobInfo):
    """Blob info of US labor ppi commodity Data."""

    def __init__(self):
        """Initialize Blob Info."""
        super(UsLaborPPICommodityBlobInfo, self).__init__()
        self.registry_id = 'us-producer-price-index-commodities'
        self.blob_relative_path = "ppi_commodity/"
