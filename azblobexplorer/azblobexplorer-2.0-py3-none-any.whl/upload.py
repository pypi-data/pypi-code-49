import os
from pathlib import Path

from typing import List

from .base import BlobBase

__all__ = ['AzureBlobUpload']


class AzureBlobUpload(BlobBase):
    """
    Upload a file or a folder.
    """

    def upload_file(self, file_path: str, upload_to: str = None, timeout: int = 10):
        """
        Upload a file to a given blob path.

        :param str upload_to:
            Give the path to upload.
        :param str file_path:
            Absolute path of the file to upload.
        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        >>> from azblobexplorer import AzureBlobUpload
        >>> import os
        >>> az = AzureBlobUpload('account name', 'account key', 'container name')
        >>> here = os.path.abspath(os.path.dirname(__file__)) + os.sep
        >>> az.upload_file(os.path.join(here, 'file1.txt'), 'blob_folder/')
        """

        path = Path(file_path)

        if upload_to is None:
            blob = self.container_client.get_blob_client(path.name)
            with open(file_path, 'rb') as f:
                blob.upload_blob(f, timeout=timeout)
        else:
            blob = self.container_client.get_blob_client(upload_to + path.name)
            with open(file_path, 'rb') as f:
                blob.upload_blob(f, timeout=timeout)

    def upload_files(self, files_path: List[str], timeout: int = 10):
        """
        Upload a list of files.

        :param list(str) files_path:
            A list of files to upload.
        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        >>> import os
        >>> from azblobexplorer import AzureBlobUpload
        >>> az = AzureBlobUpload('account name', 'account key', 'container name')
        >>> here = os.path.abspath(os.path.dirname(__file__)) + os.sep
        >>> path_list = [
        ...     [os.path.join(here, 'file1.txt'), 'folder_1/'],
        ...     [os.path.join(here, 'file2.txt'), 'folder_2/'],
        ...     os.path.join(here, 'file3.txt')
        ... ]
        >>> az.upload_files(path_list)
        """

        for path in files_path:
            if isinstance(path, list):
                self.upload_file(path[0], path[1], timeout=timeout)
            else:
                self.upload_file(path, timeout=timeout)

    def upload_folder(self, folder_path: str, upload_to: str = None, timeout: int = 10):
        """
        Upload a folder to a given blob path.

        :param str upload_to:
            Give the path to upload. Default ``None``.
        :param str folder_path:
            Absolute path of the folder to upload.
        :param int timeout: Request timeout in seconds

            .. versionadded:: 2.0

        **Example without "upload_to"**

        >>> import os
        >>> from azblobexplorer import AzureBlobUpload
        >>> here = os.path.abspath(os.path.dirname(__file__)) + os.sep
        >>> az = AzureBlobUpload('account name', 'account key', 'container name')
        >>> az.upload_folder(os.path.join(here, 'folder_name'))

        **Example with "upload_to"**

        >>> import os
        >>> from azblobexplorer import AzureBlobUpload
        >>> here = os.path.abspath(os.path.dirname(__file__)) + os.sep
        >>> az = AzureBlobUpload('account name', 'account key', 'container name')
        >>> az.upload_folder(os.path.join(here, 'folder_name'), upload_to="my/blob/location/")
        """

        path = Path(folder_path)

        if not path.is_dir():
            raise TypeError("The path should be a folder.")

        root_name = path.name

        for _dir, _, files in os.walk(path):
            for file_name in files:
                rel_dir = os.path.relpath(_dir, path)
                rel_folder_path = os.path.join(root_name, rel_dir) + '/'
                abs_path = os.path.join(_dir, file_name)
                if upload_to is None:
                    self.upload_file(abs_path, rel_folder_path, timeout=timeout)
                else:
                    self.upload_file(abs_path, upload_to + rel_folder_path, timeout=timeout)
