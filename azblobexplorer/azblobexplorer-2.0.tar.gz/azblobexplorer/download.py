import os
from pathlib import Path

from .base import BlobBase
from .exceptions import NoBlobsFound

__all__ = ['AzureBlobDownload']


class AzureBlobDownload(BlobBase):
    """
    Download a file or folder.
    """

    def download_file(self, blob_name: str, download_to: str = None, timeout: int = 10):
        """
        Download a file to a location.

        :param str blob_name:
            Give a blob path with file name.
        :param str download_to:
            Give a local absolute path to download.
        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        :raises OSError: If the directory for ``download_to`` does not exists

        >>> from azblobexplorer import AzureBlobDownload
        >>> az = AzureBlobDownload('account name', 'account key', 'container name')
        >>> az.download_file('some/name/file.txt')
        """

        file_dict = self.read_file(blob_name, timeout=timeout)
        file_name = Path(file_dict['file_name']).name

        if download_to is None:
            write_to = file_name
        else:
            write_to = Path(os.path.join(download_to, file_name))
            write_to.parent.mkdir(parents=True, exist_ok=True)

        with open(write_to, 'wb') as file:
            file.write(file_dict['content'])

    def download_folder(self, blob_folder_name: str, download_to: str = None, timeout: int = 10):
        """
        Download a blob folder.

        :param str blob_folder_name:
            Give a folder name.
        :param str download_to:
            Give a local path to download.
        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        :raises NoBlobsFound: If the blob folder is empty or is not found.
        :raises OSError: If the directory for ``download_to`` does not exists

        >>> from azblobexplorer import AzureBlobDownload
        >>> az = AzureBlobDownload('account name', 'account key', 'container name')
        >>> az.download_folder('some/folder/name')
        """

        blobs = list(self.container_client.list_blobs(blob_folder_name))

        if len(blobs) == 0:
            raise NoBlobsFound(
                "There where 0 blobs found with blob path '{}'".format(blob_folder_name))

        if download_to is None:
            for blob in blobs:
                name = blob['name']
                path = Path(name)
                path.parent.mkdir(parents=True, exist_ok=True)
                _blob = self.read_file(name, timeout=timeout)
                file = open(path, 'wb')
                file.write(_blob['content'])
                file.close()
        else:
            for blob in blobs:
                name = blob['name']
                path = Path(os.path.join(download_to, name))
                path.parent.mkdir(parents=True, exist_ok=True)
                _blob = self.read_file(name, timeout=timeout)
                file = open(path, 'wb')
                file.write(_blob['content'])
                file.close()

    def read_file(self, blob_name: str, timeout: int = 10) -> dict:
        """
        Read a file.

        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        :param str blob_name:
            Give a file name.
        :rtype: dict
        :return:
            Returns a dictionary of name, content,

        >>> from azblobexplorer import AzureBlobDownload
        >>> az = AzureBlobDownload('account name', 'account key', 'container name')
        >>> az.read_file('some/name/file.txt')
        {
            'file_name': 'file.txt',
            'content': byte content,
            'file_size_bytes': size in bytes
        }
        """

        blob_obj = self.container_client.get_blob_client(blob_name)
        blob_properties = blob_obj.get_blob_properties()
        download_blob = blob_obj.download_blob(timeout=timeout)

        return {
            'file_name': blob_properties['name'],
            'content': download_blob.readall(),
            'file_size_bytes': blob_properties['size']
        }
