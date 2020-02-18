# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of Sample Iris Data."""

from .base_blob_info import BaseBlobInfo


class SampleIrisBlobInfo(BaseBlobInfo):
    """Blob info of Sample Iris Data."""

    def __init__(self):
        """Initialize Blob Info."""
        self.registry_id = 'sample-iris'
        self.blob_account_name = 'azureopendatastorage'
        self.blob_container_name = "sample"
        self.blob_relative_path = "datasets/Iris Data Set.csv"
        self.blob_sas_token = (
            "?st=2019-11-01T07%3A53%3A53Z&se=2219-11-02T07%3A53%3A00Z&sp=rl&sv=2018-03-28&sr=b"
            r"&sig=gQ%2FMQwvyvwr5T4kAnbngWzndkwZO0JtsjjOPQeWB3K0%3D")

    def get_url(self):
        """Get the url of Dataset."""
        self._update_blob_info()
        return 'https://%s.blob.core.windows.net/%s/%s' % (
            self.blob_account_name,
            self.blob_container_name,
            self.blob_relative_path)
