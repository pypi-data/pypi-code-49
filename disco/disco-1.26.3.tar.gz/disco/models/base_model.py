

class BaseModel:
    """
    Base Model
    """

    def __init__(self, data):
        self._data = data or {}

    def __repr__(self):
        if hasattr(self, 'id'):
            return '%s(%s)' % (type(self).__name__, repr(self.id))  # pylint: disable=no-member

        return dict.__repr__(self._data)
