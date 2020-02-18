# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of Sample Boston Housing Data."""

from .base_blob_info import BaseBlobInfo


class SampleBostonHousingBlobInfo(BaseBlobInfo):
    """Blob info of Sample Boston Housing Data."""

    def __init__(self):
        """Initialize Blob Info."""
        self.registry_id = 'sample-housing'
        self.blob_account_name = 'azureopendatastorage'
        self.blob_container_name = "sample"
        self.blob_relative_path = "datasets/Boston Housing Data.csv"
        self.blob_sas_token = (
            "?st=2019-11-01T08%3A03%3A28Z&se=2211-11-02T08%3A03%3A00Z&sp=rl&sv=2018-03-28&sr=b"
            r"&sig=6ICREoc3SMUfy0RkNm2rtWWUxnTk7jLd8OsHs1sQB7c%3D")

    def get_url(self):
        """Get the url of Dataset."""
        self._update_blob_info()
        return 'https://%s.blob.core.windows.net/%s/%s' % (
            self.blob_account_name,
            self.blob_container_name,
            self.blob_relative_path)
