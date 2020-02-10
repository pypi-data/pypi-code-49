from .base_model import BaseModel


class Task(BaseModel):
    """
    Task
    """

    @property
    def id(self):
        """
        Returns:
            str
        """
        return self._data.get('id')

    @property
    def status(self):
        """
        Returns:
            str
        """
        return self._data.get('status')

    @property
    def duration(self):
        """
        Returns:
            int
        """
        return self._data.get('stats', {}).get('duration', 0)

    @property
    def input_file_id(self):
        """
        Returns:
            str
        """
        return self._data.get('request', {}).get('inputFile', {}).get('id')

    @property
    def artifact_ids(self):
        """
        Returns:
            list(str)
        """
        return self._data.get('result', {}).get('artifactIds', [])
