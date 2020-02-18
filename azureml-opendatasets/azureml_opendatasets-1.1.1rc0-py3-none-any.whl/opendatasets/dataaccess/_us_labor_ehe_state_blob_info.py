# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US labor ehe state data."""

from ._us_labor_base_blob_info import UsLaborBaseBlobInfo


class UsLaborEHEStateBlobInfo(UsLaborBaseBlobInfo):
    """Blob info of US labor ehe state Data."""

    def __init__(self):
        """Initialize Blob Info."""
        super(UsLaborEHEStateBlobInfo, self).__init__()
        self.registry_id = 'us-employment-hours-earnings-state'
        self.blob_relative_path = "ehe_state/"
