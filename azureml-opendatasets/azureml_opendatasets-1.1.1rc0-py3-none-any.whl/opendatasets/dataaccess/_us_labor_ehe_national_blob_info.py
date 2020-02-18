# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US labor ehe national data."""

from ._us_labor_base_blob_info import UsLaborBaseBlobInfo


class UsLaborEHENationalBlobInfo(UsLaborBaseBlobInfo):
    """Blob info of US labor ehe national Data."""

    def __init__(self):
        """Initialize Blob Info."""
        super(UsLaborEHENationalBlobInfo, self).__init__()
        self.registry_id = 'us-employment-hours-earnings-national'
        self.blob_relative_path = "ehe_national/"
