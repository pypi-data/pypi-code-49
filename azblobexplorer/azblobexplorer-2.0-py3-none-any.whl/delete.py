from .base import BlobBase
from .exceptions import NoBlobsFound


class AzureBlobDelete(BlobBase):
    """
    Delete file and folder from Azure blob storage.
    """

    def delete_file(self, file_name: str, timeout: int = 10) -> bool:
        """
        Delete a file from Azure Storage Blob.

        :param str file_name:
            Give a file name to delete
        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        :rtype: bool
        :returns: ``True`` if a file is deleted.

        >>> from azblobexplorer import AzureBlobDelete
        >>> az = AzureBlobDelete('account name', 'account key', 'container name')
        >>> az.delete_file('file_name.txt')
        True
        """
        blob = self.container_client.get_blob_client(file_name)

        blob.delete_blob(timeout=timeout)

        return True

    def delete_files(self, file_names: list, timeout: int = 10) -> bool:
        """
        Delete a list of file from Azure Storage Blob.

        :param str file_names:
            Give a list of file names to delete
        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        :rtype: bool
        :returns: ``True`` if files are deleted.


        >>> from azblobexplorer import AzureBlobDelete
        >>> az = AzureBlobDelete('account name', 'account key', 'container name')
        >>> blob_list = [
        ...     'folder_1/file1.txt',
        ...     'file3.txt'
        ... ]
        >>> az.delete_files(blob_list)
        True
        """

        for file in file_names:
            self.delete_file(file, timeout=timeout)

        return True

    def delete_folder(self, blob_folder_name: str, timeout: int = 10) -> bool:
        """
        Delete a folder from Azure Storage Blob.

        :param str blob_folder_name:
            Give a folder name to delete
        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        :rtype: bool
        :returns: ``True`` if a folder is deleted.
        :raises NoBlobsFound: If the blob folder is empty or is not found.

        >>> from azblobexplorer import AzureBlobDelete
        >>> az = AzureBlobDelete('account name', 'account key', 'container name')
        >>> az.delete_folder('temp/')
        True
        """

        blobs = list(self.container_client.list_blobs(blob_folder_name))

        if len(blobs) == 0:
            raise NoBlobsFound(
                "There where 0 blobs found with blob path '{}'".format(blob_folder_name))

        for blob in blobs:
            self.delete_file(blob.name, timeout=timeout)

        return True

    def delete_container(self, timeout: int = 10) -> bool:
        """
        Delete the current container.

        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        :rtype: bool
        :return: Returns ``True`` is the current container is deleted.

        >>> from azblobexplorer import AzureBlobDelete
        >>> az = AzureBlobDelete('account name', 'account key', 'container name')
        >>> az.delete_container()
        True
        """

        self.container_client.delete_container(timeout=10)

        return True
