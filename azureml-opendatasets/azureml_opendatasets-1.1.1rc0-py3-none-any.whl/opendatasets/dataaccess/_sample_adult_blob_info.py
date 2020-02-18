# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of Sample Adult Data."""

from .base_blob_info import BaseBlobInfo


class SampleAdultBlobInfo(BaseBlobInfo):
    """Blob info of Sample Adult Data."""

    def __init__(self):
        """Initialize Blob Info."""
        self.registry_id = 'sample-adult'
        self.blob_account_name = 'azureopendatastorage'
        self.blob_container_name = "sample"
        self.blob_relative_path = "datasets/Adult Data Set.csv"
        self.blob_sas_token = (
            "?st=2019-11-01T08%3A00%3A33Z&se=2295-11-02T08%3A00%3A00Z&sp=rl&sv=2018-03-28&sr=b"
            r"&sig=ACS5GdlcBnb40%2FGTWW7soe0Z%2BZe41nC%2BjIcMsSFWoU4%3D")

    def get_url(self):
        """Get the url of Dataset."""
        self._update_blob_info()
        return 'https://%s.blob.core.windows.net/%s/%s' % (
            self.blob_account_name,
            self.blob_container_name,
            self.blob_relative_path)
