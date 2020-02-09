from .base_model import BaseModel


class JobDetails(BaseModel):
    """
    Job Details
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
    def name(self):
        """
        Returns:
            str
        """
        return self._data.get('request', {}).get('meta', {}).get('name')

    @property
    def tasks_summary(self):
        """
        Returns:
            TasksSummary
        """
        summary_data = self._data.get('tasksSummary')
        if not summary_data:
            return None

        return TasksSummary(**summary_data)


class TasksSummary:  #pylint: disable=redefined-builtin,too-many-instance-attributes
    """
    Tasks Summary
    """

    # pylint: disable=too-many-arguments
    def __init__(self, waiting=0, queued=0, running=0, failed=0, success=0, timeout=0, lost=0, unknown=0, all=0):
        self.queued = queued
        self.running = running
        self.failed = failed
        self.success = success
        self.timeout = timeout
        self.waiting = waiting
        self.lost = lost
        self.unknown = unknown
        self.all = all
