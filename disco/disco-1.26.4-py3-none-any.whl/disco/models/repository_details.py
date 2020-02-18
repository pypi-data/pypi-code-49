from .base_model import BaseModel


class RepositoryDetails(BaseModel):
    """
    Repository Details
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
    def is_active(self):
        """
        Returns:
            str
        """
        return self._data.get('isActive')
