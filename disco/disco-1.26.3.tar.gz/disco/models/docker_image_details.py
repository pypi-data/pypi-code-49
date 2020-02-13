from .base_model import BaseModel


class DockerImageDetails(BaseModel):
    """
    Docker image details.
    """

    @property
    def id(self):
        """
        Returns:
            str
        """
        return self._data.get('id')

    @property
    def name(self):
        """
        Returns:
            str
        """
        return self._data.get('displayName')

    @property
    def repository_type(self):
        """
        Returns:
            str
        """
        return self._data.get('repositoryType')

    @property
    def path(self):
        """
        Returns:
            str
        """
        return self._data.get('path')

    @property
    def entry_point(self):
        """
        Returns:
            str
        """
        return self._data.get('entryPoint')

    @property
    def is_active(self):
        """
        Returns:
            str
        """
        return self._data.get('isActive')
