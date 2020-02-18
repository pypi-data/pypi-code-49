# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of MNIST Data."""

from .base_blob_info import BaseBlobInfo
from azure.storage.blob import BlockBlobService


class MNISTBlobInfo(BaseBlobInfo):
    """Blob info of MNIST Data."""

    def __init__(self):
        """Initialize Blob Info."""
        self.registry_id = 'mnist'
        self.blob_account_name = 'azureopendatastorage'
        self.blob_container_name = "mnist"
        self.blob_relative_path = "processed/"
        self.blob_sas_token = (
            "?st=2019-09-17T03%3A25%3A12Z&se=9999-09-18T01%3A25%3A00Z&sp=rl&sv=2018-03-28&sr=c"
            # [SuppressMessage("Microsoft.Security", "CS002:SecretInNextLine", Justification="Offline sas token")]
            r"&sig=E4h6PxSrKs8vAt7fBGMeGHA7UbTeJDp0gihvMOKZbNg%3D")

    def get_csv_url(self, dataset_filter='all'):
        """Get the url of Dataset."""
        self._update_blob_info()
        block_service = BlockBlobService(account_name=self.blob_account_name)
        blob_list = block_service.list_blobs(self.blob_container_name)
        target_urls = []
        for blob in blob_list:
            if dataset_filter == 'all':
                if(blob.name.endswith('processed/merged.csv')):
                    target_urls.append('https://%s.blob.core.windows.net/%s/%s' % (
                        self.blob_account_name,
                        self.blob_container_name,
                        blob.name))
            elif dataset_filter == 'train':
                if(blob.name.endswith('processed/train.csv')):
                    target_urls.append('https://%s.blob.core.windows.net/%s/%s' % (
                        self.blob_account_name,
                        self.blob_container_name,
                        blob.name))
            elif dataset_filter == 'test':
                if(blob.name.endswith('processed/t10k.csv')):
                    target_urls.append('https://%s.blob.core.windows.net/%s/%s' % (
                        self.blob_account_name,
                        self.blob_container_name,
                        blob.name))
        return target_urls

    def get_raw_url(self, dataset_filter='all'):
        """Get the url of Dataset."""
        self._update_blob_info()
        if dataset_filter == 'all':
            return 'https://%s.blob.core.windows.net/%s/**/*.gz' % (
                self.blob_account_name,
                self.blob_container_name)
        elif dataset_filter == 'train':
            return 'https://%s.blob.core.windows.net/%s/**/train-*.gz' % (
                self.blob_account_name,
                self.blob_container_name)
        elif dataset_filter == 'test':
            return 'https://%s.blob.core.windows.net/%s/**/t10k-*.gz' % (
                self.blob_account_name,
                self.blob_container_name)
