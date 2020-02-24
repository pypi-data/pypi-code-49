from abc import ABCMeta, abstractmethod

from .types import FileInfo, FileMetadata, PresignedPostInfo


class BaseStorage(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def from_url(cls, url):  # type: (str) -> BaseStorage
        pass

    @abstractmethod
    def get_file(self, key: str) -> FileInfo:
        """
        Returns:
            FileInfo: information about the file
        """
        pass

    @abstractmethod
    def get_file_meta(self, key: str) -> FileMetadata:
        """
        Returns:
            FileMetadata: file metadata
        """
        pass

    @abstractmethod
    def get_file_content(self, key: str) -> bytes:
        """
        Returns:
            bytes: the file contents
        """
        pass

    @abstractmethod
    def put_file(self, key: str, data: bytes, mime_type: str = None) -> None:
        """Upload a file to the storage

        Args:
            key: where to store the file
            mime_type: mime type of the uploaded file
        """
        pass

    def get_presigned_post(self, key: str, content_type: str) \
            -> PresignedPostInfo:
        """Get presigned-POST information, for backends supporting it

        Returns:
            PresignedPostInfo: URL and form data for the client-side upload

        Raises:
            NotImplementedError: if the backend doesn't support direct uploads
        """
        raise NotImplementedError('Not supported by backend')

    @abstractmethod
    def get_file_url(self, key: str) -> str:
        pass

    def file_exists(self, key: str) -> bool:
        return True

    def get_etag(self, key: str) -> str:
        return None
