import zlib
import json


sentinel = object()


class Pressdict(object):
    """Compressed key-value store for JSON-serializable objects."""

    def __init__(self):
        self._d = {}

    def __iter__(self):
        for key in self._d:
            yield key

    def __len__(self):
        return len(self._d)

    def __contains__(self, key):
        return key in self._d

    def __getitem__(self, key):
        return self.decompress(self._d[key])

    def __delitem__(self, key):
        del self._d[key]

    def __setitem__(self, key, value):
        self._d[key] = self.compress(value)

    def clear(self):
        return self._d.clear()

    def get(self, key, default=None):
        if key in self:
            return self[key]
        else:
            return default

    def items(self):
        for key, value in self._d.items():
            yield key, self.decompress(value)

    def keys(self):
        for key in self._d.keys():
            yield key

    def values(self):
        for value in self._d.values():
            yield self.decompress(value)

    def pop(self, key, default=sentinel):
        if default is sentinel:
            return self.decompress(self._d.pop(key))
        else:
            try:
                return self.decompress(self._d.pop(key))
            except KeyError:
                return default

    def compress(self, obj):
        return zlib.compress(json.dumps(obj).encode("utf-8"))

    def decompress(self, string):
        return json.loads(zlib.decompress(string))
