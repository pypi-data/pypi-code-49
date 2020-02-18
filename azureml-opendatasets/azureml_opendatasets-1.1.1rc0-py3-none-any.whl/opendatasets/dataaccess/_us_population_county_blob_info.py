# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of US population by county data."""

from ._us_population_base_blob_info import UsPopulationBaseBlobInfo


class UsPopulationCountyBlobInfo(UsPopulationBaseBlobInfo):
    """Blob info of US population by county Data."""

    def __init__(self):
        """Initialize Blob Info."""
        super(UsPopulationCountyBlobInfo, self).__init__()
        self.registry_id = 'us-decennial-census-county'
        self.blob_relative_path = "release/us_population_county/"
