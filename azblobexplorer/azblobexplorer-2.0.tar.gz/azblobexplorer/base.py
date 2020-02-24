from datetime import timedelta, datetime

from azure.storage.blob import BlobServiceClient, BlobSasPermissions, generate_blob_sas


class BlobBase:
    """

    .. versionadded:: 2.0

    """
    def __init__(self, account_name: str, account_key: str, container_name: str):
        """
        :param str account_name:
            Azure storage account name.
        :param str account_key:
            Azure storage key.
        :param str container_name:
            Azure storage container name, URL will be added automatically.
        """
        self.account_name = account_name
        self.account_key = account_key
        self.container_name = container_name

        block_blob_service = BlobServiceClient.from_connection_string(
            f"DefaultEndpointsProtocol=https;AccountName={self.account_name};AccountKey={self.account_key};EndpointSuffix=core.windows.net")
        self.container_client = block_blob_service.get_container_client(self.container_name)

    def generate_url(self, blob_name: str, read: bool = True, add: bool = False,
                     create: bool = False, write: bool = False, delete: bool = False,
                     sas: bool = False, access_time: int = 1) -> str:
        """
        Generate's blob URL. It can also generate Shared Access Signature (SAS) if ``sas=True``.

        :param bool write: Write access

            .. versionadded:: 2.0

        :param bool create: Create access

            .. versionadded:: 2.0

        :param bool add: Add access

            .. versionadded:: 2.0

        :param bool read: Read access

            .. versionadded:: 2.0

        :param bool delete: Delete access

            .. versionadded:: 2.0

        :param int access_time: Time till the URL is valid
        :param str blob_name: Name of the blob, this could be a path
        :param bool sas: Set ``True`` to generate SAS key
        :return: Blob URL

        **Example without ``sas``**

        >>> import os
        >>> from azblobexplorer import AzureBlobDownload
        >>> az = AzureBlobDownload('account name', 'account key', 'container name')
        >>> az.generate_url("filename.txt")
        https://containername.blob.core.windows.net/blobname/filename.txt

        **Example with ``upload_to`` and ``sas``**

        >>> import os
        >>> from azblobexplorer import AzureBlobDownload
        >>> az = AzureBlobDownload('account name', 'account key', 'container name')
        >>> az.generate_url("filename.txt", sas=True)
        https://containername.blob.core.windows.net/blobname/filename.txt?se=2019-11-05T16%3A33%3A46Z&sp=w&sv=2019-02-02&sr=b&sig=t%2BpUG2C2FQKp/Hb8SdCsmaZCZxbYXHUedwsquItGx%2BM%3D
        """

        blob = self.container_client.get_blob_client(blob_name)

        if sas:
            sas_token = generate_blob_sas(
                blob.account_name,
                blob.container_name,
                blob.blob_name,
                account_key=blob.credential.account_key,
                permission=BlobSasPermissions(read, add, create, write, delete),
                expiry=datetime.utcnow() + timedelta(hours=access_time)
            )
            return blob.url + '?' + sas_token
        else:
            return blob.url

    def generate_url_mime(self, blob_name: str, mime_type: str, sas: bool = False,
                          read: bool = True, add: bool = False, create: bool = False,
                          write: bool = False, delete: bool = False, access_time: int = 1) -> str:
        """
        Generate's blob URL with MIME type. It can also generate Shared Access Signature (SAS) if ``sas=True``.

        :param bool write: Write access

            .. versionadded:: 2.0

        :param bool create: Create access

            .. versionadded:: 2.0

        :param bool add: Add access

            .. versionadded:: 2.0

        :param bool read: Read access

            .. versionadded:: 2.0

        :param bool delete: Delete access

            .. versionadded:: 2.0

        :param int access_time: Time till the URL is valid
        :param str blob_name: Name of the blob
        :param int access_time: Time till the URL is valid
        :param str mime_type: MIME type of the application
        :param bool sas: Set ``True`` to generate SAS key
        :return: Blob URL

        >>> import os
        >>> from azblobexplorer import AzureBlobDownload
        >>> az = AzureBlobDownload('account name', 'account key', 'container name')
        >>> az.generate_url_mime("filename.zip", sas=True, mime_type="application/zip")
        https://containername.blob.core.windows.net/blobname/filename.zip?se=2019-11-05T16%3A33%3A46Z&sp=w&sv=2019-02-02&sr=b&sig=t%2BpUG2C2FQKp/Hb8SdCsmaZCZxbYXHUedwsquItGx%2BM%3D
        """

        blob = self.container_client.get_blob_client(blob_name)

        if sas:
            sas_token = generate_blob_sas(
                blob.account_name,
                blob.container_name,
                blob.blob_name,
                account_key=blob.credential.account_key,
                permission=BlobSasPermissions(read, add, create, write, delete),
                expiry=datetime.utcnow() + timedelta(hours=access_time),
                content_type=mime_type
            )
            return blob.url + '?' + sas_token
        else:
            return blob.url
