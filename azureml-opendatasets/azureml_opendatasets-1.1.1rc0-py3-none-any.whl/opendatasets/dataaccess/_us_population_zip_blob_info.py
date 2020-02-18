# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US population by zip data."""

from ._us_population_base_blob_info import UsPopulationBaseBlobInfo


class UsPopulationZipBlobInfo(UsPopulationBaseBlobInfo):
    """Blob info of US population by zip Data."""

    def __init__(self):
        """Initialize Blob Info."""
        super(UsPopulationZipBlobInfo, self).__init__()
        self.registry_id = 'us-decennial-census-zip'
        self.blob_relative_path = "release/us_population_zip/"
