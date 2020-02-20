import zlib
import json


sentinel = object()


class Presslist(object):
    """List that stores JSON-serializable objects compressed."""

    def __init__(self):
        self._li = []

    def __iter__(self):
        for elem in self._li:
            yield self.decompress(elem)

    def __len__(self):
        return len(self._li)

    def __contains__(self, elem):
        for li_elem in self._li:
            if self.decompress(li_elem) == elem:
                return True
        return False

    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self.decompress(el) for el in self._li[i]]
        return self.decompress(self._li[i])

    def __delitem__(self, i):
        del self._li[i]

    def __setitem__(self, index, elem):
        if isinstance(index, slice):
            self._li[index] = list(map(self.compress, elem))
            return
        self._li[index] = self.compress(elem)

    def append(self, elem):
        return self._li.append(self.compress(elem))

    def count(self, elem):
        c = 0
        for li_elem in self._li:
            if self.decompress(li_elem) == elem:
                c += 1
        return c

    def extend(self, values):
        return self._li.extend(map(self.compress, values))

    def index(self, elem):
        for i, li_elem in enumerate(self._li):
            if self.decompress(li_elem) == elem:
                return i
        raise ValueError("%s is not in Presslist." % elem)

    def pop(self, i=sentinel):
        if i is not sentinel:
            return self.decompress(self._li.pop(i))
        else:
            return self.decompress(self._li.pop())

    def remove(self, elem):
        index = None
        for i, li_elem in enumerate(self._li):
            if self.decompress(li_elem) == elem:
                index = i
                break
        if index is not None:
            del self._li[index]
        else:
            raise ValueError("%s is not in Presslist." % elem)

    def compress(self, obj):
        return zlib.compress(json.dumps(obj).encode("utf-8"))

    def decompress(self, string):
        return json.loads(zlib.decompress(string))
