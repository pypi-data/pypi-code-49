# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Blob info of MNIST Data."""

from .base_blob_info import BaseBlobInfo


class OjSalesSimulatedBlobInfo(BaseBlobInfo):

    def __init__(self):
        self.registry_id = 'sample-oj-sales-simulated'
        self.blob_account_name = 'azureopendatastorage'
        self.blob_container_name = 'ojsales-simulatedcontainer'
        self.blob_relative_path = "oj_sales_data/"
        self.blob_sas_token = None

    def get_url(self):
        self._update_blob_info()
        return 'https://%s.blob.core.windows.net/%s/%s*.csv' % (
            self.blob_account_name,
            self.blob_container_name,
            self.blob_relative_path)
