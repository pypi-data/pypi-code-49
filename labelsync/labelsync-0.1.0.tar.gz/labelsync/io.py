from abc import ABC
import json
from labelsync.util import map_to_dictionary

class FileLoader(ABC):
    """Simple storage manager. Operates on filesystem.
    """

    def load(self, path, if_not_exist=''):
        try:
            with open(path) as file:
                return file.read()
        except FileNotFoundError:
            self.save(path, if_not_exist)
            return if_not_exist

    def save(self, path, content):

        with open(path, "w") as file:
            file.write(content + "\n")

class JsonFileLoader(FileLoader):

    def load(self, path, if_not_exist=''):
        return json.loads(super.load())

    def save(self, path, content):
        return super.save(path, json.dumps(content))

class LabelCacheManager():

    def __init__(self, storage_handler, path, cache_id, id_key):
        self.storage_handler = storage_handler
        self.path = path
        self.cache_id = cache_id
        self.id_key = id_key
        self.attached = self._refresh()

    def _refresh(self):
        return map_to_dictionary(json.loads(self.storage_handler.load(self.path + "/" + self.cache_id, '[]')), self.id_key)

    def attach(self, label):
        self.attached[label[self.id_key]] = label

    def detach(self, id):
        del self.attached[id]

    def read(self):
        return list(self.attached.values())

    def persist(self):
        self.storage_handler.save(self.path + "/" + self.cache_id, json.dumps(self.read()))

    def nuke(self):
        self.storage_handler.save(self.path + "/" + self.cache_id, '[]')

