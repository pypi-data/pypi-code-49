class Manager(object):
    """
    Manager class for http operations
    """

    _path = None
    _obj_cls = None

    def __init__(self, fic, parent=None):
        """REST manager constructor.
        Args:
            fic (FattureInCloud): :class:`~fattureincloud.FattureInCloud` connection to use to make requests.
            parent: REST object to which the manager is attached.
        """
        self.fattureincloud = fic

    @property
    def path(self):
        return self._path


class MultipleManager(object):
    """
    Manager class for multiple resource-types
    """
    _resources = None

    def __init__(self, fic):
        self.fattureincloud = fic

    def __getattr__(self, name):
        """
        Retrieve manager for single resource
        """
        if name in self._resources:
            return self._resources[name](self.fattureincloud)


class RESTObject(object):
    """
    Class that represent the object returned from server
    """
    _id_attr = 'id'

    def __init__(self, manager, data=None):
        self._manager = manager
        self._data = data

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        elif hasattr(self._manager, name):
            return getattr(self._manager, name)

        raise AttributeError('%s does not exist' % name)

    def __eq__(self, other):
        if self.get_id() and other.get_id():
            return self.get_id() == other.get_id()
        return super(RESTObject, self) == other

    def __ne__(self, other):
        if self.get_id() and other.get_id():
            return self.get_id() != other.get_id()
        return super(RESTObject, self) != other

    def __hash__(self):
        if not self.get_id():
            return super(RESTObject, self).__hash__()
        return hash(self.get_id())

    def get_id(self):
        """Returns the id of the resource."""
        if self._id_attr is None or not hasattr(self, self._id_attr):
            return None
        return getattr(self, self._id_attr)