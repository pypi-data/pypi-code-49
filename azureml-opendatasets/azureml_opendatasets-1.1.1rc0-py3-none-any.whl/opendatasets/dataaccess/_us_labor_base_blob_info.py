# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Base blob info of US labor data."""

from .base_blob_info import BaseBlobInfo


class UsLaborBaseBlobInfo(BaseBlobInfo):
    """Base blob info of US Data."""

    def __init__(self):
        """Initialize Blob Info."""
        self.registry_id = ''
        self.blob_account_name = 'azureopendatastorage'
        self.blob_container_name = "laborstatisticscontainer"
        self.blob_relative_path = ''
        self.blob_sas_token = (
            r"?st=2019-10-16T03%3A21%3A26Z&se=9999-10-17T03%3A21%3A00Z&sp=rl&sv=2018-03-28&sr=c"
            # [SuppressMessage("Microsoft.Security", "CS002:SecretInNextLine", Justification="Offline sas token")]
            r"&sig=5OsFSzyi5HUfKnVBaYVN9iLZBpdMmJzICiwHsfd3diY%3D")

    def get_url(self) -> str:
        """Get the url of Dataset."""
        self._update_blob_info()
        return 'https://%s.blob.core.windows.net/%s/%s%s' % (
            self.blob_account_name,
            self.blob_container_name,
            self.blob_relative_path,
            '*.parquet')
