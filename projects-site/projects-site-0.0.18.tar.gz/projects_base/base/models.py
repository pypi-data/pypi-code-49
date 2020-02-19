import shelve
import uuid
import fnmatch
import fcntl
import operator
from projects_base.base import config


class ShelveObject:
    def __init__(self):
        # Key Identifier
        self._id = str(uuid.uuid4())
        # Type identifier, used for retrieving the relevant instances
        self._type = str(type(self))

    def save(self):
        with open(config.get('BASE', 'db_lock'), 'wb') as lock:
            # Lock before db write operation, blocking for now
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
            with shelve.open(config.get('BASE', 'db_path')) as db:
                db[self._id] = {key: self.__dict__[key] for key in
                                self.__dict__.keys()}
            # Unlock after operation
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)

        return self._id

    # Returns a new instance of the calling class with the same _shelve id.
    @classmethod
    def get(cls, instance_id):
        _object = None
        try:
            with shelve.open(config.get('BASE', 'db_path')) as db:
                _object = cls(**db[instance_id])
        except KeyError:
            pass
        return _object

    # Returns a list of instances of the calling class
    @classmethod
    def get_all(cls):
        ids = []
        with shelve.open(config.get('BASE', 'db_path')) as db:
            ids = [key for key in db.keys() if db[key]['_type'] == str(cls)]
        return [cls.get(instance_id) for instance_id in ids]

    @classmethod
    def remove(cls, shelve_id):
        with open(config.get('BASE', 'db_lock'), 'wb') as lock:
            # Lock before db write operation, blocking for now
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
            with shelve.open(config.get('BASE', 'db_path')) as db:
                db.pop(shelve_id)
            # Unlock after operation
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)

    @classmethod
    def clear(cls):
        for instance in cls.get_all():
            cls.remove(instance._id)

    @classmethod
    def get_with_attr(cls, attr, value, collection=None):
        result = []
        if not collection:
            collection = cls.get_all()
        for obj in collection:
            if hasattr(obj, attr):
                obj_attr = getattr(obj, attr)
                if isinstance(obj_attr, type(value)) and \
                        obj_attr == value:
                    result.append(obj)
                else:
                    if isinstance(obj_attr, (list, set, tuple, dict)):
                        if value in obj_attr:
                            result.append(obj)
        return result

    @classmethod
    def get_with_search(cls, key, value, collection=None):
        result = []
        search = "*" + value + "*"
        if not collection:
            collection = cls.get_all()
        for obj in collection:
            if hasattr(obj, key):
                if len(fnmatch.filter([obj.__dict__[key].lower()],
                                      search.lower())) > 0:
                    result.append(obj)
        return result

    @classmethod
    def get_with_first(cls, key, value, collection=None):
        if not collection:
            collection = cls.get_all()
        for obj in collection:
            if hasattr(obj, key):
                if obj.__dict__[key] == value:
                    return obj
        return None

    @classmethod
    def get_top_with(cls, key, collection=None, num=10):
        if not collection:
            collection = cls.get_all()
        distinct_count = {}
        for obj in collection:
            if hasattr(obj, key):
                struct = obj.__dict__[key]
                distinct_count.update(count_distinct_in(struct,
                                                        distinct_count))
        top_num = dict(sorted(distinct_count.items(),
                              key=operator.itemgetter(1),
                              reverse=True)[:num])
        return top_num


def count_distinct_in(struct, current_count=None):
    if not current_count:
        current_count = {}
    if isinstance(struct, str):
        if struct not in current_count:
            current_count[struct] = 1
        else:
            current_count[struct] += 1
    if isinstance(struct, list):
        for i in struct:
            return count_distinct_in(i, current_count)
    if isinstance(struct, dict):
        for k, v in struct.items():
            return count_distinct_in(k, current_count)
    return current_count
