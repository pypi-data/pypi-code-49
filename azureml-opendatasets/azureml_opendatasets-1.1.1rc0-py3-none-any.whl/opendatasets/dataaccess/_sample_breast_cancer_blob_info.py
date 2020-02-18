# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of Sample Breast Cancer Wisconsin Data."""

from .base_blob_info import BaseBlobInfo


class SampleBreastCancerBlobInfo(BaseBlobInfo):
    """Blob info of Sample Breast Cancer Wisconsin Data."""

    def __init__(self):
        """Initialize Blob Info."""
        self.registry_id = 'sample-breast-cancer'
        self.blob_account_name = 'azureopendatastorage'
        self.blob_container_name = "sample"
        self.blob_relative_path = "datasets/Breast Cancer Wisconsin Data Set.csv"
        self.blob_sas_token = (
            "?st=2019-11-01T08%3A02%3A18Z&se=2190-11-02T08%3A02%3A00Z&sp=rl&sv=2018-03-28&sr=b"
            r"&sig=Jr8vda%2B9dcxKDzrQpIWVvIWjkaHsazJ0XyX55wZ0ApI%3D")

    def get_url(self):
        """Get the url of Dataset."""
        self._update_blob_info()
        return 'https://%s.blob.core.windows.net/%s/%s' % (
            self.blob_account_name,
            self.blob_container_name,
            self.blob_relative_path)
