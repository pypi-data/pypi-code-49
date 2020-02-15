from collections import defaultdict
from uuid import uuid4


class SessionExchange:
    def __init__(self):
        self._instances = defaultdict(list)

    def last(self, instance_type_name):
        return self._instances.get(instance_type_name, None).pop()

    def new(self, instance_type_name):
        oid = uuid4()
        self._instances[instance_type_name].append(oid)
        return oid

    def clear_all(self):
        for k in self._instances.keys():
            self._instances[k] = []
