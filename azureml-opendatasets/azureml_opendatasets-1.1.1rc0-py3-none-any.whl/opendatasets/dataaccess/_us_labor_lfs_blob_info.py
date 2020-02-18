# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US labor lfs data."""

from ._us_labor_base_blob_info import UsLaborBaseBlobInfo


class UsLaborLFSBlobInfo(UsLaborBaseBlobInfo):
    """Blob info of US labor lfs Data."""

    def __init__(self):
        """Initialize Blob Info."""
        super(UsLaborLFSBlobInfo, self).__init__()
        self.registry_id = 'us-labor-force-statistics'
        self.blob_relative_path = "lfs/"
